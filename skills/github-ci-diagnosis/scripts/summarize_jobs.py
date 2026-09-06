#!/usr/bin/env python3
import json
import sys
from pathlib import Path

data = json.loads(Path(sys.argv[1]).read_text())
jobs = data.get("jobs", data if isinstance(data, list) else [])
for job in jobs:
    failed = [s for s in job.get("steps", []) if s.get("conclusion") not in (None, "success", "skipped")]
    if job.get("conclusion") != "success" or failed:
        print(f"{job.get('name', '<unnamed>')}: {job.get('conclusion', 'unknown')}")
        for step in failed:
            print(f"  - {step.get('name', '<unnamed>')}: {step.get('conclusion', 'unknown')}")
