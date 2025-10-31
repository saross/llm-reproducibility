# ARCHIVED: Paper-Specific Extraction Plan

**Archive Date:** 2025-10-31
**Original Location:** extraction-system/EXTRACTION_PLAN_ROSS_BALLSUN_STANTON_2022.md
**Superseded By:** extraction-system/EXTRACTION_PLAN_UNIFIED_MODEL.md
**Archival Reason:** Consolidated into unified model for consistency across paper types

**Historical Value:** This plan demonstrates successful extraction for a methodological/theoretical paper with minimal empirical data. Key lessons incorporated into unified model:
- 4-5 section structure for short methodological papers (19 pages)
- Lower evidence counts (15-25 items - mainly citations/examples) but high claims (60-90 items - methodological arguments)
- Research designs distributed throughout (NOT concentrated in Methods section)
- Equal attention strategy CRITICAL for methodological papers (designs in Intro/Theory/Discussion)
- Systematic implicit argument search for practice assumptions

**Example Paper:** Ross & Ballsun-Stanton 2022 - Introducing Preregistration of Research Design to Archaeology (SocArXiv)

---

# Extraction Plan: ross-ballsun-stanton-2022

**Paper:** "Introducing Preregistration of Research Design to Archaeology" (Ross & Ballsun-Stanton, 2022)
**Authors:** Shawn A. Ross, Brian Ballsun-Stanton
**Type:** Book chapter, 19 pages (445KB)
**Publication:** SocArXiv preprint
**Challenge:** Methodological/theoretical argumentation paper with minimal empirical data

**Extraction Date:** 2025-10-31
**Schema Version:** 2.5
**Workflow Version:** 3.0.0 (7-pass with Pass 0 metadata)

---

## Paper Overview

This book chapter introduces the concept of preregistration to archaeological research, arguing for increased transparency and reproducibility through advance specification of research designs. The paper:

- Makes methodological/theoretical arguments about research practices
- Provides minimal empirical data (methodological argumentation focus)
- Likely contains research designs about transparency frameworks
- Expected to have fewer evidence items but substantial claims about methodology
- Tests extraction capability on theoretical/argumentative content

---

## Extraction Strategy

### Pre-Execution Requirements

**CRITICAL:** Research-assessor skill must be invoked at start and **kept invoked throughout all 7 passes**

### Chunking Strategy

**Word-length based chunking (consistent across Pass 1 and Pass 3):**
- Target: ~1000 words per section/chunk
- Maximum: 1500 words per chunk
- Range: 500-1500 words acceptable
- If section exceeds 1500 words: split using natural breaks (subsections, topic shifts, paragraphs)
- Document: Track word counts, split decisions, and rationale in extraction_notes

**Expected section structure (4-6 groups):**
1. Abstract + Introduction
2. Theoretical Framework / Background
3. Preregistration Argument / Case for Archaeology
4. Discussion / Implementation Considerations / Examples
5. Conclusion

### Section Coverage for RDMAP

**CRITICAL:** Equal attention to ALL sections, not just methods

**Research designs likely scattered throughout:**
- **Introduction:** Rationale for preregistration, strategic positioning
- **Theory/Background:** Transparency frameworks, open science designs
- **Argument sections:** Preregistration design elements, methodological frameworks
- **Discussion/Conclusion:** Reflections on research design decisions

**Common mistake:** Expecting RDMAP items concentrated in "Methods" section. This methodological paper will have designs distributed across all sections.

---

## Complete 7-Pass Workflow

### Pre-Flight: Initialisation

**Actions:**
1. Create output directory: `outputs/ross-ballsun-stanton-2022/`
2. Initialise blank extraction.json with schema v2.5 structure
3. Update input/queue.yaml:
   - Status: `pending` → `in_progress`
   - Checkpoint: "Pre-flight complete - extraction environment initialised"

**Duration:** 1-2 minutes

---

### Pass 0: Metadata Extraction

**Purpose:** Extract accurate bibliographic metadata from title page

**Input:** First 2-3 pages of PDF (title page, abstract, headers)

**Actions:**
1. Read title page with full author names and affiliations
2. Extract from PDF metadata/pdfinfo if available
3. Populate all 8 project_metadata fields:
   - paper_title (complete title)
   - authors (array of full names, not initials)
   - publication_year (integer)
   - journal (full citation with volume/issue/pages or "SocArXiv preprint")
   - doi (string or null)
   - paper_type (book chapter, methodological argument)
   - discipline (archaeology, research methodology)
   - research_context (1-2 sentence summary)

