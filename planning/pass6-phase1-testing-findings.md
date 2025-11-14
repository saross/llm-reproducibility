# Pass 6 Infrastructure Extraction: Phase 1 Testing Findings

**Date:** 2025-11-11

**Status:** Testing complete on 4-paper diverse corpus

**Purpose:** Document extraction challenges, guidance gaps, schema adequacy, and recommendations from Pass 6 infrastructure prompt testing.

## Executive Summary

Completed Pass 6 infrastructure extraction testing on 4 archaeologically-themed papers spanning publication types, disciplines, and eras (2016-2024):

| Paper | Type | FAIR Score | PID Connectivity | Key Finding |
|-------|------|------------|------------------|-------------|
| Ballsun-Stanton et al. 2018 | SoftwareX | 13/15 (86.7%) | 3/6 | Software publication with exceptional documentation but no systematic structure for assessment |
| Sobotkova et al. 2024 | J Documentation | 4/15 (26.7%) | 1/6 | Typical Humanities, Arts, and Social Sciences (HASS) computational paper: code shared but infrastructure minimal |
| Penske et al. 2023 | Nature | 14/15 (93.3%) | 2/6 | Ancient DNA best practices: exemplary data infrastructure, minimal code sharing |
| Sobotkova et al. 2016 | Book chapter | 0/15 (0%) | 0/6 | Pre-FAIR baseline: transition era before Persistent Identifier (PID) adoption |

**Overall Assessment:** Pass 6 prompt successfully extracts infrastructure across diverse publication types. Schema robust but software documentation structure needed. Guidance gaps identified for edge cases.

## Test Corpus Design

### Selection Rationale

Papers selected to stress-test extraction framework across multiple dimensions:

1. **Publication Type Diversity**
   - Journal article (Nature, Journal of Documentation, SoftwareX)
   - Edited book chapter (Sidestone Press)
   - Rationale: Test applicability beyond standard journal articles

2. **Discipline Norms**
   - Ancient DNA genomics (gold-standard data FAIR practices)
   - Computational archaeology (emerging code sharing norms)
   - Research software engineering (FAIR4RS principles)
   - Rationale: Compare FAIR adoption across archaeological sub-disciplines

3. **Temporal Spread**
   - 2016: Pre-FAIR Guidelines (Wilkinson et al. 2016)
   - 2018: Post-FAIR Guidelines, software publication focus
   - 2023: High-profile Nature publication
   - 2024: Recent HASS computational methods
   - Rationale: Assess historical evolution and current state

4. **Infrastructure Complexity**
   - Minimal (2016 book chapter)
   - Code-only (2024 methods paper)
   - Data-focused (2023 genomics)
   - Multi-component (2018 software publication)
   - Rationale: Test extraction across infrastructure maturity spectrum

### Coverage Achieved

- **Publication venues:** 4 types (journal article, software journal, book chapter, high-impact journal)
- **FAIR spectrum:** 0/15 to 14/15 (full range)
- **PID connectivity:** 0/6 to 3/6 (partial coverage, no paper had full 6/6)
- **Funding sources:** 12 distinct grants across 5 countries (Australia, Germany, Czech Republic, United States, European Research Council)
- **Research outputs:** 9 GitHub repositories, 1 European Nucleotide Archive (ENA) accession, 6 FAIMS software components, 1 Python package

## Extraction Challenges Encountered

### 1. Missing or Informal Data Availability Statements

**Challenge:** Not all papers include formal "Data Availability" statements despite referencing datasets.

**Example:** Sobotkova et al. 2024 builds on TRAP (Tunisian Regional Archaeological Project) survey dataset but has no data availability statement. Text extraction found:
- References to "TRAP survey data from 2009-2015"
- "Fieldwork data" and "survey records"
- No repository, no access information, no PID

**Current Solution:** Created data availability entry with:

