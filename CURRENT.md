# Current State

> Human-readable view. Canonical live state is in `machine/`. Updated 2026-10-04.

## Phase
Kimi-parity gap closure, interleaved with v0.4 Task DAG + verifier workers.

## Home
GitHub org BrowserHarness. Forgejo is retired. BrowserCrew was renamed BrowserHarness; code and docs still carry `browsercrew` strings.

## Verified product build
- `BrowserHarness/BrowserHarness` main: `42d67d37530a4e7a49c3a4d982a8ab770c857a25`
- Extension tests 269/269, Local Bridge tests 16/16 (reproduced 2026-10-04)
- Manual real-Chrome acceptance still deferred; public release blocked on it.

## Mission
A harness for the browser: total automation via Chrome, Hermes-agent style. Build everything Kimi's extension has (clean-room, inspiration not copying), then exceed it.

## Current task
V0.4-TASK-DAG-VERIFIERS-001: pure scheduler `runtime/task-dag.ts` + tests first, then read-only verifier workers.

## Kimi-parity order
Executable site recipes, skill-creator workflow, conversation compaction, per-domain grants, recording-to-intent skills, selection quick-explain, outbound relay, prompt polish, rich rendering, attachment upload.

## Blocker
`SK-BROWSER-001`: 25-case cross-runtime evaluation needs a real external runtime paired to Local Bridge. Never fabricate results.

## Reports
See project files: product-status/extension-completion-2026-10-04.md and competitor-analysis/kimi-extension-2.0.22-teardown.md.

## GitHub safety
Mode `local_only_no_actions` (set by user 2026-10-04): no GitHub Actions or workflows; work and test locally, push/pull in batches. Policy in `docs/policies/GITHUB-SAFETY-GUARDRAILS.md`; checker `python3 scripts/check_github_actions_policy.py <repo>`. Reason: GitHub flagged false positives.
