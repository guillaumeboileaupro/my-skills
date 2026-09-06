#!/usr/bin/env bash

set -euo pipefail

repository_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_directory="$repository_root/skills"
target="${1:-all}"

install_into() {
    local agent_name="$1"
    local destination_root="$2"

    mkdir -p "$destination_root"

    for skill_directory in "$source_directory"/*; do
        [[ -d "$skill_directory" ]] || continue

        skill_name="$(basename "$skill_directory")"
        destination="$destination_root/$skill_name"

        if [[ -e "$destination" || -L "$destination" ]]; then
            if [[ -L "$destination" && "$(readlink -f "$destination")" == "$(readlink -f "$skill_directory")" ]]; then
                printf '%s already installed: %s\n' "$agent_name" "$skill_name"
                continue
            fi

            printf '%s skipped existing path: %s\n' "$agent_name" "$destination" >&2
            continue
        fi

        ln -s "$skill_directory" "$destination"
        printf '%s installed: %s\n' "$agent_name" "$skill_name"
    done
}

case "$target" in
    all)
        install_into "Codex" "${CODEX_HOME:-$HOME/.codex}/skills"
        install_into "Claude" "${CLAUDE_HOME:-$HOME/.claude}/skills"
        ;;
    codex)
        install_into "Codex" "${CODEX_HOME:-$HOME/.codex}/skills"
        ;;
    claude)
        install_into "Claude" "${CLAUDE_HOME:-$HOME/.claude}/skills"
        ;;
    *)
        printf 'Usage: %s [all|codex|claude]\n' "$0" >&2
        exit 2
        ;;
esac
