---
id: "0002"
title: "ND Skills Ecosystem: Namespacing, Lifecycle Skills, Token-Budget Doctor Checks, and Plugin Toggles"
status: draft
last-audit: 2026-09-10
---

# Change Proposal: ND Skills Ecosystem — Namespacing, Lifecycle Skills, Token-Budget Doctor Checks, and Plugin Toggles

Use only for unresolved product scope. Local delta convention, not an OpenSpec CLI schema. Lifecycle: draft, approved, in-progress, shipped, archived; integrated but unreleased work stays in-progress with deployment pending.

## Problem and scope
- User / problem / desired outcome:
  - Problem 1: Workflow Doctor currently verifies file presence and structural references but does not inspect whether instruction and skill files are token-efficient ("token-saver") or unnecessarily bloated context hogs ("token-burner").
  - Problem 2: Skills lack uniform namespacing, risking collisions with native agent tools or external skills across target platforms (Claude Code, Cursor, Codex, Windsurf, Continue).
  - Problem 3: No standardized in-workflow skills exist to scaffold new skills, safely edit existing skills, or record concrete user bug reports and suggestions encountered during workflow usage.
  - Problem 4: Plugin bundles include a static, all-or-nothing list of skills with no mechanism for users or maintainers to toggle specific skills on or off in configuration or during build packaging.
  - Desired outcome: A cohesive skills ecosystem featuring `nd:` namespacing (with Windows NTFS-safe folder names), automated token efficiency classification in Workflow Doctor, 3 dedicated lifecycle skills (`nd:skill-creator`, `nd:skill-editor`, `nd:feedback-collector`) with per-skill feedback persistence, and configurable skill toggles in `plugin-config.json` with CLI filter support.
- In scope:
  - Doctor Token Check: Add token footprint and size threshold evaluation to `scripts/workflow_doctor.py` and `.agents/skills/nd-workflow-doctor/SKILL.md`. Classify analyzed files and project configuration into `TOKEN_SAVER` or `TOKEN_BURNER` with actionable diagnostic findings.
  - Skill Namespacing: Standardize skills with `nd:` prefix in metadata (`name: nd:<skill>`) and slash commands (`/nd:<skill>`), using hyphenated folder names (`.agents/skills/nd-<skill>/`) for cross-platform and Windows NTFS filesystem safety.
  - Three Lifecycle Skills:
    1. `nd:skill-creator`: Interactive scaffolding of new skills conforming to ND standards (frontmatter, procedures, verification).
    2. `nd:skill-editor`: Safe inspection, editing, and version auditing of existing skills without breaking structural contracts.
    3. `nd:feedback-collector`: Capture bug reports, usability frictions, and improvement suggestions while using workflows, persisting feedback to `.agents/skills/nd-<skill>/feedback/` (or `.agents/skills/feedback/` for cross-cutting items).
  - Plugin Skill Toggles: Update `plugins/plugin-config.json` schema to support enabled/disabled skill toggling and update `scripts/build_plugins.py` to support both config-driven toggles and an optional `--skills` CLI override.
  - Canonical documentation and test updates across plugins, doctor, and onboarding.
- Non-goals:
  - Creating a remote skill registry or network-based marketplace.
  - Dynamic runtime hot-reloading of skills inside host IDE processes without host reload.
  - Automatic destructive modifications to user skills without reviewed user confirmation.
  - Modifying external or third-party plugins.
- Selected requirements / open questions (clarification is not approval):
  - Selected (via questionnaire): Folder names use hyphen (`nd-<name>`); skill metadata and commands use colon (`nd:<name>`).
  - Selected (via questionnaire): Workflow Doctor checks token footprint and size thresholds for instructions and skills.
  - Selected (via questionnaire): 3 dedicated skills with feedback stored per-skill in `.agents/skills/nd-<skill>/feedback/`.
  - Selected (via questionnaire): Toggle in `plugin-config.json` with CLI filter override in `build_plugins.py`.
  - Open question 1: Exact threshold values for token-burner warnings (e.g. >2,000 estimated tokens or >8KB per skill/instruction file).
  - Open question 2: Feedback file format (e.g. timestamped Markdown logs `feedback/YYYY-MM-DD-issue.md` vs JSON Lines).
  - Open question 3: Backward compatibility alias support for existing non-prefixed slash commands during migration.

