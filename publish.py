"""
Commit and push the built docs/ dir to GitHub main branch.
Handles remote sync, safe commits, and rebases cleanly.
"""
import os
import subprocess
import sys

from dotenv import load_dotenv

load_dotenv()

BRANCH = os.getenv("GIT_REMOTE_BRANCH", "main")
PUBLIC_DIR = os.getenv("PUBLIC_DIR", "docs")


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
        # Pull with rebase before pushing to avoid remote push conflicts
        run(["git", "pull", "--rebase", "origin", BRANCH])
        return run(["git", "push", "origin", BRANCH])
    
    output = result.stdout + result.stderr
    if "nothing to commit" in output or "nothing added to commit" in output:
        print("[publish] nothing to commit (clean working tree)")
        return True
    print(result.stdout)
    print(result.stderr)
    print(f"[publish] git commit failed (exit {result.returncode})")
    return False


if __name__ == "__main__":
    if not publish():
        sys.exit(1)
