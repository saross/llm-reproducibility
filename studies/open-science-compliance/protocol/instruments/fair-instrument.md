# FAIR instrument v2.1 — canonical file

**Status: FROZEN by OSF registration 2026-07-20 (DOI 10.17605/OSF.IO/DQNHG);
v2.1 clarifications applied under erratum-log Entry 3 (RATIFIED 2026-08-14)
and the 2026-08-15 platform-table rulings** — queued for OSF amendment 2,
which must lodge before any affected analysis runs (re-benchmark and census).
Changes require the §8 regression gate + an erratum-log entry + an OSF
amendment before any affected analysis runs.
**Version:** 2.1 (clarifications 2026-08-15; v2.0 standardised 2026-02-11)
**Canonical home** per routing design §4 (extracted 2026-07-24 from
`extraction-system/prompts/06-infrastructure_pass6_prompt.md`, review finding D1;
the Pass 6 prompt mirrors this content verbatim under a machine-checked banner).
**Registration consistency:** matches preregistration §7.1 as clarified by
erratum-log entries 1 (2026-07-22) and 3 (2026-08-10, ratified 2026-08-14);
the platform table's evidence base is the dated verification note and
repository-evaluation enrichment addendum under
`studies/open-science-compliance/outputs/validation/platform-rows-2026-08-15/`.
**Consumers:** `fair-assessor` (pushed, with read receipt); research-assessor
Pass 6 prompt (verbatim mirror, human lane); registered in `manifest.yaml`
`shared_content`.

---

<!-- canon-begin: fair-instrument -->
## The research surface — unit of assessment (v2.1)

The unit of assessment is the paper's research surface: the complete set of
digital artefacts — data, code, and other digital inputs — required to
reproduce the paper's reported results, as reachable from the published
paper. Each FAIR sub-principle scores the empirical status of those
artefacts; creator identity, depositor identity, and responsibility for
closure never affect scores. A precisely cited, well-archived third-party
input earns full credit; a closed or unpublished input is penalised even
where closure is beyond the authors' control. Provenance (author-deposited /
third-party / undeterminable) is recorded per required input as non-scoring
metadata, keeping responsibility reportable as a study finding.

## Rubric: 15 binary sub-principles, data and code scored independently

Score data and code **independently** as two parallel Findable, Accessible,
Interoperable, Reusable (FAIR) assessments. Each sub-principle is binary:
present (1) or absent (0). **Unscoreable sub-principles score 0 — the instrument
scores evidenced practice** (preregistration §7.1; see the unscoreable boundary
under the evidence ladder below).

```text
FINDABLE (max 4):
  F1: Globally unique, persistent identifier explicitly associated with     /1
      the artefact — its own PID (DOI, IGSN, SWHID, accession), or the
      article DOI where the artefact is distributed as that article's
      supplement. This is a deliberate, declared departure from the
      strict object-PID reading (cf. F-UJI): F2/F3/F4 remain strictly
      artefact-level (independent metadata record; identifier carried
      in that record; registry indexing), so the granularity deficiency
      of supplement-only deposit is scored there, yielding F subtotals
      of 4/4 (own-PID deposit), 1/4 (supplement under the article DOI),
      0/4 (unpublished).
  F2: Rich metadata (structured: authors, title, keywords, description)     /1
  F3: Metadata explicitly includes the identifier                           /1
  F4: Resource indexed in searchable registry (Zenodo, CRAN, DataCite)      /1

ACCESSIBLE (max 4):
  A1:   Retrievable via standard protocol — assess against FULL research    /1
        dataset, not just supplement. If data_completeness coverage is
        "minimal" or "partial", A1 = 0. Exception: ethical restrictions.
  A1.1: Protocol is open, free, universally implementable                   /1
  A1.2: Protocol allows authentication/authorisation where needed           /1
        (CARE-compliant restrictions = POSITIVE signal). A fully open
        resource requiring no authentication satisfies A1.2 — the
        protocol supports authentication where needed, and none is
        needed. Score 0 only where access control exists or is
        warranted but the mechanism is undocumented or unjustified.
  A2:   Metadata remains accessible even if resource unavailable            /1

INTEROPERABLE (max 3 — NOT 4):
  I1: Uses formal, accessible, shared knowledge representation              /1
  I2: Vocabularies follow FAIR principles themselves                        /1
  I3: Includes qualified references to other resources (PIDs)               /1

REUSABLE (max 4):
  R1:   Richly described with plurality of relevant attributes              /1
  R1.1: Released with clear, accessible data usage licence                  /1
        (licence semantics: see the R1.1 section below)
  R1.2: Associated with detailed provenance                                 /1
  R1.3: Meets domain-relevant community standards                           /1
        (qualifying standards: see the R1.3 section below)

TOTAL per artefact type: /15
```

