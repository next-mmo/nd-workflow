# Workflow Starter Plugins

Local beta packages for Claude Code, Cursor and Codex. Five on-demand skills share canonical source in `.agents/skills/`. Packaging version `0.1.0-beta.1` identifies these bundles only; no root release tag or public listing exists.

## What you receive

- Five skills: doc-lookup, spec-feature, converge-check, compound, bump-version.
- Platform manifest plus explicit resource-resolution note in generated skills.
- Full allowlisted starter under `starter/` so templates and relative references remain available.
- Preview-first staging helper; no hooks, MCP servers, telemetry, external commands on load, or automatic project edits.
- Codex presentation metadata includes display name, description, starter prompts and skill labels. Catalog UI layout remains controlled by the host; screenshot appearance is not guaranteed.

Plugin installation alone does not make its root policy standing project instructions. Existing project policy remains authoritative. Adopt needed rules/templates by reviewed merge. Do not install both repository skills and plugin copies unless duplicate selectors are intentional.

## Build locally

Python 3.10+ standard library; from this source repository root:

```powershell
python scripts/build_plugins.py --target claude-code --output artifacts/workflow-starter-claude-code.zip
python scripts/build_plugins.py --target cursor --output artifacts/workflow-starter-cursor.zip
python scripts/build_plugins.py --target codex --output artifacts/workflow-starter-codex.zip
python -m unittest discover -s tests -p 'test_plugins.py' -v
```

Output must not exist; use a fresh name. Generated bundles are derivatives, not editable source. Edit canonical skills/docs/config and rebuild. Skills keep canonical name/description and body, with one generated resource note. Publisher identity, license, repository URL and legal URLs are deliberately omitted until verified and chosen by owner; public submission still requires release hygiene.

## Claude Code

Extract Claude bundle to a new directory. Its `.claude-plugin/plugin.json` and `skills/` are at root. Local validation:

```powershell
claude plugin validate C:\path\to\extracted-plugin
claude --plugin-dir C:\path\to\extracted-plugin
```

Second command launches a session with this plugin; it is an explicit user action, not run by builder. In the selected project, invoke `/workflow-starter:spec-feature` or another namespaced skill. Check installed CLI help because command availability varies by version. Marketplace listing/persistent installation is separate; no fake publisher or marketplace URL provided.

## Cursor

Extract Cursor bundle; `.cursor-plugin/plugin.json` identifies native Cursor format. Official local test route is a folder under `~/.cursor/plugins/local/workflow-starter`, then restart or Developer: Reload Window and inspect Customize. Copying there changes user-level configuration: review/authorize that action separately; builder does not perform it.

Local imports may be disabled by organization policy. An installed marketplace version may take precedence. Skills can be selected manually in chat. Verify all five appear in Customize and run a non-mutating routing prompt before adopting into work. This is not a VSIX; do not use `--install-extension` for these ZIPs.

## Codex

Codex bundle uses root `plugin.json` with Agent Plugins schema and `skills/`, with `extensions.com.openai.interface` for catalog presentation. Official compatibility path `.codex-plugin/plugin.json` is not needed for this portable package.

A local marketplace may expose the extracted directory. Example, relative to the marketplace root, not the `.agents/plugins/` folder:

```json
{
  "name": "workflow-starter-local",
  "interface": { "displayName": "Workflow Starter Local Beta" },
  "plugins": [{
    "name": "workflow-starter",
    "source": { "source": "local", "path": "./plugins/workflow-starter" },
    "policy": { "installation": "AVAILABLE", "authentication": "ON_INSTALL" },
    "category": "Productivity"
  }]
}
```

Save to `.agents/plugins/marketplace.json` only after collision review; place extracted plugin at `plugins/workflow-starter`. Use `codex plugin marketplace --help` and `codex plugin --help` for installed version. Registering/installing changes configuration, so no such action runs automatically. Repository skills under `.agents/skills` remain an alternative local authoring route; use one route to avoid duplicates. ChatGPT website/mobile support is outside this task's tested scope.

## Project adoption without overwriting

From extracted plugin root, use its actual filesystem location, not a guessed working-directory path:

```powershell
python scripts/stage_project.py --target C:\path\to\project
python scripts/stage_project.py --target C:\path\to\project --apply
```

Preview lists collisions but writes nothing. Apply creates only `<project>/.workflow-starter-review/`, fails if it exists, and does not merge any live project file. Review and selectively merge desired files; do not copy example data/history or erase existing architecture, settings, indexes, or instructions. Treat staging as a review copy, not automatically loaded project policy. Avoid running it inside another installed plugin. Preserve partial staging on failure for diagnosis; no cleanup deletes user files.

Before invocation, target project must have appropriate permissions and scope. Missing project templates can be read from bundled starter; project-specific facts must come from actual source. Bundled release scripts concern this starter distribution only.

## Acceptance and compatibility evidence

Automated gates: shared-source integrity; three manifest layouts; resource closure; deterministic packaging; unknown target/output collision rejection; preview no-write; staging preserves existing files and refuses repeat application; tampered bundle rejection.

Native Claude manifest validation can run without model calls. Cursor UI discovery and Codex installed-skill invocation require explicit install/session smoke tests. A valid JSON manifest does not prove UI listing, implicit routing, model behavior, policy enforcement, or public marketplace acceptance. Fresh-session test: request plan for approved scope, critical handling for one-line auth change, and checkpoint before handover; inspect selected skill and paths without production edits.

Documentation checked 2026-09-09:
- Claude: https://code.claude.com/docs/en/plugins-reference.md
- Cursor: https://cursor.com/docs/plugins.md
- OpenAI skills: https://developers.openai.com/codex/skills.md
- OpenAI packaging: https://developers.openai.com/plugins/build/plugins.md
- Portable schema: https://agent-plugins.org/schemas/1.0.0/plugin.schema.json

Current docs can exceed installed client features. Record actual client versions and native test results separately. None of these packages is published, endorsed, or certified by its host vendor.
