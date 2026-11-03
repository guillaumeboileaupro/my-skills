---
name: database-migration-validation
description: Verify SQLite-to-PostgreSQL migrations with integrity, data parity, sequences, functional regression and rollback checks.
---
# Database migration validation

## Procedure
1. Capture consistent source and destination snapshots or stop writes before comparing. Record versions and migration revision.
2. Compare table inventories and exact row counts; compare deterministic canonicalized row digests keyed by stable primary key, accounting for intended type conversions, NULL, timestamps, binary data and float precision.
3. Check PK/unique constraints, foreign-key violations, orphan references, CHECK constraints, NULL/default behavior, views, triggers, indexes and sequences. Verify next inserted ID does not collide.
4. Exercise representative CRUD, transactions, concurrent writes, upserts, pagination, filtering, ordering, timezone and error cases using the project's existing tests.
5. Compare query plans for critical paths (EXPLAIN ANALYZE in a safe environment); avoid unbounded production scans.
6. Test rehearsal rollback before cutover. If PostgreSQL accepted writes after cutover, flag reverse synchronization as mandatory before rollback.
7. Report PASS/FAIL/SKIP with commands, expected/observed results and limitations. Never mark unexecuted tests PASS.

## Acceptance
No unexplained missing/duplicate rows, broken references or behavior changes. All required tests green, documented recovery plan and explicit approval before switching production traffic.

## Deliverable
Concise verification matrix, unresolved risks, go/no-go recommendation and time spent.
