#!/usr/bin/env python3
"""Deterministically inspect common project manifests and suggest agent tooling."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "vendor", "dist", "build", "__pycache__"}
MANIFESTS = {"package.json", "requirements.txt", "pyproject.toml", "Dockerfile", "docker-compose.yml", "compose.yaml"}


def files_in(root: Path) -> list[Path]:
    found: list[Path] = []
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS or part.startswith(".") and part not in {".github"} for part in path.relative_to(root).parts):
            continue
        if path.is_file() and (path.name in MANIFESTS or path.name in {"tsconfig.json", "next.config.js", "next.config.ts", "next.config.mjs"}):
            found.append(path)
    return sorted(found)


def inspect(root: Path) -> dict:
    evidence: list[str] = []
    package: dict = {}
    for path in files_in(root):
        relative = path.relative_to(root).as_posix()
        evidence.append(relative)
        if path.name == "package.json":
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
                if relative == "package.json":
                    package = data
            except (OSError, UnicodeError, json.JSONDecodeError):
                evidence.append(f"{relative} (invalid/unreadable JSON)")
    deps = {**package.get("dependencies", {}), **package.get("devDependencies", {})}
    files = set(evidence)
    skills: set[str] = set()
    hooks: set[str] = set()
    mcps: set[str] = set()
    if "next" in deps or any(Path(item).name.startswith("next.config.") for item in files):
        skills.update(("modern-frontend", "ui-ux-pro-max"))
    if any(name in deps for name in ("react", "vue", "svelte", "angular")):
        skills.add("ui-ux-pro-max")
    if any(name in files for name in ("Dockerfile", "docker-compose.yml", "compose.yaml")):
        skills.add("strix-security-audit")
        hooks.add("container-build-review")
    if "pyproject.toml" in {Path(item).name for item in files} or "requirements.txt" in {Path(item).name for item in files}:
        skills.add("python-project-review")
    if "package.json" in {Path(item).name for item in files}:
        hooks.add("lint-and-test-before-commit")
    if any(Path(item).suffix in {".ts", ".tsx", ".js", ".jsx"} for item in files):
        mcps.add("filesystem (read-only, project-scoped)")
    return {"project": str(root), "evidence": evidence, "recommendations": {"skills": sorted(skills), "hooks": sorted(hooks), "mcps": sorted(mcps)}, "limitations": ["Static heuristics only; verify project context and tool compatibility.", "No files were modified and no project code was executed."]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", type=Path, default=Path.cwd())
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    args = parser.parse_args()
    root = args.directory.expanduser().resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")
    report = inspect(root)
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"# Project setup audit: {root}

## Evidence
")
        print("
".join(f"- `{item}`" for item in report["evidence"]) or "- No recognized manifests found")
        print("
## Recommendations
")
        for group, values in report["recommendations"].items():
            print(f"### {group.title()}
")
            print("
".join(f"- {value}" for value in values) or "- None")
            print()
        print("## Limitations

" + "
".join(f"- {item}" for item in report["limitations"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
