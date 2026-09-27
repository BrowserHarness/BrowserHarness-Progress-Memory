# Current State

> Human-readable view. Canonical live state is in `machine/`.

## Phase
**v0.2 Watch Me v2 Verified → Skill Compiler — active**

BrowserCrew now uses the full Kimi-class browser-control substrate in the primary extension and has a verified cross-page/multi-tab Watch Me recorder. Manual real-Chrome acceptance remains intentionally deferred by the user while automated development continues.

## Latest verified product build
- Product SHA: `440a27cbe26e00ffb341c844d9ac81d8b5ab2586`
- GitHub Actions run: `36338958528`
- Result: **success**
- Extension tests: **107/107 PASS across 25 files**
- Local Bridge tests: **3/3 PASS**
- TypeScript: **PASS**
- Production build: **PASS**
- MV3 validation: **PASS**
- 23-tool contract gate: **PASS**
- Package/upload: **PASS**
- Artifact ID: `10938625438`
- Artifact digest: `sha256:612f168d1ca338e912265c4c92d37d041a2d3801bed2abdb349903c8e702c213`

## Watch Me v2 — verified cross-page/multi-tab recorder

### Ownership
- Recording state lives in the background service worker.
- Durable active state is stored in `chrome.storage.session`.
- Content scripts no longer own the recording array; they stream actionable steps to the background.
- Serialized writes prevent simultaneous navigation/tab/input events from losing data.

### Cross-page behavior
- Top-frame `webNavigation.onCommitted` produces navigation evidence.
- `webNavigation.onCompleted` automatically re-arms the content recorder after navigation/reload.
- The active recording therefore survives document replacement.

### Multi-tab / multi-window behavior
- Tabs opened by a recorded tab are adopted.
- Existing or manually created tabs become part of the recording when the user activates them during Watch Me.
- Newly adopted tabs are armed immediately.
- Tab-open, activation and closure context is retained.
- Action steps receive their actual `tab_id`.

### Workflow v3 evidence
Saved workflows can now contain:
- actionable click/type/key steps;
- navigation events;
- tab-open/tab-activation/tab-close events;
- inferred reusable text inputs;
- `boundary_step_id` identifying the last accepted demonstrated action;
- recording summary with tab/event/drop/size evidence.

### Evidence budgets
- max actionable steps: **1,000**
- max browser-context events: **2,000**
- max tabs: **50**
- approximate recording evidence budget: **2 MB**
- oversize evidence increments drop counters but cannot move the workflow boundary.

### Lifecycle durability
- `WATCH_STATUS` exposes active background recording state.
- Reopening/reloading the side panel restores the Recording UI.
- Stop disarms all tracked tabs, flushes pending text entry, and atomically returns the completed recording.

## Browser capability baseline retained
Primary BrowserCrew still includes:
- 23 browser tools;
- debugger/CDP;
- Accessibility.getFullAXTree backend-node refs;
- trusted mouse/text/key input;
- focus emulation;
- native dialogs;
- network inspection/response bodies;
- file upload;
- PDF export;
- raw CDP;
- full Local Bridge surface;
- provider-neutral model routing and Primary/Fallback.

## External-agent Skill
`SK-BROWSER-001` remains **v0.3.0 candidate** with 25 evaluation cases. It is not promoted without cross-runtime evidence.

## Current task
**V0.2-SKILL-COMPILER-001 — Record and Session → Skill compiler**

## Next precise action
Implement **Record → Skill** from verified SavedWorkflow v3:
1. normalize action + browser-context evidence;
2. infer reusable variables/inputs;
3. compile navigation/tab evidence into a portable browser-context plan;
4. preserve `boundary_step_id` as the demonstrated maximum action boundary;
5. attach provenance and source workflow evidence;
6. generate candidate evaluation cases;
7. register the output as **candidate only**;
8. then add Session → Skill using BrowserCrew task-session evidence.
