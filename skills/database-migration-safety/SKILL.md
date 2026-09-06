---
name: database-migration-safety
description: Plan, review, test, and execute database schema or data migrations with backups, compatibility, rollback, and integrity checks. Use for SQLite or server database changes and application upgrades.
---

# Database Migration Safety

Protect user data and make the migration repeatable.

- Identify the exact database, schema version, application versions, data volume, constraints, and deployment topology.
- Separate schema migration, data backfill, validation, and cleanup.
- Prefer additive compatible changes before destructive cleanup.
- Define backup, restore, rollback, retry, interruption, locking, and disk-space behavior.
- Test empty, representative, large, old-version, partially migrated, and invalid datasets.
- Validate row counts, keys, constraints, nullability, checksums or aggregates, and application reads after migration.
- Never run a production migration or destructive rollback without explicit authorization and a verified recovery path.

Run `python scripts/sqlite_preflight.py database.sqlite` for read-only integrity, size, table, and schema-version information.
