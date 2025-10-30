# Research Extraction Workflow

## Overview

This document describes the 7-pass autonomous extraction workflow used to systematically extract research designs, methods, protocols, evidence, claims, and implicit arguments from research papers.

**Schema Version:** 2.5

**Workflow Version:** 3.0.0 (adds Pass 0 metadata extraction)

**Extraction Philosophy:**
- Liberal over-extraction followed by conservative rationalization
- 100% sourcing discipline (verbatim_quote or trigger_text for every item)
- Autonomous execution (no stopping between passes)
- Iterative refinement maintaining cross-reference integrity

## Workflow Stages

### Pre-Flight: Initialisation

**Purpose:** Prepare environment and initialise extraction schema

**Steps:**
1. Check queue: Read `input/queue.yaml` to identify next paper with `status: pending`
2. Verify paper exists: Confirm PDF exists at specified path
3. Create output directory: `outputs/{paper-slug}/`
4. Initialise schema: Create blank `extraction.json` with schema v2.5 structure
5. Update queue: Set paper status to `in_progress` with initial checkpoint

**Outputs:**
- `outputs/{paper-slug}/extraction.json` (blank schema)
- Updated `input/queue.yaml` (status: in_progress)

**Checkpoint:** "Pre-flight complete - extraction environment initialised"

**Duration:** 1-2 minutes

**Critical Rules:**
- Verify PDF is readable before proceeding
- Use exact paper slug from queue.yaml for directory name
- Create extraction.json with all required top-level keys

---

### Pass 0: Metadata Extraction

**Purpose:** Extract accurate bibliographic metadata from title page

**Input:** First 2-3 pages of PDF (title page, abstract, JSTOR header if present)

**Output:** Populated `project_metadata` object in extraction.json

**Prompt:** `extraction-system/prompts/00-metadata_pass0_prompt.md`

**Script Pattern:** `pass0_metadata_extraction.py`

**Extraction Strategy:**
- **Primary source:** Title page with full author names and affiliations
- **Secondary source:** JSTOR/repository header for journal citation
- **Validation:** Cross-check with pdfinfo metadata if available
- **Cross-check:** Verify consistency between title page, abstract, and headers

**Fields Extracted (8 total):**
1. `paper_title` - Complete title from title page
2. `authors` - Array of full author names (not initials)
3. `publication_year` - Integer year
4. `journal` - Full citation including volume, issue, pages
5. `doi` - DOI string or null
6. `paper_type` - Classification (research article, methods paper, review, etc.)
7. `discipline` - Primary discipline (archaeology, ethnography, etc.)
8. `research_context` - 1-2 sentence summary of research topic/location

**Critical Rules:**
- Extract from title page ONLY (not acknowledgements)
- Use full author names, not initials (e.g., "Shawn A. Ross" not "S. A. Ross")
- Use exact journal name as printed
- publication_year must be integer (no quotes)
- Include volume, issue, pages in journal field
- Set doi to null if not present (not empty string)

**Validation:**
- All 7 required fields non-empty (doi can be null)
- Authors array has at least one author
- No periods at end of author names (except middle initials)
- Journal includes volume and pages
- research_context is 1-2 complete sentences

**Checkpoint:** "Pass 0 complete - metadata extracted ({author count} authors, {journal})"

**Duration:** 2-3 minutes

**Proceeds to:** Pass 1 (no user confirmation)

---

### Pass 1: Liberal Claims & Evidence Extraction

**Purpose:** Cast wide net extracting all potential evidence, claims, and implicit arguments

**Input:** Entire paper, processed in section groups

**Output:** Evidence, claims, and implicit_arguments arrays populated

**Prompt:** `extraction-system/prompts/01-initial-extraction_pass1_prompt.md`

**Script Pattern:** `pass1_section{N}_{section-description}.py`

**Approach:**
- **Liberal extraction** - Over-extract 40-50% to capture all potential items
- **Section-by-section** - Process in 1500-word chunks with natural boundaries
- **100% sourcing** - Every item must have verbatim_quote

**Section Handling:**
- Define 4-8 section groups based on paper structure
- Common pattern: Abstract+Intro, Methods, Results, Discussion+Conclusion
- Technical papers: May split Methods into 2-3 groups
- Each section becomes one extraction script

