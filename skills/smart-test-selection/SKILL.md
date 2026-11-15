---
name: smart-test-selection
description: Select focused tests during development without skipping mandatory final gates.
---

# Smart test selection

- Identify affected modules, dependency boundaries and relevant test files from the diff.
- Run the smallest reliable tests first; include regression and error-path tests.
- Expand testing if interfaces, shared infrastructure or dependencies changed.
- Run all repository-mandated quality, coverage, security and CI gates before completion.
- Report targeted and full results separately, including skipped tests and environment limitations.
- Never use test selection to bypass a required gate or claim hardware validation.
