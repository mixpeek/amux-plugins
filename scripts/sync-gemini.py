#!/usr/bin/env python3
"""Generate the Gemini CLI commands from the shared skills, so all three hosts run the same text.

plugins/amux/skills/<name>/SKILL.md  ->  commands/amux/<name>.toml  (/amux:<name> in Gemini CLI)

Run with --check to exit 1 when the generated files are out of date (CI uses this).
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "plugins/amux/skills"
OUT = ROOT / "commands/amux"


def render(skill: pathlib.Path) -> str:
    text = skill.read_text()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        sys.exit(f"{skill}: no front matter")
    desc = re.search(r"^description:\s*(.+)$", m.group(1), re.M).group(1).strip()
    body = m.group(2).strip() + "\n\nThe user's request, if any: {{args}}\n"
    # TOML basic strings: json.dumps gives a valid escaped one-line string; the body uses a literal multi-line string.
    if "'''" in body:
        sys.exit(f"{skill}: body contains ''' and cannot be a TOML literal string")
    return (f"# Generated from {skill.relative_to(ROOT)} by scripts/sync-gemini.py. Edit the skill, not this file.\n"
            f"description = {json.dumps(desc)}\nprompt = '''\n{body}'''\n")


def main() -> int:
    check = "--check" in sys.argv
    stale = []
    want = {}
    for skill in sorted(SKILLS.glob("*/SKILL.md")):
        want[OUT / f"{skill.parent.name}.toml"] = render(skill)
    for path, content in want.items():
        if not path.exists() or path.read_text() != content:
            stale.append(path)
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
    extra = [p for p in OUT.glob("*.toml") if p not in want]
    for p in extra:
        stale.append(p)
        if not check:
            p.unlink()
    print(f"{len(want)} skills, {len(stale)} command file(s) {'out of date' if check else 'written or removed'}")
    return 1 if (check and stale) else 0


if __name__ == "__main__":
    sys.exit(main())
