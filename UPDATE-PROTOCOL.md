# Update Protocol

Update Progress-Memory when verified events change:
- current workstream/task;
- blocker;
- release/deployment state;
- repository ownership/routing;
- incident/security state;
- material roadmap state.

Do not update it for every commit.

## Sequence
1. Verify canonical/external state.
2. Update the canonical owner.
3. Update machine state here.
4. Reconcile the human summary.
5. Add a handoff only when continuity requires it.

## Handoff minimum
Verified state; completed work; material files/PRs/SHAs; failed checks/blockers; constraints; one precise next action.
