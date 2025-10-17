# Claims Extraction Project Plan

**Last Updated:** October 17, 2025  
**Status:** Two-Pass Workflow Ready → Next Test Extraction  
**Current Version:** Schema v2.2, Prompt v2.2 (Pass 1 + Pass 2)

---

## Project Overview

**Goal:** Develop a systematic methodology for extracting and assessing claims from research papers to enable credibility assessment.

**Approach:** Iterative, empirically-grounded development starting with one test paper (Sobotkova et al. 2023 on crowdsourced geospatial data) and expanding to broader application.

**Current Phase:** Schema v2.2 and two-pass extraction workflow (Pass 1 + Pass 2) ready for testing.

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
- Created four-level hierarchical structure (core → intermediate → supporting → evidence)
- Designed claim composition structure (evidence + calculations + boundary decisions + framing)
- Defined implicit argument taxonomy (Type 1/2/3)

**Deliverable:** extraction_decisions_synopsis.md

**3. Schema Design (v2.0 → v2.2)**
- v2.0: Comprehensive JSON schema with evidence, claim, and implicit argument objects
- v2.1: Added Type 3 (disciplinary assumptions) formalization and COI field
- v2.2: Separated extraction-time vs assessment-time fields; added credibility_assessment structure (unpopulated during extraction); enhanced extraction observability

**Current Deliverable:** claims_extraction_schema_v2.2.json

**4. Extraction Methodology**
- v2.0: Initial comprehensive prompt
- v2.1: Conservative refinements after calibration
- v2.2 unified: Added 4 empirical principles from Methods rationalization + Type 3 distinguishing criteria
- v2.2 split: Two-pass workflow (Pass 1: Liberal extraction, Pass 2: Rationalization)

**Current Deliverables:** 
- extraction_prompt_v2.2.md (unified, committed to git)
- extraction_prompt_pass1_v2.2.md (liberal extraction)
- extraction_prompt_pass2_v2.2.md (rationalization)

### Phase 2: Calibration and Validation (Complete)

**Objective:** Test implicit argument extraction reliability before full extraction

**Process:**
- Extracted 21 implicit arguments from Discussion section (Sobotkova et al. 2023)
- Author validation: 95% success rate (20/21 confirmed)
- Identified refinement opportunities (multi-dimensionality, COI awareness)

**Results:**
- Type 1 (logical implications): 100% reliability
- Type 2 (unstated assumptions): 93% reliability (1 missed multi-dimensional assumption)
- Conservative approach validated: high precision, acceptable recall

**Refinements Applied (v2.1):**
- Formalized Type 3 (disciplinary assumptions) extraction
- Added optional COI note field
- Maintained conservative extraction approach

**Key Finding:** Conservative extraction of implicit arguments achieves 93%+ accuracy.

### Phase 3: Methods Section Test & Rationalization (Complete)

**Objective:** Test extraction workflow and develop consolidation heuristics

**Process:**
- Extracted Methods section with Pass 1 approach (liberal extraction)
- Manual rationalization: 85 items → 69 items (19% reduction)
- Identified consolidation patterns and decision heuristics
- Discovered 4 empirical principles for prompt improvement

**Key Learnings:**
1. Single-case observations → implicit generalizations (foundational HASS pattern)
2. Context management critical (source text must be available for rationalization)
3. Over-extraction is strategy, not bug (easier to consolidate than recover missed items)
4. Evidence/claim boundary fuzzy by nature (default to claim when expertise required)
5. Granularity should match assessment question granularity
6. Methods ≠ Evidence/Claims (could be parallel extraction passes)
7. Abductive research pattern distinctive (innovation presented as planned, not discovered)

**Empirical Principles Identified:**
1. Track record = context, not evidence
2. Single-case generalizations require both evidence + implicit claim
3. Professional judgment statements are claims, not evidence
4. Evidence must support claims (test: "would removal lose evidential support?")

**Deliverable:** Session Learnings & Decisions - Methods Extraction Rationalization.md

**Refinements Applied (v2.2):**
- Added 4 empirical principles to prompt (~125 words)
- Formalized Type 3 distinguishing criteria
- Created two-pass workflow architecture

### Phase 4: Schema & Workflow Refinement (Complete)

**4.1 Assessment Structure Addition (v2.2)**

**Decision:** Separate extraction-time vs assessment-time workflow

