---
title: "Instrument clarification plan — amendment 2 route"
tags: [governance, validation, planning]
created: 2026-08-03
updated: 2026-08-03
status: active
---

# Instrument clarification plan — amendment 2 route

**Decision (Shawn, 2026-08-03):** the amendment 1 §2 routing-fix card is
declined as the candidate stood; the project takes the instrument-
clarification route (benchmark summary, registered decision path 3).
Overriding goal: a robust and useful instrument — root problems are solved
even where that requires errata or a further amendment. Shawn contributes
FAIR (Findable, Accessible, Interoperable, Reusable) domain expertise at
Phase B.

**Compliance position.** The preregistration's erratum-then-amendment
mechanism is established practice in this project (amendment 1 lodged
2026-08-03, Open Science Framework (OSF) registration Version 2, DOI
10.17605/OSF.IO/DQNHG). Amendment 2 will be dated and lodged *before* the
re-validation it governs, and both pre-fix and post-fix reliability results
are reported with study outcomes, per amendment 1 §2's reporting rule
(`studies/open-science-compliance/prereg/amendment-1-draft.md:109–118`).
Because amendment 2 changes instrument text, it re-specifies the validation
check itself; the §2 ladder is restated within amendment 2 rather than
consumed (see Phase D).

## Evidence base (verified 2026-08-03, this session)

- **The routing-fix premise held only for the sonnet arm.** Pull receipts
  (`.receipts.pulled_files_read` across
  `studies/open-science-compliance/outputs/validation/benchmark-2026-08/arm-*/run-*/*.json`):
  sonnet-5 pulled `fair-principles-guide.md` in 9/15 spawns; opus-5 and
  fable-5 in 15/15 each. Both full-pulling arms failed both 0.90 gates
  (stability 0.873 / 0.813; concordance 0.807 / 0.820 —
  `benchmark-summary.md`).
- **The disagreement is item-structured and survives full guide exposure.**
  Top disagreement sub-principles in the full-pulling arms: R1.1 (5 and 4
  items), A1.2 (4 and 4), A2 (2 and 4), plus R1.3, I3, and the F-block
  upstream-crediting question (dye-et-al-2023 flips 6–13 on data FAIR
  within the fable arm).
- **The interpretation guide is silent on the disputed cases.** Its A1.2
  guidance
  (`.claude/skills/research-assessor/references/infrastructure/fair-principles-guide.md:180–184`)
  covers restricted-with-justification and closed-without-justification but
  never the fully-open, no-authentication-needed case; the R1.1 licence
  target and F-block upstream questions are likewise unaddressed. Pushing a
  document that does not contain the answer cannot make the answer uniform.
- **Within sonnet, guide absence does correlate with instability** — of its
  29 disagreement items, roughly 17 have the minority vote from a guideless
  spawn against ~11 expected by chance (hand-tallied 2026-08-03 from
  `arm-sonnet-5/run-record.json` `.stability.disagreements` plus receipts;
  the Phase A script re-verifies this figure). Real but secondary: the
  binding constraint is concordance, which no delivery fix plausibly lifts
  from 0.773 to 0.90 when full-exposure arms sit at 0.807/0.820.
- **The concordance gate is structurally confounded** (benchmark summary):
  reference scores were produced with reproduction-informed context under
  the pre-clarification instrument; the census lane scores from the paper
  alone. Phase B addresses this.

## Phase A — root-cause analysis and clarification drafting (no API spend)

- [x] 2026-08-03 **A1. Disagreement mining pass.** Script recomputes stability and
      concordance from the 45 spawn outputs and the E8-registered reference
      scores (`manifest.yaml:510–533`), verifying the published figures;
      extracts every disputed item (within-arm disagreement or
      majority-vs-reference mismatch) with each spawn's `evidence` string;
      clusters by sub-principle and ambiguity class. Outputs:
      `disagreement-analysis.md` (+ machine-readable `disputed-items.json`)
      in the benchmark package. Also re-verifies the sonnet
      guideless-minority correlation above.
- [ ] **A2. One clarification draft per ambiguity class**, each an
      erratum-log entry with proposed replacement instrument text and the
      observed failure it resolves. Known five (mining may add more), each
      a scoring-policy decision for Shawn:
      - A1.2 — does a fully open resource needing no authentication score 1?
      - R1.1 — which artefact's licence counts?
      - A2 — metadata persistence for supplement-only deposits.
      - R1.3 — what counts as a domain-relevant community standard?
      - F-block — does a DOI-bearing *upstream* dataset credit the paper's
        own data FAIR?
- [ ] **A3. Align `fair-principles-guide.md`** with the clarified text and
      decide its routing (candidate: promote pull → push so interpretive
      context is uniform by construction; rides amendment 2's delivery
      spec, subsuming the §2 card question).

### Working position on decision point #1 (2026-08-10, pending scout)

