# OSF amendment 2 — LODGED 2026-08-17

**Status: LODGED 2026-08-17.** Filed via the OSF API as a versioned
registration update (SchemaResponse revision `6a824828f323f5c6ead66c4b`,
created, populated, submitted, and approved the same day on the
registrant's proceed instruction): the amendment text was appended to the
registration's Summary field under a dated banner, following the
amendment-1 placement precedent. DOI unchanged — 10.17605/OSF.IO/DQNHG.
Round-trip verification (authenticated at patch time, anonymous after
approval): stored text equals the sent text under the registry's known
write transform (literal comparators stored as HTML entities, decoded
correctly by the renderer); the original registration + amendment 1 body
is byte-identical; `updated_response_keys` exactly `["summary"]`. Public
page render-checked: AMENDMENT 2 banner visible, zero entity artefacts,
§6's quoted comparators display correctly. Repository state at lodgement
tagged `osf-amendment-2-2026-08-17` (commit `9f7343e`). Amendment
version URL:
<https://osf.io/dqnhg?revisionId=6a824828f323f5c6ead66c4b>.
Paste artefact: `osf-amendment-2.txt` (this directory). **The D3
re-benchmark is now unblocked** (lodgement was its hard stop).

**Drafting-period note (superseded by lodgement).** Consolidated at plan
D1 (2026-08-15) from erratum-log Entry 3's ratified scope
(RATIFIED 2026-08-14), the registrant's 2026-08-10/11 scoring-policy rulings,
and the 2026-08-15 rulings (Phase B shape; platform-table corrections;
operative-default and infrastructure-layer principles). Lodgement (plan D2)
follows the proven amendment-1 route — OSF API, versioned registration
update, DOI unchanged (10.17605/OSF.IO/DQNHG) — and is a **hard stop before
the D3 re-benchmark**: no scoring spawn receives an evidence pack or the
clarified instrument's scores before this amendment lodges. The repository
implementation landed ahead of lodgement on branch
`feat/d1-amendment-2-window` (instrument v2.1; guide v1.1 promoted
pull→push; agent definitions v1.1; C7 registry hashes), which is compliant
because no affected analysis runs before lodgement (amendment-1 precedent:
text describes changes already present in the repository at lodgement time).

**Why this amendment.** The 2026-08-03 validation benchmark (amendment 1 §3)
put all three arms below both 0.90 gates — stability 0.807/0.873/0.813,
concordance 0.773/0.807/0.820 — with disagreement item-structured and shared
across arms (A1.2, R1.1, A2, R1.3, F-block target question). The registrant
declined the single permitted routing-fix attempt as then framed and chose
instrument clarification (2026-08-03): the A1 mining pass reduced 68 of 150
disputed items to three root causes (undefined assessment target; undefined
evidence basis under paper-only scoring; semantic gaps in A1.2 and R1.3),
all addressed below. This is evidence about the instrument, and the
clarifications are lodged transparently before any re-validation or census
scoring.

---

## Amendment text (draft for the OSF field)

### 1. Instrument clarifications (FAIR instrument v2.0 → v2.1)

The canonical instrument gains the following operative sections (ratified
erratum-log Entry 3, items 1–7 and 9; full text in the canonical file,
mirrored verbatim in the Pass 6 prompt and hash-registered):

1. **Research-surface rule.** The unit of assessment is the paper's
   research surface: the complete set of digital artefacts — data, code,
   and other digital inputs — required to reproduce the paper's reported
   results, as reachable from the published paper. Each FAIR sub-principle
   scores the empirical status of those artefacts; creator identity,
   depositor identity, and responsibility for closure never affect scores.
   A precisely cited, well-archived third-party input earns full credit; a
   closed or unpublished input is penalised even where closure is beyond
   the authors' control. Provenance (author-deposited / third-party /
   undeterminable) is recorded per required input as non-scoring metadata.
   Rationale cites the verified precedent set (RDA FDMM v1.00,
   10.15497/rda00050; JIE Data Openness Badges secondary-data rule,
   10.1111/jiec.12738; CODECHECK; Colavizza et al. 2020; Culina et al.
   2020; Tedersoo et al. 2021; Marwick 2017); ACM Artifact Review and
   Badging v1.1 ("Author-created artifacts…") is the named deliberate
   departure — the study measures the credibility of published results,
   not author compliance.
