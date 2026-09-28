# Current State

> Human-readable view. Canonical live state is in `machine/`.

## Phase
**v0.2 Kimi-reference parity hardening verified → Site → Skill v1 — active**

BrowserCrew now has verified Record → Skill, Session → Skill, Watch Me v3 adaptive replay, privileged trusted-input approval proof, Kimi-style trusted-click verification, background/full-page/element CDP screenshots, semantic AX `find`, bounded page `evaluate`, and high-fidelity network request evidence. Manual real-Chrome MVP acceptance remains intentionally deferred by the user.

## Latest verified product build
- Verified code SHA: `3b6c7567f5f20124bedbe30abdac45005c777756`
- GitHub Actions run: `36367934722`
- Result: **success**
- Extension tests: **160/160 PASS across 32 files**
- Local Bridge tests: **3/3 PASS**
- TypeScript: **PASS**
- Production build: **PASS**
- MV3 validation: **PASS**
- automated BrowserCrew contract gate: **PASS**
- package/upload: **PASS**
- Artifact ID: `10947872942`
- Artifact digest: `sha256:7329bb00a869ff475f1e5bc270446d945a44b5624e6353e1bab46b353b5a1923`

## Newly verified Kimi-reference reliability work
- Adaptive replay can carry one-shot approval proof only from the BrowserCrew extension page; Local Bridge/content pages cannot mint it.
- Newly risky AX-only trusted actions can prompt and retry exactly once after explicit approval.
- Trusted click rejects an occluded target with an `elementFromPoint` hit test.
- Trusted click verifies pointer/mouse delivery to the intended target before reporting success.
- Screenshot uses `Page.captureScreenshot` for background viewport, full-page and semantic-element clip modes.
- `find` searches a fresh accessibility tree by semantic text/role.
- `evaluate` exposes bounded JSON-safe page-context inspection while raw CDP remains available.
- Network capture merges `Network.requestWillBeSentExtraInfo` wire headers and recovers omitted POST bodies through `Network.getRequestPostData`.
- Local Bridge/browser runtime surface is now **25 tools**.

## Skill state
- Record → Skill verified at `9a21949333de565e5a77001ce1f39da95e346657`.
- Session → Skill verified at `595af74d2a947a8ef7cc41d29c0f119cc9798dfa`.
- Watch Me v3 adaptive replay remains verified.
- Generated Skills remain candidate-only and require evaluation before promotion.
- `SK-BROWSER-001` remains **v0.3.0 candidate** with 25 evaluation cases.

## Parallel blocker
The actual 25-case `SK-BROWSER-001` cross-runtime evaluation still requires a real external agent runtime paired to BrowserCrew Local Bridge. Product unit tests do not count and results must not be fabricated. This blocker no longer stops independent product engineering.

## Current task
**V0.2-SITE-SKILL-001 — Site → Skill v1**

## Next precise action
Build the first usable Site → Skill vertical slice using the newly verified primitives:
1. collect fresh site identity + AX evidence;
2. inspect forms/interactive structure with bounded `evaluate`;
3. capture relevant high-fidelity network evidence;
4. normalize this into inspectable SiteSkillEvidence;
5. compile a candidate executable Skill recipe with parameters, provenance and safety boundary;
6. verify the recipe/evidence contract with deterministic tests;
7. keep the generated Skill candidate-only; never auto-promote.

## Standing product direction
- Functionality first.
- Kimi 2.0.22 is a proven competitor/reference baseline, not BrowserCrew's ceiling.
- Use its shipped behavior/architecture to shorten discovery and testing, independently implement BrowserCrew, and improve reliability/autonomy/reuse.
- Do not weaken browser capability merely to minimize permissions.
- Preserve BrowserCrew's provider neutrality, task-session ownership, explicit approvals, deterministic tests, Skill evaluation/versioning and future rollback.
