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

Prior intermittent failure:
- `Model did not return a BrowserCrew action`
- affected direct chat/final-answer tasks and Google Docs runs
- left **Reading the current page** spinning on failure

## Latest stability fix
BrowserCrew now:
- requests Groq JSON Object Mode;
- suppresses reasoning output;
- uses low GPT-OSS reasoning effort for the control loop;
- parses balanced JSON defensively;
- normalizes a small set of equivalent action shapes;
- performs one bounded repair retry on malformed output;
- closes the activity spinner as an error when model decision parsing fails.

## Latest verified build
- Head SHA: `27bdb56514361d7b08f2a62b8d89df9ade49b3b1`
- GitHub Actions run: `36250176492`
- Result: **success**
- Typecheck: success
- Production build: success
- Extension validation: success
- ZIP packaging: success
- Artifact upload: success
- Artifact ID: `10908643490`

## Current task
**MVP-QA-001**

## Next precise action
Install the latest stability build, first test a direct chat response such as a 30-second AI-future script, then repeat the same Google Docs insertion command at least five times and record reliability before continuing the remaining smoke scenarios.
