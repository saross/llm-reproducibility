# OSF amendment 3 — DRAFT for registrant review (2026-10-04)

**Status: DRAFT, not lodged.** Consolidated on 2026-10-04 from the erratum
log's "Queued amendment 3 scope (running list)", items 1–9
(`erratum-log.md`), for the registrant to edit and lodge. Lodgement follows
the amendment-1 and amendment-2 route: Open Science Framework (OSF)
Application Programming Interface (API), versioned registration update,
text appended to the Summary field under a dated banner, DOI unchanged
(10.17605/OSF.IO/DQNHG). Registrant decisions still open are marked
**[D-n]** in the text and listed after it.

**Hard stops.** This amendment must lodge before three things happen:

1. the frozen instruments are edited to the clarified text in §4 and §7;
2. the registered §8 regression gate runs under that text;
3. the census-input re-validation (§6) and census scoring begin.

The repository implementation of §5 and §6 (harvester v1.2, the F2 rule,
and the hybrid validation) is already committed. That is compliant on the
amendment-1 precedent: the text describes changes present in the
repository at lodgement, and no analysis they govern runs before it.

**Why this amendment.** The 2026-10-03 re-derivation of the pilot
reference (E8-v2) and the 2026-10-04 gates ruling produced three kinds of
change. First, model selection moved the census scorer off the registered
pins to a newer model that cleared the same gates. Second, adjudication
exposed rules the instruments do not state, and the reproduction-lane
shakedown did the same for the reproduction instruments. Third, two
measurement defects surfaced: a model miscount that the output schema let
through, and evidence packs that lacked the fields one sub-principle
needs. Each is lodged here before the analyses it governs.

---

## Amendment text (draft for the OSF field)

### 1. Correction: amendment 2 §2's precedent case

Amendment 2 §2 closes its identifier-recovery rule with "Precedent case:
marwick-2025's cited 10.5281/zenodo.14561925 resolves at neither DataCite
nor Zenodo (2026-08-15)." That sentence is corrected, because the paper
does not cite 10.5281/zenodo.14561925. The identifier appears nowhere in the
version of record, the preprint, or the corpus text (verified 2026-10-03).
Its only source was the pilot extraction record, a model-produced record
that carried an unverified identifier into the declared-links registry and
from there into the lodged text. The paper cites the compendium's concept
DOI, 10.5281/zenodo.14897252, and the record "recovered" for the dead
identifier, 10.5281/zenodo.15603267, is version 1.3 of that same concept.
No deposit was lost, and the paper has no dead-link defect. The
identifier-recovery rule itself is unaffected, because it worked as
specified on a wrong input. The registry entry is withdrawn and kept for
the record (erratum log, Entry 4). As a safeguard, every identifier in the
registry must appear verbatim in the paper or its supplement before
harvest (§5(c)).

### 2. Census scorer: claude-opus-5-5 at effort medium

The census scores FAIR with `claude-opus-5-5` at reasoning effort
`medium`, in place of the registered model pins (`claude-sonnet-5`,
`claude-opus-5`, and `claude-fable-5`). Opus 5.5 is a newer model in the
same tier. Before any data, the registrant declared that an Opus 5.5 configuration was eligible only if it
cleared both gates under the 2026-10-04 ruling (§3), and that amendment 1's
selection rule (the cheapest eligible configuration at the prices in force)
would then apply unchanged across registered and Opus 5.5 configurations
alike.

- **Gate results.** All three Opus 5.5 efforts were eligible. Stability
  was 0.953, 0.953, and 0.967, and BI-excluded majority-vote concordance
  0.922, 0.929, and 0.922 (high, medium, and xhigh). Two independent
  derivations, the analysis tool and a blinded re-derivation script (H13),
  agree on every figure.
- **Prices in force at selection.** The provider's published table,
  cached 2026-09-25, lists `claude-opus-5-5` at $4 input and $20 output per
  million tokens, and `claude-opus-5` at $5 and $25.
