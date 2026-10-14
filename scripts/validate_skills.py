#!/usr/bin/env python3
"""Validate skill frontmatter, directory names, and the 1,000-line limit."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REQUIRED = {"name", "description", "license"}
MAX_LINES = 1000
KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$")


def scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, ["frontmatter must start with --- on line 1"]
    try:
        end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        return {}, ["frontmatter closing --- is missing"]
    fields: dict[str, str] = {}
    current_key: str | None = None
    for number, raw in enumerate(lines[1:end], start=2):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        match = KEY_RE.match(raw)
        if match:
            current_key = match.group(1)
            if current_key in fields:
                errors.append(f"line {number}: duplicate field {current_key!r}")
            fields[current_key] = scalar(match.group(2) or "")
        elif raw.startswith((" ", "\t")) and current_key:
            fields[current_key] = (fields[current_key] + " " + raw.strip()).strip()
        else:
            errors.append(f"line {number}: unsupported frontmatter syntax")
    for key in sorted(REQUIRED - fields.keys()):
        errors.append(f"required field {key!r} is missing")
    for key in sorted(REQUIRED & fields.keys()):
        if not fields[key].strip():
            errors.append(f"required field {key!r} is empty")
    return fields, errors


def main() -> int:
    if not SKILLS.is_dir():
        print("ERROR: skills/ directory is missing", file=sys.stderr)
        return 1
    skill_dirs = sorted(path for path in SKILLS.iterdir() if path.is_dir())
    errors: list[str] = []
    if not skill_dirs:
        errors.append("skills/: no skill directories found")
    for directory in skill_dirs:
        spec = directory / "SKILL.md"
        if not spec.is_file():
            errors.append(f"{directory.relative_to(ROOT)}: SKILL.md is missing")
            continue
        fields, parse_errors = parse_frontmatter(spec)
        errors.extend(f"{spec.relative_to(ROOT)}: {error}" for error in parse_errors)
        if not directory.name.startswith("gemini-skills-"):
            errors.append(
                f"{directory.relative_to(ROOT)}: folder name must start with 'gemini-skills-' (standard: gemini-skills-<objetivo>)"
            )
        if fields.get("name") and fields["name"] != directory.name:
            errors.append(
                f"{spec.relative_to(ROOT)}: name {fields['name']!r} does not match folder {directory.name!r}"
            )
        IGNORED_PARTS = {"__pycache__", ".git"}
        IGNORED_EXTS = {".pyc", ".pyo", ".png", ".jpg", ".jpeg", ".ico", ".zip", ".tar", ".gz"}
        for file_path in sorted(path for path in directory.rglob("*") if path.is_file()):
            if any(part in file_path.parts for part in IGNORED_PARTS) or file_path.suffix.lower() in IGNORED_EXTS:
                continue
            try:
                with file_path.open("r", encoding="utf-8") as stream:
                    count = sum(1 for _ in stream)
            except (UnicodeError, OSError) as exc:
                errors.append(f"{file_path.relative_to(ROOT)}: cannot read file: {exc}")
                continue
            if count > MAX_LINES:
                errors.append(f"{file_path.relative_to(ROOT)}: {count} lines exceeds {MAX_LINES}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Validated {len(skill_dirs)} skill(s); all specs and files meet requirements.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