```json
"data_availability": {
  "statement_present": false,
  "statement_type": "implicit_reference",
  "verbatim_statement": "No formal data availability statement. References 'TRAP survey data from 2009-2015' and 'fieldwork data' but no repository or access information provided.",
  "datasets": []
}
```

**Guidance Gap:** Pass 6 prompt instructs "extract verbatim statement" but doesn't specify how to handle:
- Informal dataset references without availability statements
- Proprietary/unpublished datasets referenced in methods
- Legacy datasets predating repository deposition norms

**Recommendation:** Add guidance section "Handling Missing Availability Statements" with decision tree:
1. Formal statement present → extract verbatim
2. No statement but datasets referenced → `statement_type: "implicit_reference"` with note
3. No statement, no dataset mentions → `statement_present: false`, `statement_type: "not_applicable"`

### 2. Book Chapters Without Digital Object Identifiers (DOIs)

**Challenge:** Sobotkova et al. 2016 published in edited volume with International Standard Book Number (ISBN) but no chapter DOI.

**Example:**
- Book: "Mobilising the Past for a Digital Future" (ISBN 978-90-8890-276-7)
- Chapter: pp. 333-384 (52 pages)
- Publisher DOI for book: `10.2307/j.ctvqc6h0v` (JSTOR)
- No individual chapter DOI assignable

**Current Solution:** Captured book-level ISBN and publisher DOI in alternative identifiers:

```json
"publication_identifiers": {
  "paper_doi": null,
  "paper_doi_status": "book_chapter_no_doi",
  "alternative_identifiers": [
    {
      "type": "isbn",
      "value": "978-90-8890-276-7",
      "note": "Book ISBN (print)"
    },
    {
      "type": "publisher_doi",
      "value": "10.2307/j.ctvqc6h0v",
      "note": "JSTOR book DOI (not chapter-specific)"
    }
  ]
}
```

**Guidance Gap:** PID systems guide doesn't address book chapters, edited volumes, or ISBN handling.

**Recommendation:** Add "Book Chapters and ISBNs" section to `pid-systems-guide.md`:
- When to use `paper_doi_status: "book_chapter_no_doi"`
- How to record book-level ISBNs vs chapter-level DOIs
- Publisher DOIs (JSTOR, Springer, Taylor & Francis) as alternative identifiers
- Page ranges as location specifiers

### 3. Permission Statements vs Ethics Approval for Ancient DNA

**Challenge:** Penske et al. 2023 involves ancient human DNA from 135 individuals but lacks formal ethics committee statement.

**Example:** Found in Methods section:

> "Permission to work on the archaeological samples was granted by the respective excavators, archaeologist and curators and museum directors of the sites, who are co-authoring the study."

**Current Solution:** Recorded as permission statement (not ethics):

```json
"ethics_and_permissions": {
  "ethics_approval_present": false,
  "ethics_statement_location": null,
  "permission_statements": [
    {
      "type": "archaeological_samples",
      "authority": "excavators, archaeologists, curators, museum directors (as co-authors)",
      "verbatim": "Permission to work on the archaeological samples was granted...",
      "notes": "Standard ancient DNA practice: institutional permissions via authorities controlling remains rather than ethics committee approval"
    }
  ]
}
```

**Guidance Gap:** Infrastructure prompt doesn't distinguish between:
- Ethics committee approval (living human subjects, contemporary communities)
- Institutional permissions (museum curators, excavators controlling archaeological materials)
- Cultural protocols (Indigenous stakeholder engagement)

**Recommendation:** Add "Ancient DNA and Archaeological Materials Ethics" section to infrastructure prompt:
- Permission statements: institutional authorities (excavators/curators)
- Ethics approval: living subjects, contemporary genetic communities
- Cultural protocols: Indigenous remains, descendant communities
- Examples from ancient DNA literature (Parker et al. 2020 PNAS ethical framework)

### 4. GitHub URLs as Non-Persistent Identifiers

