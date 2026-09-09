# Benchmark and Tool Compatibility

[Back to README](README.md)

## Why choose ND Workflow?

**For small teams, ND offers a shared delivery policy without requiring the full planning-and-delegation loop for every change.** Keep routine work direct, raise verification requirements when risk rises, and leave a checkpoint another developer or agent can resume. Choose it for that combination—not a claim of higher coding success or broader tool support.

| Team problem | ND mechanism | Intended benefit | Evidence and limit |
|---|---|---|---|
| Small fixes trigger too much process | Low-risk, single-turn work needs a scoped edit and focused check; no mandatory PRD or delegation | Less procedural overhead on routine changes | [Root policy](AGENTS.md), [workflow](.agents/docs/WORKFLOW.md); time savings not measured |
| A tiny change hides serious risk | Highest applicable risk wins; auth, security, payments and data integrity use critical gates | Review effort follows impact, not patch size | [Risk tiers](.agents/docs/WORKFLOW.md); written policy is not runtime enforcement |
| Work disappears into chat history | Task ownership, tested state, blockers and next action survive in repository checkpoints | Easier transfer between people, sessions and tools | [Handover guide](docs/HANDOVER.md); real-team recovery success rate unmeasured |
| Adoption might overwrite existing project knowledge | Preview, reviewed merges, hash-bound apply and recovery journal | Reviewable adoption into an existing repository | [Onboarding](docs/ONBOARDING.md); manual recovery, not automatic rollback |
| A passing build gets called a shipped feature | Separate implemented, integrated and deployed states; evidence tied to affected behavior | Clearer delivery status and fewer unsupported completion claims | [Verification policy](AGENTS.md); no production-readiness certification |
| Framework-specific automation becomes a dependency | Repository policy and canonical skill files; Python standard-library maintenance tooling | Inspectable workflow that can be adapted to different hosts | [Tool setup](START-HERE.md); loading still needs host-specific verification; examples have their own dependencies |

**Positioning:** Lightweight on low-risk work, explicit on high-risk work, portable at handover. These are design choices, not exclusive features: the peer frameworks also provide planning, verification and continuity in different forms.

## Estimated fit scores for small teams

**Editorial estimates, not measured benchmarks.** Scores assess the documented approach for small teams that value setup, planning, verification, continuity and tool compatibility equally. Assessment date: 2026-09-10, using local documents and [S1]–[S4] below. This project-authored assessment is not an independent evaluation; ND's internal evidence is more detailed than the upstream overview material reviewed for peers.

### Scoring rubric

Each dimension receives an integer from 1 to 5: **1** = limited documented fit, **2** = substantial adaptation needed, **3** = usable with notable gaps, **4** = strong documented fit with caveats, **5** = especially strong documented fit for that dimension. Unknown capability must not be treated as absent; these are whole-dimension judgments, not counts of missing features. A 5 does not mean runtime-tested, bug-free, or universally best.

| Dimension | Weight | What earns a stronger fit judgment |
|---|---:|---|
| Setup | 20% | Clear installation/adoption path, existing-project guidance, manageable setup burden |
| Planning | 20% | Actionable plans, explicit requirements, maintained change artifacts |
| Verification | 20% | Explicit tests/review, completion evidence, handling of failures and risk |
| Continuity | 20% | Durable state, reusable learning and explicit handoff/recovery guidance |
| Tool compatibility | 20% | Documented host-specific installation routes and breadth, with maturity limits visible |

**Calculation:** overall fit = sum of the five ratings / 5. This is a rating out of 5, not a success percentage. Equal-weight arithmetic is a decision aid over subjective ordinal judgments, not a scientific measurement. A one-point change in any dimension changes the overall rating by 0.2; small gaps should not decide adoption without a team pilot.

| Framework | Setup /5 | Planning /5 | Verification /5 | Continuity /5 | Tool compatibility /5 | Estimated overall /5 |
|---|---:|---:|---:|---:|---:|---:|
| **ND Workflow** | 4 | 4 | 5 | 5 | 3 | **4.2** |
| Superpowers | 4 | 5 | 5 | 3 | 5 | **4.4** |
| OpenSpec | 4 | 5 | 3 | 4 | 5 | **4.2** |
| Compound Engineering | 4 | 5 | 4 | 5 | 5 | **4.6** |
| GSD Core | 4 | 4 | 4 | 5 | 4 | **4.2** |

### Why these ratings?