## Approval record
- Scope approval: pending (draft)
- Approver / decision date: pending
- Exact approved requirement IDs, exclusions and document revision or content hash: pending
- Approval evidence: pending explicit user decision. Questionnaire answers selected architecture and operational defaults; draft review and explicit approval required before implementation.
- Execution authorization: not authorized by default. Implementation, file renaming, code edits, and new skill creation remain unauthorized until separate explicit user instruction.
- Scope changes since approval / renewed decision needed: none (initial draft).

## Canonical targets and baseline
- Current feature/API/spec document(s), exact sections and stable requirement IDs:
  - Canonical diagnosis target: `scripts/workflow_doctor.py` and `.agents/skills/workflow-doctor/SKILL.md`
  - Canonical plugin target: `plugins/plugin-config.json`, `scripts/build_plugins.py`, `docs/PLUGINS.md`
  - Canonical skill catalog: `.agents/skills/`
  - Verification target: `tests/test_tooling.py`, `tests/test_plugins.py`
- Source baseline revision or file-state reference:
  - Git HEAD at commit `a00b26fc0a20abe4029202992629e8369c35667f`
- New capability: intended current-doc target; explicitly state no baseline exists:
  - New skills (`nd:skill-creator`, `nd:skill-editor`, `nd:feedback-collector`) have no prior baseline.
  - Token-saver/burner classification has no prior baseline in doctor.
  - Plugin toggle mechanism has no prior baseline in build scripts.
- Integration owner / related concurrent changes:
  - Integration owner: Root session coordinator.
  - Concurrent proposals: `prd-0001-benchmark-top5-nestjs-todo.md` (benchmark suite).

## Requirement changes
Use only relevant sections; each requirement has stable ID and observable scenarios. Specify full resulting behavior for modifications, not fragments dependent on old chat.

### ADDED
- REQ-SKILL-001: `nd:` Skill Namespacing and NTFS-Safe Directory Layout
  - Behavior: All skills adopt canonical naming with `name: nd:<skill-name>` in `SKILL.md` frontmatter. Directory paths under `.agents/skills/` use `nd-<skill-name>/` to avoid invalid colon (`:`) characters on Windows NTFS.
  - Given any skill in `.agents/skills/nd-<skill-name>/SKILL.md`, when parsed by doctor, validator, or plugin builder, its frontmatter `name` matches `nd:<skill-name>`.
- REQ-SKILL-002: Workflow Doctor Token-Saver vs Token-Burner Audit
  - Behavior: `scripts/workflow_doctor.py` inspects `AGENTS.md`, `CLAUDE.md`, and all `.agents/skills/*/SKILL.md` files for character count, line count, and estimated token footprint.
  - Files exceeding configured budget thresholds (e.g. >2,500 estimated tokens or >10 KB) are flagged as `TOKEN_BURNER` with the exact path, token count, and suggested compression action.
  - Projects where all instruction and skill files remain within tight budget limits receive `TOKEN_SAVER` health status.
- REQ-SKILL-003: `nd:skill-creator` Lifecycle Skill
  - Behavior: Interactive skill located at `.agents/skills/nd-skill-creator/SKILL.md` providing step-by-step guidance for authoring new ND-compliant skills.
  - Generates valid `SKILL.md` with required frontmatter (`name: nd:<name>`, `description:`), bounded procedure steps, Windows compatibility notes, and verification criteria.
- REQ-SKILL-004: `nd:skill-editor` Lifecycle Skill
  - Behavior: Interactive skill located at `.agents/skills/nd-skill-editor/SKILL.md` providing safe procedure for modifying existing skills.
  - Enforces change reviews, preserves existing contracts, prevents accidental deletion of safety constraints, and triggers validation after modification.
- REQ-SKILL-005: `nd:feedback-collector` Lifecycle Skill
  - Behavior: Interactive skill located at `.agents/skills/nd-feedback-collector/SKILL.md` to collect real-world feedback, bugs, and user suggestions while executing workflows.
  - Prompts user for context (workflow step, observed bug vs suggestion, expected behavior), formats a structured feedback record, and persists it to `.agents/skills/nd-<skill>/feedback/YYYYMMDD-HHMMSS-<slug>.md` (or `.agents/skills/feedback/` if general).
