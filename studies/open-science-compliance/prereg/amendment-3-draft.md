# OSF amendment 3 — DRAFT for registrant review (revised 2026-10-06)

**Status: DRAFT, not lodged.** Consolidated on 2026-10-04 from the erratum
log's "Queued amendment 3 scope (running list)", items 1–9
(`erratum-log.md`), for the registrant to edit and lodge. Revised on
2026-10-06 after the registrant's read and Astra's review; the revision
record is at the end of this file. Lodgement follows
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
the record (erratum log, Entry 4). As a safeguard, every identifier the
registry records as cited must appear verbatim in the paper or its
supplement before harvest, and a version selected or a record recovered
from a cited identifier carries its own provenance instead (§5(c)).

### 2. Census scorer: claude-opus-5-5 at effort medium

The census scores FAIR with `claude-opus-5-5` at reasoning effort
`medium`, in place of the registered model pins (`claude-sonnet-5`,
`claude-opus-5`, and `claude-fable-5`). Opus 5.5 is a newer model in the
same tier. The three Opus 5.5 arms were exploratory validation runs, made
after the registered benchmark and the unblinded reference work, with no
amendment lodged before them. Before those arms produced any data, the
registrant declared that an Opus 5.5 configuration was eligible only if it
cleared both gates under the 2026-10-04 ruling (§3), and that amendment 1's
selection rule (the cheapest eligible configuration at the prices in force)
would then apply unchanged across registered and Opus 5.5 configurations
alike. The arms and the selection therefore preceded this amendment, and
census scoring has not begun.

- **Gate results.** All three Opus 5.5 efforts were eligible. Stability
  was 0.953, 0.953, and 0.967, and BI-excluded majority-vote concordance
  0.922, 0.929, and 0.922 (high, medium, and xhigh). Two independent
  derivations, the analysis tool and a blinded re-derivation script (H13),
  agree on every figure.
- **Prices in force at selection.** The provider's published table,
  cached 2026-09-25, lists `claude-opus-5-5` at $4 input and $20 output per
  million tokens, and `claude-opus-5` at $5 and $25.
- **Rule applied.** At `medium`, the 15 benchmark scorings cost $8.70 as
  recorded per request. A known output under-count in the usage records
  (register F-019) makes that figure a lower bound, so the cost was
  estimated twice more, imputing each affected request's output from the
  complete requests of its kind, which gives $9.25 at their median and
  $9.37 at their maximum. The selection is unchanged under both, since the
  next
  configuration (`high`) recorded $9.55 before any imputation. The
  cheapest registered eligible configuration, `claude-opus-5` at `high`,
  recorded $17.27. Every figure is an API-equivalent scoring cost in
  United States dollars at the prices above, for the scoring model only
  and excluding reconciliation. The runs were billed through a
  subscription plan, not invoiced per token.
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
- The tagging convention was adopted on 2 October 2026 and the tagged set
  was completed on 3 October (worksheet commits `7298681` to `7da90bf`),
  before the six-arm concordance was computed and committed later that
  day (`6e0d17a`). The exclusion ruling of 4 October followed that
  computation. The reference adjudication was not blinded to the arms'
  scores.
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
   Three checks always run where their inputs exist. They compare the
   deposit's files with the published supplement by checksum, test whether
   its deposited outputs reproduce the values printed in the paper (a
   published-values match), and read its dates against the article
   history. A check whose inputs do not exist, because there is no
   supplement or no deposited numerical output, is recorded as
   unavailable, not as failed. A cited version that fails a check is a
   version-citation finding. The score still assesses the cited version.
   Reproduction tries it first, as a reader would, and then the version the
   checks identify, recorded as a recoverable repair whose results are
   uplift evidence under §7(d) and never count toward coverage or the
   verdict. Where no single version is cited (a concept DOI, an untagged
   repository URL, or more than one version), this is flagged, and the
   checks choose in that order, the date check selecting the latest
   version released before the article first appeared online. If the
   candidates do not differ on any scored fact, the choice is recorded as
   immaterial. If they differ and nothing settles it, every candidate is
   scored, the earliest-released candidate supplies the value the census
   analyses use, and the others are reported as a sensitivity. For
   example, crema-et-al-2024 cites a concept DOI, and the published-values
   match selects v1.0.0. A date-only rule would have chosen v2.0.0, which
   never produced the published numbers.
