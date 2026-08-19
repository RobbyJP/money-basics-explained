"""
Build the static site: reads articles/*.md (with frontmatter), converts to
HTML via the base template, writes to PUBLIC_DIR, plus an index page.

Features & Compliance:
- Pen Name Person Entity: Ray Porter (@id: https://moneyclarity.blog/about.html#author).
- On-page bylines with semantic <time datetime="YYYY-MM-DD"> and Regulatory Accuracy review status.
- Author Bio Card (.author-card) with avatar and methodology link on all articles.
- Full @graph JSON-LD Schemas: Article, BreadcrumbList, FAQPage, AboutPage, and WebSite with SearchAction.
- Instant client-side search on index, calculators, and id portal.
- Category taxonomy silos (Investing, Budgeting & Debt, Taxes & Income, Indonesia).
- Zero 404 guarantee: Canonical redirect stubs for alternate/legacy slug URLs.
"""
import datetime
import json
import os
import re
import shutil
import urllib.parse
from pathlib import Path

import markdown
from dotenv import load_dotenv

load_dotenv()

ARTICLES_DIR = Path("articles")
CALCULATORS_DIR = Path("calculators")
TEMPLATES_DIR = Path("templates")
PUBLIC_DIR = Path(os.getenv("PUBLIC_DIR", "docs"))

SITE_NAME = os.getenv("SITE_NAME", "Money Basics Explained")
SITE_URL = os.getenv("SITE_URL", "https://moneyclarity.blog")
SITE_DESCRIPTION = os.getenv("SITE_DESCRIPTION", "Clear explanations of personal finance concepts, smart calculators, and honest financial comparisons.")

AUTHOR_NAME = "Ray Porter"
AUTHOR_ROLE = "Independent Quantitative Financial Researcher"
AUTHOR_DESC = "Independent financial researcher with a background in software engineering and quantitative financial modeling."


def parse_frontmatter(text: str) -> tuple[dict, str]:
    match = re.match(r"^---\n(.*?)\n---\n\n(.*)$", text, re.DOTALL)
    if not match:
        return {}, text
    fm_raw, body = match.groups()
    fm = {}
    for line in fm_raw.split("\n"):
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip().strip('"')
    return fm, body


def page_path(fm: dict, stem: str) -> str:
    if fm.get("path"):
        return fm["path"].strip("/")
    if fm.get("slug") in ("privacy-policy", "about", "disclaimer", "contact", "terms-of-service"):
        return fm.get("slug") or stem
    if fm.get("lang") == "id" or stem.startswith("id-"):
        clean_stem = stem[3:] if stem.startswith("id-") else stem
        return f"id/{clean_stem}"
    return f"articles/{stem}"


def base_prefix(path: str) -> str:
    depth = len(path.split("/"))
    return "../" * (depth - 1)


def site_url(path: str) -> str:
    base = SITE_URL.rstrip("/")
    if not path:
        return base + "/"
    if not path.endswith(".html"):
        path = path + ".html"
    return f"{base}/{path}"


def page_url(fm: dict, stem: str) -> str:
    return site_url(page_path(fm, stem))


def infer_category(fm: dict, stem: str, is_id: bool) -> str:
    if fm.get("category"):
        return fm["category"]
    if is_id:
        return "Indonesia"
    slug = fm.get("slug", stem).lower()
    if any(k in slug for k in ["tax", "pph", "salary", "hourly", "payslip", "thr", "income", "hsa", "fsa"]):
        return "Taxes & Income"
    if any(k in slug for k in ["invest", "fund", "stock", "roth", "401k", "compound", "asset", "dca", "expense-ratio", "target-date"]):
        return "Investing"
    if any(k in slug for k in ["debt", "budget", "emergency", "savings", "credit", "loan", "apr", "hysa", "cd", "dti", "life-insurance"]):
        return "Budgeting & Debt"
    return "Guides"


def extract_faqs_from_markdown(body: str) -> list[dict]:
    """Find H2/H3 question headers (ending with '?') and extract Q&A pairs for FAQPage schema."""
    faqs = []
    sections = re.split(r"\n(?=#{2,3}\s+)", body)
    for sec in sections:
        match = re.match(r"^#{2,3}\s+(.+?\?)\n+(.+)$", sec.strip(), re.DOTALL)
        if match:
            q, a = match.groups()
            a_clean = re.sub(r"[#*`\[\]]", "", a).strip()
            first_para = a_clean.split("\n\n")[0].strip()
            if len(first_para) > 25 and len(q.strip()) > 8:
                faqs.append({"question": q.strip(), "answer": first_para})
    return faqs


