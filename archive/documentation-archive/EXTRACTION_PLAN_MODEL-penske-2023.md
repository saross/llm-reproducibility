# ARCHIVED: Paper-Specific Extraction Plan

**Archive Date:** 2025-10-31
**Original Location:** extraction-system/EXTRACTION_PLAN_MODEL.md
**Superseded By:** extraction-system/EXTRACTION_PLAN_UNIFIED_MODEL.md
**Archival Reason:** Consolidated into unified model for consistency across paper types

**Historical Value:** This plan demonstrates successful extraction for a long empirical archaeogenetic paper with complex genetic methods. Key lessons incorporated into unified model:
- 9-section structure for 23-page papers with word-length chunking
- Methods section split into 3 parts (DNA Lab, Pop Genetics, Advanced Analysis)
- High RDMAP counts due to complex genetic workflows (designs 5-8, methods 15-25, protocols 25-40)
- Equal attention to all sections for research design extraction

**Example Paper:** Penske et al. 2023 - Early contact between late farming and pastoralist societies in southeastern Europe (Nature)

---

# Extraction Plan Model

**Version:** 1.0.0
**Date:** 2025-10-30
**Example:** Penske et al. 2023 archaeogenetic study
**Purpose:** Template for planning 7-pass research extraction workflow

---

## Planning Checklist

Before beginning extraction, create a detailed plan covering:

### ✓ Paper Analysis
- [ ] Paper title, type, size, complexity assessed
- [ ] Primary discipline and methodology identified
- [ ] Slug assigned (matches queue.yaml)

### ✓ Section Structure (CRITICAL)
- [ ] **Same sections for Pass 1 AND Pass 3**
- [ ] **Target:** ~1000 words per section
- [ ] **Maximum:** <1500 words per section (hard limit)
- [ ] Natural section boundaries identified
- [ ] All sections listed with:
  - Section number and title
  - Page range
  - Estimated word count
  - Content summary
  - Natural boundary location

### ✓ Chunking Strategy
- [ ] Sections split to enforce <1500 word maximum
- [ ] Natural breaks between major results/methods subsections
- [ ] Chunking metadata recording plan specified
- [ ] Methods section subdivided if >1500 words

### ✓ Extraction Targets
- [ ] Liberal over-extraction percentages (40-50%)
- [ ] Conservative rationalization percentages (15-20%)
- [ ] Expected item counts per category
- [ ] Research design extraction emphasis noted

### ✓ Autonomous Execution
- [ ] No stopping points between passes
- [ ] Checkpoint strategy for queue.yaml
- [ ] File save points after each pass
- [ ] Auto-resume strategy if session compacts

---

## Exemplary Plan: Penske et al. 2023

### Paper Overview
- **Title:** Early contact between late farming and pastoralist societies in southeastern Europe
- **Type:** Archaeogenetic research article (Nature)
- **Size:** 23 pages, 12.4MB
- **Complexity:** High - combines ancient DNA analysis, population genetics, archaeological synthesis
- **Slug:** penske-et-al-2023
- **Discipline:** Archaeogenetics

### Section Structure (9 sections, all <1500 words)

**CRITICAL: Same sections used for Pass 1 (claims/evidence) AND Pass 3 (RDMAP)**

1. **Section 1: Abstract + Introduction** (pages 1-2, ~1200 words)
   - Two genetic turnover events, research gap, study overview
   - **Natural break:** End of introduction paragraph

2. **Section 2: Copper Age Background** (page 2, ~900 words)
   - Fifth/fourth millennia changes, tell settlements, Varna, tell abandonment
   - **Natural break:** Before "Neolithic and Copper Age ancestries" results section

3. **Section 3: Neolithic and Copper Age Ancestries** (pages 2-3, ~1300 words)
   - PIE039, SEE CA individuals, PCA results, outgroup f3, qpAdm modelling
   - **Natural break:** Before "Early contacts during the Eneolithic"

4. **Section 4: Early Eneolithic Contacts** (pages 3-4, ~1400 words)
   - Ukraine Eneolithic cline, Kartal heterogeneity, Majaky/Usatove
   - **Natural break:** Before "Genetic ancestries during the Bronze Age"

