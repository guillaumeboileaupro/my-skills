#!/usr/bin/env python3
import json
import sys
from pathlib import Path

evidence = json.loads(Path(sys.argv[1]).read_text())
requirements = [line.strip() for line in Path(sys.argv[2]).read_text().splitlines() if line.strip()]
items = evidence if isinstance(evidence, list) else evidence.get("evidence", [])
for requirement in requirements:
    words = {word.lower() for word in requirement.split() if len(word) > 3}
    matches = [item for item in items if words & set(str(item).lower().split())]
    print(f"{'SUPPORTED' if matches else 'UNSUPPORTED'}: {requirement}")
    for match in matches[:3]:
        print(f"  - {match}")
