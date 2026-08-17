# D3 probe gate record — S4 + P2 (contract hardening 7)

**Date:** 2026-08-17. **Workflow runs:** `wf_56a0ba6f-93e` (first pass),
`wf_69da75f4-ab0` (aborted launch, 0 spawns, args error — no spend).
Re-probe run recorded in the addendum below.

## P2 — Bash capability in the reconcile lane: PASS

One haiku `general-purpose` workflow spawn executed Bash cleanly:
`scripts/reconcile-run.py` located; `venv/bin/python --version` returned
Python 3.13.3; `reconcile-run.py --help` printed usage (exit 0), with the
agent's report naming the v1.2 flags (`--expect-spawns`, `--require-pack`)
— the per-item C9 hard stop's mechanism is operative. No permission
prompts or tool denials reported. (Audit finding 14 discharged.)

## S4 — draft-07 conditionals through the spawn-side validator: FAIL → named retreat

The scoring-spawn API **rejects the v1.1 schema at tool registration**:

> API Error: 400 tools.11.custom.input_schema: input_schema does not
> support oneOf, allOf, or anyOf at the top level

The failure is at the schema-registration layer — the probe agent never
ran (0 tokens). This is definitive for the S4 question: the v1.1
conditional requirements (ESCALATE ⇒ `escalate_reason`; OK ⇒ scoring
blocks; the A1-exception cross-reference) cannot be enforced spawn-side.

**Retreat executed as pre-specified** (C3/C6 joint design note,
2026-08-14; contract hardening 7 — a recorded decision, not a silent
fallback):

1. The **registered schema v1.1 file is unchanged** and remains the
   contract of record.
2. `scripts/build-benchmark-args.py` v1.1 derives the **runtime variant**
   by stripping the top-level `allOf` (only); `$ref`/`definitions` are
   retained — proven acceptable by the 2026-08-03 v1.0 run, and the
   probe's error names only oneOf/allOf/anyOf.
3. The **conditional requirements enforce at the C9 reconciliation
   layer**: `reconcile-run.py` v1.3 gains `--contract-schema`, validating
   every governed payload in full against the registered file (Python
   jsonschema, draft-07 — `allOf` supported); the workflow's per-item
   reconcile command and the authoritative per-arm pass both carry the
   flag. Anchor test:
   `tests/test_reconcile.py::test_contract_schema_enforces_moved_conditionals`
   (an ESCALATE payload without `escalate_reason` fails at
   reconciliation, validated against the real registered file).

Consequence for run semantics: a conditionally-invalid output is caught
post-spend at the per-item reconcile stage (verdict `fail`) rather than
pre-emission — acceptable because the per-item stage is the hard stop
that already gates acceptance, and the live receipt gate's checks are
unchanged.

**Probe-schema note:** the S4 probe's schema was the registered v1.1
constraint structure with description annotations trimmed for the call;
constraint-wise byte-equivalent. The 400 depends only on the presence of
top-level `allOf`.

## Addendum — re-probe after the retreat

(Recorded after the re-probe run; expected: the runtime variant is
accepted and an ESCALATE-shaped output validates.)
