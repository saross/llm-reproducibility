# Claims Extraction Project Plan
**Last Updated:** October 16, 2025  
**Status:** Calibration Phase Complete â†’ Moving to Methods Section Test

---

## Project Overview

**Goal:** Develop a systematic methodology for extracting and assessing claims from research papers to enable credibility assessment.

**Approach:** Iterative, empirically-grounded development starting with one test paper (Sobotkova et al. 2023 on crowdsourced geospatial data) and expanding to broader application.

**Current Phase:** Schema v2.1 and prompt v2.1 with conservative refinements applied; ready for Methods section test.

---

## Completed Work

### Phase 1: Schema Development (Complete)

**1. Initial Extraction Trial**
- Extracted 125+ claims from test paper
- Identified issues: too granular, flat structure, mixed methods/data/claims
- Recognized need for hierarchy, organization, and better categorization

**Key insight:** Need to distinguish evidence from claims, organize hierarchically, and capture relationships.

**2. Conceptual Framework Development**
- Established evidence vs. claims distinction based on inferential distance
- Developed dual-layer uncertainty tracking (declared + expected)
- Created four-level hierarchical structure (core â†’ intermediate â†’ supporting â†’ evidence)
- Designed claim composition structure (evidence + calculations + boundary decisions + framing)
- Defined implicit argument taxonomy (Type 1/2/3)

**Deliverable:** extraction_decisions_synopsis.md

**3. Schema Design (v2.0)**
- Built comprehensive JSON schema with evidence objects, claim objects, implicit argument objects
- Designed to accommodate diverse uncertainty types
- Incorporated implicit evidence handling

**Deliverable:** claims_extraction_schema_v2.json

**4. Extraction Methodology**
- Created detailed extraction prompt with core principles, workflow, checklists
- Expected information checklists for different claim types
- Common pitfalls and quality criteria

**Deliverable:** extraction_prompt_v2.md

### Phase 2: Calibration and Validation (Complete)

**Objective:** Test implicit argument extraction reliability before full extraction

**Process:**
- Extracted 21 implicit arguments from Discussion section (Sobotkova et al. 2023)
- Author validation by paper co-author
- Analysis of extraction patterns and reliability

