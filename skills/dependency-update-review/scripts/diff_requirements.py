#!/usr/bin/env python3
import re
import sys
from pathlib import Path

def parse(path):
    result = {}
    for raw in Path(path).read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith(("#", "-")):
            continue
        match = re.match(r"([A-Za-z0-9_.-]+)(.*)", line)
        if match:
            result[match.group(1).lower().replace("_", "-")] = match.group(2).strip()
    return result

before, after = map(parse, sys.argv[1:3])
for name in sorted(before.keys() | after.keys()):
    if before.get(name) != after.get(name):
        print(f"{name}: {before.get(name, '<absent>')} -> {after.get(name, '<absent>')}")