**Challenge:** Multiple papers (Sobotkova 2024, Ballsun-Stanton 2018) share code via GitHub but no archival snapshots with DOIs.

**Example:** Sobotkova et al. 2024 references 3 repositories:
- `github.com/adivea/LeafletGit` (no DOI)
- `github.com/adivea/archaeology-grand-challenges` (no DOI)
- `github.com/adivea/archaeology-object-data-collector-app` (private)

**Current Solution:** Recorded in repositories array with PID status:

```json
"repositories": [
  {
    "url": "https://github.com/adivea/LeafletGit",
    "type": "github",
    "purpose": "Data visualisation package",
    "persistent_identifier": null,
    "pid_status": "no_archival_snapshot"
  }
]
```

**FAIR Impact:** Downgrades Findability (F1) and Accessibility (A1) - GitHub repositories can disappear, change, or become private.

**Guidance Gap:** FAIR principles guide mentions Zenodo archival but doesn't emphasise severity of GitHub-only sharing penalty.

**Recommendation:** Strengthen FAIR4RS guidance on software archival:
- GitHub URLs alone = F1 not met (not persistent)
- Zenodo/Software Heritage snapshot required for F1
- Add scoring example: "GitHub only: 4/15 FAIR; GitHub + Zenodo: 10/15 FAIR"
- Link to Software Heritage auto-archival as zero-effort solution

### 5. Author ORCID Absence Despite Recent Publication Dates

**Challenge:** Papers from 2023-2024 often lack author Open Researcher and Contributor Identifiers (ORCIDs) despite widespread journal requirements.

**Example:**
- Sobotkova et al. 2024 (Journal of Documentation): no author ORCIDs
- Penske et al. 2023 (Nature): no author ORCIDs in extracted PDF text

**Current Solution:** Recorded as missing:

```json
"author_orcids": [],
"orcid_status": "none_found_in_extracted_text",
"notes": "No author ORCIDs present in PDF text. May exist in publisher metadata but not in paper content."
```

**Guidance Gap:** Unclear whether to:
- Extract only from paper PDF (as currently done)
- Check publisher website metadata (CrossRef API)
- Note absence vs not extracted

**Recommendation:** Add ORCID extraction protocol to infrastructure prompt:
- **Primary source:** Author affiliations and acknowledgements sections in PDF
- **Secondary source:** CrossRef metadata if accessible (optional enhancement)
- **Status values:** `present_in_pdf`, `none_found_in_extracted_text`, `not_checked_publisher_metadata`
- **Note:** ORCIDs may exist in publisher systems but absent from paper content

### 6. Supplementary Materials Access Ambiguity

**Challenge:** Many papers reference supplementary materials but access unclear (publisher website, institutional repository, author website, nowhere).

**Example:** Sobotkova et al. 2016 mentions "Supplementary videos available" but no URL or access information.

**Current Solution:** Recorded with uncertain status:

```json
"supplementary_materials": {
  "present": true,
  "description": "Supplementary videos mentioned in text",
  "access": "unclear",
  "repository_url": null,
  "notes": "Videos referenced but no access information, URL, or repository provided"
}
```

**Guidance Gap:** No clear protocol for:
- Checking publisher website vs institutional repository
- Recording "mentioned but inaccessible"
- Distinguishing unavailable vs behind paywall vs lost

**Recommendation:** Add supplementary materials protocol:
1. Extract access information from paper (URL, "available from authors", "see publisher website")
2. Do not attempt external searches (beyond scope)
3. Status taxonomy: `publicly_accessible`, `available_on_request`, `publisher_website`, `unclear`, `mentioned_unavailable`

### 7. Funding Grant Number Format Variations

**Challenge:** Grant identifiers vary widely in format across funding agencies.

**Examples:**
- Australian Research Council (ARC): `LE140100151` (prefix optional)
- European Research Council (ERC): `ERC-CoG-2Form 2019 - GA 834616` (multiple formats)
- Czech Science Foundation: `P405/12/0926` (slashes)
- NeCTAR (Australia): `RT043` (short codes)

