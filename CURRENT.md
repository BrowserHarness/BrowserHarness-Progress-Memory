# Current State

> Human-readable view. Canonical live state is in `machine/`.

## Phase
**v0.1.1 focused acceptance**

## Internal stability work completed
BrowserCrew v0.1.1 now implements the reliable model + agent runtime planned for this build:

- multiple saved provider/model connections;
- automatic model discovery where supported;
- model capability classification: Chat, Agent, Vision, Embedding, Reranker, Audio, Image, Unknown;
- separate Chat and Agent health probes;
- explicit Primary + one Fallback route;
- fallback only on recoverable failures such as 429, 5xx, timeout, empty response or malformed agent output;
- no silent failover on authorization failures;
- direct chat fully separated from browser-agent planning;
- compact page observations capped at 6,000 normalized visible-text characters and 250 interactive elements;
- duplicate-action loop protection and bounded execution;
- explicit `generic-web` / `google-docs` site-adapter boundary;
- Google Docs semantic editor target retained behind the adapter;
- **Auto** header state when Primary + Fallback routing is configured;
- internal-first stability gate required before user acceptance.

## Verified build
- Head SHA: `7a50b165684e3ff4118691495af2250cbb4eed7a`
- GitHub Actions run: `36258863723`
- Result: **success**
- TypeScript: **PASS**
- Unit tests: **36/36 PASS across 9 files**
- Production build: **PASS**
- MV3 extension validation: **PASS**
- ZIP package: **PASS**
- Artifact upload: **PASS**
- Artifact ID: `10911493020`
- GitHub artifact digest: `sha256:835dab18c1a1819fcc20c4985b96adafb3aa4acf9c6a71aba1318a66bca2f0b2`

## Canonical contracts
- `BrowserCrew/browsercrew/ROADMAP.md` now includes **v0.1.1 — Reliable Model + Agent Runtime**.
- `BrowserCrew/browsercrew/machine/capabilities.json` defines model roles, validation, and fallback policy.
- `BrowserCrew/browsercrew/docs/qa/STABILITY-GATE.md` remains the mandatory internal-first verification policy.

## Current task
**MVP-QA-001 — focused real-Chrome acceptance**

## Next precise action
Install the exact verified v0.1.1 candidate. In Settings, validate one model with **Test Chat + Agent & save**; optionally configure one validated fallback. Then run exactly one direct-chat prompt and one browser task. Do not return to patch-by-patch user testing.
