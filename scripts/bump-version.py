#!/usr/bin/env python3
"""
Bump the containerhive dependency version and tag the release.

Usage:
    ./scripts/bump-version.py 0.14.0
    ./scripts/bump-version.py v0.14.0
"""

import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PYPROJECT = REPO_ROOT / "pyproject.toml"

VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
DEP_RE = re.compile(r'"containerhive==([\d.]+)"')
PROJECT_VERSION_RE = re.compile(r'^(version\s*=\s*)"[\d.]+"', re.MULTILINE)


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/bump-version.py <version>")
        sys.exit(1)

    raw = sys.argv[1]
    version = raw.removeprefix("v")

    if not VERSION_RE.match(version):
        print(f"error: invalid version '{raw}'. Expected format: x.y.z or vx.y.z")
        sys.exit(1)

    tag = f"v{version}"
    content = PYPROJECT.read_text()

    dep_match = DEP_RE.search(content)
    if not dep_match:
        print("error: could not find 'containerhive==<version>' in pyproject.toml")
        sys.exit(1)

    old_version = dep_match.group(1)
    content = content.replace(f'"containerhive=={old_version}"', f'"containerhive=={version}"')
    content = PROJECT_VERSION_RE.sub(rf'\1"{version}"', content)

    PYPROJECT.write_text(content)
    print(f"Updated containerhive dependency: {old_version} -> {version}")
    print(f"Updated project version: {old_version} -> {version}")

    subprocess.run(["git", "add", "pyproject.toml"], check=True, cwd=REPO_ROOT)
    subprocess.run(["git", "add", ".pre-commit-config.yaml"], check=False, cwd=REPO_ROOT)
    subprocess.run(
        ["git", "commit", "-m", f"chore: bump containerhive to {tag}"],
        check=True,
        cwd=REPO_ROOT,
    )
    subprocess.run(["git", "tag", tag], check=True, cwd=REPO_ROOT)
    print(f"Created commit and tag: {tag}")


if __name__ == "__main__":
    main()
