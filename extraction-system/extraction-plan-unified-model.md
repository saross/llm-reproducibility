# Unified Extraction Plan Model

**Version:** 1.1.0
**Date:** 2025-11-18
**Purpose:** Flexible planning template for 8-pass research extraction workflow across diverse paper types
**Disciplines:** HASS, environmental sciences, fieldwork-based research (archaeology, palaeoecology, ethnography, etc.)
**Schema:** v2.6 | **Workflow:** v4.0.0 (8-pass: 0-7)

---

## Overview

This unified model provides a flexible framework for planning extractions across diverse paper types while maintaining consistency in critical requirements. Use this as a planning guide, not a prescriptive template - adapt sections and strategies to the specific paper you're extracting.

**Key Principle:** Universal process with paper-specific adaptation

---

# Part 1: Universal Planning Checklist

## ✓ Pre-Planning Requirements

Before creating your extraction plan, complete this checklist:

- [ ] **Paper identified:** Read `input/queue.yaml` to get paper path, slug, status
- [ ] **Paper assessed:** Examine PDF for length, structure, type, complexity
- [ ] **Skill preparation:** Ready to invoke `research-assessor` at Pre-Flight start
- [ ] **Model reviewed:** Read this unified model for guidance
- [ ] **Workflow understood:** Familiarise with `input/WORKFLOW.md` 8-pass structure

## ✓ Mandatory Plan Components

Every extraction plan MUST include all of the following:

### 1. Skill Invocation
- [ ] **Invoke research-assessor skill at start of Pre-Flight**
- [ ] **Keep skill invoked throughout ALL 8 passes**
- [ ] **Never proceed without this skill active**

**Why critical:** Skill provides extraction guidance, pattern recognition, quality checks

### 2. Section Structure Definition (Pass 1 AND Pass 3)
- [ ] Define section groups ONCE (will be used for BOTH Pass 1 and Pass 3)
- [ ] Target: ~1000 words per section
- [ ] Maximum: 1500 words per section (hard limit - must split if exceeded)
- [ ] List ALL sections with:
  - Section number and descriptive title
  - Page range
  - Estimated word count
  - Content summary (what topics/methods/results covered)
  - Natural boundary location (where section ends)

**Why critical:** Consistent sectioning prevents under-extraction from long sections

### 3. Explicit Chunking Examples
- [ ] Show actual section splits with word counts
- [ ] Document chunking rationale when splitting oversized sections
- [ ] Example format: "Section 2: Methods Part 1 (pp. 5-7, ~1100 words) - DNA extraction through library prep. [Natural break at subsection 2.2 boundary]"

**Why critical:** Makes chunking strategy explicit, enables validation

### 4. Liberal Over-Extraction Approach
- [ ] **Pass 1 (Claims/Evidence):** State "40-50% over-extraction expected"
- [ ] **Pass 3 (RDMAP):** State "40-50% over-extraction expected"
- [ ] **Especially liberal with research designs** (commonly under-extracted)

**Why critical:** Ensures comprehensive capture, avoids conservative under-extraction

### 5. Pass 3 Equal Attention Strategy
- [ ] Explicitly state: "Equal attention to ALL sections (not just Methods)"
- [ ] Note where research designs appear: Introduction, Theory, Methods, Discussion, Conclusions
- [ ] Warn against over-focusing on Methods section

**Why critical:** Research designs scattered throughout paper, over-focus on Methods causes under-extraction

### 6. Chunking Metadata Recording
- [ ] Plan to document word counts for each section
- [ ] Plan to record split decisions and rationale
- [ ] Plan to track natural boundaries used
- [ ] Include in extraction_notes.section_extracted

**Why critical:** Enables prompt refinement, extraction performance analysis

---

# Part 2: Paper Analysis Framework

## Critical Principle: Always Run All 8 Passes

**All papers receive all 8 passes (0-7), regardless of paper type.**

Paper type classification informs *how you adapt* each pass (item count expectations, section attention strategy, consolidation targets), NOT which passes to run.

**Why:** Initial assumptions about pass utility have proven incorrect. For example, methodological papers were assumed to need minimal RDMAP extraction, but empirical testing showed:
- Pass 2 consolidation achieved 28% reduction (meaningful rationalization)
- RDMAP extraction captured the research contribution (software development, testing, evaluation procedures)
- Implicit RDMAP items exposed methodological opacity (unstated tracking/comparison methods)

**Approach:** Gather empirical evidence using the full pipeline before making workflow adjustments for any paper type.

## Step 1: Identify Paper Type

**Empirical/Data-Rich Papers:**
- Original research with primary data collection
- Quantitative measurements, observations, datasets
- Methods section with detailed protocols
- Examples: Archaeological excavations, palaeoecological studies, genetic analyses
- **Extraction profile:** High evidence counts, moderate-high claims, substantial RDMAP

**Methodological/Theoretical Papers:**
- Arguments about research practices or theory
- Literature synthesis, framework development
- Minimal primary empirical data
- Examples: Method introductions, theoretical frameworks, reviews
- **Extraction profile:** Lower evidence (citations/examples), high claims, scattered RDMAP

**Mixed/Interdisciplinary Papers:**
- Combine multiple approaches (e.g., palaeoecology + archaeology)
- Multiple proxy methods integrated
- Complex analytical workflows
- Examples: Multi-proxy reconstructions, integrated syntheses
- **Extraction profile:** High evidence (multi-source), high claims, extensive RDMAP hierarchy

## Step 2: Assess Length and Complexity

**Short papers (<15 pages):**
- Typical sections: 4-6 section groups
- Timeline: 8-12 hours total
- May combine Results+Discussion

**Medium papers (15-25 pages):**
- Typical sections: 6-9 section groups
- Timeline: 12-18 hours total
- Standard structure: Abstract, Intro, Methods, Results, Discussion, Conclusion

