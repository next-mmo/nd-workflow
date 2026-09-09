from pathlib import Path
import hashlib
import json
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from build_plugins import build, collect, ADAPTER, TARGETS
from stage_project import stage, STAGE

class PluginTests(unittest.TestCase):
    def setUp(self):
        base = ROOT / '.validation' / 'plugin-tests'
        base.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=base)
        self.root = Path(self.temp.name)
    def tearDown(self):
        self.temp.cleanup()
    def extract(self, target='claude-code'):
        out = self.root / (target + '.zip')
        build(ROOT, target, out)
        dest = self.root / target
        dest.mkdir()
        with zipfile.ZipFile(out) as archive:
            archive.extractall(dest)  # Only locally generated, allowlisted archive.
        return dest
    def test_three_manifest_formats_and_shared_bodies(self):
        for target, manifest in TARGETS.items():
            entries = collect(ROOT, target)
            metadata = json.loads(entries[manifest])
            self.assertEqual(metadata['name'], 'workflow-starter')
            self.assertEqual(metadata['version'], '0.1.0-beta.1')
            for name in json.loads((ROOT/'plugins/plugin-config.json').read_text())['skills']:
                original = (ROOT/f'.agents/skills/{name}/SKILL.md').read_text(encoding='utf-8')
                header, body = original.split('\n---\n', 1)
                generated = entries[f'skills/{name}/SKILL.md'].decode()
                self.assertTrue(generated.startswith(header+'\n---\n'))
                self.assertIn(ADAPTER, generated)
                self.assertTrue(generated.endswith(body.lstrip('\n')))
                self.assertIn('starter/.agents/templates/TASK.md', entries)
            self.assertFalse(any(name.startswith(('hooks/', 'mcp')) for name in entries))
    def test_codex_schema_and_presentation(self):
        data = json.loads(collect(ROOT, 'codex')['plugin.json'])
        self.assertEqual(data['$schema'], 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json')
        self.assertEqual(len(data['extensions']['com.openai']['interface']['defaultPrompt']), 3)
        self.assertFalse(set(data) - {'$schema','name','version','description','extensions'})
    def test_deterministic_zip_and_collision(self):
        a=self.root/'a.zip'; b=self.root/'b.zip'
        result=build(ROOT,'cursor',a); build(ROOT,'cursor',b)
        self.assertEqual(a.read_bytes(), b.read_bytes())
        self.assertEqual(result['sha256'],hashlib.sha256(a.read_bytes()).hexdigest())
        with self.assertRaises(FileExistsError): build(ROOT,'cursor',a)
        self.assertEqual(a.read_bytes(),b.read_bytes())
    def test_unknown_target_and_outside_destination(self):
        with self.assertRaises(ValueError): collect(ROOT,'not-supported')
        with self.assertRaises(ValueError): build(ROOT,'cursor',ROOT.parent/'outside-plugin-test.zip')
    def test_preview_and_apply_preserve_live_project(self):
        plugin=self.extract(); project=self.root/'project'; project.mkdir()
        (project/'AGENTS.md').write_text('User policy',encoding='utf-8')
        result=stage(plugin,project)
        self.assertEqual(result['status'],'PREVIEW')
        self.assertFalse((project/STAGE).exists())
        self.assertIn('AGENTS.md',result['project_collisions'])
        stage(plugin,project,True)
        self.assertEqual((project/'AGENTS.md').read_text(),'User policy')
        self.assertEqual((project/STAGE/'AGENTS.md').read_bytes(),(ROOT/'AGENTS.md').read_bytes())
        with self.assertRaises(FileExistsError): stage(plugin,project,True)
    def test_tampered_bundle_rejected_before_write(self):
        plugin=self.extract(); project=self.root/'project'; project.mkdir()
        (plugin/'starter/AGENTS.md').write_text('tampered',encoding='utf-8')
        with self.assertRaises(ValueError): stage(plugin,project,True)
        self.assertFalse((project/STAGE).exists())
    def test_unsafe_path_rejected_before_write(self):
        plugin=self.extract(); project=self.root/'project'; project.mkdir()
        meta=plugin/'bundle.json'; value=json.loads(meta.read_text()); value['canonical_sha256']['../escape']='x'; meta.write_text(json.dumps(value))
        with self.assertRaises(ValueError): stage(plugin,project,True)
        self.assertFalse((project/STAGE).exists())
    def test_all_resources_match_hashes(self):
        entries=collect(ROOT,'codex'); hashes=json.loads(entries['bundle.json'])['canonical_sha256']
        for name,digest in hashes.items():
            self.assertEqual(hashlib.sha256(entries['starter/'+name]).hexdigest(),digest)
        self.assertEqual(entries['scripts/stage_project.py'],(ROOT/'scripts/stage_project.py').read_bytes())

if __name__ == '__main__': unittest.main()
