#!/usr/bin/env python3
import re
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
pattern = re.compile(r"https?://|\b(requests|httpx|fetch|axios|telemetry|analytics|websocket)\b", re.I)
for path in root.rglob("*"):
    if path.is_file() and path.suffix.lower() in {".py", ".js", ".ts", ".tsx", ".rs", ".json", ".toml"}:
        try:
            for number, line in enumerate(path.read_text(errors="ignore").splitlines(), 1):
                if pattern.search(line):
                    print(f"{path}:{number}:{line.strip()[:180]}")
        except OSError:
            pass
