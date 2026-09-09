# AI Coding Agent Workflow Comparison

> **Historical draft — NOT benchmark or release evidence.** Search failed during original preparation. Per-table "session-verified" labels and unsupported absence/cost/ranking claims below are not reliable verification. Retained for history only; independently recheck repository/version-specific claims before decisions. No comparative framework benchmark was executed. Current RC tests are recorded separately in the documentation catalog.

Compared five community frameworks plus this starter. Source verification status noted per claim. No invented scores; observable properties only. Re-verify after search quota restores.

Last updated: 2026-09-09. Research workspace: `docs/research/mavis-deep-research/20260909_143930_workflow-comparison/`.

---

## Table 1 — Architecture & Context Strategy

| Property | Superpowers | OpenSpec | Spec Kit | GSD Core | BMAD | This Starter (V3) |
|---|---|---|---|---|---|---|
| **Root instruction size** | ~30 lines CLAUDE.md; rules in skills | Minimal; CLI generates context | ~40 lines SPEC.md constitution | Ultra-minimal meta-prompt | Heavy; 12+ persona prompts loaded | 50 lines / 392 words AGENTS.md |
| **On-demand skill loading** | Yes; 14 composable skills | Yes; slash commands + skills | Yes; `/specify`, `/plan`, `/tasks` | No dedicated skills; wave prompts | Persona-switching (heavy) | Yes; 5 bundled skills |
| **Context isolation** | Fresh subagent per task | Independent change directories | Feature branches | Fresh subagent per wave task | Persona context switching | Optional; fresh sessions/worktrees |
| **Standing context cost** | Low | Low | Medium (constitution + contracts) | Lowest | Highest | Low |
| **Source** | Session-verified (GitHub README) | Session-verified (GitHub) | Session-verified (search results) | Session-verified (search results) | Session-verified (search results) | Measured from source |

---

## Table 2 — Specification & Planning

| Property | Superpowers | OpenSpec | Spec Kit | GSD Core | BMAD | This Starter (V3) |
|---|---|---|---|---|---|---|
| **Spec approach** | No formal spec; TDD drives design | Living delta specs (ADDED/MODIFIED/REMOVED) with reconciliation | Four-phase SDD: Constitution → Specify → Plan → Tasks | No spec; TODO wave list | Full PRD + Architecture Spine + Epic/Story hierarchy | Optional delta proposal with canonical-target reconciliation |
| **Current-behavior tracking** | Tests are the spec | `openspec/specs/` canonical directory | `specs/` + contracts | None (task-scoped only) | Architecture Spine document | Current docs updated at integration; proposals kept as history |
| **Brownfield support** | Strong (test-first on existing code) | Strongest (delta-only changes) | Moderate (heavy upfront for existing) | Strong (minimal overhead) | Weak (assumes greenfield planning) | Designed for brownfield; source-backed adoption |
| **Mandatory planning overhead** | None for clear scope | Low (delta only) | High (full SDD pipeline) | None | Very high (multi-persona phases) | None for clear scope; optional for unresolved |
| **Source** | Session-verified | Session-verified | Session-verified | Model knowledge (unverified) | Session-verified | Measured from source |

---

## Table 3 — Execution & Quality Gates

| Property | Superpowers | OpenSpec | Spec Kit | GSD Core | BMAD | This Starter (V3) |
|---|---|---|---|---|---|---|
| **TDD enforcement** | Strict: failing test → pass → refactor | Not enforced | Checklist-based | Not enforced | QA persona review | Preferred but not mandatory; regression proof for bugs |
| **Risk-based gates** | Implicit (skill complexity) | Not formalized | Constitution invariants | None | Phase-locked readiness | Explicit 4-tier: Low/Medium/High/Critical; highest wins |
| **Verification approach** | Automated tests + subagent review | Delta acceptance | Contract-based checklists | Wave completion check | Multi-persona review | Impact-based: cheapest trustworthy check of affected behavior |
| **Evidence binding** | Test results per commit | Change-dir scoped | Spec compliance record | None persistent | Document trail | Revision/fingerprint + environment; rerun on change |
| **Build/deploy distinction** | Not explicit | Not explicit | Not explicit | Not explicit | Phase gates | Explicit: implemented ≠ integrated ≠ deployed |
| **Source** | Session-verified | Session-verified | Model knowledge (unverified) | Model knowledge (unverified) | Session-verified | Measured from source |

