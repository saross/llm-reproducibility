# Workflow Improvements from Chatbot vs CC Comparison
## Based on Sobotkova et al. 2023 Extraction Analysis

**Date:** 2025-10-25
**Source:** outputs/sobotkova-et-al-2023/extraction-comparison.md
**Context:** Comparing chatbot extraction (with-skill v2.4) vs CC autonomous extraction (v2.6)

---

## Executive Summary

The comparison revealed CC autonomous workflow is **fundamentally sound** with comprehensive coverage (33% more total items than chatbot) and excellent quality (100% source verification). However, two critical gaps and one validation need emerged:

**Critical Gaps:**
1. **Implicit arguments:** CC extracted 0, chatbot extracted 10 (MUST FIX)
2. **Research design granularity:** CC extracted 2 holistic frameworks, chatbot extracted 5 strategic decisions (SHOULD FIX)

**Validation Needed:**
3. **Consolidation appropriateness:** CC's conservative approach (3% consolidation) vs chatbot's aggressive synthesis (69% consolidation) - verify CC approach is appropriate for assessment purposes

**CC Strengths to Preserve:**
- Section-by-section comprehensive extraction (captured 177% more evidence)
- Conservative consolidation philosophy (maintains assessability)
- Implicit protocol identification (4 found by CC, 0 by chatbot)
- Comprehensive expected information tracking

---

## Priority Tasks

### 1. CRITICAL: Add Implicit Argument Extraction

**The Gap:**
- **CC extracted:** 0 implicit arguments
- **Chatbot extracted:** 10 implicit arguments
- **Impact:** Missing critical layer of reasoning analysis needed for FAIR4RS assessment

**Chatbot's 10 implicit arguments included:**
1. IA001: Feature density affects digitization rates (unstated assumption)
2. IA002: Staff time is appropriate optimization criterion (disciplinary assumption)
3. IA003: Volunteer retention risk differs (desktop GIS vs mobile) (comparative assumption)
4. IA004: Linear extrapolation from small-scale measurements valid (scaling assumption)
5. IA005: ML expertise unavailable to small HASS projects (barrier assumption)
6. IA006: Urban Occupations Project is reasonable ML benchmark (comparability assumption)
7. IA007: 6% error rate is acceptable quality (threshold assumption)
8. IA008: Volunteer satisfaction matters for method selection (evaluation assumption)
9. IA009: In-field time more constrained than pre/post fieldwork (temporal assumption)
10. IA010: ML requires manual training data vs synthetic (approach assumption)

**Why these matter:** They expose unstated assumptions that affect generalizability, comparative validity, and threshold applicability.

**Action Required:**
- **Investigate root cause:** Why did CC find 0 when using similar prompts? (See Section 3)
- **Add explicit extraction pass:** Pass 2.5 or Pass 4.5 dedicated to implicit arguments
- **Update prompts:** Ensure implicit argument detection is explicitly required
- **Provide examples:** Reference chatbot's 10 items as exemplars in skill/prompts

**Implementation Notes:**
- CC successfully found 4 implicit protocols, so capability exists
- May be workflow sequencing issue (when implicit detection happens)
- May be prompt emphasis issue (implicit arguments vs implicit protocols treated differently)

---

### 2. IMPORTANT: Clarify Research Design Granularity

**The Gap:**
- **CC extracted:** 2 overarching frameworks
  - RD001: Case study of crowdsourced map digitization
  - RD002: Research question about optimal approach selection (implicit)
- **Chatbot extracted:** 5 distinct strategic decisions
  - RD001: Extract features from maps (research goal)
  - RD002: Crowdsourcing approach (strategic choice responding to 2010 failure)
  - RD003: Mobile platform selection (7-factor rationale)
  - RD004: Division of labor design (workflow architecture)
  - RD005: Systematic evaluation (opportunistic measurement decision)

**Why This Matters:**
- Each strategic design decision should be independently assessable for transparency
- "Why mobile vs desktop?" is different assessment than "Why crowdsourcing vs ML?"
- FAIR4RS principle: Design decisions should be documented and justified
- CC's holistic approach may miss specific design choices needing scrutiny

**Which Approach is Correct?**
- **Assessment verdict:** Chatbot's granularity is more appropriate
- **Rationale:** Each design decision represents independent choice point requiring separate justification
- **Test:** "Could two researchers independently assess different aspects?" → If yes, split them

