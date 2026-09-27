# Current State

> Human-readable view. Canonical live state is in `machine/`.

## Phase
**v0.2 Skill Compiler Verified → Adaptive Replay — active**

BrowserCrew now has verified **Record → Skill** and **Session → Skill** pure compiler contracts. Cross-page/multi-tab Watch Me remains verified, the primary extension retains the full Kimi-class browser-control substrate, and manual real-Chrome acceptance remains intentionally deferred by the user.

## Latest verified product build
- Verified code SHA: `595af74d2a947a8ef7cc41d29c0f119cc9798dfa`
- Product main docs/machine head: `079f4d32e1feb53c6550284354137a1fd126e272`
- GitHub Actions run: `36341514622`
- Result: **success**
- Extension tests: **133/133 PASS across 27 files**
- Local Bridge tests: **3/3 PASS**
- TypeScript: **PASS**
- Production build: **PASS**
- MV3 validation: **PASS**
- automated BrowserCrew contract gate: **PASS**
- package/upload: **PASS**
- Artifact ID: `10938903183`
- Artifact digest: `sha256:7a9209f88aed5ad3e2ba7ed2496c6d0f0136d8acb0cac738d816ec98865b0d10`

## Record → Skill — verified
- Input: `SavedWorkflow v3`.
- Output: portable candidate Skill contract.
- Raw tab IDs become logical tab refs; source IDs remain provenance only.
- Recorded text becomes explicit reusable parameters.
- Navigation/tab-open/tab-activate/tab-close evidence becomes an ordered browser-context plan.
- `boundary_step_id` is enforced as the maximum demonstrated action boundary.
- Approval semantics, source provenance and deterministic evaluation cases are preserved.
- Generated Skills are **candidate only** and cannot auto-promote.
- Verified compiler SHA: `9a21949333de565e5a77001ce1f39da95e346657`.

## Session → Skill — verified
- `runBrowserTask` emits `BrowserTaskSessionEvidence v1` bound to the real BrowserCrew task-session ID/title.
- Only successfully executed actions enter the evidence trace.
- Each action carries before/after browser context, target semantics and approval evidence.
- Stale failed attempts do **not** advance the learned boundary.
- Actions denied by approval do **not** enter the learned procedure.
- Raw task tab IDs become logical refs in the candidate plan.
- Transient element IDs/semantic refs are evidence hints only; replay must re-observe.
- Typed values become reusable parameters.
- Password values and local upload paths become sensitive parameters without retained compiled examples.
- `boundary_action_id` is the final successful demonstrated action ceiling.
- Generated Session Skills are **candidate only** and require evaluation before promotion.

## Browser capability baseline retained
Primary BrowserCrew still includes the verified 23-tool runtime, debugger/CDP, AX backend-node refs, trusted input, dialogs, network capture, upload, PDF, raw CDP, bounded read_page, task sessions, full Local Bridge surface, provider-neutral routing and Primary/Fallback.

## External-agent Skill
`SK-BROWSER-001` remains **v0.3.0 candidate** with 25 evaluation cases. It is not promoted without cross-runtime evidence.

## Completed task
**V0.2-SKILL-COMPILER-001 — Record and Session → Skill compiler**

## Current task
**V0.2-ADAPTIVE-REPLAY-001 — Adaptive multi-tab workflow replay**

## Next precise action
Implement the pure adaptive replay planner/executor:
1. consume the verified candidate browser plan;
2. create a fresh logical-tab → BrowserCrew task-tab mapping;
3. never reuse recorded source tab IDs as live IDs;
4. resolve recorded target hints from fresh DOM/AX semantic evidence;
5. bind reusable Skill parameters at runtime;
6. execute only through the existing BrowserCrew tool surface;
7. preserve consequential-action approval rules;
8. stop at the demonstrated boundary;
9. verify navigation/tab/mutation results;
10. add deterministic multi-tab, stale-target, parameter and approval tests before UI wiring.
