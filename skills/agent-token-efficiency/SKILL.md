---
name: agent-token-efficiency
description: Minimize Claude Code and Codex token usage through scoped reads, concise outputs, incremental context and targeted validation. Use on every development mission.
---

# Token efficiency - Claude Code and Codex

## Shared rules
- Read the smallest relevant scope. Locate with `rg -n` or `grep -n`, then inspect bounded line ranges; avoid dumping entire files, logs, generated trees and lockfiles.
- Filter output at the source. Show concise failure summaries and exact relevant lines; keep full logs in artifacts when needed for debugging.
- Reuse verified facts and command results already available in the current session. Re-run checks when code, dependencies, environment or required verification changed.
- Batch independent, cheap inspections; avoid repeated polling and unnecessary broad repository scans.
- Keep prompts focused on objective, scope, constraints, current branch/PR and required skill names. Do not paste instructions already available in repository guidance.
- Prefer focused tests during development, then run all mandatory quality and security gates before handoff. Never skip required checks to save tokens.
- Report only decisions, changed files, evidence, blockers and next action, following the repository's reporting skill.
- Never start subagents unless explicitly authorized. Respect repository limits on active agents and open PRs.
- At context boundaries, preserve a short factual handoff: objective, branch, commit, verified results, unresolved issues, next action. Do not discard safety rules or claim unverified outcomes.
- Do not use aggressive truncation that hides test failures, warnings or security findings. Keep a pointer to the complete evidence.

## Codex
- Use `AGENTS.md` as repository instructions and reference this skill by name; keep `AGENTS.md` short rather than duplicating this file.
- Use the skill's `SKILL.md` for procedures; keep optional `agents/openai.yaml` metadata concise.
- Request narrow tool output and scoped edits. Avoid repeating prior context in subsequent prompts.
- Codex-specific compaction and token accounting depend on the client/version; do not assume Claude hooks or commands exist.

## Claude Code
- Use `CLAUDE.md` and the same `SKILL.md` rules, without duplicating the full instructions in prompts.
- Claude-specific hooks and context commands require separate configuration; never copy them into Codex as-is.

## Measurement
- Compare equivalent tasks and model settings before and after changes.
- Track available input/output token usage, number of tool calls, repeated reads and successful quality gates.
- Do not promise a fixed saving percentage; prioritize correctness and traceability over token reduction.
