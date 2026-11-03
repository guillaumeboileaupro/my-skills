---
name: database-schema-audit
description: Audit a SQLite database and application SQL before a PostgreSQL migration, producing an evidence-based inventory and compatibility report.
---
# Database schema audit

## When to use
Before planning or changing a SQLite-to-PostgreSQL migration.

## Procedure
1. Read repository instructions (AGENTS.md, CLAUDE.md, local rules) and identify database paths, ORM, migrations, environments, and test commands.
2. Work read-only. Never copy production data into chat, logs, commits, or external services. Obtain approval before accessing sensitive data.
3. Inspect SQLite schema via sqlite_master and PRAGMA table_info, table_xinfo, foreign_key_list, index_list, index_xinfo, user_version and integrity_check. Inventory views, triggers, virtual tables, FTS, CHECK constraints, collations and generated columns.
4. Find all SQL statements and connection handling in application code. Identify SQLite-specific syntax: PRAGMA, INSERT OR REPLACE, INSERT OR IGNORE, last_insert_rowid, ?, AUTOINCREMENT, rowid, datetime functions, JSON and FTS.
5. Inspect actual data shapes without exporting sensitive values: nulls, integer booleans, text timestamps/timezones, BLOBs, non-UTF8 data, orphan keys, duplicate candidate unique keys and numeric range violations.
6. Record table row counts, schema hashes, dependency versions, expected concurrency and outage budget. Use transactionally consistent snapshots for changing databases.
7. Produce a compatibility matrix with evidence, severity, conversion rule, and validation query. Mark uncertain assumptions explicitly.

## Deliverable
A concise audit report with table/row inventory, incompatibilities, proposed type mapping, risks, migration prerequisites and time estimate. Do not modify code or databases in this skill.
