"""
Build the static site: reads articles/*.md (with frontmatter), converts to
HTML via the base template, writes to PUBLIC_DIR, plus an index page.

Frontmatter extras:
  path:        optional URL path (without .html), e.g. "calculators/compound-interest".
               Defaults to slug or filename. Enables subdirectory pages.
  calculator:  optional name of a calculator in calculators/<name>.html + .js.
               The HTML is injected above the article body and the JS is copied
               next to the built page (for real, client-side interactivity).
"""
import os
import re
import shutil
from pathlib import Path

import markdown
from dotenv import load_dotenv

load_dotenv()

ARTICLES_DIR = Path("articles")
CALCULATORS_DIR = Path("calculators")
TEMPLATES_DIR = Path("templates")
PUBLIC_DIR = Path(os.getenv("PUBLIC_DIR", "docs"))

SITE_NAME = os.getenv("SITE_NAME", "Money Basics Explained")
SITE_URL = os.getenv("SITE_URL", "")
SITE_DESCRIPTION = os.getenv("SITE_DESCRIPTION", "")


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
    return (fm.get("path") or fm.get("slug") or stem).strip("/")


def base_prefix(path: str) -> str:
    depth = len(path.split("/"))
    return "../" * (depth - 1)


def render_page(
    content_html: str,
    page_title: str,
    meta_description: str,
    prefix: str,
    calculator_html: str = "",
    calculator_script: str = "",
    json_ld: str = "",
) -> str:
    base = (TEMPLATES_DIR / "base.html").read_text(encoding="utf-8")
    import datetime

    return (
        base.replace("{{ page_title }}", page_title)
        .replace("{{ meta_description }}", meta_description)
        .replace("{{ site_name }}", SITE_NAME)
        .replace("{{ base_prefix }}", prefix)
        .replace("{{ content }}", content_html)
        .replace("{{ calculator_html }}", calculator_html)
        .replace("{{ calculator_script }}", calculator_script)
        .replace("{{ json_ld }}", json_ld)
        .replace("{{ year }}", str(datetime.date.today().year))
    )


def json_ld_article(title: str, description: str, url: str, date: str) -> str:
    import json

    data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": description,
        "datePublished": date,
        "dateModified": date,
        "author": {"@type": "Organization", "name": "Money Clarity Editorial Team"},
        "publisher": {"@type": "Organization", "name": SITE_NAME},
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
    }
    return '<script type="application/ld+json">' + json.dumps(data) + "</script>"


def json_ld_website() -> str:
    import json

    data = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": SITE_NAME,
        "url": SITE_URL,
        "description": SITE_DESCRIPTION,
    }
    return '<script type="application/ld+json">' + json.dumps(data) + "</script>"


def site_url(path: str) -> str:
    base = SITE_URL.rstrip("/")
    if not path:
        return base + "/"
    if not path.endswith(".html"):
        path = path + ".html"
    return f"{base}/{path}"


def page_url(fm: dict, stem: str) -> str:
    return site_url(page_path(fm, stem))


def load_calculator(name: str) -> tuple[str, str]:
    """Return (injected HTML, script tags) for a calculator asset pair."""
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


def build():
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
    if SITE_URL:
        sitemap_url = f"{SITE_URL.rstrip('/')}/sitemap.xml"
        (PUBLIC_DIR / "robots.txt").write_text(
            "User-agent: *\n"
            "Allow: /\n\n"
            "User-agent: Mediapartners-Google\n"
            "Allow: /\n\n"
            f"Sitemap: {sitemap_url}\n",
            encoding="utf-8",
        )
        print(f"[site_builder] wrote robots.txt (sitemap: {sitemap_url})")

    sitemap_entries = []
    import datetime

    today = datetime.date.today().isoformat()

    def add_sitemap(path: str, lastmod: str = ""):
        sitemap_entries.append((path, lastmod or today))

    add_sitemap("", today)

    articles = []
    calculators = []
    for md_path in sorted(ARTICLES_DIR.glob("*.md")):
        raw = md_path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(raw)
        p = page_path(fm, md_path.stem)
        html_body = markdown.markdown(body, extensions=["tables", "fenced_code"])
        html_body = re.sub(r"<table>", '<div class="table-wrap"><table>', html_body)
        html_body = re.sub(r"</table>", "</table></div>", html_body)
        calc_html, calc_script = load_calculator(fm.get("calculator", ""))
        date = fm.get("date", today)
        is_meta = fm.get("slug") in ("privacy-policy", "about", "disclaimer", "contact")
        if not is_meta:
            byline = (
                f'<p class="byline">By the Money Clarity Editorial Team '
                f"&middot; Updated {date}</p>"
            )
            html_body = byline + html_body
        page_html = render_page(
            html_body,
            page_title=f"{fm.get('title', md_path.stem)} | {SITE_NAME}",
            meta_description=fm.get("description", SITE_DESCRIPTION),
            prefix=base_prefix(p),
            calculator_html=calc_html,
            calculator_script=calc_script,
            json_ld=json_ld_article(
                fm.get("title", md_path.stem),
                fm.get("description", SITE_DESCRIPTION),
                page_url(fm, md_path.stem),
                date,
            ),
        )
        out_path = PUBLIC_DIR / f"{p}.html"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(page_html, encoding="utf-8")
        add_sitemap(p, date)

        item = fm | {"path": p, "filename": f"{p}.html"}
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

    guides = sorted(
        [a for a in articles if a.get("slug") not in ("privacy-policy", "about", "disclaimer", "contact")],
        key=lambda a: a.get("date", ""),
        reverse=True,
    )
    calcs = sorted(calculators, key=lambda a: a.get("title", ""))

    hero = (
        '<section class="hero">'
        '<p class="kicker">Independent &middot; Free &middot; Plain language</p>'
        f"<h1>{SITE_NAME}</h1>"
        f'<p class="hero-desc">{SITE_DESCRIPTION}</p>'
        "</section>"
    )
    index_content = (
        hero
        + link_block("Calculators", calcs, kind="Calculator")
        + link_block("Guides", guides, kind="Guide")
    )
    (PUBLIC_DIR / "index.html").write_text(
        render_page(
            index_content,
            page_title=SITE_NAME,
            meta_description=SITE_DESCRIPTION,
            prefix="",
            json_ld=json_ld_website(),
        ),
        encoding="utf-8",
    )
    print(f"[site_builder] built index: {len(calcs)} calculators, {len(guides)} guides")

    if calcs:
        calc_items = [dict(a, filename=a["filename"].split("/")[-1]) for a in calcs]
        calc_page = render_page(
            f"<h1>Calculators</h1><p>Free interactive tools to help you explore your money.</p>"
            + link_block("Tools", calc_items, kind="Calculator"),
            page_title=f"Calculators | {SITE_NAME}",
            meta_description="Free interactive personal finance calculators.",
            prefix="../",
            json_ld=json_ld_article(
                "Calculators — Money Basics Explained",
                "Free interactive personal finance calculators.",
                site_url("calculators"),
                today,
            ),
        )
        calc_dir = PUBLIC_DIR / "calculators"
        calc_dir.mkdir(parents=True, exist_ok=True)
        (calc_dir / "index.html").write_text(calc_page, encoding="utf-8")
        add_sitemap("calculators/index", today)
        print(f"[site_builder] built calculators index with {len(calcs)} calculators")

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
