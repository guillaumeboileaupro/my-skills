# Agent Skills

Central repository for personal skills shared by Codex and Claude.

## Structure

Each skill lives in its own directory under `skills/`:

```text
skills/
`-- <skill-name>/
    |-- SKILL.md
    |-- scripts/             optional executable helpers
    `-- agents/
        `-- openai.yaml      optional Codex interface metadata
```

## Install

Install every skill for both agents:

```bash
bash scripts/install.sh
```

Install for one agent only:

```bash
bash scripts/install.sh codex
bash scripts/install.sh claude
```

The installer creates symbolic links in `${CODEX_HOME:-$HOME/.codex}/skills` and `${CLAUDE_HOME:-$HOME/.claude}/skills` without replacing existing files or directories. Each `SKILL.md` is shared. The optional `agents/openai.yaml` file provides Codex interface metadata and is ignored by Claude.

## Add a skill

1. Create `skills/<skill-name>/SKILL.md`.
2. Validate its frontmatter and instructions.
3. Run `bash scripts/install.sh`.
4. Commit the change with Conventional Commits and open a pull request.