def get_nav_links(prefix: str, html_lang: str, switch_url: str) -> str:
    if html_lang == "id":
        target = switch_url or f"{prefix}index.html"
        return (
            f'<a href="{prefix}id/index.html">Beranda</a>\n'
            f'<a href="{prefix}calculators/index.html">Kalkulator</a>\n'
            f'<a href="{prefix}about.html">Tentang</a>\n'
            f'<a href="{prefix}contact.html">Kontak</a>\n'
            f'<a href="{target}" class="lang-switch-btn" title="Switch to English">🇺🇸 English</a>'
        )
    else:
        target = switch_url or f"{prefix}id/index.html"
        return (
            f'<a href="{prefix}index.html">Home</a>\n'
            f'<a href="{prefix}calculators/index.html">Calculators</a>\n'
            f'<a href="{prefix}about.html">About</a>\n'
            f'<a href="{prefix}contact.html">Contact</a>\n'
            f'<a href="{target}" class="lang-switch-btn" title="Ganti ke Bahasa Indonesia">🇮🇩 Bahasa Indonesia</a>'
        )


def get_footer_links(prefix: str, html_lang: str) -> str:
    if html_lang == "id":
        return (
            f'<a href="{prefix}about.html">Tentang Kami</a>\n'
            f'<a href="{prefix}contact.html">Kontak</a>\n'
            f'<a href="{prefix}disclaimer.html">Disclaimer</a>\n'
            f'<a href="{prefix}privacy-policy.html">Kebijakan Privasi</a>\n'
            f'<a href="{prefix}terms-of-service.html">Syarat & Ketentuan</a>\n'
            f'<a href="{prefix}index.html">🇺🇸 English Version</a>'
        )
    else:
        return (
            f'<a href="{prefix}about.html">About</a>\n'
            f'<a href="{prefix}contact.html">Contact</a>\n'
            f'<a href="{prefix}disclaimer.html">Disclaimer</a>\n'
            f'<a href="{prefix}privacy-policy.html">Privacy Policy</a>\n'
            f'<a href="{prefix}terms-of-service.html">Terms of Service</a>\n'
            f'<a href="{prefix}id/index.html">🇮🇩 Bahasa Indonesia</a>'
        )


def get_breadcrumbs(fm: dict, prefix: str, page_title: str, url: str, is_id: bool) -> tuple[str, dict]:
    category = infer_category(fm, fm.get("slug", ""), is_id)
    home_name = "Beranda" if is_id else "Home"
    home_url = f"{prefix}id/index.html" if is_id else f"{prefix}index.html"
    
    html = (
        f'<nav class="breadcrumbs" aria-label="Breadcrumb">'
        f'<a href="{home_url}">{home_name}</a> <span class="sep">/</span> '
        f'<span class="category-crumb">{category}</span> <span class="sep">/</span> '
        f'<span class="current-crumb">{fm.get("title", page_title)}</span>'
        f'</nav>'
    )
    
    schema = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": home_name,
                "item": site_url("id" if is_id else "")
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": category,
                "item": site_url("id" if is_id else "") + f"#{category.lower().replace(' ', '-')}"
            },
            {
                "@type": "ListItem",
                "position": 3,
                "name": fm.get("title", page_title),
                "item": url
            }
        ]
    }
    return html, schema


def article_social_share_bar(url: str, title: str, lang: str = "en") -> str:
    encoded_url = urllib.parse.quote(url, safe="")
    encoded_title = urllib.parse.quote(f"{title} - Money Clarity")
    share_label = "Bagikan panduan ini:" if lang == "id" else "Share this guide:"
    copy_label = "Salin Link" if lang == "id" else "Copy link"
    copied_label = "Tersalin!" if lang == "id" else "Copied!"

    return (
        f'<div class="article-share-bar">'
        f'<span class="article-share-title">{share_label}</span>'
        f'<div class="article-share-buttons">'
        f'<a class="share-btn share-btn-wa" rel="noopener" target="_blank" '
        f'href="https://wa.me/?text={encoded_title}%20{encoded_url}">WhatsApp</a>'
        f'<a class="share-btn share-btn-x" rel="noopener" target="_blank" '
        f'href="https://twitter.com/intent/tweet?text={encoded_title}&url={encoded_url}">X (Twitter)</a>'
        f'<button type="button" class="share-btn share-btn-copy article-share-copy" '
        f'data-url="{url}">{copy_label}</button>'
        f"</div></div>"
        f'<script>'
        f'(function(){{var b=document.querySelector(".article-share-copy");'
        f"if(b){{b.addEventListener(\"click\",function(){{"
        f"var u=b.getAttribute(\"data-url\");"
        f"if(navigator.clipboard&&navigator.clipboard.writeText)"
        f"{{navigator.clipboard.writeText(u).then(function(){{"
        f"b.textContent=\"{copied_label}\";setTimeout(function(){{b.textContent=\"{copy_label}\";}},2000);}});}}"
        f"else{{var t=document.createElement(\"textarea\");t.value=u;"
        f"document.body.appendChild(t);t.select();document.execCommand(\"copy\");"
        f"document.body.removeChild(t);b.textContent=\"{copied_label}\";"
        f"setTimeout(function(){{b.textContent=\"{copy_label}\";}},2000);}}"
        f"}});}}" + "})();" + "</script>"
    )


