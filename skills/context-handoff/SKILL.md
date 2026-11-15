---
name: context-handoff
description: Preserve concise verified context between Claude Code and Codex sessions.
---

# Context handoff

Use when a session is ending, interrupted or resumed.

- Record objective, scope, repository, branch, current commit, open PR and ownership.
- Record verified commands and results, changed files, blockers and next concrete action.
- Separate observed facts from assumptions; never mark untested work as complete.
- Keep a compact handoff in the repository's existing approved handoff location; do not create competing tracking documents.
- On resume, check branch/PR and changed state before relying on the handoff.
- Never include secrets, private logs or personal data.
- Respect the repository's one-agent and PR rules; never modify another agent's work.
