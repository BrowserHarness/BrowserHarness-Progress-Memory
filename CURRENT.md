# Current State

> Human-readable view. Canonical live state is in `machine/`.

## Phase
**BrowserCrew v0.1 MVP — automated complete, manual acceptance pending**

## Product status
v0.1 feature development is frozen.

The canonical product repo now reports:
- automated implementation: **COMPLETE**
- automated testing: **COMPLETE**
- real-Chrome manual acceptance: **PENDING**
- public release: **BLOCKED only by the final manual acceptance gate**

Do **not** start v0.2 feature work until manual acceptance is completed or a genuine acceptance blocker is found.

## Final verified product state
- Product SHA: `44fe5752af1f7956ec1fcf59a1a2604cbf33a84c`
- GitHub Actions run: `36262805588`
- Result: **success**
- TypeScript: **PASS**
- Unit/regression tests: **63/63 PASS across 14 files**
- Production build: **PASS**
- MV3 validation: **PASS**
- MVP automated contract gate: **PASS**
- ZIP packaging: **PASS**
- Artifact upload: **PASS**
- Artifact ID: `10912383198`
- Artifact digest: `sha256:76c7b5f01c436d07329170a9ab8c79f4e2026edf5f1f14f83c3a1eaaefdd5d3a`

## MVP capabilities now implemented
- Chat-first MV3 side panel.
- Direct chat separated from browser-agent execution.
- OpenAI, Anthropic, NVIDIA, and OpenAI-compatible provider paths.
- Automatic model discovery where supported.
- Model capability classification.
- Separate Chat + Agent health probes.
- Multiple saved model connections.
- Primary + one validated Fallback with recoverable-only failover.
- Single browser agent with retained multi-tab evidence.
- 11 browser tools.
- Observe → decide → act → verify runtime.
- Bounded execution, stale recovery, and duplicate-action protection.
- Pause and Stop.
- Consequential-action approvals.
- Optional all-sites and custom-endpoint permissions.
- Google Docs site adapter.
- Vision screenshot evidence handoff.
- Watch Me workflow persistence/replay.
- Local task-history UI with privacy control.
- System/light/dark appearance.
- Privacy, terms, support, Web Store permission baseline, and temporary package icons.
- Machine-checkable automated MVP contract gate.

## QA boundaries
Automated evidence:
`BrowserCrew/browsercrew/docs/qa/MVP-AUTOMATED-GATE.md`

Final manual gate:
`BrowserCrew/browsercrew/docs/qa/MVP-SMOKE-TEST.md`

## Current task
**MVP-MANUAL-001 — ready, not started**

## Next precise action
When the user decides to test, use the focused real-Chrome acceptance checklist. Until then, preserve this exact v0.1 state and do not expand scope.
