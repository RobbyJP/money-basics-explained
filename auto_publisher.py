"""
Dynamic Weekly AI Content Publisher for Money Clarity.

Robustness & Error-Handling Features:
1. Multi-tiered Topic Discovery (Google Suggest + Gemini Niche Fallback).
2. Semantic AI Deduplication (Strict overlap checks against existing articles).
3. API Quota & Rate-Limit Shield (Exponential backoff & graceful degradation).
4. Content Quality Validation (Word count, structural headers, frontmatter sanity).
5. Safe Site Rebuild & Sitemap Updates.
"""
import argparse
import datetime
import json
import os
import re
import time
import urllib.parse
from pathlib import Path

import requests
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import APIError

import site_builder

load_dotenv()

ARTICLES_DIR = Path("articles")
ARTICLES_DIR.mkdir(exist_ok=True)

DISCLAIMER = (
    "\n\n---\n\n*This article is for general educational purposes only "
    "and is not personalized financial advice. Consider consulting a "
    "licensed financial advisor for guidance specific to your situation.*\n"
)

DISCLAIMER_ID = (
    "\n\n---\n\n*Artikel ini disusun hanya untuk tujuan edukasi umum "
    "dan bukan merupakan nasihat keuangan atau investasi pribadi. Pertimbangkan "
    "untuk berkonsultasi dengan penasihat keuangan berlisensi untuk situasi spesifik Anda.*\n"
)

SEED_EN_TOPICS = [
    "personal finance basics",
    "emergency fund high yield savings",
    "index fund vs etf investing",
    "debt snowball vs debt avalanche payoff",
    "budgeting rules for beginners",
    "how to calculate net worth",
    "inflation purchasing power savings",
    "credit score factors explained",
    "diversification for beginner investors",
    "dollar cost averaging vs lump sum",
    "certificate of deposit vs money market",
    "understanding 401k match and roth",
]

SEED_ID_TOPICS = [
    "simulasi perhitungan pph 21 karyawan",
    "cara hitung thr karyawan kontrak tetap",
    "tips kpr rumah pertama bunga fixed floating",
    "cara membaca slip gaji bpjs ketenagakerjaan",
    "investasi reksadana pasar uang vs obligasi",
    "screener saham dividen yield ihsg",
    "cara mengelola gaji umr menabung investasi",
    "dana darurat ideal keluarga muda indonesia",
    "pajak penghasilan atas dividen dan saham bei",
    "keuntungan dan risiko deposito bank digital",
]


def call_gemini_with_retry(client: genai.Client, model: str, prompt: str, config: types.GenerateContentConfig, max_retries: int = 3):
    """Execute Gemini API calls with exponential backoff for rate limits."""
    for attempt in range(1, max_retries + 1):
        try:
            return client.models.generate_content(
                model=model,
                contents=prompt,
                config=config,
            )
        except Exception as e:
            err_msg = str(e).lower()
            is_rate_limit = "429" in err_msg or "quota" in err_msg or "resource_exhausted" in err_msg
            if is_rate_limit and attempt < max_retries:
                wait_time = attempt * 8
                print(f"[auto_publisher] Rate limit encountered. Retrying in {wait_time}s (Attempt {attempt}/{max_retries})...")
                time.sleep(wait_time)
            else:
                print(f"[auto_publisher] API call failed on attempt {attempt}: {e}")
                if attempt == max_retries:
                    raise e
    return None


def fetch_google_suggestions(query: str, lang: str = "en") -> list[str]:
    """Fetch real-time search queries from Google Suggest API."""
    try:
        url = f"http://suggestqueries.google.com/complete/search?client=chrome&hl={lang}&q={urllib.parse.quote(query)}"
        resp = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        if resp.status_code == 200:
            data = resp.json()
            if len(data) > 1 and isinstance(data[1], list):
                return [s.strip() for s in data[1] if isinstance(s, str) and len(s.split()) >= 3]
    except Exception as e:
        print(f"[auto_publisher] Warning: Google Suggest query failed for '{query}': {e}")
    return []


def get_existing_articles_summary() -> list[dict]:
    """Gather all existing article titles, descriptions, and slugs to prevent duplicates."""
    existing = []
    for md_path in ARTICLES_DIR.glob("*.md"):
        fm, body = site_builder.parse_frontmatter(md_path.read_text(encoding="utf-8"))
        if fm.get("slug") not in ("privacy-policy", "about", "disclaimer", "contact", "terms-of-service"):
            existing.append({
                "slug": fm.get("slug", md_path.stem),
                "title": fm.get("title", md_path.stem),
                "description": fm.get("description", ""),
                "lang": fm.get("lang", "en"),
                "file": md_path.name,
            })
    return existing


