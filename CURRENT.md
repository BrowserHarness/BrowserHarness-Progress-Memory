# Current State

> Human-readable view. Canonical live state is in `machine/`.

## Phase
**v0.2 Site → Skill v1 verified → Kimi-reference interaction parity — active**

Manual real-Chrome MVP acceptance remains intentionally deferred by the user. BrowserCrew development continues with functionality-first competitor parity/improvement using Kimi 2.0.22 as a shipped behavioral reference while independently implementing BrowserCrew code.

## Latest verified product build
- Verified code SHA: `bbfed3443eea22df9b0115407519836263032469`
- GitHub Actions run: `36369232137`
- Result: **success**
- Extension tests: **181/181 PASS across 38 files**
- Local Bridge tests: **3/3 PASS**
- TypeScript/build/MV3/automated contract/package gates: **PASS**
- Artifact ID: `10947964449`
- Artifact digest: `sha256:e0b48d34eecb612ef4774b9918f3bfedb89b2c2479b1034cb3cc22ffe82bc9ea`

## Verified in this milestone
- Privileged approval proof works in adaptive replay and the normal agent loop; Local Bridge/web tabs cannot mint it.
- Trusted click rejects occluded targets and proves pointer/mouse delivery before success.
- CDP screenshots support background viewport, full-page and semantic-element capture.
- Fresh AX `find` and bounded `evaluate` are available.
- Network evidence merges ExtraInfo headers and recovers omitted POST bodies.
- Native `select_option` is available from a fresh AX ref.
- Site → Skill v1 is functional:
  - `create` analyzes fresh AX/form/network evidence and persists candidate Skills.
  - request/header secret values are not retained in Site Skill evidence.
  - `verify` detects origin/form/field/submit drift.
  - `run` re-verifies immediately, resolves fresh semantic targets, rejects ambiguous matches and executes text/select/upload/toggle/submit recipes.
  - non-GET/risky submission uses the extension-only approval proof.
  - run parameter values are redacted from session evidence.
  - `list/get/delete` candidate library operations are available.
  - successful execution does not auto-promote the Skill.
- Primary runtime/Local Bridge surface: **27 tools**.

## Parallel blocker
`SK-BROWSER-001` v0.3.0 remains a 25-case candidate evaluation requiring a real external agent runtime paired to Local Bridge. Product tests do not count and cross-runtime results must never be fabricated. This does not block independent engineering.

## Current task
**V0.2-KIMI-INTERACTION-PARITY-001 — Kimi-reference interaction parity**

## Next precise action
Implement the next proven browser primitives:
1. hover using real CDP pointer placement;
2. drag/drop with real pointer sequence and post-action verification;
3. richer key chords/sequences/modifiers;
4. await-user-action/human handoff for login, CAPTCHA, 2FA or explicit manual steps;
5. register each capability in the same BrowserCrew/Bridge contract and deterministic test gate.

After interaction parity, move to versioned Skill revisions, evaluation comparison, explicit promotion and rollback so BrowserCrew exceeds Kimi's opaque refinement model.

## Standing direction
- Functionality first.
- Kimi is a proven baseline, not the ceiling.
- Do not weaken browser capability merely to minimize permissions.
- Independently implement BrowserCrew code; use shipped competitor behavior to avoid rediscovering solved browser-agent problems.
- Preserve BrowserCrew's stronger task ownership, approvals, deterministic testing, provenance, candidate/evaluation lifecycle, versioning and rollback direction.
