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

**Status: instrument ambiguity record + queued amendment 2 scope (RATIFIED —
registrant read the log end-to-end and approved 2026-08-14, incorporating
the 2026-08-11 ratification-read consolidations; the underlying
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

## Queued amendment 2 scope (running list; RATIFIED 2026-08-14)

Items 1–9 below are ratified operative text for the instrument (v2.0 → v2.1)
and the validation-phase re-specification (registrant's end-to-end read,
2026-08-14). Consolidation into `amendment-2-draft.md` is plan Phase D1,
pending the Phase B concordance-reference decision and A3.

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
   recorded per required input as non-scoring metadata, keeping
   responsibility reportable as a study finding." Amendment
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
   section; ruled 2026-08-10; ladder form consolidated 2026-08-11).
   Admissible evidence forms a two-rung ladder. Rung (i), direct
   evidence: the paper's own text and the verified artefact evidence
   pack (item 8) — complementary records, with disagreements between
   them governed by the specific rules (e.g. item 6's most-restrictive
   licence rule). Rung (ii), by-construction inference: platform
   entitlements from a closed, instrument-listed table, applicable only
   to facts on which rung (i) is silent. Table entitlements are floors,
   not ceilings: they state the minimum apparatus the platform enforces
   on everything it hosts; rung-(i) evidence may establish more. Initial
   table rows: DataCite-registered DOI (metadata record carrying the
   identifier; tombstone persistence); Zenodo (DataCite metadata;
   licence field exists — the licence itself must still be identified
   per item 6); CRAN (structured package metadata; archival); accredited
   domain repositories (ADS, tDAR, DANS: ingest-enforced domain metadata
   standard — satisfies R1.3 by construction); GitHub/GitLab (licence
   field via evidence pack only; no persistence entitlement); publisher
   supplement of a Crossref-registered article, applicable only where
   the supplement is served directly from the article landing page with
   no independent deposit (HTTPS delivery via the article landing page;
   article-level record persistence; NO independent metadata record,
   licence field, registry indexing, or resource-level identifier —
   hence F2 = F3 = F4 = 0 and A2 = 0 for supplement-only deposits). A
   supplement deposited under its own identifier in a general or domain
   repository (e.g. journal supplements hosted at Figshare; data in
   Dryad) is scored as a deposit on that platform — via the evidence
   pack and, where listed, that platform's row — never under the
   supplement row. The table is extensible by dated amendment or,
   pre-census, by gated instrument edit (Dataverse, Australian Data
   Archive, Figshare, and Dryad flagged as likely additions).

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

6. **R1.1 licence semantics** (ruled 2026-08-10; per-artefact scope
   clarified 2026-08-11). "Licences are assessed per artefact: where a
   paper and its separately deposited dataset or software carry
   different licences, each artefact is scored on its own licence — a
   clean division, not a conflict. The most-restrictive default applies
   only where sources disagree about the licence of the *same* artefact:
   (a) a supplement carried in or served with the article itself —
   unless explicitly stated otherwise, the article's licence extends to
   publisher-hosted supplements; check for both article and supplement
   licences; absent a separate supplement licence, default to
   same-as-paper; where both exist and differ, the more restrictive
   governs; (b) a deposited artefact whose licence as asserted in the
   paper differs from the licence recorded at the hosting service — the
   more restrictive governs scoring (the responsible-consumer reading).
   Where the paper is silent, artefacts on third-party services are
   scored on the licence recorded at the service (via the evidence
   pack) — a platform's mandatory licence field does not itself satisfy
   R1.1; the licence must be identified."

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
   2026-08-10; endpoint list settled 2026-08-11; supersedes amendment 1
   §4's paper-only formulation for the re-validation and census).
   Scoring spawns receive: the paper source, the pushed instruments, and
   a per-paper verified evidence pack produced by a deterministic
   harvester that resolves the paper's declared artefact links via
   enumerated endpoints (DataCite, Crossref, Zenodo, GitHub, GitLab,
   OSF; CRAN and Dryad flagged as early additions; extensible) into
   licence fields, metadata records, and conflict flags, receipt-covered
   like the instruments. The endpoint list and the item-3 platform table
   are maintained independently: endpoints are chosen for queryability
   of verifiable records, table rows for defensible by-construction
   entitlements; membership in one implies nothing about the other.
   Spawns remain network-free; evidence is identical across runs. The
   prohibition on reading persisted assessments stands unchanged.

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

