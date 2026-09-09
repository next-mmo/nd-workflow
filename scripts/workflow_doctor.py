"""Read-only ND Workflow file diagnosis; does not run project or host commands."""
from pathlib import Path
import argparse
import json
import os
import re
from setup_project import safe_target, checked_path, JOURNAL

SKILLS = ('setup-project', 'workflow-doctor', 'doc-lookup', 'spec-feature', 'converge-check', 'compound', 'bump-version')


def inspect_project(target):
    target = safe_target(target)
    findings = []
    missing = []
    unknowns = []
    superpowers = []
    duplicates = []
    paths = ['AGENTS.md', 'CLAUDE.md', '.agents/docs/PROJECT.md', '.agents/docs/ARCHITECTURE.md', '.agents/docs/WORKFLOW.md']
    paths += [f'.agents/skills/{name}/SKILL.md' for name in SKILLS]
    for name in paths:
        path = checked_path(target, name)
        if not path.exists():
            missing.append(name)
            continue
        if path.stat().st_size > 100_000:
            findings.append({'path': name, 'issue': 'Too large for bounded diagnosis'})
            continue
        text = path.read_text(encoding='utf-8')
        if name.endswith(('PROJECT.md', 'ARCHITECTURE.md')) and 'UNSET' in text:
            unknowns.append(name)
        if name in ('AGENTS.md', 'CLAUDE.md') and re.search('superpowers?', text, re.I):
            superpowers.append(name)
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            link = link.split('#', 1)[0]
            if not link or '://' in link or link.startswith(('mailto:', '#')):
                continue
            candidate = Path(os.path.abspath(path.parent / link))
            if candidate != target and target not in candidate.parents:
                findings.append({'path': name, 'issue': 'Reference outside project; not inspected'})
                continue
            relative = candidate.relative_to(target).as_posix()
            try:
                linked = checked_path(target, relative)
                if not linked.exists():
                    findings.append({'path': name, 'issue': 'Missing reference', 'reference': relative})
            except ValueError:
                findings.append({'path': name, 'issue': 'Unsafe or non-file reference; not inspected'})
    for name in SKILLS:
        candidate = checked_path(target, f'.claude/skills/{name}/SKILL.md')
        canonical = checked_path(target, f'.agents/skills/{name}/SKILL.md')
        if candidate.exists() and canonical.exists():
            duplicates.append(name)
    journal = target / JOURNAL
    from stage_project import reject_links
    reject_links(journal)
    journal_state = 'ABSENT'
    if journal.exists():
        complete = checked_path(target, JOURNAL + '/COMPLETE')
        journal_state = 'COMPLETE_MARKER_PRESENT' if complete.exists() else 'INCOMPLETE_REVIEW_REQUIRED'
    return {'status': 'ATTENTION' if missing or unknowns or findings or superpowers or duplicates or journal_state == 'INCOMPLETE_REVIEW_REQUIRED' else 'FILES_PRESENT',
            'project': str(target), 'package_available': 'DOCTOR_EXECUTABLE',
            'project_adoption': 'INCOMPLETE' if missing or unknowns or findings else 'REQUIRES_SEMANTIC_REVIEW',
            'host_loading': 'UNVERIFIED', 'application_baseline': 'NOT_RUN',
            'missing': missing, 'template_unknowns': unknowns, 'findings': findings,
            'superpowers_references': superpowers, 'potential_duplicate_skills': duplicates,
            'journal': journal_state,
            'next_action': 'Review file findings, inspect host context in a fresh session, then run approved source-backed application checks. No global configuration inspected.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', type=Path, required=True)
    args = parser.parse_args()
    try:
        result = inspect_project(args.target)
        print(json.dumps(result, indent=2))
        return 0 if result['status'] == 'FILES_PRESENT' else 2
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({'status': 'FAIL', 'error': str(exc)}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
