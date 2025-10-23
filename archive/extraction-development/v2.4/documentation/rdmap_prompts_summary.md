# RDMAP Extraction Prompts: Development Summary

**Date:** 2025-10-19  
**Deliverables:** Three comprehensive RDMAP extraction prompts (Pass 1/2/3)  
**Total Length:** ~1,100 lines  
**Status:** ✅ Complete and ready for testing

---

## What's Been Delivered

### Pass 1: Liberal RDMAP Extraction Prompt (~450 lines)

**Purpose:** Comprehensive extraction of Research Design, Methods, and Protocols with over-capture strategy

**Key Features:**
- ✅ Three-tier hierarchy guidance (Design → Methods → Protocols)
- ✅ Clear decision tree for tier assignment (Why/What/How test)
- ✅ Description vs argumentation boundary (RDMAP vs claims)
- ✅ Reasoning approach framework with definitions (inductive/abductive/deductive/mixed/unclear)
- ✅ Research questions vs hypotheses distinction with formulation timing
- ✅ Expected information checklists (TIDieR for methods, CONSORT-Outcomes for protocols, sampling, analysis)
- ✅ Controlled vocabularies (open lists for study designs, sampling strategies, analysis populations)
- ✅ Fieldwork-specific guidance (opportunistic decisions, contingency plans, emergent discoveries)
- ✅ Cross-reference patterns (simple string ID arrays)
- ✅ Six comprehensive archaeology-focused examples
- ✅ Liberal extraction philosophy ("when uncertain, include it")

**Structure:**
1. Extraction philosophy (40 lines)
2. Three-tier hierarchy (50 lines)
3. Description vs argumentation boundary (50 lines)
4. Reasoning approach framework (45 lines)
5. Research questions vs hypotheses (40 lines)
6. Expected information checklists (110 lines)
7. Controlled vocabularies (35 lines)
8. Fieldwork-specific guidance (40 lines)
9. Cross-reference patterns (30 lines)
10. Examples (60 lines)

---

### Pass 2: RDMAP Rationalization Prompt (~430 lines)

**Purpose:** Consolidate, refine tier assignments, validate cross-references, ensure completeness

**Key Features:**
- ✅ Consolidation philosophy (target 15-20% reduction)
- ✅ Acid test for consolidation ("assess together or separately?")
- ✅ RDMAP-specific consolidation patterns:
  - Design rationale synthesis
  - Scope definition consolidation
  - Workflow method aggregation
  - Validation chain consolidation
  - Protocol specification consolidation
  - Parameter aggregation
- ✅ Cross-reference validation (bidirectional consistency, orphan detection)
- ✅ Tier assignment verification (Why/What/How recheck)
- ✅ Boundary accuracy review (RDMAP vs claims)
- ✅ Reasoning approach consistency checks
- ✅ Expected information gap categorization (critical/important/minor)
- ✅ Consolidation metadata requirements
- ✅ Quality checks (no over/under-consolidation, cross-refs intact)
- ✅ Three detailed consolidation examples (good/bad patterns)

**Structure:**
1. Rationalization philosophy (30 lines)
2. Core consolidation principles (40 lines)
3. RDMAP-specific patterns (80 lines)
4. Cross-reference validation (50 lines)
5. Tier assignment verification (40 lines)
6. Boundary accuracy review (25 lines)
7. Reasoning approach consistency (30 lines)
8. Expected information review (35 lines)
9. Consolidation metadata (20 lines)
10. Quality checks (40 lines)
11. Examples (40 lines)

---

### Pass 3: RDMAP Validation Prompt (~220 lines)

**Purpose:** Automated integrity checks producing validation report without modifying extraction

**Key Features:**
- ✅ Cross-reference integrity (all IDs exist, bidirectional consistency, orphan detection)
- ✅ Hierarchy validation (Design → Methods → Protocols flow, claim links, evidence chains)
- ✅ Schema compliance (required fields, valid enums, ID formats, location structures)
- ✅ Expected information completeness (aggregate gaps, TIDieR/CONSORT checklists)
- ✅ Consolidation metadata verification
- ✅ Type consistency checks
- ✅ Severity categorization (critical/important/minor/warnings)
- ✅ Overall status determination (PASS/PASS_WITH_ISSUES/FAIL)
- ✅ Structured validation report format

