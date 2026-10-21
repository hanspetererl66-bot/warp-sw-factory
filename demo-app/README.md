# Lifecycle demo app

A tiny quote service the demo software factory works on. Start the run by
filing the issue from `scenarios/happy-path.md` with the label
`factory-ready`.

- `make test`, `make lint`, `make run`, `make smoke URL=...`
- `.github/workflows/ci.yml`: lint, tests, secret scan, CodeQL
- `.github/workflows/deploy.yml`: staging, then production behind a
  required-reviewer environment (Gate 4)
- `scripts/deploy.sh`: placeholder; it fails until wired to a hosting target

This directory is meant to live in its own repository
(`hanspetererl66-bot/lifecycle-demo-app`), which the factory definition in
`examples/08-lifecycle-demo` points at. It sits here for now so both can be
reviewed together.