5. **Section 5: Bronze Age Ancestries** (pages 5-6, ~1300 words)
   - YUN_EBA, PIE078, BOY_EBA, MAJ_EBA, Yamnaya comparisons, qpAdm modelling
   - **Natural break:** Before "Discussion"

6. **Section 6: Discussion** (pages 6-7, ~1200 words)
   - Genetic homogeneity, population transformations, early contact implications
   - **Natural break:** Before "Methods"

7. **Section 7: Methods Part 1 - DNA Laboratory** (page 9, ~1100 words)
   - Ancient DNA procedures, extraction, library preparation, sequencing
   - **Natural break:** Before "Sequence data processing"

8. **Section 8: Methods Part 2 - Population Genetics** (pages 9-10, ~1200 words)
   - Data processing, authentication, PCA, f-statistics, qpAdm
   - **Natural break:** Before "Imputation"

9. **Section 9: Methods Part 3 - Advanced Analysis** (pages 10-11, ~1000 words)
   - Imputation, ROH, IBD, DATES, pathogen screening
   - **Natural break:** End of methods

**Chunking Metadata Template:**
```json
{
  "section_number": 1,
  "section_title": "Abstract + Introduction",
  "page_range": "1-2",
  "estimated_words": 1200,
  "actual_words": 1187,
  "natural_boundary": "End of introduction paragraph",
  "items_extracted": {
    "evidence": 5,
    "claims": 12,
    "implicit_arguments": 2
  }
}
```

### Pass 0: Metadata Extraction (2-3 min)

**Objective:** Extract accurate bibliographic metadata from title page

**Outputs:**
- paper_title
- authors (30 in this case - Sandra Penske et al.)
- publication_year (2023)
- journal (Nature, Vol. 620, pp. 358-365)
- doi (10.1038/s41586-023-06334-8)
- paper_type (research article)
- discipline (archaeogenetics)
- research_context (1-2 sentence summary)

**Validation:**
- All 8 fields non-empty (doi can be null)
- Authors in full name format
- publication_year is integer
- Journal includes volume and pages

### Pass 1: Liberal Claims & Evidence (5-7 hours)

**Objective:** Cast wide net, over-extract 40-50%

**Section Processing:**
- Process all 9 sections sequentially
- Enforce <1500 word maximum per section
- Record chunking metadata for each section
- Extract liberally from each section

**Extraction Targets:**
- **Evidence:** 40-70 items (genetic data, radiocarbon dates, archaeological observations, Y/mtDNA lineages, IBD patterns, ROH)
- **Claims:** 70-110 items (ancestry interpretations, continuity/discontinuity, admixture narratives, contact assertions)
- **Implicit Arguments:** 15-35 items (identity assumptions, sampling assumptions, temporal resolution assumptions)

**100% Sourcing Discipline:**
- EVERY item MUST have verbatim_quote
- EVERY item MUST have page number
- Cross-reference claims → evidence via supporting_evidence array
- Cross-reference evidence → claims via supports_claims array

**Script Naming:**
- `pass1_section1_abstract-intro.py`
- `pass1_section2_background-ca.py`
- ... (9 scripts total)

### Pass 2: Rationalize Claims & Evidence (1.5-2 hours)

**Objective:** Conservative consolidation, reduce 15-20%

**Consolidation Types:**
- Merge overlapping claims
- Consolidate redundant evidence
- Absorb restatements
- Delete vague claims

**Expected Outputs:**
- Evidence: 30-50 (minimal reduction - preserve data granularity)
- Claims: 60-90 (15-20% reduction)
- Implicit Arguments: 15-35 (no reduction)

**Cross-Reference Integrity:**
- Update ALL supporting_evidence arrays after consolidation
- Update ALL supports_claims arrays after consolidation
- Document consolidations with consolidation_note field
- Add consolidation metadata to extraction_notes

### Pass 3: Liberal RDMAP Extraction (4-6 hours)

**Objective:** Extract research designs, methods, protocols - ESPECIALLY liberal with designs

**CRITICAL:** Use SAME 9 sections as Pass 1

**Extraction Targets (40-50% over-extraction):**

**Research Designs (5-8 items):**
- Multi-proxy archaeogenetic sampling design
- Temporal/spatial contact zone investigation
- Comparative population genetic design
- IBD-based relationship detection design
- Integrated genetic/archaeological synthesis design

