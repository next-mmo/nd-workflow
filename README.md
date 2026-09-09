# ND Workflow: AI Agent Workflow Starter

Lightweight, evidence-driven delivery workflow for AI-assisted software development.

`AGENTS.md` holds shared policy; local skills hold task-specific procedures. Works across Claude Code, OpenAI Codex, Cursor, Aider, and custom LLM agent tools.

---

## Key Features

- **Spec before code:** [Delta PRDs](.agents/templates/PRD.md) and [task checkpoints](.agents/templates/TASK.md) prevent scope drift and duplicate specifications.
- **Risk-tiered gates:** Clear routing for low, medium, high, and critical changes in [WORKFLOW.md](.agents/docs/WORKFLOW.md).
- **Evidence-backed verification:** Structured checks, acceptance verification with `converge-check`, and durable learnings with `compound`.
- **Multi-platform package targets:** Generate reviewable bundles for Claude Code, Cursor, Codex, ChatGPT, Windsurf, and Continue via `scripts/build_plugins.py`. Local format tests pass; host installation, discovery, marketplace acceptance, and model behavior require separate smoke tests (see [PLUGINS.md](docs/PLUGINS.md)).
- **Runnable reference implementations:**
  - Full-stack Todo app in [example/full-stack-todo-express-vanillajs/](example/full-stack-todo-express-vanillajs/GUIDE.md).
  - Full-stack CMS Portfolio with auth and full `.agents` adoption in [example/full-stack-nd-workflow-cms-portfolio/](example/full-stack-nd-workflow-cms-portfolio/GUIDE.md).

---

## Benchmarks and Comparisons

**Why choose ND?** Keep low-risk work lightweight, raise verification with risk, and leave clear handover checkpoints. Built for small teams that want a shared delivery policy without a mandatory full execution loop for every change.

See [why choose ND, estimated fit scores, and tool compatibility](BENHMARK.md) for a balanced comparison with four peer frameworks, workflow tradeoffs, historical delivery evidence, and sources. Fit scores are editorial judgments—not measured speed, cost, or success rates.

---

## Quickstart

### 1. Choose your starting point

- **Fresh project:** ask `setup-project` to add workflow only, before choosing an application stack.
- **Existing project:** ask `setup-project` to preview adoption while preserving instructions, facts and uncommitted work.
- **From Superpowers:** ask `setup-project` to inventory active work and guide replacement or coexistence.
- **Setup looks wrong:** ask `workflow-doctor` for read-only findings.

Follow [guided onboarding](docs/ONBOARDING.md) for exact commands, reviewed merge and recovery. If skills are not discovered, explicitly load their files. [START-HERE.md](START-HERE.md) covers manual adoption and host setup. Plugin installation alone does not activate project policy.

### 2. Verify local starter integrity

Requires Python 3.10+ (standard library only; no external pip dependencies):

```powershell
python scripts/validate.py
python -m unittest discover -s tests -p 'test_*.py' -v
```

### 3. Package distributable zip

```powershell
python scripts/package.py --output artifacts/workflow-starter.zip
```

---

## Repository Map

| Path | Purpose |
|---|---|
| [AGENTS.md](AGENTS.md) | Universal agent instructions, risk precedence, and safety boundaries |
| [START-HERE.md](START-HERE.md) | Adoption steps, tool setup matrix, and portable checks |
| [CLAUDE.md](CLAUDE.md) | Claude Code import adapter pointing to `AGENTS.md` |
| [LICENSE](LICENSE) | MIT License |
| [docs/README.md](docs/README.md) | Topic catalog across specs, plans, tasks, and guides |
| [docs/PLUGINS.md](docs/PLUGINS.md) | Plugin building, distribution, and target agent configurations |
| [docs/HANDOVER.md](docs/HANDOVER.md) | Session pause, developer handover, and cold recovery drill |
| [example/full-stack-todo-express-vanillajs/](example/full-stack-todo-express-vanillajs/GUIDE.md) | Reference Todo app (Express + vanilla JS) |
| [example/full-stack-nd-workflow-cms-portfolio/](example/full-stack-nd-workflow-cms-portfolio/GUIDE.md) | Reference CMS Portfolio with auth and full `.agents` adoption |

---

## License

This project is licensed under the [MIT License](LICENSE).
