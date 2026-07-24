# FAIR instrument v2.0 — canonical file

**Status: FROZEN by OSF registration 2026-07-20 (DOI 10.17605/OSF.IO/DQNHG)** —
changes require the §8 regression gate + an erratum-log entry + an OSF amendment
before any affected analysis runs.
**Version:** 2.0 (standardised 2026-02-11)
**Canonical home** per routing design §4 (extracted 2026-07-24 from
`extraction-system/prompts/06-infrastructure_pass6_prompt.md`, review finding D1;
the Pass 6 prompt mirrors this content verbatim under a machine-checked banner).
**Registration consistency:** matches preregistration §7.1; the 2026-07-22
erratum-log entry 1 corrections are incorporated (the /15 example scale; Tier 0–4
demarcation).
**Consumers:** `fair-assessor` (pushed, with read receipt); research-assessor
Pass 6 prompt (verbatim mirror, human lane); registered in `manifest.yaml`
`shared_content`.

---

## Rubric: 15 binary sub-principles, data and code scored independently

Score data and code **independently** as two parallel Findable, Accessible,
Interoperable, Reusable (FAIR) assessments. Each sub-principle is binary:
present (1) or absent (0). **Unscoreable sub-principles score 0 — the instrument
scores evidenced practice** (preregistration §7.1).

```text
FINDABLE (max 4):
  F1: Globally unique persistent identifier (DOI, IGSN, SWHID, accession)  /1
  F2: Rich metadata (structured: authors, title, keywords, description)     /1
  F3: Metadata explicitly includes the identifier                           /1
  F4: Resource indexed in searchable registry (Zenodo, CRAN, DataCite)      /1

ACCESSIBLE (max 4):
  A1:   Retrievable via standard protocol — assess against FULL research    /1
        dataset, not just supplement. If data_completeness coverage is
        "minimal" or "partial", A1 = 0. Exception: ethical restrictions.
  A1.1: Protocol is open, free, universally implementable                   /1
  A1.2: Protocol allows authentication/authorisation where needed           /1
        (CARE-compliant restrictions = POSITIVE signal)
  A2:   Metadata remains accessible even if resource unavailable            /1

INTEROPERABLE (max 3 — NOT 4):
  I1: Uses formal, accessible, shared knowledge representation              /1
  I2: Vocabularies follow FAIR principles themselves                        /1
  I3: Includes qualified references to other resources (PIDs)               /1

REUSABLE (max 4):
  R1:   Richly described with plurality of relevant attributes              /1
  R1.1: Released with clear, accessible data usage licence                  /1
  R1.2: Associated with detailed provenance                                 /1
  R1.3: Meets domain-relevant community standards                           /1

TOTAL per artefact type: /15
```

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

---

Receipt-token: 3ddcbfd82575a2f8