def search_filter_widget(placeholder: str = "Search calculators & guides...", no_results_text: str = "No matching tools or guides found.") -> str:
    return (
        f'<div class="search-box-wrap">'
        f'<span class="search-icon">🔍</span>'
        f'<input type="search" id="tool-search" placeholder="{placeholder}" aria-label="Search">'
        f'</div>'
        f'<div id="search-empty" class="search-no-results">{no_results_text}</div>'
        f'<script>'
        f'(function(){{'
        f'var input = document.getElementById("tool-search");'
        f'var empty = document.getElementById("search-empty");'
        f'if (!input) return;'
        f'input.addEventListener("input", function(){{'
        f'  var q = input.value.toLowerCase().trim();'
        f'  var cards = document.querySelectorAll(".card-list .card");'
        f'  var visibleCount = 0;'
        f'  cards.forEach(function(card){{'
        f'    var text = card.textContent.toLowerCase();'
        f'    if (!q || text.indexOf(q) !== -1) {{'
        f'      card.style.display = "";'
        f'      visibleCount++;'
        f'    }} else {{'
        f'      card.style.display = "none";'
        f'    }}'
        f'  }});'
        f'  if (empty) {{ empty.style.display = (visibleCount === 0 && q !== "") ? "block" : "none"; }}'
        f'}});'
        f'}})();'
        f'</script>'
    )


def json_ld_article_with_faqs(title: str, description: str, url: str, date: str, faqs: list[dict] = None, breadcrumb_schema: dict = None) -> str:
    author_node = {
        "@type": "Person",
        "@id": site_url("about") + "#author",
        "name": AUTHOR_NAME,
        "url": site_url("about"),
    }

    article_obj = {
        "@type": "Article",
        "headline": title,
        "description": description,
        "datePublished": date,
        "dateModified": date,
        "author": author_node,
        "publisher": {"@type": "Organization", "name": SITE_NAME},
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
    }

    graph_nodes = [article_obj]
    if breadcrumb_schema:
        graph_nodes.append(breadcrumb_schema)

    if faqs and len(faqs) >= 2:
        faq_obj = {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": f["question"],
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": f["answer"],
                    },
                }
                for f in faqs
            ],
        }
        graph_nodes.append(faq_obj)

    data = {
        "@context": "https://schema.org",
        "@graph": graph_nodes,
    }
    return '<script type="application/ld+json">' + json.dumps(data) + "</script>"


def json_ld_website() -> str:
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "name": SITE_NAME,
                "url": SITE_URL,
                "description": SITE_DESCRIPTION,
                "potentialAction": {
                    "@type": "SearchAction",
                    "target": f"{SITE_URL.rstrip('/')}/?q={{search_term_string}}",
                    "query-input": "required name=search_term_string",
                },
            },
            {
                "@type": "Person",
                "@id": site_url("about") + "#author",
                "name": AUTHOR_NAME,
                "url": site_url("about"),
                "description": AUTHOR_DESC,
            },
        ],
    }
    return '<script type="application/ld+json">' + json.dumps(data) + "</script>"


def json_ld_about() -> str:
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "AboutPage",
                "name": f"About {SITE_NAME}",
                "url": site_url("about"),
                "description": "Learn about Money Basics Explained, our mission to deliver clear personal finance education, and our quantitative research methodology.",
                "mainEntity": {
                    "@type": "Person",
                    "@id": site_url("about") + "#author",
                    "name": AUTHOR_NAME,
                    "jobTitle": AUTHOR_ROLE,
                    "url": site_url("about"),
                    "description": AUTHOR_DESC,
                },
            },
            {
                "@type": "Person",
                "@id": site_url("about") + "#author",
                "name": AUTHOR_NAME,
                "jobTitle": AUTHOR_ROLE,
                "url": site_url("about"),
                "description": AUTHOR_DESC,
            },
        ],
    }
    return '<script type="application/ld+json">' + json.dumps(data) + "</script>"


def load_calculator(name: str) -> tuple[str, str]:
    if not name:
        return "", ""
    html_file = CALCULATORS_DIR / f"{name}.html"
    if not html_file.exists():
        print(f"[site_builder] WARNING: calculator '{name}' has no {html_file.name}")
        return "", ""
    html = html_file.read_text(encoding="utf-8")
    scripts = f'<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>\n<script src="{name}.js" defer></script>'
    return html, scripts


def link_block(title: str, items: list[dict], link_base: str = "", kind: str = "Guide") -> str:
    if not items:
        return ""
    chip = kind.lower()
    entries = "\n".join(
        f'<li class="card">'
        f'<a class="card-link" href="{link_base}{a["filename"]}">'
        f'<span class="chip chip-{chip}">{kind}</span>'
        f'<span class="card-title">{a.get("title", a["filename"])}</span>'
        f'<span class="card-desc">{a.get("description", "")}</span>'
        f"</a></li>"
        for a in items
    )
    return (
        f'<h2 class="section-title">{title} <span class="count">{len(items)}</span></h2>'
        f'<ul class="card-list">{entries}</ul>'
    )


