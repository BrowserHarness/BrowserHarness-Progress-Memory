#!/usr/bin/env python3
"""Local scanner for .github/workflows/*.yml|yaml against machine/github-guardrails.json.

Usage: check_github_actions_policy.py [repo_root]
In local_only_no_actions mode any workflow file is a blocking violation.
Exit 1 on blocking violations, 0 otherwise. Never runs in GitHub Actions.
"""
import json, re, sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
policy_path = Path(__file__).resolve().parent.parent / "machine" / "github-guardrails.json"
policy = json.loads(policy_path.read_text())
limits = policy["actions"]["if_ever_approved"]["limits"]
no_actions = not policy["actions"]["allowed"]

BLOCK = {
    "schedule/cron trigger": r"^\s*(schedule\s*:|-?\s*cron\s*:)",
    "persistent loop": r"while\s+(true|:)|sleep\s+infinity",
    "daemon/service": r"\b(nohup|daemon|systemctl\s+start)\b",
    "tunnel/proxy": r"\b(ngrok|cloudflared|frp|localtunnel|socks5?|mitmproxy)\b",
    "model serving": r"\b(vllm|ollama\s+serve|text-generation-server|llama-server)\b",
    "cryptomining": r"\b(xmrig|minerd|cpuminer|stratum\+tcp)\b",
}
WARN = {
    "self-hosted runner": r"self-hosted",
    "browser automation": r"\b(playwright|puppeteer|selenium|cypress)\b",
    "crawler/scraper wording": r"\b(crawl|scrap(e|er|ing))\b",
    "write-all permissions": r"permissions\s*:\s*write-all",
    "retry logic": r"\b(retry|retries|nick-invision/retry)\b",
}

blocking, warnings = [], []
files = sorted(list(root.glob(".github/workflows/*.yml")) + list(root.glob(".github/workflows/*.yaml")))
for f in files:
    rel = f.relative_to(root)
    text = f.read_text(errors="replace")
    if no_actions:
        blocking.append(f"{rel}: workflow present but mode is {policy['mode']} (Actions not allowed)")
    if not re.search(r"^\s*concurrency\s*:", text, re.M):
        blocking.append(f"{rel}: missing concurrency")
    timeouts = [int(m) for m in re.findall(r"timeout-minutes\s*:\s*(\d+)", text)]
    if not timeouts:
        blocking.append(f"{rel}: missing timeout-minutes")
    elif max(timeouts) > limits["job_timeout_minutes_max"]:
        blocking.append(f"{rel}: timeout-minutes {max(timeouts)} > {limits['job_timeout_minutes_max']}")
    for m in re.findall(r"retention-days\s*:\s*(\d+)", text):
        if int(m) > limits["artifact_retention_days_max"]:
            blocking.append(f"{rel}: artifact retention {m} days > {limits['artifact_retention_days_max']}")
    for name, pat in BLOCK.items():
        if re.search(pat, text, re.I | re.M):
            blocking.append(f"{rel}: {name}")
    for name, pat in WARN.items():
        if re.search(pat, text, re.I | re.M):
            warnings.append(f"{rel}: needs human review: {name}")

print(f"scanned {len(files)} workflow file(s) under {root}")
for w in warnings: print("WARN ", w)
for b in blocking: print("BLOCK", b)
sys.exit(1 if blocking else 0)
