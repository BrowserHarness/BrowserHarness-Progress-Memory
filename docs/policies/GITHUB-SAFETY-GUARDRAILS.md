# GitHub Safety Guardrails

Canonical for all BrowserHarness agents. Machine form: `machine/github-guardrails.json`. Local checker: `scripts/check_github_actions_policy.py`.

## Operating model (user decision, 2026-10-04)
GitHub is source control and collaboration only, not compute.
- **No GitHub Actions, no workflows.** Do not create or modify `.github/workflows/*`. Tests, builds, linting and evals run locally.
- **Work locally, sync in batches.** Commit locally, then `git push` / `git pull` when a unit of work is done. Do not use the GitHub API to write files, one call per file.
- Agents, schedulers, crawlers, queues, model inference and automation run locally or on the designated operational runtime, never on GitHub.
- Heavy tests (crypto, fuzz, stress, benchmarks, browser e2e) run locally.

Mode: `local_only_no_actions`. Only the user can change it.

## Circuit breaker
If GitHub returns a 403 or 429 about restriction, suspension, abuse controls or rate limiting:
1. stop GitHub writes and automatic retries;
2. record the exact error;
3. do not work around it (no alternate accounts, orgs, runners or workflows);
4. keep working locally and commit locally;
5. get human approval before resuming GitHub writes.
This overrides "keep working until done".

## Bulk limits
- At most 20 GitHub write operations per task (a push counts as one).
- More than 3 repositories mutated in one task needs human approval.
- No automated starring, following, comment spam or bulk repo creation.
- Prefer one PR per unit of work over many small pushes.

## Needs explicit human approval
New or changed workflows, schedules, self-hosted runners, workflow secrets, Pages for production, guardrail changes, and any exception. An agent cannot approve its own exception. Exceptions are written to `exceptions/github/<date>-<name>.md`, must have an expiry, and must name the rollback.

## If Actions is ever approved
Restricted CI only: lint, format, type check, unit tests, light build. Timeout at most 15 minutes, concurrency set, read-only permissions, no schedule, no retries, artifacts at most 3 days. Run `scripts/check_github_actions_policy.py` first.

## Pages
Not for commercial production without review and approval.

## Resilience
Source must not live only on GitHub. Keep a local clone of every repo with full history. Mirroring and backups run locally, never as an Actions job.