**The assessment target is the "research surface"** (Shawn's framing): the
study assesses credibility — reproducibility, transparency, FAIRness — from
a reviewer's, funder's, or consumer-researcher's standpoint. What matters is
what the available research surface of the publication supports as the
culmination of the research programmes that produced it (the authors' work
and whatever the authors chose to utilise), not who created or deposited any
given artefact. Consequences accepted:

- Well-archived third-party inputs earn full credit; closed or unpublished
  inputs are penalised even where blameless — the empirical status of the
  research is what is measured, fault is not.
- Decision points #1 and #8 merge: the coverage denominator and the
  assessment object are the same rule ("the set of artefacts required to
  reproduce the result").
- **Provenance is recorded as a per-input flag** (author-deposited /
  third-party / undeterminable) that never touches scores — keeping fault
  visible as a reportable *finding* (e.g. the share of FAIR failures
  attributable to upstream artefacts). Flag rides the schema work (C3).
- The aggregation rule for heterogeneous input sets is acknowledged
  non-trivial: make a reasonable initial choice, iterate until results
  "vibe right" against pilot papers, and declare instrument refinement an
  explicit research goal as the study expands.
- Final ruling deferred until the prior-art scout report
  (`wiki/planning/scout-reports/2026-08-10-fair-third-party-artefacts-prior-art.md`)
  is in and verified, so any departure from field convention is deliberate
  and citable.

**Stretch goal (not scheduled):** a sidecar report per paper — "how did
these researchers, at their stage of the greater research chain, do on
reproducibility?" — crediting value added (data/code clean-up, artefact
quality). Side quest; recorded so it is not lost.

## Phase B — concordance-reference decision (Shawn + Claude)

The E8 reference scores are old-instrument, reproduction-informed; the
census lane is new-instrument, paper-only. Comparing across both axes is
incoherent and structurally caps concordance below the gate. Options
(Claude's preference order; Shawn decides with FAIR expertise):

- [ ] **B1 (preferred). Re-derive reference scores** under the clarified
      instrument and census configuration, anchored by human adjudication
      (the preregistration's n=12 human-validation subsample can seed
      this); register the new set as an E8 update, retaining the old set.
- [ ] **B2. Redefine the concordance check** in amendment 2 to compare
      like-with-like another way.
- [ ] **B3. Keep the gate as-is** — advised against: a structurally
      unreachable gate measures nothing.

## Phase C — harness hardening (pre-census register, runs in parallel)

Register of record: `wiki/planning/audit-2026-08-03-follow-ups.md`.

- [ ] **C1. Audit fix round 2** — all seven register items; priority to the
      receipt-gate binding (re-audit C-2) and gate logging/field-names
      (re-audit C-1).
- [ ] **C2. Capture one live SubagentStop event** (single cheap probe
      spawn) to confirm real field names; then the live pass-plus-catch
      demonstration. Gate counts as operative only after both.
- [ ] **C3. Schema v1.1** (C6 ESCALATE-forces-fabrication; M12; M13) plus
      its supply mechanism (currently orchestrator-side only).
- [ ] **C4. C7 GOVERNED decision (Shawn):** add `sha256:` content-integrity
      hashes to `shared_content` entries alongside the amendment 2
      instrument edits, so clarified text lands hash-checked from day one.
- [ ] **C5. `unwrap-paste-file.py` M14–M16 fixes** with a self-check —
      due before amendment 2's paste artefact.

## Phase D — amendment 2, re-benchmark, then the registered ladder

- [ ] **D1. Consolidate amendment 2:** instrument clarifications (A2
      outputs), concordance-reference decision (B), guide routing (A3),
      the remediation ladder restated for the new check (carry §2's
      structure: one routing-fix attempt, single re-run, else majority
      vote), plus the two escaped-comparator cosmetic fixes flagged at
      amendment 1 lodgement.
- [ ] **D2. Lodge** via the proven OSF API route (versioned registration
      update; DOI unchanged).
- [ ] **D3. Re-benchmark** on the clarified instrument, schema v1.1, and
      fixed harness — same design (3 arms × 5 papers × 3 runs = 45 spawns,
      ≈ $27 API-equivalent at benchmark rates), harness
      `studies/open-science-compliance/protocol/validation/fair-benchmark-arm.workflow.js`.
      Standing API review gate presented before the run.
- [ ] **D4. Gates → selection → census.** Pass: cheapest eligible arm,
      registered regression gate, census. Still below: majority-vote
      consequence, now with a defensible claim that the residual is
      irreducible; arm choice recorded explicitly.

## Decision log

| Date | Decision | By |
|---|---|---|
| 2026-08-03 | Routing-fix card declined as candidate stood; instrument-clarification route (path 3) adopted; robust-instrument goal overrides speed-to-census | Shawn |
| 2026-08-03 | Phase B to draw on Shawn's FAIR expertise; plan externalised to this file | Shawn |
| 2026-08-10 | Working position, decision point #1: assessment target = the research surface (empirical status, fault-free); ruling deferred to the verified prior-art scout report | Shawn |
| 2026-08-10 | Provenance flag accepted: per-input author-deposited / third-party / undeterminable metadata, never affecting scores; upstream-attributable failures become findings | Shawn |
| 2026-08-10 | Aggregation rule: reasonable initial choice, then iterate; instrument refinement declared an explicit research goal for the study's expansion | Shawn |
| 2026-08-10 | Amendment 2 names the assessment-object definition the **research-surface rule** (framing endorsed) | Shawn |
