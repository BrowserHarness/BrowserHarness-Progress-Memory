# Current State

> Human-readable view. Canonical live state is in `machine/`.

## Phase
**MVP internal smoke testing**

## Confirmed
- Groq connection: **PASS**
- Groq current-page summary: **PASS**
- Google Docs insertion: **PASS at least once**
- Groq later hit provider-side HTTP 429 TPM rate limit
- NVIDIA provider + automatic model discovery: implementation **CI-green**

## NVIDIA first runtime test
Observed on the first NVIDIA build:
- direct chat prompts hung until manually stopped;
- Google Docs write task stayed at **Reading the current page**;
- manual stops appeared as `Stopped.`.

## Runtime fix now packaged
BrowserCrew now:
- routes the user request **before** observing the current page;
- answers normal chat/writing prompts without reading the Google Doc;
- asks for `observe_page` only when browser state is actually needed;
- bounds NVIDIA generations with `max_tokens`;
- requests JSON Object Mode;
- disables reasoning/thinking for common NVIDIA reasoning model families where supported;
- times model requests out after 30 seconds;
- retries NVIDIA HTTP 400 structured-output incompatibility once with plain OpenAI-compatible chat parameters;
- distinguishes explicit user Stop from provider/network interruption;
- surfaces empty/non-chat model responses as actionable errors.

## Latest verified build
- Head SHA: `8663c5b75aee631651bf9f3e4cb3b03e2c65fe02`
- GitHub Actions run: `36254678941`
- Result: **success**
- Typecheck: success
- Production build: success
- Extension validation: success
- ZIP packaging: success
- Artifact upload: success
- Artifact ID: `10909394225`

## Current task
**MVP-QA-001**

## Next precise action
Install the latest runtime-fix build and test, in order:
1. `hi whats your name`
2. `write 30 sec video script about ai and its future`
3. Google Docs insertion

Direct chat should no longer read the page. Browser tasks should observe only when required.
