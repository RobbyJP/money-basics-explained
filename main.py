"""
Full cycle: generate N new articles -> rebuild static site -> publish.

Usage:
    python main.py --once --count 2
"""
import argparse
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--count", type=int, default=1)
    parser.add_argument("--skip-publish", action="store_true", help="Build but don't git push")
    args = parser.parse_args()

    if not args.once:
        print("This scaffold only supports --once (use cron/GitHub Actions to schedule).")
        return

    steps = [
        [sys.executable, "content_gen.py", "--count", str(args.count)],
        [sys.executable, "site_builder.py"],
    ]
    if not args.skip_publish:
        steps.append([sys.executable, "publish.py"])

    for step in steps:
        result = subprocess.run(step)
        if result.returncode != 0:
            print(f"[main] step failed: {' '.join(step)}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