**Target Counts:**
- Evidence: 30-60 items (quantitative measurements, observations, datasets)
- Claims: 60-100 items (interpretations, assertions, conclusions)
- Implicit Arguments: 10-30 items (unstated assumptions, logical leaps)

**Cross-Referencing:**
- Link claims to supporting evidence via `supporting_evidence` and `supports_claims` arrays
- Link implicit arguments to related claims via `related_claims` array

**Critical Rules:**
- MUST include verbatim_quote for every explicit item
- MUST include page number for every item
- Over-extraction is expected and encouraged
- Do not rationalize or consolidate during Pass 1
- Maintain chronological order within each section

**Checkpoint:** "Pass 1 complete - liberal extraction yielded {total} items ({evidence} evidence, {claims} claims, {implicit_arguments} implicit_arguments). All {section_count} sections extracted with 100% sourcing discipline."

**Duration:** 2-6 hours (depends on paper length and complexity)

**Proceeds to:** Pass 2

---

### Pass 2: Rationalize Claims & Evidence

**Purpose:** Consolidate redundant/overlapping claims and evidence

**Input:** Entire extraction.json from Pass 1

**Output:** Reduced claims and evidence counts with consolidation documentation

**Prompt:** `extraction-system/prompts/02-rationalization_pass2_prompt.md`

**Script Pattern:** `pass2_rationalization.py`

**Approach:**
- **Conservative consolidation** - Target 15-20% reduction
- **Well-differentiated papers** - May yield lower reduction (10-15%)
- **Whole-paper analysis** - Review all items together for redundancy

**Consolidation Types:**
1. **Merge overlapping claims** - Two claims asserting same conclusion from different angles
2. **Absorb restatements** - Later restatement of earlier claim merged into first instance
3. **Delete vague claims** - Uninformative general assertions removed
4. **Combine split evidence** - Related measurements or observations unified

**Consolidation Documentation:**
- Update `verbatim_quote` to encompass merged content
- Add `consolidation_note` field documenting the merge
- Update cross-references (supporting_evidence, supports_claims)

**Critical Rules:**
- MUST update all cross-references when consolidating
- MUST preserve distinct technical/methodological claims
- Evidence consolidation should be minimal (preserve data granularity)
- Document rationale for each consolidation in extraction_notes

**Target Reduction:**
- Claims: 15-20% reduction typical
- Evidence: 0-5% reduction (preserve granular data)
- Implicit Arguments: No reduction (already selective)

**Checkpoint:** "Pass 2 complete - conservative rationalization reduced to {total} items ({evidence} evidence, {claims} claims, {implicit_arguments} implicit_arguments). {reduction_pct}% claims reduction appropriate for well-differentiated {paper_type}."

**Duration:** 1-2 hours

**Proceeds to:** Pass 3

---

### Pass 3: Liberal RDMAP Extraction

**Purpose:** Extract research designs, methods, and protocols

**Input:** Entire paper, using SAME section groups as Pass 1

**Output:** research_designs, methods, and protocols arrays populated

**Prompt:** `extraction-system/prompts/03-rdmap_pass3_prompt.md`

**Script Pattern:** `pass3_rdmap_extraction.py`

**Approach:**
- **Liberal extraction** - Over-extract 40-50% to capture all potential RDMAP
- **SAME sections as Pass 1** - Use identical section groups, equal attention to all
- **ESPECIALLY liberal with designs** - Research designs commonly under-extracted

**RDMAP Hierarchy:**
- **Research Designs (WHY)** - High-level strategic approaches
  - Integrated multi-method design
  - Comparative evaluation design
  - Experimental control design
  - Iterative feedback design
- **Methods (WHAT)** - Analytical approaches and techniques
  - Links to designs via `implements_design`
  - Examples: Surface survey, remote sensing, quantitative analysis
- **Protocols (HOW)** - Specific step-by-step procedures
  - Links to methods via `implements_method`
  - Examples: Georeferencing procedure, band combination, sampling strategy

**Critical Rules:**
- Equal attention to ALL sections (not just Methods)
- Research designs found in Introduction, Methods, Discussion
- MUST include verbatim_quote for every explicit item
- MUST link protocols → methods → designs
- Over-extraction expected (rationalization in Pass 5)

**Target Counts:**
- Research Designs: 3-6 items
- Methods: 8-15 items
- Protocols: 15-30 items
- Total RDMAP: 30-50 items

