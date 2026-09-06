#!/usr/bin/env python3
import re
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
readme = root / "README.md"
todo = root / "TODO.md"
issues = []
if not readme.is_file():
    issues.append("missing README.md")
else:
    text = readme.read_text(errors="ignore")
    if re.search(r"/(home|Users)/[^/]+/", text):
        issues.append("README contains an absolute user path")
    if "```" not in text:
        issues.append("README contains no command example")
if not todo.is_file():
    issues.append("missing TODO.md")
print("\n".join(issues) if issues else "Documentation checks passed")
raise SystemExit(bool(issues))
