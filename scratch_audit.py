"""
Comprehensive audit script for all generated HTML files in docs/
"""
import json
import re
from pathlib import Path

DOCS = Path("docs")
html_files = list(DOCS.glob("**/*.html"))

print(f"[Audit] Scanning {len(html_files)} HTML files in docs/...")
errors = []

for hf in html_files:
    rel_path = hf.relative_to(DOCS).as_posix()
    content = hf.read_text(encoding="utf-8")
    
    # Check if redirect stub
    if '<meta http-equiv="refresh"' in content:
        print(f"  [Redirect Stub] {rel_path} -> OK")
        continue

    # 1. Check JSON-LD
    json_match = re.search(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
    if not json_match:
        errors.append(f"{rel_path}: Missing JSON-LD script block")
    else:
        raw_json = json_match.group(1).strip()
        try:
            parsed = json.loads(raw_json)
            if "@graph" in parsed:
                pass
            elif "@type" in parsed:
                pass
            else:
                errors.append(f"{rel_path}: JSON-LD missing @graph or @type")
        except json.JSONDecodeError as e:
            errors.append(f"{rel_path}: Invalid JSON in JSON-LD: {e}")

    # 2. Check for duplicate pre/code blocks consecutively
    pre_blocks = re.findall(r'<pre><code>(.*?)</code></pre>', content, re.DOTALL)
    for i in range(len(pre_blocks) - 1):
        if pre_blocks[i].strip() == pre_blocks[i+1].strip():
            errors.append(f"{rel_path}: Consecutive duplicate pre/code block detected!")

    # 3. Check internal links
    internal_links = re.findall(r'href="([^"#:]+\.html)"', content)
    for link in internal_links:
        if link.startswith("http://") or link.startswith("https://") or link.startswith("mailto:"):
            continue
        if link.startswith("/"):
            target = (DOCS / link.lstrip("/")).resolve()
        else:
            target = (hf.parent / link).resolve()
        if not target.exists():
            errors.append(f"{rel_path}: Broken internal link to {link}")

if errors:
    print(f"\nFOUND {len(errors)} AUDIT ISSUES:")
    for err in errors:
        print(f"  - {err}")
else:
    print("\nSUCCESS: All 60+ HTML files passed with 100% valid JSON-LD, 0 duplicate blocks, and 0 broken internal links!")
