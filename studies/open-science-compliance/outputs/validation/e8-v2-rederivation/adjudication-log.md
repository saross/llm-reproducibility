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
- **AP-6 — Repair rule** (three routes since 2026-10-02, above-and-beyond, good-will;
  full text `protocol/data-repair-rule-2026-09-03.md`): (a)
  archived-equivalent retrieval where a proper deposit of the at-risk
  artefact exists; (b) documented re-derivation from archived/published
  inputs where only the generator is archived. (Shawn, 2026-09-03.)
  **Route (c) added (Shawn, 2026-10-02, with AP-9):** format recovery —
  extracting code or data from a non-machine-actionable carrier (e.g. code
  printed in a PDF), verified by parsing, running, and matching published
  outputs. Like (a) and (b), it is score-independent and reported as a
  recoverable or unrecoverable error.
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
- **AP-8 — R1.1 is a clarity test, not a permissiveness test** (Shawn,
  2026-10-01). R1.1 = 1 when a usage licence is published for the artefact
  at all — however restrictive, and even where it is not entirely
  appropriate to the artefact type. Same-artefact contradictions still
  resolve to the most restrictive licence (item 6), which passes if it is
  itself a published licence. A Creative Commons licence applied to code is
  a non-fatal author/outlet error that signals intent to make the code
  available: recorded as a finding, never a fail. Restrictiveness can bear
  on other parts of an assessment (e.g. whether code can be run or adapted
  without breaching its licence) but is not R1.1's gate. Coheres with the
  instrument's A1.2 stance (CARE-compliant restriction is a positive
  signal); a permissiveness gate would penalise clearly licensed sensitive
  data (AP-7). **Boundary (Shawn, 2026-10-02):** "available on request" →
  0 — no usage licence is published. **"All rights reserved" → 0 (Shawn,
  2026-10-02, on the survey `rights-reserved-survey-2026-10-02.md`):** an
  "all rights reserved" notice is not a licence to *do* anything, under any
  circumstances. The test is any grant versus no grant, never how much is
  granted. Guards (endorsed): (i) the rule turns on the absence of any
  grant, not the phrase — a grant followed by "all other rights reserved"
  passes; (ii) a copyright notice alongside a licence is not a
  same-artefact conflict — the most-restrictive rule compares licences
  with licences, never a notice with a licence. This matches the pushed
  guide's existing line, so it needs no `rule` tag and no guide change.
  Backward
  consistency: Sitting 1's dye data R1.1 = 0 stands — conjunction with
  beads-1.csv, which carries no licence anywhere.
- **AP-9 — I1 assesses the artefact as served: is it machine-actionable as
  published?** (Shawn, 2026-10-02.) Code or data available only as text or
  tables inside a PDF fails I1, whatever the formal language underneath;
  extraction is reconstruction (repair route (c)), not an executable
  download. Rationale (registrant): machine-actionability is expected by
  the original FAIR principles — Wilkinson et al. 2016: "the FAIR
  Principles put specific emphasis on enhancing the ability of machines to
  automatically find and use the data, in addition to supporting its reuse
  by individuals" (abstract; verified 2026-10-02, see
  `rights-reserved-survey-2026-10-02.md`) — and "human-only FAIR" is
  generally seen as a defect; whitespace-significant languages such as Python make
  code-in-PDF as layout-dependent and unreliable to extract as a table.
  Clerk's supporting arguments, endorsed: scores must be properties of
  papers, not of assessor tooling (a repairability test would score the
  same paper 0 in 2020 and 1 in 2026); and "repairable → pass" fails AP-7
  — almost everything is now model-repairable, so I1 would stop
  discriminating and proper deposit would earn no credit. Guards (AP-7,
  endorsed): (i) where the same artefact is also served in a
  machine-actionable form, I1 scores the best form, so printing code for
  readers alongside a proper deposit is never penalised; (ii) illustrative
  snippets are not principal artefacts and never enter I1. Accepted
  consequence: outlets that accept only PDF supplements push their authors
  to 0 — consistent with the research-surface rule, with responsibility
  recorded as non-scoring provenance. File format is scored only at I1, so
  this counts no fact twice. **Held in reserve:** a "human FAIR vs machine
  FAIR" refinement scoring actionability separately (registrant notes a
  lively discourse on this).