def semantic_dedup_check(client: genai.Client, model: str, candidate_topic: str, lang: str, existing: list[dict]) -> tuple[bool, str]:
    """Use Gemini to semantically verify if a topic is genuinely new or duplicates existing content."""
    existing_titles = [f"- [{item.get('lang', 'en').upper()}] {item['title']}: {item['description']}" for item in existing]
    titles_block = "\n".join(existing_titles)

    prompt = f"""You are an editorial director for a personal finance reference site.
We have an existing catalog of published articles:

{titles_block}

We are evaluating a new candidate topic:
Candidate Topic: "{candidate_topic}" (Target Language: {lang})

Question: Does this candidate topic cover the EXACT SAME concept or substantially overlap in primary intent with any existing article listed above?
Note: Related topics with different specific focuses are ACCEPTABLE. Identical concepts framed slightly differently are DUPLICATES.

Respond with ONLY valid JSON with this exact schema:
{{
  "is_duplicate": true or false,
  "reason": "Brief 1-sentence explanation of why it is unique or what existing article it duplicates",
  "suggested_title": "A compelling, clear article headline in the target language (no hype, no exclamation marks)",
  "suggested_slug": "url-friendly-slug-in-kebab-case",
  "meta_description": "A 1-2 sentence compelling summary (under 160 characters)"
}}"""

    try:
        response = call_gemini_with_retry(
            client=client,
            model=model,
            prompt=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.2,
            ),
        )
        if not response or not response.text:
            return False, {}
        data = json.loads(response.text.strip())
        is_dup = bool(data.get("is_duplicate", False))
        return not is_dup, data
    except Exception as e:
        print(f"[auto_publisher] Semantic dedup evaluation error: {e}")
        return False, {}


def generate_niche_fallback_topics(client: genai.Client, model: str, lang: str, existing: list[dict]) -> list[str]:
    """Fallback generator when search suggestions are exhausted or all duplicates."""
    existing_titles = [f"- {item['title']}" for item in existing if item.get("lang") == lang]
    titles_block = "\n".join(existing_titles)

    prompt = f"""Here are our existing articles in {lang.upper()}:
{titles_block}

Propose 5 FRESH, specific, and unaddressed personal finance questions or niche educational topics that are NOT already covered above.
Target demographic: {'Indonesian personal finance, tax, or property' if lang == 'id' else 'Global / US personal finance, investing, or budgeting'}.
Return ONLY a JSON array of 5 strings (e.g. ["topic 1", "topic 2", ...])."""

    try:
        response = call_gemini_with_retry(
            client=client,
            model=model,
            prompt=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.7,
            ),
        )
        if response and response.text:
            return json.loads(response.text.strip())
    except Exception as e:
        print(f"[auto_publisher] Niche fallback generation error: {e}")
    return []


def validate_article_quality(markdown_text: str) -> tuple[bool, str]:
    """Validate that the generated article meets length, formatting, and structural standards."""
    if not markdown_text or len(markdown_text.strip()) < 800:
        return False, "Content too short (under 800 characters)."
    
    words = len(markdown_text.split())
    if words < 500:
        return False, f"Word count too low ({words} words; minimum required: 500)."
    
    # Must have at least 2 H2 sections
    h2_count = len(re.findall(r"^##\s+", markdown_text, flags=re.MULTILINE))
    if h2_count < 2:
        return False, f"Missing structured subheadings (found {h2_count} '##' sections)."
    
    # Must have frontmatter
    if not (markdown_text.startswith("---") and "\n---\n" in markdown_text):
        return False, "Missing frontmatter delimiters."
    
    return True, "Quality checks passed."


