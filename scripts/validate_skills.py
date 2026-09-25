"""Validate the YAML metadata of every skill in a library."""

from __future__ import annotations

from pathlib import Path

import yaml


def validate_skills(skills_root: Path) -> list[str]:
    problems: list[str] = []
    skill_dirs = sorted(path for path in skills_root.iterdir() if path.is_dir())
    if not skill_dirs:
        problems.append("no skill directories found")

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            problems.append(f"{skill_dir}: missing SKILL.md")
            continue

        lines = skill_file.read_text(encoding="utf-8").splitlines()
        if not lines or lines[0].strip() != "---":
            problems.append(f"{skill_file}: missing opening frontmatter delimiter")
            continue

        try:
            end = next(index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---")
        except StopIteration:
            problems.append(f"{skill_file}: missing closing frontmatter delimiter")
            continue

        try:
            metadata = yaml.safe_load("\n".join(lines[1:end]))
        except yaml.YAMLError as error:
            problems.append(f"{skill_file}: invalid YAML frontmatter: {error}")
            continue

        if not isinstance(metadata, dict):
            problems.append(f"{skill_file}: frontmatter must be a mapping")
            continue

        for required in ("name", "description"):
            if required not in metadata:
                problems.append(f"{skill_file}: missing frontmatter key '{required}'")

    return problems


if __name__ == "__main__":
    root = Path("skills")
    errors = validate_skills(root)
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Validated {sum(path.is_dir() for path in root.iterdir())} skills")
