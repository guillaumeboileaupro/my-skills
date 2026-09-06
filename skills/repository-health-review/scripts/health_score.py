#!/usr/bin/env python3
import json
import sys
from pathlib import Path

signals = json.loads(Path(sys.argv[1]).read_text())
weights = {"default_ci_passing": 30, "readme_current": 15, "tests_present": 15, "recent_release": 10, "security_policy": 10, "todo_current": 10, "open_blocker": -20, "stale_pr": -10}
score = max(0, min(100, 20 + sum(weight for key, weight in weights.items() if signals.get(key))))
print(json.dumps({"score": score, "advisory": True, "signals": signals}, indent=2, sort_keys=True))