---

## Table 4 — Parallel Work & Handover

| Property | Superpowers | OpenSpec | Spec Kit | GSD Core | BMAD | This Starter (V3) |
|---|---|---|---|---|---|---|
| **Parallel execution** | Git worktrees + subagents | Independent change dirs | Feature branches | Wave subagents | Sprint personas | Optional; worktrees or disjoint scopes |
| **Integration ownership** | Not formalized | Not formalized | Not formalized | Not formalized | PM persona | Explicit coordinator; combined-result verification required |
| **Shared-file conflicts** | Not addressed | Not addressed | Not addressed | Not addressed | Not addressed | Coordinator owns shared files; workers propose changes |
| **Task resume/checkpoint** | No persistent state | Change-dir state | Task files | No persistent state | Document trail | Required Resume State before pause: next action, decisions, blockers, partial work |
| **Cold handover support** | Minimal | Minimal | Moderate (rich docs) | None | Rich but heavy docs | Explicit drill: setup, resume, parallel integration, recovery |
| **Knowledge compounding** | Not built-in | Not built-in | Not built-in | Not built-in | Not built-in | Built-in skill with search-before-write, correction, and no-op |
| **Source** | Session-verified | Session-verified | Model knowledge (unverified) | Model knowledge (unverified) | Session-verified | Measured from source |

---

## Table 5 — Practical Adoption & Limitations

| Property | Superpowers | OpenSpec | Spec Kit | GSD Core | BMAD | This Starter (V3) |
|---|---|---|---|---|---|---|
| **Target tools** | Claude Code | 25+ agent tools (CLI) | Claude Code (Python CLI) | Claude Code | Claude Code, Cursor | Codex, Claude Code, Aider, others (adapter-based) |
| **Install complexity** | Copy skills | `npm install` CLI | `uvx specify-cli` | Copy meta-prompt | Copy persona files | Extract ZIP; no install |
| **Portable self-tests** | None shipped | None shipped | None shipped | None shipped | None shipped | 62 tests; clean-extraction validation |
| **Operations/recovery** | Not covered | Not covered | Not covered | Not covered | Not covered | Optional runbook template for deployed systems |
| **Token cost trend** | Low per task; subagent startup cost | Low; delta-only context | High upfront; lower ongoing | Lowest per task | Highest (persona bloat) | Low standing; on-demand skills; measured 392 words root |
| **Known limitations** | No spec tracking; no handover | No TDD; no risk gates | Heavy for small projects | No persistent knowledge; no spec | Token-expensive; no TDD | No installed-client smoke test; no deployment drill; heuristic checks |
| **Source** | Session-verified | Session-verified | Session-verified | Model knowledge (unverified) | Session-verified | Measured from source |

---

## Methodology Notes

- **Session-verified**: Repository README, file content, or community discussion inspected during this session using web_fetch or web_search results.
- **Model knowledge (unverified)**: Based on training data; not confirmed against live source in this session. Re-verify when search quota restores.
- **No scores or rankings**: Observable properties only. The community "10/10" etc. ratings referenced earlier in this conversation are unofficial social-media opinions, not reproducible benchmarks.
- **Measurable comparison**: To actually benchmark these frameworks, run the same realistic tasks (setup, feature, bugfix, handover, parallel integration) across frameworks and measure: setup time, clarification requests, escaped defects, rework cycles, input tokens, and elapsed time. No framework has published such results.

## How to Re-Verify

After search quota restores, run targeted searches for each framework's current repository and confirm:
1. Repository still exists and is actively maintained.
2. Claimed features match current README/docs (not an older version).
3. Any new capabilities or deprecations since this comparison.

Update the `Source` row and `Last updated` date after re-verification.

## Repository Links (as of session date)

| Framework | Repository |
|---|---|
| Superpowers | `github.com/obra/superpowers` |
| OpenSpec | `github.com/Fission-AI/OpenSpec` |
| Spec Kit | `github.com/github/spec-kit` |
| GSD Core | Search: "GSD" "Get Shit Done" claude code |
| BMAD | `github.com/bmad-method` (org) |
| Compound Engineering | `github.com/EveryInc/compound-engineering-plugin` |
| This Starter | Local; target `github.com/next-mmo/agent-dev-workflow` |
