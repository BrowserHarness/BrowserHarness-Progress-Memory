# Current State

> Human-readable view. Canonical live state is in `machine/`.

## Phase
**v0.2 Browser Reliability + Bridge Foundation — active**

The user explicitly reopened development before the final manual MVP acceptance pass. Manual acceptance remains required before public v0.1 release, but it is intentionally deferred while BrowserCrew is improved using proven browser-agent patterns.

## Latest verified build
- Product SHA: `4188403ee33f95cb35e75f48bfcfbdc324fb7182`
- GitHub Actions run: `36333800978`
- Result: **success**
- Extension unit/regression tests: **73/73 PASS across 16 files**
- Local Bridge daemon tests: **3/3 PASS**
- TypeScript: **PASS**
- Production build: **PASS**
- MV3 validation: **PASS**
- MVP contract gate: **PASS**
- Packaging/upload: **PASS**
- Artifact ID: `10936717457`
- Artifact digest: `sha256:27005c0c93f7f41a1ac4de99434daf8fc49ed335727b99aad65dfc7924a0b517`

## Verified post-MVP improvements

### Task sessions + semantic browser model
- One browser task = one task session.
- The user's starting tab is borrowed, not owned.
- Tabs BrowserCrew creates are task-owned and grouped in Chrome.
- Borrowed/unrelated user tabs are protected from session cleanup.
- Session-scoped `list_tabs` and `find_tab`.
- Stable semantic `@e` references and compact accessibility snapshots.

### Rich input reliability
- Native input/textarea value setters for framework-controlled fields.
- `beforeinput`, `input`, and `change` sequencing.
- Stronger range-based contenteditable insertion fallback.

### BrowserCrew Local Bridge v0.1
- Separate local daemon workspace.
- Loopback-only HTTP/WebSocket transport.
- Pairing-token authentication.
- `GET /status` and authenticated `POST /command`.
- Extension protocol/version handshake.
- Heartbeat/reconnect path compatible with modern MV3 service-worker WebSockets.
- External session IDs map directly to BrowserCrew task sessions.
- Bridge commands use the same 13 BrowserCrew tools and semantic refs.
- Risky bridge click/Enter actions return `APPROVAL_REQUIRED`.
- Settings UI for enable/address/token/connection state.
- CLI: `start`, `status`, `stop`, `restart`, `logs`, `pair`.
- Machine-readable contract: `BrowserCrew/browsercrew/machine/bridge-protocol.json`.
- Human docs: `BrowserCrew/browsercrew/docs/architecture/LOCAL-BRIDGE.md`.

## CDP / debugger decision
Chrome does not allow the `debugger` permission to be optional. Core BrowserCrew remains least-privilege. Trusted CDP/input control is reserved for a separately disclosed **BrowserCrew Advanced/Bridge** distribution.

## MVP status
- implementation: **complete**
- automated gate: **complete**
- manual real-Chrome acceptance: **pending and intentionally deferred by the user**
- public release: still requires that final manual pass

## Current task
**V0.2-RELIABILITY-001 — Browser reliability and Local Bridge foundation**

## Next precise action
Create a reusable external-agent BrowserCrew Bridge skill/adapter (usable by Hermes/Codex/Claude-class local agents), then build Record → Skill / Session → Skill / Site → Skill on top of the stable task-session and bridge protocol.
