# Research Extraction Workflow

---

# PLANNING MODE REQUIREMENTS - READ THIS FIRST

When creating extraction plans in planning mode, you MUST include ALL of the following. These requirements address recurring issues where plans lack critical details.

## ✓ Mandatory Plan Components

### 1. Skill Invocation
- [ ] **Invoke research-assessor skill at start of Pre-Flight**
- [ ] **Keep skill invoked throughout ALL 8 passes**
- [ ] **Never proceed without this skill active**

**Why critical:** Skill provides extraction guidance, pattern recognition, and quality checks.

### 2. Section Structure Definition (Pass 1 AND Pass 3)
- [ ] Define section groups ONCE (will be used for BOTH Pass 1 and Pass 3)
- [ ] Target: ~1000 words per section
- [ ] Maximum: 1500 words per section (hard limit - MUST split if exceeded)
- [ ] List ALL sections with:
  - Section number and descriptive title
  - Page range
  - Estimated word count
  - Content summary (what topics/methods/results covered)
  - Natural boundary location (where section ends)

**Why critical:** Consistent sectioning prevents under-extraction from long sections.

### 3. Explicit Chunking Examples in Plan
- [ ] Show actual section splits with word counts
- [ ] Document chunking rationale when splitting oversized sections
- [ ] Example format: "Section 2: Methods Part 1 (pp. 5-7, ~1100 words) - DNA extraction through library prep. [Natural break at subsection 2.2 boundary]"

**Why critical:** Makes chunking strategy explicit, enables validation.

### 4. Liberal Over-Extraction Approach
- [ ] **Pass 1 (Claims/Evidence):** State "40-50% over-extraction expected"
- [ ] **Pass 3 (RDMAP):** State "40-50% over-extraction expected"
- [ ] **Especially liberal with research designs** (commonly under-extracted)

**Why critical:** Ensures comprehensive capture, avoids conservative under-extraction.

### 5. Pass 3 Equal Attention Strategy
- [ ] Explicitly state: "Equal attention to ALL sections (not just Methods)"
- [ ] Note where research designs appear: Introduction, Theory, Methods, Discussion, Conclusions
- [ ] Warn against over-focusing on Methods section

**Why critical:** Research designs scattered throughout paper; over-focus on Methods causes under-extraction.

### 6. Chunking Metadata Recording
- [ ] Plan to document word counts for each section
- [ ] Plan to record split decisions and rationale
- [ ] Plan to track natural boundaries used
- [ ] Include in extraction_notes.section_extracted

**Why critical:** Enables prompt refinement, extraction performance analysis.

### 7. Use Unified Model Plan
- [ ] Reference: `extraction-system/EXTRACTION_PLAN_UNIFIED_MODEL.md`
- [ ] Adapt guidelines for paper type (empirical/methodological/short/long/multi-proxy)

**Why critical:** Provides consistent planning framework adapted for diverse paper types.

---

# Common Planning Mistakes - AVOID THESE

## ❌ Mistake 1: Forgetting Skill Invocation
**Problem:** Proceeding without research-assessor skill
**Impact:** Missing extraction guidance, lower quality
**Fix:** First step of every plan: "Invoke research-assessor skill"

## ❌ Mistake 2: Section-Based Instead of Word-Length Chunking
**Problem:** "Process Introduction section" (but Introduction is 3000 words)
**Impact:** Systematic under-extraction from long sections
**Fix:** Always check word counts, split sections >1500 words

## ❌ Mistake 3: Different Sections for Pass 1 vs Pass 3
**Problem:** Creating new section groups for Pass 3
**Impact:** Inconsistent coverage, difficult to validate
**Fix:** Explicitly state "SAME sections as Pass 1" in Pass 3 plan

## ❌ Mistake 4: Over-Focus on Methods Section (Pass 3)
**Problem:** Spending 70% of Pass 3 time on Methods section
**Impact:** Under-extraction of research designs from Introduction/Discussion
**Fix:** Allocate equal time/attention to each section

## ❌ Mistake 5: Not Stating Liberal Approach
**Problem:** Plan says "Extract RDMAP items" without "liberal over-extraction"
**Impact:** Conservative extraction, missing items
**Fix:** Always explicitly state "40-50% over-extraction expected"

## ❌ Mistake 6: No Chunking Metadata
**Problem:** Not documenting word counts or split decisions
**Impact:** Can't validate chunking compliance, can't improve prompts
**Fix:** Include word counts and split rationale for every section

---

## Overview

This document describes the 8-pass autonomous extraction workflow used to systematically extract research designs, methods, protocols, evidence, claims, implicit arguments, and reproducibility infrastructure from research papers.

**Schema Version:** 2.6

