#!/usr/bin/env bash

set -euo pipefail

repository_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_directory="$repository_root/skills"
codex_skills_directory="${CODEX_HOME:-$HOME/.codex}/skills"

mkdir -p "$codex_skills_directory"

for skill_directory in "$source_directory"/*; do
    [[ -d "$skill_directory" ]] || continue

    skill_name="$(basename "$skill_directory")"
    destination="$codex_skills_directory/$skill_name"

    if [[ -e "$destination" || -L "$destination" ]]; then
        if [[ -L "$destination" && "$(readlink -f "$destination")" == "$(readlink -f "$skill_directory")" ]]; then
            printf 'Already installed: %s\n' "$skill_name"
            continue
        fi

        printf 'Skipped existing path: %s\n' "$destination" >&2
        continue
    fi

    ln -s "$skill_directory" "$destination"
    printf 'Installed: %s\n' "$skill_name"
done