| Framework | Rationale across the five dimensions | Important caveat |
|---|---|---|
| ND Workflow | Setup 4: reviewed adoption with recovery evidence, but manual reconciliation. Planning 4: pragmatic PRD/tasks rather than a dedicated spec lifecycle. Verification 5: explicit risk tiers, evidence freshness and completion boundaries. Continuity 5: ownership/checkpoints, recovery guidance and knowledge maintenance. Compatibility 3: generated bundles/manual routes with limited native validation. | Highest ratings describe policy detail, not proven agent compliance. Host smoke tests and team outcome measurements remain missing. |
| Superpowers [S1] | Setup 4: clear per-host installs, with separate setup for each host. Planning 5: approved design plus detailed execution tasks. Verification 5: explicit TDD, staged review and completion checks. Continuity 3: plans/checkpoints documented, but cross-session recovery is less established in the overview reviewed. Compatibility 5: numerous explicit plugin/extension installation routes. | Continuity score reflects the reviewed overview, not proof that richer recovery support is absent. Mandatory workflow can be more process than a small fix needs. |
| OpenSpec [S2] | Setup 4: CLI init, profiles and existing-project guidance, with CLI setup required. Planning 5: proposal/spec/design/task lifecycle and synchronization. Verification 3: optional expanded verify workflow; testing discipline is not the overview's main focus. Continuity 4: durable changes and archived specs. Compatibility 5: detailed multi-host skills/command adapters. | Spec continuity is not identical to operational handover; verify which additional review/test policy the team needs. |
| Compound Engineering [S3] | Setup 4: per-host installs plus project setup, with a larger skill catalog to navigate. Planning 5: requirements-to-implementation plan enrichment. Verification 4: review and platform testing skills, but the overview does not establish ND-style risk-tier routing. Continuity 5: reusable solutions, knowledge refresh and handoff. Compatibility 5: numerous explicit native installation routes. | Strongest estimated balanced fit in this rubric, not proof of better delivery. Optional autonomous pipeline has commit/push/PR effects that teams must understand before use. |
| GSD Core [S4] | Setup 4: installer and existing-project onboarding; runtime conversion requires the installer. Planning 4: research and phase plans emphasize milestone execution. Verification 4: explicit verify-and-fix phase. Continuity 5: persistent state/context and fresh-context execution. Compatibility 4: several named installer targets, with host details less deeply inspected here. | Phase-oriented execution can be a poor match when the team mainly wants a minimal process for isolated changes. |

**Why ND despite a lower overall score than some peers?** A balanced average hides the decision that matters for some teams: they want a short safe path for ordinary work, explicit escalation for sensitive changes, and reviewable handover artifacts without adopting a mandatory full execution methodology. ND makes that policy central. If native plugin breadth or a richer opinionated execution loop matters more, a peer may be the better choice.

## Workflow feature tradeoffs

| Team scenario | ND approach | Peer approach worth considering | Selection advice |
|---|---|---|---|
| Isolated, low-risk fix | Scoped edit and focused check; no required spec/task/delegation ceremony | Superpowers emphasizes mandatory skill-driven design, planning and TDD [S1] | ND for a deliberately lighter policy; Superpowers for consistency through a stricter methodology |
| Multi-file feature with stable requirements | Reuse approved scope; inline task plan; spec only for unresolved scope | OpenSpec maintains explicit proposal/spec/design/task artifacts [S2] | ND for pragmatic task delivery; OpenSpec when specification lifecycle is the main need |
| Sensitive one-line change | Critical risk gates regardless of patch size | Superpowers emphasizes TDD/review; CE provides review/testing skills [S1][S3] | ND when explicit risk classification is central; no framework replaces security expertise |
| Teammate resumes unfinished work | Record owner, scope, current evidence, blockers and next action | GSD persists state/context; CE has a handoff skill [S3][S4] | ND for explicit repository handover policy; compare actual recovery in a pilot |
| Team wants knowledge to improve future work | Compound only durable learnings; deduplicate and retire stale guidance | CE makes reusable solutions a central engineering loop [S3] | ND for selective learning; CE when the learning loop is the primary workflow |
| Large milestone needs coordinated execution | Optional delegation with disjoint ownership and integration checks | GSD uses phased, fresh-context execution waves [S4] | ND for flexible coordination; GSD for a more prescribed milestone engine |
| Team wants ready-made multi-host installs | Local beta bundles and manual loading routes; runtime checks still needed | Superpowers, OpenSpec and CE document broad host integrations [S1][S2][S3] | Do not choose ND on an unproven claim of best compatibility |