## Aggregation over heterogeneous input sets (v2.1 — initial rule, iterable)

Within each artefact type, sub-principles are scored on the principal
artefact(s): those whose absence would block reproduction of the reported
results. For data, a sub-principle scores 1 only if it holds for every
principal dataset (conjunctive scoring — mirroring the most-restrictive rule
for licence conflicts); proportional coverage of the full required set,
including non-principal upstream sources, is carried by the data-completeness
lane and feeds the A1 override as registered. For code, the paper's own
analysis scripts are always principal; third-party dependencies are never
substitutes for them and enter scoring only through citation quality (I3)
and the evidence pack.

## Evidence admissibility — the two-rung ladder (v2.1)

Admissible evidence forms a two-rung ladder. Rung (i), direct evidence: the
paper's own text and the per-paper verified artefact evidence pack supplied
at scoring time — complementary records, with disagreements between them
governed by the specific rules (e.g. the R1.1 most-restrictive licence
rule). Rung (ii), by-construction inference: platform entitlements from the
closed, instrument-listed table below, applicable only to facts on which
rung (i) is silent. Table entitlements are floors, not ceilings: they state
the minimum apparatus the platform enforces on everything it hosts;
rung-(i) evidence may establish more.

**Unscoreable boundary:** the registered unscoreable→0 default applies only
after this ladder is exhausted: a sub-principle is unscoreable only when
neither the paper, nor the evidence pack, nor a listed by-construction
entitlement speaks to it.

## Platform entitlement table (v2.1)

A closed table: only listed entitlements support rung-(ii) inference. Rows
were verified at the granting services on 2026-08-15 (dated verification
note + repository-evaluation enrichment, committed under
`outputs/validation/platform-rows-2026-08-15/`). The table is extensible by
dated amendment or, pre-census, by gated instrument edit (Dataverse,
Australian Data Archive, Figshare, and Dryad flagged as likely additions).
CoreTrustSeal (CTS) certification status is a presence-floor credential
informing how much weight by-construction inference can bear; it is never
itself a scoring input.

**Row 1 — DataCite-registered DOI.** Entitlements: a DataCite metadata
record carrying the identifier exists; the DOI string is undeletable and
Handle-resolvable. NOT guaranteed: public metadata accessibility after
withdrawal — DataCite's prescribed retraction workflow sets the DOI to
Registered, which is not retrievable via the Public API. Caveats: mandatory
DataCite metadata can be legally satisfied with null-codes (`:unkn`,
`:none`, `:null`) — schema compliance is not substantive description; and
DataCite mandates no rights/licence property, so every licence entitlement
in this table is repository-level, never DataCite-level.

