#!/usr/bin/env python3
"""
One-off remediation: wrap the body of every *converted* post/page (those with a
`ghost_id:` in their front matter) in {% raw %}...{% endraw %} so Jekyll's Liquid
parser doesn't choke on embedded {{ }} / {% %} code snippets.

Hand-written files (no ghost_id) are left untouched. Idempotent: files already
wrapped are skipped. Run from the repo root:  python tools/fix_liquid_raw.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FM = re.compile(r"^(---\n.*?\n---\n)(.*)$", re.DOTALL)


def fix(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    m = FM.match(text)
    if not m:
        return False
    front, body = m.group(1), m.group(2)
    if "ghost_id:" not in front:          # only converted content
        return False
    if "{% raw %}" in body:                # already wrapped
        return False
    stripped = body.strip("\n")
    if not stripped:
        return False
    new_body = "\n{% raw %}\n" + stripped + "\n{% endraw %}\n"
    path.write_text(front + new_body, encoding="utf-8")
    return True


def main() -> None:
    changed = 0
    for folder in ("_posts", "_pages", "_drafts"):
        for path in sorted((ROOT / folder).glob("*.md")):
            if fix(path):
                changed += 1
                print(f"wrapped {path.relative_to(ROOT)}")
    print(f"\nDone. Wrapped {changed} file(s).")


if __name__ == "__main__":
    main()