**Long papers (>25 pages):**
- Typical sections: 9-15 section groups
- Timeline: 18-25 hours total
- Methods and Discussion likely need subdivision

**Complexity factors:**
- Statistical methods (DCA, cluster analysis, Bayesian modelling)
- Multiple analytical techniques (multi-proxy)
- Regional syntheses (multiple datasets integrated)
- Interdisciplinary integration (archaeology+palaeoenvironment)

## Step 3: Estimate Item Counts

Use these ranges as guidelines, adapt based on paper characteristics:

**Empirical Papers:**
- Evidence: 30-80 items (measurements, observations, dates, datasets)
- Claims: 60-120 items (interpretations, conclusions)
- Implicit Arguments: 10-35 items (assumptions, logical bridges)
- Research Designs: 3-8 items
- Methods: 8-20 items
- Protocols: 15-40 items

**Methodological Papers:**
- Evidence: 10-30 items (citations, examples from literature)
- Claims: 50-100 items (methodological arguments)
- Implicit Arguments: 15-40 items (practice assumptions)
- Research Designs: 3-6 items (frameworks, designs)
- Methods: 6-15 items (assessment approaches)
- Protocols: 8-25 items (procedures, templates)

**Mixed/Interdisciplinary Papers:**
- Evidence: 50-120 items (multi-proxy data)
- Claims: 80-150 items (integrated interpretations)
- Implicit Arguments: 15-40 items
- Research Designs: 5-10 items (multi-method integration)
- Methods: 15-35 items (multiple analytical approaches)
- Protocols: 25-60 items (detailed procedures for each method)

---

# Part 3: Section Structure Planning Guide

## Default Chunking Strategy

**Target:** ~1000 words per section
**Range:** 500-1500 words acceptable
**Hard maximum:** 1500 words (MUST split if exceeded)

## Default Section Grouping Pattern

### Standard Research Paper (6-8 sections):

1. **Section 1: Abstract + Introduction** (~800-1200 words)
   - Research questions, background, objectives
   - Natural break: Before Methods section

2. **Section 2-N: Middle Sections** (~1000-1300 words each)
   - Methods (may need 2-3 sections if long)
   - Results (may need 2-3 sections if long)
   - Each section saved to JSON after processing

3. **Section N+1: Discussion + Conclusion** (~900-1200 words)
   - Interpretations, implications, future directions
   - Natural break: End of paper

### Methods Section Subdivision (if >1500 words):

Split at natural subsection boundaries:
- Methods Part 1: Field procedures, sampling (pp. X-Y, ~1100 words)
- Methods Part 2: Laboratory analyses (pp. Y-Z, ~1200 words)
- Methods Part 3: Statistical analyses, modelling (pp. Z-A, ~1000 words)

### Discussion Section Subdivision (if >1500 words):

Split at conceptual/thematic boundaries:
- Discussion Part 1: Environmental interpretations (pp. X-Y, ~1300 words)
- Discussion Part 2: Human impacts and synthesis (pp. Y-Z, ~1100 words)

## Chunking Examples by Paper Type

### Example 1: Short Methodological Paper (19 pages)

**Structure:** 4-5 section groups

1. Section 1: Abstract + Introduction (pp. 1-5, ~1200 words)
2. Section 2: Theoretical Framework (pp. 5-10, ~1400 words)
3. Section 3: Preregistration Argument (pp. 10-15, ~1300 words)
4. Section 4: Discussion + Implementation (pp. 15-18, ~1100 words)
5. Section 5: Conclusion (pp. 18-19, ~400 words) - combine with Section 4 if too short

### Example 2: Long Multi-Proxy Paper (44 pages)

**Structure:** 11-13 section groups

1. Section 1: Abstract (p. 3, ~200 words)
2. Section 2: Introduction (pp. 3-5, ~1000 words)
3. Section 3: Methods Part 1 - Field + Laboratory (pp. 5-7, ~1100 words)
4. Section 4: Methods Part 2 - Analytical Techniques (pp. 7-9, ~1200 words)
5. Section 5: Results Part 1 - Proxy A Data (pp. 9-12, ~1400 words)
6. Section 6: Results Part 2 - Proxy B Data (pp. 12-15, ~1300 words)
7. Section 7: Discussion Part 1 - Environmental History (pp. 15-18, ~1300 words)
8. Section 8: Discussion Part 2 - Climate Drivers (pp. 18-21, ~1200 words)
9. Section 9: Discussion Part 3 - Human Impacts (pp. 21-24, ~1100 words)
10. Section 10: Regional Synthesis (pp. 24-27, ~1500 words)
11. Section 11: Discussion Part 4 - Archaeological Implications (pp. 27-29, ~900 words)
12. Section 12: Conclusions (p. 29, ~300 words)

[Note: Original Discussion was ~6500 words, split into 5 sections at natural subsection boundaries]

### Example 3: Standard Empirical Paper (23 pages)

**Structure:** 6-7 section groups

1. Section 1: Abstract + Introduction (pp. 1-4, ~1300 words)
2. Section 2: Methods (pp. 5-9, ~1400 words)
3. Section 3: Results Part 1 - Genetic Data (pp. 9-13, ~1300 words)
4. Section 4: Results Part 2 - Archaeological Context (pp. 13-17, ~1200 words)
5. Section 5: Discussion (pp. 17-21, ~1400 words)
6. Section 6: Conclusion (pp. 21-23, ~600 words)

## Papers Without Formal Sections

**Strategy:** Use paragraph/thematic boundaries

1. Count approximate words in paper (pages × 500 words/page rough estimate)
2. Divide into ~1000-word chunks
3. Find paragraph boundaries closest to chunk divisions
4. Extract and document: "Chunk 1 (pp. 1-3, ~1000 words) - Intro through early methodology discussion [Break at paragraph boundary before experimental design]"

