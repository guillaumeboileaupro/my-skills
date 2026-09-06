# Skills

Central repository for personal Codex skills.

## Structure

Each skill lives in its own directory under `skills/`:

```text
skills/
`-- conventional-commits-pr/
    |-- SKILL.md
    `-- agents/
        `-- openai.yaml
```

## Install for Codex

Run:

```bash
bash scripts/install.sh
```

The installer creates symbolic links in `${CODEX_HOME:-$HOME/.codex}/skills` without replacing existing files or directories.

## Add a skill

1. Create `skills/<skill-name>/SKILL.md`.
2. Validate it with Codex's `quick_validate.py`.
3. Run `bash scripts/install.sh`.
4. Commit the change with Conventional Commits and open a pull request.