- **Rule applied.** At `medium`, the 15 benchmark scorings cost $8.70
  measured per request. A known output under-count in the usage records
  (register F-019) bounds the true cost at $9.25 (central) and $9.37
  (upper), still below the next configuration's lower bound (`high`,
  $9.55). The cheapest registered eligible configuration, `claude-opus-5`
  at `high`, cost $17.27.
- **Source:** `outputs/validation/opus-5-5-arms-2026-10/results-2026-10-04.md`.

The registered regression gate (§8 of the registration) and the
census-input re-validation (§6) run on this configuration.

### 3. Gate statistics: concordance clarified, beyond-instrument items excluded

*(a) Clarification of amendment 1 §3.* Concordance is majority-vote item
agreement. Each item's score is the majority of three runs, and it is
compared with the reference score. The gate is the proportion of items
that agree. This is the operationalisation used for every concordance
figure the study has reported, including those in amendment 2. A blinded
re-derivation before the gates ruling showed that the registered phrase
"(same statistic)" also admits a stricter reading (all three runs agree
and equal the reference). That reading counts each unstable item against
concordance as well as stability, and it was not adopted.

*(b) Deviation: beyond-instrument items excluded from the concordance
gate.*

- The re-derived pilot reference tags 9 of 150 items as beyond-instrument
  (BI). Their reference scores rest on evidence the validation spawns did
  not have. For four items (all dye-et-al-2023) that evidence is in the
  papers' supplementary files, which the spawns were deliberately not
  given. For five it is deposit content that neither the paper nor the
  evidence pack recorded, such as file formats, a lockfile, and version
  relations. Four items also rest on a principle adopted during
  adjudication that the instrument does not state.
- The registrant ruled, before any model selection, that concordance
  computed without these items (141) is the gate statistic. Concordance
  over all 150 items is reported alongside it.
- The tags were assigned on 2 October 2026, before concordance was
  computed. The reference adjudication was not blinded to the arms' scores.
- Under this ruling the selected configuration (§2) scores 131/141 = 0.929.
  Over all 150 items it scores 133/150 = 0.887, below the gate. Under the
  hybrid scorer of §5 it scores 137/141 = 0.972, and 139/150 = 0.927 over
  all items.
- The census-input re-validation (§6) gives the spawns the inputs whose
  absence motivated this deviation, and states its own gate statistic.

### 4. FAIR instrument clarifications (v2.1 → v2.2) [D-1]

The E8-v2 adjudication (registrant, 2026-09-03 to 2026-10-03) adopted the
principles below while re-deriving the pilot reference. Each item is
scored as stated from instrument v2.2 onwards. Their reasoning and the
cases that produced them are recorded in the adjudication log
(`outputs/validation/e8-v2-rederivation/adjudication-log.md`, principles
AP-3 and AP-8 to AP-17). Each was checked before adoption for foreseeable
perverse results when generalised (AP-7).

1. **I1 assesses the artefact as served (AP-9).** Code or data available
   only as text or tables inside a PDF fails I1, whatever formal language
   underlies it, because extracting it is reconstruction. Two guards
   apply. Where the same artefact is also served in a machine-actionable
   form, I1 scores the best form. Illustrative snippets are not principal
   artefacts. For example, dye-et-al-2023's OxCal model and R code are served
   only inside a supplement PDF, so I1 = 0 for both.
2. **R1.1 tests whether any usage licence is published (AP-8).** R1.1 = 1
   when a licence is published for the artefact, however restrictive.
   Same-artefact contradictions still resolve to the most restrictive
   licence, which passes if it is itself a published licence. "Available on
   request" and an "all rights reserved" notice with no grant score 0. A
   grant followed by "all other rights reserved" passes, and a copyright
   notice beside a licence is not a conflict. R1.1 does not adjudicate
   whether the licensor holds the rights it licenses (item 11).