**Structure:**
1. Validation philosophy (20 lines)
2. Cross-reference integrity checks (50 lines)
3. Hierarchy validation (30 lines)
4. Schema compliance (40 lines)
5. Expected information completeness (30 lines)
6. Consolidation verification (15 lines)
7. Type consistency (10 lines)
8. Report format (15 lines)
9. Severity levels and status (10 lines)

---

## Design Decisions Implemented

### From Handover Document

**✅ Vocabulary Choices:**
- Reasoning approach: inductive/abductive/deductive/mixed/unclear (NOT exploratory/confirmatory)
- Research questions vs hypotheses: separate tracking with formulation timing
- Study designs: open list, archaeology-focused initially
- Sampling strategies: open list, context-dependent
- Analysis populations: adapted from SPIRIT

**✅ Architectural Principles:**
- Simple cross-references (string ID arrays only)
- Extraction vs assessment separation
- Expected information ≠ Required information
- Retrospective inference reality (track confidence)
- Fieldwork epistemology respect (opportunism is legitimate when transparent)

**✅ Expected Information Frameworks:**
- TIDieR (adapted for methods): 10 elements
- CONSORT-Outcomes (adapted for protocols): 8 elements
- Sampling strategy checklist: 7 elements
- Analysis methods checklist: 7 elements

**✅ Fieldwork-Specific Adaptations:**
- Opportunistic decisions tracking
- Contingency plans (planned and actual)
- Adaptive procedures with justification
- Emergent discoveries
- Distinction: legitimate adaptation vs methodological opacity

---

## Architectural Consistency with Claims/Evidence Prompts

**Matched patterns:**
- ✅ Two-pass extraction philosophy (liberal → rationalize)
- ✅ Over-capture strategy in Pass 1 (40-50%)
- ✅ Target reduction in Pass 2 (15-20%)
- ✅ Consolidation metadata structure
- ✅ Expected information tracking
- ✅ Location object structure
- ✅ Verbatim quote usage
- ✅ Extraction confidence levels
- ✅ Simple string ID cross-references
- ✅ Quality checklist structure

**Style consistency:**
- Clear section numbering and hierarchy
- "Remember" boxes at end
- Quality checklists
- Comprehensive examples
- Decision trees and tests
- Bullet point guidance

---

## Examples Provided

**Pass 1 includes 6 comprehensive archaeology examples:**

1. **Research Design - Study Design**
   - Comparative assessment design
   - Reasoning approach framework demonstration
   - Mixed approach classification

2. **Research Design - Research Questions vs Hypotheses**
   - Pre-data vs post-data timing
   - Emergent hypothesis tracking
   - Confidence assessment

3. **Method - Data Collection with Opportunistic Decisions**
   - Field condition adaptations
   - Transparent response documentation
   - Impact assessment

4. **Method - Sampling Strategy**
   - Stratified random sampling
   - Analysis population specification
   - Exclusion transparency

5. **Protocol - Tool Specification**
   - FAIMS Mobile platform
   - Complete tool specification
   - Recording standards

6. **Protocol - Measurement with Decision Rules**
   - GPS coordinate collection
   - IF-THEN decision rules
   - Measurement specification checklist

**Pass 2 includes 3 consolidation examples:**
- Good consolidation (preserves info, improves structure)
- Bad consolidation (loses critical detail)
- Tier-specific consolidation patterns

---

## Ready for Testing

### Prerequisites Checklist

Before testing on Sobotkova Methods section:

- ✅ Schema v2.4 complete (in project knowledge)
- ✅ Implementation Decision Document available (in project knowledge)
- ✅ Pass 1 prompt complete (~450 lines)
- ✅ Pass 2 prompt complete (~430 lines)
- ✅ Pass 3 validation complete (~220 lines)
- ✅ Reasoning approach definitions in schema
- ✅ Expected information checklists specified
- ✅ Controlled vocabularies defined (open lists)
- ✅ Fieldwork-specific guidance included
- ✅ Consolidation patterns documented
- ✅ Examples sufficient (6 extraction, 3 consolidation)