- REQ-SKILL-006: Plugin Skill Toggles in Configuration and CLI
  - Behavior: `plugins/plugin-config.json` supports an `enabledSkills` array (or per-skill boolean flags). `scripts/build_plugins.py` respects these toggles when generating platform bundles (Claude Code, Cursor, Codex, Windsurf, Continue).
  - Supports `--skills <list>` CLI argument on `scripts/build_plugins.py` to override configured skill sets at build time.

### MODIFIED
- REQ-SKILL-007: Existing Core Skills Migration to `nd:` Prefix
  - Existing: 8 core skills named without prefix (`setup-project`, `workflow-doctor`, `doc-lookup`, `task-status`, `spec-feature`, `converge-check`, `compound`, `bump-version`) in directories named `<skill>/`.
  - Modified resulting behavior: Folders renamed to `nd-<skill>/`, metadata names updated to `name: nd:<skill>`, documentation references and prompt templates updated to reference `/nd:<skill>`.
- REQ-SKILL-008: Workflow Doctor Inspection Contract
  - Existing: `workflow_doctor.py` inspects file existence, missing links, UNSET templates, Superpowers references, and adoption journal. Returns `status`, `project`, `missing`, etc.
  - Modified resulting behavior: Result payload includes `token_efficiency: {"status": "TOKEN_SAVER"|"TOKEN_BURNER", "total_estimated_tokens": int, "file_breakdown": [...], "warnings": [...]}`. Script flags attention if any core instruction file is a token burner.

## Design impact and decisions
- Components, data ownership, contracts, and trust boundaries touched:
  - Touches `.agents/skills/` directory tree (renaming and 3 new skills).
  - Touches `scripts/workflow_doctor.py` and `scripts/build_plugins.py`.
  - Touches `plugins/plugin-config.json` schema and platform provider manifest generation.
  - Touches unit tests in `tests/test_tooling.py` and `tests/test_plugins.py`.
- Selected approach / rejected alternatives / consequences:
  - Selected: Hyphen in folder names (`nd-name`), colon in metadata (`nd:name`). Rejected: Colons in folder names (rejected due to Windows NTFS fatal error).
  - Selected: Token footprint thresholds in doctor. Rejected: Pure configuration check (rejected because it misses actual file content bloat).
  - Selected: Three distinct skills with per-skill feedback directory. Rejected: Single monolithic skill manager (rejected to keep individual skill contexts bounded and token-efficient).
  - Selected: Toggle in `plugin-config.json` with CLI `--skills` override. Rejected: Config-only or CLI-only (rejected because maintainers need both checked-in defaults and ad-hoc bundling).
- Link significant decision record only when warranted: N/A.

## Acceptance and delivery
- [ ] All skills in `.agents/skills/` prefixed with `nd-` in folder names and `nd:` in `SKILL.md` frontmatter.
- [ ] `scripts/workflow_doctor.py` executes read-only token footprint analysis and correctly outputs `TOKEN_SAVER` or `TOKEN_BURNER` diagnostic rating.
- [ ] `nd:skill-creator`, `nd:skill-editor`, and `nd:feedback-collector` skills created, verified against ND standards, and functional.
- [ ] `nd:feedback-collector` writes structured feedback files to `.agents/skills/nd-<target>/feedback/` without mutating skill code.
- [ ] `plugins/plugin-config.json` allows toggling active skills, and `scripts/build_plugins.py` filters bundled skills according to config and `--skills` CLI override.
- [ ] Unit tests pass for doctor token checks, plugin skill toggles, and skill namespacing across all supported platform providers.
- Risk / required approvals / rollback constraints:
  - Risk: Low-to-Medium (renaming folders touches references across docs and tests). Rollback is straightforward via git.
  - Requires explicit user approval of this PRD before any implementation work.
- Current-doc reconciliation plan: compare baseline, resolve conflicts, update canonical behavior and source/test links:
  - Update `docs/PLUGINS.md`, `docs/ONBOARDING.md`, `.agents/docs/WORKFLOW.md`, `CLAUDE.md`, `AGENTS.md`.
- Implementation, integration, and deployment gates:
  - Pre-implementation gate: User must explicitly approve this PRD draft and explicitly authorize implementation.
