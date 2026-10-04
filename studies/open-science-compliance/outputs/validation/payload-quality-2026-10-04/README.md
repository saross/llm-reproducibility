# Payload quality, Layer 1 rules v1.1 (2026-10-04)

A retroactive run of the payload-quality checker, rules version 1.1, over the
nine committed validation arms: 135 FAIR (Findable, Accessible,
Interoperable, Reusable) scoring payloads, which are 9 arms × 3 runs × 5 pilot
papers.

## Purpose

Rules v1.1 implements Layer 1 of the mechanical-check policy that Shawn ruled
on 2026-10-04 ("Disagreement policy", item 1, in the planning note). The
policy covers derived quantities: section totals, `coverage_percentage`, and
`coverage_category`. The checker computes them from the scored items and the
dataset counts rather than merely checking them. On disagreement the
computed value governs automatically, and the model's value is kept only as a
consistency signal. Every finding records both values, the rules version, and
which value governed.

The payload files are evidence and were not modified. Computed values exist
only in `report.json`.

Check identifiers follow the planning note's Layer 1 table:

| Check | Rule | Kind on a hit |
| --- | --- | --- |
| C1 | Section `total` = sum of its 15 items | derived |
| C2 | `coverage_percentage` = 100 × accessible / enumerated | derived |
| C3 | `coverage_category` from the exact fraction | derived |
| C4 | A1 cross-reference, on the governing category | failure |
| C5 | `available: false` with any item scored 1 | flag |
| C6 | Every `pack_refs` id is in the paper's evidence pack | failure |

A *derived* hit is resolved by computation, so the computed value governs. A
*failure* fails the run. A *flag* goes to human review and never overrides a
score. The C2 tolerance is 0.5 percentage points (pp), inclusive. The C3
category reads the instrument's bands as intervals on the exact fraction
accessible / enumerated: complete only when every enumerated dataset is
accessible, substantial from 0.75, partial from 0.25, and minimal below that.
The governing category is the computed one, unless the derivation is
undefined (zero datasets enumerated), in which case the recorded one stands.
The reasoning for the tolerance and the boundaries is in the script's module
docstring (`scripts/check-payload-quality.py`).

## Invocation

Run from the repository root at commit `132f95a` (rules v1.1), in default
(non-strict) mode:

```bash
V=studies/open-science-compliance/outputs/validation
venv/bin/python scripts/check-payload-quality.py \
  --json $V/payload-quality-2026-10-04/report.json \
  $V/benchmark-2026-08-17/arm-sonnet-5 \
  $V/benchmark-2026-08-17/arm-opus-5 \
  $V/benchmark-2026-08-17/arm-fable-5 \
  $V/effort-study-2026-08-17/arm-sonnet-5-high \
  $V/effort-study-2026-08-17/arm-sonnet-5-max \
  $V/effort-study-2026-08-17/arm-opus-5-high \
  $V/opus-5-5-arms-2026-10/arm-opus-5-5-high \
  $V/opus-5-5-arms-2026-10/arm-opus-5-5-medium \
  $V/opus-5-5-arms-2026-10/arm-opus-5-5-xhigh
```

The exit status was 0: there were no failures, and in default mode derived
disagreements and flags are reported but do not fail the run. With `--strict`
the same input exits 1.

## Results

| Arm | Payloads | C1 totals | C2 % | C3 category | C4 A1 | C5 flags | C6 refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| benchmark-2026-08-17 / sonnet-5 | 15 | 0 | 0 | 0 | 0 | 0 | 0 |
| benchmark-2026-08-17 / opus-5 | 15 | 0 | 0 | 0 | 0 | 0 | 0 |
| benchmark-2026-08-17 / fable-5 | 15 | 0 | 0 | 0 | 0 | **1** | 0 |
| effort-study-2026-08-17 / sonnet-5-high | 15 | 0 | 0 | 0 | 0 | 0 | 0 |
| effort-study-2026-08-17 / sonnet-5-max | 15 | 0 | 0 | 0 | 0 | 0 | 0 |
| effort-study-2026-08-17 / opus-5-high | 15 | 0 | 0 | 0 | 0 | 0 | 0 |
| opus-5-5-arms-2026-10 / opus-5-5-high | 15 | 0 | 0 | 0 | 0 | 0 | 0 |
| opus-5-5-arms-2026-10 / opus-5-5-medium | 15 | **1** | 0 | 0 | 0 | 0 | 0 |
| opus-5-5-arms-2026-10 / opus-5-5-xhigh | 15 | 0 | 0 | 0 | 0 | 0 | 0 |
| **All nine arms** | **135** | **1** | **0** | **0** | **0** | **1** | **0** |

No payload had ESCALATE status, none was malformed, and no coverage derivation
was undefined (no paper had zero enumerated datasets). Letting the computed
category govern changed no A1 outcome, because the computed and recorded
categories agree in all 135 payloads.

### The two findings

1. **C1, derived: opus-5-5 `medium`, run 3, `dye-et-al-2023`, `code_fair`.**
   The recorded total is 7 and the 15 items sum to 8, so the computed 8
   governs. This is the miscount flagged by H13 in the Opus 5.5 arm results
   (`../opus-5-5-arms-2026-10/results-2026-10-04.md`), which prompted the
   policy. Under policy item 1 ("Review"), the items get a spot check, not a
   block, because a miscount can also mean the model wavered on an item. The
   gate statistics use items, so they are unaffected.
2. **C5, flag: fable-5 (benchmark-2026-08-17), run 1, `key-et-al-2024`,
   `data_fair`.** The block records `available: false` but scores R1 as 1. The
   model's scores stand, and the item goes to human review. The H13
   re-derivation recorded the same anomaly and used the scores as recorded
   (`../h13-rederivation-2026-10-04/report.md`, "Anomalies", item 1).

An independent `jq` pass over the same 135 payloads, written separately from
the checker, reproduced both findings and the zero counts for C2, C3, and C4.

## Scope

The nine arms are the 2026-08-17 benchmark, the 2026-08-17 effort study, and
the 2026-10 Opus 5.5 arms. The three 2026-08-03 benchmark arms under
`../benchmark-2026-08/` are not included. They were scored on output schema
v1.0 and FAIR instrument v2.0 (`../benchmark-2026-08/benchmark-summary.md`).
That was before the `a1_exception_rationale` field and the evidence packs
existed, so their payloads cannot name an A1 exception or cite pack records,
and these rules are not a like-for-like fit for them.

## See also

- Planning note and the ruled policy:
  [`wiki/planning/deterministic-output-checks.md`](../../../../../wiki/planning/deterministic-output-checks.md)
  (sections "Layer 1" and "Disagreement policy").
- Checker and tests: `scripts/check-payload-quality.py` and
  `tests/test_payload_quality.py`.
- Machine-readable findings and per-arm summaries: `report.json` (this
  directory).