**Action Required:**
- **Update WORKFLOW.md:** Add guidance on research design granularity
  - "Capture distinct strategic decisions, not just overall study framework"
  - "Each design decision should represent independent choice requiring justification"
- **Provide examples:** Platform choice, participant selection, workflow architecture as separate RD items
- **Add decision rule:** "If the paper provides separate rationale for different aspects, extract as separate designs"

**Implementation Notes:**
- This is conceptual guidance issue, not prompt issue
- May need examples in skill references
- Consider: "opportunistic" designs (like RD005 evaluation decision) - these are valuable to capture

---

### 3. VALIDATION: Review Consolidation Appropriateness

**The Gap:**
- **CC approach:** 3% consolidation (31 claims from 32, 36 evidence unchanged)
- **Chatbot approach:** 69% consolidation (16 claims from 51, 13 evidence from 28)

**Different Philosophies:**
- **Chatbot:** "Create interpretable narrative by merging related items"
  - Example: C012 consolidated 5 separate threshold claims into single guidance
  - Rationale: "All threshold recommendations part of integrated guidance framework"
  - Result: Coherent, readable synthesis

- **CC:** "Only consolidate clear redundancies or sequential workflow steps"
  - Example: C001 consolidated Abstract claim and identical Conclusion claim (redundancy)
  - Rationale: "Better to preserve appropriate granularity than force consolidations"
  - Result: Independently assessable items

**Trade-offs:**
- **Chatbot advantage:** Easier to understand, clearer narrative arc, less repetition
- **CC advantage:** Each item independently assessable, inferential chain explicit, temporal/contextual distinctions preserved

**For FAIR4RS Assessment:**
- **Need:** Independent assessment of each finding for transparency/replicability
- **Implication:** CC's conservative approach likely more appropriate
- **BUT:** Need to verify no unnecessary fragmentation

**Action Required:**
- **Manual review of CC extraction:** Are any items unnecessarily split?
  - Evidence: Review E001-E036 - do any represent same measurement at same time?
  - Claims: Review C001-C032 - are any trivially similar interpretations?
  - Test: "Would I assess these together or separately for transparency?"

- **Spot check examples:**
  - E032-E035: Four separate productivity calculations (staff GIS, 2010 volunteer, crowdsourcing, threshold)
    - Question: Should these merge?
    - Answer likely: NO - different contexts, different time periods, different participants
  - C020, C021, C022: Three claims about approach characteristics
    - Question: Should these merge?
    - Answer likely: NO - different dimensions (training, complementarity, suitability)

- **Document consolidation philosophy more explicitly in WORKFLOW.md:**
  - "Only consolidate when items represent identical finding stated in multiple places (redundancy)"
  - "Do NOT consolidate temporal variations (2017 vs 2018 measurements stay separate)"
  - "Do NOT consolidate different dimensions of same finding (training + cost + scalability stay separate)"
  - "Do NOT consolidate interpretive steps (let inferential chain stay explicit)"

**Implementation Notes:**
- This is validation, not necessarily change
- Likely outcome: CC approach is appropriate, but needs documentation
- May find 1-2 cases where consolidation appropriate
- Chatbot's approach optimized for publication readiness, CC for assessment utility

---

## Secondary Considerations (Already Working Well)

### 4. Section-by-Section Comprehensive Extraction ✅
**CC Strength - Preserve**

**What happened:**
- CC extracted evidence from Abstract, Introduction, Methods, Results, Discussion
- Chatbot focused primarily on Discussion section (where arguments are)
- Result: CC captured 36 evidence items vs chatbot's 13 (177% more)

**Why it matters:**
- Evidence in Methods/Results crucial for replication assessment
- Scattered measurements need comprehensive capture
- Temporal sequences important (2017 vs 2018 data)

**Action:** Keep CC's section-by-section workflow approach

---

### 5. Implicit Protocol Identification ✅
**CC Strength - Preserve**

**What happened:**
- CC identified 4 implicit protocols (mentioned but undocumented procedures):
  - P009: Volunteer training (minimal, minutes - mentioned but no protocol documented)
  - P010: GPS coordinate extraction automation (mentioned in Results, not Methods)
  - P011: Performance mitigation (export/reset protocol - applied but undocumented)
  - P012: Data correction protocol (spatial omission fixes - mentioned but not described)
