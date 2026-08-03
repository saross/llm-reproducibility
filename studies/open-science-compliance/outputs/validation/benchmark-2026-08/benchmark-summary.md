# Validation benchmark summary — 2026-08-03

**Design:** amendment 1 §3 (lodged 2026-08-03, registration DOI
10.17605/OSF.IO/DQNHG). Three arms × five pilot papers × three runs = 45
scoring spawns. Uniform configuration: corpus-store `vor.pdf` as sole paper
source (supplements deliberately excluded), output schema v1.0, FAIR
instrument v2.0 pushed with receipts, default-temperature sampling, fresh
spawns with no shared context. Per-arm verification, receipts, isolation
evidence, per-spawn token usage, and item-level disagreements are in each
arm's `run-record.json`.

## Registered statistics

Stability = unanimity proportion across three runs (150 items: 5 papers × 2
artefact types × 15 sub-principles). Concordance = majority-vote item
agreement with the E8-registered pilot reference scores (same statistic, per
amendment §3). Both gates: ≥ 0.90.

| Arm | Model ID reported | Stability | Concordance | Gates |
|---|---|---|---|---|
| sonnet-5 | `claude-sonnet-5` | 121/150 = 0.807 | 0.773 | both BELOW |
| opus-5 | `claude-opus-5[1m]` | 131/150 = 0.873 | 0.807 | both BELOW |
| fable-5 | `claude-fable-5` | 122/150 = 0.813 | 0.820 | both BELOW |

**No arm is eligible for census selection under the amendment §3 rule as
measured.** Pre-fix reliability results recorded per amendment §2.

## The disagreement is item-structured, not random

Recurring across all three arms: A1.2 (auth-where-needed — the instrument
does not say how to score a fully open resource that needs no
authentication), R1.1 (which artefact's licence counts), A2 (metadata
persistence for supplement-only deposits), R1.3 (community-standards
judgement), and the F-block target question (whether a DOI-bearing
*upstream* dataset counts toward the paper's own data FAIR — dye-et-al-2023
flips 6–13 on data FAIR within the Fable arm on exactly this). The most
capable model does not resolve the instability, and the three arms disagree
with the reference in overlapping places: this is evidence about the
instrument (amendment §3's framing), not about any model.

Concordance is additionally depressed by configuration: the pilot reference
scores were produced with reproduction-informed context; the census lane
scores from the paper alone. That gap is a property of the census
configuration being validated, not an error.

## Registered decision paths (registrant's call, amendment §2)

1. **One routing-fix attempt** (content-delivery only; instrument text
   untouched) followed by a single re-run of the §8(a) stability check.
   Candidate routing fix consistent with §2: push the FAIR-principles
   interpretation guide (`fair-principles-guide.md`, currently pull-only —
   receipts show inconsistent pulling across spawns) to all scoring spawns,
   making interpretive context uniform. If the re-run remains below
   threshold, the registered majority-vote consequence applies with no
   further iteration.
2. **Majority-vote census** (registration §8(a) consequence): the census is
   scored by majority vote of three independent runs. Which arm runs it is
   a selection question the amendment's cost rule answers only among
   *eligible* arms; with none eligible, the reading (cheapest arm under
   majority vote) should be recorded explicitly when decided.
3. **Instrument clarification via gated amendment** (erratum log → OSF
   amendment 2): resolve the A1.2 no-restriction case, the R1.1 licence
   target, and the F-block upstream-crediting question in the instrument
   text, then re-benchmark. Slower; addresses cause rather than symptom.

## Usage

4,246,831 tokens across 45 spawns (sonnet 1,313,017; opus 1,535,598; fable
1,398,216); per-spawn range 35k–130k. Approximate API-equivalent cost ≈ $27
(sonnet ≈ $3 at intro pricing, opus ≈ $8.5, fable ≈ $15.5), Max-plan
allocation absorbing part per the billing decision. Per-spawn figures are in
the run records for future estimation.
