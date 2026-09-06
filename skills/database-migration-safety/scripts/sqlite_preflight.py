#!/usr/bin/env python3
import json
import sqlite3
import sys
from pathlib import Path

path = Path(sys.argv[1]).resolve()
connection = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
version = connection.execute("PRAGMA user_version").fetchone()[0]
tables = [row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
print(json.dumps({"path": str(path), "bytes": path.stat().st_size, "integrity": integrity, "user_version": version, "tables": tables}, indent=2))
