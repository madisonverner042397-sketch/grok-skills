#!/usr/bin/env python3
"""Check the YAML frontmatter of every skills/<name>/SKILL.md.

Each skill must have frontmatter that parses as a YAML mapping with non-empty
`name`, `description` and `license`, where `name` matches the folder, and the
skill must be listed in the README catalog.

Usage: python3 scripts/check_frontmatter.py   (run from the repo root)
Exits 1 if any skill fails. Errors use GitHub Actions annotation format.
"""
import os
import re
import sys

import yaml

REQUIRED = ("name", "description", "license")
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def check_skill(name, readme):
    path = f"skills/{name}/SKILL.md"
    if not os.path.isfile(path):
        return path, ["missing SKILL.md"]
    with open(path, encoding="utf-8") as f:
        match = FRONTMATTER.match(f.read())
    if not match:
        return path, ["no frontmatter block (file must start with '---')"]
    try:
        fm = yaml.safe_load(match.group(1))
    except yaml.YAMLError as e:
        first = str(e).splitlines()[0]
        return path, [f"invalid YAML: {first} (quote values that contain ': ')"]
    if not isinstance(fm, dict):
        return path, ["frontmatter is not a YAML mapping"]
    errors = [f"missing or empty `{key}`" for key in REQUIRED if not fm.get(key)]
    if fm.get("name") and fm["name"] != name:
        errors.append(f"`name` is {fm['name']!r} but the folder is {name!r}")
    if path not in readme:
        errors.append("not listed in the README catalog")
    return path, errors


def main():
    with open("README.md", encoding="utf-8") as f:
        readme = f.read()
    names = sorted(d for d in os.listdir("skills") if os.path.isdir(f"skills/{d}"))
    failed = 0
    for name in names:
        path, errors = check_skill(name, readme)
        for err in errors:
            print(f"::error file={path}::{err}")
        failed += bool(errors)
    print(f"{len(names)} skills checked, {failed} with problems")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