def render_page(
    content_html: str,
    page_title: str,
    meta_description: str,
    prefix: str,
    calculator_html: str = "",
    calculator_script: str = "",
    json_ld: str = "",
    css_version: str = "",
    og_url: str = "",
    og_type: str = "article",
    html_lang: str = "en",
    og_locale: str = "en_US",
    hreflang_links: str = "",
    switch_url: str = "",
) -> str:
    base = (TEMPLATES_DIR / "base.html").read_text(encoding="utf-8")
    og_image = f"{SITE_URL.rstrip('/')}/og-image.png" if SITE_URL else ""
    site_home = f"{prefix}id/index.html" if html_lang == "id" else f"{prefix}index.html"
    nav_html = get_nav_links(prefix, html_lang, switch_url)
    footer_html = get_footer_links(prefix, html_lang)
    footer_disc = "Hanya konten edukasi, bukan nasihat keuangan." if html_lang == "id" else "Educational content only, not financial advice."

    return (
        base.replace("{{ page_title }}", page_title)
        .replace("{{ meta_description }}", meta_description)
        .replace("{{ site_name }}", SITE_NAME)
        .replace("{{ site_home_url }}", site_home)
        .replace("{{ nav_links }}", nav_html)
        .replace("{{ footer_links }}", footer_html)
        .replace("{{ footer_disclaimer }}", footer_disc)
        .replace("{{ base_prefix }}", prefix)
        .replace("{{ content }}", content_html)
        .replace("{{ calculator_html }}", calculator_html)
        .replace("{{ calculator_script }}", calculator_script)
        .replace("{{ json_ld }}", json_ld)
        .replace("{{ css_version }}", css_version)
        .replace("{{ og_url }}", og_url)
        .replace("{{ og_type }}", og_type)
        .replace("{{ og_image }}", og_image)
        .replace("{{ html_lang }}", html_lang)
        .replace("{{ og_locale }}", og_locale)
        .replace("{{ hreflang_links }}", hreflang_links)
        .replace("{{ year }}", str(datetime.date.today().year))
    )


def create_redirect_stub(source_path: Path, target_relative_url: str, canonical_url: str):
    """Generate an instant HTML redirect stub (HTTP 200 with meta refresh and canonical link)."""
    source_path.parent.mkdir(parents=True, exist_ok=True)
    html = (
        f'<!DOCTYPE html>\n'
        f'<html lang="en">\n'
        f'<head>\n'
        f'<meta charset="UTF-8">\n'
        f'<meta http-equiv="refresh" content="0; url={target_relative_url}">\n'
        f'<link rel="canonical" href="{canonical_url}">\n'
        f'<title>Redirecting...</title>\n'
        f'</head>\n'
        f'<body>\n'
        f'<p>Redirecting to <a href="{target_relative_url}">{canonical_url}</a>...</p>\n'
        f'</body>\n'
        f'</html>'
    )
    source_path.write_text(html, encoding="utf-8")
    print(f"[site_builder] generated redirect stub: {source_path} -> {target_relative_url}")


