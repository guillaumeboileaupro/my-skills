#!/usr/bin/env bash
set -euo pipefail

docker compose "$@" config --quiet
printf 'Compose configuration is valid\n'
docker compose "$@" config --services
docker compose "$@" ps --all 2>/dev/null || true