**Section Coverage:**
- **Introduction/Theory:** Research designs, conceptual frameworks
- **Methods:** Methods and protocols (majority)
- **Results:** Analytical methods, data processing protocols
- **Discussion/Conclusion:** Research design reflections, methodological insights

**Checkpoint:** "Pass 3 complete - liberal RDMAP extraction yielded {rdmap_total} items ({designs} research_designs, {methods} methods, {protocols} protocols). Used same {section_count} section groups as Pass 1 with equal attention to all sections."

**Duration:** 2-4 hours

**Proceeds to:** Pass 4

---

### Pass 4: Implicit RDMAP Extraction

**Purpose:** Identify mentioned-but-undocumented procedures

**Input:** Entire paper (whole-paper scan)

**Output:** Implicit methods and protocols added to arrays

**Prompt:** `extraction-system/prompts/04-implicit-rdmap_pass4_prompt.md`

**Script Pattern:** `pass4_implicit_rdmap.py`

**Approach:**
- **Pattern recognition** - Scan for trigger phrases indicating undocumented procedures
- **Systematic documentation** - Record what's mentioned vs. what's documented

**Common Implicit RDMAP Patterns:**
- "using X software" → Software specifications protocol (IP001)
- "trained personnel" → Training procedure protocol (IP00X)
- "grab sample collected" → Sample processing protocol (IP00X)
- "features inventoried" → Recording procedure protocol (IP00X)
- "data were analysed" → Analysis workflow method (IM00X)

**Implicit RDMAP Fields:**
- `status: "implicit"` (vs. "explicit")
- `trigger_text` instead of verbatim_quote
- `expected_information_missing` array (what should be documented)
- `reconstruction_confidence` (low/medium/high)
- `notes` explaining the inference

**Critical Rules:**
- MUST use trigger_text (not verbatim_quote) for implicit items
- MUST set status: "implicit"
- MUST document expected_information_missing
- Conservative approach (only capture clear references)

**Target Implicit RDMAP:**
- 10-30% of total RDMAP
- Higher percentage indicates lower transparency
- Typical: 5-10 implicit protocols, 0-2 implicit methods

**Checkpoint:** "Pass 4 complete - implicit RDMAP extraction yielded {implicit_count} items ({implicit_protocols} protocols, {implicit_methods} methods). Implicit RDMAP: {implicit_pct}% of total RDMAP."

**Duration:** 1-2 hours

**Proceeds to:** Pass 5

---

### Pass 5: Rationalize RDMAP

**Purpose:** Consolidate redundant/overlapping RDMAP items

**Input:** Entire extraction.json from Passes 3-4

**Output:** Reduced RDMAP counts with consolidation documentation

**Prompt:** `extraction-system/prompts/05-rdmap-rationalization_pass5_prompt.md`

**Script Pattern:** `pass5_rdmap_rationalization.py`

**Approach:**
- **Conservative consolidation** - Target 15-20% reduction
- **Preserve technical differentiation** - Methods papers may yield lower reduction
- **Hierarchy awareness** - Update child_protocols/implements_method links

**Consolidation Types:**
1. **Merge overlapping methods** - Combine related analytical approaches
2. **Consolidate protocol sequences** - Merge sequential steps into comprehensive procedure
3. **Absorb redundant specifications** - Combine duplicate parameter descriptions

**Critical Rules:**
- MUST update RDMAP hierarchy links (implements_method, child_protocols)
- MUST preserve well-differentiated technical procedures
- Research designs rarely consolidate (already high-level)
- Document each consolidation with consolidation_note

**Target Reduction:**
- Research Designs: 0-10% (usually 0%)
- Methods: 10-20%
- Protocols: 15-25%
- Total RDMAP: 15-20% overall

**Checkpoint:** "Pass 5 complete - conservative RDMAP rationalization reduced from {before} to {after} items ({reduction_pct}% reduction). Final RDMAP: {designs} designs, {methods} methods, {protocols} protocols."

**Duration:** 1-2 hours

**Proceeds to:** Pass 6

---

### Pass 6: Validation & Repair

**Purpose:** Comprehensive quality checks and integrity validation

**Input:** Entire extraction.json

**Output:** Validation report and repaired cross-references if needed