## What these scores cannot claim

No estimated success rate, token savings, cycle-time gain, or defect-reduction percentage is supplied. Existing local test counts measure starter/example checks—not the probability that an agent delivers a feature correctly.

For a real comparison, run the same representative tasks with pinned framework revisions, the same model/version and tools, equal token/time budgets, the same starting repository and human-intervention rules. Repeat runs, vary execution order, record failures, and use a reviewer unaware of which workflow produced each result where practical.

| Outcome to measure | Definition | Current evidence |
|---|---|---|
| Task success rate | Tasks meeting all predeclared acceptance criteria / tasks attempted; report sample size and uncertainty | Unmeasured across frameworks |
| Delivery time | Median and spread of elapsed time to accepted result, including review and repair | Unmeasured across frameworks |
| Token cost | Total input/output tokens and actual model charges per accepted task, including failed runs | Unmeasured across frameworks |
| Handover recovery rate | Paused tasks resumed by a fresh person/session without hidden chat context and meeting acceptance / recovery attempts | Unmeasured across frameworks |
| Human intervention | Clarifications, corrections and manual repair time per task, separately from mandatory safety approvals | Unmeasured across frameworks |
| Regression/defect rate | Failed predeclared regression checks and defects found during a fixed follow-up window | Unmeasured across frameworks |

**Adoption decision:** Pilot one small fix, one cross-file feature, one sensitive-change scenario in an isolated test environment, and one interrupted handover. Choose the workflow your team can operate reliably; do not treat the editorial score above as a purchasing or production-readiness guarantee.

---

## Benchmark Score Table

Historical delivery evidence from task records dated 2026-09-09; not a fresh test run or a controlled cross-framework benchmark. Python starter checks used Windows PowerShell and Python 3.12.10; Todo API/browser checks used Node.js and Playwright.

| Task record | Test cases | Passed | Skipped | Separate validation evidence | Package evidence |
|---|---:|---:|---:|---|---|
| [1. Harden starter](docs/tasks/done/done-0001-harden-workflow-starter.md) | — | — | — | 13/13 policy assertions | 20,549 B; 16 entries |
| [2. Workflow synthesis](docs/tasks/done/done-0002-synthesize-best-in-class-workflow.md) | — | — | — | 16/16 policy checks | CRC and source-byte checks passed; size not recorded |
| [3. Portable checks and handover](docs/tasks/done/done-0003-portable-handover-workflow.md) | 62 | 59 | 3 | Validator passed; 25 manifest files (not 25 policy checks) | 44,372 B; 25 entries |
| [4. Todo RC](docs/tasks/done/done-0004-rc-todo-example.md) | 82 | 79 | 3 | 63 core + 11 API + 8 Chromium cases | 90,901 B; 54 entries |
| [5. Platform plugins](docs/tasks/done/done-0005-platform-plugins.md) | 71 | 68 | 3 | Eight plugin tests passed within the suite; validator covered 59 files | Three bundles; 68–73 entries each |

**Counting convention:** Rows 3–5 sum to 215 test cases: 206 passed, 9 skipped, zero reported failures in their final runs. Counts include repeated/evolving suites across tasks, not 215 unique tests; source/extraction reruns are not counted twice. Skips required Windows symlink privileges. Only rows 1–2 report numeric policy-check scores; file counts are not policy scores.

These records establish historical local-scope results, not current runtime compatibility, production readiness, or faster/cheaper delivery. Cycle time, token cost, defect escape rate, and controlled competitor scores remain unmeasured.

---

## Tool Compatibility Comparison

ND Workflow compared with four selected peers: Superpowers, OpenSpec, Compound Engineering, and GSD Core. This is a documentation-based comparison, not a popularity ranking or performance leaderboard. Upstream sources retrieved 2026-09-10; moving branches may change.

**Evidence labels:** **Local** = ND bundle or adapter described in this repository, not verified end-to-end host operation. **Documented** = upstream provides a host installation route, not independently tested here. **Unknown** = not established by the cited sources; it does not mean unsupported.