**Current Solution:** Recorded as provided in text:

```json
"funding": [
  {
    "agency": "Australian Research Council",
    "grant_number": "LE140100151",
    "amount": "AUD $945,000",
    "period": "2014-2016"
  }
]
```

**Guidance Gap:** No guidance on:
- Normalising grant numbers (with/without agency prefix)
- Persistent identifiers for grants (Open Funder Registry, RAiD)
- Recording collaborative grants with multiple agency codes

**Recommendation:** Add grant identifier guidance:
- Record exactly as appears in paper (verbatim)
- Note preferred formats by major funders (ERC, ARC, National Science Foundation (NSF), National Institutes of Health (NIH))
- Future enhancement: link to Open Funder Registry DOIs

## Guidance Gaps in Reference Materials

### Gap 1: Pre-FAIR Era Papers

**Issue:** Sobotkova et al. 2016 scores 0/15 FAIR but this reflects 2016 norms, not research quality.

**Current Handling:** Added contextual note:

```json
"fair_assessment": {
  "fair_rating": "not_fair",
  "notes": "Zero FAIR score reflects 2016 book chapter baseline before widespread PID adoption and FAIR principles. Published pre-FAIR Guidelines (Wilkinson 2016) and pre-FAIR4RS (Chue Hong 2022)."
}
```

**Guidance Gap:** FAIR principles guide doesn't address:
- Historical baselines (2010 vs 2015 vs 2020 vs 2024)
- When to note "pre-FAIR era" vs "non-compliant"
- Whether 0/15 scores need publication year context

**Recommendation:** Add "Historical Context and Baseline Scores" section to FAIR guide:
- **Pre-2016:** FAIR Guidelines not yet published (Wilkinson et al. 2016)
- **2016-2019:** Early adoption period, discipline variation expected
- **2020-2024:** Widespread awareness, infrastructure maturing
- **Scoring notes:** Always include publication year context for scores <5/15

### Gap 2: Code vs Data FAIR Divergence

**Issue:** Papers can have high data FAIR but low code FAIR (or vice versa).

**Examples:**
- Penske et al. 2023: Data FAIR 14/15, no code shared
- Sobotkova et al. 2024: Code shared (GitHub), Data FAIR 0/15

**Current Handling:** Separate `code_fair_score` and `data_fair_score` fields, plus `combined_fair_score` (max of code/data).

**Guidance Gap:** Unclear how to interpret divergent scores:
- Is 14/15 data + 0/15 code "highly FAIR" overall?
- Should combined score be max, average, or weighted?
- How does discipline norm factor in (ancient DNA = data-centric, software engineering = code-centric)?

**Recommendation:** Add FAIR interpretation guidance:
- **Combined score:** Use maximum of data/code as overall FAIR rating (current approach validated)
- **Rationale:** FAIR applies to research outputs; if primary output (data for genomics, code for software) is FAIR, research meets threshold
- **Report both:** Always show `data_fair_score` and `code_fair_score` separately
- **Discipline context:** Note whether data or code is primary research output

### Gap 3: Software Documentation Assessment

**Issue:** Documentation is critical for FAIR R1 (Reusability) but scattered across multiple fields with no systematic structure.

**Current Handling:** Documentation mentioned in:
- Repository descriptions: "API reference available"
- FAIR rationale: "Comprehensive user manual supports reuse (R1.2)"
- Analysis notes: "Extensive README files"

**Example:** Ballsun-Stanton et al. 2018 (FAIMS) has exceptional documentation:
- API reference (wiki)
- User manual ("FAIMS Cookbook")
- Installation guide
- Developer documentation
- Tutorial examples
- Video walkthroughs

But no structured way to assess completeness, quality, or accessibility.