**Prompt:** `extraction-system/prompts/06-validation_pass6_prompt.md`

**Script Pattern:** `pass6_validation.py` + `pass6_repair_references.py` (if needed)

**Validation Checks:**

**1. Cross-Reference Integrity**
- ✓ All claim→evidence references point to valid evidence IDs
- ✓ All evidence→claim references point to valid claim IDs
- ✓ All implicit_argument→claim references point to valid claim IDs

**2. RDMAP Hierarchy Integrity**
- ✓ All protocol→method references (implements_method) valid
- ✓ All method→design references (implements_design) valid
- ✓ No orphaned protocols (missing implements_method)
- ✓ No orphaned methods (missing implements_design)

**3. Metadata Completeness (NEW - Pass 0)**
- ✓ All 7 required project_metadata fields non-empty
- ✓ Authors in full name format (not initials)
- ✓ DOI present or explicitly null
- ✓ Journal includes volume/issue/pages

**4. Schema Compliance**
- ✓ All required fields present for each item type
- ✓ Status fields match sourcing (explicit vs implicit)
- ✓ Page numbers present and valid

**5. Sourcing Completeness**
- ✓ 100% of explicit items have non-empty verbatim_quote
- ✓ 100% of implicit items have non-empty trigger_text
- ✓ All quotes/triggers reference valid page numbers

**6. Page Number Validity**
- ✓ All page numbers are positive integers
- ✓ Page numbers within reasonable range for paper

**Validation Status:**
- **PASS:** No critical or important issues
- **PASS_WITH_WARNINGS:** Minor issues or warnings only
- **WARN:** Important issues present
- **FAIL:** Critical issues present (requires repair)

**Repair Process:**
If critical issues found:
1. Create repair script (e.g., `pass6_repair_references.py`)
2. Document broken references and repairs
3. Update cross-references to point to consolidated IDs
4. Re-run validation to confirm PASS status

**Critical Rules:**
- MUST achieve PASS or PASS_WITH_WARNINGS before proceeding
- MUST repair all critical cross-reference issues
- MUST document all repairs in extraction_notes
- Warnings are acceptable (e.g., methods without protocols)

**Checkpoint:** "Pass 6 complete - validation status: {status}. {issue_counts}. Total items validated: {total} ({explicit} explicit + {implicit} implicit)."

**Duration:** 30 minutes - 1 hour

**Proceeds to:** Summary generation

---

## Post-Extraction Tasks

### Generate summary.md

**Purpose:** Create human-readable summary of extraction

**Output:** `outputs/{slug}/summary.md`

**Content:**
1. Paper details (metadata from Pass 0)
2. Extraction overview (total counts, quality metrics)
3. Pass-by-pass summary (what was done in each pass)
4. Key findings and characteristics
5. Quality assessment (strengths, limitations, challenges)
6. Recommendations for replication
7. Files generated

**Duration:** 15-30 minutes

### Update queue.yaml

**Purpose:** Mark paper as completed and document final statistics

**Changes:**
- `status: pending` → `status: completed`
- Update notes with "COMPLETED - 7-pass extraction with 100% sourcing completeness"
- Update checkpoint with final item counts and validation status

**Final Checkpoint Format:**
```yaml
checkpoint: "EXTRACTION COMPLETE - {total} total items ({evidence} evidence, {claims} claims, {implicit_arguments} implicit_arguments, {designs} research_designs, {methods} methods, {protocols} protocols). Validation: {status}. Implicit RDMAP: {implicit_pct}%. Rationalization: {pass2_pct}% claims, {pass5_pct}% RDMAP reductions."
```

---

## File Safety Rules

### CRITICAL: Prevent Data Loss

**Always Read Full Files:**
- ✓ `Read(extraction.json)` with NO limit parameter
- ✓ Validate counts after every write
- ✗ NEVER use `Read(file, limit=N)` before `Write(file)`

**Validation After Every Write:**
```bash
# Verify file is valid JSON
jq . extraction.json > /dev/null

# Count items in each array
jq '{evidence: (.evidence | length), claims: (.claims | length), ...}' extraction.json
```

**Previous Data Loss Incident:**
- Using `Read(extraction.json, limit=100)` before Write
- Resulted in 367-line file truncated to 100 lines
- Lost 267 lines of extracted data
- Required complete re-extraction