6. **Unpublished principal data fail conjunctively (AP-13).** Under the
   aggregation rule, a principal dataset that is deposited nowhere, whether
   unpublished, "available on request", or held only by the authors, fails
   every artefact-property sub-principle (F1, A1.1, A1.2, R1.1, and the
   rest), because it has no persistent identifier, no retrieval protocol,
   no access mechanism, and no licence for the evidence to show. This is
   the registered unscoreable → 0 default applied as written. It does not
   reach a deposited dataset under access control, which is scored on what
   its record evidences. Its persistent identifier passes F1, its published
   licence passes R1.1 (item 2), and a documented and justified access
   mechanism passes A1.2 (amendment 2 §1 item 4, and the registration's
   ethical and legal exception in §7.1). The article and its summary
   statistics are never scored as if they were the data. For example,
   key-et-al-2024 requires 13 assemblage datasets, of which 10 are
   deposited nowhere. The completeness percentage carries the nuance that
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
    from a personal or unmanaged host, with no metadata record of its own,
    is principal if reproduction needs it, and it fails what the evidence
    shows it fails (typically F1, F2, A2, and R1.1). For example,
    dye-et-al-2023's `beads-1.csv`, read by the supplement's R code from a
    personal server.

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
  artefact is deposited nowhere (§4 item 6), served only as a journal
  supplement (amendment 2 §1, the publisher-supplement row), or served from
  unmanaged hosting with no metadata record (§4 item 12). It is also
  decided where the scored version's record lacks creators, a title, a
  non-empty description, or a subject keyword. The test is conjunctive
  across principal artefacts.
- **The registrant confirms 1s [D-8].** Where every principal deposit has
  all four fields, whether the description is substantive goes to the
  registrant. The rule never awards F2 = 1. The registrant is also the
  human validator of registration §8, so the validation is kept separate
  from these confirmations. The seeded 12-paper subsample is drawn before
  any census confirmation starts, the confirmations on those papers are
  deferred until the registrant has hand-scored them, and the hand-scorer
  is blinded to the rule's outputs as well as to the model's. The
  registered validation statistics compare the hand scores with the raw
  model majority. For F2 on the subsample, three figures are reported. The
  rule's 0s are compared with the hand score, the raw model majority is
  compared with the hand score, and the confirmed 1s are not validated,
  because they are the registrant's own decisions. Agreement with the
  hybrid scorer is reported alongside as a secondary figure.
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
- **Platform-row rules beyond F2 (planned, declared in advance).** The
  platform table's other implications are declared here as planned rules,
  restricted like the F2 rule to deciding 0s. The eligible cells are the
  entries the instrument v2.1 table fixes at 0 (for a supplement-only
  deposit, F3, F4, and A2), and each candidate rule's scope, the cells it
  decides and the registry fields it reads, is frozen in writing before its
  adoption check. Rung (i) evidence keeps precedence over a table entry, as
  the instrument states. A row's floors, which award credit, stay with the
  model, and disagreements are flagged. A planned rule is adopted only if,
  before census scoring, the pilot items it decides form a non-empty set,
  it matches the E8-v2 reference on every one of them, the branches those
  items exercise are recorded, and the hybrid scorer still clears both
  gates. A branch no pilot item exercises stays flag-only until it is
  validated separately, and the F2 rule's all-zero validation is not
  evidence for any other rule. A rule that does not validate stays
  flag-only, and that outcome is reported. [D-2, ruled]
- **Reporting.** Model–rule disagreement rates are reported as a study
  finding.

*(c) Evidence checks flag; they never override.* Quote verification against
the paper's text, and an identifier check, send an item for re-scoring or
adjudication. They never set a score. The identifier check has two
classes. An identifier that a payload or the registry asserts as cited
must appear verbatim in the paper or its supplement. A derived identifier,
namely a version selected under §4 item 5 or a record recovered under
amendment 2 §2, need not appear in the paper. The registry instead records
its provenance class, its cited parent identifier, the authoritative
relation or recorded recovery query that led to it, and the retrieval
evidence, and a recovery keeps its citation-defect flag. An identifier of
either class that lacks its evidence fails the check.

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
evidence strings for those deposits state expressly that the pack did not
show, or did not let the model verify, the description or keyword fields
(one further string says only that the fields' richness was not
evidenced, and is not counted). The gates have therefore not yet tested
the scorer on the inputs the census will give it.

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
The BI-excluded figure is reported alongside. [D-3, ruled] If the
stability gate fails, the registered remediation ladder applies as lodged
(amendment 1 §2, carried forward by amendment 2 §4). At most one routing
fix is made, to content delivery only and never to instrument text,
followed by one re-run of the 15 scorings with both gates recomputed. If
stability is still below 0.90, the census is scored by majority vote of
three runs, with no further iteration. No other change is made or
re-tested. If the concordance gate fails, on the re-run or without a
stability failure, the ladder does not apply, because concordance already
uses majority vote. Census scoring does not begin, and any route past the
failure is lodged as a further amendment before it does. This ladder
governs FAIR scoring
only and never waives the §8 regression gate (§9). Both gate results,
before and after any fix, the F2 model–rule disagreement rate, and the
scores on the nine BI items are reported with the study results.

