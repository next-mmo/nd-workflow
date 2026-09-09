# Change Proposals

Use [PRD template](../../.agents/templates/PRD.md) only for unresolved product scope. Clear implementation tasks reuse approved requirements.

- Record canonical target, baseline, stable requirement IDs, acceptance, and integration owner.
- ADDED/MODIFIED/REMOVED are local change-summary headings; this starter does not implement OpenSpec CLI parsing or automatic synchronization.
- At integration, reconcile against current target and resolve concurrent conflicts before changing canonical behavior docs. Record result in task; retain proposal as history.
- Small projects update existing current docs directly; larger projects may adopt capability specs. Do not reconstruct current behavior from a stack of historical proposals.

Lifecycle: `draft` (unapproved), `approved`, `in-progress` (including integrated but deployment pending), `shipped` (release evidence recorded), `archived` (superseded/abandoned). For non-deployable documentation deliverables, record completion scope explicitly rather than invent deployment.