**Workflow Version:** 5.0.0 (session-per-pass execution mode)

**Extraction Philosophy:**
- Liberal over-extraction followed by conservative rationalization
- 100% sourcing discipline (verbatim_quote or trigger_text for every item)
- Autonomous execution (no stopping between passes)
- Iterative refinement maintaining cross-reference integrity

---

## Session-per-Pass Execution Mode

### Why Session-per-Pass?

Run comparison (crema-et-al-2024) demonstrated session-per-pass yields significantly better extractions:
- +75% claims captured
- +100% research designs captured
- Better methodological reasoning and cross-references

### Session Structure

| Session | Passes | Focus | Stop After |
|---------|--------|-------|------------|
| **A** | Pre-Flight + Pass 0 + Pass 6 | Metadata + Infrastructure | ✅ Session A complete |
| **B** | Pass 1 + Phase 2b + Pass 2 | Claims/Evidence | ✅ Session B complete |
| **C** | Pass 3 + Pass 4 + Phase 5b + Pass 5 | RDMAP | ✅ Session C complete |
| **D** | Pass 7 + FAIR Assessment | Validation | ✅ Extraction complete |

### Within-Session Rules

**Within each session**, work autonomously:

- ✅ Complete all passes in the session without stopping
- ✅ Save to extraction.json after each pass
- ✅ Do not ask "Should I continue?" within a session
- ✅ Do not stop between section groups within a pass

**At session end**, provide handoff summary:

```text
Session [A/B/C/D] complete for {paper-slug}

Completed:
- Pass X: {summary}
- Pass Y: {summary}

Counts: {evidence}, {claims}, {research_designs}, {methods}, {protocols}

Next session: [B/C/D/Complete]
```

### Session Resumption

When starting a new session:

1. Read extraction.json → check `extraction_notes.passes_completed`
2. Read queue.yaml → verify paper status
3. Read paper text if needed for extraction passes
4. Continue from next incomplete session

**ONLY stop if:**
- Session complete (natural checkpoint)
- Critical error requires user intervention
- Structural problem with input files

---

## Workflow Stages

---

## 🅰️ SESSION A: Metadata + Infrastructure

---

### Pre-Flight: Initialisation

**Purpose:** Prepare environment and initialise extraction schema

**Steps:**
1. Check queue: Read `input/queue.yaml` to identify next paper with `status: pending`
2. Verify paper exists: Confirm PDF exists at specified path
3. Create output directory: `outputs/{paper-slug}/`
4. Initialise schema: Create blank `extraction.json` with schema v2.6 structure
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

**Proceeds to:** Pass 6 (infrastructure) within Session A

---

### Pass 6: Infrastructure Extraction

**Note:** Pass 6 is done in Session A alongside metadata for efficiency. See full Pass 6 documentation below.

**Proceeds to:** Session A handoff (stop after Pass 6)

---

## 🅱️ SESSION B: Claims & Evidence

---

### Pass 1: Liberal Claims & Evidence Extraction

**Purpose:** Cast wide net extracting all potential evidence, claims, and implicit arguments

### CRITICAL PLANNING REQUIREMENTS for Pass 1:
1. **Define section groups ONCE** (will reuse for Pass 3)
2. **Word-length chunking**: Target 1000 words, max 1500 words
3. **Liberal over-extraction**: 40-50% more than final target
4. **Chunking examples**: Show actual splits with word counts in plan
5. **Chunking metadata**: Plan to document word counts and split rationale
6. **100% sourcing discipline**: Every item requires verbatim_quote

**Input:** Entire paper, processed in section groups

**Output:** Evidence, claims, and implicit_arguments arrays populated

**Prompt:** `extraction-system/prompts/01-initial-extraction_pass1_prompt.md`

**Script Pattern:** `pass1_section{N}_{section-description}.py`

**Approach:**
- **Liberal extraction** - Over-extract 40-50% to capture all potential items
- **Section-by-section** - Process in ~1000-word chunks (max 1500 words) with natural boundaries
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

**Proceeds to:** Phase 2b (Bidirectional Mapping Reconciliation)

---

### Phase 2b: Bidirectional Mapping Reconciliation

**Purpose:** Validate and auto-correct bidirectional mapping consistency after consolidation

**Input:** extraction.json after Pass 2 consolidation

**Output:** extraction.json with corrected bidirectional mappings

**Script:** `extraction-system/scripts/validate_bidirectional.py`

**When to run:**
- MANDATORY after Pass 2 (claims/evidence consolidation)
- MANDATORY after Pass 4 (RDMAP consolidation)
- RECOMMENDED after any manual edits to mappings