**D1 window executed 2026-08-15** (branch `feat/d1-amendment-2-window`):
items 1–9 implemented as FAIR instrument v2.1 (canon region; Pass 6 mirror
re-spliced byte-identically), with the platform table carrying the
registrant's 2026-08-15 rulings on the platform-row verification note (all
§A rewrites; row 4 graded — ADS by construction, DANS/tDAR rung-(i);
all §B additions; operative-default footnote; harvester-integrity
commitment) and the same-day CoreTrustSeal/re3data enrichment evidence.
Item 10 executed: guide v1.1 aligned and promoted pull→push;
agent definitions v1.1; C7 content-integrity hashes registered and
gate-enforced. Consolidated amendment text drafted at
`amendment-2-draft.md`; the Phase B reference re-derivation shape (ruled
2026-08-15) is pre-specified in its §3. Lodgement (plan D2) remains the
hard stop before the D3 re-benchmark.

**AMENDMENT 2 LODGED 2026-08-17** (SchemaResponse revision
`6a824828f323f5c6ead66c4b`, approved; DOI unchanged; tag
`osf-amendment-2-2026-08-17` at commit `9f7343e`; round-trip and public
render verified). Registrant approved the draft verbatim; the
identifier-recovery rule (ruled 2026-08-17) rode in §2. One item changed
at pre-lodgement verification: **the item-10 escaped-comparator fix
DISSOLVED** — the registry's write path stores every literal comparator
as an HTML entity and its renderer decodes them correctly, so the public
page never had a defect; amendment §6 records the dissolution instead of
a correction. The D3 re-benchmark's lodgement hard stop is now
discharged.

## Entry 4 — 2026-10-03: amendment 2 §2's precedent case was a pilot-extraction error

**Status: correction recorded; public correction queued for the next OSF
lodgement (registrant decision, 2026-10-03, option (a)).**

**Lodged text affected.** Amendment 2 §2 (lodged 2026-08-17) closes its
identifier-recovery rule with: "Precedent case: marwick-2025's cited
10.5281/zenodo.14561925 resolves at neither DataCite nor Zenodo
(2026-08-15)."

**Defect.** The paper does not cite 10.5281/zenodo.14561925. Verified
2026-10-03: the identifier appears nowhere in the version of record, the
preprint, or the corpus extracted text. Its only source is the pilot
extraction record (`studies/open-science-compliance/outputs/marwick-2025/extraction.json`,
field `reproducibility_infrastructure.data_completeness.assessment_scope_rationale`:
"Bibliometric study with all data in Zenodo research compendium (DOI:
10.5281/zenodo.14561925)") — an unverified identifier in a model-produced
record. The paper cites the compendium's concept DOI
10.5281/zenodo.14897252 (data-availability statement and §2.1); the
preprint cites v1.1 (10.5281/zenodo.14897253). The deposit "recovered" for
the dead identifier, 10.5281/zenodo.15603267, is v1.3 of that same concept
(published 2025-06-05). No deposit was lost, and the paper carries no
dead-link citation defect.

**Propagation.** The declared-links registry was curated from the pilot
extraction records (2026-08-15), so the identifier entered the harvester's
input, both evidence-pack cycles, the D3 arms' inputs, the plan, the
continuity log, and the lodged §2 text.

**Unaffected.** The identifier-recovery rule itself, which worked as
specified on a wrong input, and every registered analysis.

**Repository-side corrections (2026-10-03).** The registry entry moved to
`withdrawn_links` (never harvested again); the v1.3 entry re-described as
the version selected by the E8-v2 version rule (adjudication log AP-12),
not a recovery; dated correction notes added to the plan and the continuity
log. The committed evidence packs stay as dated snapshots.

**Safeguard (registrant direction, 2026-10-03).** A deterministic check that
every identifier in the declared-links registry appears verbatim in the
paper or its supplement — and, more generally, mechanical verification
wherever it is possible (pre-census item in
`wiki/planning/instrument-clarification-plan.md`).

## Entry 5 — 2026-10-04: concordance statistic; BI exclusion at the gates

**Status: registrant rulings recorded 2026-10-04
(`outputs/validation/gates-ruling-2026-10-04/ruling.md`). Public
clarification and deviation queued for amendment 3. Both must be lodged
before census scoring begins.**