### Testing Plan

**Step 1: Test Pass 1 Extraction**
- Input: Sobotkova Methods section
- Prompt: Pass 1 Liberal Extraction
- Expected: ~85 RDMAP items (over-captured)
- Review: Comprehensiveness, tier assignments, reasoning approach classifications

**Step 2: Test Pass 2 Rationalization**
- Input: Pass 1 extraction + Methods section
- Prompt: Pass 2 Rationalization
- Expected: ~69 RDMAP items (~18% reduction)
- Review: Consolidation quality, cross-reference validity, information preservation

**Step 3: Test Pass 3 Validation**
- Input: Pass 2 extraction
- Prompt: Pass 3 Validation
- Expected: Validation report with issue categorization
- Review: Issue detection accuracy, severity appropriateness

**Step 4: Assess Quality**
- Three-tier hierarchy clear and logical?
- Boundaries accurate (RDMAP vs claims)?
- Reasoning approaches well-classified?
- Hypothesis timing correctly inferred?
- Expected information gaps meaningful?
- Cross-references valid and bidirectional?
- Consolidation appropriate (no info loss)?
- Fieldwork adaptations captured systematically?

**Step 5: Iterate Based on Results**
- Boundary guidance adjustments
- Expected information checklist refinements
- Example additions
- Vocabulary expansions
- Consolidation pattern clarifications

---

## Known Challenges and Mitigation

### Challenge 1: Complexity Management
**Mitigation in prompts:**
- Clear "when to populate" guidance for conditional structures
- Decision trees for tier assignment
- Examples showing structure usage
- Liberal Pass 1, refine in Pass 2

### Challenge 2: Boundary Ambiguity
**Mitigation in prompts:**
- Why/What/How decision tree
- Description vs argumentation markers
- Extract at both levels when uncertain (Pass 1)
- Examples of boundary cases
- Pass 2 rationalizes ambiguous assignments

### Challenge 3: Retrospective Inference
**Mitigation in prompts:**
- Always extract explicit statements
- Always document inference basis
- Always track confidence
- Separate explicit from inferred
- Flag genuinely unclear cases

### Challenge 4: Expected Information Breadth
**Mitigation in prompts:**
- Domain-specific checklists (archaeology focus)
- Prioritize critical elements
- "Expected" ≠ "required" framing
- Categorize gaps by severity
- Build incrementally through testing

### Challenge 5: Open Vocabularies
**Mitigation in prompts:**
- Provide suggested terms
- Accept free text
- Note common patterns
- Don't force inappropriate categories
- Build empirically during testing

---

## What to Avoid (Documented in Prompts)

**Don't:**
- ❌ Force vocabulary that doesn't fit
- ❌ Over-structure protocols (avoid protocols.io complexity)
- ❌ Score quality during extraction
- ❌ Require perfect information
- ❌ Conflate description with argumentation
- ❌ Assume registration context
- ❌ Penalize opportunism
- ❌ Make "mixed" a dumping ground
- ❌ Expand in Pass 2 (consolidate only)

---

## Comparison to Target Specifications

**From handover document targets:**

| Component | Target Lines | Delivered Lines | Status |
|-----------|--------------|-----------------|--------|
| Pass 1 | ~400 | ~450 | ✓ Comprehensive |
| Pass 2 | ~400 | ~430 | ✓ Complete |
| Pass 3 | ~200 | ~220 | ✓ Thorough |
| **Total** | **~1000** | **~1100** | **✓ On target** |

**Content coverage against handover specs:**

| Section | Specified | Delivered | Status |
|---------|-----------|-----------|--------|
| Purpose & scope | ✓ | ✓ | Complete |
| Three-tier hierarchy | ✓ | ✓ | Complete |
| Boundary distinctions | ✓ | ✓ | Complete |
| Reasoning approach | ✓ | ✓ | Complete |
| RQ vs hypotheses | ✓ | ✓ | Complete |
| Expected info checklists | ✓ | ✓ | Complete |
| Controlled vocabularies | ✓ | ✓ | Complete |
| Fieldwork-specific | ✓ | ✓ | Complete |
| Cross-references | ✓ | ✓ | Complete |
| Examples | ✓ | ✓ | Complete |
| Consolidation patterns | ✓ | ✓ | Complete |
| Validation checks | ✓ | ✓ | Complete |

