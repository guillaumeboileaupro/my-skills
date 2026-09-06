---
name: docker-compose-operations
description: Inspect, start, diagnose, and safely reset Docker Compose applications with multiple services, health checks, volumes, and networks. Use for local or demo environment operations and Compose failures.
---

# Docker Compose Operations

Preserve persistent state unless deletion is explicitly requested.

- Resolve the exact Compose files, profiles, project name, environment files, external volumes, and external networks.
- Run `docker compose config` before mutation and inspect service dependencies and health checks.
- Start only the required services and verify readiness, not merely container state.
- Diagnose from container status, health output, service logs, ports, mounts, DNS, and dependency order.
- Pin the Compose project name for repeatable demos and maintenance.
- Provision declared external resources explicitly.
- Never use `down -v`, prune commands, or broad deletion as a routine fix.
- Preserve certificate, database, upload, and user-data volumes during resets.

Run `bash scripts/compose_preflight.sh [compose arguments]` for a read-only configuration and resource check.