**(a) Clarification: the concordance statistic.** Amendment 1 §3 sets "a
concordance floor of at least 0.90 (same statistic) against the pilot
reference scores" without saying how three runs meet one reference score.

- The H13 blinded re-derivation (2026-10-04) showed that a fresh reader
  takes the literal reading: all three runs agree *and* equal the reference.
- The study has computed concordance since 2026-08-03 as majority-vote item
  agreement, and amendment 2 reports figures computed that way.
- The registrant ruled majority vote, the operationalisation in force before
  the gate data. This corrects an underspecification, not a change of
  analysis.

**(b) Deviation: the gate statistic excludes beyond-instrument items.**

- E8-v2 tags 9 of 150 reference items as beyond-instrument (BI). Their
  reference scores rest on supplementary evidence that the benchmark spawns
  were deliberately not given, and 4 of them also on a principle adopted at
  adjudication.
- The registrant ruled the BI-excluded concordance (141 items) admissible as
  the gate statistic, with the all-items figure reported alongside it.
- Amendment 2 specified concordance against the re-derived reference with
  no exclusion, so this is a deviation and is lodged as one.

**Proposed OSF wording (for amendment 3; registrant to edit and lodge):**

> *Concordance statistic (clarifies amendment 1, section 3).* Concordance is
> majority-vote item agreement. Each item's score is the majority of the
> three runs, and it is compared with the reference score; the gate is the
> proportion of items that agree. This is the operationalisation used for
> every concordance figure the study has reported, including those in
> amendment 2. A blinded re-derivation before the gates ruling found that
> the registered phrase "(same statistic)" also admits a stricter reading
> (all three runs agree and equal the reference). That reading would count
> each unstable item against concordance as well as stability, and it was
> not adopted.
>
> *Deviation: beyond-instrument items excluded from the concordance gate.*
>
> - The re-derived pilot reference tags 9 of 150 items as beyond-instrument.
>   Their reference scores rest on evidence that the validation spawns were
>   deliberately not given, namely the papers' supplementary files; four
>   also rest on a principle adopted during adjudication that the instrument
>   does not state.
> - The registrant ruled, before any model selection, that concordance
>   computed without these items (141) is the gate statistic. Concordance
>   over all 150 items is reported alongside it.
> - The tags were assigned on 2 October 2026, before concordance was
>   computed. The reference adjudication was not blinded to the arms'
>   scores.
> - Under this ruling, claude-opus-5 clears both gates at two reasoning
>   efforts (high: 127/141 = 0.901; xhigh: 130/141 = 0.922). Over all 150
>   items it does not (0.873 and 0.893). claude-fable-5 clears both readings
>   but is not selectable on price.
> - Census scoring will include the papers' published supplementary files,
>   and the selected configuration is re-checked on the five pilot papers
>   with supplements before census.

**Correction (2026-10-05, amendment 3 decision D-5).** The proposed wording
above overstates what the BI items rest on. Only dye's four items rest on
the papers' supplementary files. The other five (crema data I1 and I3,
herskind data I1, marwick data I1 and code I3) rest on deposit content the
2026-08-17 packs never recorded, which was not deliberately withheld. The
lodged text is amendment 3 §3(b), and the `input` tag's definition is
clarified in the adjudication log. Which items are excluded, and every
figure, are unchanged.