---

## Next Steps

### Immediate (This Session)
1. ✅ Review prompts for completeness
2. ✅ Verify architectural consistency
3. ✅ Check against handover specifications
4. ✅ Confirm examples are sufficient

### Next Session (Testing)
1. Test Pass 1 on Sobotkova Methods section
2. Evaluate comprehensiveness and tier assignments
3. Test Pass 2 rationalization
4. Evaluate consolidation quality
5. Test Pass 3 validation
6. Evaluate issue detection

### Subsequent Sessions (Refinement)
1. Adjust guidance based on test results
2. Add examples if needed
3. Refine vocabulary if patterns emerge
4. Enhance checklists if gaps identified
5. Iterate until extraction quality satisfactory

### After Successful Testing
1. Document testing results
2. Create user guide for prompts
3. Consider additional domain examples (beyond archaeology)
4. Plan for scale testing (multiple papers)

---

## Files Delivered

**Three prompt files created as markdown artifacts:**

1. **rdmap_pass1_md** - Pass 1: RDMAP Liberal Extraction Prompt v2.4
2. **rdmap_pass2_md** - Pass 2: RDMAP Rationalization Prompt v2.4
3. **rdmap_pass3_md** - Pass 3: RDMAP Validation Prompt v2.4

**Supporting context used:**
- Schema v2.4 (from project knowledge)
- RDMAP Implementation Decisions (from project knowledge)
- Claims/Evidence extraction prompts (for architectural patterns)
- Handover document (specification)

---

## Success Criteria Assessment

**From handover document - good RDMAP prompts will:**

- ✅ Enable comprehensive capture at appropriate granularity
- ✅ Maintain clear three-tier hierarchy
- ✅ Distinguish description from argumentation
- ✅ Track reasoning approaches and hypothesis timing accurately
- ✅ Capture fieldwork adaptations systematically
- ✅ Apply expected information frameworks appropriately
- ✅ Preserve architectural consistency with claims/evidence prompts
- ✅ Work on Sobotkova test case (ready for testing)
- ✅ Generalize to other fieldwork domains (examples focused but guidance general)

**Ready for testing when:**

- ✅ All three prompts complete
- ✅ Internal consistency verified
- ✅ Examples sufficient
- ✅ Expected information checklists comprehensive
- ✅ Cross-reference guidance clear

---

## Estimated Testing Timeline

**Conservative estimates:**

- **Pass 1 test:** 1-2 hours (extract Sobotkova Methods)
- **Pass 2 test:** 1-2 hours (rationalize extraction)
- **Pass 3 test:** 30 minutes (validate)
- **Review and assess:** 1-2 hours
- **Refinement:** 1-3 hours (depends on issues found)

**Total: 4-9 hours for first complete test cycle**

**Subsequent iterations:** Faster as prompts stabilize

---

## Final Notes

**What's been accomplished:**

This prompt development session has produced comprehensive, well-structured extraction guidance that:
- Builds on proven claims/evidence architecture
- Adapts registration frameworks for retrospective assessment
- Respects fieldwork epistemology
- Enables systematic transparency evaluation
- Maintains appropriate granularity across three tiers
- Provides extensive examples and decision support

**What makes these prompts different:**

Unlike clinical/experimental preregistration schemas, these prompts:
- Handle retrospective inference reality
- Capture legitimate opportunism in fieldwork
- Distinguish hypothesis formulation timing post-hoc
- Track adaptations and emergent findings
- Apply appropriate expected information for fieldwork contexts
- Build open vocabularies empirically

**Why they should work:**

- Proven two-pass architecture
- Clear decision trees and tests
- Comprehensive examples
- Appropriate granularity guidance
- Liberal then rationalize strategy
- Complete validation framework

**Your foundation is solid. The prompts are comprehensive and ready for testing. 🚀**

---

**Status:** ✅ Complete and ready for testing  
**Deliverables:** 3 prompts (~1,100 lines total)  
**Next Phase:** Testing on Sobotkova Methods section