**Guidance Gap:** No systematic framework for:
- Documentation types taxonomy
- Completeness assessment (none → minimal → basic → good → comprehensive)
- Quality indicators (versioned, includes examples, machine-readable)
- Accessibility (publicly accessible, archived)

**Recommendation:** Already documented in `planning/pass6-software-documentation-enhancement.md`. Decision point: implement now or gather more evidence?

**Status:** DEFERRED to Phase 2 (after broader corpus testing).

### Gap 4: Licence Taxonomy

**Issue:** Licence identifiers vary (full names, abbreviations, URLs, custom statements).

**Examples Encountered:**
- "Creative Commons Attribution 4.0 International (CC-BY-4.0)"
- "CC BY 4.0"
- "https://creativecommons.org/licenses/by/4.0/"
- "MIT License"
- "GNU General Public License v3.0"
- "Custom proprietary licence (see documentation)"

**Current Handling:** Recorded as provided, no normalisation.

**Guidance Gap:** No guidance on:
- Standardising licence identifiers (SPDX codes)
- Recording custom licences
- "No licence" vs "Licence unclear" vs "Proprietary"

**Recommendation:** Add licence identification guidance:
- Use SPDX identifiers where possible: `CC-BY-4.0`, `MIT`, `GPL-3.0`
- Record full name as `licence_name`, SPDX as `spdx_identifier`
- Custom licences: `spdx_identifier: "LicenseRef-Custom"`, description in `notes`
- Link to SPDX licence list: https://spdx.org/licenses/

### Gap 5: Multi-Component Research Outputs

**Issue:** Ballsun-Stanton et al. 2018 describes FAIMS platform with 6 interdependent repositories.

**Example:**
- Core platform: `faims-android`
- Server component: `faims-web`
- Module definition language: `faims-dsl`
- Sample modules: `faims-surveys`
- Documentation: `faims-cookbook`
- Spatial module: `spatialite-android`

**Current Handling:** Created 6 separate repository entries with cross-references.

**Guidance Gap:** No guidance on:
- Capturing component relationships (core, dependency, extension)
- Recording system architecture (client-server, modules, plugins)
- Assessing FAIR for component vs entire system

**Recommendation:** Add "Multi-Component Software Systems" section:
- **Repository relationships:** Add `component_type` field (core, dependency, module, documentation)
- **System architecture:** Add `system_architecture` field describing overall structure
- **FAIR scope:** Assess entire system as unit, not individual repositories

## Schema Adequacy Assessment

### Schema Strengths

1. **Robust PID Coverage**
   - Handles DOIs, ORCIDs, accession numbers, GitHub URLs
   - `alternative_identifiers` array flexible for ISBNs, publisher DOIs, project IDs
   - PID graph summary captures connectivity (0-6 scale)

2. **Flexible Availability Statements**
   - Accommodates formal statements, implicit references, and absences
   - `statement_type` taxonomy covers common cases
   - Verbatim extraction preserves original wording

3. **Comprehensive FAIR Assessment**
   - Separate data/code/combined scores work well
   - 15-principle breakdown enables gap analysis
   - Rationale field captures contextual notes

4. **Funding Granularity**
   - Grant numbers, amounts, periods, agencies well-captured
   - Array structure handles multiple funders

5. **Repository Metadata**
   - Type, purpose, PID status fields adequate
   - URL, description, licence fields cover essentials

### Schema Gaps

#### Gap 1: Software Documentation Structure (Confirmed)

**Issue:** Documentation scattered across multiple fields, no systematic assessment.

**Evidence from Testing:**
- Ballsun-Stanton 2018: Exceptional documentation but ad hoc capture
- Sobotkova 2024: README mentioned in notes, no structured recording
- No completeness scale, no quality indicators

**Proposed Enhancement:** Add `documentation` sub-object within `code_availability`:

