# Claims Extraction Project Plan
**Last Updated:** October 16, 2025  
**Status:** Schema Development Complete → Moving to Calibration Phase

---

## Project Overview

**Goal:** Develop a systematic methodology for extracting and assessing claims from research papers to enable credibility assessment.

**Approach:** Iterative, empirically-grounded development starting with one test paper (Sobotkova et al. 2023 on crowdsourced geospatial data) and expanding to broader application.

**Current Phase:** Schema v2.0 complete; ready for calibration round on implicit argument extraction.

---

## Completed Work (Phase 1: Schema Development)

### 1. Initial Extraction Trial
**What we did:**
- Extracted 125+ claims from test paper (Sobotkova et al. 2023)
- Identified issues: too granular, flat structure, mixed methods/data/claims
- Recognized need for hierarchy, organization, and better categorization

**Key insight:** Need to distinguish evidence from claims, organize hierarchically, and capture relationships.

### 2. Conceptual Framework Development
**What we did:**
- Established evidence vs. claims distinction based on inferential distance
- Developed dual-layer uncertainty tracking (declared + expected)
- Created four-level hierarchical structure (core → intermediate → supporting → evidence)
- Designed claim composition structure (evidence + calculations + boundary decisions + framing)
- Defined implicit argument taxonomy (Type 1/2/3)

