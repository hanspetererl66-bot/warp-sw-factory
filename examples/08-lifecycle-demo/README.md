# 08 - Lifecycle demo

A demo factory that walks one feature request through the whole lifecycle,
with a human in control at every decision that matters.

| Stage | Agent | Artifact | Human gate |
|---|---|---|---|
| Requirements | `requirements` | Spec PR: stories, Gherkin, open questions | Gate 1: spec approval |
| Plan | `planner` | `plans/<item>.md`: tasks, risks, tests, rollback | Gate 2: plan approval |
| Code | `implementer` (Claude Code) | Commits and tests on the spec branch | none |
| Review | `reviewer` (Codex) | Findings report, loops back on blockers | none |
| Human decision | foreman hand-off | Diff, evidence, risk summary | Gate 3: merge |
| Deploy | `deployer` | Staging, smoke test, production | Gate 4: `approve-deploy` label and production environment reviewer |

The `gate-compliance` scorer samples every foreman run and fails any run in
which an agent approved, merged, or promoted on a human's behalf.

Target app: [`demo-app`](../../demo-app). Demo scripts:
[`happy-path`](../../demo-app/scenarios/happy-path.md) and
[`planted-flaw`](../../demo-app/scenarios/planted-flaw.md).

## Make it yours

1. Move `demo-app` into its own repository and point `factory.yaml` and the two
   automations at it (they use `hanspetererl66-bot/lifecycle-demo-app`).
2. Add managed secrets `ANTHROPIC_API_KEY` and `OPENAI_API_KEY`.
3. In the app repository, create the `staging` and `production` environments;
   add required reviewers to `production`. Set `STAGING_URL`,
   `PRODUCTION_URL`, and `DEPLOY_TOKEN`, and implement `scripts/deploy.sh`.
4. Create the labels `factory-ready`, `approve-deploy`, and
   `factory:Lifecycle Demo`.

Validation: `python3 scripts/validate_factory_files.py examples/08-lifecycle-demo`
(needs network access to the Warp schema service).
