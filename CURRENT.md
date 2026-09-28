# Current State

> Human-readable view. Canonical live state is in `machine/`.

## Phase
**v0.2 Kimi-reference interaction parity verified → versioned Skill lifecycle active**

Manual real-Chrome MVP acceptance remains intentionally deferred by the user. BrowserCrew development continues functionality-first, using shipped Kimi 2.0.22 behavior as a proven competitor reference while independently implementing BrowserCrew code and preserving BrowserCrew's stronger evidence/evaluation model.

## Latest verified product build
- Product/docs head: `4153f5292d485abb382e31280d2c5a960e2b83f1`
- Verified interaction-parity code head: `0204ecbf78b5be694267cf7a9dc0ea04afaeb9f4`
- GitHub Actions run: `36371599324`
- Result: **success**
- Extension tests: **201/201 PASS across 42 files**
- Local Bridge tests: **3/3 PASS**
- TypeScript/build/MV3/automated contract/package gates: **PASS**
- Artifact ID: `10949531602`
- Artifact digest: `sha256:ab86431440c0f7829562d63e45c388376393f83a6e2b11e92e336cff075e1560`

## Newly verified
- Kimi-reference interaction parity is complete:
  - real CDP hover with target verification;
  - drag/drop with source + target hit-tests, held-button pointer path and down/up delivery proof;
  - `send_keys` with OS-aware `Mod`, Alt/Ctrl/Cmd/Meta/Shift, named navigation keys, F1-F12, chords, sequences and repeat 1-100;
  - orchestrator-only `await_user_action` human handoff for login, CAPTCHA/human verification, 2FA and explicit manual consent.
- Human handoff waits 10 seconds for natural navigation before showing takeover UI; navigation remains a live resume path while the card is visible.
- “I’m done, continue” resumes and forces a fresh page observation; “Cancel task” stops.
- Manual handoffs are recorded as non-executable session evidence and never advance `boundary_action_id`.
- Session → Skill compilation rejects sessions crossing a manual-handoff precondition rather than pretending a human-only gate is automated.
- Built-in planner surface: **31 tools**.
- Local Bridge surface: **30 tools**; `await_user_action` remains intentionally orchestrator-only.

## Parallel blocker
`SK-BROWSER-001` v0.3.0 still requires a real external agent runtime paired to Local Bridge for its 25-case cross-runtime evaluation. Product/unit tests do not count and results must never be fabricated. This remains parallel and does not block independent engineering.

## Current task
**V0.2-SKILL-LIFECYCLE-001 — Versioned Skill lifecycle + refinement**

## Next precise action
Replace destructive Site Skill candidate updates with an inspectable versioned store:
1. immutable revision records with parent links;
2. backward-compatible migration/read of existing v1 candidates;
3. latest revision lookup plus revision history;
4. explicit active-revision pointer in the data model;
5. no promotion yet without evaluation evidence.

Then add evaluation comparison, explicit promotion, refinement candidates and rollback.

## Standing direction
- Functionality first.
- Kimi is a proven baseline, not the ceiling.
- Independently implement BrowserCrew code rather than copying competitor source.
- Do not weaken browser capability merely to minimize permissions.
- Preserve task ownership, approvals, deterministic testing, provenance, candidate/evaluation lifecycle, explicit promotion and rollback.
