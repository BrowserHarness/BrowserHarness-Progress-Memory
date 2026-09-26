# Current State

> Human-readable view. Canonical live state is in `machine/`.

## Phase
**MVP internal smoke testing**

## Completed
- **FOUNDATION-001** — organization operating layer complete across all 20 repositories.
- **RUNTIME-001** — first BrowserCrew v0.1 vertical slice implemented and build-verified.

## Verified BrowserCrew v0.1 slice
The `BrowserCrew/browsercrew` main branch now contains:
- Chrome Manifest V3 side-panel application;
- Material UI chat-first shell with Poppins headings and Inter body/UI;
- current-tab context;
- OpenAI, Anthropic and OpenAI-compatible connection settings stored locally;
- semantic page observation;
- navigate/click/type/press-key/scroll/wait/tab/screenshot tool routing;
- bounded single-agent observe → act → re-observe loop;
- structured in-chat activity;
- pause / resume / stop;
- local task history storage;
- approval gates for consequential labels, POST-form submit controls and Enter-submit paths;
- basic current-page Watch Me → save local workflow → replay;
- password fields excluded from Watch Me capture/replay;
- CI packaging of a loadable extension ZIP.

## Latest verified build
- Head SHA: `14258fa704489dbdb9a86acc31809810a05da624`
- GitHub Actions run: `36247804894`
- Result: **success**
- Install: success
- Typecheck: success
- Production build: success
- Extension-output validation: success
- ZIP package: success
- Artifact upload: success
- Artifact ID: `10908361241`
- Artifact: `browsercrew-extension`

CI verifies build/package integrity. It does **not** prove real Chrome/provider behavior.

## Current blockers
None recorded. Real Chrome acceptance testing is now the active task rather than a blocker.

## Current task
**MVP-QA-001** — load the packaged extension in real Chrome and execute `docs/qa/MVP-SMOKE-TEST.md`.

## Next precise action
Install the packaged build in Chrome, connect a test provider, run smoke scenario 1 (**Summarize this page**), and fix the first genuine runtime failure before expanding scope.