*(d) Boundaries.* The E8-v2 reference is unchanged and remains unblinded
(amendment 2 §3). For the pilots, the registry's principal-artefact and
version curation was taken from the adjudication, so the re-validation does
not measure curation error. For census papers, the curation procedure (who
curates the registry's curation fields, from which sources, and how the
curation is checked) is lodged in a further amendment before census scoring
begins [D-4, ruled]. Three constraints bind it now:

- curation fields are never copied into evidence packs;
- every identifier the registry records as cited appears verbatim in the
  paper or its supplement before harvest, and every derived identifier
  carries its cited parent and provenance (§5(c));
- a human audit checks the curation, with its sample and its agreement
  threshold declared before any census curation starts.

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
  - **Supplied pins take precedence [D-7].** "The authors' environment
    specification is built as supplied, as the preparation procedure
    already does, so a lockfile is restored, a container specification is
    built, and an explicit runtime or package version is used. Whether a
    component is specified is judged per dependency, not per project,
    because a container image can pin the runtime and a package snapshot
    date without naming each package. The date-based search below governs
    only what the specification leaves unspecified, and a specified
    component whose build fails. Each such fallback is logged against the
    component. The run reports, beside the verdict (§8(a)), whether the
    pins were honoured in full, with how many fallbacks, or not at all."
    Supplied pins keep precedence so that registered H3, which compares
    build effort between pinned and unpinned environments, measures the
    authors' pins and not a reconstructed environment.
  - **Version-search cap [D-7].** "An unspecified dependency is first
    built at the release current at the article's first online appearance.
    If a specific dependency fails to build, at most its immediately
    preceding and following releases are tried, so a dependency has at
    most three attempts. A specified dependency that failed counts its
    pinned version as the first of its three. Where a repository publishes
    commits but no releases, the release current at publication is the
    last commit on the default branch at or before first online
    appearance, and the adjacent attempts are the nearest earlier and
    later commits that change the package's declared version, or, where
    none does, that change the package's files. The cap governs build
    failures only. A deprecated function is handled by a separate logged
    search backwards to the last public release that still carries it,
    without this cap. Each attempt is logged."
  - **Wrapper boundary cases.** "Mechanics are applied in wrappers only,
    never in the authors' files. They are recorded, and they include:
    setting a random seed where the authors set none (stochastic tolerances
    still apply); converting an input file's format, allowed only when a
    mechanical check confirms every value is unchanged (any change of value
    is fail-and-uplift); and choosing the language runtime version, which
    is routine like any dependency."
  - **Mechanics placed in an authors' file (RULED 2026-10-05).** "A
    mechanical change made inside an authors' file rather than in a wrapper,
    such as a changed input path, breaks the wrapper rule even when it
    changes nothing computed. A result that rests on such a file does not
    count toward coverage or the verdict until it is re-run with the
    mechanics moved into a wrapper and the authors' file restored
    byte-identical. A change of logic, indices, data selection, parameters,
    or functions called remains fail-and-uplift whatever its effect,
    including a restructuring that gives the same result."
  - **Further boundary cases (RULED 2026-10-05, executed-code audit Q6).**
    "A wrapper may make an authors' statement error-tolerant only where the
    statement computes nothing that enters a result, such as registering a
    font; the tolerance is declared, and the run log records whether it
    fired. Per-section error capture is routine, but a target is credited
    only from a section that completed without error and whose inputs come
    only from sections that also completed. Sections may run in another
    order only when they are independent, none reading an object another
    defines; otherwise re-ordering changes the execution logic and is
    fail-and-uplift. A dependency fetched from a public repository is
    installed when the environment is built, pinned to a tagged release or,
    where the repository has none, to a recorded commit, preferring the one
    current at publication. An unpinned install at run time is not
    routine." Independence between sections is judged on every state a
    section can pass to another, namely named objects, files written and
    read, global options, and random-number state. The dependency sentence
    is read with the precedence rule above, so where the authors pinned the
    dependency, their pin is used.
  - **Verification aids and reconstructed inputs (RULED 2026-10-06,
    executed-code audit Q5).** "Where no authors' code produces a published
    result, the reproducer may test it with a labelled verification aid: a
    read-only lookup in the deposited data, or a call to a documented
    function of the package the authors used, making no new statistical
    choice. A formula the reproducer infers from the paper's wording
    qualifies only where it reproduces the paper's own printed values from
    the paper's own printed inputs, and it is credited only where its
    inputs come from executing the authors' code. A result resting on
    inputs the reproducer reconstructed, for example from upstream datasets
    the authors cite, never counts toward coverage or the verdict: the
    target stays in the denominator as expected-untestable, and the
    reconstructed result is reported as uplift evidence." A printed value
    that the formula does not reproduce is never credited and goes to the
    paper-error protocol of §7(a), as the ruling directs for its two
    inconsistent cells.

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

