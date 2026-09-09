# Task: Specification for ND Skills Ecosystem, Doctor Token Audit, and Plugin Toggles

Use for multi-step work; skip for genuinely low-risk single-turn changes. Keep this file current before pause, handover, or completion. A session checklist is not a substitute for this durable file. A pre-approval drafting checkpoint is allowed; it authorizes no implementation.

## Goal and scope
- Mode: specification-only.
- Outcome / why: Define specification and architecture for `nd:` skill namespacing (NTFS-safe), Workflow Doctor token-saver vs token-burner analysis, 3 lifecycle skills (`nd:skill-creator`, `nd:skill-editor`, `nd:feedback-collector`) with per-skill feedback persistence, and skill toggles in `plugin-config.json` with CLI filter support.
- Requirement or issue / exact draft or approved PRD path and version: `docs/prd/prd-0002-nd-skills-ecosystem-doctor-token-and-toggles.md` (version: draft, last-audit: 2026-09-10).
- Scope approval evidence / approver / date / exclusions: pending explicit user decision. Questionnaire answers selected architecture and decisions; draft PRD presented and awaiting review.
- Execution authorization: not authorized. Code modifications, folder renaming, skill authoring, and test updates remain unauthorized until separate explicit user instruction.
- In scope / non-goals:
  - In scope: PRD drafting, task checkpoint, defining requirement IDs (REQ-SKILL-001 through REQ-SKILL-008), acceptance criteria.
  - Non-goals: Implementation, file moves, running build scripts during specification mode.
- Risk and required gates: Low-to-Medium risk. Requires explicit PRD scope approval, followed by separate execution authorization.

## Ownership and integration
- Exact task path (update on rename): `docs/tasks/wip-0009-spec-nd-skills-lifecycle-and-doctor.md`
- Owner / team; optional session ID: root maintainer; session `mvs_9f3b6aa9e9da447e9a3a96dda33086bd`.
- Branch/worktree and base revision (or non-Git/unborn workspace state): `a00b26fc0a20abe4029202992629e8369c35667f`.
- Owned write paths: `docs/prd/prd-0002-nd-skills-ecosystem-doctor-token-and-toggles.md`, `docs/tasks/wip-0009-spec-nd-skills-lifecycle-and-doctor.md`.
- Dependencies / outstanding workers: none.
- Integration owner / shared files / merge order: root maintainer.

## Plan and acceptance
- Next steps within authorized mode (draft/review steps before implementation authorization):
  1. Present draft PRD `docs/prd/prd-0002-nd-skills-ecosystem-doctor-token-and-toggles.md` to user.
  2. Confirm open questions (token-burner threshold values, feedback file format, backward compatibility aliases).
  3. Stop and await explicit user approval of the specification.
  4. Upon approval, split into concrete implementation tasks (doctor token check, skill renaming & namespacing, lifecycle skills authoring, plugin toggle configuration & CLI filter, test updates).
- [ ] Draft PRD written following `.agents/templates/PRD.md` with approval record.
- [ ] Drafting task checkpoint saved following `.agents/templates/TASK.md`.
- [ ] Implementation explicitly marked not authorized.
- Canonical behavior/architecture targets; baseline and requirement IDs:
  - PRD: `docs/prd/prd-0002-nd-skills-ecosystem-doctor-token-and-toggles.md` (REQ-SKILL-001 through REQ-SKILL-008).

## Resume State
- Updated at / author: 2026-09-10 / root maintainer.
- Completed / partial / not started:
  - Completed: User questionnaire answers received, draft PRD created, task checkpoint saved.
  - Not started: Scope approval, implementation tasks, code and skill file changes.
- Exact next action or command and working directory: Present draft to user and await explicit scope approval. Working directory: repository root.
- Current hypothesis / blockers / decision needed: Awaiting user review and explicit approval of PRD scope and requirements.
- Decisions and rejected approaches with reasons:
  - Hyphen in folder names (`nd-name`) and colon in skill metadata (`nd:name`) selected over colons in folders (NTFS compatibility on Windows).
  - Token footprint and size threshold check selected over configuration-only inspection (evaluates actual file bloat).
  - Three distinct lifecycle skills with per-skill feedback storage selected over monolithic skill manager (keeps tool context small and bounded).
  - Configuration toggles in `plugin-config.json` plus CLI `--skills` flag selected over single-mode toggling (supports both persistent settings and ad-hoc builds).
- Current revision and uncommitted work location/fingerprint: Workspace uncommitted files: `docs/prd/prd-0002-nd-skills-ecosystem-doctor-token-and-toggles.md`, `docs/tasks/wip-0009-spec-nd-skills-lifecycle-and-doctor.md`.
- Evidence still valid / invalidated and why: PRD draft matches user questionnaire selections from 2026-09-10.
- Relevant source, docs, and output paths: `docs/prd/prd-0002-nd-skills-ecosystem-doctor-token-and-toggles.md`, `docs/tasks/wip-0009-spec-nd-skills-lifecycle-and-doctor.md`.
- Successor ownership transfer / outstanding coordination: none.

## Verification and closure
- Criterion / command or inspection / result / evidence location:
  - Inspection: PRD and task checkpoint files exist on disk, contain valid Markdown and frontmatter.
- Tested state and relevant environment: Windows PowerShell, node/python standard tooling.
- Combined-state checks and integration result: Independent files; no merge conflicts with existing codebase.
- Current-doc reconciliation result / conflicts resolved: N/A for draft phase.
- Optional durable learning: N/A.
- Failed / skipped / unverified checks and reasons: Implementation not run; unauthorized in specification-only mode.
- Status: active (drafting mode complete, awaiting scope approval; implementation not authorized).
