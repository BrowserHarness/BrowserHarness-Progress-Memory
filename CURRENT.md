# Current State

> Human-readable view. Canonical live state is in `machine/`.

## Phase
**v0.2 Full Browser-Agent Parity + Watch Me v2 — active**

The user explicitly set the product direction: functionality is the priority. BrowserCrew should use the proven Kimi Browser Extension/WebBridge implementation as an engineering shortcut, match the capabilities that make it reliable, and then exceed it with BrowserCrew's provider-neutral model layer, routing, Local Bridge, Skills, approvals, and stronger automated evaluation.

The old reduced-permission Core/Advanced split is retired.

## Latest verified product build
- Product SHA: `62003ecade09966635beaddc7330642f1892175e`
- GitHub Actions run: `36337556896`
- Result: **success**
- Extension tests: **96/96 PASS across 23 files**
- Local Bridge tests: **3/3 PASS**
- TypeScript: **PASS**
- Production build: **PASS**
- MV3 validation: **PASS**
- 23-tool automated contract gate: **PASS**
- Package/upload: **PASS**
- Artifact ID: `10937204939`
- Artifact digest: `sha256:7df54862f0b748829e1c509ac47e04c8614a1c96bf62d50796b6596fdaac39cf`

## Primary BrowserCrew capability envelope

### Full browser permissions
The primary BrowserCrew extension now intentionally includes:
- `debugger`
- `<all_urls>`
- `webNavigation`
- `webRequest`
- `unlimitedStorage`
- `downloads`
- `tabs`
- `windows`
- `tabGroups`
- `scripting`
- alarms / context menus / notifications / favicon / storage / side panel

These permissions are treated as product capabilities, not a separate edition.

### 23 browser tools
1. observe_page
2. read_page
3. ax_snapshot
4. navigate
5. click
6. trusted_click
7. type
8. trusted_type
9. press_key
10. trusted_key
11. scroll
12. wait
13. open_tab
14. find_tab
15. list_tabs
16. switch_tab
17. close_tab
18. screenshot
19. dialog
20. network
21. upload
22. save_pdf
23. cdp

### CDP / accessibility layer
- debugger attach/detach manager.
- Accessibility.getFullAXTree.
- backend DOM node mapped `@e` refs.
- trusted mouse input via Input.dispatchMouseEvent.
- trusted text via DOM.focus + Input.insertText.
- trusted keyboard via Input.dispatchKeyEvent.
- Emulation.setFocusEmulationEnabled for background task tabs.
- native JavaScript dialog tracking and accept/dismiss/prompt handling.
- raw CDP escape hatch.

### Network / files
- Network.enable lifecycle capture.
- request/response headers, request body and response metadata.
- Network.getResponseBody when available.
- bounded request record retention.
- DOM.setFileInputFiles upload with supplied local paths.
- Page.printToPDF + Chrome downloads.

### Existing BrowserCrew advantages retained
- provider-neutral OpenAI / Anthropic / NVIDIA / OpenAI-compatible model routing.
- model discovery and capability classification.
- separate Chat + Agent health.
- Primary + Fallback.
- direct-chat/browser-agent separation.
- task sessions and tab ownership.
- Local Bridge + pairing token.
- deterministic engine tests.
- consequential-action approvals.
- candidate Skill evaluation/promotion discipline.
- bounded read_page and token-efficient evidence.

## Source reference
`BrowserCrew/browsercrew/docs/research/KIMI-EXTENSION-REFERENCE-AUDIT.md`

The audit now reflects the full-capability direction rather than the old least-privilege split.

## External-agent Skill
- Repo: `BrowserCrew/Skills-`
- Skill: `SK-BROWSER-001`
- Version: **0.3.0**
- Status: **candidate**
- Evaluation matrix: **25 cases**
- Promotion blocker: cross-runtime execution evidence.

## Manual acceptance
Still intentionally deferred by the user. Public release will eventually require a focused real-Chrome pass, but development continues first.

## Current task
**V0.2-RELIABILITY-001 — Full browser-agent parity + Watch Me v2**

## Next precise action
Implement **Watch Me v2 cross-page/multi-tab recording**:
1. move recording ownership/state into the background runtime;
2. use webNavigation/tab/window events to record navigation and task context;
3. collect content-script steps incrementally across page reloads/navigations;
4. re-arm recording after navigation;
5. record new-tab and activation context;
6. enforce bounded recording/evidence storage;
7. preserve the final recorded step as the workflow/safety boundary;
8. only then compile Record/Session → candidate Skill.
