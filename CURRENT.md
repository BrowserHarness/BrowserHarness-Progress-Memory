# Current State

> Human-readable view. Canonical live state is in `machine/`.

## Phase
**MVP internal smoke testing**

## Confirmed
- Groq connection through OpenAI-compatible adapter: **PASS**
- Current-page summary: **PASS**
- Google Docs insertion: **PASS at least once**
- Groq later returned HTTP 429 due provider-side TPM rate limit

## NVIDIA + automatic model discovery
BrowserCrew now includes:
- first-class **NVIDIA** provider;
- NVIDIA hosted NIM base URL `https://integrate.api.nvidia.com/v1`;
- automatic model discovery from compatible `/models` endpoints;
- searchable Material model selector;
- manual model-ID fallback;
- automatic discovery for generic OpenAI-compatible endpoints such as Groq;
- provider-switch credential clearing to avoid sending a previous provider's key to a new provider.

## Latest verified build
- Head SHA: `8976a1d52f30a6dc8621a368574b80638f9ce118`
- GitHub Actions run: `36251379178`
- Result: **success**
- Typecheck: success
- Production build: success
- Extension validation: success
- ZIP packaging: success
- Artifact upload: success
- Artifact ID: `10908774990`

## Current task
**MVP-QA-001**

## Next precise action
Install the latest build, choose NVIDIA, enter an NVIDIA API key, confirm the live model list loads automatically, choose a model, save it, then rerun the direct-chat and Google Docs tests.
