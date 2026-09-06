---
name: repository-health-review
description: Review repository health from activity, pull requests, issues, CI, releases, documentation, and TODOs. Use for project status reports, maintenance decisions, and prioritized next actions.
---

# Repository Health Review

Base the review on current evidence and distinguish inactive from unhealthy.

- Inspect recent commits, open PRs and issues, workflow results, releases, dependency state, README, TODO, and branch divergence.
- Identify blocked work, failing default-branch CI, unreviewed changes, stale plans, missing release validation, and security or data risks.
- Classify next actions as urgent, important, useful, or optional.
- Recommend active development, maintenance mode, or archive only with explicit reasons.
- Do not penalize a stable finished project solely for low activity.
- Link every actionable finding to its source when possible.

Use `python scripts/health_score.py signals.json` for a transparent advisory score. The narrative evidence remains authoritative.