**Row 2 — Zenodo.** Entitlements: DataCite metadata; a licence field on
open-access records (restricted and embargoed records sit outside the
guarantee's scope) — the licence itself must still be identified per the
R1.1 rule; persistence: tombstone page on withdrawal with DOI and URL
retained, records and files preserved on retraction, retention for the
lifetime of the repository, and metadata always publicly accessible.
These persistence entitlements are the platform's own policy assertions,
third-party-unaudited (Zenodo holds no CTS certification and has never
applied). Default-licence footnote: Zenodo pre-fills CC-BY-4.0 at deposit
(82.6% of sampled records carry the default value). A default-valued
licence is fully operative — the instrument assesses the research surface,
not intent; the empirical default-domination is interpretive context only,
never a score modifier. A description is recommended, not guaranteed.

**Row 3 — CRAN.** Entitlements: structured package metadata (mandatory
DESCRIPTION fields with controlled vocabulary); a licence field with NO
default value — the only listed platform where a licence value is, by
construction, evidence of an author decision; a perpetual distribution
grant. NOT guaranteed: persistence is a URL-path convention governed by
"will not normally be removed", and CRAN issues no persistent identifier
(registry-corroborated: re3data records pidSystem none). The strongest
metadata floor in the table must not be read as implying a persistence
floor.

**Row 4 — accredited domain repositories (graded; not a uniform floor).**

- ADS (Archaeology Data Service): mandatory validated core template plus
  category-specific technical metadata, enforced at ingest — an
  ingest-enforced domain metadata standard; R1.3 = 1 by construction.
  CTS-certified to 2027-02-12, with a visible renewal chain.
- DANS Data Station Archaeology: a mandatory-field submission gate is
  verified, but it covers a small generic core; the archaeology (ABR+)
  domain vocabulary block is optional — R1.3 requires rung-(i) evidence.
  CTS-certified to 2028-02-27. Metadata always publicly available under
  CC0. Default-licence footnote: DANS pre-fills CC0 1.0 at deposit; the
  Row 2 operative-default rule applies identically.
- tDAR (the Digital Archaeological Record): enforces its internal
  resource model; no external domain metadata standard is named;
  per-field mandatory status and the preservation policy could not be
  verified; CTS certificate lapsed 2025-12-16 (renewal at First Submit
  as of 2026-08-15) — R1.3 requires rung-(i) evidence.

Certification statements are as-of 2026-08-15; re-checks ride any dated
table amendment.

**Row 5 — GitHub and GitLab.** Entitlement: a licence field via the
evidence pack only — and the two platforms differ: GitHub's licence
detection may return NOASSERTION for unrecognised files; GitLab exposes no
SPDX identifier and reports licence data only on an opt-in query. Detection
is not a usable SPDX identifier; the licence must be identified per the
R1.1 rule. NO persistence entitlement of any kind (repositories are
deletable, renamable, and rewritable).

**Row 6 — publisher supplement of a Crossref-registered article.**
Applicable only where the supplement is served directly from the article
landing page with no independent deposit. Entitlements: HTTPS delivery via
the article landing page; article-level record persistence — a Crossref
member obligation plus a Crossref retention right under "commercially
reasonable efforts", not a by-construction warranty, and scored
accordingly. NO independent metadata record, licence field, registry
indexing, or resource-level identifier — hence F2 = F3 = F4 = 0 and A2 = 0
for supplement-only deposits. Component DOIs exist at scale but are
metadata-poor; a component DOI, where present, is rung-(i) evidence, never
a table entitlement. A supplement deposited under its own identifier in a
general or domain repository (e.g. journal supplements hosted at Figshare;
data in Dryad) is scored as a deposit on that platform — via the evidence
pack and, where listed, that platform's row — never under this row.

**Table-wide note:** a description field is guaranteed by no listed
platform except CRAN; entitlements are verified at the service that grants
them — aggregator assertions (including re3data's certificate field) never
override the granting service's own register.

## Licence semantics — R1.1 (v2.1)

Licences are assessed per artefact: where a paper and its separately
deposited dataset or software carry different licences, each artefact is
scored on its own licence — a clean division, not a conflict. The
most-restrictive default applies only where sources disagree about the
licence of the *same* artefact: (a) a supplement carried in or served with
the article itself — unless explicitly stated otherwise, the article's
licence extends to publisher-hosted supplements; check for both article and
supplement licences; absent a separate supplement licence, default to
same-as-paper; where both exist and differ, the more restrictive governs;
(b) a deposited artefact whose licence as asserted in the paper differs
from the licence recorded at the hosting service — the more restrictive
governs scoring (the responsible-consumer reading). Where the paper is
silent, artefacts on third-party services are scored on the licence
recorded at the service (via the evidence pack) — a platform's mandatory
licence field does not itself satisfy R1.1; the licence must be identified.

## Community standards — R1.3 (v2.1)

R1.3 scores deposit-level standards — what GO-FAIR measures: artefact
reusability, not method quality. Qualifying routes: (a) generic metadata
schemas (DataCite, Dublin Core); (b) domain schemas and vocabularies
(ARIADNEplus, CIDOC-CRM, Darwin Core); (c) deposit in an accredited domain
repository whose ingest enforces its metadata standard. For code: package
structure, CITATION.cff, CodeMeta, or community review (CRAN, JOSS,
rOpenSci). Methodological standards (IntCal20, OxCal, established methods)
do not qualify. Route (c) is operationalised by the platform entitlement
table's graded Row 4: currently ADS by construction; DANS and tDAR require
rung-(i) evidence.

## Independent data and code scoring

- Score `data_fair` (/15) and `code_fair` (/15) separately.
- Do NOT sum into a single aggregate — report independently
  (never aggregated into a combined score; preregistration §7.1).
- When data or code is absent/not applicable, set `"available": false`.
- Absence ≠ non-compliance (distinguish N/A from Not FAIR).

## Rating bands (per artefact type, on /15)

| Score | Percentage | Rating |
|-------|------------|--------|
| 13-15 | 87-100% | Highly FAIR |
| 9-12 | 60-80% | Moderately FAIR |
| 5-8 | 33-53% | Minimally FAIR |
| 0-4 | 0-27% | Not FAIR |

Worked example of totals: Findable 3/4; total 14/15; percentage 93.3%;
rating `highly_fair`.

## Data-completeness coverage procedure

Assess whether the paper shares **all** the data needed for reproduction, not
just the subset deposited in a supplement or repository. This feeds the A1
completeness rule and captures a dimension FAIR infrastructure scoring alone
misses.

1. **Enumerate datasets** referenced in Methods/Results (including upstream
   sources).
2. **Classify each** using the five-tier access classification (Tier 0-4):
   - Tier 0: Direct download (DOI-based repository, open supplement)
   - Tier 1: Programmatic extraction (HTML tables, API)
   - Tier 2: Available but requires manual steps (registration, paywall, PDF
     table extraction)
   - Tier 3: Exists but inaccessible (closed thesis, paywalled monograph,
     co-author held)
   - Tier 4: Not found / never published

   > **Demarcation note (2026-07-22):** these access tiers are a working
   > classification used only for the data-completeness coverage computation.
   > They are distinct from the preregistered six-level data-availability
   > taxonomy (L1-L6, Phase 2 preregistration §7.3), which is assigned only at
   > reproduction time from actual retrieval attempts. Never conflate the two.

3. **Calculate coverage**: datasets accessible (Tier 0-2) / total datasets.
   Where feasible, also compute record-weighted coverage.
4. **Assign category**: complete (100%), substantial (75-99%), partial
   (25-74%), minimal (0-24%).
5. **Identify barriers**: co-author gatekeeping, closed monograph, unpublished,
   embargoed, proprietary, ethics restricted, paywall, registration required.

**Assessment scope** (for meta-analyses or papers aggregating many datasets):
`straightforward` (<20 datasets — full inventory) / `complex` (20-99 —
sampled inventory with extrapolation) / `infeasible` (100+ — estimate only,
with rationale).

**A1 cross-reference:** if `coverage_category` is "minimal" or "partial", set
A1 = 0 for data FAIR. Exception: ethically restricted data (CARE principles,
human subjects) does not count against completeness — A1 requires that a
*majority* of the research data be retrievable via standard protocol, with an
exception for documented ethical/legal restriction (preregistration §7.1).

## Out of scope

FAIR for Research Software (FAIR4RS) scoring of code artefacts is a planned
exploratory extension, not part of the registration: if implemented, the
FAIR4RS instrument will be lodged as a dated OSF amendment and will pass the
same reliability protocol (preregistration §8) before any FAIR4RS scoring
begins.
<!-- canon-end: fair-instrument -->

---

Receipt-token: 5ff4c48c4f5c7321
