#!/usr/bin/env python3
"""Check SQLite availability and a chosen persistence directory without writing data."""

from __future__ import annotations

import shutil
import sqlite3
import sys
from pathlib import Path


def main() -> int:
    target = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else Path(".agent-memory")
    sqlite_cli = shutil.which("sqlite3")
    sqlite_module = sqlite3.sqlite_version
    print(f"PASS Python SQLite: {sqlite_module}")
    print(f"PASS sqlite3 CLI: {sqlite_cli}" if sqlite_cli else "INFO sqlite3 CLI: not found (Python SQLite is available)")
    try:
        target.mkdir(parents=True, exist_ok=True)
        writable = target.is_dir()
    except OSError as exc:
        print(f"BLOCKED persistence directory: {exc}", file=sys.stderr)
        return 1
    print(f"PASS persistence directory: {target.resolve()}" if writable else "BLOCKED persistence path")
    print("Preflight passed. No memory record was created.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