### 9. Deviation: the §8 regression gate's baseline (correction ledger)

The registered gate (§8 of the registration) requires a new pipeline to give
identical verdicts and identical value-level results when it re-runs at least
two pilot papers. An audit of the pilots' executed code (2026-10-04) found
that this baseline is not what the gate assumes. In three pilots (dye,
herskind, and key) the first reproduction executed a reproducer's
re-implementation rather than the authors' files. Two pilots (crema and
marwick) executed a version other than the one §4 item 5 selects, and
crema's Table 1 was credited against that other version's own re-run.
For example, the paper's Japan r is 0.1023, against 0.1003 in the pilot
comparison report's "published" column. Matching those results exactly
would reward a new pipeline for reproducing the pilots' errors.

- **The pilot artefacts are preserved unchanged.**
- **A separate, versioned correction ledger** records the registrant's
  ruling for each affected verification target: the admissible source
  version (§4 item 5), the published value, the tolerance, the repair status
  (§7(d)), and the coverage treatment. The ledger is committed and hashed
  before the regression run, and it does not change during the run.
- **The gate is reported twice.** The registered strict comparison against
  the original pilot artefacts is reported as registered, including the
  Crema archived-posterior leg. The amended comparison is against the frozen
  ledger, and it is the pass criterion.
- **A corrected result is never relabelled.** Where a corrected result
  differs from an erroneous pilot value, it is reported as a correction, not
  as an unchanged pass, and the pipeline is never adjusted to reproduce a
  pilot error.