**Correction (2026-10-06, Astra's amendment 3 review, should-fix 1).** The
proposed wording's "tags were assigned on 2 October 2026" is only partly
right. The tagging convention was adopted on 2 October (five items tagged
at worksheet commit `7298681`), and the nine-item set was completed on
3 October (`6c0c2ec`, `8905c6c`, `7da90bf`), before the six-arm
concordance was computed and committed later that day (`6e0d17a`). The
lodged text is amendment 3 §3(b), which states both dates.

## Queued amendment 3 scope (running list)

**AMENDMENT 3 LODGED 2026-10-08** (SchemaResponse revision
`6ac775afb5ed5b4afee88a4a`, approved; DOI unchanged; tag
`osf-amendment-3-2026-10-08` at commit `abde9b1`; round-trip verified byte
for byte). The items below are folded into the lodged text and
discharged; the draft's revision record carries the rulings. Version URL:
<https://osf.io/dqnhg?revisionId=6ac775afb5ed5b4afee88a4a>.

**Consolidated 2026-10-04:** the full draft text of items 1–9 is in
`amendment-3-draft.md` (this directory), for the registrant to edit and
lodge. Six registrant decisions (D-1 to D-6) are open in that draft;
D-5 corrects Entry 5's proposed wording on what the BI items rest on.

1. Entry 4 — correct amendment 2 §2's precedent case.
2. Candidates: the pre-census instrument clarifications collected from the
   E8-v2 adjudication (plan pre-census item), if they are lodged as an
   instrument amendment rather than a gated edit.
3. Entry 5(a) — clarify the concordance statistic as majority-vote item
   agreement.
4. Entry 5(b) — the deviation admitting the BI-excluded concordance as the
   gate statistic, with the all-items figure reported alongside it.
5. ~~Candidate — the selected configuration (model, effort, prices in
   force), once the registrant confirms the D4 arm choice.~~ **CONFIRMED
   (Shawn, 2026-10-04): `claude-opus-5-5` at effort `medium`.** This moves
   the census scorer off the registered pin (`claude-opus-5`), so it is an
   amendment item, and the amendment should state:
   - **Why:** a newer model in the same tier, benchmarked through the same
     gates under the same pre-declared rule (design note Q4, declared
     before any data). All three Opus 5.5 efforts were eligible.
     Stability was 0.953 / 0.953 / 0.967 and BI-excluded majority-vote
     concordance 0.922 / 0.929 / 0.922 (high / medium / xhigh). The
     analysis tool and the H13 script agree on every figure.
   - **Prices in force at selection:** the claude-api skill's table, cached
     2026-09-25. `claude-opus-5-5` costs $4 / $20 per million tokens, with
     cache reads at 0.05× input; `claude-opus-5` costs $5 / $25.
   - **Rule applied:** cheapest eligible. `medium` cost $8.70 for 15
     scorings, recorded per request; the bounds are $9.25 central and $9.37
     upper (register F-019). Opus 5 at `high` cost $17.27. The answer is
     robust to F-019.
   - **Source:** `outputs/validation/opus-5-5-arms-2026-10/results-2026-10-04.md`.
   - **Then:** the registered regression gate and the pre-census
     supplement check run on this configuration.
6. **Candidate — deterministic checks on scoring outputs** (policy RULED by
   Shawn 2026-10-04; `wiki/planning/deterministic-output-checks.md`).
   - **(a) Disclosure.** Derived fields (section totals,
     `coverage_percentage`, and `coverage_category`) are computed
     deterministically from the scored items and counts. A model-reported
     value is kept only as a consistency signal. This implements the
     registered definitions rather than changing the method.
   - **(b) Mechanical F2 (AP-15) and platform-row rules.** Lodge these as an
     adopted rule if their validation completes before lodgement, or else
     as a planned rule with the criteria declared in advance:
     - the rule matches the E8-v2 reference on the pilot F2 items at least
       as well as the selected model does;
     - the hybrid scorer (the rule for those items, the model elsewhere)
       clears both gates under the 2026-10-04 ruling.
   - **(c) Judgement items.** Evidence checks (quote verification, and
     identifiers present in the paper's text) flag items for adjudication
     and never override a score.
   - **(d) Audit.** Both values, the rule's version, and which value
     governed are recorded for every item a check touches.
7. **Reproduction-lane instrument clarifications (RULED by Shawn,
   2026-10-04; from the Phase 2 shakedown).** All four instruments are
   frozen, so each needs this amendment, and the §8 regression gate must
   run under the clarified text. Rulings are in
   `outputs/validation/phase2-shakedown/results-2026-10-03.md`, "Rulings
   (2026-10-04)", "Clarifications RULED". Draft wording for lodging:
   - **(a) `verdicts-and-precision.md`, paper error handling.** "When a
     reproduced value disagrees with a published value, the reproduction
     is internally consistent, and the authors' own materials support the
     reproduced value, classify as PAPER_ERROR rather than
     MAJOR_DISCREPANCY. Admissible evidence, in descending strength: (1)
     the paper's own tabulated data; (2) the authors' deposited data for
     that analysis; (3) the authors' own code, run unmodified (invariant
     2), on the authors' own data. The reproduction's own
     re-implementation is never evidence. The comparison report names the
     tier used. PAPER_ERROR findings escalate for human confirmation
     before entering study data."
   - **(b) `data-availability-taxonomy.md`, the L2 counting unit.**
     "Counting unit: the distinct datasets that the paper's verification
     targets require as inputs, as enumerated in the reproduction plan.
     Replicate runs presented as one result count as one dataset, which is
     available only if every part is retrievable. Upstream sources count
     only when a verification target requires them; otherwise they are
     provenance."
   - **(c) `coverage-rules.md`, check scope.** "Each target's verification
     method states its scope, which must equal the target's full
     published scope at the pre-stated tolerance. A check that covers part
     of a target is completed before the target counts as reproduced;
     otherwise the target is recorded as partially verified and counts
     against coverage. Where feasible, the plan declares the target's
     element count, and a deterministic gate compares it with the elements
     checked."
   - **(d) `invariants.md`, an invariant 2 corollary.** "Routine (execution
     environment): choosing among publicly available versions of
     dependencies and language runtimes, meaning releases from the
     package's official archive (for example CRAN or PyPI) or a tagged
     public repository, preferring the version current at publication.
     The search and the chosen versions are recorded. Fail-and-uplift: any
     edit to the authors' code that changes logic, indices, data
     selection, parameters, or the functions called, however obvious the
     intent. A deprecated function is handled by pinning a public version
     that still runs it; if none exists, replacing it is an edit, and so
     fail-and-uplift. A repaired result is
     recorded as uplift evidence and never counts toward coverage or the
     verdict."
     **Added the same day (Shawn, 2026-10-04):**
     - **Version-search cap.** "The environment is first built with every
       dependency at the release current at the article's first online
       appearance. If a specific dependency fails, at most its immediately
       preceding and following releases are tried, so a dependency has at
       most three attempts. Each attempt is logged."
     - **Wrapper boundary cases.** "Mechanics are applied in wrappers only,
       never in the authors' files. They are recorded, and they include:
       setting a random seed where the authors set none (stochastic
       tolerances still apply); converting an input file's format, allowed
       only when a mechanical check confirms every value is unchanged (any
       change of value is fail-and-uplift); and choosing the language
       runtime version, which is routine like any dependency."
