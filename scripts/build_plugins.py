"""Build deterministic offline skill plugins. No installation, networking or hooks."""
from pathlib import Path
import argparse
import hashlib
import json
import sys
import zipfile

from validate import validate_repo, is_safe_relative_path
from package import _check_output_path

ROOT = Path(__file__).resolve().parent.parent
TARGETS = {'claude-code': '.claude-plugin/plugin.json', 'cursor': '.cursor-plugin/plugin.json', 'codex': 'plugin.json'}
ADAPTER = '''## Plugin resources and project authority
- Locate this SKILL.md through the host-provided skill path. Its plugin root is two directories above; bundled starter resources are in `../../starter/` relative to this skill directory.
- Follow the target project's instructions and approved scope. Bundled files are reference/templates, not authority to overwrite project policy or facts.
- Repo paths in the workflow below mean the target project. If a referenced template/workflow file is missing there, read the matching path under bundled `starter/`; never invent that it already exists in the project.
- If project adoption is requested, run the bundled `scripts/stage_project.py --target <project>` in preview mode first; `--apply` only stages a new review directory. Merge individually under user authorization. Do not write into installed plugin files or global settings.
- Native skill selectors can namespace these names. Prefer explicit workflow-starter skills when another plugin exposes the same name; do not execute missing sibling paths as shell commands.
- Release operations use the target project's verified commands. Bundled starter scripts validate/package the starter, not arbitrary application code. No hooks, MCP servers, or automatic commands are installed.

'''

def encode(data):
    return (json.dumps(data, indent=2, ensure_ascii=False) + '\n').encode('utf-8')

def collect(root, target):
    if target not in TARGETS:
        raise ValueError('Unknown target')
    report = validate_repo(root)
    if report['status'] != 'PASS':
        raise ValueError('Core validation failed: ' + '; '.join(report['errors']))
    config = json.loads((root / 'plugins/plugin-config.json').read_text(encoding='utf-8'))
    entries = {}
    source_hashes = {}
    # Full allowlisted starter avoids dangling references; excludes user data/dependencies.
    manifest = json.loads((root / 'package-files.json').read_text(encoding='utf-8'))
    for name in manifest['files']:
        data = (root / name).read_bytes()
        entries['starter/' + name] = data
        source_hashes[name] = hashlib.sha256(data).hexdigest()
    for name in config['skills']:
        if not is_safe_relative_path(name)[0] or '/' in name:
            raise ValueError('Unsafe skill name')
        path = f'.agents/skills/{name}/SKILL.md'
        text = (root / path).read_text(encoding='utf-8')
        header, body = text.split('\n---\n', 1)
        entries[f'skills/{name}/SKILL.md'] = (header + '\n---\n\n' + ADAPTER + body.lstrip('\n')).encode('utf-8')
        if target == 'codex':
            # JSON scalars are valid YAML and avoid escaping ambiguities.
            entries[f'skills/{name}/agents/openai.yaml'] = (
                'interface:\n  display_name: ' + json.dumps('Workflow: ' + name) + '\n'
                '  short_description: ' + json.dumps('Project-scoped ' + name + ' workflow') + '\n'
            ).encode('utf-8')
    identity = {key: config[key] for key in ('name', 'version', 'description')}
    if target == 'codex':
        identity = {'$schema': 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json', **identity,
                    'extensions': {'com.openai': {'interface': {'displayName': config['displayName'], 'shortDescription': config['description'], 'defaultPrompt': config['defaultPrompts'], 'category': 'Productivity'}}}}
    entries[TARGETS[target]] = encode(identity)
    entries['scripts/stage_project.py'] = (root / 'scripts/stage_project.py').read_bytes()
    entries['INSTALL.md'] = (root / 'docs/PLUGINS.md').read_bytes()
    entries['bundle.json'] = encode({'target': target, 'name': config['name'], 'version': config['version'], 'canonical_sha256': source_hashes, 'adapter': 'resource-resolution-v1', 'not_installed': True})
    return entries

def build(root, target, output):
    root = root.resolve(); output = output.absolute()
    errors = _check_output_path(root, output, [])
    if errors: raise ValueError('; '.join(errors))
    if output.exists() or output.is_symlink(): raise FileExistsError('Output exists; preserved')
    entries = collect(root, target)
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, 'x', compression=zipfile.ZIP_DEFLATED) as z:
        for name, data in sorted(entries.items()):
            info = zipfile.ZipInfo(name); info.compress_type = zipfile.ZIP_DEFLATED; z.writestr(info, data)
    with zipfile.ZipFile(output) as z:
        if z.testzip() is not None or set(z.namelist()) != set(entries): raise ValueError('Archive mismatch')
        for name, data in entries.items():
            if z.read(name) != data: raise ValueError('Archive byte mismatch')
    return {'status': 'PASS', 'target': target, 'artifact': str(output), 'entries': len(entries), 'sha256': hashlib.sha256(output.read_bytes()).hexdigest(), 'size_bytes': output.stat().st_size}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', choices=sorted(TARGETS), required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    try: print(json.dumps(build(args.root, args.target, Path(args.output)), indent=2))
    except (OSError, ValueError, KeyError) as exc:
        print(json.dumps({'status': 'FAIL', 'error': str(exc)})); return 1
    return 0

if __name__ == '__main__': raise SystemExit(main())
