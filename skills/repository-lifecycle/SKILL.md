---
name: repository-lifecycle
description: Prevent branch, worktree, PR, workflow and token proliferation. Reuse existing authorized workspaces; preserve user work.
---

# Repository lifecycle — deliver code without sprawl

## Before creating resources
1. Inspect relevant branch, worktree and PR once, using targeted Git commands; do not repeat broad diagnoses.
2. Reuse the existing repository checkout, authorized branch and PR whenever safe. New reconciliation branches, worktrees and PRs require owner approval and a demonstrated need.
3. Repository boundary is absolute: do not create, write, move, rename or delete any file or directory outside the root of the repository being worked on. In particular, never create sibling directories such as `../<repo>-codex`, `../<repo>-e03` or external worktree folders. This applies to agents, scripts, tests, caches, temporary artifacts and cleanup. An explicit owner-approved exception is required for any outside path; merely asking for a worktree is not such an exception.
4. Default to no new worktree. If the owner explicitly authorizes a new worktree, first confirm a safe location inside the repository root, ignored by Git, and verify that Git supports the chosen layout without interfering with the primary checkout. Otherwise stop and ask the owner to choose a permitted workflow.
5. One mission, one worktree is a safety ceiling, NOT a requirement to create a new worktree on every task.
6. Run Graphify only to answer a concrete unresolved dependency question; reuse cached graphs. Prefer impacted tests over whole-suite repetition.
7. Review CI coverage before adding workflows; consolidate duplicated jobs/triggers while retaining release builds and security audits.

## Execution
6. Implement actual source changes, run focused tests, commit and push only on authorized branches. Reports are not a substitute for coding.
7. Follow the owner's merge strategy. Do not require a consolidated candidate when the owner chooses to merge existing PRs.
8. Never modify another agent's worktree or overwrite dirty files. Do not invent hardware results or claim unverified CI success.

## Completion and cleanup
9. After owner-approved integration, prove which old PRs are subsumed. Close only with explicit authorization; closing a PR is not merging it.
10. With approval, remove only clean, pushed, no-longer-used worktrees via git worktree remove (without force), then fully integrated branches with git branch -d. Preserve dirty and active worktrees. For any pre-existing worktree outside the repository root, do not remove or alter it without a separate explicit owner exception to the boundary rule; report it as requiring owner action.
11. Never clean sibling folders or other outside-repository paths, even if they appear obsolete, without explicit per-path authorization. Delete remote branches only with owner approval and reachability verification. Never use rm -rf, git clean, reset --hard, or force push as routine cleanup.
12. Check workflow triggers and job overlap; do not disable audits to obtain green CI.
13. If requested to write a prompt, provide only a prompt; if asked for a plan, give a plan. Never perform GitHub mutations without the explicit requested action.

## Tokens, reporting, estimates
- Avoid repeated analyses, re-indexing or reviews when failures are already known.
- Report in ten lines or fewer: code changes, commit, tests, CI, blockers, next action.
- Count integration, cleanup, packaging and hardware acceptance once, from the start. Reduce remaining time after completed work; mark unmeasured estimates as unknown.
- If blocked, move to an independent implementation task rather than creating new diagnostic PRs.