**Deliverable:** [extraction_decisions_synopsis.md](computer:///mnt/user-data/outputs/extraction_decisions_synopsis.md)

### 3. Schema Design (v2.0)
**What we did:**
- Built comprehensive JSON schema with:
  - Evidence objects (with declared + expected uncertainty)
  - Claim objects (with hierarchical roles and functions)
  - Implicit argument objects
  - Expected information checklists
  - Credibility flag taxonomy
- Designed to accommodate diverse uncertainty types (radiometric ±, stylistic ranges, hedged language)
- Incorporated implicit evidence handling (author observation, professional judgment, etc.)

**Deliverable:** [claims_extraction_schema_v2.json](computer:///mnt/user-data/outputs/claims_extraction_schema_v2.json)

### 4. Extraction Methodology
**What we did:**
- Created detailed extraction prompt with:
  - Core principles (evidence/claims distinction, uncertainty tracking, hierarchy)
  - Step-by-step workflow (scan → extract by section → build hierarchy → quality check)
  - Expected information checklists (quantitative, comparative, methodological, causal, generalizability)
  - Common pitfalls to avoid
  - Quality criteria for good extraction

**Deliverable:** [extraction_prompt_v2.md](computer:///mnt/user-data/outputs/extraction_prompt_v2.md)

### 5. Test Case: Student/Staff Time Measurement
**What we did:**
- Re-extracted time measurement data from test paper using new schema
- Demonstrated dual-layer uncertainty tracking in practice
- Showed how to capture both declared uncertainty and expected (but missing) uncertainty
- Identified transparency issues (missing bounded ranges, false precision)

**Key finding:** Schema successfully captures what's present, what's missing, and why it matters.

### 6. Key Decisions Finalized
- ✅ Evidence/claims distinction based on inferential distance
- ✅ Dual-layer uncertainty (declared + expected)
- ✅ Four-level hierarchy (will reduce to three if unnecessary)
- ✅ Hierarchical claim_function (primary + secondary)
- ✅ Claim scope tagging (project/domain/general)
- ✅ Implicit argument extraction (Type 1 & 2 for high-priority claims)
- ✅ Expected information checklists
- ✅ Implicit vs. missing evidence distinction
- ✅ Extraction/assessment boundary

---

## Remaining Open Questions

### Critical for Next Phase:
1. **Implicit argument extraction reliability** - Can Type 1 and Type 2 be consistently identified?
2. **Uncertainty generalization** - Need to build comprehensive taxonomy across domains through empirical observation

### To Be Determined Through Use:
3. Four-level vs. three-level hierarchy utility
4. Expected information checklist coverage/completeness
5. Which tags actually matter for assessment
6. Claim scope granularity sufficiency
7. How to determine extraction completeness

---

## Next Steps (Phase 2: Calibration)

### Immediate: Calibration Round on Implicit Arguments
**Objective:** Test extraction reliability before full paper extraction

**Process:**
1. **Select section:** Discussion section of Sobotkova et al. (2023) - contains high-priority claims
2. **Focused extraction:** Extract ONLY implicit arguments (Type 1 & 2) for core and intermediate claims
3. **User review:** Identify false negatives (implicit arguments Claude missed)
4. **Pattern analysis:** What types of implicit arguments are reliably caught vs. missed?
5. **Prompt refinement:** Improve extraction prompts based on patterns
6. **Reliability assessment:** Decide if approach is reliable enough for full extraction

**Expected outcome:** 
- Understanding of extraction consistency
- Refined prompts for implicit argument detection
- Confidence in methodology (or recognition of limitations)

**Duration:** One focused chat session

### Then: Full Section Test Extraction
**Objective:** Validate complete schema on manageable section

**Process:**
1. Extract all evidence, claims, and implicit arguments from one section (likely Discussion)
2. Apply full schema including all tags, relationships, checklists
3. Assess which elements are useful vs. burdensome
4. Time the extraction process
5. Identify schema gaps or ambiguities

**Expected outcome:**
- Practical experience with full schema
- Identification of needed refinements
- Realistic assessment of effort required

### Then: Full Paper Extraction
**Objective:** Complete end-to-end extraction

**Process:**
1. Extract all sections of Sobotkova et al. (2023)
2. Build complete hierarchical structure
3. Map all relationships
4. Apply credibility flags systematically
5. Document uncertainty patterns that don't fit schema

**Expected outcome:**
- Complete extraction for assessment
- List of schema refinements needed
- Uncertainty patterns for generalization

### Later: Schema Refinement and Expansion
**Objective:** Generalize beyond archaeology methods paper

**Process:**
1. Compile lessons from full extraction
2. Refine schema based on actual use
3. Generalize uncertainty taxonomy
4. Update expected information checklists
5. Test on papers from other domains
6. Iterate

---

## Evolution Principles

1. **Start specific, generalize empirically** - Build from one good example, expand through observation
2. **Prefer granularity now, pare later** - Better to have unused tags than miss important distinctions
3. **Absence is data** - Document what's missing, not just what's present
4. **Iterate based on use** - Let practical experience drive refinement
5. **Transparency over perfection** - Schema should capture uncertainty, not hide it

---

## Success Criteria

### For Calibration Round (Next Phase):
- [ ] Can consistently identify Type 1 implicit arguments (logical implications)
- [ ] Can identify most Type 2 implicit arguments (unstated assumptions) with <30% false negative rate
- [ ] Understand patterns in what gets missed
- [ ] Have refined prompts that improve detection

### For Full Extraction:
- [ ] Complete, hierarchically organized extraction of all claims
- [ ] Clear evidential chains from evidence → supporting → intermediate → core
- [ ] Systematic application of expected information checklists
- [ ] Appropriate credibility flags on all problematic claims
- [ ] Documentation of uncertainty patterns for schema refinement

### For Schema Refinement:
- [ ] Validated tag utility (know which matter for assessment)
- [ ] Generalized uncertainty taxonomy with examples from multiple domains
- [ ] Updated expected information checklists based on real papers
- [ ] Clear extraction/assessment workflow

### For Cross-Domain Application:
- [ ] Successfully extract from papers in 3+ different fields
- [ ] Schema accommodates domain-specific uncertainty patterns
- [ ] Reusable prompt templates for different paper types
- [ ] Assessment methodology scales across domains

---

## Resources and Deliverables

### Current Deliverables (in project knowledge and /outputs):
1. **claims_extraction_schema_v2.json** - Complete JSON schema
2. **extraction_decisions_synopsis.md** - Rationale and decision record
3. **extraction_prompt_v2.md** - Comprehensive extraction guide
4. **claims_extraction_project_plan.md** - This document
5. **sobotkova_claims_extraction.json** - Initial 125-claim extraction (v1.0, needs re-extraction)
6. **Sobotkova et al. 2023 paper** - Test case paper

### Future Deliverables:
- Calibration round results and refined prompts
- Full Sobotkova extraction (v2.0)
- Schema v3.0 (refined based on use)
- Cross-domain extraction examples
- Assessment methodology documentation

---

## Technical Notes

**Context Management:** 
- Schema development chat approaching context limits (~94k/190k tokens used)
- Starting fresh chat for calibration to ensure focused work
- Will reference project knowledge for schema/prompt/paper access

**Tools:**
- JSON schema for structured extraction
- Project knowledge for document storage and retrieval
- Iterative prompt refinement based on results

**Known Capabilities (from past work):**
- Claude (Sonnet 3.5-3.7) can follow complex rubrics reliably on single sources
- Granular schemas are manageable if well-structured
- Focused tasks (e.g., implicit argument extraction only) improve reliability

---

## Decision Log

**October 16, 2025:**
- Finalized schema v2.0 with four-level hierarchy and dual-layer uncertainty
- Created comprehensive extraction prompt
- Identified uncertainty generalization as critical open question
- Decided on calibration-then-extraction workflow
- Ready to begin Phase 2 (Calibration)

---

## Contact Points for Next Chat

**What to bring forward:**
1. Project knowledge contains: schema, prompt, synopsis, paper
2. Focus: Implicit argument extraction from Discussion section only
3. Goal: Test reliability, identify patterns, refine prompts
4. Success metric: <30% false negative rate on Type 1 & 2 implicit arguments

**What NOT to do:**
- Don't extract full paper yet
- Don't extract evidence/claims (focus on implicit arguments only)
- Don't worry about hierarchy (will do in full extraction)
- Don't assess credibility (extraction only)

This targeted approach maximizes learning while managing scope.