3. **Completeness counts only what reproduction requires (AP-10).** An
   upstream source enters the data-completeness denominator only if
   reproducing the reported results needs it. A source the authors fully
   transcribed into their deposited inputs is provenance, scored at R1.2
   and listed with its tier but not counted. If the transcription is
   partial and the results need fields only the source holds, the source
   counts. For example, herskind-riede-2024's printed catalogue (Płonka 2003),
   fully transcribed into S1.xlsx.
4. **A DataCite-registered deposit with its mandatory metadata passes R1.3
   for data (AP-11).** A minimal record's poverty is scored at F2,
   not R1.3. For code, R1.3 uses the instrument's code list (package
   structure, CITATION.cff, CodeMeta, or community review) and not this
   route. A research compendium without package metadata does not meet the
   code list, although its lockfile and container are credited at R1.2
   and I3 (an initial decision, open to reconsideration).
5. **Version selection for versioned deposits (AP-12, as refined
   2026-10-03).** Where the paper cites exactly one version (a version DOI,
   tagged release, or commit), that version is scored and reproduced.
   Three checks always run. They compare the deposit's files with the
   published supplement by checksum, test whether its deposited outputs
   reproduce the values printed in the paper (a published-values match),
   and read its dates against the article history. A cited version that fails the checks
   is a version-citation finding, and the score still assesses it. Where no
   single version is cited (a concept DOI, an untagged repository URL, or
   two versions), this is flagged, and the checks choose in that order. If
   the candidates do not differ on any scored fact, the choice is recorded
   as immaterial. If they differ and nothing settles it, both are scored
   and the sensitivity reported. For example, crema-et-al-2024 cites a concept
   DOI, and the published-values match selects v1.0.0. A date-only rule
   would have chosen v2.0.0, which never produced the published numbers.
6. **Unpublished principal data fail conjunctively (AP-13).** Under the
   aggregation rule, an unpublished or closed principal dataset fails every
   artefact-property sub-principle (F1, A1.1, A1.2, R1.1, and the rest).
   This is the registered unscoreable → 0 default applied as written. The
   article and its summary statistics are never scored as if they were the
   data. For example, key-et-al-2024 requires 13 assemblage datasets, of which
   10 are unpublished. The completeness percentage carries the nuance that
   conjunction removes.
7. **Documentation earns R1 and R1.2, but the paper is never the metadata
   for machine-actionable sub-principles (AP-14).** R1 and R1.2 can be
   satisfied by the paper's documentation even for closed data, because
   FAIR separates metadata from data (A2). Conjunction still applies to
   R1.2. Prose in a paper never supplies F2, F3, F4, I1–I3, or R1.3.
   Dependency identifiers count for I3 when they are deposited in the
   article's machine-readable reference metadata, as Crossref records them.
8. **F2 needs a machine-readable record that itself describes the artefact
   (AP-15).** F2 = 1 requires all four of creators, title, a substantive
   description of the artefact's own content, and at least one subject
   keyword, in the deposit's own record. A description that is empty or
   only cites the paper fails, as do bare registrar-mandatory fields. The
   instrument's own F2 wording names keywords ("structured: authors, title,
   keywords, description"), as does F-UJI's core-descriptive-metadata test.
   A rich description without keywords therefore scores 0, a harshness the
   registered wording accepts. For example, marwick-2025's Zenodo record has a
   one-sentence description citing the paper and no keywords, so F2 = 0.
   §5(b) applies this item mechanically.
9. **A complete machine-readable dependency manifest satisfies code I3
   (AP-16).** A lockfile or manifest that pins every dependency by name,
   exact version, and source counts as qualified references (for example
   `renv.lock`, a pinned `requirements.txt`, a versioned `DESCRIPTION`, or
   `environment.yml`). For example, marwick-2025's `renv.lock` pins 152
   packages.