def generate_article_content(client: genai.Client, model: str, topic_info: dict, lang: str) -> str:
    """Generate comprehensive educational article content in Markdown."""
    title = topic_info.get("suggested_title", "")
    description = topic_info.get("meta_description", "")
    slug = topic_info.get("suggested_slug", "")
    today = datetime.date.today().isoformat()

    if lang == "id":
        system_prompt = """Anda adalah penulis edukasi keuangan profesional untuk situs Money Clarity.
Tugas Anda adalah menjelaskan konsep keuangan dengan jelas, objektif, jujur, dan mudah dipahami oleh masyarakat umum.
Aturan Penting:
1. Hindari kalimat menggurui seperti "Anda harus" — gunakan bahasa netral seperti "Pilihan yang umum digunakan adalah" atau "Metode ini efektif bagi orang yang...".
2. Berikan contoh perhitungan konkret dan realistis dalam Rupiah (Rp) menggunakan tabel Markdown standar.
3. JANGAN PERNAH membungkus tabel Markdown di dalam blok kode (```markdown atau ```). Tulis tabel langsung dengan baris pipa (| Kolom | Kolom |).
4. JANGAN PERNAH menggambar diagram dengan karakter kotak ASCII (┌, ─, │, └).
5. Jangan mengarang peraturan resmi — sebutkan dasar aturan jika relevan (misal UU HPP, aturan Depnaker, atau BI/OJK).
6. JANGAN gunakan markup LaTeX (seperti \\frac, $$, \\times) — tulis rumus dengan teks biasa (misal: "Rumus = (A / B) x C").
7. Format artikel menggunakan Markdown terstruktur: H1 judul, H2 subjudul, poin tebal, dan tabel ringkasan/perbandingan."""

        user_prompt = f"""Tulis panduan edukasi keuangan lengkap tentang topik: "{title}".
Ringkasan/Meta Deskripsi: "{description}"

Panduan harus mencakup:
- Penjelasan konsep dasar tanpa jargon membingungkan.
- Contoh angka/perhitungan nyata dalam Rupiah (tabel simulasi).
- Kelebihan, kekurangan, dan pertimbangan praktis.
- Kesalahan umum yang sering terjadi dan cara menghindarinya.
- Tanya Jawab (FAQ) singkat yang sering dicari masyarakat.

Tulis dalam Bahasa Indonesia yang profesional dan mengalir (800-1200 kata). Jangan sertakan disclaimer di akhir karena akan ditambahkan otomatis."""

    else:
        system_prompt = """You are writing educational content for personal finance website Money Clarity.
Your job is to explain concepts clearly and compare options honestly - NOT to tell readers what they personally should do with their money.
Critical Guidelines:
1. Avoid prescriptive phrasing like "you should" - prefer "one common option is" or "this approach tends to work well for people who...".
2. Be concrete and specific: use realistic example numbers and standard Markdown tables.
3. NEVER wrap Markdown tables inside code fences (```markdown or ```) - write tables directly in standard markdown syntax (| Column | Column |).
4. NEVER draw diagrams using ASCII line/box characters (┌, ─, │, └, ▼).
5. Do not fabricate specific statistics or invented rates - explain principles clearly with labeled example figures.
6. NEVER use LaTeX or math markup (no \\frac, $$, \\times) - write formulas as plain text using standard symbols (+, -, x, /, =).
7. Format with clean Markdown: H1 title, clear H2 subheadings, bullet points, and comparative tables."""


        user_prompt = f"""Write a comprehensive educational personal finance guide on the topic: "{title}".
Summary: "{description}"

The guide must include:
- Clear explanation of the concept and why it matters.
- A worked numerical example with a clean Markdown comparison table.
- Practical pros, cons, and trade-offs.
- Common mistakes people make and how to avoid them.
- A concise FAQ section answering 2-3 common practical questions.

Length: 800-1200 words in clear, engaging English. Do not include a closing disclaimer (it is appended automatically)."""

    response = call_gemini_with_retry(
        client=client,
        model=model,
        prompt=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.4,
        ),
    )

    if not response or not response.text:
        raise ValueError("Empty response received from Gemini API.")

    body = response.text.strip()
    # Strip any duplicated frontmatter
    body = re.sub(r"^---.*?---\n+", "", body, flags=re.DOTALL).strip()
    
    frontmatter = (
        f'---\n'
        f'title: "{title}"\n'
        f'description: "{description}"\n'
        f'slug: "{slug}"\n'
        f'keyword: "{title.lower()}"\n'
        f'date: "{today}"\n'
        f'lang: "{lang}"\n'
        f'---\n\n'
    )

    disclaimer = DISCLAIMER_ID if lang == "id" else DISCLAIMER
    full_text = frontmatter + body + disclaimer

    is_valid, reason = validate_article_quality(full_text)
    if not is_valid:
        raise ValueError(f"Generated article failed quality gate: {reason}")

    return full_text


