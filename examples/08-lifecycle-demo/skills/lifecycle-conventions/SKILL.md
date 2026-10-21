---
name: lifecycle-conventions
description: Branch, commit, and test conventions for the lifecycle demo app.
---
# Lifecycle conventions

- Branch: `factory/<issue-number>-<slug>`.
- Commits: imperative mood, one per plan task, reference the issue.
- `make test` and `make lint` must pass before a PR leaves draft.
- Money is integer cents; never floats.
- Every endpoint that changes data checks the caller's role.
- No secrets in code; read configuration from environment variables.
