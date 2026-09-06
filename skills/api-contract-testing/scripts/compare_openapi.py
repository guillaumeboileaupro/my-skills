#!/usr/bin/env python3
import json
import sys
from pathlib import Path

before, after = (json.loads(Path(name).read_text()) for name in sys.argv[1:3])
for path, methods in before.get("paths", {}).items():
    for method, operation in methods.items():
        if method.startswith("x-") or not isinstance(operation, dict):
            continue
        current = after.get("paths", {}).get(path, {}).get(method)
        if current is None:
            print(f"REMOVED operation {method.upper()} {path}")
            continue
        old_codes = set(operation.get("responses", {}))
        new_codes = set(current.get("responses", {}))
        for code in sorted(old_codes - new_codes):
            print(f"REMOVED response {method.upper()} {path} {code}")