## Documenting Chunking Metadata

**Template for extraction_notes.section_extracted:**

```json
{
  "section_number": 3,
  "section_title": "Methods Part 1 - Field and Laboratory Procedures",
  "page_range": "5-7",
  "estimated_words": 1100,
  "actual_words": 1087,
  "natural_boundary": "End of subsection 2.2 (Laboratory Analyses), before subsection 2.3 (Statistical Analyses)",
  "split_rationale": "Original Methods section was ~3200 words (pp. 5-11), exceeded 1500 word limit. Split into 3 roughly equal parts at subsection boundaries.",
  "items_extracted": {
    "evidence": 12,
    "claims": 8,
    "implicit_arguments": 2
  }
}
```

---

# Part 4: Pass-by-Pass Planning Template

## Pre-Flight: Initialisation (1-2 min)

**Checklist:**
1. **Invoke research-assessor skill** (CRITICAL - do not proceed without this)
2. Check queue: Read `input/queue.yaml` → identify paper with `status: pending`
3. Verify paper exists at specified path
4. Create output directory: `outputs/{paper-slug}/`
5. Initialise extraction.json with blank schema v2.6
6. Update queue.yaml: Set status to `in_progress`, add checkpoint

**Output:**
- outputs/{slug}/extraction.json (blank schema)
- Updated input/queue.yaml

**Checkpoint:** "Pre-flight complete - extraction environment initialised"

---

## Pass 0: Metadata Extraction (2-3 min)

**Objective:** Extract accurate bibliographic metadata from title page

**Input:** First 2-3 pages of PDF (title page, abstract, headers)

**Extract 8 fields:**
1. paper_title (complete title from title page)
2. authors (array of FULL names, not initials)
3. publication_year (integer, no quotes)
4. journal (full citation with volume/issue/pages OR "SocArXiv preprint")
5. doi (string or null if not present)
6. paper_type (research article, book chapter, methods paper, review, etc.)
7. discipline (primary discipline - archaeology, palaeoecology, ethnography, etc.)
8. research_context (1-2 sentence summary of research topic/location)

**Critical rules:**
- Use FULL author names: "Shawn A. Ross" NOT "S. A. Ross"
- Extract from title page ONLY (not acknowledgements)
- Set doi to null if not present (not empty string)
- publication_year must be integer
- Journal field must include volume/issue/pages where available

**Validation:**
- All 7 required fields non-empty (doi can be null)
- Authors array has ≥1 author
- No periods at end of author names (except middle initials)
- research_context is 1-2 complete sentences

**Checkpoint:** "Pass 0 complete - metadata extracted ({author_count} authors, {journal})"

---

## Pass 1: Liberal Claims & Evidence Extraction (2-7 hours)

### Planning Requirements for Pass 1

**Section structure (CRITICAL):**
- [ ] List ALL section groups (these SAME sections will be used in Pass 3)
- [ ] Show word counts for each section
- [ ] Document split decisions for any section >1500 words
- [ ] Plan to save to extraction.json after EACH section group

**Approach statement (MUST include):**
```
**Approach:** Liberal extraction - cast wide net, aim for 40-50% over-extraction.
Extract every potential claim, evidence item, and implicit argument. Items will be
consolidated in Pass 2. Better to over-extract than miss items.
```

**Item targets (adapt based on paper type):**
- Evidence: 30-80 items (empirical) OR 10-30 items (methodological)
- Claims: 60-120 items (empirical) OR 50-100 items (methodological)
- Implicit Arguments: 10-35 items (adapt based on complexity)

**100% Sourcing Discipline:**
- EVERY item MUST have verbatim_quote
- EVERY item MUST have page number
- Cross-reference claims → evidence via supporting_evidence array
- Cross-reference evidence → claims via supports_claims array

**Systematic implicit argument search REQUIRED:**
- Type 1: Logical implications (if X then Y, but Y unstated)
- Type 2: Unstated assumptions (assumes Z without stating Z)
- Type 3: Bridging claims (A→C requires B, but B not explicit)
- Type 4: Disciplinary assumptions (takes for granted community norms)

**Script naming pattern:**
- pass1_section1_{description}.py
- pass1_section2_{description}.py
- [One script per section group]

**Checkpoint:** "Pass 1 complete - liberal extraction yielded {total} items ({evidence} evidence, {claims} claims, {implicit_arguments} implicit_arguments). All {section_count} sections extracted with 100% sourcing discipline."

---

## Pass 2: Rationalize Claims & Evidence (1-3 hours)

### Planning Requirements for Pass 2

**Objective:** Conservative consolidation - reduce 15-20%

**Approach:** Whole-paper analysis
- Review ALL Pass 1 items together
- Identify redundancies, overlaps, vague claims
- Consolidate conservatively (preserve well-differentiated content)

**Consolidation types:**
1. Merge overlapping claims (same conclusion, different angles)
2. Absorb restatements (later restatement merged into first instance)
3. Delete vague claims (uninformative general assertions)
4. Combine split evidence (related observations unified)

**Critical rules:**
- MUST update all cross-references when consolidating
- MUST preserve distinct technical/methodological claims
- Evidence consolidation minimal (preserve data granularity)
- Document rationale in consolidation_note field

**Target reduction (adapt if paper is well-differentiated):**
- Claims: 15-20% reduction typical (may be 10-15% for technical papers)
- Evidence: 0-5% reduction (preserve granular data)
- Implicit Arguments: No reduction (already selective)

**Script pattern:** pass2_rationalization.py

**Checkpoint:** "Pass 2 complete - conservative rationalization reduced to {total} items ({evidence} evidence, {claims} claims, {implicit_arguments} implicit_arguments). {reduction_pct}% reduction appropriate for {paper_type}."

---

## Pass 3: Liberal RDMAP Extraction (2-6 hours)

