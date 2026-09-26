# Current State

> Human-readable view. Canonical live state is in `machine/`.

## Phase
**MVP internal stability hardening**

## Process change
BrowserCrew will no longer use the user as the primary debugger for every small runtime patch.

New order:
1. coherent fix/build;
2. regression coverage;
3. TypeScript;
4. unit tests;
5. production build;
6. MV3 validation;
7. ZIP packaging;
8. one focused user acceptance check only after all gates pass.

Canonical policy:
`BrowserCrew/browsercrew/docs/qa/STABILITY-GATE.md`

## Architecture change
BrowserCrew now has two runtime paths.

### Direct chat
Normal conversation/writing/brainstorming:
- deterministic local routing;
- no current-page observation;
- no browser-agent JSON protocol;
- plain provider chat response.

### Browser agent
Explicit page/tab/site/document/cursor/browser tasks:
- page observation;
- bounded agent loop;
- structured actions;
- mutation verification and approval gates.

## Provider reliability
- provider/model must pass **Test & save connection** before BrowserCrew will use it;
- successful validation is stamped into local config;
- stale/unvalidated provider configs cannot execute tasks;
- NVIDIA/Groq/OpenAI-compatible model discovery supported when `/models` exists;
- provider failures, 429s, empty responses and timeouts surface explicitly;
- explicit user Stop is distinct from provider/network interruption.

## Regression gate
Latest verified candidate:
- Head SHA: `12ce556f460487966cbf96c925866a9d3bc30d97`
- GitHub Actions: `36255741358`
- Result: **success**
- TypeScript: **PASS**
- Unit tests: **19/19 PASS across 3 files**
- Production build: **PASS**
- Extension validation: **PASS**
- ZIP package: **PASS**
- Artifact upload: **PASS**
- Artifact ID: `10910941366`

## Current task
**MVP-QA-001**

## Next rule
Do not ask for repeated user testing. Continue internal hardening first; the next user acceptance request should be minimal and only after the provider/model health check passes inside Settings.
