"""
Generate SEO articles from keywords.csv using the Anthropic API.

Deliberately prompts for EDUCATIONAL / COMPARISON framing, not
prescriptive financial advice - see README for why. Every article gets
a disclaimer block appended automatically (do not rely on the model to
always include it - it's added programmatically as a safety net).
"""
import argparse
import csv
import os
import re
import time
from pathlib import Path

from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

KEYWORDS_FILE = "keywords.csv"
ARTICLES_DIR = Path("articles")
ARTICLES_DIR.mkdir(exist_ok=True)

DISCLAIMER = (
    "\n\n---\n\n*This article is for general educational purposes only "
    "and is not personalized financial advice. Consider consulting a "
    "licensed financial advisor for guidance specific to your situation.*\n"
)

SYSTEM_PROMPT = """You are writing educational content for a personal \
finance website. Your job is to explain concepts clearly and compare \
options honestly - NOT to tell readers what they personally should do \
with their money. Avoid phrases like "you should" - prefer "one option \
is" or "this approach tends to work well for people who...". Be concrete \
and specific (use realistic example numbers), avoid vague filler, and \
write at a level accessible to someone with no finance background. \
Do not fabricate specific statistics, rates, or figures - if a number \
matters, describe it in general/relative terms instead (e.g. "typically \
higher than" rather than a specific invented percentage). Never use \
LaTeX or math markup (no \frac, \text, $$...$$, \times, etc.) - write any \
formulas as plain text using normal symbols like x, /, +, = (e.g. \
"THR Amount = (Months of Service / 12) x One Month's Wages")."""


def load_keywords():
    with open(KEYWORDS_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows


def save_keywords(rows):
    fieldnames = ["keyword", "intent", "priority", "used"]
    with open(KEYWORDS_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


_LATEX_REPLACEMENTS = [
    (re.compile(r"\\times"), "x"),
    (re.compile(r"\\div|\\divide"), "/"),
    (re.compile(r"\\text\{([^}]*)\}"), r"\1"),
    (re.compile(r"\\frac\{([^}]*)\}\{([^}]*)\}"), r"(\1 / \2)"),
    (re.compile(r"\\left|\\right|\\cdot|\\approx|\\sum|\\sqrt|\\%"), ""),
    (re.compile(r"\\\$"), "$"),
    (re.compile(r"\\([a-zA-Z]+)"), ""),
    (re.compile(r"[{}]"), ""),
]


def _strip_latex(text: str) -> str:
    def replace_block(m):
        inner = m.group(1) or m.group(2) or ""
        for pat, repl in _LATEX_REPLACEMENTS:
            inner = pat.sub(repl, inner)
        inner = inner.strip()
        inner = re.sub(r"\(\s*\(", "(", inner)
        inner = re.sub(r"\)\s*\)", ")", inner)
        return inner.strip()

    text = re.sub(r"\$\$(.+?)\$\$", replace_block, text, flags=re.DOTALL)
    text = re.sub(r"\\\(|\\\)", "", text)
    return text


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text[:80]


def generate_article(client, keyword: str, intent: str) -> dict:
    user_prompt = f"""Write an article for the keyword: "{keyword}"
Content intent: {intent}

Structure:
1. A clear H1 title (as markdown # heading) - naturally include the keyword
2. A 1-2 sentence meta description (I'll extract this separately, put it \
right after the title, prefixed with "META: ")
3. Article body in markdown with H2/H3 subheadings, 600-900 words
4. If intent is "comparison", include a simple markdown table comparing \
the options

Do not include any disclaimer - that will be added automatically."""

    text = _generate_with_retry(client, user_prompt).text

    lines = text.split("\n")
    title = ""
    meta_description = ""
    body_lines = []
    for line in lines:
        if line.startswith("# ") and not title:
            title = line[2:].strip()
            continue
        if line.startswith("META:") and not meta_description:
            meta_description = line[5:].strip()
            continue
        body_lines.append(line)

    body = "\n".join(body_lines).strip()
    while body.startswith("---"):
        body = body[3:].lstrip("\n")
    body = _strip_latex(body)
    body = body.strip() + DISCLAIMER

    return {
        "title": title or keyword.title(),
        "meta_description": meta_description or f"A clear explanation of {keyword}.",
        "body": body,
        "slug": slugify(keyword),
        "keyword": keyword,
    }


def _retry_delay(exc) -> float:
    import re as _re
    hint = getattr(exc, "message", "") or ""
    m = _re.search(r"retry in ([0-9.]+)s", hint, _re.IGNORECASE)
    if m:
        return max(float(m.group(1)), 5.0)
    for detail in getattr(exc, "details", None) or []:
        delay = detail.get("retryDelay", "")
        m = _re.search(r"([0-9.]+)s", delay)
        if m:
            return max(float(m.group(1)), 5.0)
    return 0.0


def _generate_with_retry(client, user_prompt: str, max_retries: int = 5):
    model = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")
    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        max_output_tokens=8000,
    )
    for attempt in range(1, max_retries + 1):
        try:
            return client.models.generate_content(
                model=model,
                contents=user_prompt,
                config=config,
            )
        except Exception as exc:
            if getattr(exc, "code", None) in (400, 401, 403, 404):
                raise
            wait = _retry_delay(exc)
            if not wait:
                wait = 45.0
            print(
                f"[content_gen] API error (attempt {attempt}/{max_retries}): "
                f"{type(exc).__name__} code={getattr(exc, 'code', '?')}; retrying in {wait:.0f}s"
            )
            time.sleep(wait)
    raise RuntimeError(f"gave up generating after {max_retries} retries")


def write_article_file(article: dict):
    frontmatter = (
        "---\n"
        f"title: \"{article['title']}\"\n"
        f"description: \"{article['meta_description']}\"\n"
        f"slug: \"{article['slug']}\"\n"
        f"keyword: \"{article['keyword']}\"\n"
        f"date: \"{time.strftime('%Y-%m-%d')}\"\n"
        "---\n\n"
    )
    path = ARTICLES_DIR / f"{article['slug']}.md"
    path.write_text(frontmatter + article["body"], encoding="utf-8")
    print(f"[content_gen] wrote {path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=1, help="Number of articles to generate")
    args = parser.parse_args()

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit("GEMINI_API_KEY not set in .env")

    client = genai.Client(api_key=api_key)
    rows = load_keywords()

    # ensure 'used' column exists
    for r in rows:
        r.setdefault("used", "")

    unused = [r for r in rows if r.get("used") != "yes"]
    unused.sort(key=lambda r: {"high": 0, "medium": 1, "low": 2}.get(r.get("priority", "medium"), 1))

    if not unused:
        print("[content_gen] no unused keywords left - add more to keywords.csv")
        return

    to_generate = unused[: args.count]
    for row in to_generate:
        print(f"[content_gen] generating: {row['keyword']}")
        article = generate_article(client, row["keyword"], row.get("intent", "educational"))
        write_article_file(article)
        row["used"] = "yes"
        save_keywords(rows)


if __name__ == "__main__":
    main()