**Critical rules:**
- Use full author names: "Shawn A. Ross" not "S. A. Ross"
- Extract from title page ONLY (not acknowledgements)
- Set doi to null if not present (not empty string)
- publication_year must be integer (no quotes)

**Checkpoint:** "Pass 0 complete - metadata extracted (2 authors, SocArXiv)"

**Duration:** 2-3 minutes

**Proceeds to:** Pass 1 automatically

---

### Pass 1: Liberal Claims & Evidence Extraction

**Purpose:** Cast wide net extracting all potential evidence, claims, and implicit arguments

**Input:** Entire paper processed in 4-6 section groups (1000-word target chunks)

**Extraction approach:**
- **Liberal extraction:** 40-50% over-extraction expected
- **100% sourcing discipline:** Every item must have verbatim_quote
- **Equal attention to ALL sections:** Designs scatter throughout
- **Section-by-section:** Save to JSON after each section group

**Expected extraction profile for methodological paper:**
- **Evidence:** 15-25 items (fewer than empirical papers)
  - Literature citations supporting methodological claims
  - Examples from other studies
  - Historical precedents for preregistration
- **Claims:** 60-90 items (substantial methodological argumentation)
  - Arguments for preregistration benefits
  - Claims about archaeological practice
  - Assertions about transparency impacts
- **Implicit Arguments:** 15-30 items (assumptions about research practices)
  - Unstated assumptions about current practices
  - Logical implications of preregistration adoption
  - Bridging claims between transparency and quality

**Systematic implicit argument search REQUIRED for all core claims:**
- Type 1: Logical implications
- Type 2: Unstated assumptions
- Type 3: Bridging claims
- Type 4: Disciplinary assumptions

**Cross-referencing:**
- Link claims → supporting evidence
- Link implicit arguments → related claims
- Bidirectional consistency required

**Script pattern:** `pass1_section{N}_{description}.py` for each section group

**Checkpoint:** "Pass 1 complete - liberal extraction yielded {total} items ({evidence} evidence, {claims} claims, {implicit_arguments} implicit_arguments). All {section_count} sections extracted with 100% sourcing discipline."

**Duration:** 2-4 hours (methodological paper, less dense than empirical)

**Proceeds to:** Pass 2 automatically

---

### Pass 2: Rationalize Claims & Evidence

**Purpose:** Consolidate redundant/overlapping claims and evidence

**Input:** Entire extraction.json from Pass 1

**Approach:**
- **Conservative consolidation:** Target 15-20% reduction
- **Well-differentiated content:** May yield lower reduction (10-15%)
- **Whole-paper analysis:** Review all items together for redundancy

**Consolidation types:**
1. Merge overlapping claims (same conclusion, different angles)
2. Absorb restatements (later restatement merged into first instance)
3. Delete vague claims (uninformative general assertions)
4. Combine split evidence (related observations unified)

**Critical rules:**
- MUST update all cross-references when consolidating
- MUST preserve distinct methodological/technical claims
- Evidence consolidation minimal (preserve data granularity)
- Document rationale for each consolidation

**Target reduction:**
- Claims: 15-20% typical (may be lower if well-differentiated)
- Evidence: 0-5% (preserve granular data)
- Implicit Arguments: No reduction (already selective)

**Script pattern:** `pass2_rationalization.py`

**Checkpoint:** "Pass 2 complete - conservative rationalization reduced to {total} items ({evidence} evidence, {claims} claims, {implicit_arguments} implicit_arguments). {reduction_pct}% reduction appropriate for well-differentiated methodological paper."

**Duration:** 1-2 hours

**Proceeds to:** Pass 3 automatically

---

### Pass 3: Liberal RDMAP Extraction

**Purpose:** Extract research designs, methods, and protocols

**Input:** Entire paper using SAME section groups as Pass 1

**CRITICAL REQUIREMENTS:**
- **Use SAME section groups as Pass 1** (identical 4-6 section grouping)
- **Equal attention to ALL sections** (designs NOT concentrated in methods)
- **ESPECIALLY liberal with designs** (commonly under-extracted)

**Extraction approach:**
- **Liberal extraction:** 40-50% over-extraction expected
- **100% sourcing discipline:** Every explicit item must have verbatim_quote
- **Section-by-section:** Process each group, save after each

