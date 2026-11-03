---
name: sqlite-to-postgres
description: Implement a reproducible and reversible SQLite-to-PostgreSQL schema, data and application migration with controlled cutover.
---
# SQLite to PostgreSQL

## Preconditions
Read AGENTS.md/CLAUDE.md and database-schema-audit findings. Require a verified SQLite backup, PostgreSQL target credentials supplied via environment variables, approved outage window and explicit authorization before touching production. Never commit secrets or database dumps.

## Implementation
1. Create a dedicated migration branch and a single focused PR; do not merge. Prefer existing project migration tooling (Alembic, Prisma, TypeORM, Django, etc.) over parallel schema management.
2. Build explicit PostgreSQL DDL and migrations. Map SQLite affinities based on observed values: INTEGER primary keys to BIGINT/INTEGER identity where appropriate, REAL to DOUBLE PRECISION, BLOB to BYTEA, booleans to BOOLEAN only after checking data, and text dates to TIMESTAMPTZ only after validating timezone semantics. Preserve nullable/default/unique/check/foreign-key behavior.
3. Evaluate pgloader only for supported schema/data; manually migrate unsupported triggers, views, FTS, collations, generated columns and application-specific behavior. Avoid blindly copying SQLite SQL.
4. Import into a new empty PostgreSQL database or staging schema. Use explicit table ordering or deferred FK validation where safe. Preserve original IDs, then synchronize identity sequences to max(id) without overwriting existing records.
5. Update application drivers, connection pooling, parameter placeholders, transaction semantics, upsert syntax, error handling and SQL dialect. Never expose PostgreSQL directly to untrusted clients.
6. Test a rehearsal migration against a sanitized or approved snapshot. Keep original SQLite database unchanged.
7. For cutover, stop writes, take a final consistent SQLite backup, run final migration, validate, switch configuration and monitor. Rollback means stopping writes to PostgreSQL and switching back only if no divergent writes occurred; otherwise require a reconciliation plan. Never claim a lossless rollback without it.

## Deliverable
Versioned migrations, documented commands, environment examples without credentials, repeatable rehearsal and cutover/rollback runbook. No destructive operations or automatic production cutover.