10. **Independent code review counts for code R1.3 only when recorded
    machine-readably (AP-17).** A journal reproducibility review or a
    CODECHECK counts as community review when it leaves a machine-readable
    record, such as a certificate DOI or a badge or relation in the deposit
    or article metadata. A prose acknowledgement is recorded as the finding
    "reviewed, unrecorded" and does not score.
11. **Rights problems are coded, not scored.** Where an open licence
    covers content the licensor may not hold rights to, the census records
    a non-scoring finding. For data the coding variable is "data shared,
    rights-incompatible". For example, marwick-2025 deposits Web of Science
    exports under an open licence, and key-et-al-2024 distributes code
    adapted from a GPL-2 package under CC BY.
12. **Principal artefacts on unmanaged hosting (AP-3).** An artefact served
    from a personal or unmanaged host is principal if reproduction needs
    it, and it fails what the evidence shows it fails (typically F1, A2, and
    R1.1). For example, dye-et-al-2023's `beads-1.csv`, read by the supplement's
    R code from a personal server.

Items 1 and 9 extend the instrument's text, so reference items decided by
them carry the BI `rule` tag (§3(b)).

### 5. Deterministic checks on scoring outputs

The registrant ruled a disagreement policy on 2026-10-04, decided by the
kind of quantity a check concerns.

*(a) Derived fields are computed.* Section totals, `coverage_percentage`,
and `coverage_category` are computed from the scored items and counts. A
model-reported value is kept only as a consistency signal, and the
computed value governs. This implements the registered definitions rather
than changing the method. For example, one benchmark payload recorded a
`code_fair` total of 7 against an item sum of 8, and the schema allowed
it. The model's items, which the gates validated, stand.

*(b) F2 is scored mechanically where the rule can decide it (adopted).* A
deterministic rule (`scripts/score-f2-rule.py` v1.0) applies §4 item 8 to
structured inputs, namely the curated registry and the scored version's
DataCite record in the evidence pack. Its scope is limited to what the pilots could
validate.

- **The rule gives 0s.** F2 = 0 is decided mechanically where any principal
  artefact is unpublished (§4 item 6), served only as a journal supplement
  (amendment 2 §1, the publisher-supplement row), or served from unmanaged
  hosting (§4 item 12). It is also decided where the scored version's
  record lacks creators, a title, a non-empty description, or a subject
  keyword. The test is conjunctive across principal artefacts.
- **The registrant confirms 1s.** Where every principal deposit has all
  four fields, whether the description is substantive goes to the
  registrant. The rule never awards F2 = 1.
- **Missing inputs fall back.** Where an input is missing, the model's score
  stands and is flagged.
- **Validation (2026-10-04, no API spend).** The rule matches the E8-v2
  reference on all 10 pilot F2 items. The selected model's majority matches
  4. The hybrid scorer clears both gates for the selected configuration.
  Stability is unchanged at 143/150, and concordance is 137/141 = 0.972
  (BI excluded) and 139/150 = 0.927 (all items). Two derivations agree on
  every figure (`outputs/validation/f2-rule-hybrid-2026-10-04/report.md`).
- **Limitation.** Every pilot reference F2 is 0, so the pilots test only the
  rule's 0 paths. That is the reason the rule never awards a 1.
- **Platform-row implications beyond F2** (for example F3, F4, and A2 for
  supplement-only deposits) stay flag-only until validated and amended.
  [D-2]
- **Reporting.** Model–rule disagreement rates are reported as a study
  finding.

*(c) Evidence checks flag; they never override.* Quote verification against
the paper's text, and a check that every identifier a payload or the
registry cites appears in the paper or its supplement, send an item for
re-scoring or adjudication. They never set a score.

*(d) Audit.* For every item a check touches, both values, the rule's
version, and which value governed are recorded.

### 6. Evidence packs (harvester v1.2) and the census-input re-validation

