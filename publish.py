"""
Commit and push the built public/ dir. Assumes this repo is already
connected to GitHub Pages / Cloudflare Pages pointing at PUBLIC_DIR (or a
dedicated branch - adjust GIT_REMOTE_BRANCH in .env if you deploy from a
separate branch like gh-pages instead of committing public/ to main).
"""
import os
import subprocess
import sys

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
    result = subprocess.run(["git", "commit", "-m", "Auto-publish: new content"], capture_output=True, text=True)
    if result.returncode == 0:
        return run(["git", "push", "origin", BRANCH])
    output = result.stdout + result.stderr
    if "nothing to commit" in output or "nothing added to commit" in output:
        print("[publish] nothing to commit")
        return True
    print(result.stdout)
    print(result.stderr)
    print(f"[publish] git commit failed (exit {result.returncode})")
    return False


if __name__ == "__main__":
    sys.exit(0 if publish() else 1)
