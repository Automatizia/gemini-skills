#!/usr/bin/env python3
"""Check Node tooling and local gateway candidate ports; does not start a server."""

from __future__ import annotations

import shutil
import socket
import sys


def port_available(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        return sock.connect_ex(("127.0.0.1", port)) != 0


def main() -> int:
    node = shutil.which("node")
    npx = shutil.which("npx")
    checks = [bool(node), bool(npx)]
    print(f"PASS Node.js: {node}" if node else "BLOCKED Node.js: executable 'node' not found")
    print(f"PASS npx: {npx}" if npx else "BLOCKED npx: executable not found")
    for port in (8000, 3000):
        available = port_available(port)
        print(f"{'PASS' if available else 'INFO'} localhost:{port}: {'available' if available else 'in use'}")
    if all(checks):
        print("Preflight passed. Confirm the actual listening port after starting the gateway.")
        return 0
    print("Preflight failed: install Node.js with npx.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