**Methods (15-25 items):**
- Ancient DNA extraction and library preparation
- Target enrichment (1.24M SNP capture)
- PCA projection onto modern variation
- qpAdm ancestry modelling (distal and proximal)
- F-statistics (f3, f4 symmetry tests)
- DATES admixture dating
- hapROH parental relatedness analysis
- ancIBD identity-by-descent detection
- Y-chromosome haplogroup calling
- mtDNA haplogroup assignment
- Radiocarbon dating
- Genetic relatedness estimation
- Contamination estimation
- Imputation

**Protocols (25-40 items):**
- Petrous bone sampling protocol
- Tooth extraction protocol
- DNA extraction procedure
- UDG-half treatment
- Double indexing
- Shotgun sequencing specs
- 1.24M SNP capture protocol
- Read processing pipeline
- Adapter removal parameters
- Read mapping settings
- Duplicate removal
- Damage analysis
- Read trimming specifications
- Genotyping parameters
- Contamination estimation procedures
- Sex determination method
- PCA projection parameters
- qpAdm outgroup selection
- F-statistics computation
- DATES configuration
- hapROH thresholds
- GLIMPSE imputation workflow
- ancIBD block filtering
- Pathogen screening

**Hierarchy Linking:**
- Link protocols → methods via implements_method
- Link methods → designs via implements_design

**Equal Attention to All Sections:**
- Research designs appear in Introduction (rationale), Methods (implementation), Discussion (reflection)
- Scan ALL 9 sections, not just Methods
- Designs commonly under-extracted - cast wide net

**Script Naming:**
- `pass3_section1_rdmap.py`
- `pass3_section2_rdmap.py`
- ... (9 scripts total)

### Pass 4: Implicit RDMAP (1.5-2 hours)

**Objective:** Identify mentioned-but-undocumented procedures

**Scan Patterns:**
- "Data were analysed" without workflow
- Software mentioned without version/parameters
- "Standard procedures" without specification
- Analytical choices without justification
- "Following published protocols" without details

**Expected Outputs:**
- 5-12 implicit methods/protocols
- 15-25% of total RDMAP should be implicit
- Higher % indicates lower transparency

**Fields for Implicit Items:**
- status: "implicit"
- trigger_text (not verbatim_quote)
- expected_information_missing array
- reconstruction_confidence (low/medium/high)
- notes explaining inference

### Pass 5: Rationalize RDMAP (1.5-2 hours)

**Objective:** Conservative consolidation, reduce 15-20%

**Consolidation Types:**
- Merge overlapping methods
- Consolidate protocol sequences
- Absorb redundant specifications

**Expected Outputs:**
- Research Designs: 5-8 (0-10% reduction)
- Methods: 12-20 (10-20% reduction)
- Protocols: 20-32 (15-25% reduction)

**Hierarchy Verification:**
- Update implements_method arrays
- Update implements_design arrays
- Update child_protocols arrays
- Preserve technical differentiation (methods-heavy papers may have lower reduction)

### Pass 6: Validation & Repair (45-60 min)

**Validation Checks:**

1. **Cross-Reference Integrity:**
   - All claim→evidence references point to valid IDs
   - All evidence→claim references point to valid IDs
   - All implicit_argument→claim references valid

2. **RDMAP Hierarchy Integrity:**
   - All protocol→method references valid
   - All method→design references valid
   - No orphaned protocols/methods

3. **Metadata Completeness:**
   - All 8 project_metadata fields non-empty

4. **Schema Compliance:**
   - All required fields present for each item type
   - Status fields match sourcing (explicit vs implicit)

5. **Sourcing Completeness:**
   - 100% explicit items have verbatim_quote
   - 100% implicit items have trigger_text
   - All page numbers valid

6. **Chunking Metadata:**
   - All sections documented with metadata
   - All sections <1500 words verified

**Validation Status:**
- PASS: No critical issues
- PASS_WITH_WARNINGS: Minor issues only
- FAIL: Critical issues (requires repair)

**Repair Process:**
- Create repair script if FAIL
- Document broken references
- Update cross-references
- Re-run validation to achieve PASS

### Pass 7: Summary Generation (20-30 min)

**Objective:** Create human-readable summary