**RDMAP Hierarchy:**
- **Research Designs (WHY):** Strategic decisions (preregistration frameworks, transparency designs)
- **Methods (WHAT):** Analytical approaches (assessment methodologies, evaluation approaches)
- **Protocols (HOW):** Step-by-step procedures (preregistration procedures, reporting protocols)

**Expected extraction profile for methodological paper:**
- **Research Designs:** 4-6 items
  - Preregistration framework design
  - Transparency enhancement design
  - Archaeological adaptation design
  - Open science integration design
- **Methods:** 8-12 items
  - Assessment methodologies for transparency
  - Evaluation approaches for preregistration effectiveness
  - Comparison methods (archaeology vs other fields)
- **Protocols:** 10-20 items
  - Preregistration submission procedures
  - Reporting protocols for registered research
  - Template specification protocols

**Section coverage expectations:**
- **Introduction/Theory:** Research designs, conceptual frameworks (HIGH yield)
- **Argument sections:** Methods for assessment, protocols for implementation
- **Discussion/Conclusion:** Design reflections, methodological insights

**Target counts:**
- Research Designs: 3-6 items
- Methods: 8-15 items
- Protocols: 15-30 items
- Total RDMAP: 30-50 items

**Script pattern:** `pass3_rdmap_extraction_group{N}.py` for each section group

**Checkpoint:** "Pass 3 complete - liberal RDMAP extraction yielded {rdmap_total} items ({designs} research_designs, {methods} methods, {protocols} protocols). Used same {section_count} section groups as Pass 1 with equal attention to all sections."

**Duration:** 2-4 hours

**Proceeds to:** Pass 4 automatically

---

### Pass 4: Implicit RDMAP Extraction

**Purpose:** Identify mentioned-but-undocumented procedures

**Input:** Entire paper (whole-paper scan)

**Approach:**
- **Pattern recognition:** Scan for trigger phrases indicating undocumented procedures
- **Systematic documentation:** Record what's mentioned vs what's documented

**Common implicit RDMAP patterns for methodological papers:**
- "using preregistration templates" → Template specification protocol (implicit)
- "following standard procedures" → Procedure specification missing
- "assessed effectiveness" → Assessment methodology undocumented
- "compared with other fields" → Comparison methodology unspecified

**Implicit RDMAP fields:**
- status: "implicit" (not "explicit")
- trigger_text (not verbatim_quote)
- trigger_locations (page numbers of triggers)
- expected_information_missing (what should be documented)
- reconstruction_confidence (low/medium/high)

**Target implicit RDMAP:**
- 10-30% of total RDMAP
- Typical: 3-8 implicit protocols, 1-3 implicit methods, 0-1 implicit designs

**Script pattern:** `pass4_implicit_rdmap.py`

**Checkpoint:** "Pass 4 complete - implicit RDMAP extraction yielded {implicit_count} items ({implicit_protocols} protocols, {implicit_methods} methods, {implicit_designs} designs). Implicit RDMAP: {implicit_pct}% of total RDMAP."

**Duration:** 1-2 hours

**Proceeds to:** Pass 5 automatically

---

### Pass 5: Rationalize RDMAP

**Purpose:** Consolidate redundant/overlapping RDMAP items

**Input:** Entire extraction.json from Passes 3-4

**Approach:**
- **Conservative consolidation:** Target 15-20% reduction
- **Preserve technical differentiation:** May yield lower reduction
- **Hierarchy awareness:** Update child_protocols/implements_method links

**Consolidation types:**
1. Merge overlapping methods (related analytical approaches)
2. Consolidate protocol sequences (sequential steps into comprehensive procedure)
3. Absorb redundant specifications (duplicate parameter descriptions)

**Critical rules:**
- MUST update RDMAP hierarchy links (implements_method, child_protocols)
- MUST preserve well-differentiated technical procedures
- Research designs rarely consolidate (already high-level)
- Document each consolidation with consolidation_note

**Target reduction:**
- Research Designs: 0-10% (usually 0%)
- Methods: 10-20%
- Protocols: 15-25%
- Total RDMAP: 15-20% overall

**Script pattern:** `pass5_rdmap_rationalization.py`

**Checkpoint:** "Pass 5 complete - conservative RDMAP rationalization reduced from {before} to {after} items ({reduction_pct}% reduction). Final RDMAP: {designs} designs, {methods} methods, {protocols} protocols."

**Duration:** 1-2 hours

**Proceeds to:** Pass 6 automatically

---

### Pass 6: Validation & Repair

**Purpose:** Comprehensive quality checks and integrity validation

