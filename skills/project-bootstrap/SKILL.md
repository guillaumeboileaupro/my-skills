---
name: project-bootstrap
description: Verify and bootstrap project instructions, rules, skills and safety controls for Codex and Claude Code before development tasks.
---

# Project bootstrap - Codex and Claude Code

## Mandatory preflight
Before changing application code, inspect the repository and determine which agent runtimes are actually used. Check existing `AGENTS.md`, `CLAUDE.md`, `.agents/`, `.claude/`, `.codex/`, `.mcp.json`, scripts and `.gitignore`. Report missing elements. Never overwrite or duplicate existing configuration without reviewing it.

## Shared policy
- `AGENTS.md` is the entry point for Codex. Keep concise project purpose, build/test commands, SOLID and security constraints, and pointers to detailed documents.
- `CLAUDE.md` is the entry point for Claude Code; refer to shared rules rather than copying large instructions.
- `CLAUDE.local.md`, `.claude/settings.local.json`, local worktrees and credentials must remain local and ignored by Git.
- Store reusable skills as `SKILL.md` with valid YAML frontmatter; load only skills relevant to the task.
- Follow existing project conventions, SOLID principles, least privilege, focused tests and verification.
- Avoid redundant context and unnecessary agent/tool invocations to minimize tokens.

## Claude Code layout (when Claude is used)
```text
CLAUDE.md
CLAUDE.local.md                 # local, gitignored
.mcp.json                       # only non-secret configuration
.claude/
  settings.json
  settings.local.json           # local, gitignored
  rules/
    code-style.md
    testing.md
    api-conventions.md
  skills/<skill-name>/SKILL.md
  agents/code-reviewer.md
  agents/security-auditor.md
  hooks/validate-bash.sh
  worktrees/                    # gitignored
```
Create files only when applicable. Do not create placeholder agents, MCP servers, hooks or permissions that are not implemented.

## Codex layout (when Codex is used)
```text
AGENTS.md
.agents/skills/<skill-name>/SKILL.md   # project-scoped skills, when needed
.codex/config.toml                     # only supported, project-specific settings
```
Codex does not automatically execute Claude-specific hooks, agents, rules or settings. Translate requirements into `AGENTS.md`, native Codex configuration and explicitly invoked project scripts. Do not assume that arbitrary paths in `.codex/` or `.agents/` are natively supported. Reuse this shared skills repository and its installer for user-level skills; avoid unnecessary duplication.

## Procedure
1. Inspect tracked and untracked files and current branch; check for existing agent instructions.
2. Identify runtime(s), language, build/test tooling and project-specific constraints.
3. Propose minimal missing files; create only necessary supported configuration. Preserve user content and secrets.
4. Update `.gitignore` carefully for local settings, worktrees and credentials, without hiding tracked project files.
5. Validate YAML frontmatter, JSON/TOML syntax and shell scripts when present.
6. Run the smallest relevant checks, record failures, and only then start the requested development task.

## Stop conditions
Stop and ask before destructive changes, overwriting conflicting instructions, introducing new external integrations, or committing secrets. Never claim setup or tests succeeded without checking.