- **AP-10 — Completeness counts only what reproduction requires** (Shawn,
  2026-10-02; the purposive reading, generalised to analogous cases). An
  upstream source enters the data-completeness coverage denominator only if
  reproducing the reported results needs it — the aggregation rule's "full
  *required* set". A source that the authors have fully transcribed or
  derived into the deposited analysis inputs is provenance: it is scored at
  R1.2 and listed in the completeness inventory with its tier, but it is not
  counted. Guard (AP-7): if a transcription is partial and the results need
  fields that exist only in the source, the source is required and counts.
  Perverse result avoided: the literal reading would penalise authors for
  digitising and depositing an analogue source, and reward not citing it.
  A disambiguation of pushed text (seven of nine v2.1 runs read it this
  way), so no BI tag; on the pre-census clarification list. Herskind
  precedent: Płonka (2003), a printed catalogue (Tier 3), fully transcribed
  into S1.xlsx.
- **AP-11 — R1.3 route (a): a DataCite-registered deposit with its mandatory
  metadata passes** (Shawn, 2026-10-02; option (a), applying ratified
  erratum-log item 7 as written). A deposit's DataCite record is compliance
  with a generic community metadata standard. The poverty of a minimal
  record is scored at F2, not R1.3, so passing R1.3 hides nothing.
  Accepted property: for data, R1.3 then nearly coincides with "has a
  DataCite deposit" and does not separate domain-standard deposits from bare
  ones. F-UJI makes the same distinction as a gradient (multidisciplinary
  standard at maturity 1, community-specific at 3); a graded R1.3 is
  **held in reserve** with differential scoring.
  **Scope (Shawn, 2026-10-02, Sitting 4): data only.** For code, R1.3 uses
  the instrument's code list — package structure, CITATION.cff, CodeMeta,
  or community review (CRAN, JOSS, rOpenSci) — which replaces routes
  (a)–(c) for code. Reasons: code has well-defined, low-cost community
  standards, so R1.3 can separate packaged or citable code from a bare
  script; extending route (a) would pass every Zenodo code deposit and
  make R1.3 track deposit location only (AP-7); and a DataCite record
  typed "Dataset" does not describe the code as software. Eight of nine
  v2.1 runs read the instrument this way, so no BI tag.
- **AP-12 — Which version of a versioned deposit is scored and reproduced**
  (Shawn, 2026-10-02, with clerk refinements). In priority order: (1)
  published supplementary files, by checksum match against the repository
  versions — the supplement is the publisher's record of what was
  published (AP-2); (2) the version the paper cites, if it cites exactly
  one; (3) the latest version published on or before the article's first
  online appearance (Crossref `published-online`, else the record's
  `created` date, as proxy). A concept DOI (all versions) resolves to the
  latest version, which may post-date the paper, so rule (3) applies to it.
  Versions published after the article are out of scope for scoring (the
  published surface, AP-1) and are recorded as findings, not flaws —
  updating datasets is normal. A paper citing two different versions is a
  minor citation-inconsistency finding. Pre-census: the harvester must
  record each repository record's version, version date, and concept DOI.
  Herskind precedent: the methods cite v1 (10.5281/zenodo.10623550, 2024-02-06),
  the data-availability statement cites v2 (10.5281/zenodo.10801706,
  2024-03-10), the article first appeared 2024-04-03; the publisher's
  supplement files match v2 byte for byte, and rule (3) also selects v2.