```json
"code_availability": {
  "repositories": [
    {
      "url": "https://github.com/FAIMS/faims-android",
      "documentation": {
        "types_present": ["readme", "api_reference", "user_manual", "installation_guide", "tutorial"],
        "completeness": "comprehensive",
        "quality_indicators": {
          "versioned": true,
          "includes_examples": true,
          "machine_readable": false,
          "citation_cff_present": false
        },
        "accessibility": {
          "publicly_accessible": true,
          "archive_preserved": false
        },
        "notes": "Extensive documentation spanning wiki (API reference), PDF manual (Cookbook), video tutorials, but not machine-readable or archived separately."
      }
    }
  ]
}
```

**Status:** Documented in `planning/pass6-software-documentation-enhancement.md`, deferred to Phase 2.

**Decision Point:** Implement now (4 papers provide sufficient evidence) or gather more evidence (extend testing to 10+ papers)?

**Recommendation:** **DEFER to Phase 2.** Current evidence from 4 papers demonstrates need but sample size small (only 2 papers share code). Gather evidence from broader corpus including:
- Pure software publications (SoftwareX, JOSS)
- Computational method papers across disciplines
- User-perspective papers (citing but not creating software)

#### Gap 2: Supplementary Materials Structure

**Issue:** Current schema has binary `supplementary_materials.present` but needs richer structure.

**Evidence from Testing:**
- Penske 2023: 25+ supplementary tables, 9+ supplementary figures (extensive)
- Sobotkova 2024: Supplementary document mentioned (moderate)
- Sobotkova 2016: Videos mentioned but inaccessible (minimal/unclear)

**Current Schema:**

```json
"supplementary_materials": {
  "present": true,
  "description": "string",
  "access": "string",
  "repository_url": "string | null"
}
```

**Proposed Enhancement:**

```json
"supplementary_materials": {
  "present": true,
  "types": {
    "tables": 25,
    "figures": 9,
    "datasets": 2,
    "code": 1,
    "videos": 0,
    "text": 1
  },
  "access_status": "publicly_accessible" | "publisher_website" | "on_request" | "unclear" | "unavailable",
  "repository_url": "https://...",
  "persistent_identifier": "doi:10.XXX/...",
  "notes": "Extensive supplementary materials including damage patterns, contamination estimates, geographical metadata."
}
```

**Priority:** MEDIUM (not critical for FAIR assessment but improves completeness)

**Recommendation:** **IMPLEMENT in Phase 2.** Enhancement straightforward, add to schema v2.6 alongside software documentation structure.

#### Gap 3: Computational Environment Specification

**Issue:** Computational reproducibility requires environment details (software versions, dependencies, container images).

**Evidence from Testing:**
- Sobotkova 2024: R scripts shared but no R version, no package versions, no renv/packrat manifest
- Ballsun-Stanton 2018: Android app requires specific Android API levels but not systematically recorded
- Penske 2023: Bioinformatics pipeline mentioned but tool versions scattered in methods text

**Current Schema:** No dedicated fields for computational environment.

**Proposed Enhancement:**

```json
"computational_reproducibility": {
  "level": "code_dependencies" | "containerised" | "fully_reproducible",
  "environment_specification": {
    "runtime_versions": {
      "language": "R",
      "version": "4.3.1"
    },
    "dependency_management": {
      "manifest_present": true,
      "manifest_type": "renv.lock" | "requirements.txt" | "Dockerfile" | "DESCRIPTION",
      "manifest_location": "https://..."
    },
    "container_image": {
      "present": true,
      "type": "Docker" | "Singularity",
      "registry_url": "https://hub.docker.com/...",
      "persistent_identifier": "doi:10.XXX/..."
    }
  }
}
```

**Priority:** HIGH (critical for computational reproducibility assessment on FAIR spectrum)

**Recommendation:** **IMPLEMENT in Phase 2.** Requires careful design - should align with existing `computational_reproducibility_level` field (currently 5-level spectrum). Consider merging into unified `computational_reproducibility` object.

