# OSF registration erratum log — Phase 2 preregistration

**Registration:** <https://osf.io/dqnhg/> — DOI 10.17605/OSF.IO/DQNHG,
lodged 2026-07-20, public 2026-07-21.
**Frozen artefact set:** repository state at commit `ee3fda3`
(tag `osf-prereg-phase2-2026-07-20`).
**Amendment 1: LODGED 2026-08-03** as an OSF versioned registration update
(SchemaResponse revision `6a7017da97adb06288afef80`), appending the
consolidated amendment text to the registration Summary field. DOI
unchanged (no new identifier is minted for a version); amendment version
URL <https://osf.io/dqnhg?revisionId=6a7017da97adb06288afef80>; repository
tag `osf-amendment-1-2026-08-03`. Entries 1–2 and queued-scope items 1–5
below are all folded into the lodged text and discharged.
**Purpose:** records defects discovered in the frozen registration artefacts
after lodgement, together with the corresponding repository-side corrections.
The frozen Open Science Framework (OSF) copies cannot be edited by design;
entries here accumulate until an amendment is worthwhile, at which point this
log is folded into a dated OSF amendment. Any instrument-affecting change must
pass the preregistration §8 regression gate, and an amendment must be lodged
before census scoring begins (prereg §8–§9). Decision path approved by the
registrant 2026-07-22 (erratum log now; amendment when warranted).

---

## Entry 1 — 2026-07-22: three defects in the Pass 6 FAIR instrument prompt

**Artefact affected:** `extraction-system/prompts/06-infrastructure_pass6_prompt.md`
(uploaded to OSF as markdown in the frozen artefact set at `ee3fda3`).
**Discovered by:** implementation review of the agent content-routing design
(`wiki/planning/reviews/2026-07-22-routing-design-implementation-review.md`,
finding D1), with each defect re-verified at source against both the working
tree and `git show ee3fda3` before correction.
**Corrected in repository:** commit `abdc526` (2026-07-22).

| # | Defect (line refs in the frozen copy) | Correction |
|---|---|---|
| 1 | Stale scoring example "Total FAIR score (e.g., 14/16)" / "87.5%" at lines 662–663, contradicting the v2.0 rubric of 15 binary sub-principles defined at lines ~115–163 of the same file | Example corrected to 14/15 / 93.3% |
| 2 | Legacy "5-level access taxonomy" (Level 0–4) at lines 202–208, colliding in vocabulary with the preregistered six-level data-availability taxonomy (L1–L6, registration §7.3) | Renamed to "five-tier access classification (Tier 0–4)" with an explicit demarcation note; the L1–L6 taxonomy remains reproduction-time-only per §7.3 |
| 3 | Dead file pointer "→ See `wiki/planning/REPRODUCIBILITY_INFRASTRUCTURE_SCHEMA.md`" at line 802 (file removed in the 2026-07-03 wiki migration) | Repointed to `extraction-system/schema/extraction-schema-v2.6.json` (canonical), with the archived proposal noted as historical reference |

**Impact assessment.** The registration's normative instrument statement
(§7.1: 15 binary GO-FAIR sub-principles, independent data/code scoring) is
internally consistent and unaffected. The pilot re-scoring (standardised
2026-02-11) demonstrably applied the /15 scale — all five pilot papers carry
/15 scores (pilot findings report v1.2, Table 5) — so no scored output was
produced under the defective example. Defects 1 and 3 are clerical
(a stale worked example from the pre-standardisation era; a pointer broken by
a file move). Defect 2 is a vocabulary-collision hazard rather than a scoring
error: the access tiers feed only the data-completeness coverage computation,
and no persisted schema field uses the "Level n" labels (verified against
pilot `extraction.json` files — `data_completeness` stores aggregate counts
only). Classification: erratum-class corrections that align the operational
file with the registration's own normative text; no instrument semantics
changed. The corrections will nonetheless ride through the §8 regression gate
with the Phase 1 validation runs before census scoring, and this entry is
queued for inclusion in the first OSF amendment.

