#!/usr/bin/env python3
import csv
import math
import statistics
import sys

with open(sys.argv[1], newline="", encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))
invalid_only = False
for name in rows[0] if rows else []:
    values = []
    invalid = 0
    for row in rows:
        try:
            value = float(row[name])
            values.append(value) if math.isfinite(value) else None
            invalid += int(not math.isfinite(value))
        except (TypeError, ValueError):
            invalid += 1
    if values:
        print(f"{name}: n={len(values)} invalid={invalid} mean={statistics.fmean(values):.6g} min={min(values):.6g} max={max(values):.6g}")
    else:
        invalid_only = True
        print(f"{name}: n=0 invalid={invalid} no finite values")
raise SystemExit(invalid_only)