### Planning Requirements for Pass 3

**CRITICAL REQUIREMENTS:**
- [ ] **Use SAME section groups as Pass 1** (no new grouping)
- [ ] **Equal attention to ALL sections** (explicitly state this)
- [ ] **ESPECIALLY liberal with research designs** (commonly under-extracted)

**Section coverage statement (MUST include):**
```
**Equal Attention Strategy:** Scan ALL sections with equal attention, not just Methods.
Research designs commonly appear in: Introduction (rationale), Theory (frameworks),
Methods (implementation), Discussion (reflection), Conclusions (insights).
Over-focusing on Methods causes systematic under-extraction of research designs.
```

**Approach statement (MUST include):**
```
**Approach:** Liberal extraction - cast wide net, aim for 40-50% over-extraction.
MIRROR Pass 1 liberal approach. Be ESPECIALLY liberal with research designs (commonly
under-extracted). Items will be consolidated in Pass 5. Better to over-extract than
miss RDMAP items.
```

**RDMAP Hierarchy (WHY → WHAT → HOW):**
- **Research Designs (WHY):** Strategic decisions about research framing
  - Examples: Multi-proxy integration design, comparative framework, temporal sampling strategy
- **Methods (WHAT):** Tactical analytical approaches
  - Examples: Pollen analysis, radiocarbon dating, statistical clustering
  - Link to designs via implements_design array
- **Protocols (HOW):** Operational step-by-step procedures
  - Examples: Pollen extraction procedure, calibration settings, sampling intervals
  - Link to methods via implements_method array

**Item targets (adapt based on paper type):**
- Research Designs: 3-8 items (be liberal - commonly under-extracted)
- Methods: 8-25 items (empirical/multi-proxy papers at high end)
- Protocols: 15-50 items (methods-heavy papers at high end)
- Total RDMAP: 30-70 items

**Where to find RDMAP by section:**
- **Introduction/Theory:** Research designs (40% of designs here), conceptual frameworks
- **Methods:** Methods and protocols (majority here), some research designs (30%)
- **Results:** Analytical methods, data processing protocols
- **Discussion/Conclusion:** Research designs (30% of designs here), methodological reflections

**Script pattern:**
- pass3_section1_rdmap.py
- pass3_section2_rdmap.py
- [One script per section group, SAME sections as Pass 1]

**Checkpoint:** "Pass 3 complete - liberal RDMAP extraction yielded {rdmap_total} items ({designs} research_designs, {methods} methods, {protocols} protocols). Used same {section_count} section groups as Pass 1 with equal attention to all sections."

---

## Pass 4: Implicit RDMAP Extraction (1-2 hours)

### Planning Requirements for Pass 4

**Objective:** Identify mentioned-but-undocumented procedures

**Approach:** Whole-paper scan using pattern recognition

**Common implicit RDMAP patterns:**
- "using X software" → Software specifications protocol (version/parameters missing)
- "trained personnel" → Training procedure protocol (training undefined)
- "standard procedures" → Procedure specification missing
- "data were analysed" → Analysis workflow method (steps undocumented)
- "following published protocols" → Which protocols? Citation insufficient

**Implicit RDMAP fields:**
- status: "implicit" (not "explicit")
- trigger_text (not verbatim_quote)
- trigger_locations (array of page numbers where triggers appear)
- expected_information_missing (array of what should be documented)
- reconstruction_confidence (low/medium/high)
- notes (explain the inference)

**Target implicit RDMAP:**
- 10-30% of total RDMAP should be implicit
- Higher percentage indicates lower transparency
- Typical: 5-15 implicit protocols, 1-4 implicit methods, 0-1 implicit designs

**Script pattern:** pass4_implicit_rdmap.py

**Checkpoint:** "Pass 4 complete - implicit RDMAP extraction yielded {implicit_count} items ({implicit_protocols} protocols, {implicit_methods} methods, {implicit_designs} designs). Implicit RDMAP: {implicit_pct}% of total RDMAP."

---

## Pass 5: Rationalize RDMAP (1-3 hours)

### Planning Requirements for Pass 5

**Objective:** Conservative consolidation - reduce 15-20%

**Approach:** Whole-paper analysis with hierarchy awareness

**Consolidation types:**
1. Merge overlapping methods (related analytical approaches combined)
2. Consolidate protocol sequences (sequential steps into comprehensive procedure)
3. Absorb redundant specifications (duplicate parameter descriptions removed)

**Critical rules:**
- MUST update RDMAP hierarchy links (implements_method, implements_design, child_protocols)
- MUST preserve well-differentiated technical procedures
- Research designs rarely consolidate (already high-level, 0-10% reduction)
- Document each consolidation with consolidation_note

**Target reduction (adapt for methods-heavy papers):**
- Research Designs: 0-10% (usually 0%)
- Methods: 10-20%
- Protocols: 15-25%
- Total RDMAP: 15-20% overall (may be 10-15% for methods papers)

**Script pattern:** pass5_rdmap_rationalization.py

**Checkpoint:** "Pass 5 complete - conservative RDMAP rationalization reduced from {before} to {after} items ({reduction_pct}% reduction). Final RDMAP: {designs} designs, {methods} methods, {protocols} protocols."

---

## Pass 6: Infrastructure Extraction (45-90 min)

### Planning Requirements for Pass 6

**Objective:** Extract reproducibility infrastructure and assess FAIR compliance

**Approach:** Systematic scan of entire paper with focus on front matter, back matter, and acknowledgements sections

**13 Infrastructure Sections to Extract:**

1. **Persistent Identifiers (PIDs)**
   - Paper DOI (from metadata)
   - Author ORCIDs (from title page, author list)
   - Data PIDs (DOIs, IGSNs from data availability statements)
   - Software PIDs (GitHub, Zenodo, CRAN from code availability)
   - Funding PIDs (RAiDs, CrossRef Funder IDs)
   - PID graph connectivity scoring (0-20 scale)

