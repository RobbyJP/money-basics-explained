"""
Commit and push the built public/ dir. Assumes this repo is already
connected to GitHub Pages / Cloudflare Pages pointing at PUBLIC_DIR (or a
dedicated branch - adjust GIT_REMOTE_BRANCH in .env if you deploy from a
separate branch like gh-pages instead of committing public/ to main).
"""
import os
import subprocess

from dotenv import load_dotenv

load_dotenv()

BRANCH = os.getenv("GIT_REMOTE_BRANCH", "main")
PUBLIC_DIR = os.getenv("PUBLIC_DIR", "public")


def run(cmd: list[str]):
    print(f"[publish] $ {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
    return result.returncode == 0


def publish():
    run(["git", "add", "articles", PUBLIC_DIR, "keywords.csv"])
    committed = run(["git", "commit", "-m", "Auto-publish: new content"])
    if not committed:
        print("[publish] nothing to commit")
        return
    run(["git", "push", "origin", BRANCH])


if __name__ == "__main__":
    publish()
