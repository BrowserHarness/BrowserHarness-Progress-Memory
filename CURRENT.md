# Current State

> Human-readable view. Canonical live state is in `machine/`.

## Phase
**MVP internal smoke testing**

## Provider under test
- Groq via OpenAI-compatible
- model: `openai/gpt-oss-120b`

## Real Chrome evidence
Confirmed:
- **Current-page summary: PASS**
- **Google Docs insertion: PASS at least once**

Intermittent failure observed on the prior build:
- `Model did not return a BrowserCrew action`
- affected both direct chat/final-answer prompts and Google Docs tasks
- activity could remain at **Reading the current page**

This points to the model-output contract rather than Google Docs control itself.

## Latest fix
BrowserCrew now:
- detects Groq through its OpenAI-compatible endpoint;
- requests JSON Object Mode;
- excludes reasoning output;
- uses low GPT-OSS reasoning effort for the control loop;
- parses balanced JSON more defensively;
- performs one bounded repair retry for malformed action output.

## Latest verified build
- Head SHA: `c507d8f05916e8e016add31a0cd69aa23735b55b`
- GitHub Actions run: `36250049822`
- Result: **success**
- Typecheck: success
- Production build: success
- Extension validation: success
- ZIP packaging: success
- Artifact upload: success
- Artifact ID: `10908409160`

## Current task
**MVP-QA-001**

## Next precise action
Install the latest build, verify a direct chat response such as a 30-second AI-future script, then repeat the same Google Docs insertion command at least five times to measure reliability before continuing the remaining smoke scenarios.