**What it validates:**
- Claim↔Evidence mappings: claims.supported_by ↔ evidence.supports_claims
- Method↔Design mappings: methods.implements_designs ↔ research_designs.implemented_by_methods
- Protocol↔Method mappings: protocols.implements_methods ↔ methods.implemented_by_protocols

**Auto-correction behaviour:**
- Adds missing reverse mappings automatically (safe corrections)
- Reports corrections made in terminal output
- Flags conflicts for manual review (exit code 2)
- Saves corrections directly to extraction.json

**Command:**
```bash
python3 extraction-system/scripts/validate_bidirectional.py outputs/{paper-slug}/extraction.json
```

**Success criteria:**
- Exit code 0: All consistent or auto-corrections successful
- Exit code 2: Conflicts require manual resolution (review and fix before proceeding)
- Exit code 1: Error (investigate and fix)

**Manual conflict resolution:**
If conflicts are reported (exit code 2):
1. Review terminal output for conflict descriptions
2. Inspect the specific mappings in extraction.json
3. Manually resolve contradictions (usually consolidation reference not updated in both directions)
4. Re-run script to verify resolution

**Why critical:**
Pass 2 consolidation often creates bidirectional inconsistencies when:
- Consolidated items have their forward references updated but reverse references in other arrays are missed
- Multiple items consolidated but not all reverse references merged
- Items removed but references not cleaned up

This phase catches 88+ errors across 5 papers according to cross-paper error analysis (2025-11-02).

**Checkpoint:** "Phase 2b complete - bidirectional mappings validated: {corrections_made} auto-corrections, {conflicts_found} conflicts resolved."

**Duration:** 5-10 minutes (mostly automated)

**Session B ends here.** Provide handoff summary, then stop.

---

## 🅲 SESSION C: RDMAP (Research Designs, Methods, Protocols)

---

### Pass 3: Liberal RDMAP Extraction

**Purpose:** Extract research designs, methods, and protocols

### CRITICAL PLANNING REQUIREMENTS for Pass 3:
1. **Use SAME section groups as Pass 1** (no new grouping)
2. **Equal attention to ALL sections** (not just Methods)
3. **Liberal over-extraction**: 40-50% more than final target
4. **ESPECIALLY liberal with research designs** (commonly under-extracted)
5. **Scan entire paper**: Designs appear in Intro, Theory, Methods, Discussion, Conclusions
6. **Avoid Methods over-focus**: Over-focusing on Methods causes systematic under-extraction of designs

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

**Proceeds to:** Phase 5b (Bidirectional Mapping Reconciliation)

---

### Phase 5b: Bidirectional Mapping Reconciliation

**Purpose:** Validate and auto-correct bidirectional RDMAP mapping consistency after consolidation

**Input:** extraction.json after Pass 5 (RDMAP rationalization)

**Output:** extraction.json with corrected bidirectional RDMAP mappings

**Script:** `extraction-system/scripts/validate_bidirectional.py`

**What it validates:**
- Method↔Design mappings: methods.implements_designs ↔ research_designs.implemented_by_methods
- Protocol↔Method mappings: protocols.implements_methods ↔ methods.implemented_by_protocols
- Claim↔Evidence mappings (if both present): claims.supported_by ↔ evidence.supports_claims

**Auto-correction behaviour:**
- Adds missing reverse mappings automatically (safe corrections)
- Reports corrections made in terminal output
- Flags conflicts for manual review (exit code 2)
- Saves corrections directly to extraction.json

**Command:**
```bash
python3 extraction-system/scripts/validate_bidirectional.py outputs/{paper-slug}/extraction.json
```

**Success criteria:**
- Exit code 0: All consistent or auto-corrections successful
- Exit code 2: Conflicts require manual resolution (review and fix before proceeding)
- Exit code 1: Error (investigate and fix)

**Why critical:**
Pass 5 RDMAP consolidation often creates bidirectional inconsistencies when:
- Consolidated methods have their forward references to designs updated but reverse references in research_designs.implemented_by_methods are missed
- Protocol→Method mappings not updated when methods are consolidated
- Hierarchy chains broken (Protocol→Method→Design)

This phase ensures RDMAP hierarchy integrity before validation.

**Checkpoint:** "Phase 5b complete - RDMAP bidirectional mappings validated: {corrections_made} auto-corrections, {conflicts_found} conflicts resolved."

**Duration:** 5-10 minutes (mostly automated)

**Session C ends here.** Provide handoff summary, then stop.

---

### Pass 6: Infrastructure Extraction (Full Documentation)

**Note:** Pass 6 is executed in Session A alongside Pass 0. This section provides full documentation.

**Purpose:** Extract reproducibility infrastructure and assess FAIR compliance

**Input:** Entire paper (focus on front matter, back matter, acknowledgements)

