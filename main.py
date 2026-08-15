"""
Full cycle: generate new trending content -> rebuild static site -> publish.

Usage:
    python main.py --once
    python main.py --once --dry-run
    python main.py --once --static
"""
import argparse
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description="Money Clarity Content & Publishing Runner")
    parser.add_argument("--once", action="store_true", help="Execute single publishing cycle")
    parser.add_argument("--dry-run", action="store_true", help="Run without generating new articles or publishing")
    parser.add_argument("--static", action="store_true", help="Use static keywords.csv instead of dynamic trending discovery")
    parser.add_argument("--lang", choices=["en", "id"], default=None, help="Force specific language (en or id)")
    parser.add_argument("--skip-publish", action="store_true", help="Build but don't git push")
    args = parser.parse_args()

    if not args.once and not args.dry_run:
        print("Usage: python main.py --once (or --dry-run / --help)")
        return

    if args.dry_run:
        cmd = [sys.executable, "auto_publisher.py", "--dry-run"]
        if args.lang:
            cmd.extend(["--lang", args.lang])
        subprocess.run(cmd)
        return

    if args.static:
        steps = [
            [sys.executable, "content_gen.py", "--count", "1"],
            [sys.executable, "site_builder.py"],
        ]
    else:
        auto_cmd = [sys.executable, "auto_publisher.py"]
        if args.lang:
            auto_cmd.extend(["--lang", args.lang])
        steps = [
            auto_cmd,
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