---

## Entry 2 — 2026-07-27: Pass 6 prompt restated the FAIR instrument incompletely

**Artefact affected:** `extraction-system/prompts/06-infrastructure_pass6_prompt.md`
(uploaded to OSF as markdown in the frozen artefact set at `ee3fda3`).
**Discovered by:** extending the manifest-consistency check
(`scripts/check-manifest-consistency.py`, build item D5) with a byte-exact
comparison of the marker-delimited mirror region against the canonical file
(`studies/open-science-compliance/protocol/instruments/fair-instrument.md`,
extracted 2026-07-24). The check as first built compared the canonical file's
fenced code blocks and table rows — all of which matched. The banner added at
extraction asserted a *verbatim* mirror; the first byte-level comparison showed
the assertion was untrue, because everything missing was prose.
**Corrected in repository:** 2026-07-27 (see the session log).

Four normative statements present in preregistration §7.1 and in the canonical
file were absent from the operational prompt:

| # | Omitted from the Pass 6 prompt | Source |
|---|---|---|
| 1 | "Unscoreable sub-principles score 0 (the instrument scores evidenced practice)" | Registration §7.1 |
| 2 | Scores are "never aggregated into a combined score" | Registration §7.1 |
| 3 | The A1 completeness rule in full: "A1 requires that a majority of the research data be retrievable via standard protocol, with an exception for documented ethical/legal restriction" (the prompt carried only the coverage-category trigger) | Registration §7.1 |
| 4 | The FAIR4RS out-of-scope statement (planned amendment-path extension, not part of this registration) | Registration §7.1 |

**Correction.** The prompt's FAIR section now embeds a byte-exact,
marker-delimited copy of the canonical instrument. Pass 6 workflow content that
previously interleaved with the instrument — output JSON structures, the
coverage-category threshold table, the barrier-type enumeration, and the
context-dependent assessment notes — was relocated below the mirrored region
under a heading marking it as workflow guidance, not instrument. No workflow
content was removed: the restructure was performed programmatically and the
result diffed line by line against the original, every difference accounted for
as either a canonical rewording or one of the four additions above.

**Impact assessment.** The registration's normative instrument statement (§7.1)
is unchanged and was always the governing text; the defect was an incomplete
operational restatement of it, so this is the same erratum class as Entry 1.
Checked against the persisted pilot outputs
(`studies/open-science-compliance/outputs/*/extraction.json`, the four papers
carrying FAIR assessments — dye-et-al-2023, herskind-riede-2024, key-et-al-2024,
marwick-2025):

- all four use the `binary_sub_principles` /15 scale;
- no sub-principle is recorded unscored (zero null `present` values), so
  omission 1 changed no pilot score;
- no output carries a combined or aggregate FAIR field, so omission 2 was
  honoured in practice;
- omission 3 was likewise applied where it bit — key-et-al-2024 records
  A1 = false with the evidence "Only 3 of 13 datasets (23.1%) retrievable via
  HTTPS", the majority rule operating as registered;
- omission 4 is declaratory and affects no score.

**Coverage correction (2026-08-02).** The scoping statement above — "the four
papers carrying FAIR assessments" — under-counts. A fifth persisted FAIR
assessment exists, for crema-et-al-2024, at
`studies/open-science-compliance/outputs/crema-et-al-2024/run-02-session-per-pass/extraction.json`.
The 2026-07-27 sweep missed it for two structural reasons: the file sits one
directory below the `outputs/*/extraction.json` pattern swept, and it stores
the assessment under the pre-v2.6-convention top-level key `infrastructure`
rather than `reproducibility_infrastructure`. Located 2026-08-02 on the
registrant's query and re-checked the same day: it uses the
`binary_sub_principles` /15 scale (data 12/15, code 12/15, matching pilot
findings report v1.2 Table 5 exactly), leaves no sub-principle unscored,
carries no aggregate field, and records A1 present — so key-et-al-2024 remains
the one pilot where the A1 majority rule was decisive. All four impact
conclusions above therefore hold across five of five pilots; this entry's
conclusion is strengthened, not weakened. (The related run-01 artefacts were
archived, not deleted — `c41242b`, 2026-01-13. Working-notes Observation 20
records the sweep-scope lesson; the monitoring plan §1(c) and class E8 carry
the structural fix.)