#### Gap 4: Author Contributions (CReDIT Taxonomy)

**Issue:** Penske et al. 2023 includes detailed author contributions using Contributor Roles Taxonomy (CReDIT) but no schema structure to capture.

**Example from Penske 2023:**
- W.H.: Conceptualisation, funding acquisition, investigation, project administration, supervision
- K.G.: Formal analysis, methodology, software, visualisation, writing
- [17 more authors with specific roles]

**Current Schema:** No author contributions fields.

**Proposed Enhancement:**

```json
"author_contributions": {
  "statement_present": true,
  "taxonomy": "credit" | "custom",
  "contributions": [
    {
      "author": "W. Haak",
      "roles": ["conceptualisation", "funding_acquisition", "investigation", "project_administration", "supervision"]
    },
    {
      "author": "K. Gawrysiak",
      "roles": ["formal_analysis", "methodology", "software", "visualisation", "writing_original_draft"]
    }
  ],
  "verbatim_statement": "Full text of author contributions statement..."
}
```

**Priority:** LOW (nice-to-have for reproducibility culture assessment but not core FAIR)

**Recommendation:** **DEFER indefinitely.** Author contributions valuable for understanding research roles but:
- Not directly related to FAIR assessment
- High extraction effort (17+ authors × 5+ roles each)
- CReDIT taxonomy adoption still variable
- Focus limited extraction effort on core infrastructure

#### Gap 5: Multi-Version Tracking

**Issue:** Software repositories may have multiple versions with different FAIR characteristics (initial release vs current state).

**Example:** Ballsun-Stanton 2018 describes FAIMS 2.x (Android app, 2012-2018) but FAIMS 3.0 now exists (web-based, 2020+).

**Current Schema:** Single snapshot only (publication date state).

**Proposed Enhancement:** Out of scope for current project.

**Recommendation:** **DO NOT IMPLEMENT.** Multi-version tracking requires:
- Longitudinal data collection beyond publication snapshot
- Software Heritage integration for historical analysis
- Out of scope for paper-based extraction

Record software state **as described in paper** (2018 publication describes 2.x, not 3.0).

## Recommendations

### Immediate Actions (Phase 1 Completion)

1. **Update Infrastructure Prompt** ✅ Priority: HIGH
   - Add "Handling Missing Availability Statements" decision tree (Section 2.1)
   - Add "Permission Statements vs Ethics Approval" guidance for ancient DNA (Section 2.3)
   - Add ORCID extraction protocol (Section 2.5)
   - Add supplementary materials protocol (Section 2.6)

2. **Update PID Systems Guide** ✅ Priority: HIGH
   - Add "Book Chapters and ISBNs" section (Section 2.2)
   - Add grant identifier format examples (Section 2.7)
   - Add SPDX licence identifiers guidance (Section 2.4)

3. **Update FAIR Principles Guide** ✅ Priority: HIGH
   - Add "Historical Context and Baseline Scores" section (Section 3.1)
   - Add FAIR interpretation guidance for divergent data/code scores (Section 3.2)
   - Strengthen GitHub-only vs Zenodo guidance with scoring examples (Section 2.4)

### Phase 2 Enhancements (After Broader Testing)

4. **Software Documentation Structure** ⏳ Priority: MEDIUM
   - Status: Enhancement documented, evidence from 4 papers
   - Action: Extend testing to 10+ papers (mix of software creators and software users)
   - Decision point: If pattern holds, implement in schema v2.6

5. **Supplementary Materials Enhancement** ⏳ Priority: MEDIUM
   - Action: Implement structured types and access status in schema v2.6
   - Low effort, clear benefit for completeness

6. **Computational Environment Specification** ⏳ Priority: HIGH
   - Action: Design unified `computational_reproducibility` object for schema v2.6
   - Integrate with existing 5-level spectrum
   - Critical for assessing code FAIR R1 (reusability)

