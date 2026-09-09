"""Preview or stage plugin starter files for manual merge; never overwrite project files."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import sys

STAGE = '.workflow-starter-review'

def linked(path):
    return path.is_symlink() or (os.name == 'nt' and path.exists() and bool(path.lstat().st_file_attributes & 1024))

def stage(plugin, target, apply=False):
    plugin = plugin.absolute(); target = target.absolute()
    if not target.is_dir(): raise ValueError('Target must be an existing project directory')
    for path in (target, *target.parents):
        if linked(path): raise ValueError('Target contains link/reparse point')
    destination = target / STAGE
    if destination.exists() or destination.is_symlink(): raise FileExistsError('Review staging directory exists; preserved')
    metadata = json.loads((plugin / 'bundle.json').read_text(encoding='utf-8'))
    files = metadata['canonical_sha256']
    planned = []
    for name, digest in files.items():
        parts = name.split('/')
        if not name or any(p in ('', '.', '..') for p in parts) or any(c in name for c in ':\\'):
            raise ValueError('Unsafe bundled path')
        source = plugin / 'starter' / name
        if any(linked(p) for p in (source, *source.parents)): raise ValueError('Linked bundle source')
        data = source.read_bytes()
        if hashlib.sha256(data).hexdigest() != digest: raise ValueError('Bundle checksum mismatch: ' + name)
        planned.append((name, data))
    result = {'status': 'PREVIEW', 'target': str(target), 'stage': str(destination), 'files': len(planned), 'project_collisions': [name for name, _ in planned if (target / name).exists()], 'note': 'No files merged; inspect staged content and merge deliberately.'}
    if apply:
        destination.mkdir(exist_ok=False)
        for name, data in planned:
            out = destination / name
            out.parent.mkdir(parents=True, exist_ok=True)
            with out.open('xb') as handle: handle.write(data)
        result['status'] = 'STAGED'
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', type=Path, required=True)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    plugin = Path(__file__).resolve().parent.parent
    try: print(json.dumps(stage(plugin, args.target, args.apply), indent=2))
    except (OSError, ValueError, KeyError) as exc:
        print(json.dumps({'status': 'FAIL', 'error': str(exc)})); return 1
    return 0

if __name__ == '__main__': raise SystemExit(main())
