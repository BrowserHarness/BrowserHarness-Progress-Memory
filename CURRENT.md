# Current State

> Human-readable view. Canonical live state is in `machine/`.

## Phase
**v0.2 Source-Audited Browser Reliability + Watch Me v2 — active**

The user supplied the shipped Kimi Browser Extension/WebBridge 2.0.22 package as a proven reference implementation. BrowserCrew is using it as a clean-room architecture/behavior reference to avoid rediscovering mature browser-agent engineering patterns. No proprietary implementation is copied verbatim.

Manual real-Chrome MVP acceptance remains required before public release, but is intentionally deferred while automated development continues.

## Latest verified product build
- Product SHA: `d2d1cc9600119ffb9c61830c3639c40eba4afc43`
- GitHub Actions run: `36335635257`
- Result: **success**
- Extension tests: **84/84 PASS across 19 files**
- Local Bridge tests: **3/3 PASS**
- TypeScript: **PASS**
- Production build: **PASS**
- MV3 validation: **PASS**
- MVP contract gate: **PASS**
- Package/upload: **PASS**
- Artifact ID: `10936324239`
- Artifact digest: `sha256:767a8252412a2c27e58abf4a13c395effd424c12c6ad6fed5ca1df1b0da62ddc`

## Source reference
Behavioral audit:
`BrowserCrew/browsercrew/docs/research/KIMI-EXTENSION-REFERENCE-AUDIT.md`

Key observed mature patterns include layered DOM/CDP control, real accessibility/backend-node refs, task sessions/tab groups, serialized state writes, load/readiness waits, background-safe focus policy, full-page bounded reading, frame isolation, trusted input, native dialog handling, richer recording evidence, network/upload/PDF tools, and adaptive workflow distillation.

BrowserCrew Core deliberately does **not** copy Kimi's broad permission envelope. Core stays least-privilege; debugger/CDP remains reserved for a separately disclosed Advanced/Bridge distribution.

## Verified source-derived improvements

### Session/navigation reliability
- One task = one session.
- Starting user tab borrowed; created tabs owned/grouped.
- Concurrent session mutations are serialized and merge against latest state.
- Navigation waits for a usable page/document and returns final redirect state.
- Session-scoped `list_tabs` / `find_tab`.

### Semantic observation and reading
- Stable `@e` refs and compact snapshots.
- Dedicated `read_page` instead of bloating every observation.
- 12k default extraction window for provider/token efficiency.
- Hard char/screen/time budgets.
- Scroll restoration.
- `next_start` continuation.
- stalled/endless-feed/budget/shadow-host signals.
- separate `#fN` frame reads.

### Rich input
- Native input/textarea value setters.
- `beforeinput` / `input` / `change` sequencing.
- stronger contenteditable insertion fallback.

### Watch Me v2 — first verified pass
- richer semantic locator metadata.
- stable step IDs/timestamps/page/scroll context.
- pointer coordinates.
- text-input debouncing instead of one action per keystroke.
- Enter/Tab key steps.
- inferred reusable workflow inputs.
- readable step descriptions.
- weighted replay matching instead of brittle exact matching.
- Enter-submit approval metadata and approval-aware replay.
- reinjection-safe content runtime; older duplicate listeners are invalidated.

### Foreground safety
- task-created tabs open in background by default.
- `find_tab` changes BrowserCrew's task target without stealing Chrome foreground.
- `switch_tab` is explicit foreground activation.
- screenshot refuses a background target instead of silently capturing another active tab.

### Local Bridge
- loopback-only daemon + pairing token.
- HTTP command relay + WebSocket extension channel.
- BrowserCrew task/session semantics and approval policy reused.
- operational CLI.
- external-agent candidate Skill `SK-BROWSER-001` is now **0.2.0 candidate**, with **15 evaluation cases** and still blocked from promotion until cross-runtime evaluation.

## Current architecture rule
- **Core:** least privilege, semantic DOM/scripting, approvals, bounded reading/recording.
- **Advanced/Bridge later:** debugger/CDP, trusted mouse/key/text, focus emulation, native dialogs, raw CDP, advanced network/PDF.
- Do not add `<all_urls>`, `unlimitedStorage`, always-on broad content scripts, or `debugger` to Core merely for parity.

## Current task
**V0.2-RELIABILITY-001 — Source-audited browser reliability and Watch Me v2**

## Next precise action
Implement **Watch Me v2 cross-page/multi-tab recording before Skill compilation**:
1. move recording ownership/state into the background/task runtime;
2. collect steps incrementally instead of only at page-local stop;
3. capture navigation/new-tab/tab-activation context;
4. re-arm the recorder after navigation;
5. enforce evidence/storage budgets;
6. preserve the final recorded step as the workflow goal/safety boundary;
7. only then compile Record/Session → candidate Skill.