2. **Funding** - Grants, funding bodies, award numbers

3. **Data Availability** - Data sharing statements, repository URLs, access restrictions

4. **Code Availability** - Software/scripts sharing, GitHub links, computational environments

5. **Author Contributions** - CReDIT taxonomy roles (Conceptualization, Data curation, etc.)

6. **Conflicts of Interest** - Declarations of competing interests

7. **Ethics Approval** - IRB/ethics committee approvals, consent procedures

8. **Permits and Authorisations** - Research permits, access permissions, CARE principles compliance

9. **Preregistration** - Study preregistration (OSF, clinical trials registries)

10. **Supplementary Materials** - Supplementary files, appendices, online resources

11. **References Completeness** - Citation practices, data citations, software citations

12. **FAIR Assessment** - Findable, Accessible, Interoperable, Reusable (scored 0-40)

13. **Extraction Metadata** - Confidence levels, missing information flags

**FAIR Scoring Rubric (0-40 total):**

- **Findable (0-10):** PIDs, metadata richness, searchability
- **Accessible (0-10):** Data/code sharing, access protocols, licence clarity
- **Interoperable (0-10):** Standard formats, controlled vocabularies, integration potential
- **Reusable (0-10):** Licence clarity, provenance documentation, domain standards

**Critical Rules:**

- Extract ALL PIDs found (not just DOI)
- Assess PID graph connectivity (how PIDs link to each other)
- Apply CARE principles for Indigenous/community data (appropriate restrictions do NOT penalise FAIR scores)
- Document missing information explicitly (null vs not_mentioned vs not_applicable)
- Score FAIR dimensions independently (0-10 each)

**Where to Look:**

- **Front matter:** Title page (ORCIDs), acknowledgements (funding, permits)
- **Data availability section:** Data PIDs, sharing statements
- **Code/software section:** GitHub links, computational environments
- **Author contributions section:** CReDIT roles
- **Ethics section:** IRB approvals, consent
- **References:** Data citations, software citations
- **Supplementary materials section:** Additional resources

**Script pattern:** pass6_infrastructure.py

**Checkpoint:** "Pass 6 complete - infrastructure extraction populated 13 sections. FAIR score: {fair_total}/40 ({findable}F + {accessible}A + {interoperable}I + {reusable}R). PIDs: {pid_count} total ({paper_doi} + {orcid_count} ORCIDs + {data_pids} data + {software_pids} software + {other_pids} other). PID graph connectivity: {connectivity}/20."

---

## Pass 7: Validation (30-60 min)

### Planning Requirements for Pass 7

**Objective:** Comprehensive quality checks and integrity validation

**Validation checks:**

1. **Cross-Reference Integrity**
   - All claim→evidence references point to valid IDs
   - All evidence→claim references point to valid IDs
   - All implicit_argument→claim references point to valid IDs

2. **RDMAP Hierarchy Integrity**
   - All protocol→method references (implements_method) valid
   - All method→design references (implements_design) valid
   - No orphaned protocols (missing implements_method)
   - No orphaned methods (missing implements_design)

3. **Metadata Completeness**
   - All 8 required project_metadata fields non-empty
   - Authors in full name format (not initials)
   - DOI present or explicitly null
   - Journal includes volume/issue/pages

4. **Schema Compliance**
   - All required fields present for each item type
   - Status fields match sourcing (explicit vs implicit)
   - Page numbers present and valid

5. **Sourcing Completeness**
   - 100% of explicit items have non-empty verbatim_quote
   - 100% of implicit items have non-empty trigger_text
   - All quotes/triggers reference valid page numbers

6. **Page Number Validity**
   - All page numbers are positive integers
   - Page numbers within reasonable range for paper length

7. **Infrastructure Completeness**
   - reproducibility_infrastructure object present
   - FAIR assessment scores (0-40) calculated
   - PID graph connectivity assessed
   - All 13 infrastructure sections populated (null if not applicable)

**Validation status:**
- **PASS:** No critical or important issues
- **PASS_WITH_WARNINGS:** Minor issues only (acceptable)
- **WARN:** Important issues present (investigate)
- **FAIL:** Critical issues present (MUST repair before proceeding)

**Repair process (if FAIL):**
1. Create repair script: pass7_repair_references.py
2. Document broken references and repairs
3. Update cross-references to consolidated IDs
4. Re-run validation to confirm PASS status

**Script pattern:** pass7_validation.py + pass7_repair_references.py (if needed)

**Checkpoint:** "Pass 7 complete - validation status: {status}. {issue_counts}. Total items validated: {total} ({explicit} explicit + {implicit} implicit). Infrastructure: {infrastructure_sections} sections populated, FAIR score: {fair_score}/40."

---

## Post-Extraction: Generate summary.md (15-30 min)

**Purpose:** Create human-readable summary of extraction

**Output:** outputs/{slug}/summary.md

**Content sections:**
1. Paper details (metadata from Pass 0)
2. Extraction overview (total counts by category, quality metrics)
3. Pass-by-pass summary (what was done in each pass, key decisions)
4. Key findings and characteristics
5. Quality assessment:
   - Sourcing completeness (should be 100%)
   - Implicit RDMAP percentage
   - Rationalization percentages (Pass 2 and Pass 5)
   - Validation status
6. Challenges encountered and how resolved
7. Files generated (list all scripts and outputs)

---

## Post-Extraction: Update queue.yaml (5 min)

**Purpose:** Mark paper as completed, document final statistics

**Changes:**
- Status: `pending` → `completed`
- Notes: "COMPLETED - 8-pass extraction with 100% sourcing completeness"
- Checkpoint: Final item counts, validation status, and infrastructure metrics

