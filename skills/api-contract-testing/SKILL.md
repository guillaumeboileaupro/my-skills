---
name: api-contract-testing
description: Test HTTP API contracts across schemas, status codes, errors, persistence, and frontend consumers. Use when creating, changing, reviewing, or debugging REST APIs and their clients.
---

# API Contract Testing

Treat the contract as observable behavior, not only a route list.

- Inventory methods, paths, authentication, request schemas, response schemas, status codes, headers, pagination, and error shapes.
- Test valid, boundary, malformed, missing, unauthorized, conflicting, and not-found cases.
- Verify persisted state and idempotency where applicable.
- Confirm frontend assumptions against the backend source of truth.
- Detect undocumented nullable fields, renamed keys, type changes, and success responses containing errors.
- Preserve backward compatibility or document breaking changes and migration steps.
- Use isolated data and deterministic fixtures.

Run `python scripts/compare_openapi.py before.json after.json` to flag removed operations and response codes. It is a compatibility aid, not a complete semantic proof.
