# E8-v2 re-derivation — adjudication log

**Purpose:** sitting-by-sitting record of the registrant's adjudications on
`worksheet.md` (amendment 2 §3 procedure), and the running list of **forward
principles** — rulings made on one section that the registrant has directed
be applied forward to later sections ("if/when we record a decision that's a
principle that can be applied forward to other rulings, please do apply it
forward" — Shawn, 2026-09-03). The worksheet carries per-item scores and
short notes; the reasoning lives here. Registrant: Shawn; clerk: Claude.
Exercise is unblinded (recorded in amendment 2 §3).

## Forward principles (applied to every subsequent section)

- **AP-1 — Scores assess the published research surface; repair is
  score-independent.** An explicitly cited unreliable source (e.g. a
  personal server) fails the criteria it fails; a successful repair is
  documented as a *recoverable error* finding and never lifts a score.
  Differential scoring of recoverable vs unrecoverable errors is **held in
  reserve**, not adopted. (Shawn, 2026-09-03; consistent with the
  research-surface rule and the identifier-recovery precedent.)
- **AP-2 — "Paper" includes the published supplement** for rung-(i)
  evidence and the census-surface (S) check. Supplements live in the corpus
  store and scoring spawns can read them; the evidence pack is structurally
  blind to supplement-embedded artefacts, so S=y with a pack-blind note for
  facts that require the supplement. Code published as a supplement is
  available and DOI-covered (F1 via item 5) with no intrinsic failure mode;
  its weaker metadata surface is judged case-by-case. (Shawn, 2026-09-03.)
- **AP-3 — Personal-server artefacts:** where a required artefact is served
  from a personal/unmanaged host it is principal if reproduction needs it,
  and it fails what the evidence shows it fails (typically F1 no-PID, A2
  no-persistence, R1.1 no-licence). Dye precedent:
  `https://tsdye.online/AP/beads-1.csv` (Bluehost shared hosting,
  last-modified 2022-10-20; live at 2026-09-03 check). (Shawn, 2026-09-03.)
- **AP-4 — Conjunction blocks entitlement lifts.** Under the aggregation
  rule a platform entitlement (e.g. ADS R1.3-by-construction) can never
  raise a conjunctive score unless *every* principal artefact qualifies.
  The worksheet's ENTAILED flags were computed per sub-principle and are
  advisory only — each is re-checked against the aggregation rule at
  adjudication. Dye precedent: the anticipated R1_3 data flip was rejected.
- **AP-5 — Registry curation practice:** supplement-embedded artefact URLs
  enter `corpus/evidence-packs/declared-links.yaml` when found, so census
  packs record their status even where no routing endpoint exists (the
  harvester logs them as honest gaps). (Shawn, 2026-09-03.)
- **AP-6 — Repair rule** (two routes, above-and-beyond, good-will;
  full text `protocol/data-repair-rule-2026-09-03.md`): (a)
  archived-equivalent retrieval where a proper deposit of the at-risk
  artefact exists; (b) documented re-derivation from archived/published
  inputs where only the generator is archived. (Shawn, 2026-09-03.)
  **Effort bound (initial heuristic, Shawn, 2026-09-03, second ruling):**
  up to ~3× the dye estimate (≈ one to two sessions, ~6–12 h wall-clock,
  modest CPU on sapphire, Claude Max session work) proceeds without
  discussion; above that, discuss first. Refine empirically from the
  recorded cost of each repair.
- **AP-7 — Anti-perversity generalisation check** (Shawn, 2026-09-03):
  before applying any adjudication precedent forward, ask *"does
  generalisation of this precedent produce any foreseeable perverse
  result?"* — and record the answer whenever it is not obviously no.
  Type case: the dye code_fair precedent (dependency evidence
  inadmissible for principal-artefact scores) must not penalise a paper
  that cites versioned CRAN packages and properly deposits a specific
  wrapper script — there the wrapper is the principal artefact and
  scores on its own (good) deposit; dye's penalty attaches to the
  principal scripts' publication quality, never to the fact of using
  dependencies. Noted foreseeable edge, not yet ruled: a paper whose
  entire analysis is a bare invocation of a dependency with no custom
  code — the principal-script set is empty and conjunctive scoring needs
  a convention; rule it when a paper poses it.

## Sitting 1 — 2026-09-03 — dye-et-al-2023 `data_fair`: 9 → 7

**Principal-set ruling (P1):** principal data = the supplement contents
(OxCal model, probability tables) **plus** the personal-server MCMC file
`beads-1.csv` that the supplement's R code reads (reproduction
`attempt-01/log.md:44`, `environment.md:40`). The ADS deposit
(10.5284/1018290) is the *upstream third-party raw* dataset — non-principal;
it enters through I3 (qualified reference, scores 1) and the
data-completeness lane.

**Flips:** F1 1→0 (beads-1.csv has no PID; conjunctive — flips *against*
the opus/fable arm majority); A2 1→0 (row 6: supplement-only A2=0;
personal server has no persistence entitlement — the sonnet minority had
the v2.1-correct reading). **Confirmed 0:** F2/F3/F4 (row 6), I2, R1.1
(beads-1.csv carries no licence anywhere; the CC-BY-NC-ND clarity question
is moot for this artefact set), R1.3 (ENTAILED flip rejected per AP-4).
**Confirmed 1:** A1, A1.1, A1.2, I3, I1 (OxCal formal language + CSV), R1
(Methods + 50-page supplement), R1.2 (seeded spot-check confirmed;
provenance chain ADS → OxCal model → MCMC documented). Registrant's note
on R1.2: the score recognises that a plausible chain-of-FAIR-compliance
exists — partly what a future stand-alone "can this be
reconstructed/repaired" process would test.

**S column:** y on all 15 (AP-2); F1, A2, and R1.1 carry the pack-blind
note — their evidence requires the supplement PDF.

**Repair status (score-independent, AP-1/AP-6):** dye is route (b) —
no archived copy of the MCMC output exists anywhere; re-derivation =
re-run the supplement's OxCal model (dates embedded; OxCal + IntCal20
public) and compare statistically, tolerance framed by the authors' own
five-run replicability analysis (Supplement §3, Table 1). Queued as
reproduction attempt-02 pending the registrant's acceptance of the effort
estimate.
