# AGENTS.md — Progress-Memory

- Maintain continuity without duplicating canonical specifications.
- Point to the repository that owns each truth.
- Update live state only from evidence.
- Tool-call success is not proof of completion; verify resulting state.
- Keep blockers concrete and actionable.
- Never store secrets, API keys, session tokens, private user data, or browsing history here.
- If machine state and prose disagree, machine state wins until reconciled.
- Every handoff ends with one precise next action.

## GitHub safety circuit breaker

All GitHub-capable agents follow `docs/policies/GITHUB-SAFETY-GUARDRAILS.md` and `machine/github-guardrails.json`.

- Mode is `local_only_no_actions`: no GitHub Actions, and never create or modify `.github/workflows/*`.
- Work locally and test locally. Commit locally, then push or pull once per unit of work. Do not write files through the API one by one.
- If GitHub returns a 403/429 about restriction, suspension, abuse controls or rate limiting: stop writes, stop retries, record the exact error, do not work around it, keep working locally, and get human approval before resuming.
- At most 20 GitHub writes per task; more than 3 repos in one task needs approval.
- Agents, crawlers, schedulers and heavy tests run locally, not on GitHub.
- Agents cannot approve their own guardrail exceptions.