**Input:** Entire extraction.json

**Validation checks:**

1. **Cross-Reference Integrity**
   - All claim→evidence references point to valid IDs
   - All evidence→claim references point to valid IDs
   - All implicit_argument→claim references point to valid IDs

2. **RDMAP Hierarchy Integrity**
   - All protocol→method references valid
   - All method→design references valid
   - No orphaned protocols or methods

3. **Metadata Completeness**
   - All 7 required project_metadata fields non-empty
   - Authors in full name format
   - DOI present or explicitly null
   - Journal includes volume/issue/pages or preprint designation

4. **Schema Compliance**
   - All required fields present
   - Status fields match sourcing (explicit vs implicit)
   - Page numbers present and valid

5. **Sourcing Completeness**
   - 100% of explicit items have non-empty verbatim_quote
   - 100% of implicit items have non-empty trigger_text
   - All quotes/triggers reference valid page numbers

6. **Page Number Validity**
   - All page numbers are positive integers
   - Page numbers within range for 19-page paper

**Validation status:**
- **PASS:** No critical or important issues
- **PASS_WITH_WARNINGS:** Minor issues only
- **WARN:** Important issues present
- **FAIL:** Critical issues (requires repair)

**Repair process:**
If critical issues found:
1. Create repair script: `pass6_repair_references.py`
2. Document broken references
3. Update cross-references to consolidated IDs
4. Re-run validation to confirm PASS

**Script pattern:** `pass6_validation.py` + `pass6_repair_references.py` (if needed)

**Checkpoint:** "Pass 6 complete - validation status: {status}. {issue_counts}. Total items validated: {total} ({explicit} explicit + {implicit} implicit)."

**Duration:** 30 minutes - 1 hour

**Proceeds to:** Summary generation automatically

---

### Post-Extraction: Generate summary.md

**Purpose:** Create human-readable summary of extraction

**Output:** `outputs/ross-ballsun-stanton-2022/summary.md`

**Content sections:**
1. Paper details (metadata from Pass 0)
2. Extraction overview (total counts, quality metrics)
3. Pass-by-pass summary (what was done in each pass)
4. Key methodological findings
5. Extraction characteristics (consolidation rates, implicit percentages)
6. Validation quality metrics
7. Files generated (all scripts and artifacts)

**Duration:** 15-30 minutes

---

### Post-Extraction: Update queue.yaml

**Purpose:** Mark paper as completed and document final statistics

**Changes:**
- Status: `pending` → `completed`
- Notes: "COMPLETED - 7-pass extraction with 100% sourcing completeness"
- Checkpoint: Final item counts and validation status

**Final checkpoint format:**
```yaml
checkpoint: "EXTRACTION COMPLETE - {total} total items ({evidence} evidence, {claims} claims, {implicit_arguments} implicit_arguments, {designs} research_designs, {methods} methods, {protocols} protocols). Validation: {status}. Implicit RDMAP: {implicit_pct}%. Rationalization: {pass2_pct}% claims, {pass5_pct}% RDMAP reductions. Methodological/theoretical paper successfully extracted."
```

**Duration:** 5 minutes

---

## Expected Outcomes

### Item Count Estimates

**Claims/Evidence Framework:**
- Evidence: 15-25 items (literature citations, examples)
- Claims: 60-90 items (methodological arguments)
- Implicit Arguments: 15-30 items (research practice assumptions)
- **Total:** 90-145 items

**RDMAP:**
- Research Designs: 4-6 items (preregistration frameworks)
- Methods: 8-12 items (assessment approaches)
- Protocols: 10-20 items (implementation procedures)
- **Total:** 22-38 items

**Grand Total:** 112-183 items (smaller than empirical papers due to methodological focus)

### Quality Metrics

**Sourcing Completeness:** 100% target
- All explicit items: verbatim_quote
- All implicit items: trigger_text

**Implicit RDMAP Percentage:** 10-30%
- Higher percentage may indicate lower transparency about methodological recommendations

**Rationalization Percentages:**
- Pass 2 (Claims/Evidence): 10-20% reduction
- Pass 5 (RDMAP): 10-20% reduction
- May be lower if well-differentiated content

**Validation Status:** PASS or PASS_WITH_WARNINGS required

---

## Methodological Paper Considerations

### Characteristics

1. **Evidence types different from empirical papers:**
   - Literature citations supporting arguments
   - Examples from other studies/fields
   - Historical precedents
   - Case studies of preregistration use

