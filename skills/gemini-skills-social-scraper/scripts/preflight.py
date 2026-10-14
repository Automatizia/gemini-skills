#!/usr/bin/env python3
"""Check Agent-Reach runtime dependencies without installing or accessing sites."""

from __future__ import annotations

import importlib.util
import shutil
import sys


def main() -> int:
    checks: list[bool] = []
    print(f"PASS Python: {sys.version.split()[0]}" if sys.version_info >= (3, 8) else "BLOCKED Python: 3.8+ required")
    checks.append(sys.version_info >= (3, 8))

    cli = shutil.which("agent-reach")
    if cli:
        print(f"PASS Agent-Reach CLI: found at {cli}")
        checks.append(True)
    else:
        print("INFO Agent-Reach CLI: not found; install from the upstream project if needed")

    for module, label, optional in (("requests", "requests", True), ("bs4", "beautifulsoup4", True), ("playwright", "playwright", True)):
        present = importlib.util.find_spec(module) is not None
        print(f"{'PASS' if present else 'INFO'} {label}: {'available' if present else 'not installed (optional, feature-dependent)'}")
        if not optional:
            checks.append(present)

    if all(checks):
        print("Preflight passed. Platform access and extraction permissions are not tested.")
        return 0
    print("Preflight failed: install a supported Python 3 runtime.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
