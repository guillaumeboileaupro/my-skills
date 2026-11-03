---
name: database-migration-review
description: Independently review a SQLite-to-PostgreSQL migration for correctness, security, data integrity and operational readiness.
---
# Database migration independent review

## Agent coordination
Run only after the implementation agent has stopped. Do not modify code unless explicitly authorized. Respect one active agent and one open PR.

## Review checklist
1. Read the audit, migration plan, code diff, tests and runbook; identify undocumented assumptions.
2. Verify that SQLite backup is consistent and recoverable, secrets are excluded, and production data is not exported to external systems.
3. Review type conversions, timestamp/timezone normalization, booleans, decimal/float precision, BLOB handling, collations, constraints, views, triggers, FTS and indexes.
4. Check concurrency behavior, transaction boundaries, connection pooling, locking, retries and SQL injection defenses.
5. Verify row-level parity evidence, foreign keys, sequences, representative regression tests, staging rehearsal and query performance.
6. Challenge cutover/rollback claims, especially divergent writes after switching to PostgreSQL.
7. Report findings ordered by severity with file/line evidence and required remediation. Distinguish observed failures from untested risks.

## Deliverable
Independent review with blocking issues, nonblocking improvements, missing evidence and merge recommendation. Never approve or merge automatically.