Conditions on the ledger (drafted 2026-10-05 from the Fable review of PR #7;
registrant's direction to draft them):

- **Ledger values come from the paper and the selected deposit only.** Each
  expected value cites the paper or, with the §7(a) evidence tier named,
  the selected deposit. No value comes from any output of the pipeline
  under test. The shakedown re-runs of dye and herskind (attempt-02)
  finished before the ledger was ruled, so their results were known when it
  was written. They serve only as evidence that the authors' unmodified
  code yields a value.
- **Per-target fields:**
  - the source version, and the deposit file checksum that the lane's
    provenance check must match;
  - the paper's printed value, as printed, and the tolerance category from
    the pilot plan;
  - where the printed value is corrected, the corrected expected value,
    its evidence tier, and the ruling that corrects it, kept beside the
    printed value, which is never overwritten;
  - the pilot's recorded value and outcome, so that each correction is an
    explicit difference;
  - the repair status and class under §7(d);
  - credit eligibility, recorded separately from the class;
  - the coverage treatment, including whether the target is
    expected-untestable (§7(d)) and whether its comparison is exact or
    within tolerance.
- **Per-paper fields.** The expected verdict is derived by applying the
  verdict rules to the ledger rather than copied from the pilot. The
  pilot's locked target list is executed as planned, so the denominator is
  preserved by construction. A target whose scope changes is identified
  separately from a corrected value.
- **The ledger is frozen in the launch commit.** It is committed at a
  registered path before the run, its sha256 is recorded in the run
  configuration, and the run's launch commit contains it. If the
  registrant concludes after the run that the ledger was wrong, the
  correction is a dated ledger amendment followed by a re-run, never a
  re-reading of the result.
- **The amended pass predicate [D-9].** On each regression paper, the gate
  passes only if all of these hold. Every unchanged deterministic target
  gives the pilot's outcome and value, equal at the precision the pilot's
  comparison table recorded, after the same rounding. Every unchanged
  stochastic target gives the pilot's outcome, with a value within the
  pre-stated tolerance of the printed value rather than equal to the
  pilot's sampled value. The Crema archived-posterior leg is deterministic
  and compares exactly. Every corrected target gives the ledger's expected
  outcome, with a value within the pilot plan's tolerance category of the
  expected value. A changed tolerance is itself a ledger correction with
  a stated reason, and no tolerance is widened to make a corrected target
  pass. A target with several values passes only when every value passes
  (§7(c)). Every expected-untestable target comes out expected-untestable.
  One the new pipeline can test is reported as an explained difference
  for a ruling, not as a failure. The paper's verdict equals the ledger's
  expected verdict.
- **Two target sets, both counted.** Targets are split into those the ledger
  leaves unchanged and those it corrects. The strict comparison fails by
  construction on corrected targets, so a failure there is not a
  regression. The regression signal is the unchanged set, and its size is
  reported for each paper. The two gate papers are chosen by the size of
  their unchanged sets, because the audit's Q1 ruling leaves some pilots
  with few unchanged targets. A paper whose unchanged set is empty gives
  no regression signal, and that is reported.
- **Crema's archived-posterior leg runs from the posteriors of v1.0.0**, the
  version §4 item 5 selects, held in the corpus store.
- **Code integrity is part of the pass criterion.** On each regression
  paper, the §8 verdict is computed only when both of these hold. First,
  the reproduction lane's code-integrity gate records no hard failure,
  meaning that the authors' code is byte-identical to its independently
  anchored original,
  the run record and receipt chain verify, the execution evidence is
  complete, and no prohibited repair ran. A hard failure is never waived by
  a ruling. Second, every remaining admissibility issue the gate raises
  carries a recorded registrant ruling. A repaired result never counts,
  and a result resting on an authors' file edited for mechanics counts
  only after the wrapper-only re-run of §7(d).

### 10. Order of operations

1. The registrant lodges this amendment on OSF as a versioned registration
   update.
2. The frozen instruments are edited to the §4 and §7 text and given new
   version numbers, with content-integrity hashes registered.
3. The registrant rules the correction ledger (§9), and it is frozen.
4. The §8 regression gate runs on the selected configuration under the
   clarified text, reported against both baselines (§9).
5. The census-input re-validation (§6) runs on the selected configuration.
6. Census scoring begins only after the §8 gate passes and the
   re-validation clears both gates, or after the §6(c) ladder resolves a
   stability failure. A concordance failure stops census scoring, and a §8
   failure stops the reproduction lane, until a further amendment is
   lodged. Neither the ladder nor a ruling waives either gate.

**Evidence locations.** Every path in this amendment is in the study
repository, <https://github.com/saross/llm-reproducibility>, at the tagged
lodgement commit (`osf-amendment-3-<date>`). They include the frozen pilot
reference and its beyond-instrument tags
(`studies/open-science-compliance/outputs/validation/e8-v2-rederivation/worksheet.json`),
the selected-arm results (§2), the F2 rule report (§5), the executed-code
audit and its rulings (§9), and, once ruled, the correction ledger at the
path the launch commit's run configuration records.

---

## Decisions for the registrant before lodgement

- **D-1. Instrument clarifications in this amendment.** Running-list item 2
  left open whether the E8-v2 clarifications lodge here or as a gated edit.
  The draft lodges them (§4), since the instrument is frozen and the census
  re-validation (§6) runs on the clarified text. The version number v2.2,
  and a matching guide bump, are proposed.
  **RULED (Shawn, 2026-10-05): lodge here,** as instrument v2.2 with a
  matching guide bump, so the registered text matches what the census
  scores.
- **D-2. Platform-row rules beyond F2.** Item 6(b) named "platform-row
  rules" alongside F2. Only F2 is built and validated, so the draft keeps
  the rest flag-only. Alternative: declare them as planned rules with the
  same two validation criteria.
  **RULED (Shawn, 2026-10-05): planned rules, restricted to 0s.** They are
  pre-declared with F2's two validation criteria and, like the F2 rule,
  decide only failures; floors stay with the model and disagreements are
  flagged. Avoids adopting a rule after census data exist. §5(b) redrafted
  to match.
- **D-3. The re-validation's gate statistic.** The draft uses all 150 items,
  because the re-validation removes most of the reasons for the BI
  exclusion (one, marwick's lockfile contents, remains).
  Alternative: keep the BI-excluded statistic as in §3(b). For context, the
  hybrid at `medium` already scores 139/150 = 0.927 on the old inputs.
  **RULED (Shawn, 2026-10-05): all 150 items,** with the BI-excluded figure
  reported alongside, as drafted. The re-validation supplies the inputs
  whose absence motivated the exclusion; the one item still resting on
  content outside the inputs (marwick code I3) costs at most 1/150.
- **D-4. Census registry curation.** The F2 rule and version selection read
  curated fields (`role`, `home`, `carries`, `scored_version`,
  `unpublished_principal`). For the pilots these came from adjudication.
  The census needs a stated procedure (who curates, from which sources, and
  how curation is checked) before §6(d) can be completed.
  **RULED (Shawn, 2026-10-05): defer the procedure to a further amendment,
  lodged before census scoring,** with three constraints fixed now in
  §6(d): curation fields never enter packs; identifiers are checked
  verbatim against the paper or supplement (refined after Astra's review:
  cited identifiers verbatim, derived identifiers by provenance, §5(c));
  and a human audit, with its sample and agreement threshold declared
  before census curation starts.
  Neither the §8 regression gate nor the §6 re-validation needs census
  curation, so this does not block lodging amendment 3.
- **D-5. Correction to Entry 5's proposed wording.** Entry 5 said the BI
  items rest on "the papers' supplementary files". The worksheet's notes
  show that holds for the four dye items only; the other five (crema data
  I1 and I3, herskind data I1, marwick data I1 and code I3) rest on deposit
  content the packs never recorded. §3(b) is corrected accordingly. Those
  five were not deliberately withheld, which the BI `input` definition
  ("deliberately not given") does not quite cover.
  **RULED (Shawn, 2026-10-05): lodge the corrected §3(b) wording, and widen
  the `input` definition** to "evidence the spawns were not given:
  supplementary files deliberately withheld, or deposit content the packs
  did not record". The adjudication log and worksheet carry the clarified
  definition with a dated note that the tagged set is unchanged, and
  erratum Entry 5 carries a correction pointer.
- **D-6. The regression gate's baseline.** The executed-code audit (PR #7,
  `outputs/validation/executed-code-audit-2026-10-04/findings.json`) found
  that three pilot attempt-01s (dye, herskind, and key) executed no
  authors' file, and two (crema and marwick) executed a version other than
  the AP-12 one. Crema's Table 1 credit compares v2.0.0's re-run with itself:
  the paper's Japan r is 0.1023, against 0.1003 in the comparison report's
  "published" column. The §8 gate requires identical verdicts and values
  against the pilot artefacts, so its baseline may need re-basing, and a
  re-basing may need declaring here. This depends on the audit's questions
  Q1–Q5.
  **RULED (Shawn, 2026-10-05): adopt the correction-ledger approach** that
  Astra (GPT, Codex) proposed in its PR #7 review, now drafted as §9. The
  ledger's per-target contents are still to be ruled, from the audit's Q1–Q5.
  **The audit's questions Q1–Q10 are RULED (2026-10-05 and 06;
  `question_rulings` in the audit's `findings.json`, PR #7).** The ledger is
  to be drafted from them, and the general principles of Q5 and Q6 are added to
  §7(d).
  §9's ledger conditions were drafted on 2026-10-05 from the Fable review, at
  the registrant's direction. The class (ii) consequence is RULED
  (2026-10-05, §7(d)): a result resting on an authors' file edited for
  mechanics counts only after a wrapper-only re-run. That answers the
  audit's Q1 for dye's 22 attempt-02 targets: they need re-running before
  they count.
- **D-7. Precedence between supplied pins and the date-based search
  (Astra, blocking 4).** §7(d)'s cap text repeated the shakedown ruling,
  under which every dependency is first built at the publication-date
  release. The preparation procedure restores the authors' lockfile and
  builds their container, and registered H3 compares build effort between
  pinned and unpinned environments. Options: (a) supplied pins take
  precedence, judged per dependency, and the date rule governs only what
  the specification leaves open and a pin whose build fails, with the
  fallback logged and reported beside the verdict; (b) a standardised
  publication-date environment replaces supplied pins, declared as a
  change with its H3 consequence stated. The draft takes (a), with a
  commits-without-releases rule and a separate deprecation search (Fable's
  refinements, 2026-10-06). **PROPOSED (a); awaiting the registrant.**
- **D-8. Human validation independence (Astra, blocking 6).** The
  registrant confirms F2 = 1 candidates and is also the §8 hand-scorer.
  Options: (a) draw the subsample and hand-score before any confirmation on
  those papers, blind the hand-scorer to the rule's outputs too, validate
  against the raw model majority, and report F2 in three parts with the
  confirmed 1s unvalidated; (b) a second rater confirms the twelve papers'
  F2 candidates, the only route to an independent confirmation; (c)
  declare the limitation only. The draft takes (a); (b) can be added if a
  colleague is available. **PROPOSED (a); awaiting the registrant.**
- **D-9. The ledger's pass predicate (Astra, should-fix 4).** §9 named the
  fields but not the predicate. The draft states one: exact at recorded
  precision for unchanged deterministic targets, within tolerance for
  stochastic and corrected targets, every value of a multi-value target,
  expected-untestable preserved, the verdict a paper-level field, the
  printed value kept beside any correction, and the two gate papers chosen
  by unchanged-set size. Dye carries little regression signal on either
  baseline: attempt-02's unchanged set is the three verification-aid
  targets (T01, T33, and T34; `attempt-02/comparisons/comparison-report.md`
  lines 297, 299, 332, and 509, of 25 credited targets in its
  `comparison.json`), and attempt-01's depends on the ledger's ruling on
  its re-assembled wrapper (DYE1-2). Herskind's attempt-01 credits 291
  n-gram values matched against S3.xlsx (its `comparison-report.md` line
  5 and lines 59–63). Anchors from Fable, re-verified 2026-10-06.
  **PROPOSED; awaiting the registrant.**

## Pre-lodgement checklist

- [X] Registrant reads and edits the full draft; decisions D-1 to D-6 ruled
      (2026-10-06).
- [ ] Astra's review (2026-10-06) folded in; D-7 to D-9 ruled; the ruling
      dates of audit Q5 and Q6 reconciled with `findings.json`.
- [x] 2026-10-06 Consistency check (maintenance rule 4): §4 and §7 text
      against the adjudication log and the shakedown rulings; §5 and §6
      against the planning note, the F2 report, and `manifest.yaml`;
      deliberate differences recorded in the revision record below.
      Re-read after D-7 to D-9 are ruled.
- [x] 2026-10-06 Token classes verified: numbers and statistics;
      identifiers (DOIs, versions, model identifiers, dates); registered
      vocabulary; quoted strings (revision record). One open item: the
      ruling dates of audit Q5 and Q6.
- [x] 2026-10-06 Register exit checks run on the lodged portion and
      recorded (revision record).
- [ ] D5 manifest-consistency gate PASS and full test suite green at the
      lodgement commit; repository tagged `osf-amendment-3-<date>`. Run on
      the revised working tree 2026-10-06: gate PASS (81/81), 387 tests
      passed. Re-run at the lodgement commit.
- [x] 2026-10-06 (provisional) Paste artefact `osf-amendment-3.txt`
      produced from the lodged portion and unwrapped with
      `unwrap-paste-file.py`; flowing lines, no tables; word, bullet, and
      numbered-line counts unchanged by unwrapping. Regenerate at lodgement
      with the banner date set and the [D-n] markers resolved.
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
| §9 | `outputs/validation/executed-code-audit-2026-10-04/` (PR #7); Astra's PR #7 review, 2026-10-05; registration §8 |

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

## Revision record (2026-10-06)

**Inputs.** The registrant's read (checklist step 1 ticked, no text edits),
and Astra's review of `38b59b0`
(`~/agent-mail/codex/outbox/claude/20261006T073349Z-codex-repro-amendment3-review.md`,
with its checking artefacts beside it). Every premise in the review was
re-verified at source before any edit; all held. Fable gave a second
opinion on D-7 to D-9 by SendMessage (session `llm-reproducibility-ea`,
2026-10-06); its refinements are taken where verified and named in the
decisions.

**Disposition of the review's findings.**

- **Blocking 1, bounded ladder and concordance failure.** §6(c) restated
  from amendment 1 §2 and amendment 2 §4; concordance failure is a stop; §10
  step 6.
- **Blocking 2, inaccessible versus absent evidence.** §4 item 6 limited to
  datasets deposited nowhere, access-controlled case scored on its record;
  §4 item 12 and §5(b) carry "no metadata record".
- **Blocking 3, derived identifiers.** §1, §5(c), and §6(d): cited
  identifiers verbatim, derived identifiers by provenance.
- **Blocking 4, pin precedence.** §7(d) new precedence rule and restated
  cap; D-7.
- **Blocking 5, integrity failures not rulable.** §9 code-integrity
  condition separates hard failures from ruled issues.
- **Blocking 6, validation independence.** §5(b) confirm-1 procedure; D-8.
- **Should-fix 1, chronology.** §2 scopes "before any data" to the Opus 5.5
  arms; §3(b) gives both tagging dates with commits; Q5/Q6 dates left for
  the registrant (below).
- **Should-fix 2, cost as estimates.** §2 "Rule applied" rewritten; billing
  route stated.
- **Should-fix 3, version-selection consequences.** §4 item 5: reproduction
  route, unavailable versus failed, date check, more than two candidates,
  primary value.
- **Should-fix 4, ledger comparison.** §9 fields split, per-paper fields,
  pass predicate; D-9.
- **Should-fix 5, planned-rule scope.** §5(b) planned rules: eligible cells,
  frozen scope, non-empty pilot set, branch recording.
- **Optional 1, permanent links.** "Evidence locations" paragraph after §10.
- **Optional 2, section independence and inferred formulae.** Sentences
  after the Q6 and Q5 quotes in §7(d).

**Consistency check (maintenance rule 4), deliberate differences
introduced by this revision.** Line references are to the files at
`60ec56d` unless stated.

1. §4 item 6 narrows AP-13's "unpublished or closed" to datasets
   deposited nowhere, on AP-13's own reasoning that such data have no
   identifier, protocol, mechanism, or licence (`adjudication-log.md`
   lines 232–245), and states the access-controlled case from amendment
   2 §1 item 4 and registration §7.1. Instrument v2.2 is to follow this
   wording.
2. §4 item 5 adds AP-12 refined's reproduction route (`adjudication-log.md`
   lines 202–221), with the recovery's results as uplift under §7(d).
   The unavailable-versus-failed distinction, the date check's
   definition, the more-than-two case, and the earliest-released primary
   value are drafting choices for the registrant's confirmation.
3. §4 item 12 takes "no metadata record of its own" from the registry's
   `home` definition (`corpus/evidence-packs/declared-links.yaml` lines
   37–40) and the F2 report (`f2-rule-hybrid-2026-10-04/report.md` line
   21), and adds F2 to the typical failures.
4. §5(b)'s confirmation procedure (D-8) is new. The F2 report (lines 25–27)
   and the planning note (`deterministic-output-checks.md` lines 188–192)
   describe the confirmation only.
5. §5(b)'s planned-rule conditions (frozen scope, non-empty pilot set,
   branch recording) are new; D-2's substance is unchanged. "Rung (i)
   evidence keeps precedence" is `fair-instrument.md` lines 106–115.