*(a) Pack specification, extending amendment 2 §2.* Harvester v1.2 also
records each registry record's creators, titles, descriptions, subject
keywords, related identifiers, version, version dates, and file list with
formats. It resolves the version selected under §4 item 5, so the pack
holds that version's own record. It keeps every raw response body,
addressed by the content hash the pack already records, outside the
public repository. Packs carry registry facts only. The registry's
curation fields (which links are principal, where each is hosted, and
which version was selected) record adjudication outcomes and are never
copied into packs, so a scoring spawn is never told the reference's
judgements.

*(b) Why re-validate.* The registered benchmark validated the scorer on
packs without these fields and on papers without their supplements. The
census will use both. The 2026-08-17 packs could not show, for example,
that a deposit's keyword field was empty. Every Opus arm's majority
credited F2 on all three pilot Zenodo deposits, and 20 of the 90 Opus F2
evidence strings for those deposits state that the pack did not show the
description or keyword fields. The gates have therefore not
yet tested the scorer on the inputs the census will give it.

*(c) Pre-declared re-validation.* Before census scoring, the selected
configuration (§2) is re-run on the five pilot papers, three runs each (15
scorings), with:

- the paper and its published supplementary files (the 2026-10-02 reading
  of "the paper source");
- a v1.2 evidence pack from a dated harvest committed before the run;
- the clarified instruments (§4 and §7);
- the hybrid scorer (§5(b)) and computed derived fields (§5(a)).

Both gates, stability and majority-vote concordance against E8-v2, must
reach at least 0.90. The concordance gate is computed over all 150
items. The re-validation supplies the supplementary files, the
deposits' file lists and relations, and the §4 rules, which together cover
most of what the §3(b) exclusion was for. A lockfile's contents remain
outside the packs.
The BI-excluded figure is reported alongside. [D-3] If either gate fails,
the registered remediation ladder applies (amendment 2 §4), and changes are
re-tested one at a time to find the cause. The result, the F2 model–rule
disagreement rate, and the scores on the nine BI items are reported with
the study results.

*(d) Boundaries.* The E8-v2 reference is unchanged and remains unblinded
(amendment 2 §3). For the pilots, the registry's principal-artefact and
version curation was taken from the adjudication, so the re-validation does
not measure curation error. For census papers, curation follows
[D-4: the census curation procedure, to be stated].

### 7. Reproduction-lane instrument clarifications

The Phase 2 shakedown (2026-10-03) and the registrant's rulings of
2026-10-04 clarify four frozen reproduction instruments
(`outputs/validation/phase2-shakedown/results-2026-10-03.md`, "Rulings
(2026-10-04)"). The §8 regression gate runs under the clarified text.

- **(a) `verdicts-and-precision.md`, paper error handling.** "When a
  reproduced value disagrees with a published value, the reproduction is
  internally consistent, and the authors' own materials support the
  reproduced value, classify as PAPER_ERROR rather than MAJOR_DISCREPANCY.
  Admissible evidence, in descending strength: (1) the paper's own
  tabulated data; (2) the authors' deposited data for that analysis; (3)
  the authors' own code, run unmodified (invariant 2), on the authors' own
  data. The reproduction's own re-implementation is never evidence. The
  comparison report names the tier used. PAPER_ERROR findings escalate for
  human confirmation before entering study data."
- **(b) `data-availability-taxonomy.md`, the L2 counting unit.** "Counting
  unit: the distinct datasets that the paper's verification targets
  require as inputs, as enumerated in the reproduction plan. Replicate runs
  presented as one result count as one dataset, which is available only if
  every part is retrievable. Upstream sources count only when a
  verification target requires them; otherwise they are provenance."
- **(c) `coverage-rules.md`, check scope.** "Each target's verification
  method states its scope, which must equal the target's full published
  scope at the pre-stated tolerance. A check that covers part of a target is
  completed before the target counts as reproduced; otherwise the target is
  recorded as partially verified and counts against coverage. Where
  feasible, the plan declares the target's element count, and a
  deterministic gate compares it with the elements checked."
- **(d) `invariants.md`, an invariant 2 corollary.** "Routine (execution
  environment): choosing among publicly available versions of dependencies
  and language runtimes, meaning releases from the package's official
  archive (for example CRAN or PyPI) or a tagged public repository,
  preferring the version current at publication. The search and the chosen
  versions are recorded. Fail-and-uplift: any edit to the authors' code that
  changes logic, indices, data selection, parameters, or the functions
  called, however obvious the intent. A deprecated function is handled by
  pinning a public version that still runs it; if none exists, replacing it
  is an edit, and so fail-and-uplift. A repaired result is recorded as
  uplift evidence and never counts toward coverage or the verdict."
  - **Version-search cap.** "The environment is first built with every
    dependency at the release current at the article's first online
    appearance. If a specific dependency fails, at most its immediately
    preceding and following releases are tried, so a dependency has at
    most three attempts. Each attempt is logged."
  - **Wrapper boundary cases.** "Mechanics are applied in wrappers only,
    never in the authors' files. They are recorded, and they include:
    setting a random seed where the authors set none (stochastic tolerances
    still apply); converting an input file's format, allowed only when a
    mechanical check confirms every value is unchanged (any change of value
    is fail-and-uplift); and choosing the language runtime version, which
    is routine like any dependency."