---

## Autonomous Execution Mode

### Critical Rules

**NEVER ask:**
- "Would you like me to continue?"
- "Should I proceed to the next section?"
- "Shall I move to Pass X?"

**Continue automatically after:**
- Completing a section group
- Completing a pass
- Saving to extraction.json
- Updating queue.yaml
- Validation checks
- Any intermediate step

**ONLY stop if:**
- All 7 passes complete (extraction fully done)
- Critical error requires user intervention
- Structural problem with input files

### Session Behaviour

**Auto-compact handling:**
- Auto-compact will occur naturally during long extractions
- When resuming: Check queue.yaml checkpoint
- Resume from last checkpoint automatically
- Do not ask before resuming
- Do not summarize progress unnecessarily
- Treat entire workflow as single continuous job

---

## Quality Metrics

### Sourcing Completeness

**Target:** 100%

**Definition:** All items have either verbatim_quote (explicit) or trigger_text (implicit)

**Validation:** Pass 6 checks sourcing completeness

### Implicit RDMAP Percentage

**Typical Range:** 10-30%

**Definition:** (Implicit RDMAP items / Total RDMAP items) × 100

**Interpretation:**
- < 10%: High methodological transparency
- 10-20%: Good transparency
- 20-30%: Moderate transparency
- \> 30%: Lower transparency (many undocumented procedures)

### Rationalization Percentages

**Pass 2 (Claims/Evidence):**
- Target: 15-20% reduction
- Technical papers: May be 10-15% (well-differentiated content)
- Typical: 12-18% claims reduction, 0-5% evidence reduction

**Pass 5 (RDMAP):**
- Target: 15-20% reduction
- Methods papers: May be 5-10% (detailed technical procedures)
- Typical: 10-20% overall RDMAP reduction

### Cross-Reference Integrity

**Target:** PASS or PASS_WITH_WARNINGS

**Critical Issues:** Must be repaired
- Broken claim→evidence references
- Broken evidence→claim references
- Broken RDMAP hierarchy links

**Acceptable Warnings:**
- Methods without child protocols (conceptual methods)
- Designs without implementations (aspirational designs)

---

## Troubleshooting

### Common Issues

**Issue: Validation fails with broken references**

**Cause:** Pass 2 or Pass 5 consolidation didn't update all cross-references

**Solution:**
1. Create repair script mapping old IDs → new IDs
2. Update all references in evidence, implicit_arguments arrays
3. Re-run validation
4. Document repairs in extraction_notes

**Issue: Implicit RDMAP > 40%**

**Cause:** Paper has low methodological transparency

**Solution:**
- This is a characteristic of the paper, not an error
- Document in summary.md
- Include in assessment of replicability
- Consider if paper is suitable for extraction workflow

**Issue: Low rationalization percentages (< 10%)**

**Cause:** Liberal extraction wasn't liberal enough, OR paper has very distinct claims

**Solution:**
- Review Pass 1 and Pass 3 scripts for under-extraction
- Verify each claim/RDMAP item is truly distinct
- Accept lower reduction if content is genuinely well-differentiated
- Document rationale in extraction_notes

**Issue: Section groups unclear**

**Cause:** Paper has unusual structure (no clear Methods section, integrated results/discussion)

**Solution:**
- Define sections based on content, not headers
- Common patterns:
  - Theory papers: Abstract, Introduction, Theory/Framework, Case Studies, Conclusion
  - Mixed methods: Abstract, Intro, Quant Methods, Qual Methods, Results, Discussion
  - Book chapters: May lack abstract, combine intro/lit review
- Document section strategy in extraction_notes

---

## Version History

### v3.0.0 (2025-10-30)
- Added Pass 0: Metadata Extraction
- Added metadata completeness validation to Pass 6
- Updated workflow from 6 passes to 7 passes
- Added file safety rules documentation

### v2.7.0 (2025-10-29)
- Clarified autonomous execution rules
- Added RDMAP hierarchy documentation
- Updated section handling guidance
- Added troubleshooting section

### v2.5.0 (2025-10-25)
- Initial workflow documentation
- 6-pass structure (no metadata pass)
- Schema v2.5 compatibility

---

**Maintained by:** research-assessor skill

**Schema Compatibility:** v2.5

**Last Updated:** 2025-10-30