6. §5(c)'s two identifier classes are new. The registry's marwick-2025
   entries (`declared-links.yaml` lines 147–171) are the derived case:
   the scored version `10.5281/zenodo.15603267` is not printed in the
   paper.
7. §6(c) restates the ladder from amendment 1 §2 (lines 109–118) and
   amendment 2 §4 (lines 244–258). The concordance-failure stop is new.
8. §7(d)'s precedence rule and restated cap (D-7) change the shakedown
   ruling's cap sentence (`phase2-shakedown/results-2026-10-03.md` lines
   347–350). The preparation prompt's existing practice is
   `reproduction-system/prompts/01-preparation.md` §2.1 and §2.3.
9. The sentences after the Q6 and Q5 quotes in §7(d) are outside the
   ruled text. Q5's record (`findings.json`, PR #7) sends the two
   inconsistent cells to the paper-error protocol.
10. §9's per-target fields, per-paper fields, pass predicate (D-9), ledger
    amendment guard, and gate-paper choice are new. The registered gate
    text is registration §8 (`osf-registration-summary.txt` line 134).
11. §9's code-integrity condition follows the gate 1.3 specification's
    hard-failure list (`wiki/planning/reproduction-gate-1-3-design.md`
    lines 552–555 on PR #7).
12. §10 step 6 and the evidence-locations paragraph are new.
13. `manifest.yaml`: `fair-instrument` is v2.1 (line 408), to become v2.2
    at §10 step 2; the four reproduction instruments are at 1.0
    (`pipeline-invariants` at lines 470–472) and need new versions and
    hashes at the same step.

**Token checks on this revision's specifics.** Worksheet commits `7298681`
(2026-10-02, 5 tags), `6c0c2ec`, `8905c6c`, `7da90bf` (2026-10-03, 9 tags),
concordance `6e0d17a` (2026-10-03 22:14), from `git log` and `jq` on
`worksheet.json` at each commit. Costs $8.70, $9.25, $9.37, $9.55, $17.27
from `opus-5-5-arms-2026-10/selection-cost.json`; `billing_route:
max-plan` from the three arms' `run-record.json`. The 20-of-90 count's
inclusion rule from the F2 report (lines 84–88) and Astra's
`missing_field_review` (20 selected; index 57 the broader string).
Amendment 2 §1 item 4 (A1.2 no-restriction case), registration §7.1
(ethical and legal exception) and §8 (12-paper subsample, blinded), H3
(pinned versus unpinned), all re-read in `osf-registration-summary.txt`
and `amendment-2-draft.md`. Hard-failure list from the gate 1.3
specification §6. Q5 ruling text from `findings.json` (PR #7).
Repository URL from `git remote`.

**Open for the registrant before lodgement.** (a) D-7, D-8, and D-9.
(b) The ruling dates of audit Q5 and Q6: `findings.json` records every
question as ruled 2026-10-05, its commit `c4553f9` is dated 2026-10-06
08:56 +1100, the continuity log places the walk-through on 2026-10-06,
and the draft labels Q6 2026-10-05 and Q5 2026-10-06. The registrant
confirms the date; the draft and `findings.json` are then made to agree.
(c) The `[D-n]` markers are resolved and stripped from the paste artefact,
and its banner date set, at lodgement.

**Register exit checks (lodged portion, 6,037 words; academic register
gate, `register-gate.py` advisories read item by item).**

- Em-dashes: 0. The gate's 0.52 per thousand is en dashes in ranges.
- Semicolons: 22, of which 12 end list items, 7 are in the §7 ruling text
  quoted unchanged, and 3 are sentential in revised prose (about 0.5 per
  thousand against the 3.4 draft target).
- Announcement colons: 1.56 per thousand, against the 1.6 ceiling (2.09
  before the register pass). Colon-led lists of three or more: 2, both in
  text the registrant had already read (§7(a)'s evidence tiers and §9's
  ledger ruling list).
- Boosters, "whilst", "important to note", and "not X but Y": 0. "The
  authors" refers only to the studied papers' authors.
- Hedges: 0.12 per hundred words (may 4, could 2, typically 1), under the
  0.72 academic target; registered text hedges where it should.
- Consecutive short sentences: the one flag is a list-number artefact.
- Mean sentence length 20.5 words.
- markdownlint: the only findings are the pre-existing Sources table
  (MD013, MD060), outside the lodged portion.
