# Arm sonnet-5 @ max — completion report (2026-08-17)

**Status: COMPLETE AND ACCEPTED-PENDING-OPERATOR-READ.** The halt
(`halt-report-2026-08-17.md`) was adjudicated same day: operator ruled
completion with the output cap raised to 128K. This report records the
completed arm.

## Headline

**Stability 130/150 = 0.8667 — below the ≥ 0.90 gate.** Against the D3
xhigh figure (128/150 = 0.853), pinned `max` bought **+2 items of
unanimity for 3.4× the token cost** (21.25M vs 6.22M contract-metric)
plus the compliance degradation documented in the halt report and
F-008–F-011. Effort does not rescue the cheapest arm on this evidence.

- 20 non-unanimous items; dye-et-al-2023 alone contributes 11 of them
  (its data_fair F2/F3/F4 block flips together — the supplement-only
  deposit boundary remains sonnet's least stable judgement).
- Recount replicates the registered derivation
  (`analyse-benchmark-disagreements.py` unanimity definition) for a
  single arm; the registered tool's own three-arm layout runs at the
  summary stage, and the fresh-context re-derivation (contract H13) is
  due before any gates ruling.

## Completion path (three workflow runs, declared split provenance)

| Run | Items | Outcome |
|---|---|---|
| `wf_46738e9f-9a3` (primary, commit `a042c50`, cap 64K) | 15 | 11 clean; 4 unusable; 14 dead retry transcripts |
| `wf_0d67dbff-d2b` (re-run, commit `d6c35eb`, cap 128K) | 4 | dye r2, dye r3, crema r2 clean; key r2 failed again (repo-root Glob) |
| `wf_63013f81-a3a` (re-run 2, commit `d6c35eb`, cap 128K) | 1 | key r2 clean on the third attempt |

- **The 128K cap eliminated the retry churn**: zero dead attempts across
  both re-run rounds (vs 14 in the primary run at 64K) — F-008's
  mechanism confirmed by intervention, not just diagnosis.
- **key r2 is the arm's recurring specimen**: contract-schema violation
  (attempt 1), repo-root Glob (attempt 2), clean (attempt 3). Two distinct
  max-effort failure modes on one (paper, run) slot; noted against F-010's
  open pattern-vs-path question.
- 18 superseded transcripts (14 dead + 3 failed originals + 1 failed
  re-run); every accepted spawn reconciled by authoritative whole-dir
  passes; assembly enforced the declared two-commit provenance
  (`--allow-launch-commits`) and `--expect-effort max`.

## Effort→cost measurand (operator rider, Q4)

| Metric | D3 sonnet @ xhigh | This arm @ max |
|---|---|---|
| Contract-metric tokens (all spend) | 6,216,252 | **21,245,484 (3.4×)** |
| Output tokens, accepted spawns | 745,461 (15 spawns) | **1,984,840 (2.7×)** |
| Per-spawn output range | — | 32,953–346,283 |
| Thinking blocks, accepted spawns | — | 106 |
| Stability | 128/150 = 0.853 | 130/150 = 0.867 |

Served-effort evidence (residual R1): the 2.7× output inflation at
identical prompts/instrument, the P3 probe differential (7.5×), and the
Provenance pin in all 33 scoring transcripts triangulate served `max`.

## Environment attestations

`session_effort=xhigh` (main session; scoring spawns pinned via opts),
`billing_route=max-plan`, `output_cap=64000-primary-run/128000-reruns`,
`operator_ruling=completion-2026-08-17`. Model receipted:
`claude-sonnet-5` (no served-variant markers).

## Next per the operator's rulings

sonnet-5 @ `high` (full 15-item arm, 12M wire) launches on this arm's
closure; opus-5 @ `max` stays off unless the opus xhigh record shows
deficiencies.