- Chatbot had all 13 protocols as explicit

**Why it matters:**
- Implicit protocols = transparency gaps
- These are procedures actually used but not documented in Methods
- Critical for replicability assessment

**Action:** Keep this capability - finding undocumented procedures is valuable

**Note:** This demonstrates CC can find implicit items when appropriate - makes implicit argument gap more puzzling (investigate in Section 3)

---

### 6. Comprehensive Expected Information Tracking ✅
**CC Strength - Preserve**

**What happened:**
- Both extractions tracked missing information
- CC's lists more extensive (e.g., M004 listed 7 missing items)
- CC provided specific detail (e.g., "Symbol recognition criteria", "Inter-rater reliability testing")

**Why it matters:**
- Transparency gap documentation
- Guides replication attempts
- Identifies areas needing clarification

**Action:** Keep CC's thorough approach

---

## Implementation Plan

### Phase 1: Root Cause Investigation (Immediate)
**Goal:** Understand why CC found 0 implicit arguments but 4 implicit protocols

**Tasks:**
1. Review skill definition - is implicit argument extraction clearly specified?
2. Review all 5 prompts - do they emphasize implicit arguments equally to implicit protocols?
3. Review WORKFLOW.md - is there guidance on when to extract implicit arguments?
4. Review CC interaction logs - was skill loaded throughout? Any relevant thinking traces?
5. Compare chatbot vs CC prompt differences - could minor changes have had major impact?

**Deliverable:** Diagnosis document explaining the gap

---

### Phase 2: Workflow Updates (After diagnosis)
**Goal:** Fix identified issues in workflow/prompts

**Tasks:**
1. **Add implicit argument extraction:**
   - Decide: Pass 2.5 (after claims rationalization) or Pass 4.5 (after RDMAP rationalization)?
   - Update WORKFLOW.md with explicit pass description
   - Update relevant prompt(s) to emphasize implicit argument detection
   - Add examples/references to skill materials

2. **Clarify research design granularity:**
   - Add section to WORKFLOW.md: "Research Design Granularity Guidance"
   - Provide decision rule: "Each strategic choice requiring separate justification = separate RD"
   - Add examples: platform choice, participant selection, workflow design
   - Update prompt 03 (RDMAP Pass 1) with granularity guidance

3. **Document consolidation philosophy:**
   - Add section to WORKFLOW.md: "Consolidation Decision Rules"
   - Specify: only redundancies and sequential workflow steps
   - Specify: preserve temporal variations, preserve interpretive steps
   - Add counter-examples

**Deliverable:** Updated WORKFLOW.md v2.6.2

---

### Phase 3: Validation on Sobotkova (After updates)
**Goal:** Verify fixes work on already-extracted paper

**Tasks:**
1. **Manual implicit argument extraction:**
   - Read paper with updated guidance
   - Extract implicit arguments targeting ~10 items
   - Compare with chatbot's 10 items
   - Validate approach before automating

2. **Review research designs:**
   - Should CC's 2 designs become 5?
   - Map chatbot's 5 designs to paper sections
   - Determine if granularity guidance would have captured them

3. **Spot-check consolidations:**
   - Review E032-E036: separate productivity calculations - appropriate split? (likely yes)
   - Review C020-C022: approach characteristics - appropriate split? (likely yes)
   - Identify any that should merge (expect 0-2 cases)

**Deliverable:** Validation report confirming fixes are appropriate

---

### Phase 4: Test on New Paper (After validation)
**Goal:** Verify updated workflow works autonomously

**Tasks:**
1. Select new paper (different domain if possible)
2. Run updated workflow autonomously
3. Compare:
   - Implicit arguments extracted (target: similar ratio to chatbot, ~10-15% of claims)
   - Research design granularity (multiple strategic decisions captured?)
   - Consolidation rate (stays conservative, ~3-5%?)

**Deliverable:** Test extraction confirming workflow improvements

---

## Success Criteria

### Must Achieve:
1. **Implicit arguments:** CC extracts implicit arguments at similar rate to chatbot
   - Metric: 8-12 implicit arguments for Sobotkova-type paper
   - Quality: Captures unstated assumptions, disciplinary norms, bridging claims

2. **Research design granularity:** CC captures distinct strategic decisions
   - Metric: 4-6 research designs for Sobotkova-type paper (vs current 2)
   - Quality: Each design represents independent choice point with separate justification