| AI tool | ND Workflow | Superpowers [S1] | OpenSpec [S2] | Compound Engineering [S3] | GSD Core [S4] |
|---|---|---|---|---|---|
| Claude Code | Local plugin; historical native manifest validation passed | Documented marketplace plugin | Documented skills + commands | Documented marketplace plugin | Documented installer target |
| OpenAI Codex | Local plugin + repository skills | Documented App/CLI plugin | Documented `.agents/skills`; skills-only | Documented App/CLI custom marketplace | Documented installer target |
| Cursor | Local plugin bundle | Documented marketplace plugin | Documented skills + commands | Documented marketplace plugin | Documented installer target |
| Aider | Local manual `--read` route | Unknown | Unknown | Unknown | Unknown |
| ChatGPT Custom GPT | Local instructions/knowledge assets; upload behavior unverified | Unknown | Unknown | Unknown | Unknown |
| Windsurf | Local generated rules; host loading unverified | Unknown | Documented `windsurf` alias for `devin`; skills + workflows | Unknown | Documented installer target |
| Continue | Local generated prompt assets | Unknown | Documented skills + prompts | Unknown | Unknown |
| GitHub Copilot | Unknown | Documented CLI plugin | Documented integration; IDE/CLI/cloud distinctions apply | Documented VS Code and CLI plugin | Documented installer target |
| OpenCode | Unknown | Documented plugin install | Documented skills + commands | Documented native plugin | Documented installer target |

ND routes: [plugin packages](docs/PLUGINS.md) and [manual tool setup](START-HERE.md). Six generated bundle targets do not equal six tested host integrations. A generic `AGENTS.md` loading route is not an additional tool. Competitor cells describe upstream claims only; no competitor was installed or exercised for this comparison.

### Workflow and delivery approach

| Dimension | ND Workflow | Superpowers [S1] | OpenSpec [S2] | Compound Engineering [S3] | GSD Core [S4] |
|---|---|---|---|---|---|
| Main focus | Risk-scaled delivery and evidence-backed handover | Design, detailed plans, TDD and reviewed execution | Artifact-guided specification and change lifecycle | Plan, build, review and reusable learning | Context engineering and milestone delivery |
| Planning artifacts | Delta PRD when scope unresolved; task checkpoints | Design document and bite-sized implementation plan | Proposal, specs, design and tasks | Unified plan enriched from requirements to execution | Discuss, research and phase plans |
| Execution | Small tasks stay direct; delegation optional | Subagent execution or batches with checkpoints | Apply tasks from change artifacts | Work skills; optional autonomous pipeline | Parallel waves with fresh-context executors |
| Verification | Four risk tiers; impact-based checks; acceptance evidence | RED-GREEN-REFACTOR and verification before completion | Optional expanded verify workflow | Code/doc review and browser/Xcode test skills | Verify phase and generated fix plans |
| Continuity | Task handover; compound deduplication and stale-knowledge retirement | Saved plans and execution checkpoints | Change artifacts, spec sync and archive | `docs/solutions/` learning loop and handoff skill | Persistent `STATE.md` and `CONTEXT.md` |
| Adoption | Guided fresh/existing setup and Superpowers migration | Per-host installation | `openspec init`; selectable tool/profile setup | Host installation and `ce-setup` | Installer plus new-project/onboard commands |

ND test-first is preferred where practical, not universally enforced. Its delta headings are a local convention, not OpenSpec CLI compatibility. See [workflow policy](.agents/docs/WORKFLOW.md).

**Selection guide:** Choose ND for explicit risk routing and portable handover; Superpowers for an opinionated TDD/review workflow; OpenSpec for maintained specs and change artifacts; Compound Engineering for a reusable learning loop; GSD Core for phase-based execution with fresh contexts. These are differences in documented approach, not measured superiority. Comparable speed, cost, reliability, and task-success scores require the same tasks, models, budgets, environments, and scoring rules across all five.

**Sources (primary project documentation, retrieved 2026-09-10):**
- **[S1]** [Superpowers README](https://github.com/obra/superpowers/blob/main/README.md): installation routes, skills, TDD and review workflow.
- **[S2]** [OpenSpec README](https://github.com/Fission-AI/OpenSpec/blob/main/README.md) and [supported tools](https://github.com/Fission-AI/OpenSpec/blob/main/docs/supported-tools.md): artifacts, profiles, host-specific paths and invocation limits.
- **[S3]** [Compound Engineering README](https://github.com/EveryInc/compound-engineering-plugin/blob/main/README.md): host installation, core loop, review, learning and handoff.
- **[S4]** [GSD Core README](https://github.com/open-gsd/gsd-core/blob/main/README.md): installer targets, phase loop and persistent context. The former `gsd-build/get-shit-done` repository redirects to this project.

