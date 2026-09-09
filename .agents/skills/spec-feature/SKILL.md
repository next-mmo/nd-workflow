---
name: spec-feature
description: Feature specification and planning skill. Guides drafting a new Delta PRD in docs/prd/ and breaking it down into actionable tasks in docs/tasks/. Use when asked to "spec a new feature", "create PRD", "write spec for X", or when unresolved product scope needs definition. Skip for bug fixes or straightforward tasks.
---

# Spec Feature: Product Requirement & Planning

This skill translates feature ideas, issues, and roadmap items into clean, actionable **Delta PRDs** and task files, avoiding premature or uncontrolled coding.

---

## When to Run This Skill

- When planning new product scope, multi-component architectural additions, or features that lack clear requirements (see `.agents/docs/WORKFLOW.md`).
- When a user asks to *"design a new feature"*, *"write a PRD for X"*, or *"plan feature Y"*.
- **Reuse approved scope**: Straightforward bug fixes and localized changes do not need a duplicate PRD. Apply `AGENTS.md` risk precedence first; sensitive changes still require their risk-tier plan and verification even when small. Draft a PRD only for unresolved product scope.

---

## Step-by-Step Specification Process

### Step 1: Find current truth
1. Locate existing requirements, source, and affected architecture using catalog or targeted search. Approved scope needs no duplicate PRD.
2. Name canonical document targets, baseline revision/sections, and stable requirement IDs; new capability explicitly has no baseline. Do not use historical proposals as current behavior.
3. Coordinate unique proposal/task IDs and integration owner. Never overwrite existing files; coordinator owns shared catalog/spec updates.

### Step 2: Draft only unresolved scope
Use `.agents/templates/PRD.md`; do not embed another template here. Record outcome, non-goals, decisions, observable scenarios, relevant failure cases, and recovery constraints.
Use ADDED/MODIFIED/REMOVED only when useful. These are local summaries, not OpenSpec CLI schema. Modifications contain full resulting behavior; removals include migration effects.

### Step 3: Approve and assign
Present unresolved scope for approval before implementation. Record approval and create tasks with `.agents/templates/TASK.md`, exact ownership, dependencies, write scope, and integration order. Worker returns proposed catalog/shared-doc edits to coordinator.

### Step 4: Reconcile at integration
Compare canonical targets against recorded baseline. Resolve concurrent conflicts before applying deltas; update current docs to describe implemented behavior with source/test links and deployment state. Record reconciliation in task before closure. Keep proposal as history; `shipped` requires release evidence. Follow `.agents/docs/WORKFLOW.md` for lifecycle details.
