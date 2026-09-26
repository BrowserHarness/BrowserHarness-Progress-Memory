# Current State

> Human-readable view. Canonical live state is in `machine/`.

## Phase
**MVP internal smoke testing**

## Real Chrome evidence
Provider:
- Groq via OpenAI-compatible
- model: `openai/gpt-oss-120b`

Confirmed:
- **Current-page summary: PASS**

Failures found and now patched for retest:
- **Google Docs writing** — initial DOM-only typing could not handle Docs; candidate rich-editor + Docs text-event fallback packaged.
- **Stop control** — initial placement/cancellation was insufficient; sticky header Stop now aborts the in-flight model request.
- **Content script unavailable after extension reload** — BrowserCrew now attempts on-demand reinjection on normal HTTP(S) pages instead of immediately reporting them as protected.

## Latest verified candidate build
- Head SHA: `15fb2ebc6b81b2cd91ec5b4818b08b9fb8db08b5`
- GitHub Actions run: `36249400786`
- Result: **success**
- Install: success
- Typecheck: success
- Production build: success
- Extension-output validation: success
- ZIP package: success
- Artifact upload: success
- Artifact ID: `10908522721`

## Current task
**MVP-QA-001**

## Next precise action
Install the latest candidate build, retry Google Docs without manually refreshing the tab, confirm the header Stop control aborts immediately, then continue the remaining smoke scenarios.