### 8. Pre-declared descriptive outcomes for the reproduction lane

Neither outcome enters a verdict or coverage.

- **(a) Verdict beside the environment-specification level.** Each paper's
  verdict is reported alongside the environment-specification level the
  authors provided. A SUCCESSFUL verdict that depended on the reproducer's
  version search therefore cannot be read as the authors having captured a
  working environment.
- **(b) Recoverable with repair.** For each fail-and-uplift target, the
  result a repair recovers and the repair's size are reported. Size is
  measured as the lines changed in the authors' code. Recovery is also
  reported against paper age, since deprecations accumulate over time.

### 9. Order of operations

1. The registrant lodges this amendment on OSF as a versioned registration
   update.
2. The frozen instruments are edited to the §4 and §7 text and given new
   version numbers, with content-integrity hashes registered.
3. The §8 regression gate runs on the selected configuration under the
   clarified text.
4. The census-input re-validation (§6) runs on the selected configuration.
5. Census scoring begins only after both pass, or after the remediation
   ladder resolves a failure.

---

## Decisions for the registrant before lodgement

- **D-1. Instrument clarifications in this amendment.** Running-list item 2
  left open whether the E8-v2 clarifications lodge here or as a gated edit.
  The draft lodges them (§4), since the instrument is frozen and the census
  re-validation (§6) runs on the clarified text. The version number v2.2,
  and a matching guide bump, are proposed.
- **D-2. Platform-row rules beyond F2.** Item 6(b) named "platform-row
  rules" alongside F2. Only F2 is built and validated, so the draft keeps
  the rest flag-only. Alternative: declare them as planned rules with the
  same two validation criteria.
