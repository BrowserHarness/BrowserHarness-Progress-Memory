# Current State

> Human-readable view. Canonical live state is in `machine/`.

## Phase
**v0.2 Browser Reliability + Bridge Foundation — active**

The user explicitly reopened development before the final manual MVP acceptance pass. Manual acceptance remains required before public v0.1 release, but it is intentionally deferred while BrowserCrew is improved using proven browser-agent patterns.

## Latest verified build
- Product SHA: `35a66fa0fbd5610dcee0f2b023186af080770a49`
- GitHub Actions run: `36333144524`
- Result: **success**
- Unit/regression tests: **69/69 PASS across 15 files**
- TypeScript: **PASS**
- Production build: **PASS**
- MV3 validation: **PASS**
- MVP contract gate: **PASS**
- Packaging/upload: **PASS**
- Artifact ID: `10936581674`
- Artifact digest: `sha256:52821b3d90b4a7ea4f94196b74cb0ca9f820f919688e648f79cddc23a5a723a5`

## Verified post-MVP improvements
### Task sessions + semantic browser model
- One browser task = one task session.
- The user's starting tab is borrowed, not owned.
- Tabs BrowserCrew creates are task-owned and grouped in Chrome.
- Borrowed/unrelated user tabs are protected from task-session close operations.
- Added session-scoped `list_tabs` and `find_tab`.
- Regular interactive controls expose stable semantic `@e` references.
- Observations include a compact accessibility-style snapshot.

### Rich input reliability
- Form fills use native input/textarea value setters for framework-controlled fields.
- BrowserCrew emits `beforeinput`, `input`, and `change` events.
- Contenteditable/rich-editor insertion now has a stronger range-based fallback.

## CDP / debugger decision
Chrome does not allow the `debugger` permission to be optional. BrowserCrew therefore keeps the core extension least-privilege. Trusted CDP/input control will be designed as a separately disclosed **BrowserCrew Advanced/Bridge** distribution instead of silently expanding core permissions.

## MVP status
- implementation: **complete**
- automated gate: **complete**
- manual real-Chrome acceptance: **pending and intentionally deferred by the user**
- public release: still requires that final manual pass

## Current task
**V0.2-RELIABILITY-001 — Browser reliability and Local Bridge foundation**

## Next precise action
Implement the BrowserCrew Local Bridge protocol for external agents, carrying the same task session IDs, owned/borrowed tab semantics, semantic `@e` refs, approval rules, and BrowserCrew tool envelopes across the local connection.