**Output:** Populated `reproducibility_infrastructure` object in extraction.json

**Prompt:** `extraction-system/prompts/06-infrastructure_pass6_prompt.md`

**Script Pattern:** `pass6_infrastructure_extraction.py`

**Approach:**
- **Section targeting:** Front matter (title page, affiliations), Back matter (acknowledgements, data availability statements, references)
- **Systematic infrastructure capture:** PIDs, funding, data/code sharing, ethics, permits
- **FAIR assessment:** 40-point scoring rubric (10 each for Findable, Accessible, Interoperable, Reusable)

**Infrastructure Sections (13 total):**

1. **persistent_identifiers** - Paper DOI, author ORCIDs, data/code DOIs, software PIDs, funder IDs, project IDs
2. **funding** - Sources, grant numbers, acknowledgement text
3. **data_availability** - Repositories, DOIs, access conditions, statements
4. **code_availability** - Repositories, DOIs, licences, documentation
5. **author_contributions** - CReDIT taxonomy roles, contribution statements
6. **conflicts_of_interest** - Declarations, relationships
7. **ethics_approval** - IRB/ethics committee approvals, consent procedures
8. **permits_and_authorizations** - Fieldwork permits, access permissions, CARE principles compliance
9. **preregistration** - Protocol registration, OSF links, trial IDs
10. **supplementary_materials** - Links, descriptions, DOIs
11. **references_completeness** - Bibliography assessment
12. **fair_assessment** - Findable (0-10), Accessible (0-10), Interoperable (0-10), Reusable (0-10), total score (0-40)
13. **extraction_metadata** - Extractor, timestamp, notes

**Critical Rules:**
- MUST scan front matter for ORCIDs (often in title page footnotes/affiliations)
- MUST check back matter for funding acknowledgements
- MUST assess data/code availability statements
- MUST score FAIR assessment using 40-point rubric
- Document absence of infrastructure (null values indicate checked but absent)

**Target Infrastructure:**
- PIDs: 1-10 items (paper DOI always present, author ORCIDs variable, data/code DOIs if shared)
- Funding: 0-10 sources (varies widely by discipline and project scale)
- FAIR score: 15-40 (higher for empirical data papers, lower for theoretical papers)

**Checkpoint:** "Pass 6 complete - infrastructure extracted. PIDs: {pid_count}, Funding: {funding_count}, FAIR: {fair_score}/40, Data availability: {data_status}, Code availability: {code_status}."

**Duration:** 30 minutes - 1 hour

**Session A ends here.** Provide handoff summary, then stop.

---

## 🅳 SESSION D: Validation + FAIR Assessment

---

### Pass 7: Validation

**Purpose:** Comprehensive quality checks and integrity validation

**Input:** Entire extraction.json

**Output:** Validation report and repaired cross-references if needed

**Prompt:** `extraction-system/prompts/07-validation_prompt.md`

**Script Pattern:** `pass7_validation.py` + `pass7_repair_references.py` (if needed)

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

**3. Metadata Completeness (Pass 0)**
- ✓ All 8 required project_metadata fields non-empty
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

**4. Infrastructure Completeness (Pass 6)**
- ✓ reproducibility_infrastructure object populated
- ✓ FAIR assessment scored (0-40)
- ✓ PIDs extracted where present
- ✓ Data/code availability documented

**Checkpoint:** "Pass 7 complete - validation status: {status}. {issue_counts}. Total items validated: {total} ({explicit} explicit + {implicit} implicit)."

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

## Quality Metrics

### Sourcing Completeness

**Target:** 100%

**Definition:** All items have either verbatim_quote (explicit) or trigger_text (implicit)

**Validation:** Pass 7 checks sourcing completeness

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

### v5.0.0 (2026-01-13)
- **Replaced autonomous mode with session-per-pass execution**
- Run comparison (crema-et-al-2024) showed +75% claims, +100% research designs with session-per-pass
- Defined 4 focused sessions: A (metadata+infra), B (claims), C (RDMAP), D (validation)
- Added session boundary markers throughout workflow
- Reordered Pass 6 to Session A (alongside Pass 0) for efficiency
- Updated extraction-launch.md to v2.0.0

### v4.0.0 (2025-11-18)
- Added Pass 6: Infrastructure Extraction (PIDs, FAIR assessment, funding, ethics, permits)
- Updated schema from v2.5 to v2.6
- Renumbered Pass 6 Validation to Pass 7
- Added Phases 2b and 5b (bidirectional reconciliation scripts)
- Updated from 7 passes to 8 passes (0-7)
- Added infrastructure completeness validation checks

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

**Schema Compatibility:** v2.6

**Last Updated:** 2025-11-18
