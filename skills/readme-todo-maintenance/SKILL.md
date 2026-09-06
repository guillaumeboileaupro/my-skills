---
name: readme-todo-maintenance
description: Keep README and TODO documentation aligned with verified repository behavior. Use after feature, architecture, command, packaging, limitation, or roadmap changes.
---

# README and TODO Maintenance

Write documentation a new user can execute without hidden context.

- Verify commands in the repository before documenting them.
- Cover purpose, current features, prerequisites, install, launch, stop, tests, build, package, install, uninstall, persistence, architecture, limitations, and license when relevant.
- Explain the runtime flow between interface, API, domain logic, and storage.
- Mark sample data, experimental features, unsigned packages, and untested platforms accurately.
- Remove completed TODOs only after their acceptance conditions are met.
- Give each remaining TODO a priority, concrete outcome, and verification condition.
- Avoid absolute local paths, stale version numbers, and claims copied from plans rather than code.

Run `python scripts/check_docs.py <project-root>` for a lightweight documentation consistency report.