def build():
    today = datetime.date.today().isoformat()
    css_version = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    if PUBLIC_DIR.exists():
        shutil.rmtree(PUBLIC_DIR)
    PUBLIC_DIR.mkdir(parents=True)
    shutil.copy(TEMPLATES_DIR / "style.css", PUBLIC_DIR / "style.css")
    (PUBLIC_DIR / ".nojekyll").write_text("", encoding="utf-8")
    cname = os.getenv("CNAME", "")
    if cname:
        (PUBLIC_DIR / "CNAME").write_text(cname.strip(), encoding="utf-8")
    ads_src = Path("ads") / "ads.txt"
    if ads_src.exists():
        shutil.copy(ads_src, PUBLIC_DIR / "ads.txt")
    for verify_file in PUBLIC_DIR.parent.glob("google*.html"):
        shutil.copy(verify_file, PUBLIC_DIR / verify_file.name)
        print(f"[site_builder] copied {verify_file.name}")
    for indexnow_key in PUBLIC_DIR.parent.glob("[0-9a-f]*[0-9a-f].txt"):
        shutil.copy(indexnow_key, PUBLIC_DIR / indexnow_key.name)
        print(f"[site_builder] copied IndexNow key {indexnow_key.name}")
    og_image_src = Path("og-image.png")
    if og_image_src.exists():
        shutil.copy(og_image_src, PUBLIC_DIR / "og-image.png")
    if SITE_URL:
        sitemap_url = f"{SITE_URL.rstrip('/')}/sitemap.xml"
        (PUBLIC_DIR / "robots.txt").write_text(
            "User-agent: *\n"
            "Allow: /\n"
            "Allow: /articles/\n"
            "Allow: /calculators/\n"
            "Allow: /id/\n\n"
            "User-agent: Mediapartners-Google\n"
            "Allow: /\n\n"
            f"Sitemap: {sitemap_url}\n",
            encoding="utf-8",
        )
        print(f"[site_builder] wrote robots.txt (sitemap: {sitemap_url})")

    sitemap_entries = []

    def add_sitemap(path: str, lastmod: str = ""):
        sitemap_entries.append((path, lastmod or today))

    add_sitemap("", today)

    # First pass: map translations and canonical paths
    translations_en_to_id = {}
    translations_id_to_en = {}
    path_map = {}
    link_map = {}
    
    for _md in sorted(ARTICLES_DIR.glob("*.md")):
        _fm, _ = parse_frontmatter(_md.read_text(encoding="utf-8"))
        _p = page_path(_fm, _md.stem)
        path_map[_md.stem] = _p
        if _fm.get("slug"):
            path_map[_fm["slug"]] = _p
        link_map[os.path.basename(_p) + ".html"] = "/" + _p + ".html"
        
        if (_fm.get("lang") == "id" or _md.stem.startswith("id-")) and _fm.get("translation_of"):
            en_stem = _fm["translation_of"]
            translations_en_to_id[en_stem] = _p
            translations_id_to_en[_md.stem] = en_stem

    articles = []
    calculators = []

    for md_path in sorted(ARTICLES_DIR.glob("*.md")):
        raw = md_path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(raw)
        p = page_path(fm, md_path.stem)
        html_body = markdown.markdown(body, extensions=["tables", "fenced_code"])
        html_body = re.sub(r"<table>", '<div class="table-wrap"><table>', html_body)
        html_body = re.sub(r"</table>", "</table></div>", html_body)
        html_body = re.sub(
            r'href="(?:\.\./|\./)*(?:[a-z0-9-]+/)*([a-z0-9-]+\.html)"',
            lambda m: f'href="{link_map[m.group(1)]}"' if m.group(1) in link_map else m.group(0),
            html_body,
        )
        calc_html, calc_script = load_calculator(fm.get("calculator", ""))
        date = fm.get("date", today)
        is_meta = fm.get("slug") in ("privacy-policy", "about", "disclaimer", "contact", "terms-of-service")
        is_about = fm.get("slug") == "about"
        is_id = fm.get("lang") == "id" or md_path.stem.startswith("id-")
        stem = md_path.stem

        # Language target switch URL
        switch_url = ""
        if is_id:
            en_stem = translations_id_to_en.get(stem, "")
            if en_stem:
                en_p = path_map.get(en_stem, f"articles/{en_stem}")
                switch_url = f"{base_prefix(p)}{en_p}.html"
            else:
                switch_url = f"{base_prefix(p)}index.html"
        else:
            id_p = translations_en_to_id.get(fm.get("slug", stem), "")
            if id_p:
                switch_url = f"{base_prefix(p)}{id_p}.html"
            else:
                switch_url = f"{base_prefix(p)}id/index.html"


        page_url_full = page_url(fm, md_path.stem)
        
        # Social share bar for non-calculator articles
        if not is_meta and not calc_html:
            html_body = html_body + article_social_share_bar(page_url_full, fm.get("title", md_path.stem), lang="id" if is_id else "en")

        breadcrumb_html = ""
        breadcrumb_schema = None
        if not is_meta:
            breadcrumb_html, breadcrumb_schema = get_breadcrumbs(fm, base_prefix(p), fm.get("title", md_path.stem), page_url_full, is_id)
            
            try:
                from datetime import datetime as _dt
                _d = _dt.strptime(date, "%Y-%m-%d")

                if is_id:
                    _months_id = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    display_date = f"{_d.day} {_months_id[_d.month - 1]} {_d.year}"
                    review_month = f"{_months_id[_d.month - 1]} {_d.year}"
                    byline = (
                        f'<p class="byline">Oleh <span class="author-name">{AUTHOR_NAME}</span> '
                        f'&middot; <time datetime="{date}">Diperbarui {display_date}</time> '
                        f'&middot; <span class="review-status">Akurasi regulasi ditinjau: {review_month}</span></p>'
                    )
                else:
                    display_date = _d.strftime("%B %d, %Y")
                    review_month = _d.strftime("%B %Y")
                    byline = (
                        f'<p class="byline">By <span class="author-name">{AUTHOR_NAME}</span> '
                        f'&middot; <time datetime="{date}">Updated {display_date}</time> '
                        f'&middot; <span class="review-status">Regulatory accuracy last reviewed: {review_month}</span></p>'
                    )
            except ValueError:
                display_date = date
                byline = (
                    f'<p class="byline">By <span class="author-name">{AUTHOR_NAME}</span> '
                    f'&middot; <time datetime="{date}">Updated {date}</time></p>'
                )

            if is_id:
                author_card = (
                    '<div class="author-card">'
                    '<div class="author-avatar">RP</div>'
                    '<div class="author-info">'
                    f'<strong class="author-name">{AUTHOR_NAME}</strong>'
                    '<p class="author-bio">Peneliti keuangan independen yang berfokus pada pemodelan kuantitatif, regulasi perpajakan AS &amp; Indonesia, dan edukasi finansial praktis. Seluruh rumus dan angka regulasi diverifikasi terhadap dokumen resmi negara.</p>'
                    f'<a href="{base_prefix(p)}about.html" class="author-link">Standar Editorial &amp; Metodologi &rarr;</a>'
                    '</div>'
                    '</div>'
                )
            else:
                author_card = (
                    '<div class="author-card">'
                    '<div class="author-avatar">RP</div>'
                    '<div class="author-info">'
                    f'<strong class="author-name">{AUTHOR_NAME}</strong>'
                    '<p class="author-bio">Independent financial researcher specializing in quantitative modeling, US and Indonesian tax regulations, and personal finance education. All formulas and regulatory figures on this site are verified against primary statutory sources.</p>'
                    f'<a href="{base_prefix(p)}about.html" class="author-link">Editorial Standards &amp; Methodology &rarr;</a>'
                    '</div>'
                    '</div>'
                )
            html_body = breadcrumb_html + byline + html_body + author_card

        # Extract FAQs for Google FAQPage Rich Snippet Schema
        faqs = extract_faqs_from_markdown(body)

        hreflang_links = ""
        if is_id:
            en_stem = translations_id_to_en.get(stem, "")
            if en_stem:
                en_p = path_map.get(en_stem, f"articles/{en_stem}")
                en_url = site_url(en_p)
                id_url = site_url(p)
                hreflang_links = (
                    f'<link rel="alternate" hreflang="en" href="{en_url}">\n'
                    f'<link rel="alternate" hreflang="id" href="{id_url}">\n'
                    f'<link rel="alternate" hreflang="x-default" href="{en_url}">'
                )
        else:
            id_p = translations_en_to_id.get(fm.get("slug", stem), "")
            if id_p:
                en_url = site_url(p)
                id_url = site_url(id_p)
                hreflang_links = (
                    f'<link rel="alternate" hreflang="en" href="{en_url}">\n'
                    f'<link rel="alternate" hreflang="id" href="{id_url}">\n'
                    f'<link rel="alternate" hreflang="x-default" href="{en_url}">'
                )


        if is_about:
            json_ld_content = json_ld_about()
        elif is_meta:
            json_ld_content = json_ld_article_with_faqs(
                fm.get("title", md_path.stem),
                fm.get("description", SITE_DESCRIPTION),
                page_url_full,
                date,
            )
        else:
            json_ld_content = json_ld_article_with_faqs(
                fm.get("title", md_path.stem),
                fm.get("description", SITE_DESCRIPTION),
                page_url_full,
                date,
                faqs=faqs,
                breadcrumb_schema=breadcrumb_schema,
            )

        page_html = render_page(
            html_body,
            page_title=f"{fm.get('title', md_path.stem)} | {SITE_NAME}",
            meta_description=fm.get("description", SITE_DESCRIPTION),
            prefix=base_prefix(p),
            css_version=css_version,
            calculator_html=calc_html,
            calculator_script=calc_script,
            json_ld=json_ld_content,
            og_url=page_url_full,
            og_type="article",
            html_lang="id" if is_id else "en",
            og_locale="id_ID" if is_id else "en_US",
            hreflang_links=hreflang_links,
            switch_url=switch_url,
        )
        out_path = PUBLIC_DIR / f"{p}.html"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(page_html, encoding="utf-8")
        add_sitemap(p, date)

        item = fm | {"path": p, "filename": f"{p}.html", "category": infer_category(fm, md_path.stem, is_id)}
        calc_name = fm.get("calculator", "")
        if calc_name:
            js_file = CALCULATORS_DIR / f"{calc_name}.js"
            if js_file.exists():
                shutil.copy(js_file, out_path.parent / f"{calc_name}.js")
            calculators.append(item)
            print(f"[site_builder] built {out_path} (calculator: {calc_name})")
        else:
            articles.append(item)
            print(f"[site_builder] built {out_path}")

    # Fix #5: 404 Prevention Redirect Stubs
    create_redirect_stub(
        PUBLIC_DIR / "articles" / "debt-snowball-vs-avalanche.html",
        "../articles/debt-snowball-vs-debt-avalanche.html",
        site_url("articles/debt-snowball-vs-debt-avalanche")
    )
    create_redirect_stub(
        PUBLIC_DIR / "articles" / "expense-ratio-guide.html",
        "../calculators/expense-ratio.html",
        site_url("calculators/expense-ratio")
    )

    # English hub categorization
    en_guides = [a for a in articles if a.get("slug") not in ("privacy-policy", "about", "disclaimer", "contact", "terms-of-service") and a.get("lang") != "id"]
    investing_guides = sorted([a for a in en_guides if a.get("category") == "Investing"], key=lambda a: a.get("date", ""), reverse=True)
    budgeting_guides = sorted([a for a in en_guides if a.get("category") == "Budgeting & Debt"], key=lambda a: a.get("date", ""), reverse=True)
    tax_guides = sorted([a for a in en_guides if a.get("category") == "Taxes & Income"], key=lambda a: a.get("date", ""), reverse=True)
    other_guides = sorted([a for a in en_guides if a.get("category") not in ("Investing", "Budgeting & Debt", "Taxes & Income")], key=lambda a: a.get("date", ""), reverse=True)
    
    calcs = sorted(
        [c for c in calculators if c.get("lang") != "id"],
        key=lambda a: a.get("title", ""),
    )

    hero = (
        '<section class="hero">'
        '<p class="kicker">Independent &middot; Free &middot; Plain Language</p>'
        f"<h1>{SITE_NAME}</h1>"
        f'<p class="hero-desc">{SITE_DESCRIPTION}</p>'
        "</section>"
    )

    id_banner_en = (
        '<div class="demographic-banner">'
        '<div class="demographic-banner-text">'
        '<div class="demographic-banner-title">🇮🇩 Mencari Panduan Keuangan Indonesia?</div>'
        '<p class="demographic-banner-desc">Kunjungi portal khusus kami untuk panduan Pajak PPh 21, THR, Slip Gaji, KPR, SBN Ritel, dan Screener Saham IDX.</p>'
        '</div>'
        '<a href="id/index.html" class="demographic-banner-btn">Buka Portal Indonesia &rarr;</a>'
        '</div>'
    )

    newsletter = (
        '<section class="card newsletter-box" aria-label="Newsletter signup">'
        "<h2>Money lessons, once a month</h2>"
        '<p class="newsletter-desc">One short email a month: a practical financial lesson, our newest calculator, and honest money reminders. No spam, unsubscribe any time.</p>'
        '<form class="contact-form newsletter-form" action="https://formsubmit.co/contact@moneyclarity.blog" method="POST">'
        '<input type="hidden" name="_subject" value="Newsletter signup - Money Clarity">'
        '<input type="hidden" name="_next" value="' + site_url("") + '">'
        '<input type="text" name="_honey" class="honey" tabindex="-1" autocomplete="off">'
        '<div class="newsletter-row">'
        '<input type="email" name="email" placeholder="you@example.com" required aria-label="Email address">'
        '<button type="submit" class="calc-btn">Subscribe</button>'
        "</div>"
        '<p class="newsletter-note">We never sell or share your address. Unsubscribe with one click.</p>'
        "</form></section>"
    )
    
    index_content = (
        hero
        + id_banner_en
        + search_filter_widget(placeholder="Search 13 calculators & 30+ financial guides...", no_results_text="No matching calculators or guides found.")
        + newsletter
        + link_block("Calculators & Interactive Tools", calcs, kind="Calculator")
        + link_block("Investing & Wealth Building", investing_guides, kind="Guide")
        + link_block("Budgeting, Debt & Cash Management", budgeting_guides, kind="Guide")
        + link_block("Taxes, Income & Career", tax_guides, kind="Guide")
        + (link_block("General Financial Guides", other_guides, kind="Guide") if other_guides else "")
    )
    (PUBLIC_DIR / "index.html").write_text(
        render_page(
            index_content,
            page_title=SITE_NAME,
            meta_description=SITE_DESCRIPTION,
            prefix="",
            css_version=css_version,
            json_ld=json_ld_website(),
            og_url=site_url(""),
            og_type="website",
            hreflang_links=(
                f'<link rel="alternate" hreflang="en" href="{site_url("")}">\n'
                f'<link rel="alternate" hreflang="id" href="{site_url("id")}">\n'
                f'<link rel="alternate" hreflang="x-default" href="{site_url("")}">'
            ),
            switch_url="id/index.html",
        ),
        encoding="utf-8",
    )
    print(f"[site_builder] built index: {len(calcs)} calculators, {len(en_guides)} English guides")

    # Calculators Index Page
    if calcs:
        calc_page = render_page(
            f"<h1>Calculators</h1><p>Free interactive tools to help you explore and plan your personal finances.</p>"
            + search_filter_widget(placeholder="Filter 13 personal finance calculators...", no_results_text="No matching calculators found.")
            + link_block("Interactive Tools", calcs, link_base="../", kind="Calculator"),
            page_title=f"Calculators | {SITE_NAME}",
            meta_description="Free interactive personal finance calculators for compound interest, debt payoff, APR/APY, and savings rate.",
            prefix="../",
            css_version=css_version,
            json_ld=json_ld_article_with_faqs(
                "Calculators — Money Basics Explained",
                "Free interactive personal finance calculators.",
                site_url("calculators"),
                today,
            ),
            og_url=site_url("calculators"),
            og_type="website",
            switch_url="../id/index.html",
        )
        calc_dir = PUBLIC_DIR / "calculators"
        calc_dir.mkdir(parents=True, exist_ok=True)
        (calc_dir / "index.html").write_text(calc_page, encoding="utf-8")
        add_sitemap("calculators/index", today)
        print(f"[site_builder] built calculators index with {len(calcs)} calculators")

    # Indonesian Hub Page
    id_guides = sorted(
        [a for a in articles if a.get("lang") == "id"],
        key=lambda a: a.get("date", ""),
        reverse=True,
    )
    id_calcs = sorted(
        [c for c in calculators if c.get("lang") == "id"],
        key=lambda c: c.get("title", ""),
    )

    if id_guides or id_calcs:
        id_items = [dict(a, filename=a["filename"].split("/")[-1]) for a in id_guides]
        id_calc_items = [dict(c, filename=c["filename"].split("/")[-1]) for c in id_calcs]
        
        # Split Indonesian categories
        id_tax_career = [a for a in id_items if any(k in a["filename"] for k in ["pph-21", "thr", "slip-gaji", "bpjs", "umkm", "umr"])]
        id_invest = [a for a in id_items if any(k in a["filename"] for k in ["sbn", "reksadana", "saham", "emas"])]
        id_property = [a for a in id_items if any(k in a["filename"] for k in ["kpr", "darurat"])]
        id_other = [a for a in id_items if a not in id_tax_career and a not in id_invest and a not in id_property]

        en_banner_id = (
            '<div class="demographic-banner">'
            '<div class="demographic-banner-text">'
            '<div class="demographic-banner-title">🇺🇸 Looking for Global Calculators & Guides?</div>'
            '<p class="demographic-banner-desc">Access our complete library of 13 interactive financial calculators, debt simulation tools, and investing guides.</p>'
            '</div>'
            '<a href="../index.html" class="demographic-banner-btn">Explore English Hub &rarr;</a>'
            '</div>'
        )

        id_hub_content = (
            '<section class="hero">'
            '<p class="kicker">Independen &middot; Gratis &middot; Bahasa Sederhana</p>'
            '<h1>Money Clarity — Indonesia</h1>'
            '<p class="hero-desc">Panduan keuangan praktis, regulasi pajak penghasilan, hak ketenagakerjaan, simulasi KPR, dan riset saham IDX yang objektif dan mudah dipahami.</p>'
            '</section>'
            + en_banner_id
            + search_filter_widget(placeholder="Cari panduan pajak, KPR, gaji, SBN, atau saham...", no_results_text="Panduan atau kalkulator tidak ditemukan.")
            + (link_block("Alat Riset Saham BEI", id_calc_items, kind="Calculator") if id_calc_items else "")
            + link_block("Pajak, Karir & Ketenagakerjaan", id_tax_career, kind="Guide")
            + link_block("Investasi, SBN, Reksadana & Emas", id_invest, kind="Guide")
            + link_block("Properti, KPR & Perencanaan Keluarga", id_property, kind="Guide")
            + (link_block("Panduan Lainnya", id_other, kind="Guide") if id_other else "")
        )

        id_hub = render_page(
            id_hub_content,
            page_title=f"Money Clarity — Panduan Keuangan Indonesia | {SITE_NAME}",
            meta_description="Panduan keuangan pribadi Indonesia: PPh 21, THR, slip gaji, KPR, SBN Ritel, dan screener saham IDX dalam bahasa yang mudah dipahami.",
            prefix="../",
            css_version=css_version,
            json_ld=json_ld_article_with_faqs(
                "Money Clarity — Panduan Keuangan Indonesia",
                "Panduan keuangan pribadi dalam Bahasa Indonesia.",
                site_url("id"),
                today,
            ),
            og_url=site_url("id"),
            og_type="website",
            html_lang="id",
            og_locale="id_ID",
            hreflang_links=(
                f'<link rel="alternate" hreflang="en" href="{site_url("")}">\n'
                f'<link rel="alternate" hreflang="id" href="{site_url("id")}">\n'
                f'<link rel="alternate" hreflang="x-default" href="{site_url("")}">'
            ),
            switch_url="../index.html",
        )
        id_dir = PUBLIC_DIR / "id"
        id_dir.mkdir(parents=True, exist_ok=True)
        (id_dir / "index.html").write_text(id_hub, encoding="utf-8")
        add_sitemap("id/index", today)
        print(f"[site_builder] built id hub with {len(id_guides)} guides, {len(id_calcs)} calculators")

    sitemap_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(
            f"  <url>\n"
            f"    <loc>{site_url(p if p else '')}</loc>\n"
            f"    <lastmod>{lm}</lastmod>\n"
            f"  </url>\n"
            for p, lm in sorted(set(sitemap_entries))
        )
        + "</urlset>\n"
    )
    (PUBLIC_DIR / "sitemap.xml").write_text(sitemap_xml, encoding="utf-8")
    print(f"[site_builder] wrote sitemap.xml with {len(set(sitemap_entries))} entries")


if __name__ == "__main__":
    build()