Classification: erratum-class corrections aligning the operational file with the
registration's own normative text; no instrument semantics changed and no pilot
score is revised. The corrections ride the §8 regression gate with the Phase 1
validation runs, and this entry folds into the consolidated amendment below.

**Recurrence prevented.** The mirror is now byte-compared on every commit and at
orchestrator pre-flight. A future divergence fails loudly instead of persisting
behind a banner asserting it cannot happen — which is the failure mode this
entry documents: the assertion was written before anything checked it.

**Related finding, resolved the same day — deliberately not an erratum.** The
same comparison showed the second registered mirror — `verdicts-and-precision.md`
into the reproduction-assessor `SKILL.md` — carried the canonical prose only in
reworded form, and omitted two things outright: the sentence escalating
PAPER_ERROR findings for human confirmation before they enter study data, and
the environment-specification levels 0–5 (registration §7.5), which the skill
never carried at all.

No erratum entry and no amendment are required for that mirror, on three
independent grounds. First, `SKILL.md` is not part of the frozen artefact set —
the registration froze four files (the preregistration draft, the pilot findings
report, `study-protocol.md`, and the Pass 6 prompt), and an erratum by definition
records a defect in a frozen artefact. Second, the content brought into line is
either not registered at all (the discrepancy vocabulary — `CANNOT_COMPARE`,
`PAPER_ERROR`, `MAJOR_DISCREPANCY` — appears nowhere in the registration; it
comes from the reproduction-assessor protocol v1.1 that §7.2's "definitions as
in" clause points to) or is registered text already faithfully carried by the
canonical file (§7.4 precision, §7.5 environment levels). Third, converging a
mirror changes delivery, not instrument semantics: it removes a divergence
between two lanes rather than altering what either lane is supposed to apply.
It is therefore an ordinary §8 implementation change, riding the Phase 1
regression gate with everything else before production use.

**Resolved 2026-07-27:** the mirror is now byte-exact. Because the canonical
content lands in four different places in the skill's workflow, the check gained
named segments (`#precision`, `#tolerances`, `#discrepancy`, `#verdicts`,
`#scope`, `#environment`), each compared separately, so the skill keeps its
structure without giving up byte-exactness. `mirror_mode: structural` — the
declared-weaker fallback — is retained in the checker for any future mirror that
genuinely cannot be segmented, and warns on every run when used. Nothing in the
registry uses it now.

---

## Queued amendment scope (running list)

**Consolidated draft written 2026-07-24:** `amendment-1-draft.md` (this
directory) carries the lodgement wording for every item below plus Entry 1;
new entries added here after that date must also be folded into the draft
(its pre-lodgement checklist enforces this).

**RATIFIED by the registrant 2026-07-24** (proposed the same day from the
pre-build juncture review, findings D-1/D-4/D-5 + E-1/E-4/E-7/E-8; report at
`wiki/planning/reviews/2026-07-24-pre-build-juncture-review.md`). Registrant's
lodgement timing decision: **defer to the hard stop** — the amendment lodges
just before the validation phase runs, so any further errata found during the
corpus and Phase 1 builds accumulate into the same single amendment.
**Deadline note:** items 2–4 below govern the combined validation phase itself, so
the consolidated amendment must lodge **before the validation phase runs** — earlier
than the before-census-scoring deadline that Entry 1 alone would require.

1. **Entry 1 and Entry 2 corrections** (Pass 6 instrument defects, above) — already
   committed to an amendment; fold in here. Entry 2 was found on 2026-07-27, after the
   consolidated draft was written, by the D5 check's first byte-exact mirror
   comparison; the draft's §1 and its pre-lodgement checklist are updated accordingly.
2. **Below-threshold remediation ladder** (routing design §2.2): one routing-fix
   attempt (delivery mechanism only; instrument text untouched) followed by a re-run
   of the §8(a) stability check, permitted **once**; a still-below-threshold re-run
   → the registered majority-vote consequence applies with no further iteration;
   both pre-fix and post-fix reliability results reported with study outcomes.
3. **Validation-phase pre-specifications:**
   - *Agreement statistic* for the 3-run stability check — proposed: **unanimity
     proportion** (strictest of the three candidate definitions; the review shows
     the candidates cross the 0.90 gate at item-flip rates from ~10% to ~30%, so
     the choice cannot be left implicit).
   - *Pilot-paper set* — proposed: **all five** pilot papers (preregistration says
     "at least three"; n rises 90→150 items and the false-pass rate at true 0.85
     halves, ~12%→~5.5%; no amendment strictly required for this item, recorded for
     completeness).
   - *Model-selection rule* — proposed: **gates-plus-cost**. The spot-check cannot
     statistically rank models (±0.09 confidence interval on an agreement
     difference; no preregistration-compliant n exists before the census). Any
     model passing (a) the 0.90 stability gate and (b) a concordance floor against
     the pilot reference scores (proposed ≥0.90 on the same statistic — the
     accuracy gate, review E-4) is eligible; among eligible models the cheapest
     scores the census; agreement differences inside the confidence interval are
     pre-declared not to be selection grounds.
   - *Within-phase ordering:* spot-check → select model → regression-gate the
     **selected** configuration (both lanes pinned) → census.
   - *Run independence and provenance:* each run is a fresh spawn with no shared
     context and no persistent memory; sampling seeds are not controllable in this
     harness, so each run records session ID, timestamp, and the full receipt
     triple {instrument_versions, agent_version, model_id}, and reports state that
     run-to-run variation reflects default-temperature sampling.
4. **Read-scope isolation rule** (review D-4): validation-phase scoring runs
   execute with read access only to the paper source and the pushed/pulled
   instrument files — the repository holds the pilot papers' canonical scores, so
   an unisolated scorer could reproduce recorded answers and return perfect,
   uninformative agreement. Enforced by tool allowlist/sandbox scope and verified
   from the harness transcript; per-run file-access lists archived with run
   artefacts. The same hygiene applies at census to any paper with pre-existing
   repository artefacts.
5. **Robustness annex** (review E-7): scored runs from non-selected passing model
   arms are archived and citable as cross-model robustness data, not discarded.

## Entry 3 — 2026-08-10: benchmark-revealed instrument ambiguities (item-structured disagreement)

**Status: instrument ambiguity record + queued amendment 2 scope (PROPOSED —
pending registrant ratification of the drafted text below; the underlying
scoring-policy decisions were ruled by the registrant 2026-08-10).**

The 2026-08-03 validation benchmark (amendment 1 §3: three arms × five pilot
papers × three runs) put all three arms below both 0.90 gates — stability
0.807/0.873/0.813, concordance 0.773/0.807/0.820 — with the disagreement
item-structured and shared across arms. The registrant declined the §2
routing-fix card (its premise held only for the sonnet arm: pull receipts
show 9/15 guide pulls for sonnet vs 15/15 for both other arms, which failed
anyway) and chose instrument clarification via this log and OSF amendment 2
(decision 2026-08-03; plan at `wiki/planning/instrument-clarification-plan.md`).

The Phase A1 mining pass (`studies/open-science-compliance/outputs/validation/
benchmark-2026-08/disagreement-analysis.md`, machine-readable
`disputed-items.json`) recomputed both statistics from primary artefacts
(exact match to published figures) and found 68 of 150 items disputed,
reducing to three root causes: (1) the assessment target was undefined
(third-party/upstream/article-level crediting); (2) the admissible evidence
basis under paper-only scoring was undefined (platform-by-construction
inference vs paper text); (3) semantic gaps in A1.2 (all 10 possible items
disputed) and R1.3 (8 of 10). A verified prior-art survey
(`wiki/planning/scout-reports/2026-08-10-fair-third-party-artefacts-prior-art-verified.md`)
grounds the clarifications; the registrant ruled all eight decision points
on 2026-08-10 (plan, decision log).

**Consequence for the reference scores:** the clarifications below flip
identifiable pilot reference scores (at minimum dye-et-al-2023 data R1.3;
key-et-al-2024 A2; F-block items on both) and the current reference set
takes both sides of the target question across papers — reference
re-derivation under the clarified instrument (plan Phase B1) is entailed,
not optional.

## Queued amendment 2 scope (running list; PROPOSED 2026-08-10)

Items 1–9 below are drafted operative text for the instrument (v2.0 → v2.1)
and the validation-phase re-specification. Consolidation into
`amendment-2-draft.md` follows the registrant's read (plan Phase D1).

1. **Research-surface rule** (new instrument section; ruled 2026-08-10).
   "The unit of assessment is the paper's research surface: the complete
   set of digital artefacts — data, code, and other digital inputs —
   required to reproduce the paper's reported results, as reachable from
   the published paper. Each FAIR sub-principle scores the empirical status
   of those artefacts; creator identity, depositor identity, and
   responsibility for closure never affect scores. A precisely cited,
   well-archived third-party input earns full credit; a closed or
   unpublished input is penalised even where closure is beyond the authors'
   control. Provenance (author-deposited / third-party / undeterminable) is
   recorded per required input as non-scoring metadata." Amendment
   rationale cites the verified precedent set (RDA FDMM v1.00
   10.15497/rda00050; JIE Data Openness Badges secondary-data rule,
   10.1111/jiec.12738; CODECHECK; Colavizza et al. 2020; Culina et al.
   2020; Tedersoo et al. 2021; Marwick 2017) and names ACM Artifact Review
   and Badging v1.1 ("Author-created artifacts…") as the deliberate
   departure: the study measures the credibility of published results, not
   author compliance.

2. **Aggregation rule for heterogeneous input sets (initial draft —
   explicitly iterable per the registrant's 2026-08-10 decision).**
   "Within each artefact type, sub-principles are scored on the principal
   artefact(s): those whose absence would block reproduction of the
   reported results. For data, a sub-principle scores 1 only if it holds
   for every principal dataset (conjunctive scoring — mirroring the
   most-restrictive rule for licence conflicts); proportional coverage of
   the full required set, including non-principal upstream sources, is
   carried by the data-completeness lane and feeds the A1 override as
   registered. For code, the paper's own analysis scripts are always
   principal; third-party dependencies are never substitutes for them and
   enter scoring only through citation quality (I3) and the evidence
   pack." Alternatives recorded for iteration: majority-over-principals;
   proportion-weighted.

3. **Evidence-admissibility ladder + platform table** (new instrument
   section; ruled 2026-08-10). Admissible evidence, in order: (i) the
   paper's own text; (ii) the verified artefact evidence pack (item 8);
   (iii) by-construction properties of platforms in a closed,
   instrument-listed table, applicable only where the evidence pack has no
   record. Initial table rows: DataCite-registered DOI (metadata record
   carrying the identifier; tombstone persistence); Zenodo (DataCite
   metadata; licence field exists — the licence itself must still be
   identified per item 6); CRAN (structured package metadata; archival);
   accredited domain repositories (ADS, tDAR, DANS: ingest-enforced domain
   metadata standard — satisfies R1.3 by construction); GitHub/GitLab
   (licence field via evidence pack only; no persistence entitlement);
   publisher supplement of a Crossref-registered article (HTTPS delivery
   via the article landing page; article-level record persistence; NO
   independent metadata record, licence field, registry indexing, or
   resource-level identifier — hence F2 = F3 = F4 = 0 and A2 = 0 for
   supplement-only deposits). The table is extensible by dated amendment
   or, pre-census, by gated instrument edit (Dataverse, Australian Data
   Archive, Figshare flagged as likely additions).

4. **A1.2 no-restriction case** (ruled 2026-08-10). Appended to the A1.2
   line: "A fully open resource requiring no authentication satisfies
   A1.2 — the protocol supports authentication where needed, and none is
   needed. Score 0 only where access control exists or is warranted but
   the mechanism is undocumented or unjustified."

5. **F-block identifier granularity** (ruled 2026-08-10). F1 reads: "a
   globally unique, persistent identifier explicitly associated with the
   artefact — its own PID, or the article DOI where the artefact is
   distributed as that article's supplement. This is a deliberate,
   declared departure from the strict object-PID reading (cf. F-UJI):
   F2/F3/F4 remain strictly artefact-level (independent metadata record;
   identifier carried in that record; registry indexing), so the
   granularity deficiency of supplement-only deposit is scored there,
   yielding F subtotals of 4/4 (own-PID deposit), 1/4 (supplement under
   the article DOI), 0/4 (unpublished)."

6. **R1.1 licence semantics** (ruled 2026-08-10). "Unless explicitly
   stated otherwise, an article's licence extends to its publisher-hosted
   supplements: check for both article and supplement licences; absent a
   separate supplement licence, default to same-as-paper. Artefacts hosted
   on third-party services are scored on the licence recorded at the
   service (via the evidence pack) — a platform's mandatory licence field
   does not itself satisfy R1.1; the licence must be identified. Where
   paper and repository conflict, the most restrictive licence governs
   scoring."

7. **R1.3 qualifying standards** (ruled 2026-08-10). "R1.3 scores
   deposit-level standards — what GO-FAIR measures: artefact reusability,
   not method quality. Qualifying routes: (a) generic metadata schemas
   (DataCite, Dublin Core); (b) domain schemas and vocabularies
   (ARIADNEplus, CIDOC-CRM, Darwin Core); (c) deposit in an accredited
   domain repository whose ingest enforces its metadata standard. For
   code: package structure, CITATION.cff, CodeMeta, or community review
   (CRAN, JOSS, rOpenSci). Methodological standards (IntCal20, OxCal,
   established methods) do not qualify."

8. **Read-scope re-specification + artefact-metadata harvester** (ruled
   2026-08-10; supersedes amendment 1 §4's paper-only formulation for the
   re-validation and census). Scoring spawns receive: the paper source,
   the pushed instruments, and a per-paper verified evidence pack produced
   by a deterministic harvester that resolves the paper's declared
   artefact links via enumerated endpoints (DataCite, Crossref, Zenodo,
   GitHub, OSF; extensible) into licence fields, metadata records, and
   conflict flags, receipt-covered like the instruments. Spawns remain
   network-free; evidence is identical across runs. The prohibition on
   reading persisted assessments stands unchanged.

9. **Unscoreable boundary** (ruled 2026-08-10). The registered
   unscoreable→0 default applies only after the item-3 ladder is
   exhausted: a sub-principle is unscoreable only when neither the paper,
   nor the evidence pack, nor a listed by-construction entitlement speaks
   to it.

10. **Ride-alongs:** remediation ladder restated for the re-specified
    validation check (one routing-fix attempt, single re-run, else the
    registered majority-vote consequence — carrying amendment 1 §2's
    structure forward); the two escaped-comparator cosmetic fixes flagged
    at amendment 1 lodgement; `fair-principles-guide.md` alignment with
    the clarified text plus promotion pull → push (plan A3).