8. **Pre-declared descriptive outcomes for the reproduction lane (RULED by
   Shawn, 2026-10-04).** Neither enters a verdict or coverage.
   - **(a) Verdict beside the environment-specification level.** Each
     paper's verdict is reported alongside the environment-specification
     level the authors provided. A SUCCESSFUL verdict that depended on the
     reproducer's version search therefore cannot be read as the authors
     having captured a working environment.
   - **(b) Recoverable with repair.** For each fail-and-uplift target, the
     result a repair recovers and the repair's size are reported. Size is
     measured as the lines changed in the authors' code. Also reported:
     recovery against paper age, since deprecations accumulate over time.
   **Added 2026-10-05 (Shawn, adopting the Fable review of PR #7):**
     - **Mechanics placed in an authors' file.** A result resting on an
       authors' file edited for mechanics, rather than in a wrapper, counts
       only after a re-run with the mechanics in a wrapper and the file
       restored byte-identical. A change of logic, indices, data, parameters,
       or functions called stays fail-and-uplift whatever its effect.
9. **Evidence packs (harvester v1.2) and the census-input re-validation
   (Shawn, 2026-10-04).** Building the F2 rule showed that the 2026-08-17
   packs carry no creators, descriptions, or keywords, so the scorer was
   validated on inputs the census will not use. Ruled: upgrade the packs,
   then re-validate before the census, folded into the pre-census
   supplement check (one `medium` arm, 15 scorings, API gate) on v1.2
   packs, supplements, the clarified instruments, and the hybrid F2, with
   pass criteria declared in amendment 3. The §8 regression gate is a
   reproduction-lane test that never reads packs, so it is not the
   re-validation. Validation of the F2 rule:
   `../outputs/validation/f2-rule-hybrid-2026-10-04/report.md`
   (`06c1ca9`).
10. **Deviation: the §8 regression gate's baseline (RULED by Shawn,
    2026-10-05: adopt Astra's correction-ledger approach).** The executed-code
    audit (PR #7) found pilot verdicts resting on re-implementations and on
    versions other than the selected one. Pilot artefacts are kept as they
    are. A frozen per-target correction ledger becomes the pass criterion,
    and the strict comparison is reported beside it. The conditions on the
    ledger come from the Fable review. Draft text: `amendment-3-draft.md`
    §9.

---

## Entry 6 — 2026-10-09: amendment 3 applied to the frozen instruments

**Status: repository-side application of lodged text (amendment 3 §10 step
2). Pending review and the registrant's merge; not yet in force for any
run.**

Amendment 3 (lodged 2026-10-08, revision `6ac775afb5ed5b4afee88a4a`, tag
`osf-amendment-3-2026-10-08`) clarifies five frozen instruments. §10 step 2
edits them to the lodged text, with new versions and content hashes. Branch
`feat/amendment-3-instruments` (not merged).

| Instrument | Version | Receipt token | sha256 (first 16) | Lodged text |
| --- | --- | --- | --- | --- |
| `fair-instrument.md` | 2.1 to 2.2 | `bf984697092c0c20` | `3b94b57591b63106` | §4, items 1 to 12 |
| `verdicts-and-precision.md` | 1.0 to 1.1 | `46eb4ad0bfcb3b92` | `e76c2057b9e0a170` | §7(a) |
| `data-availability-taxonomy.md` | 1.0 to 1.1 | `464c1474a18abab6` | `beb5889dfd384838` | §7(b) |
| `coverage-rules.md` | 1.0 to 1.1 | `414de27c0d871a1d` | `b211a2318c7162ce` | §7(c) |
| `invariants.md` | 1.0 to 1.1 | `c70d484af7e75ec4` | `f74f393385d3074b` | §7(d), with its six ruled cases |

**How the text was placed.** Every lodged word was read from
`osf-amendment-3.txt` at the tag and only re-wrapped. A whitespace-collapsed
comparison finds each lodged paragraph in its instrument (routing design §6,
maintenance rule 4): §4's preamble, twelve items, and BI note in the FAIR
instrument's new v2.2 section; and §7's quoted text, labels, and the
amendment's own readings in the four reproduction instruments. Existing
sentences are left as they stand, except where the lodged text supersedes
them:

- the FAIR rubric lines, aggregation rule, and completeness procedure gain
  pointers to the items that govern them;
- the aggregation rule's "including non-principal upstream sources" is
  qualified to "including a non-principal upstream source only where
  reproducing the reported results needs it (v2.2 clarification 3)", since
  unqualified it still told the completeness lane to count the fully
  transcribed source that item 3 excludes (Astra's review of PR #9, B1,
  2026-10-09);
- the L2 definition's old counting-unit parenthetical points to the lodged
  counting unit;
- the paper-error paragraph's first sentence is replaced by the lodged
  text, and the tolerance rule's "differences indicate a bug in the
  reproduction" now admits a supported PAPER_ERROR as the other cause
  (the same review, N1).

**Deliberate differences (rule 4).** One. The v1.0 paper-error paragraph's
verification procedure is kept after the lodged text, reworded from an
instruction ("To verify a suspected paper error: apply the published formula
to the paper's own input values…") to an optional diagnostic: a calculation
from the paper's own formula and tabulated inputs can check their
consistency with the reported output, is recorded with its evidence tier,
and does not replace the lodged evidence and confirmation requirements. As
an instruction it could read as a prerequisite for the lodged tiers, or as
licence to treat a reproducer's formula as evidence (the same review, N1).
§7(d)'s verification-aid ruling relies on the same check, which survives as
the diagnostic. Its pointer to modernisation plan §4.4 is dropped, since the
lodged text states the escalation itself.

**Consumers.** The Pass 6 prompt's mirror of the FAIR canon region and the
reproduction skill's mirror of the paper-error segment are re-spliced byte
for byte, and each banner cites the new version and token. The agents told
to verify these versions move with them: the four FAIR assessors (definition
v1.2 to v1.3), and the reproduction planner, executor, and adversarial
reviewer (v1.1 to v1.2). All digests are re-registered in `manifest.yaml`.
The D5 gate passes. The executor's definition is also edited on PR #7, so
whichever change merges second renumbers it.

**Not done here.** §10 steps 3 to 6: the correction ledger's ruling and
freeze, the §8 regression gate under the clarified text, and the census
re-validation. Routing design rule 6 asks that the regression gate's
checklist re-confirm the routing class of every changed file: none changes
class (each instrument stays pushed; both mirrors stay mirrors).