**Final checkpoint format:**
```yaml
checkpoint: "EXTRACTION COMPLETE - {total} total items ({evidence} evidence, {claims} claims, {implicit_arguments} implicit_arguments, {designs} research_designs, {methods} methods, {protocols} protocols). Validation: {status}. Infrastructure: {infrastructure_sections} sections, FAIR {fair_score}/40. Implicit RDMAP: {implicit_pct}%. Rationalization: {pass2_pct}% claims, {pass5_pct}% RDMAP."
```

---

# Part 5: Adaptation Guidelines by Paper Type

## Empirical/Data-Rich Papers

**Characteristics:**
- Original research with primary data collection
- Quantitative measurements, observations, systematic datasets
- Detailed Methods section with protocols
- Examples: Archaeological excavations, palaeoecological cores, genetic analyses, surveys

**Extraction adaptations:**

**Pass 1 (Claims/Evidence):**
- High evidence counts expected (40-80 items)
- Evidence types: Measurements, dates, coordinates, sample counts, quantitative results
- Moderate-high claims (60-120 items)
- Focus on data-interpretation relationships

**Pass 3 (RDMAP):**
- Methods-heavy but still scan entire paper for designs
- Research designs in Introduction (study design rationale), Methods (implementation), Discussion (design reflection)
- High protocol counts (20-40 items) - detailed field/lab procedures
- Methods section may need 2-3 subdivisions if >3000 words

**Common mistakes:**
- Over-focusing on Methods in Pass 3 (still need designs from Intro/Discussion)
- Under-extracting implicit protocols (field procedures often under-documented)
- Missing research design rationale in Introduction

---

## Methodological/Theoretical Papers

**Characteristics:**
- Arguments about research practices, frameworks, or theory
- Literature synthesis, methodology introduction
- Minimal primary empirical data (citations as evidence)
- Examples: Method introductions, theoretical frameworks, critical reviews, disciplinary reflections

**Extraction adaptations:**

**Pass 1 (Claims/Evidence):**
- Lower evidence counts (10-30 items) - mostly citations and examples from literature
- Evidence types: Literature citations, case studies, historical examples
- High claims (50-100 items) - methodological arguments, prescriptive assertions
- Many implicit arguments (15-40 items) - assumptions about current practices

**Pass 3 (RDMAP):**
- Research designs distributed throughout (NOT concentrated in Methods)
- Introduction/Theory sections HIGH yield for designs (frameworks, rationales)
- Methods section may be minimal or absent
- Protocols may include recommended procedures for others to follow
- Equal attention strategy CRITICAL (designs scattered)

**Common mistakes:**
- Looking for Methods section that doesn't exist
- Under-extracting research designs from Introduction/Theory
- Missing implicit arguments about disciplinary norms

---

## Multi-Proxy/Interdisciplinary Papers

**Characteristics:**
- Combine multiple analytical approaches (e.g., pollen + charcoal + archaeology)
- Multiple datasets integrated into synthesis
- Complex statistical workflows (PCA, clustering, modelling)
- Examples: Integrated palaeoecology-archaeology, archaeogenetics + isotopes, multi-method syntheses

**Extraction adaptations:**

**Pass 1 (Claims/Evidence):**
- Very high evidence counts (60-120 items) - data from multiple proxies
- Need to track proxy type explicitly in item descriptions
- High claims (80-150 items) - integrated interpretations across proxies
- Complex cross-referencing (claims often draw on multiple evidence types)

**Pass 3 (RDMAP):**
- High design counts (5-10 items) - multi-proxy integration as design
- High method counts (15-35 items) - method for each proxy + integration methods
- Very high protocol counts (30-60 items) - protocols for each proxy method
- Hierarchy complexity (protocols → proxy methods → integration methods → overarching design)

**Common challenges:**
- Tracking which evidence items come from which proxy
- Capturing integration methods (how proxies combined) vs. individual proxy methods
- Managing complex RDMAP hierarchy with multiple branches

**Solutions:**
- Document proxy type in evidence item descriptions
- Extract integration methods separately from proxy-specific methods
- Use child_protocols arrays to track which protocols belong to which methods

---

## Short Papers (<15 pages)

**Characteristics:**
- Concise reporting, limited space for detail
- May lack formal sections or combine sections
- Examples: Short communications, letters, brief reports

**Extraction adaptations:**

**Section structure:**
- 4-6 section groups typical
- May need to combine multiple sections (e.g., Methods+Results, Discussion+Conclusion)
- Some sections may be <500 words (acceptable for short papers)

**Item counts:**
- Scale down expectations: Evidence 15-40, Claims 30-60, RDMAP 15-30
- Still apply liberal extraction, just less total content

**Timeline:**
- 8-12 hours total (faster than long papers)

---

## Long Papers (>25 pages)

**Characteristics:**
- Extensive reporting, multiple experiments/studies
- Detailed methods and results sections
- Examples: Major syntheses, multi-year studies, comprehensive reports

**Extraction adaptations:**

**Section structure:**
- 10-15 section groups typical
- Methods section likely needs 3-4 subdivisions
- Discussion section likely needs 3-5 subdivisions at thematic breaks
- Results may need subdivision by analysis type or study phase

**Item counts:**
- Scale up expectations: Evidence 80-150, Claims 120-200, RDMAP 50-100
- Liberal extraction yields more items to consolidate

**Timeline:**
- 18-25 hours total (longer duration)

**Chunking critical:**
- Must enforce 1500-word maximum strictly
- Document all splits with rationale
- Track natural boundaries carefully

---

# Part 6: Timeline Estimation Template

## Baseline Estimates by Paper Type

| Paper Type | Length | Sections | Timeline |
|------------|--------|----------|----------|
| Short methodological | <15 pages | 4-6 | 8-12 hours |
| Standard empirical | 15-25 pages | 6-9 | 12-18 hours |
| Long multi-proxy | >25 pages | 9-15 | 18-25 hours |
| Complex interdisciplinary | 20-40 pages | 10-14 | 20-28 hours |