- **D-3. The re-validation's gate statistic.** The draft uses all 150 items,
  because the re-validation removes most of the reasons for the BI
  exclusion (one, marwick's lockfile contents, remains).
  Alternative: keep the BI-excluded statistic as in §3(b). For context, the
  hybrid at `medium` already scores 139/150 = 0.927 on the old inputs.
- **D-4. Census registry curation.** The F2 rule and version selection read
  curated fields (`role`, `home`, `carries`, `scored_version`,
  `unpublished_principal`). For the pilots these came from adjudication.
  The census needs a stated procedure (who curates, from which sources, and
  how curation is checked) before §6(d) can be completed.
- **D-5. Correction to Entry 5's proposed wording.** Entry 5 said the BI
  items rest on "the papers' supplementary files". The worksheet's notes
  show that holds for the four dye items only; the other five (crema data
  I1 and I3, herskind data I1, marwick data I1 and code I3) rest on deposit
  content the packs never recorded. §3(b) is corrected accordingly. Those
  five were not deliberately withheld, which the BI `input` definition
  ("deliberately not given") does not quite cover.

## Pre-lodgement checklist

- [ ] Registrant reads and edits the full draft; decisions D-1 to D-5 ruled.
- [ ] Consistency check (maintenance rule 4): §4 and §7 text against the
      adjudication log and the shakedown rulings; §5 and §6 against the
      planning note, the F2 report, and `manifest.yaml`; deliberate
      differences recorded below.
- [ ] Token classes verified: numbers and statistics; identifiers (DOIs,
      versions, model identifiers, dates); registered vocabulary; quoted
      strings.
- [ ] Register exit checks run on the final text and recorded.
- [ ] D5 manifest-consistency gate PASS and full test suite green at the
      lodgement commit; repository tagged `osf-amendment-3-<date>`.
- [ ] Paste artefact produced with `unwrap-paste-file.py`; flowing lines,
      no tables.
- [ ] Lodged via the OSF API as a versioned update appended to the Summary
      field; DOI unchanged; round-trip byte check; change set exactly
      `["summary"]`; public page render-checked.
- [ ] Only then: instrument edits, regression gate, re-validation, census.

## Sources

| Section | Source |
|---|---|
| §1 | `erratum-log.md` Entry 4 |
| §2 | `outputs/validation/opus-5-5-arms-2026-10/results-2026-10-04.md`, `design-note.md` (Q4), `selection-cost.json`; erratum-log running-list item 5 |
| §3 | `erratum-log.md` Entry 5; `outputs/validation/gates-ruling-2026-10-04/ruling.md`; F2 report (hybrid figures) |
| §4 | `outputs/validation/e8-v2-rederivation/adjudication-log.md` (AP-3, AP-8 to AP-17); `wiki/planning/instrument-clarification-plan.md`, pre-census items (i)–(xiv) |
| §5 | `wiki/planning/deterministic-output-checks.md` (policy RULED 2026-10-04); `outputs/validation/f2-rule-hybrid-2026-10-04/report.md`; `outputs/validation/payload-quality-2026-10-04/` |
| §6 | `scripts/harvest-artefact-metadata.py` v1.2; `protocol/supplements-as-inputs-2026-10-02.md`; amendment 2 §§2–4 |
| §7, §8 | `erratum-log.md` running-list items 7 and 8; `outputs/validation/phase2-shakedown/results-2026-10-03.md` |

## Drafting record (2026-10-04)

**Registers loaded** (academic-prose gate):

1. `~/personal-assistant/data/notes/style-guides/academic/reference_register-academic.md`
2. `~/personal-assistant/data/notes/style-guides/academic/reference_register-preregistration.md`
3. `.notes/reference_register-prereg.md` (project layer)
4. `~/personal-assistant/data/notes/style-guides/reference_anti-tic.md`

**Exit checks on the amendment text** (sections 1–9, about 3,100 words;
`register-gate.py` advisories, read item by item):

- Em-dashes: 0. The gate's count of 3 is en dashes in ranges ("I1–I3").
- Semicolons: 11, of which 7 are in the §7 rule text already ruled on
  2026-10-04 and quoted unchanged; the other 4 end list items.
- Announcement colons: about 1.9 per 1,000 words, against a 1.6 ceiling.
  The remaining colons are in headings, in the quoted §7 rule text, and
  in one list of conditions (§6(c)).
- Boosters, "whilst", and "not X but Y": 0. "The authors" appears only
  for the authors of the studied papers, never as self-reference.
- Every specific was re-read at its source this session. The figures in
  §2 are from `results-2026-10-04.md` and `selection-cost.json`, the
  hybrid figures in §§3 and 5 from the F2 report's summaries, and the BI
  bases in §3(b) from `worksheet.json`.
