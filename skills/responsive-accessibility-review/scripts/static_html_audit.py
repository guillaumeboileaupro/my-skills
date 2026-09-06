#!/usr/bin/env python3
import sys
from html.parser import HTMLParser
from pathlib import Path

class Audit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.issues = []
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == "img" and "alt" not in data:
            self.issues.append("image missing alt")
        if tag in {"input", "select", "textarea"} and not any(key in data for key in ("aria-label", "aria-labelledby", "id")):
            self.issues.append(f"{tag} may lack an accessible name")
        if tag == "html" and "lang" not in data:
            self.issues.append("html missing lang")

argument = sys.argv[1]
if argument == "-":
    sources = [("<stdin>", sys.stdin.read())]
else:
    target = Path(argument)
    paths = [target] if target.is_file() else list(target.rglob("*.html"))
    sources = [(str(path), path.read_text(errors="ignore")) for path in paths]
for label, source in sources:
    audit = Audit()
    audit.feed(source)
    for issue in audit.issues:
        print(f"{label}: {issue}")
