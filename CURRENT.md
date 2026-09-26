# Current State

> Human-readable view. Canonical live state is in `machine/`.

## Phase
**MVP internal smoke testing**

## Completed
- **FOUNDATION-001** — organization operating layer complete.
- **RUNTIME-001** — first BrowserCrew v0.1 vertical slice implemented and build-verified.

## Real Chrome evidence
Provider tested successfully:
- Groq through the OpenAI-compatible adapter
- model: `openai/gpt-oss-120b`

Confirmed:
- **Current-page summary: PASS**

First failures found:
- **Google Docs writing: FAIL on the first tested build**
- **Stop control discoverability/cancellation: FAIL on the first tested build**

Both now have packaged candidate fixes awaiting real-Chrome retest.

## Candidate fixes
- Generic `contenteditable` editor support.
- Google Docs semantic **Document content** target backed by its hidden `.docs-texteventtarget-iframe`.
- No new Chrome `debugger` permission added.
- Sticky red Stop icon appears in the header while a task is running.
- Stop aborts the active provider/model request immediately rather than waiting for it to return.

## Latest verified candidate build
- Head SHA: `41dbeaf406bcfe28799b9781321bfbbefdab86fa`
- GitHub Actions run: `36249044932`
- Result: **success**
- Install: success
- Typecheck: success
- Production build: success
- Extension-output validation: success
- ZIP package: success
- Artifact upload: success
- Artifact ID: `10908303645`

## Current task
**MVP-QA-001**

## Next precise action
Install the latest candidate build, retest **Google Docs writing** and the **header Stop control**, then continue the remaining MVP smoke scenarios.