## Pass Duration Breakdown

| Pass | Short Paper | Standard Paper | Long Paper |
|------|-------------|----------------|------------|
| Pre-Flight | 1-2 min | 1-2 min | 1-2 min |
| Pass 0: Metadata | 2-3 min | 2-3 min | 2-3 min |
| Pass 1: Claims/Evidence | 2-4 hours | 4-6 hours | 6-10 hours |
| Pass 2: Rationalize C/E | 1-1.5 hours | 1.5-2 hours | 2-3 hours |
| Pass 3: RDMAP Liberal | 2-3 hours | 3-5 hours | 5-8 hours |
| Pass 4: Implicit RDMAP | 1-1.5 hours | 1-2 hours | 1.5-2 hours |
| Pass 5: Rationalize RDMAP | 1-1.5 hours | 1.5-2 hours | 2-3 hours |
| Pass 6: Infrastructure | 45-60 min | 60-75 min | 75-90 min |
| Pass 7: Validation | 30-45 min | 45-60 min | 60-90 min |
| Summary generation | 15-20 min | 20-30 min | 30-45 min |
| **Total** | **9-13 hours** | **13-19 hours** | **19-27 hours** |

## Complexity Multipliers

Add time for:
- Statistical methods (DCA, Bayesian models): +10-20%
- Multi-proxy integration: +15-25%
- Regional synthesis (multiple datasets): +10-15%
- Poor documentation (high implicit %): +5-10%

---

# Part 7: Quality Criteria and Success Metrics

## Mandatory Quality Targets

### 1. Sourcing Completeness: 100%

**Definition:** All items have either verbatim_quote (explicit) or trigger_text (implicit)

**Validation:** Pass 7 checks sourcing completeness

**Failure condition:** Any item missing sourcing field

---

### 2. Implicit RDMAP Percentage: 10-30%

**Definition:** (Implicit RDMAP items / Total RDMAP items) × 100

**Interpretation:**
- <10%: High methodological transparency
- 10-20%: Good transparency
- 20-30%: Moderate transparency
- >30%: Lower transparency (many undocumented procedures)

**Note:** This is a paper characteristic, not an extraction quality issue

---

### 3. Rationalization Percentages

**Pass 2 (Claims/Evidence):**
- Target: 15-20% reduction
- Technical/well-differentiated papers: 10-15% acceptable
- <10%: May indicate under-extraction in Pass 1 OR genuinely distinct claims
- >25%: May indicate over-consolidation (review for lost distinctions)

**Pass 5 (RDMAP):**
- Target: 15-20% overall reduction
- Methods-heavy papers: 10-15% acceptable
- Research designs: Usually 0-10% (high-level items rarely consolidate)
- Protocols: Usually 15-25% (most consolidation happens here)

---

### 4. Cross-Reference Integrity

**Target:** PASS or PASS_WITH_WARNINGS

**Critical issues (MUST repair):**
- Broken claim→evidence references
- Broken evidence→claim references
- Broken RDMAP hierarchy links (implements_method, implements_design)

**Acceptable warnings:**
- Methods without child protocols (conceptual methods)
- Designs without implemented methods (aspirational/theoretical designs)
- Claims without evidence (theoretical/logical claims)

---

### 5. Chunking Compliance

**Target:** All sections ≤1500 words

**Validation:**
- Check extraction_notes.section_extracted for word counts
- Verify no section exceeds 1500 words
- Confirm split rationale documented for subdivided sections

---

## Validation Checklist

After completing extraction, verify:

- [ ] **Skill invocation:** research-assessor skill was invoked and maintained
- [ ] **Pass 0:** All 8 metadata fields populated correctly
- [ ] **Pass 1:** All sections extracted with documented word counts
- [ ] **Pass 1:** 100% sourcing completeness (all items have verbatim_quote)
- [ ] **Pass 2:** Consolidation documented, cross-references updated
- [ ] **Pass 3:** SAME sections as Pass 1, equal attention to all sections
- [ ] **Pass 3:** Research designs extracted from ALL sections (not just Methods)
- [ ] **Pass 4:** Implicit RDMAP percentage documented (10-30% range)
- [ ] **Pass 5:** RDMAP hierarchy links updated after consolidation
- [ ] **Pass 6:** Infrastructure extraction complete (13 sections populated)
- [ ] **Pass 6:** FAIR assessment scored (0-40), PID graph connectivity assessed
- [ ] **Pass 7:** Validation status PASS or PASS_WITH_WARNINGS
- [ ] **Pass 7:** All critical issues repaired
- [ ] **Summary:** summary.md generated with complete extraction report
- [ ] **Queue:** queue.yaml updated to completed status

---

# Part 8: Worked Examples (Condensed)

## Example 1: Standard Empirical Paper (Penske et al. 2023)

**Type:** Archaeogenetic research article (Nature)
**Length:** 23 pages (main text)
**Complexity:** High - population genetics, qpAdm modelling, IBD analysis

**Section Structure (9 sections, all <1500 words):**
1. Abstract + Introduction (pp. 1-2, ~1200 words)
2. Copper Age Background (p. 2, ~900 words)
3. Neolithic/CA Ancestries (pp. 2-3, ~1300 words)
4. Early Eneolithic Contacts (pp. 3-4, ~1400 words)
5. Bronze Age Ancestries (pp. 5-6, ~1300 words)
6. Discussion (pp. 6-7, ~1200 words)
7. Methods Part 1 - DNA Laboratory (p. 9, ~1100 words)
8. Methods Part 2 - Population Genetics (pp. 9-10, ~1200 words)
9. Methods Part 3 - Advanced Analysis (pp. 10-11, ~1000 words)