7. **Multi-Component Software Guidance** ⏳ Priority: LOW
   - Action: Add guidance on component relationships and system architecture
   - Relevant primarily for software publications (narrow scope)

### Deferred Indefinitely

8. **Author Contributions (CReDIT)** ❌ Priority: LOW
   - Rationale: Not core to FAIR assessment, high extraction effort, variable adoption
   - Alternative: Note presence/absence only, don't extract detailed roles

9. **Multi-Version Tracking** ❌ Priority: N/A
   - Rationale: Out of scope (requires longitudinal data beyond publication snapshot)
   - Current approach: Record software state as described in paper (correct)

## Testing Outcomes Summary

### Pass 6 Prompt Performance

**Strengths:**
- Successfully extracted infrastructure from diverse publication types (journal, book chapter, software publication)
- Handled wide FAIR spectrum (0/15 to 14/15)
- Captured complex funding arrangements (12 grants, 5 countries)
- Navigated missing statements and informal references appropriately

**Limitations Identified:**
- Guidance gaps for edge cases (book chapters, pre-FAIR era papers, ancient DNA ethics)
- Software documentation assessment ad hoc, needs structure
- Computational environment under-specified in schema
- ORCID extraction inconsistent (PDF text vs publisher metadata)

**Overall Assessment:** Prompt robust and schema adequate for core infrastructure extraction. Identified gaps addressable through guidance updates (immediate) and schema enhancements (Phase 2).

### FAIR Adoption Insights

Cross-paper comparison reveals:

1. **Publication Type Matters**
   - Journal articles: 4/15 to 14/15
   - Book chapters: 0/15 (minimal infrastructure expectations)
   - Software publications: 13/15 (high infrastructure expectations)

2. **Discipline Norms Diverge**
   - Ancient DNA: Data-centric, exemplary repository deposition (14/15)
   - Computational archaeology: Code-centric, GitHub sharing without archival (4/15)
   - Software engineering: Multi-component systems with documentation (13/15)

3. **Historical Evolution Non-Linear**
   - 2016 (0/15) → 2018 (13/15): Rapid adoption in software publication venues
   - 2018 (13/15) → 2024 (4/15): HASS computational papers lag behind software journals
   - 2023 Nature genomics (14/15): High-impact venues enforce standards

4. **PID Connectivity Ceiling**
   - Maximum observed: 3/6 (Ballsun-Stanton 2018)
   - Common: 1-2/6 (paper DOI + dataset accession)
   - Missing: Author ORCIDs (0/4 papers had complete author ORCIDs)
   - Missing: Project RAiDs, vocabulary PIDs (0/4 papers)

5. **Code vs Data FAIR Divergence**
   - High data FAIR doesn't imply code sharing (Penske 2023: 14/15 data, 0/15 code)
   - High code sharing doesn't imply data FAIR (Sobotkova 2024: code shared, 0/15 data)
   - Discipline norms drive this divergence

## Next Steps

### Immediate (This Session)

1. ✅ Complete Phase 1 findings documentation (this document)
2. ⏳ Update infrastructure prompt with immediate guidance additions
3. ⏳ Update reference guides (PID systems, FAIR principles)
4. ⏳ Mark Phase 1 testing complete in active-todo-list.md

### Phase 2 (Future Work)

1. Extend testing to 10+ papers (software creators vs users)
2. Finalise software documentation enhancement decision
3. Implement schema v2.6 with deferred enhancements
4. Test enhanced schema on same 4-paper corpus (validation)

## Conclusion

Pass 6 infrastructure extraction framework **validated as robust** for diverse archaeological publications. Prompt successfully navigates publication types, FAIR spectrum, and temporal range. Guidance gaps identified and addressable.

**Key finding:** Software documentation structure needed but requires broader evidence base. Immediate guidance updates can proceed. Schema enhancements deferred to Phase 2 pending extended testing.

**Status:** Phase 1 testing **complete**. Ready to proceed with immediate guidance updates.
