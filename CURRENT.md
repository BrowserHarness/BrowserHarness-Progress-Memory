# Current State

> Human-readable view. Canonical live state is in `machine/`.

## Phase
**v0.2 Adaptive Replay Verified → SK-BROWSER-001 Cross-Runtime Evaluation — active**

BrowserCrew now has verified **Record → Skill**, **Session → Skill**, and **Watch Me v3 adaptive replay** contracts. Watch Me v3 recordings can be replayed from Chat through compilation plus adaptive execution; legacy v2 workflows retain exact single-tab replay. Manual real-Chrome MVP acceptance remains intentionally deferred by the user.

## Latest verified product build
- Verified code SHA: `0ad7117761a3f0d65987a6919e4eb3555f595678`
- Product main docs/machine head: `235f3180150caf7eaef6e5f0e65c28c6fe207c6f`
- GitHub Actions run: `36342347225`
- Result: **success**
- Extension tests: **143/143 PASS across 29 files**
- Local Bridge tests: **3/3 PASS**
- TypeScript: **PASS**
- Production build: **PASS**
- MV3 validation: **PASS**
- automated BrowserCrew contract gate: **PASS**
- package/upload: **PASS**
- Artifact ID: `10938894460`
- Artifact digest: `sha256:f3eff151ca632562924a91d7a4922033d664718cfcfc0765e259da521c2b8498`

## Skill compiler — verified
- Record → Skill verified at `9a21949333de565e5a77001ce1f39da95e346657`.
- Session → Skill verified at `595af74d2a947a8ef7cc41d29c0f119cc9798dfa`.
- Generated Skills remain candidate-only and require evaluation before promotion.

## Watch Me v3 adaptive replay — verified
- SavedWorkflow v3 flows through Record → Skill compilation before replay.
- Logical tab refs are remapped into a fresh BrowserCrew task session.
- Recorded source tab IDs are never executed.
- Recorded tab-open evidence creates distinct replay-owned background tabs.
- Fresh DOM semantics are resolved first; fresh AX evidence is the escalation path.
- Ambiguous equal-best targets are rejected rather than guessed.
- Recorded element IDs / semantic refs are evidence hints only, never current selectors.
- Reusable parameters support runtime overrides; Chat currently uses recorded defaults.
- Recorded and current DOM approval metadata remain in force.
- Execution stops at the demonstrated `boundary_step_id`.
- Watch Me v3 Replay in Chat uses this adaptive path; legacy v2 exact replay remains intact.

## Known adaptive replay limits
- Session-derived candidate Skills are compiled but do not yet have a user-facing runner.
- Chat does not yet expose an edit-before-run parameter form.
- A newly risky AX-only target can still be rejected by the trusted-input safety layer after the replay UI prompt; trusted-input approval-proof hardening remains explicit roadmap work.

## External-agent Skill
`SK-BROWSER-001` remains **v0.3.0 candidate** with 25 evaluation cases. Product-side runtime evidence is green, but cross-runtime Skill execution evidence is still required before promotion.

## Completed task
**V0.2-ADAPTIVE-REPLAY-001 — Adaptive multi-tab workflow replay**

## Current task
**V0.2-SK-BROWSER-EVAL-001 — SK-BROWSER-001 cross-runtime execution evaluation**

## Next precise action
1. refresh the Skill registry/evaluation source evidence to the latest verified BrowserCrew build;
2. add a machine-readable cross-runtime evaluation-result schema/runbook;
3. execute all 25 cases through each available real external agent runtime over the existing Local Bridge;
4. capture per-case result/evidence/failure details;
5. keep `SK-BROWSER-001` candidate unless real cross-runtime evidence satisfies promotion;
6. do not substitute product unit tests for the missing cross-runtime execution evidence.
