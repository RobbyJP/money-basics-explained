"""
URL Integrity & 404 Prevention Validator for Money Clarity.
Checks:
1. All sitemap.xml URLs map to existing HTML files.
2. All internal href links across all HTML files point to existing files.
3. All redirect stubs point to valid existing destinations without broken targets.
"""
import re
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

DOCS_DIR = Path("docs")

def verify_all():
    if not DOCS_DIR.exists():
        print(f"Error: {DOCS_DIR} directory does not exist.")
        sys.exit(1)

    errors = []

    # 1. Check Sitemap
    sitemap_path = DOCS_DIR / "sitemap.xml"
    if not sitemap_path.exists():
        errors.append("sitemap.xml is missing from docs directory.")
    else:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        namespace = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locs = root.findall(".//ns:loc", namespace)
        print(f"[verify] Found {len(locs)} entries in sitemap.xml.")
        for loc in locs:
            url = loc.text.strip()
            # Normalize URL to relative path
            rel = re.sub(r"^https?://[^/]+/?", "", url)
            target = DOCS_DIR / "index.html" if not rel else DOCS_DIR / rel
            if not target.exists():
                errors.append(f"Sitemap entry missing on disk: {url} -> {target}")

    # 2. Check HTML files & internal links
    html_files = list(DOCS_DIR.glob("**/*.html"))
    print(f"[verify] Scanning internal links across {len(html_files)} HTML files...")

    redirect_stubs_count = 0
    regular_pages_count = 0

    for html_path in html_files:
        content = html_path.read_text(encoding="utf-8")
        is_redirect = 'http-equiv="refresh"' in content or 'http-equiv="Refresh"' in content

        if is_redirect:
            redirect_stubs_count += 1
            m = re.search(r'content=["\']\s*\d+\s*;\s*url=([^"\']+)["\']', content, flags=re.IGNORECASE)
            if m:
                target_rel = m.group(1).split("#")[0].split("?")[0]
                target_dest = (html_path.parent / target_rel).resolve()
                if not target_dest.exists():
                    errors.append(f"Broken redirect stub in {html_path.relative_to(DOCS_DIR)}: target not found '{target_rel}'")
        else:
            regular_pages_count += 1

        # Check all href links
        hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
        for href in hrefs:
            if href.startswith(("http://", "https://", "#", "mailto:", "javascript:", "tel:")):
                continue
            clean = href.split("?")[0].split("#")[0]
            if not clean:
                continue
            if clean.startswith("/"):
                target_path = (DOCS_DIR / clean.lstrip("/")).resolve()
            else:
                target_path = (html_path.parent / clean).resolve()
            if not target_path.exists():
                errors.append(f"Broken link in {html_path.relative_to(DOCS_DIR)} -> href='{href}' (destination '{target_path}' not found)")


    print(f"[verify] Verified {regular_pages_count} full pages and {redirect_stubs_count} redirect stubs.")

    if errors:
        print(f"\n[FAIL] Found {len(errors)} URL/Link integrity issues:")
        for err in errors:
            print(f"  [ERROR] {err}")
        return False
    else:
        print(f"\n[PASS] All {len(html_files)} HTML files, sitemaps, and redirects passed integrity checks with 0 errors! [OK]")
        return True

if __name__ == "__main__":
    success = verify_all()
    if not success:
        sys.exit(1)