- **AP-13 — Unpublished principal data fail conjunctively** (Shawn,
  2026-10-03; option (β)). Under the aggregation rule a sub-principle holds
  only if it holds for every principal dataset. An unpublished or closed
  principal dataset has no persistent identifier, no retrieval protocol, no
  access mechanism, and no licence, so F1, A1.1, A1.2, and R1.1 (and every
  other artefact-property sub-principle) fail — the registered
  "unscoreable → 0" default applied as written. Scoring the article or its
  published summary statistics as if they were the data ("the accessible
  portion", option (α)) is rejected: it is the error that inflated the old
  key-et-al reference. Known property (AP-7): conjunction is harsh when
  most principal datasets are open; that harshness belongs to the ratified
  rule (flagged iterable 2026-08-10), and the completeness percentage
  carries the nuance. The arms split on the instrument text, so this is a
  clarification for the pre-census list, not a BI rule.
- **AP-14 — R1 and R1.2 can be earned from documentation when data are
  closed; the paper is not the metadata for machine-actionable
  sub-principles** (Shawn, 2026-10-03). FAIR separates metadata from data
  (A2: metadata stay accessible when data do not), so descriptive richness
  (R1) and provenance (R1.2) can be satisfied by the paper's documentation
  even for unpublished data; requiring published data would fail
  access-restricted sensitive datasets with exemplary documentation (AP-7).
  Conjunction still applies: R1.2 fails if any principal dataset's
  provenance is unstated. The counterpart, in the registrant's words:
  "I've heard the argument 'the paper is the metadata', but this is
  analogous to an earlier decision we made about information locked in a
  PDF — extracting metadata from a paper is a repair / reconstruction
  project, and FAIR expects machine-readable information." So prose in a
  paper never supplies the machine-actionable sub-principles — F2's
  structured metadata record, F3, F4, I1–I3, R1.3 — just as code inside a
  PDF fails I1 (AP-9). Consistency check, 2026-10-03: the code I3 = 1
  rulings for dye (Sitting 2) and herskind (Sitting 4) rest on dependency
  DOIs that are deposited in Crossref's machine-readable reference metadata
  for each article (`reference` entries with a `DOI` field asserted by
  Crossref: 10.18637/jss.v093.c01 among dye's 51 deposited references,
  10.21105/joss.00774 among herskind's 90), not on prose, so they stand.

## Beyond-instrument (BI) tags — concordance reporting convention

Adopted 2026-10-02 (Shawn). A reference item is tagged when its adjudicated
score rests on something the benchmark arms could not have applied, so that
the gates can report concordance **with and without** BI items rather than
grading the arms against the instrument's silences. Two reason codes, in
the worksheet note column (`[BI: …]`) and as `beyond_instrument` in
`worksheet.json`:

- `rule` — a principle adopted at adjudication that the pushed instrument
  v2.1 and guide v1.1 do not state.
- `input` — evidence the benchmark spawns were deliberately not given. The
  benchmark workflow tells every scoring spawn "The paper PDF is the sole
  paper source: supplementary files are deliberately not provided"
  (`protocol/validation/fair-benchmark-arm.workflow.js:100`); all 110
  governed spawns in the 2026-08-17 cycles read only `vor.pdf`.

Tagged so far: dye data F1 [input], R1.1 [input], I1 [input, rule]; dye
code I1 [input, rule]. Items whose reference score is derivable from the
main paper and the pack are not tagged even where the supplement adds
detail (e.g. dye code R1: all nine v2.1 runs scored 1 from the main text).
Rulings that disambiguate pushed text (AP-4, AP-8) are not `rule`-tagged;
they go on the pre-census clarification list instead.

**RULED 2026-10-02 — supplements as scoring inputs: Option A (Shawn).**
AP-2 rules that "paper" includes the published supplement, but the
benchmark workflow withheld supplements; the exclusion entered with the
original benchmark harness (`d34edd9`, 2026-08-03) with no recorded
protocol decision. Ruling: AP-2 stands and **census scoring spawns receive
published supplements** alongside the paper PDF. Amendment 2 §2's "the
paper source" is read as including the published supplement, so this
implements §2 rather than departing from it. Governance: a dated protocol
note (`protocol/supplements-as-inputs-2026-10-02.md`) plus a plan
decision-log row; no OSF amendment, as with F-010. The completed benchmark
is not re-run: its supplement-dependent reference items carry the `input`
tag, and the gates report concordance with and without them.

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
reproduction attempt-02. **Effort estimate accepted (Shawn, 2026-09-03):**
one focused session, roughly 2–4 h wall-clock, negligible compute, no API
spend; scheduled after the worksheet sittings.

**Amended 2026-10-02 — backward application of AP-9 (approved by the
registrant): data I1 1→0, data_fair 7 → 6.** The principal OxCal model is
served only as text inside the supplement PDF. BI tags added: F1 [input],
R1.1 [input], I1 [input, rule].

## Sitting 2 — 2026-10-01/02 — dye-et-al-2023 `code_fair`: 14 → 8

**Framing (no new ruling needed):** principal code = the supplement's own
scripts (OxCal model + R code), per the aggregation rule ("the paper's own
analysis scripts are always principal; third-party dependencies are never
substitutes"). Fourteen of the fifteen old scores cited ArchaeoPhases/CRAN —
the dependency — and that evidence is inadmissible for principal-artefact
scores (AP-7 type case).

**Rulings (Shawn, 2026-10-01):** **R1.1 = 1** under AP-8 — the supplement
carries no licence statement, so item 6's default extends the article's
licence to it; published licences exist (CC-BY-NC-ND on the
accepted-version cover sheet; the Elsevier licence set on the
version-of-record Crossref record in the evidence pack), so whichever
governs under most-restrictive, R1.1 passes. Finding: the code carries only
an inherited article licence (CC-on-code class, non-fatal). **R1.2 = 1** —
software versions named (OxCal 4.4.2 and the IntCal20 curve, main text p.
11), the model's derivation from Bayliss et al. (2013) with retained and
removed constraints itemised, and code authorship via CRediT. **Nods:** I3
= 1 (spot-check — ArchaeoPhases cited via Philippe & Vibet (2020), Journal
of Statistical Software, DOI 10.18637/jss.v093.c01; the printed link
carries a doubled `https://doi.org/` prefix — a citation-formatting defect
recorded as a finding; the PID itself is unambiguous); R1 = 1 (50-page
sectioned supplement); A1 = 1 (spot-check — supplement retrieved over HTTPS
from the article landing page in attempt-01; the HTTP 403 was
scripted-access-only, attempt-01 `log.md:14,65`). **Entailed set
confirmed:** F1 = 1 (supplement code under the article DOI, item 5 + AP-2
— basis corrected from CRAN); F2/F3/F4 = 0 (row 6); A1.1 = 1; A1.2 = 1
(item 4); A2 = 0 (row 6); I2 = 0; R1.3 = 0 (principal scripts carry no
package structure, CITATION.cff, CodeMeta, or community review; CRAN's
review is the dependency's).

**I1 — decision D3, ruled 2026-10-02: the as-served reading (AP-9), I1 =
0.** The supplement scripts are served only as text inside a PDF, spread
over 38 incremental sections (5.1–5.38), which attempt-01 rebuilt into a
477-line wrapper script (`attempt-01/log.md:18`, `log.md:48–51`).
Extracting them is repair route (c), recorded as a recoverable error. BI
tag [input, rule]. **code_fair total: 8** (old 14).

**Context for D3:** all nine v2.1 runs (2026-08-17 cycle) scored code I1 =
1, but every justification quotes the main paper's description of the code
(p. 11, figure captions) — none quotes the code itself, and one (sonnet r3)
calls it "not unstructured text or PDF". The arms were never in a position
to see the carrier, so their unanimity is uninformative on D3 (and is an
AP-2 workflow item for census: spawns must read supplements).

**Clerk's corrections to the Sitting 2 briefing:** (1) the briefing's
totals were overstated by one — I1 was counted twice; correct figures
above. (2) The briefing attributed "incremental code blocks with manual
execution" to attempt-01 `log.md:49`; the log reads "Supplement uses
incremental code blocks (sections 5.1-5.38) with manual list index
management" (`log.md:48-50`). No score rested on the misquote (R1.3 = 0
stands on its own grounds). (3) The briefing argued a carrier-based I1 = 0
would count one fact several times over (F2–F4, A2, R1.3). That is wrong:
the same scripts served as an `.R` file supplement would score identically
at F2–F4, A2, and R1.3, so file format is scored only at I1. (4) Sitting
1's principal-set wording lists the supplement's "probability tables" as
principal data; those tables are reported results (the reproduction's
comparison targets), not inputs — the principal inputs are the OxCal model
(dates embedded) and beads-1.csv. No Sitting 1 score changes from the
wording fix; it matters only under the language reading of D3, where
typeset tables would otherwise fall under the guide's existing PDF-tables
→ 0 rule.

## Sitting 3 — 2026-10-02 — herskind-riede-2024 `data_fair`: 12 → 12 (recomposed)

**Context.** The principal data is S1.xlsx — the coding of 483 ornamented
objects, transcribed from Płonka's (2003) printed catalogue — with S3.xlsx
(precomputed tables, a reproduction comparison target) and S2.R (code),
deposited as two versions of one Zenodo record (concept DOI
10.5281/zenodo.10623549), both CC-BY-4.0. Scored version: v2
(10.5281/zenodo.10801706), per AP-12. The publisher's supplement (Elsevier
`mmc1.xlsx`, `mmc2.zip`, `mmc3.xlsx` for PII S0305440324000359, fetched
2026-10-02 from `https://ars.els-cdn.com/content/image/1-s2.0-S0305440324000359-mmcN.<ext>`)
is a byte-identical copy of v2: MD5 `0bcde6d1…` (S1), `812be545…` (S3), and
`6760ccb3…` (S2.R inside the zip) all match v2's Zenodo checksums. So AP-2
adds nothing new, and AP-9's best-form guard scores the Zenodo deposit.
Reproduction attempt-01 (verdict SUCCESSFUL) used v1.

**Rulings (Shawn, 2026-10-02):** A1 = 1 under AP-10 — Płonka (2003) is
fully transcribed into S1 (S1's own notes: "all South Scandinavian objects
were manually transcribed into this document"), so it is provenance and not
in the coverage denominator; coverage complete. R1.3 0→1 under AP-11. The
nod table confirmed: F2 1→0 (both versions have an empty Zenodo
description and no keywords — Zenodo API, 2026-10-02; Row 1: mandatory
DataCite fields are not substantive description; Row 2: Zenodo does not
guarantee a description); I3 1→0 (neither version has any related
identifiers, not even the article DOI; Płonka (2003) has no persistent
identifier; all nine v2.1 runs scored 0); R1.1 0→1 (CC-BY-4.0 on both
versions; article CC BY; all nine runs scored 1); I1 = 1 (`.xlsx` is an
open standard, ECMA-376 / ISO/IEC 29500, read directly with R's readxl in
attempt-01 — AP-9; BI [input], since neither paper nor pack gave the
format); R1.2 = 1 (spot-check confirmed: S1's notes give per-column
provenance); R1 = 1 (basis corrected: Methods §2.1–2.2 plus v2's
README.txt; the Zenodo description cited by the old reference is empty).
Unchanged: F1, F3, F4, A1.1, A1.2, A2 = 1; I2 = 0. **Total 12** (old 12;
recomposed: F2 and I3 down, R1.1 and R1.3 up). Registrant's note: the
approach is adequate for this stage of research and development; precedent
is to be built and refined as larger corpora supply more examples.

**Findings (no score effect):** (1) the paper cites two versions in
different sections (AP-12 precedent); v2's S2.R is 33,834 bytes against
v1's 18,707. (2) Both Zenodo records list only Herskind as creator; Riede
is absent. (3) The pilot extraction's data-completeness notes for this
paper describe "lithic measurements, use-wear images", which are not in
this paper — a defect in the old E8 evidence base. (4) Pre-census: the
harvester should capture file formats, descriptions, keywords, related
identifiers, and version metadata (F2, I1, I3, and AP-12 all turned on
them); Elsevier supplements can be fetched without the ScienceDirect 403
via the Crossref PII and the CDN pattern above.

## Sitting 4 — 2026-10-02 — herskind-riede-2024 `code_fair`: 9 → 12

**Context.** The code is S2.R, deposited in the same Zenodo record as the
data (version v2 scored, per AP-12; the publisher's `mmc2.zip` holds a
byte-identical copy). **AP-12 changes two scores here:** the old reference
assessed v1 (10.5281/zenodo.10623550), whose S2.R has 451 lines, 117
comment lines, no figure mapping, and no README or version information. v2's
S2.R has 759 lines, 210 comment lines, and a contents table mapping each
part to the figure or table it produces; v2 adds a README listing R 4.3.2
and all seven package versions.

**Ruling (Shawn, 2026-10-02):** R1.3 = 0 under reading (i) — AP-11 is
data-only, and the script meets none of the instrument's code standards.
**Nods confirmed:** F2 1→0 (same record as the data: empty description, no
keywords); R1 0→1 (v2 annotation and README); R1.2 0→1 (v2 README versions;
the paper names R and quanteda); R1.1 0→1 (CC-BY-4.0 covers the record —
AP-8; CC-on-code is a non-fatal finding); I3 0→1 (quanteda cited with its
JOSS DOI 10.21105/joss.00774 — the dye code precedent: dependencies enter
through citation quality, item 2). Unchanged: F1 (spot-check confirmed),
F3, F4, A1, A1.1, A1.2, A2, I1 = 1; I2 = 0. **Total 12** (old 9). No BI
tags.

**Findings (no score effect):** the paper states R 4.2.2 but the v2 README
states R 4.3.2; the Zenodo record is typed "Dataset" although it contains
code; CC licence on code (AP-8 finding class).

## Sitting 5 — 2026-10-03 — key-et-al-2024 `data_fair`: 8 → 1

**Context.** The analysis needs record-level morphometric data from 13
assemblages; the pilot inventory (and reproduction attempt-01's
`data-availability-inventory.md`) finds 3 accessible through other
publications and 10 unpublished: 6 co-author-held, 3 in closed monographs
or a thesis, 1 never published. The publisher supplement (Elsevier, PII
S0305440323002017, fetched 2026-10-02 by the CDN route) holds three R
scripts (`mmc1`–`mmc3` zips), a header-only input template (`mmc4.csv`,
75 bytes), and a results document (`mmc5.docx`) — no input data. Under
AP-10 all 13 datasets are required (none is transcribed into a deposit),
so coverage is 3/13 (23%), "minimal", and A1 = 0. Reproduction attempt-01:
PARTIAL.

**Rulings (Shawn, 2026-10-03):** AP-13 (β) — A1.1, A1.2, R1.1 1→0. AP-14 —
R1 = 1 (every dataset described: context, variables, units, n); R1.2 1→0
(conjunctive: §2.4.3.1, the copper socketed tang points, states no
specimen source, collection, or measurer — unlike, e.g., the ceramics
section, which cites Petrie 2020 and its instruments; attempt-01 traced
the source only by following citations outside the paper). **Nods
confirmed:** F1 1→0 (no dataset has a PID; the supplement holds no data;
seven of nine v2.1 runs scored 0); A2 1→0 (entailed flag; nothing is
deposited); I1 1→0 (the old "CSV supplementary tables" is the header-only
template). Unchanged at 0: A1, F2, F3, F4, I2, I3, R1.3. **Total 1** (old
8). No BI tags — every score is derivable from the paper, which itself
says the supplement holds scripts.

**Findings (no score effect):** the paper has no data-availability
statement (the "Supplementary data … can be found online" line is
Elsevier's Appendix A boilerplate); a supplementary CSV is a header-only
template.

**Future-work idea recorded (registrant, 2026-10-03):** a FAIR and
reproducibility uplift tool that performs every possible repair and
reconstruction and produces a FAIR apparatus for a faulty publication —
`wiki/planning/active-todo-list.md`, Deferred / Future Projects item 10.

## Sitting 6 — 2026-10-03 — key-et-al-2024 `code_fair`: 6 → 8

**Context.** The code is three plain-text R scripts in zip archives in the
publisher supplement (`mmc1`–`mmc3`; OLE main, randomised, and resampling
variants), under the article's CC BY 4.0. The first section with no
decisions: the established principles and all nine v2.1 runs agree item
for item — convergence wherever the instrument text is clear.

**Nods confirmed (Shawn, 2026-10-03):** F1 0→1 (supplement code under the
article DOI — item 5 + AP-2, as for dye's code); A2 1→0 (row 6;
entailed flag); R1 0→1 (the scripts' input-formatting instructions plus
§2.3.3 and §2.4.6.1, which give every parameter); R1.2 0→1 (the paper
states R 4.3.0 — the old "no version info" was wrong — the workflow is
fully specified, CRediT names the analysts, and the scripts disclose that
the OLE function was "taken and adapted from sExtinct package"); I1 = 1
(a zip is a lossless standard container, so the code is machine-actionable
as served under AP-9, unlike dye's code-in-PDF); R1.1 = 1 (item 6 + AP-8);
I3 = 0 (the only runtime package, beepr, is uncited; the adapted sExtinct
code is not cited as software; the method papers cited with DOIs describe
the method, not the dependencies). Unchanged: A1, A1.1, A1.2 = 1; F2, F3,
F4, I2, R1.3 = 0. **Total 8** (old 6), matching all nine runs. No BI tags.

**Findings (no score effect):** (1) **possible licence inconsistency** —
sExtinct v1.1 (2013, Christopher Clements; removed from CRAN 2019-01-26)
is licensed GPL-2 per its CRAN archive DESCRIPTION, but the scripts that
adapt its OLE function are distributed under the article's CC BY 4.0;
GPL-2's copyleft would normally require derived code to stay GPL-2, so a
reuser should treat the adapted function as GPL-2. Under AP-8 this does
not touch R1.1. Registrant: "a good catch and the sort of thing that
should be flagged". (2) **Uncredited source software** — the paper never
cites sExtinct as software; only the script comments disclose the
adaptation. Registrant: "common practice, unfortunately". Both are
capabilities for the uplift tool (`wiki/planning/active-todo-list.md`
item 10).