**Summary Contents:**
1. Paper details (from metadata)
2. Extraction overview (total counts, quality metrics)
3. Pass-by-pass summary with chunking details
4. Key findings and characteristics
5. Quality assessment (sourcing %, implicit RDMAP %, rationalization %)
6. Files generated list

**Quality Metrics to Report:**
- Sourcing completeness: 100%
- Implicit RDMAP percentage: 15-25%
- Pass 2 rationalization: 15-20%
- Pass 5 rationalization: 15-20%
- Validation status: PASS/PASS_WITH_WARNINGS
- Chunking compliance: All sections <1500 words

---

## Timeline Template

| Pass | Activity | Duration |
|------|----------|----------|
| 0 | Metadata extraction | 2-3 min |
| 1 | Liberal claims/evidence (9 sections) | 5-7 hours |
| 2 | Rationalize claims/evidence | 1.5-2 hours |
| 3 | Liberal RDMAP (9 sections) | 4-6 hours |
| 4 | Implicit RDMAP | 1.5-2 hours |
| 5 | Rationalize RDMAP | 1.5-2 hours |
| 6 | Validation & repair | 45-60 min |
| 7 | Summary generation | 20-30 min |
| **Total** | **Complete extraction** | **15-20 hours** |

---

## Files Generated Template

**Extraction outputs:**
1. `outputs/{slug}/extraction.json` (complete schema v2.5)
2. `outputs/{slug}/summary.md`

**Execution scripts:**
3. `pass0_metadata_extraction.py`
4-N. `pass1_section{1-N}_{description}.py` (N scripts for N sections)
N+1. `pass2_rationalization.py`
N+2-M. `pass3_section{1-N}_rdmap.py` (N scripts for N sections)
M+1. `pass4_implicit_rdmap.py`
M+2. `pass5_rdmap_rationalization.py`
M+3. `pass6_validation.py`
M+4. `pass6_repair_references.py` (if needed)

**Queue update:**
- Updated `input/queue.yaml` with completion status

---

## Critical Success Factors

### ✓ Chunking Compliance
- ALL sections <1500 words (hard limit)
- Natural boundaries between sections
- Metadata recorded for each section
- Same sections for Pass 1 AND Pass 3

### ✓ Liberal Extraction
- Pass 1: 40-50% over-extraction
- Pass 3: 40-50% over-extraction
- ESPECIALLY liberal with research designs (commonly under-extracted)
- Equal attention to ALL sections in Pass 3

### ✓ 100% Sourcing
- Every explicit item has verbatim_quote
- Every implicit item has trigger_text
- All items have page numbers
- No exceptions

### ✓ Autonomous Execution
- No stopping between passes
- Auto-save after each pass
- Auto-checkpoint to queue.yaml
- Auto-resume if session compacts

### ✓ Cross-Reference Integrity
- Bidirectional linking (claims↔evidence)
- RDMAP hierarchy (protocols→methods→designs)
- Updated after every consolidation
- Validated in Pass 6

---

## Adaptation Guidelines

### For Different Paper Types

**Short papers (<10 pages):**
- Fewer sections (4-6)
- Shorter timeline (8-12 hours)
- May combine Results+Discussion

**Long papers (>25 pages):**
- More sections (12-15)
- Longer timeline (20-25 hours)
- May split Methods into 4-5 sections

**Methods-heavy papers:**
- More RDMAP items expected
- Lower rationalization % acceptable (10-15%)
- More protocols than typical

**Theoretical papers:**
- More claims, fewer evidence items
- More implicit arguments
- Fewer protocols, more methods

**Field report papers:**
- More evidence (observations, measurements)
- More protocols (field procedures)
- Fewer implicit arguments

### Chunking Adjustment Strategies

**If section >1500 words:**
- Find mid-section natural break
- Split at paragraph boundary
- Never split mid-paragraph
- Aim for balanced section sizes

**If section <500 words:**
- Consider merging with adjacent section
- Ensure merge doesn't exceed 1500 words
- Maintain logical grouping

**Natural boundaries to look for:**
- Between major results sections
- Before/after Methods subsections
- Between Results and Discussion
- Between Introduction and Background

---

**Maintained by:** Claude Code research-assessor skill
**Schema compatibility:** v2.5
**Workflow version:** 3.0.0 (7-pass with Pass 0 metadata)
**Last updated:** 2025-10-30
