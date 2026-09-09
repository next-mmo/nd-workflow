# Task Tracking

Use [task template](../../.agents/templates/TASK.md) for multi-step work. Genuinely low-risk single-turn fixes skip task records; sensitive changes never qualify merely by size.

- `todo-NNNN-slug.md`: planned.
- `wip-NNNN-slug.md`: active, one per executor session; different tasks can run concurrently.
- `blocked-NNNN-slug.md`: blocker and next owner/action visible at top.
- `done/done-NNNN-slug.md`: required scope verified, delivery state explicit.

Coordinate unique IDs, exact task path, owner, write scope, and integration owner before work. Update path on rename; never infer identity from first wildcard match. Reuse safe existing state without assuming Git has a first commit.

Update Resume State before interruption or ownership transfer, not only completion. See [handover drill](../HANDOVER.md). Coordinator owns shared files and combined-result verification; branch isolation alone does not prove integration.

Archive only after required scope passes. Pending deployment, skipped checks, and stale evidence remain explicit. Historical session IDs are provenance, not a current contact method.