2. **Aggregation rule (initial, explicitly iterable).** Within each
   artefact type, sub-principles score the principal artefact(s) — those
   whose absence would block reproduction. Conjunctive scoring for data;
   the paper's own analysis scripts are always principal for code;
   third-party dependencies enter only through citation quality (I3) and
   the evidence pack. Alternatives recorded for iteration:
   majority-over-principals; proportion-weighted.
3. **Evidence-admissibility ladder + platform entitlement table.**
   Two rungs: (i) direct evidence — the paper's text and the verified
   per-paper evidence pack (§2 below); (ii) by-construction inference from
   a closed, instrument-listed platform table, applicable only where rung
   (i) is silent. Entitlements are floors, not ceilings. The registered
   unscoreable→0 default applies only after the ladder is exhausted. The
   table's rows were verified at the granting services on 2026-08-15
   (dated verification note + registry enrichment committed under
   `outputs/validation/platform-rows-2026-08-15/`), and the v2.1 table
   incorporates the corrections that verification forced:
   - DataCite row: the DOI string is undeletable and Handle-resolvable,
     but public metadata accessibility is NOT guaranteed post-withdrawal
     (DataCite's own retraction workflow contradicts the tombstone limb);
     mandatory metadata is null-code-satisfiable; DataCite mandates no
     licence property.
   - Zenodo row: the licence-field guarantee is scoped to open-access
     records; verified persistence entitlements added (tombstone page,
     DOI retained, metadata always accessible — platform policy
     assertions, third-party-unaudited); default-licence footnote (82.6%
     of sampled records carry the pre-filled CC-BY-4.0 default). A
     default-valued licence is fully operative — the instrument assesses
     the research surface, not intent; default-domination is interpretive
     context, never a score modifier.
   - CRAN row: strongest metadata floor in the table, licence field with
     no default value; but no persistent identifier, and archival is a
     norm, not a guarantee.
   - Accredited-repositories row GRADED (not a uniform floor): ADS —
     ingest-enforced domain standard, R1.3 = 1 by construction,
     CoreTrustSeal-certified to 2027-02-12; DANS Data Station Archaeology
     — generic mandatory core only, domain block optional, R1.3 requires
     rung-(i) evidence, certified to 2028-02-27; tDAR — no external
     standard named, preservation policy unverifiable, CoreTrustSeal
     lapsed 2025-12-16 (renewal at First Submit), R1.3 requires rung-(i)
     evidence. Certification is a presence-floor credential informing
     by-construction weight, never a scoring input.
   - GitHub/GitLab row split: GitHub licence detection may return
     NOASSERTION; GitLab exposes no SPDX identifier and licence data is
     opt-in. No persistence entitlement on either.
   - Publisher-supplement row: article-record persistence is a Crossref
     member obligation plus retention right under "commercially
     reasonable efforts", not a warranty; F2 = F3 = F4 = 0 and A2 = 0 for
     supplement-only deposits; independently deposited supplements score
     as platform deposits, never under this row.
   The table is extensible by dated amendment or, pre-census, by gated
   instrument edit (Dataverse, Australian Data Archive, Figshare, Dryad
   flagged). Adopted evaluation principle (registrant, 2026-08-15, from
   eResearch practice): platforms are evaluated once at the
   infrastructure layer — where every lodged artefact inherits the
   platform's characteristics — with artefact-level investigation
   reserved for facts the infrastructure leaves open; rows carry dated
   CoreTrustSeal and re3data evidence, and entitlements are always
   verified at the granting service, never taken from aggregators.
4. **A1.2 no-restriction case.** A fully open resource requiring no
   authentication satisfies A1.2 — the protocol supports authentication
   where needed, and none is needed. Score 0 only where access control
   exists or is warranted but the mechanism is undocumented or
   unjustified.
5. **F-block identifier granularity.** F1 credits the artefact's own PID,
   or the article DOI where the artefact is distributed as that article's
   supplement — a declared departure from the strict object-PID reading
   (cf. F-UJI). F2/F3/F4 remain strictly artefact-level, so
   supplement-only deposit yields F subtotals of 4/4 (own-PID), 1/4
   (supplement under the article DOI), 0/4 (unpublished).
6. **R1.1 licence semantics.** Per-artefact scoring; the most-restrictive
   default applies only to same-artefact disagreements (publisher-hosted
   supplements default to the article's licence absent a separate one;
   paper-vs-service assertions resolve to the more restrictive). Where
   the paper is silent, third-party-hosted artefacts score on the licence
   recorded at the service via the evidence pack; a platform's mandatory
   licence field does not itself satisfy R1.1.
7. **R1.3 qualifying standards.** Deposit-level standards only — generic
   schemas, domain schemas and vocabularies, or deposit in an accredited
   domain repository whose ingest enforces its metadata standard (graded
   per the platform table); for code, package structure, CITATION.cff,
   CodeMeta, or community review. Methodological standards (IntCal20,
   OxCal) do not qualify.

### 2. Evidence pack and read-scope re-specification (supersedes amendment 1 §4)

Scoring spawns receive: the paper source, the pushed instruments, and a
per-paper verified evidence pack produced by a deterministic
artefact-metadata harvester that resolves the paper's declared artefact
links via enumerated endpoints (DataCite, Crossref, Zenodo, GitHub, GitLab,
OSF; CRAN and Dryad flagged as early additions; extensible) into licence
fields, metadata records, and conflict flags. Every pack record carries a
retrieval timestamp and response-content hash; packs are committed,
receipt-covered artefacts whose sha256 is echoed in scoring receipts.
**Pack-staleness rule:** packs are dated snapshots. The pack scored against
is the committed pack whose hash the receipts echo; packs are re-harvested
only between scoring cycles (an ordinary dated commit), never mid-run, so
evidence is identical across the runs of a cycle. Platform-state changes
after a pack's harvest date are out of scope for that cycle's scores, and
the harvest date is reported with results. **Harvester-integrity
commitment:** endpoints that bot-gate scripted fetches (verified 2026-08-15:
DANS returns HTTP 200 with a JavaScript challenge body — a silent false
positive; tDAR returns 403) are fetched through a rendering step with
challenge-page detection before any census reliance; where a register is
served by a script-only application, its data source is queried directly
and the queries recorded. **Identifier-recovery rule (registrant,
2026-08-15):** where a declared identifier fails to resolve — a cited DOI
that 404s at its registrar, or a dead repository link — the harvest
procedure attempts a bounded recovery before recording the gap: one search
of the relevant registrar's public API (DataCite or Crossref) by title and
author, and one search of the named repository where one is named. A
recovered record enters the evidence pack flagged `recovered`, with the
query recorded, and is never silently substituted for the cited
identifier: the citation defect remains visible in the pack and reportable
as a study finding, while the recovered record supplies ordinary rung-(i)
evidence about the artefact's actual status. Recovery is deliberately
bounded — the analogue of the reproduction lane's minimal, documented code
corrections — and a no-result after the two searches is recorded as a dead
link, not pursued further. Precedent case: marwick-2025's cited
10.5281/zenodo.14561925 resolves at neither DataCite nor Zenodo
(2026-08-15).

The isolation wording of amendment 1 §4 is corrected to what is actually
enforced (registrant's 2026-08-14 ruling: implement what can be
implemented; amend the text where a control is infeasible). Spawn-time
path-scoped read enforcement is infeasible in the harness permission model
(repo-wide); the operative controls are: the agent tool allowlist
(read-only tools); complete per-spawn file-access lists derived post hoc
from the run transcript and archived with run artefacts; contamination
flagging (any successful out-of-scope access fails the run); and a
reconciliation gate that re-validates receipts from completed transcripts —
including the attempts-are-not-reads rule (a declared read whose every
attempt errored never entered context and is not a read) — with a hard
stop on failure. Empirical anchor: post-hoc reconciliation of all 45
retained benchmark transcripts found zero contaminating file accesses
(§4 isolation held) and machine-validated all receipts. The prohibition on
reading persisted assessments stands unchanged.

### 3. Concordance reference re-derivation (E8 v2)

The registered concordance check compared census-lane scores against pilot
reference scores that are old-instrument and reproduction-informed — a
two-axis mismatch that structurally caps concordance below the gate. The
reference set is re-derived under the clarified instrument and the census
input surface (paper + evidence pack), with this pre-specified shape
(registrant, 2026-08-15):

- **Anchor:** ruling-driven re-derivation with targeted human
  adjudication. Starting from the registered reference set, the ratified
  clarifications are applied item by item; the registrant adjudicates
  every changed item, all 68 disputed items from the mining pass, and any
  item whose prior score rests on reproduction-only evidence (a
  census-surface check across all 150 items, scored through the item-3
  ladder); plus a spot-check sample of undisputed items. No
  machine-derived reference: a reference produced by the lane it gates
  would partly measure self-agreement.
- **Blinding disclosure:** the pilot adjudication is necessarily
  unblinded (the registrant has seen the benchmark outputs); the census
  human-validation subsample (registration §8, n = 12) remains blinded
  and post-census exactly as registered, and both exercises run one
  shared hand-scoring protocol (the pilot exercise rehearses it).
- **Registration:** the re-derived set is registered as a new reference
  dataset (E8 v2) with per-item provenance (prior score → ruling applied
  → adjudication note); the original set remains registered as
  historical. The concordance gate is re-pointed at v2. Entailed flips
  are documented before re-scoring (at minimum dye-et-al-2023 data R1.3;
  key-et-al-2024 A2; F-block items on both papers).

### 4. Re-validation design and remediation ladder

The reliability check re-runs on the clarified instrument, the v1.1
structured-output contract, and the reconciliation-gated harness: the same
registered design (three arms × five pilot papers × three runs; stability
and concordance-against-E8-v2, both gates ≥ 0.90; model pins
claude-sonnet-5, claude-opus-5, claude-fable-5 unchanged, price-ordered
selection unchanged). The below-threshold remediation ladder carries
amendment 1 §2's structure forward for the re-specified check: at most one
routing-fix attempt (content delivery only, instrument text untouched)
followed by a single re-run of the stability check; failing that, the
registered majority-vote consequence applies with no further iteration,
and the arm choice is recorded explicitly. The interpretation-guide
promotion in §5 below is part of this amendment's pre-declared delivery
specification, not a consumption of that routing-fix attempt.

### 5. Delivery and receipts specification

The FAIR-principles interpretation guide is promoted from pull to push:
benchmark receipts showed inconsistent pulling across spawns (and
attempt-based pull counts can mislead in both directions — one spawn's
declared pulls all failed at a wrong path and it honestly scored
guideless), so interpretive context is now uniform by construction. The
guide is version-aligned to instrument v2.1, with an explicit supremacy
clause: the instrument governs wherever the guide is silent or diverges.
Every pushed instrument is registered with a content-integrity hash; the
push layer refuses to inject text whose bytes differ from the registered
hash, and receipts echo instrument versions and receipt tokens. Scoring
outputs validate against structured-output contract v1.1
(self-identifying `schema_version`; per-input non-scoring provenance;
per-sub-principle evidence-pack citations; escalation without fabricated
scoring blocks).

### 6. Cosmetic corrections — dissolved on verification

*(Revised 2026-08-17 at pre-lodgement verification; the approved draft
proposed correcting the strings in place. The staged in-place fix was
re-escaped by the registry's write path — round-trip diff, four spans —
and the render check then showed no visible defect exists, so the
correction dissolves into this verification record.)*

Amendment 1's lodgement flagged two comparator strings in the original
registration text ("post > pre on all measures"; "pinned < unpinned") as
possibly rendering as literal HTML entity strings on the public page.
Pre-lodgement verification of this amendment (2026-08-17) resolved the
flag: the registry stores every literal comparator character as an HTML
entity on write, and its renderer decodes them correctly, so the public
page has always displayed the intended characters and no defect exists.
No correction is required or made; this section records the verification
outcome so the flag is closed rather than silently dropped.

---

## Pre-lodgement checklist (D2)

- [x] 2026-08-17 Re-run the §1 consistency check of this amendment's operative text
      against the canonical instrument v2.1, the Pass 6 mirror, and the
      erratum log (maintenance rule 4); record deliberate differences.
- [x] 2026-08-17 Verify the D5 gate PASS and the full test suite green at the
      lodgement commit; tag the repository state
      (`osf-amendment-2-<date>`).
- [x] 2026-08-17 Convert to a paste artefact with the C5-fixed unwrap script
      (`scripts/unwrap-paste-file.py`, M14–M16 + idempotence self-check);
      flowing lines, no tables (OSF text boxes render breaks literally).
- [x] 2026-08-17 Lodge via the OSF API as a versioned registration update appended
      to the Summary field under a dated banner (amendment-1 route); DOI
      unchanged; round-trip verify byte-identical.
- [x] 2026-08-17 (ran pre-lodgement; correction dissolved — see §6) Confirm the two §6 comparator fixes render correctly on the public
      page after lodgement.
- [x] 2026-08-17 UNBLOCKED — Only after lodgement: begin D3 preparation (reconcile-run wiring,
      schema push with sha256 receipts, S4 validator probe, standing API
      review gate for the 45-spawn re-benchmark — billing route stated).

---

## Promotion record (2026-08-17)

**Registrant approval.** Shawn read the full draft (as amended through
`ce0171e`, the identifier-recovery rule) and approved with no corrections
(2026-08-17). The approved text is promoted verbatim — no register
re-expression was produced, so there is no second version to choose
between (the amendment-1 re-expression step existed because two versions
did). The paste artefact is a mechanical format conversion of this
approved text (markdown structure to flowing OSF paragraphs), verified
token-invariant below.

**Registers loaded** (academic-prose gate; recorded per the canonical
preregistration register's promotion rule):

1. `~/personal-assistant/data/notes/style-guides/academic/reference_register-academic.md`
2. `~/personal-assistant/data/notes/style-guides/academic/reference_register-preregistration.md`
3. `.notes/reference_register-prereg.md` (project layer)

## §1 consistency check record — maintenance rule 4 (2026-08-17)

Checked against: instrument v2.1 canon (`fair-instrument.md`), the Pass 6
prompt mirror, erratum-log Entry 3 + ratified scope, the benchmark
summary, the disagreement analysis, the platform-rows verification note +
enrichment addendum, and `manifest.yaml`.

**Verified specifics (all match their sources):** benchmark statistics
(stability 121/131/122 of 150 = 0.807/0.873/0.813; concordance
0.773/0.807/0.820); 68 of 150 disputed items; the 82.6% Zenodo default
sample; CoreTrustSeal dates (ADS 2027-02-12; DANS 2028-02-27; tDAR lapsed
2025-12-16); precedent DOIs (10.15497/rda00050, 10.1111/jiec.12738); the
dead DOI 10.5281/zenodo.14561925; model pins (claude-sonnet-5,
claude-opus-5, claude-fable-5) against the manifest; version identifiers
(instrument v2.1, guide v1.1, contract v1.1); registered vocabulary terms
present in canon (research surface, rung (i)/(ii), by-construction,
evidence pack, principal, unscoreable).

**Deliberate differences (recorded, not defects):**

1. §1 items compress the ratified operative text rather than restating it
   byte-for-byte; the operative home is the canonical instrument v2.1,
   hash-registered (C7) at the tagged lodgement commit. Items 1, 4, and 5
   are near-verbatim; items 2, 3, 6, and 7 are condensed with no
   token-class change.
2. Item 1 drops Entry 3's closing clause "keeping responsibility
   reportable as a study finding" (present in canon; the amendment's
   research-surface paragraph states the same fact as "recorded per
   required input as non-scoring metadata").
3. The instrument's Row 6 drops the dated 9.3M component-DOI count
   (evidence detail retained in the verification note); the amendment
   states the qualitative both-halves finding.

**§6 outcome (2026-08-17, superseding the morning's "defect confirmed"
note):** the anonymous API read found both entity strings in the stored
summary (revision `6a7017da97adb06288afef80`) — but that observed the
*storage encoding*, not a rendering defect. The staged in-place fix was
re-escaped by the registry's write path (round-trip diff caught all four
sent comparators stored as entities), and the browser render check of the
public page showed the intended literal characters displayed throughout,
with zero entity strings visible. §6 was therefore revised from a
correction to a dissolution record before submission; the appended
amendment remains the only change, touching only the `summary` response
key.
