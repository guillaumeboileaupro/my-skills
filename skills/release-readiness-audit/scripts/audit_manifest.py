#!/usr/bin/env python3
import hashlib
import json
import sys
from pathlib import Path

manifest = json.loads(Path(sys.argv[1]).read_text())
missing = [key for key in ("version", "commit", "checks", "artifacts") if key not in manifest]
for artifact in manifest.get("artifacts", []):
    path = Path(artifact.get("path", ""))
    if not path.is_file():
        missing.append(f"artifact:{path}")
    elif artifact.get("sha256"):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != artifact["sha256"]:
            missing.append(f"checksum:{path}")
print(json.dumps({"ready": not missing, "problems": missing}, indent=2))
raise SystemExit(bool(missing))