**Implementation:**
- Added `credibility_assessment` structure to claims (defaults to "not_yet_assessed")
- Added `evidence_strength` placeholder to evidence (assessment-time)
- Enhanced extraction-time observability: `evidence_basis`, `extraction_flags`, `expected_information_missing`
- Added `workflow_notes` object to track completion status

**Rationale:**
- Extraction = identifying and structuring content (what's there)
- Assessment = evaluating credibility/quality (how good is it)
- Prevents scope creep during extraction
- Assessment requires domain expertise and scoring rubrics (Phase 5 work)

**4.2 Two-Pass Workflow Architecture**

**Design:**
```
Section Text 
    ↓
PASS 1: Liberal Extraction → Raw JSON (~40-50% over-extracted)
    ↓
PASS 2: Rationalization → Refined JSON (consolidated, verified)
```

**Pass 1 Philosophy:** "When uncertain, INCLUDE IT"
- Comprehensive capture
- Accept over-extraction
- Preserve granularity
- Focus on not missing anything

**Pass 2 Operations:**
- REMOVE: Items that don't support claims → project_metadata
- CONSOLIDATE: Redundant items using lumping heuristics
- SPLIT: Over-consolidated items using splitting heuristics
- RECLASSIFY: Evidence/claim boundary errors
- ADD: Missing implicit generalizations
- VERIFY: Relationships accurate, citations verified

**Consolidation Principles:**
- Acid test: "Assess together or separately?"
- When to lump: Same entity specs, compound claims, joint capabilities, single workflows
- When to split: Different claims, different assessments, different sources, different concerns

**Deliverables:**
- extraction_prompt_pass1_v2.2.md
- extraction_prompt_pass2_v2.2.md

**Status:** Ready for testing

---

## Current Resources and Deliverables

### Schema (v2.2)
**File:** claims_extraction_schema_v2.2.json

**Key Features:**
- Evidence, claim, implicit argument objects
- Dual-layer uncertainty (declared + expected)
- Four-level hierarchy
- Extraction-time vs assessment-time field separation
- Project metadata structure
- Credibility assessment structure (assessment-time)
- Evidence strength structure (assessment-time)

### Prompts (v2.2)

**Unified Version (committed to git):**
- extraction_prompt_v2.2.md
- All principles integrated
- Single comprehensive document

**Split Version (for two-pass workflow):**
- extraction_prompt_pass1_v2.2.md (liberal extraction)
- extraction_prompt_pass2_v2.2.md (rationalization)

### Planning Documents
- claims_extraction_project_plan.md (this document)
- schema_improvement_plan.md (improvement checklist with phases)
- Session Learnings & Decisions - Methods Extraction Rationalization.md

### Test Data
- Sobotkova et al. 2023 paper (test case)
- Initial 125-claim extraction (v1.0, outdated)
- Discussion section implicit arguments (21 items, 95% validated)
- Methods section extraction + rationalization (69 items after consolidation)

---

## Next Steps

### Immediate: Two-Pass Workflow Test

**Test Section:** Results or Discussion section of Sobotkova et al. 2023

**Process:**
1. Run Pass 1 (liberal extraction) using extraction_prompt_pass1_v2.2.md
2. Run Pass 2 (rationalization) using extraction_prompt_pass2_v2.2.md with Pass 1 output + source text
3. Measure metrics
4. Compare to Methods section results
5. Refine prompts based on findings

**Success Metrics (Target ~80%):**
- Precision: >85% (extracted items correct/appropriate)
- Recall: >80% (actual items extracted vs hand-coding)
- Boundary Accuracy: >75% (evidence/claim classifications correct)
- Relationship Accuracy: >70% (support links correct)
- Consolidation Quality: >80% (appropriate lumping/splitting)

### Phase 5: Empirical Refinement (After 5-10 Papers)

**5.1 Refine Expected Information Checklists**
- Replace generic theoretical checklists with domain-specific empirical ones
- Pattern analysis: What's consistently missing across papers?
- Build archaeology-specific checklists (radiocarbon, GIS, survey, statistical models)

**5.2 Develop Credibility Signal Thresholds**
- After scoring 50+ claims, establish empirical rubrics
- When does "moderate" transparency → "low"?
- What combination of red flags affects validity scores?
- Which missing checklist elements matter most?

**5.3 Validate Consolidation Heuristics**
- Track all consolidation decisions
- Identify most-used heuristics
- Find edge cases where heuristics conflict
- Refine rules based on actual ambiguities

**5.4 Review Controlled Vocabulary Completeness**
- What % of evidence/methods fit existing categories?
- Are new subtypes stabilizing or proliferating?
- Which free-text fields should become controlled vocabularies?

**5.5 Review Implicit Argument Extraction Intensity**
- Are we missing important Type 2 arguments consistently?
- Is Type 3 formalization working as expected?
- Should extraction become more liberal or stay conservative?

### Phase 6: Cross-Domain Testing

**Goal:** Validate schema across diverse HASS domains

**Domain Targets:**
- Digital archaeology (completed: Sobotkova)
- Palaeoenvironments
- Archaeogenetics
- Statistically modelled heritage management
- Large-scale landscape archaeology

**Success Criteria:**
- Schema accommodates domain-specific patterns
- Extraction accuracy stable across domains
- Domain-specific checklists developed
- Assessment methodology scales

---

## Success Criteria

### For Two-Pass Workflow Test (Next):
- [ ] Lower implicit argument density than Discussion (appropriate discrimination)
- [ ] Type 3 extraction works reliably with formalized criteria
- [ ] No systematic over-extraction from descriptive text
- [ ] Consolidation reduces items 15-20% without information loss
- [ ] Change log documents all operations clearly

### For Phase 5 Refinement (After 5-10 Papers):
- [ ] Domain-specific checklists replace generic ones
- [ ] Credibility scoring rubrics based on 50+ claim sample
- [ ] Consolidation heuristics validated across papers
- [ ] Controlled vocabulary review completed
- [ ] Implicit argument intensity review completed
- [ ] Schema stabilized (minimal changes across 3 consecutive papers)

### For Phase 6 Cross-Domain (After 10+ Papers):
- [ ] Successfully extract from papers in 3+ different fields
- [ ] Schema accommodates domain-specific uncertainty patterns
- [ ] Reusable prompt templates for different paper types
- [ ] Assessment methodology scales across domains

---

## Technical Notes

**Context Management:**
- Current chat: ~111k/190k tokens used
- Two-pass workflow prompts are substantial
- Next test should start fresh chat with prompts + section text
- Project knowledge contains all schemas, prompts, and learnings

**Tools:**
- JSON schema v2.2 for structured extraction
- Two-pass prompt workflow
- Project knowledge for document storage
- Git/GitHub for version control

**Known Capabilities:**
- Claude Sonnet 4.5 follows complex rubrics reliably
- Granular schemas manageable if well-structured
- Two-pass approach more reliable than single-pass perfection
- Conservative implicit argument extraction achieves 93%+ accuracy

---

## Decision Log

**October 16, 2025:**
- Finalized schema v2.0 with four-level hierarchy and dual-layer uncertainty
- Created comprehensive extraction prompt v2.0
- Completed calibration: 95% implicit argument accuracy

**October 17, 2025:**
- Completed Methods section rationalization (85→69 items, 19% reduction)
- Identified 4 empirical principles for prompt improvement
- Created schema v2.2 with extraction/assessment separation
- Added credibility assessment structure (unpopulated during extraction)
- Created unified prompt v2.2 with empirical improvements
- Split prompt into two-pass workflow (Pass 1 + Pass 2)
- Formalized consolidation heuristics
- Ready for two-pass workflow test

---

## Related Planning Documents

**Schema Improvement Plan** (schema_improvement_plan.md):
- Pragmatic iteration approach
- Phase 1-5 roadmap
- Decision points and scheduled reviews
- Crosswalk documentation strategy
- Success criteria per phase

**Methods Rationalization** (Session Learnings & Decisions):
- Consolidation heuristics
- Empirical principles discovered
- Category-specific patterns
- Two-pass workflow rationale

**Survey of Existing Schemas** (Comprehensive Survey document):
- 40+ schemas analyzed
- Gap analysis for HASS needs
- Mapping to existing ontologies
- Formalization pathway guidance

---

## Evolution Principles

1. **Start specific, generalize empirically** - Build from one good example, expand through observation
2. **Prefer granularity now, consolidate later** - Better to over-extract than miss content
3. **Absence is data** - Document what's missing, not just what's present
4. **Iterate based on use** - Let practical experience drive refinement
5. **Transparency over perfection** - Schema should capture uncertainty, not hide it
6. **Pragmatic iteration → formalization** - Prove viability first, invest in formal infrastructure later
7. **Conservative on quality** - Don't sacrifice 95% success for 5% improvement

---

**Document Status:** Current as of October 17, 2025  
**Next Update Trigger:** After two-pass workflow test completion