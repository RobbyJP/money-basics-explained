"""
Build the static site: reads articles/*.md (with frontmatter), converts to
HTML via the base template, writes to public/, plus an index page listing
all articles.
"""
import os
import re
import shutil
from pathlib import Path

import markdown
from dotenv import load_dotenv

load_dotenv()

ARTICLES_DIR = Path("articles")
TEMPLATES_DIR = Path("templates")
PUBLIC_DIR = Path(os.getenv("PUBLIC_DIR", "public"))

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


def render_page(content_html: str, page_title: str, meta_description: str) -> str:
    base = (TEMPLATES_DIR / "base.html").read_text(encoding="utf-8")
    import datetime

    return (
        base.replace("{{ page_title }}", page_title)
        .replace("{{ meta_description }}", meta_description)
        .replace("{{ site_name }}", SITE_NAME)
        .replace("{{ content }}", content_html)
        .replace("{{ year }}", str(datetime.date.today().year))
    )


def build():
    if PUBLIC_DIR.exists():
        shutil.rmtree(PUBLIC_DIR)
    PUBLIC_DIR.mkdir(parents=True)
    shutil.copy(TEMPLATES_DIR / "style.css", PUBLIC_DIR / "style.css")
    (PUBLIC_DIR / ".nojekyll").write_text("", encoding="utf-8")

    articles = []
    for md_path in sorted(ARTICLES_DIR.glob("*.md")):
        raw = md_path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(raw)
        html_body = markdown.markdown(body, extensions=["tables", "fenced_code"])
        page_html = render_page(
            html_body,
            page_title=f"{fm.get('title', md_path.stem)} | {SITE_NAME}",
            meta_description=fm.get("description", SITE_DESCRIPTION),
        )
        out_path = PUBLIC_DIR / f"{fm.get('slug', md_path.stem)}.html"
        out_path.write_text(page_html, encoding="utf-8")
        articles.append(fm | {"filename": out_path.name})
        print(f"[site_builder] built {out_path}")

    # Build index page
    list_items = "\n".join(
        f'<a href="/{a["filename"]}">{a.get("title", a["filename"])}</a>'
        f'<p>{a.get("description", "")}</p>'
        for a in sorted(articles, key=lambda a: a.get("date", ""), reverse=True)
    )
    index_content = f'<h1>{SITE_NAME}</h1><p>{SITE_DESCRIPTION}</p><div class="article-list">{list_items}</div>'
    index_html = render_page(index_content, page_title=SITE_NAME, meta_description=SITE_DESCRIPTION)
    (PUBLIC_DIR / "index.html").write_text(index_html, encoding="utf-8")
    print(f"[site_builder] built index with {len(articles)} articles")


if __name__ == "__main__":
    build()