2. **Claims focus on practices, not findings:**
   - Arguments about research methodology
   - Assertions about transparency benefits
   - Claims about archaeological practice norms

3. **Research designs as conceptual frameworks:**
   - Preregistration framework design
   - Transparency enhancement strategies
   - Disciplinary adaptation designs

4. **Implicit arguments about current practices:**
   - Assumptions about existing archaeological practice
   - Unstated assumptions about researcher behavior
   - Disciplinary norms taken for granted

### Extraction Adaptations

**Evidence extraction:**
- Focus on citations supporting methodological claims
- Examples from literature as evidence items
- Lower evidence count expected (15-25 vs 40-60)

**Claims extraction:**
- More claims about methodology than findings
- Prescriptive claims ("should do X") alongside descriptive
- Hierarchical argument structure for transparency benefits

**RDMAP extraction:**
- Research designs scattered throughout (not concentrated in methods)
- Methods focus on assessment/evaluation approaches
- Protocols may include recommended procedures for others

**Section attention:**
- Introduction: High research design yield
- Theory/Background: Frameworks and rationale
- Argument sections: Methods and protocols
- Discussion: Design reflections

---

## Quality Assurance Checklist

**Before considering extraction complete:**

- [ ] Research-assessor skill invoked and maintained throughout
- [ ] Pre-flight initialization completed
- [ ] Pass 0: Metadata extracted (8 fields populated)
- [ ] Pass 1: Claims/Evidence extracted (4-6 section groups, 1000-word chunks)
- [ ] Pass 1: Section word counts documented in extraction_notes
- [ ] Pass 1: Systematic implicit argument search completed
- [ ] Pass 2: Claims/Evidence rationalized (consolidation documented)
- [ ] Pass 3: RDMAP extracted using SAME sections as Pass 1
- [ ] Pass 3: Equal attention to ALL sections (not just methods)
- [ ] Pass 4: Implicit RDMAP extracted
- [ ] Pass 5: RDMAP rationalized (hierarchy links updated)
- [ ] Pass 6: Validation PASS or PASS_WITH_WARNINGS achieved
- [ ] Pass 6: All critical issues repaired
- [ ] Summary.md generated with comprehensive breakdown
- [ ] Queue.yaml updated to completed status
- [ ] All execution artifacts preserved

---

## Files Generated

**Extraction outputs:**
- `extraction.json` - Complete extraction (all passes)
- `summary.md` - Human-readable summary

**Pass 1 scripts:**
- `pass1_section1_abstract_intro.py`
- `pass1_section2_theory_framework.py`
- `pass1_section3_preregistration_argument.py`
- `pass1_section4_discussion.py`
- `pass1_section5_conclusion.py` (if needed)

**Pass 2 outputs:**
- `pass2_rationalization.py`
- `pass2_consolidation_analysis.py`
- `pass2_analysis_report.txt`

**Pass 3 scripts:**
- `pass3_rdmap_extraction_group1.py`
- `pass3_rdmap_extraction_group2.py`
- [etc., one per section group]

**Pass 4 outputs:**
- `pass4_implicit_rdmap.py`

**Pass 5 outputs:**
- `pass5_rdmap_analysis.py`
- `pass5_rdmap_rationalization.py`

**Pass 6 outputs:**
- `pass6_validation.py`
- `pass6_repair_references.py` (if needed)
- `validation_report.json`

---

## Execution Notes

**Autonomous execution mode:**
- No stopping between passes
- Continuous workflow from Pre-Flight through Post-Extraction
- Auto-compact may occur naturally (resume from queue.yaml checkpoint)

**Critical success factors:**
1. Research-assessor skill invoked and maintained
2. Word-length chunking discipline (1000-word target, 1500-word max)
3. SAME section groups for Pass 1 and Pass 3
4. Equal attention to ALL sections for RDMAP (not just methods)
5. 100% sourcing discipline throughout
6. Systematic implicit argument search (4-type checklist)
7. Conservative consolidation with cross-reference maintenance

**Common pitfalls to avoid:**
- ❌ Expecting RDMAP concentrated in methods section
- ❌ Under-extracting research designs from Introduction/Theory/Discussion
- ❌ Skipping systematic implicit argument search
- ❌ Breaking cross-references during consolidation
- ❌ Using Read with limit parameter before Write

---

**Plan Created:** 2025-10-31
**Ready for Execution:** Yes
**Estimated Total Duration:** 8-12 hours (continuous autonomous workflow)
