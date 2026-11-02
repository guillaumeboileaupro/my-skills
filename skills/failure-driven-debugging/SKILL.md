---
name: failure-driven-debugging
description: Investigate reproducible failures with bounded evidence instead of repeated broad scans.
---

# Failure-driven debugging

- Capture the exact failing command, environment and first relevant error.
- Form one falsifiable hypothesis and choose the cheapest discriminating check.
- Inspect bounded log excerpts, preserving access to complete evidence if needed.
- Do not rerun unchanged failing commands without a reason or new diagnostic signal.
- Fix the root cause; add a regression test and verify both failure and recovery paths.
- Report what was observed, what remains uncertain and the next experiment.
- Do not alter system, hardware or network settings without required authorization.