def run_pipeline(dry_run: bool = False, force_lang: str = None) -> bool:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("[auto_publisher] Notice: GEMINI_API_KEY environment variable is not set. Skipping.")
        return False

    model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    client = genai.Client(api_key=api_key)

    existing = get_existing_articles_summary()
    print(f"[auto_publisher] Found {len(existing)} existing articles in catalog.")

    # Catalog balance
    id_count = sum(1 for item in existing if item.get("lang") == "id")
    en_count = sum(1 for item in existing if item.get("lang") != "id")
    print(f"[auto_publisher] Catalog balance: {en_count} English vs {id_count} Indonesian.")

    target_lang = force_lang or ("id" if id_count * 2 < en_count else "en")
    print(f"[auto_publisher] Selected target language for this batch: {target_lang.upper()}")

    seed_list = SEED_ID_TOPICS if target_lang == "id" else SEED_EN_TOPICS

    # 1. Harvest candidates
    candidates = []
    for seed in seed_list:
        suggestions = fetch_google_suggestions(seed, lang=target_lang)
        candidates.extend(suggestions)
    
    candidates.extend(seed_list)
    candidates = list(dict.fromkeys(candidates))
    print(f"[auto_publisher] Harvested {len(candidates)} candidate search queries.")

    # 2. Evaluate candidates against catalog
    approved_topic = None
    try:
        for candidate in candidates:
            is_approved, info = semantic_dedup_check(client, model_name, candidate, target_lang, existing)
            if is_approved and info.get("suggested_title") and info.get("suggested_slug"):
                slug = info["suggested_slug"]
                target_file = ARTICLES_DIR / f"{slug}.md" if target_lang == "en" else ARTICLES_DIR / f"id-{slug}.md"
                if not target_file.exists():
                    approved_topic = info
                    print(f"[auto_publisher] Approved Unique Topic: '{info['suggested_title']}' (Slug: {slug})")
                    print(f"  Reason: {info.get('reason', '')}")
                    break
            else:
                print(f"[auto_publisher] Skipped duplicate/overlapping topic: '{candidate}' -> {info.get('reason', 'Overlap')}")

        # If all search suggestions are duplicates, trigger niche brainstorming fallback
        if not approved_topic:
            print("[auto_publisher] All standard suggestions overlapped. Triggering niche brainstorming fallback...")
            fallback_candidates = generate_niche_fallback_topics(client, model_name, target_lang, existing)
            for candidate in fallback_candidates:
                is_approved, info = semantic_dedup_check(client, model_name, candidate, target_lang, existing)
                if is_approved and info.get("suggested_title") and info.get("suggested_slug"):
                    slug = info["suggested_slug"]
                    target_file = ARTICLES_DIR / f"{slug}.md" if target_lang == "en" else ARTICLES_DIR / f"id-{slug}.md"
                    if not target_file.exists():
                        approved_topic = info
                        print(f"[auto_publisher] Approved Unique Fallback Topic: '{info['suggested_title']}' (Slug: {slug})")
                        break
    except Exception as e:
        print(f"[auto_publisher] Quota limit or connection error during topic evaluation: {e}")
        print("[auto_publisher] Gracefully exiting without modifying repository.")
        return False

    if not approved_topic:
        print("[auto_publisher] Catalog is fully comprehensive! No new unique topics found. Exiting cleanly.")
        return False

    if dry_run:
        print(f"[auto_publisher] [DRY RUN] Would generate article: {approved_topic}")
        return True

    # 3. Generate article with quality validation
    try:
        print(f"[auto_publisher] Generating full guide with {model_name}...")
        full_markdown = generate_article_content(client, model_name, approved_topic, target_lang)
    except Exception as e:
        print(f"[auto_publisher] Generation aborted due to quality or API error: {e}")
        return False

    slug = approved_topic["suggested_slug"]
    filename = f"{slug}.md" if target_lang == "en" else f"id-{slug}.md"
    out_file = ARTICLES_DIR / filename
    out_file.write_text(full_markdown, encoding="utf-8")
    print(f"[auto_publisher] Wrote new article to {out_file}")

    # 4. Rebuild static site
    print("[auto_publisher] Rebuilding static site with site_builder...")
    site_builder.build()
    print("[auto_publisher] Static site rebuilt successfully!")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Money Clarity Automated Weekly Content Publisher")
    parser.add_argument("--dry-run", action="store_true", help="Find unique topic without writing or publishing")
    parser.add_argument("--lang", choices=["en", "id"], default=None, help="Force specific target language")
    args = parser.parse_args()

    success = run_pipeline(dry_run=args.dry_run, force_lang=args.lang)
    if success:
        print("[auto_publisher] Pipeline executed successfully.")
    else:
        print("[auto_publisher] Pipeline completed with no new publish.")