### Should Achieve:
3. **Consolidation validation:** Conservative approach confirmed appropriate
   - Metric: <10% consolidation rate maintained
   - Quality: No unnecessary fragmentation identified, consolidation philosophy documented

### Already Achieved (Preserve):
4. **Comprehensive coverage:** Section-by-section extraction maintains 150%+ evidence capture
5. **Implicit protocol detection:** Continues finding undocumented procedures
6. **Expected information tracking:** Comprehensive transparency gap documentation

---

## Risk Assessment

### Low Risk Items:
- **Consolidation validation:** Likely to confirm current approach is appropriate
- **Expected information tracking:** Already working well, no changes needed
- **Section-by-section extraction:** Core workflow strength, no changes needed

### Medium Risk Items:
- **Research design granularity:** Requires conceptual guidance, not just prompt changes
  - Risk: Guidance too vague, still get holistic designs
  - Mitigation: Provide explicit examples, decision rules, test on validation paper

### High Risk Items:
- **Implicit argument extraction:** Major gap with unclear root cause
  - Risk: Prompt changes don't fix issue if root cause is structural
  - Mitigation: Phase 1 diagnosis before making changes, manual validation before automation

---

## Open Questions for Investigation

1. **Why did CC find implicit protocols but not implicit arguments?**
   - Same prompts, same skill, different results
   - Is it timing (when in workflow implicit detection happens)?
   - Is it emphasis (protocols get explicit guidance, arguments don't)?
   - Is it visibility (protocols mentioned in Results, arguments scattered)?

2. **Was the skill loaded throughout CC extraction?**
   - Auto-compact resets - did skill persist?
   - Check interaction logs for skill invocation patterns
   - Could skill loss mid-extraction explain gaps?

3. **What minor prompt differences exist between chatbot and CC?**
   - Consolidation guidance changes
   - Source quoting requirements
   - Could these have unintended side effects?

4. **Is implicit argument extraction a separate pass or integrated into claims extraction?**
   - Chatbot workflow structure?
   - CC workflow structure?
   - Could process difference explain gap?

---

## Notes for Implementation

### Skill vs Workflow vs Prompts
- **Skill:** High-level decision frameworks and assessment criteria
- **Workflow:** Process structure (5 passes, section-by-section, when to consolidate)
- **Prompts:** Specific extraction instructions for each pass

**Most likely fixes:**
- Implicit arguments: Workflow structure issue (needs dedicated pass) OR prompt emphasis issue
- Research design granularity: Skill/workflow guidance issue (conceptual clarification needed)
- Consolidation: Documentation issue (philosophy needs explicit statement)

### Testing Strategy
**Don't test everything at once:**
1. Diagnose implicit argument gap first (Phase 1)
2. Fix one issue at a time (Phase 2)
3. Validate each fix separately (Phase 3)
4. Integrated test on new paper (Phase 4)

**Rationale:** Multiple simultaneous changes make it hard to identify what fixed (or broke) what

---

## Appendix: Key Comparison Statistics

### Overall Totals
- **Total items:** 85 (CC) vs 64 (chatbot) = +33% CC
- **Claims & Evidence:** 67 (CC) vs 39 (chatbot) = +72% CC
- **RDMAP:** 18 (CC) vs 25 (chatbot) = -28% CC

### By Category
| Category | CC | Chatbot | Difference |
|----------|-----|---------|------------|
| Evidence | 36 | 13 | +177% CC |
| Claims | 31 | 16 | +94% CC |
| Implicit Arguments | 0 | 10 | -100% CC ⚠️ |
| Research Designs | 2 | 5 | -60% CC ⚠️ |
| Methods | 6 | 7 | -14% CC |
| Protocols | 10 | 13 | -23% CC |

### Consolidation Rates
| Category | CC | Chatbot |
|----------|-----|---------|
| Evidence | 0% (0/36) | 54% (28→13) |
| Claims | 3% (32→31) | 69% (51→16) |
| Protocols | 10% (1/10) | 15% (2/13) |

### Quality Metrics (Both 100%)
- Source verification
- Consolidation metadata completeness
- Location tracking

---

**Document Status:** Initial draft for planning purposes
**Next Action:** Phase 1 investigation into implicit argument gap
**Owner:** Shawn + CC collaborative investigation
