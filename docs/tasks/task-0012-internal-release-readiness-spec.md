# Task-0012: Correct readiness evidence and deliver local evaluation candidate

## Scope, approval and ownership

- Mode: implementation; local corrections, verification and packaging only.
- Owner: Mavis root `mvs_f324b4c7640d43d4a92ccf6fb15e4dc7`.
- Approved scope: [PRD-0005 v0.1](../prd/prd-0005-internal-release-readiness.md), RR-001–RR-006; unchanged 25/25/20/20/10 rubric. Approval: questionnaire `ask_98ed07f27c44a5b1c8984a87`, user, 2026-09-11. Original approval permitted planning only.
- Later execution evidence: user "do it all", "do it", and current "ship it your best now" after disclosure that certification was false. Authorizes best-effort local correction/verification/delivery; does not manufacture missing humans, approve scope reduction, or authorize an unspecified public destination.
- No commit, tag, push, production deployment or publication in this turn. Exact external release action requires separate confirmation.
- Baseline: main at c7dd5c4ddd3ee455ac058d4da8f0fc718e28c96d, dirty tree preserved. Fresh run manifest records actual input hashes and environment; earlier base is not proof of tested inputs.
- Writer scope: parent owns scorecard, candidate evidence corrections, README/catalog, this checkpoint, PRD status annotations and local evaluation artifacts. Worker owns five readiness helper scripts plus tests/test_readiness_helpers.py. Other source/CI changes remain pre-existing; no overlapping edits authorized.
- Recovery: preserve original records in artifacts/readiness-correction/withdrawn-records-20260911-171433.zip; no deleting old archives, fixtures or logs. New evaluation paths use exclusive creation. Restore owned edits only after review; no blanket reset.

## Execution plan and checks

- [x] Withdraw earned-score/certification claims and distinguish simulation from human evidence.
- [x] Disable unsafe auto-certification/destructive helpers; regression tests verify failure propagation and no overwrite/delete (20 tests PASS in `tests/test_readiness_helpers.py`).
- [x] Create candidate-002 with frozen input hashes, measured local environment, full raw outputs and explicit skipped checks (`docs/evidence/readiness/candidate-002/`).
- [x] Deliver local evaluation package with explicit release blockers recorded.

## PRD convergence: partial (local automated verified; human/platform gates open)

- RR-001: rubric approved; candidate-002 input manifest frozen; readiness score UNASSESSED.
- RR-002/003: candidate-002 ledger bound to measured hashes; raw command logs stored; candidate-001 invalid records withdrawn and archived to `artifacts/readiness-correction/withdrawn-records-20260911-171433.zip`.
- RR-004: local test suites pass (181 unit pass, 7 symlink skips on Windows; 71 hardened example tests pass; 36 full-stack tests pass; deterministic package verified). macOS, Python 3.10, and remote CI runs remain unverified.
- RR-005: fresh real-host drills and human developer onboarding (H4) have not been run on this candidate. BLOCKED.
- RR-006: independent maintainer review (E3) not performed. Token Plan limit prevented subagent review; self-authored check cannot substitute. Scorecard records BLOCKED.
- Score: UNASSESSED. Release gate: BLOCKED.

## Resume State

- Updated: 2026-09-11.
- Completed: candidate-002 local evaluation package created (`artifacts/readiness-correction/workflow-starter-candidate-002-evaluation.zip`, SHA-256: `38ddc0e4224f47b2803d00016fc170d86f865268d7e2ee3730532a74be4f763b`). Repeat build verified byte-identical.
- Next action: recruit non-author developer for onboarding drill, obtain independent maintainer review, and verify remote CI runs across declared platforms before release.
- Status: local evaluation deliverable ready; production release BLOCKED.
- Human/platform blockers: actual declared CI results, current-host drills, non-author developer, independent rubric reviewer and maintainer signoff. Do not shrink denominator or invent participants.
- Historical observations: 168 unit tests ran with seven skips; package/automated broken-link smoke checks passed after helper fixes. These are not current candidate-bound or human evidence.
- Concurrent ownership: portable-context wip-0007 belongs to another root. Do not infer its approval/closure from READY cache output; revision MISMATCH and historical completion language remain explicit limitations.
- Integration/deployment: current local corrective work only; not shipped. No background monitors or release automation scheduled.

## Verification record

Fresh command results and independent review will be appended after execution. Candidate-001 raw logs stay historical; overwritten attempts cannot be reconstructed as complete raw evidence. Required unmet criteria remain blocked/unverified even if local command checks pass.
