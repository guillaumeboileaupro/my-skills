#!/usr/bin/env python3
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
groups = [("README", ["README.md"]), ("agent context", ["AGENTS.md"]), ("planning", ["TODO.md", "ROADMAP.md", "docs/ROADMAP.md"])]
missing = [label for label, choices in groups if not any((root / name).is_file() for name in choices)]
print("Missing: " + ", ".join(missing) if missing else "Core context files present")
raise SystemExit(bool(missing))
