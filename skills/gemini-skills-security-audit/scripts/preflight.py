#!/usr/bin/env python3
"""Check local prerequisites for Strix without launching a scan or exposing secrets."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys

REQUIRED_CREDENTIALS = ("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "GOOGLE_API_KEY")


def check_docker() -> bool:
    executable = shutil.which("docker")
    if not executable:
        print("BLOCKED Docker: executable not found")
        return False
    try:
        result = subprocess.run(
            [executable, "info", "--format", "{{.ServerVersion}}"],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.TimeoutExpired):
        print("BLOCKED Docker: daemon check failed or timed out")
        return False
    if result.returncode != 0 or not result.stdout.strip():
        print("BLOCKED Docker: daemon unavailable or inaccessible")
        return False
    print(f"PASS Docker: daemon available (version {result.stdout.strip()})")
    return True


def main() -> int:
    checks = [check_docker()]
    strix = shutil.which("strix")
    if strix:
        print(f"PASS Strix CLI: executable found at {strix}")
        checks.append(True)
    else:
        print("BLOCKED Strix CLI: executable 'strix' not found")
        checks.append(False)

    configured = [name for name in REQUIRED_CREDENTIALS if os.environ.get(name, "").strip()]
    if configured:
        print("PASS model credentials: at least one supported credential variable is set (value hidden)")
        checks.append(True)
    else:
        print(
            "BLOCKED model credentials: set the provider variable required by your Strix configuration "
            f"(checked {', '.join(REQUIRED_CREDENTIALS)})"
        )
        checks.append(False)

    if all(checks):
        print("Preflight passed. This does not authorize a scan; confirm target scope separately.")
        return 0
    print("Preflight failed. No scan was started.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