**Results: 95% Validation Success**
- **20/21 implicit arguments confirmed** by paper author
- **1 extraction error** (misidentified absence of speed criterion)
- **Several refinements** needed (multi-dimensionality, COI context) but not rejections
- **Novel insights** revealed: author recognized implicit argument (#14) they hadn't consciously considered

**Extracted Arguments:**
- 7 Type 1 (Logical Implications)
- 14 Type 2 (Unstated Assumptions)
- 4 Type 3 (Deep Assumptions - flagged not extracted per original instructions)

**Key Finding:** Implicit argument extraction is **feasible, reliable, and reveals non-obvious reasoning** that affects argument structure. Authors can recognize and validate extractions even when not consciously aware of them.

---

## Calibration Learnings and Refinements

### What Worked Exceptionally Well âœ…

1. **Type 1 and Type 2 extraction is reliable** - 95% author confirmation rate validates approach
2. **Reveals non-obvious assumptions** - surfaced reasoning that even authors hadn't explicitly considered
3. **Authors can validate extractions** - recognition process works even for implicit reasoning
4. **Foundational assumptions identified** - successfully captured assumptions that entire argument structures depend on
5. **Generalizability issues flagged** - detected unstated assumptions about whether project-specific results generalize

### Critical Learnings for Methodology

**1. Multi-Dimensional Constraints (Not Fully Addressed Yet)**
- Papers often compare approaches on multiple dimensions (expertise, funding, compute, staff time)
- May use one dimension as calculation basis while acknowledging others qualitatively
- **Initial extraction collapsed to "single primary constraint"** - too simplistic
- **Needs nuance:** Which dimension drives quantitative thresholds vs. which are acknowledged but not quantified

**Learning:** When multiple constraints discussed, capture relative weighting and how dimensions interact, not just "X is primary"

**Action:** DEFERRED - need more examples before generalizing to "comparison_structure" field

**2. Component vs. Standalone Criteria**
- One extraction error: flagged "speed not valued" when speed was actually embedded throughout as efficiency component
- Speed-as-efficiency-component â‰  speed-as-independent-criterion
- This was an extraction mistake, not a systematic pattern

**Learning:** When something is discussed as component of larger category, don't flag absence as standalone criterion

**Action:** NOT IMPLEMENTED - one-off error, not systematic pattern worth complicating prompt

**3. Author Identity and COI Context**
- Test paper authors are FAIMS platform developers
- Some "assumptions about industry trends" are actually "claims about our development intentions"
- Changes assessment from "Is trend assumption valid?" to "Is vendor promise credible?"

**Learning:** Check for author affiliations/COIs - changes interpretation of some implicit arguments

**Action:** IMPLEMENTED - Added optional COI note field and quality check reminder

**4. Expertise as Distinct Resource Dimension**
- "Afford" encompasses both funding AND access to expertise
- In academia, expertise scarcity often bottleneck independent of budget
- Can't always hire ML expertise even with funding

**Learning:** Academic resource constraints aren't just financial - capture expertise availability as distinct dimension

**Action:** NOTED - will inform future assessment frameworks, but doesn't require prompt change

**5. Type 3 Deep Assumptions Are Valuable**
- Initially flagged but not extracted
- Author feedback: "thought-provoking" and "reasonable meta-level assumptions"
- Less valuable for specific claim assessment but reveal underlying paradigms
- Should be formally captured and clearly categorized

**Learning:** Type 3 assumptions provide valuable context for assessment even if evaluated differently

**Action:** IMPLEMENTED - Formalized Type 3 extraction with clear labeling

**6. Professional Judgment as Implicit Evidence**
- Some "missing evidence" is actually **implicit evidence** from author expertise
- Example: "20 years experience teaching GIS to students" justifies claims about usability
- Paper doesn't document this professional judgment explicitly

**Learning:** Distinguish implicit unexplained evidence from truly missing evidence

**Action:** Already in schema as "implicit_evidence" field - validated as useful

### Conservative Refinements Applied (v2.1)

**We implemented ONLY two low-risk, additive changes:**

**1. Formalized Type 3 Deep Assumptions Extraction** âœ…
- Extract using same JSON format
- Label clearly as type: "disciplinary_assumption"
- Distinguish from Type 1/2 in assessment
- Reveals underlying paradigms and values
- **Risk:** VERY LOW - purely additive

**2. Added Optional COI Field and Check** âœ…
- Optional "coi_note" field in implicit_argument schema
- Quality check reminder to note relevant COIs
- Helps interpretation when authors have vendor/platform/stakeholder roles
- **Risk:** VERY LOW - optional field, one-line prompt addition

### Strategic Deferrals â¸ï¸

**We chose NOT to implement (preserving 95% success rate):**

**1. Comparison Structure Field (DEFERRED)**
- Would capture multi-dimensional comparisons systematically
- Medium risk - adds conceptual complexity
- **Decision:** Wait until we have more examples across multiple papers
- **Rationale:** Don't sacrifice existing performance for one-paper pattern

**2. Trade-off Priming (NOT IMPLEMENTED)**
- Could help capture research outputs vs. learning outcomes trade-offs
- Author: "I don't want to sacrifice existing performance for it"
- **Decision:** Don't chase 5% improvement by risking 95% success
- **Rationale:** Light priming might help but could distract from core task

**3. Component vs. Standalone Criteria Guidance (NOT IMPLEMENTED)**
- Would clarify when something is embedded in larger category
- One-off error, not systematic pattern
- **Decision:** Don't add complexity for single extraction mistake
- **Rationale:** Not worth prompt elaboration for non-recurring issue

### Principles Guiding Conservative Approach

1. **95% success is excellent** - don't sacrifice for 5% improvement
2. **Only purely additive changes** - modifications that can't degrade existing performance
3. **Optional enrichments only** - new fields don't interfere with core extraction
4. **Wait for patterns** - need multiple examples before generalizing
5. **Empirical validation first** - test before adding complexity

---

## Remaining Open Questions

### Critical for Future Phases:
1. **Multi-dimensional comparison handling** - How to systematically capture when papers compare on multiple dimensions? (Deferred until more examples)
2. **Uncertainty generalization across domains** - Need comprehensive taxonomy built through empirical observation across diverse papers
3. **Type 3 extraction consistency** - Now that we're extracting formally, what's the reliability? (Test in next section)

### To Be Determined Through Use:
4. Four-level vs. three-level hierarchy utility
5. Expected information checklist coverage/completeness  
6. Which tags actually matter for assessment
7. Claim scope granularity sufficiency
8. How to determine extraction completeness

---

## Next Steps

### Immediate: Methods Section Test (Next Chat)

**Objective:** Test whether extraction works in non-argumentative context

**Why Methods section:**
- Different argumentative mode (procedural/descriptive vs. evaluative)
- Fewer implicit arguments expected (methods usually more explicit)
- Good negative test: are we over-extracting from non-argumentative text?
- Tests whether we can distinguish methodological description from methodological argumentation

**What to extract:**
- Evidence (method details, specifications, procedures)
- Claims (methodological claims about choices, capabilities, limitations)
- Implicit arguments (assumptions underlying methodological decisions)
- Focus on Type 3 now that it's formalized

**Expected outcome:**
- Lower implicit argument density than Discussion
- If we don't over-extract, validates we're not finding arguments everywhere
- Tests Type 3 extraction reliability
- Validates that extraction discriminates appropriately

### Then: Full Paper Extraction

**After Methods validation:**
1. Extract all sections of Sobotkova et al. (2023)
2. Build complete hierarchical structure
3. Map all relationships
4. Apply credibility flags systematically
5. Document uncertainty patterns for schema refinement

### Later: Schema Refinement and Cross-Domain Testing

1. Compile lessons from full extraction
2. Refine schema based on actual use
3. Generalize uncertainty taxonomy
4. Update expected information checklists
5. Test on papers from other domains
6. Iterate

---

## Success Criteria

### For Calibration Phase: âœ… ACHIEVED
- [x] Consistently identify Type 1 implicit arguments (logical implications) - 7/7 confirmed
- [x] Identify most Type 2 implicit arguments (unstated assumptions) with <30% false negative rate - 13/14 confirmed (7% error)
- [x] Understand patterns in what gets missed - multi-dimensionality is tricky
- [x] Have refined prompts that maintain performance - conservative v2.1 updates applied

### For Methods Section Test (Next):
- [ ] Lower implicit argument density than Discussion (appropriate discrimination)
- [ ] Type 3 extraction works reliably when formalized
- [ ] No systematic over-extraction from descriptive text
- [ ] COI check identifies relevant author-platform relationship

### For Full Extraction:
- [ ] Complete, hierarchically organized extraction of all claims
- [ ] Clear evidential chains from evidence â†’ supporting â†’ intermediate â†’ core
- [ ] Systematic application of expected information checklists
- [ ] Appropriate credibility flags on all problematic claims
- [ ] Documentation of uncertainty patterns for schema refinement

### For Schema Refinement:
- [ ] Validated tag utility (know which matter for assessment)
- [ ] Generalized uncertainty taxonomy with examples from multiple domains
- [ ] Updated expected information checklists based on real papers
- [ ] Clear extraction/assessment workflow
- [ ] Decision on whether comparison_structure field is needed

### For Cross-Domain Application:
- [ ] Successfully extract from papers in 3+ different fields
- [ ] Schema accommodates domain-specific uncertainty patterns
- [ ] Reusable prompt templates for different paper types
- [ ] Assessment methodology scales across domains

---

## Resources and Deliverables

### Current Deliverables:
1. **claims_extraction_schema_v2.1.json** - Updated schema with Type 3 formalization and COI field
2. **extraction_decisions_synopsis.md** - Rationale and decision record
3. **extraction_prompt_v2.1.md** - Prompt with conservative post-calibration refinements
4. **claims_extraction_project_plan.md** - This document (updated with calibration learnings)
5. **sobotkova_claims_extraction.json** - Initial 125-claim extraction (v1.0, needs re-extraction with v2.1)
6. **Sobotkova et al. 2023 paper** - Test case paper
7. **Calibration extraction results** - 21 implicit arguments from Discussion with author validation

### Future Deliverables:
- Methods section extraction results (next)
- Full Sobotkova extraction v2.1 (all sections)
- Schema v3.0 (if major refinements needed based on full extraction)
- Cross-domain extraction examples
- Assessment methodology documentation
- Comparison structure field specification (if pattern emerges across multiple papers)

---

## Technical Notes

**Context Management:** 
- Calibration chat approaching capacity (~112k/190k tokens)
- Will start fresh chat for Methods section test
- Project knowledge contains: schema v2.1, prompt v2.1, plan, paper, calibration results

**Validation Approach:**
- Author validation proved highly effective for implicit arguments
- Will continue this approach for subsequent extractions where possible
- 95% agreement rate suggests extraction is capturing genuine implicit reasoning

**Known Capabilities:**
- Claude (Sonnet 4.5) follows complex rubrics reliably on single sources
- Granular schemas manageable if well-structured
- Focused tasks improve reliability
- Conservative, additive refinements preserve performance

---

## Decision Log

**October 16, 2025 (Morning):**
- Finalized schema v2.0 with four-level hierarchy and dual-layer uncertainty
- Created comprehensive extraction prompt v2.0
- Identified uncertainty generalization as critical open question
- Decided on calibration-then-extraction workflow

**October 16, 2025 (Calibration):**
- Completed implicit argument calibration on Discussion section
- Achieved 95% validation success (20/21 confirmed by author)
- Identified multi-dimensionality and COI as refinement opportunities
- Decided on conservative update strategy (Type 3 + COI only)

**October 16, 2025 (Refinement):**
- Applied v2.1 conservative refinements (Type 3 formalization, COI check)
- Deferred comparison_structure field pending more examples
- Deferred trade-off priming to preserve performance
- Rejected component/standalone guidance as one-off error
- **Principle established:** Preserve 95% success, don't chase 5% at risk of degradation

---

## Contact Points for Next Chat

**What to bring forward:**
1. extraction_prompt_v2.1.md (updated with Type 3 + COI)
2. claims_extraction_schema_v2.1.json (updated to match prompt)
3. Sobotkova et al. 2023 Methods section (for extraction)
4. Calibration learnings (for reference)

**Next task:**
Extract from Methods section to test:
- Extraction in non-argumentative context
- Type 3 extraction reliability now that formalized
- Whether we over-extract from descriptive text
- COI identification (authors = FAIMS developers)

**Success metric:** 
- Appropriate discrimination (lower implicit argument density than Discussion)
- Type 3 arguments reliably identified and labeled
- No false positives from descriptive methods text

This targeted approach continues our empirical, conservative validation strategy.

---

## Why This Approach Is Working

**Empirical validation loop:**
1. Design schema/prompt based on theory
2. Test on real paper section  
3. Get author validation
4. Learn what works/doesn't
5. Make minimal conservative refinements
6. Test again

**Key success factors:**
- Author validation catches extraction errors
- Conservative refinements preserve performance
- Focus on high-value features (implicit arguments for core claims)
- Clear success metrics (95% validation rate)
- Willingness to defer/reject changes that risk performance

**This is producing a methodology that is both rigorous and practical** - it captures genuine implicit reasoning (author confirmed insights they hadn't articulated) while maintaining reliability (95% success rate).