**Pass 1 Targets:** Evidence 40-70, Claims 70-110, Implicit Args 15-35
**Pass 3 Targets:** Designs 4-8, Methods 15-25, Protocols 25-40

**Timeline:** 15-20 hours total

**Key Adaptations:**
- Methods section split into 3 parts (originally ~3300 words)
- High RDMAP counts due to complex genetic workflows
- Research designs in Introduction (study rationale), Methods (implementation), Discussion (reflection)

---

## Example 2: Complex Multi-Proxy Paper (Connor et al. 2013)

**Type:** Palaeoecological reconstruction (Quaternary Science Reviews)
**Length:** 44 pages (main text)
**Complexity:** Very high - pollen, charcoal, magnetics, NPPs, statistical analyses, regional synthesis

**Section Structure (13 sections, all ≤1500 words):**
1. Abstract (p. 3, ~200 words)
2. Introduction (pp. 3-5, ~1000 words)
3. Methods Part 1 - Site + Sampling (pp. 5-7, ~1100 words)
4. Methods Part 2 - Numerical Analyses + Chronology (pp. 7-9, ~500 words) - combine with Part 1? Still under 1500
5. Results - Sediments + Magnetics + Pollen (pp. 9-13, ~1400 words)
6. Discussion - Intro + Cold Steppe (pp. 13-15, ~900 words)
7. Discussion - Semidesert Phase (pp. 15-17, ~1300 words)
8. Discussion - Forest-Steppe (pp. 17-20, ~1200 words)
9. Discussion - Oak Woods + Deforestation (pp. 20-22, ~1200 words)
10. Discussion - Regional Model (pp. 22-25, ~1500 words)
11. Discussion - Climate + Agriculture (pp. 25-27, ~850 words)
12. Discussion - Neolithic to Bronze Age (pp. 27-29, ~1200 words)
13. Conclusions (p. 29, ~250 words)

**Pass 1 Targets:** Evidence 110-135, Claims 185-220
**Pass 3 Targets:** Designs 8-12, Methods 35-45, Protocols 85-105

**Timeline:** 20-28 hours total

**Key Adaptations:**
- Discussion section originally ~6500 words, split into 7 sections at thematic breaks
- Very high RDMAP counts (multi-proxy, statistical methods, chronological modelling)
- Track proxy type for each evidence item
- Complex RDMAP hierarchy (protocols → proxy methods → integration methods → overarching design)

---

## Example 3: Methodological Paper (Ross & Ballsun-Stanton 2022)

**Type:** Book chapter, methodological argument
**Length:** 19 pages
**Complexity:** Moderate - theoretical/argumentative, minimal empirical data

**Section Structure (4-5 sections):**
1. Abstract + Introduction (pp. 1-5, ~1200 words)
2. Theoretical Framework (pp. 5-10, ~1400 words)
3. Preregistration Argument (pp. 10-15, ~1300 words)
4. Discussion + Implementation (pp. 15-18, ~1100 words)
5. Conclusion (pp. 18-19, ~400 words) - combine with Section 4

**Pass 1 Targets:** Evidence 15-25, Claims 60-90, Implicit Args 15-30
**Pass 3 Targets:** Designs 4-6, Methods 8-12, Protocols 10-20

**Timeline:** 8-12 hours total

**Key Adaptations:**
- Low evidence counts (citations, examples from literature)
- High claims (methodological arguments)
- Many implicit arguments (assumptions about current practices)
- Research designs scattered throughout (NOT concentrated in Methods section)
- Introduction/Theory HIGH yield for designs
- Equal attention strategy CRITICAL

---

# Part 9: Critical Success Factors Summary

## The Six Non-Negotiable Requirements

1. **✓ Research-assessor skill:** Invoke at Pre-Flight start, maintain throughout all 7 passes
2. **✓ Same sections Pass 1 and Pass 3:** Define once, reuse (typically 4-15 sections)
3. **✓ Word-length chunking:** Target 1000 words, max 1500 words, split if exceeded
4. **✓ Liberal over-extraction:** 40-50% over in Pass 1 and Pass 3 (especially research designs)
5. **✓ Equal attention Pass 3:** Scan ALL sections for RDMAP (not just Methods)
6. **✓ Chunking metadata:** Document word counts, splits, rationale in extraction_notes

## Common Planning Failures (Avoid These)

1. ❌ **Forgetting skill invocation** → Missing extraction guidance, lower quality
2. ❌ **Section-based instead of word-length chunking** → Systematic under-extraction from long sections
3. ❌ **Different sections Pass 1 vs Pass 3** → Inconsistent coverage, validation issues
4. ❌ **Over-focus on Methods (Pass 3)** → Under-extraction of research designs from Introduction/Discussion
5. ❌ **Not stating liberal approach** → Conservative extraction, missing items
6. ❌ **No chunking metadata** → Can't validate chunking compliance, can't improve

## Plan Quality Self-Check

Before considering plan complete, verify:

- [ ] All "Universal Planning Checklist" items included
- [ ] Paper type identified and adaptation strategy stated
- [ ] Section structure defined with word counts for ALL sections
- [ ] Same sections stated for Pass 1 AND Pass 3
- [ ] Liberal over-extraction approach stated for Pass 1 and Pass 3
- [ ] Equal attention strategy stated for Pass 3
- [ ] Chunking metadata recording plan included
- [ ] Item count targets adapted for paper type
- [ ] Timeline estimated based on length and complexity
- [ ] Quality criteria specified (sourcing, implicit %, rationalization %)

---

**Version:** 1.1.0 | **Date:** 2025-11-18
**Maintained by:** research-assessor skill
**Schema compatibility:** v2.6 | **Workflow version:** 4.0.0 (8-pass: 0-7)
**For questions:** Refer to input/WORKFLOW.md for complete process documentation
