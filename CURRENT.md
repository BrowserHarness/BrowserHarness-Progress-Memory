# Current State

> Human-readable view. Canonical live state is in `machine/`.

## Phase
**MVP internal smoke testing**

## Confirmed real-Chrome evidence
- Groq connected through the OpenAI-compatible adapter.
- Current-page summary: **PASS**.
- Google Docs insertion: **PASS at least once**.
- Groq subsequently returned HTTP 429 due provider-side TPM rate limit.

## NVIDIA / model discovery
BrowserCrew now has:
- first-class **NVIDIA** provider option;
- NVIDIA hosted NIM base URL: `https://integrate.api.nvidia.com/v1`;
- automatic model discovery through compatible `/models` endpoints;
- searchable Material model selector;
- manual model-ID fallback;
- the same discovery mechanism for generic OpenAI-compatible providers such as Groq.

## Latest verified build
- Head SHA: `00b54cd7a3462801ae8fd8d586f80394cdc7a48f`
- GitHub Actions run: `36251248051`
- Result: **success**
- Typecheck: success
- Production build: success
- Extension validation: success
- ZIP packaging: success
- Artifact upload: success
- Artifact ID: `10908779632`

## Current task
**MVP-QA-001**

## Next precise action
Install the NVIDIA/model-discovery build, choose NVIDIA, enter an NVIDIA API key, confirm the live model list loads automatically, select a model and save it, then rerun direct chat and Google Docs insertion.
