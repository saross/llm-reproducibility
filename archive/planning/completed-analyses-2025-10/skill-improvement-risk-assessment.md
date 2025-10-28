# Risk Assessment: Prompt-to-Skill Content Migration

**Date**: 2025-10-27
**Scope**: Detailed risk analysis for 313 lines of content migration from prompts to skill
**Purpose**: Address user concern: "eager to realise gains but worry about risk, especially loss of fidelity/comprehensiveness"

---

## Executive Summary

**Overall Risk Assessment**: ACCEPTABLE with proper mitigations and phased approach

**Key Finding**: Risk varies significantly by content type:
- **Phase A (Duplications)**: Genuinely LOW risk - content already exists elsewhere
- **Phase B (Frameworks)**: MEDIUM risk - but manageable and worthwhile
- **Phase C (Optional)**: LOW risk

**Recommendation**: Proceed with **revised phased approach** that splits Phase B into lower-risk and higher-risk subsets, with incremental testing between phases.

---

## Risk Definition Framework

### What Makes Something "Low-Risk"?

✅ Content **already exists** in skill (just removing duplication)
✅ Simple, unambiguous guidance (one test, clear rules)
✅ Affects **limited scope** (domain-specific, verification only)
✅ Natural fit in existing reference file
✅ Claude reliably follows references in testing

### What Makes Something "Medium-Risk"?

⚠️ Content being **relocated** from prompts to skill (not mere duplication)
⚠️ Complex frameworks with **multiple categories/patterns**
⚠️ **Critical for extraction quality** (boundary decisions, consolidation patterns)
⚠️ Creating new reference files or major file enhancements
⚠️ Depends on Claude reading comprehensive reference

### What Would Make Something "High-Risk"?

🚫 Removing content **without preserving** it
🚫 Breaking workflow orchestration
🚫 Over-abstracting prompts (losing actionability)
🚫 Creating circular dependencies

**NONE of our proposed changes are HIGH RISK** - we're preserving and enhancing, not deleting.

---

## Detailed Risk Analysis by Content Item

### PHASE A: Critical Duplications (89 lines total)

#### A1: Evidence vs Claims Distinction (30 lines)

**Current State**:
- Location 1: SKILL.md lines 148-160 (13 lines)
- Location 2: Prompt 01 lines 106-122 (17 lines, more examples)

**Proposed Action**: Remove from both, create `references/checklists/evidence-vs-claims-guide.md`

**Risk Level**: **LOW** ✅

**Specific Risks**:
1. **Reference not followed** - Claude might skip reading the reference
   - **Likelihood**: LOW (we've tested reference following extensively)
   - **Impact**: MEDIUM (boundary errors would occur)

2. **Incomplete migration** - New file missing edge cases from either location
   - **Likelihood**: LOW (we control migration)
   - **Impact**: LOW (can verify completeness)

**Fidelity/Comprehensiveness Risks**:
- **Fidelity**: LOW - content exists in two places, we're synthesising both versions
- **Comprehensiveness**: LOW - can ensure new file is MORE comprehensive than either source

**Mitigations**:
1. Include ALL content from both SKILL.md and Prompt 01 in new file
2. Add examples from both locations
3. Add worked examples not in either current location
4. Test: Run extraction and verify boundary decisions still correct
5. Prominent reference placement in Prompt 01

**Testing Approach**: Run Pass 1 extraction, check evidence/claims classifications

---

#### A2: RDMAP Hierarchy Decision Tree (39 lines)

**Current State**:
- Location 1: tier-assignment-guide.md (already has comprehensive treatment)
- Location 2: Prompt 03 lines 146-184 (decision tree + tier definitions)

**Proposed Action**: Remove from Prompt 03, reference tier-assignment-guide.md

**Risk Level**: **VERY LOW** ✅

**Specific Risks**:
1. **Prompt 03 too abstract** - Users might not know to read reference
   - **Likelihood**: LOW (reference already used in other prompts)
   - **Impact**: LOW (content already in skill)

**Fidelity/Comprehensiveness Risks**:
- **Fidelity**: VERY LOW - content ALREADY EXISTS in tier-assignment-guide.md
- **Comprehensiveness**: NONE - tier-assignment-guide.md is more comprehensive than prompt version

**Mitigations**:
1. Clear, prominent reference: "See tier-assignment-guide.md for complete decision tree"
2. Keep brief overview (2-3 lines): "WHY → Design, WHAT → Method, HOW → Protocol"
3. Test: Run RDMAP Pass 1, verify tier assignments

**Testing Approach**: Run RDMAP Pass 1 extraction, verify tier classifications

---

#### A3: Tier Definitions Verification (20 lines)

**Current State**:
- Location 1: tier-assignment-guide.md (comprehensive tier guidance)
- Location 2: Prompt 04 lines 199-223 (tier indicators for verification)

**Proposed Action**: Remove tier definitions from Prompt 04, keep verification workflow

**Risk Level**: **VERY LOW** ✅

**Specific Risks**:
1. **Verification becomes less effective** - Without tier definitions in prompt
   - **Likelihood**: VERY LOW (definitions in referenced file)
   - **Impact**: LOW (verification would still happen)

**Fidelity/Comprehensiveness Risks**:
- **Fidelity**: VERY LOW - we're removing repetition, not content
- **Comprehensiveness**: NONE - reference file has more complete guidance

**Mitigations**:
1. Keep verification WORKFLOW in Prompt 04: "Check each item against tier criteria"
2. Reference tier-assignment-guide.md for tier definitions
3. Test: Run RDMAP Pass 2, verify tier corrections still happen

**Testing Approach**: Run RDMAP Pass 2 with deliberately mis-tiered items, verify corrections

---

**PHASE A OVERALL ASSESSMENT**:

| Metric | Assessment |
|--------|------------|
| **Overall Risk** | LOW ✅ |
| **Fidelity Risk** | VERY LOW (content preserved, just relocated) |
| **Comprehensiveness Risk** | NONE (reference files more comprehensive) |
| **Implementation Effort** | 1-2 hours |
| **Testing Effort** | 2-3 hours (Pass 1 + RDMAP Pass 1 + RDMAP Pass 2) |
| **Reversibility** | HIGH (easy to restore if needed) |

**Recommendation**: **PROCEED** - This is genuinely low-risk duplication removal.

---

### PHASE B: Conceptual Frameworks (204 lines total)

**Note**: This phase has MORE VARIABLE risk across candidates. Recommendation is to split into B-1 and B-2.

#### B1: Claims Hierarchy (22 lines)

**Current State**: Prompt 01 lines 139-160 only

**Proposed Action**: Create `references/checklists/claims-hierarchy-guide.md`, reference from Prompts 01 and 02

**Risk Level**: **MEDIUM-LOW** ⚠️

**Specific Risks**:
1. **Reference not read during Pass 1** - Claude skips reading, doesn't understand hierarchy
   - **Likelihood**: LOW-MEDIUM (depends on prompt salience)
   - **Impact**: MEDIUM (claim tier assignments incorrect)

2. **Incomplete framework** - New file missing nuances from prompt
   - **Likelihood**: LOW (we control migration)
   - **Impact**: MEDIUM (hierarchy extraction quality)

**Fidelity/Comprehensiveness Risks**:
- **Fidelity**: MEDIUM - Current placement ensures Pass 1 ALWAYS sees this
  - After move, depends on Claude reading reference when uncertain
- **Comprehensiveness**: LOW-MEDIUM - Can make reference MORE comprehensive
  - But need to ensure worked examples, edge cases included

**Mitigations**:
1. Make reference file MORE comprehensive than prompt (add worked examples, decision trees)
2. Reference from BOTH Prompt 01 (Pass 1) AND Prompt 02 (Pass 2)
3. Add prominent section in SKILL.md navigation
4. Keep very brief reminder in Prompt 01: "Identify 4-level hierarchy (Core/Intermediate/Supporting/Evidence) - see claims-hierarchy-guide.md for guidance"
5. Test with paper that has complex claim structure

**Testing Approach**:
- Run Pass 1 on paper with complex claims (multi-tier)
- Verify claim tier assignments correct
- Check that intermediate claims properly identified

---

#### B2: Multi-Dimensional Evidence Pattern (35 lines)

**Current State**: Prompt 02 lines 134-168 only

**Proposed Action**: Move to `consolidation-patterns.md` as new section

**Risk Level**: **MEDIUM** ⚠️

**Specific Risks**:
1. **Pattern not applied during Pass 2** - Claude misses analytical views approach
   - **Likelihood**: MEDIUM (complex pattern, easy to miss)
   - **Impact**: MEDIUM-HIGH (over-consolidation or missed analytical views)

2. **Pattern gets lost in large file** - consolidation-patterns.md already substantial
   - **Likelihood**: LOW-MEDIUM (depends on organisation)
   - **Impact**: MEDIUM (as above)

**Fidelity/Comprehensiveness Risks**:
- **Fidelity**: MEDIUM-HIGH - This pattern handles subtle edge cases
  - Missing it → poorer consolidation decisions
- **Comprehensiveness**: MEDIUM - Need to ensure reference includes:
  - Decision framework (when to use vs when not)
  - JSON examples
  - Multiple worked examples from real papers

**Mitigations**:
1. Add as PROMINENT new section in consolidation-patterns.md with clear header
2. Include comprehensive decision tree: when to create analytical views vs consolidate vs keep separate
3. Add multiple worked examples (minimum 3)
4. Keep brief mention in Prompt 02: "For multi-dimensional evidence (same observation, multiple analytical dimensions), see consolidation-patterns.md Multi-Dimensional Evidence section"
5. Test with paper that has multi-dimensional evidence

**Testing Approach**:
- Run Pass 2 on paper with multi-dimensional evidence
- Verify analytical views created appropriately
- Check that temporal comparisons NOT consolidated (related pattern)

---

#### B3: Description vs Argumentation Boundary (17 lines)

**Current State**: Prompt 03 lines 189-205 only

**Proposed Action**: Add to `tier-assignment-guide.md` as new section (or create rdmap-vs-claims-guide.md)

**Risk Level**: **MEDIUM-LOW** ⚠️

**Specific Risks**:
1. **Boundary errors** - RDMAP misclassified as claims or vice versa
   - **Likelihood**: LOW-MEDIUM (boundary is conceptually simple but critical)
   - **Impact**: MEDIUM (broken claim/RDMAP separation)

**Fidelity/Comprehensiveness Risks**:
- **Fidelity**: MEDIUM - Critical boundary for extraction accuracy
  - But conceptually simple (one test: "describing HOW vs arguing about effectiveness")
- **Comprehensiveness**: LOW - Test is clear, just needs examples

**Mitigations**:
1. Add to tier-assignment-guide.md with PROMINENT section heading
2. Include MANY examples (good: methodological descriptions, bad: effectiveness arguments)
3. Include worked examples from real papers
4. Keep test in Prompt 03: "Is this describing HOW research was done, or ARGUING about how well it worked? See tier-assignment-guide.md"
5. Test with paper that has method-effectiveness claims

**Testing Approach**:
- Run RDMAP Pass 1
- Check that effectiveness arguments NOT extracted as RDMAP
- Verify methodological descriptions correctly identified

---

#### B4: Reasoning Approach Classification (29 lines)

**Current State**: Prompt 03 lines 207-235 only

**Proposed Action**: Move to `research-design-operational-guide.md` as new section

**Risk Level**: **MEDIUM** ⚠️

**Specific Risks**:
1. **Misclassification of reasoning approaches** - Inductive/abductive/deductive/mixed/unclear
   - **Likelihood**: MEDIUM (subtle distinctions, especially mixed vs unclear)
   - **Impact**: MEDIUM (incorrect research design characterisation)

2. **Hypothesis timing errors** - Pre-data vs post-data inference incorrect
   - **Likelihood**: MEDIUM (requires careful analysis)
   - **Impact**: MEDIUM (affects deductive reasoning assessment)

**Fidelity/Comprehensiveness Risks**:
- **Fidelity**: MEDIUM - Complex framework with 5 categories + timing inference
  - Getting this wrong → incorrect RD characterisation (affects assessment)
- **Comprehensiveness**: MEDIUM - Need to ensure reference includes:
  - Clear definitions of each approach
  - Indicators for each
  - Timing basis guidance
  - Confidence assessment guidance
  - Mixed vs unclear distinction

**Mitigations**:
1. Comprehensive treatment in research-design-operational-guide.md
2. Include decision trees for each approach
3. Add hypothesis timing guidance with indicators
4. Include many examples from real papers (one per approach type)
5. Reference from BOTH Prompt 03 (Pass 1) AND Prompt 04 (Pass 2 verification)
6. Test with papers of different reasoning approaches

**Testing Approach**:
- Run RDMAP Pass 1 on papers with known reasoning approaches
- Verify classifications correct
- Check hypothesis timing inference accurate

---

#### B5: Research Questions vs Hypotheses (21 lines)

**Current State**: Prompt 03 lines 237-257 only

**Proposed Action**: Move to `research-design-operational-guide.md` with B4

**Risk Level**: **MEDIUM-LOW** ⚠️

**Specific Risks**:
1. **RQ vs hypothesis misclassification**
   - **Likelihood**: LOW (distinction clearer than reasoning approaches)
   - **Impact**: LOW-MEDIUM (affects RD characterisation but less critical)

**Fidelity/Comprehensiveness Risks**:
- **Fidelity**: LOW-MEDIUM - Important but straightforward distinction
- **Comprehensiveness**: LOW - Clear criteria, just needs examples

**Mitigations**:
1. Include in same section as B4 (related content)
2. Add examples of each
3. Include timing inference guidance
4. Test with papers that have RQs vs hypotheses

**Testing Approach**: Included in B4 testing

---

#### B6: Fieldwork Considerations (20 lines)

**Current State**: Prompt 03 lines 289-308 only

**Proposed Action**: Move to `research-design-operational-guide.md` as new section

**Risk Level**: **LOW-MEDIUM** ⚠️

**Specific Risks**:
1. **Opportunistic decisions under-extracted** - For fieldwork papers
   - **Likelihood**: MEDIUM for fieldwork papers, N/A for non-fieldwork
   - **Impact**: LOW-MEDIUM (affects subset of papers)

**Fidelity/Comprehensiveness Risks**:
- **Fidelity**: LOW-MEDIUM - Only affects fieldwork papers
  - Not critical for non-fieldwork research
- **Comprehensiveness**: LOW - Can enhance with more patterns

**Mitigations**:
1. Clear section in research-design-operational-guide.md: "Fieldwork-Specific Patterns"
2. Add examples from fieldwork papers
3. Optional mention in Prompt 03: "For fieldwork papers, see fieldwork patterns in research-design-operational-guide.md"
4. Test with fieldwork paper (Sobotkova et al. 2023)

**Testing Approach**:
- Run RDMAP Pass 1 on Sobotkova et al. 2023
- Verify opportunistic decisions extracted
- Check for emergent discovery patterns

---

#### B7: RDMAP Consolidation Patterns (45 lines, 6 patterns)

**Current State**: Prompt 04 lines 150-194 only

**Proposed Action**: Move to `consolidation-patterns.md` as new "RDMAP Consolidation Patterns" section

**Risk Level**: **MEDIUM** ⚠️

**Specific Risks**:
1. **Patterns not applied during RDMAP Pass 2** - Each of 6 patterns missed
   - **Likelihood**: MEDIUM (multiple patterns, complexity)
   - **Impact**: MEDIUM-HIGH (poor RDMAP consolidation quality)

2. **Over-consolidation or under-consolidation** - Without pattern guidance
   - **Likelihood**: MEDIUM
   - **Impact**: MEDIUM (RDMAP granularity incorrect)

**Fidelity/Comprehensiveness Risks**:
- **Fidelity**: MEDIUM-HIGH - These 6 patterns guide RDMAP Pass 2 quality
  - Missing them → poor consolidation decisions
- **Comprehensiveness**: MEDIUM - Need ALL 6 patterns with examples:
  1. Design Rationale Synthesis
  2. Scope Definition Consolidation
  3. Workflow Method Aggregation
  4. Validation Chain Consolidation
  5. Protocol Specification Consolidation
  6. Parameter Aggregation

**Mitigations**:
1. Add comprehensive new section to consolidation-patterns.md
2. Include all 6 patterns with clear headers
3. Add examples for each pattern
4. Include decision guidance for each
5. Prompt 04 line 119 ALREADY references consolidation-patterns.md - just enhance that reference to point to RDMAP section
6. Test with RDMAP Pass 2

**Testing Approach**:
- Run RDMAP Pass 2 on paper with over-extracted RDMAP
- Verify appropriate consolidations using each pattern type
- Check granularity appropriate for tier (Design high-level, Protocol detailed)

---

#### B8: Reasoning Verification (15 lines)

**Current State**: Prompt 04 lines 269-283 only

**Proposed Action**: Move to `research-design-operational-guide.md` with B4

**Risk Level**: **LOW** ✅

**Specific Risks**:
1. **Verification skipped** - Reasoning approach not verified in Pass 2
   - **Likelihood**: LOW (verification workflow stays in Prompt 04)
   - **Impact**: LOW (Pass 1 usually correct anyway)

**Fidelity/Comprehensiveness Risks**:
- **Fidelity**: LOW - Verification guidance, naturally belongs with classification
- **Comprehensiveness**: LOW - Straightforward verification steps

**Mitigations**:
1. Include as subsection under B4 (Reasoning Approach Classification)
2. Keep verification workflow in Prompt 04
3. Test included in B4 testing

**Testing Approach**: Included in B4 testing

---

**PHASE B OVERALL ASSESSMENT**:

| Candidate | Risk Level | Fidelity Risk | Comprehensiveness Risk | Effort |
|-----------|------------|---------------|------------------------|--------|
| B1: Claims Hierarchy | MEDIUM-LOW | MEDIUM | LOW-MEDIUM | 1-2h |
| B2: Multi-Dimensional Evidence | MEDIUM | MEDIUM-HIGH | MEDIUM | 1-2h |
| B3: Description vs Argumentation | MEDIUM-LOW | MEDIUM | LOW | 1h |
| B4: Reasoning Approach | MEDIUM | MEDIUM | MEDIUM | 2h |
| B5: RQ vs Hypotheses | MEDIUM-LOW | LOW-MEDIUM | LOW | 1h |
| B6: Fieldwork | LOW-MEDIUM | LOW-MEDIUM | LOW | 1h |
| B7: RDMAP Consolidation | MEDIUM | MEDIUM-HIGH | MEDIUM | 2h |
| B8: Reasoning Verification | LOW | LOW | LOW | 0.5h |

**Overall Phase B**: MEDIUM risk, but MANAGEABLE with proper mitigations and testing

**Recommendation**: **SPLIT PHASE B** into lower-risk and higher-risk subsets (see Revised Phased Approach below)

---

### PHASE C: Optional Polish (20 lines)

#### C1: Calculation Claims Pattern (20 lines)

**Current State**: Prompt 02 lines 222-241 (Pass 2 rationalization pattern)

**Proposed Action**: Add to `consolidation-patterns.md` as "Common Over-Extraction Patterns" section

**Risk Level**: **LOW** ✅

**Specific Risks**:
1. **Redundant calculation claims not removed** - Pattern not applied
   - **Likelihood**: LOW (pattern is clear)
   - **Impact**: LOW (minor quality issue, not critical)

**Fidelity/Comprehensiveness Risks**:
- **Fidelity**: LOW - Nice-to-have pattern, not critical
- **Comprehensiveness**: VERY LOW - Simple pattern, easy to document

**Mitigations**:
1. Add clear section to consolidation-patterns.md
2. Include examples (remove vs keep)
3. Test with Pass 2 extraction

**Testing Approach**: Run Pass 2, check for redundant calculation claims

---

**PHASE C OVERALL ASSESSMENT**: LOW risk, optional enhancement

---

## Revised Phased Approach with Risk Mitigation

### Phase A: Critical Duplications (89 lines)

**Risk**: LOW ✅
**Effort**: 1-2 hours implementation + 2-3 hours testing
**Reversibility**: HIGH

**Contents**:
1. Evidence vs Claims (30 lines) → Create evidence-vs-claims-guide.md
2. RDMAP Hierarchy (39 lines) → Reference tier-assignment-guide.md
3. Tier Verification (20 lines) → Reference tier-assignment-guide.md

**Testing**:
- Run Pass 1 → verify evidence/claims boundary
- Run RDMAP Pass 1 → verify tier assignments
- Run RDMAP Pass 2 → verify tier corrections

**Decision Point**: Proceed if all tests pass

---

### Phase B-1: Lower-Risk Framework Migrations (93 lines)

**Risk**: LOW-MEDIUM ⚠️
**Effort**: 3-4 hours implementation + 3-4 hours testing
**Reversibility**: HIGH

**Contents** (enhancing EXISTING files):
1. Description vs Argumentation (17 lines) → tier-assignment-guide.md
2. RQ vs Hypotheses (21 lines) → research-design-operational-guide.md
3. Reasoning Approach Classification (29 lines) → research-design-operational-guide.md
4. Reasoning Verification (15 lines) → research-design-operational-guide.md
5. Fieldwork Considerations (20 lines) → research-design-operational-guide.md

**Why lower-risk**:
- All go into EXISTING reference files (no new files)
- Content naturally fits in target files
- Lower complexity frameworks
- Some are domain-specific (fieldwork) = limited scope

**Testing**:
- Run RDMAP Pass 1 on Sobotkova et al. 2023 → verify all patterns applied
- Run RDMAP Pass 2 → verify reasoning verification works
- Check RDMAP vs claims boundary accurate

**Decision Point**: Proceed to B-2 if tests pass and quality maintained

---

### Phase B-2: Higher-Risk Framework Migrations (111 lines)

**Risk**: MEDIUM ⚠️
**Effort**: 4-5 hours implementation + 4-5 hours testing
**Reversibility**: MEDIUM

**Contents** (NEW file + major enhancements):
1. Claims Hierarchy (22 lines) → CREATE claims-hierarchy-guide.md
2. Multi-Dimensional Evidence (35 lines) → consolidation-patterns.md (major enhancement)
3. RDMAP Consolidation Patterns (45 lines, 6 patterns) → consolidation-patterns.md (major enhancement)

**Why higher-risk**:
- Creating new file (claims-hierarchy-guide.md)
- Major enhancements to consolidation-patterns.md (+170 lines)
- Complex, multi-pattern frameworks
- Critical for Pass 2 consolidation quality

**Testing**:
- Run Pass 1 on complex claims paper → verify hierarchy extraction
- Run Pass 2 on evidence with multi-dimensional cases → verify analytical views
- Run RDMAP Pass 2 on over-extracted RDMAP → verify all 6 patterns applied

**Decision Point**: User approval needed; can skip if risk seems too high

---

### Phase C: Optional Polish (20 lines)

**Risk**: LOW ✅
**Effort**: 1 hour implementation + 1 hour testing

**Contents**:
1. Calculation Claims Pattern (20 lines) → consolidation-patterns.md

**Testing**: Run Pass 2, check redundant calculations removed

---

## Overall Testing Strategy

### Incremental Testing Checkpoints

**After Phase A**:
1. Run Pass 1 Claims/Evidence extraction
2. Run RDMAP Pass 1 extraction
3. Run RDMAP Pass 2 rationalization
4. **Verify**: Reference resolution works, extraction quality unchanged

**After Phase B-1**:
1. Run full RDMAP Pass 1 on Sobotkova et al. 2023
2. Run RDMAP Pass 2
3. **Verify**: All patterns applied, quality maintained, RD classification accurate

**After Phase B-2**:
1. Run full Pass 1 Claims/Evidence
2. Run full Pass 2 Claims/Evidence
3. Run full RDMAP Pass 1-2
4. **Comprehensive verification**: Compare to baseline extraction, check all patterns applied

**After Phase C**:
1. Run Pass 2
2. **Verify**: Redundant claims removed

### Test Paper

**Recommendation**: Use **Sobotkova et al. 2023**
- Already extracted multiple times (known baseline)
- Complex enough to test all patterns
- Fieldwork paper (tests B6)
- Has multi-dimensional evidence (tests B2)
- Has complex claims (tests B1)
- Has over-extracted RDMAP (tests B7)

### Success Criteria

**Phase A Pass Criteria**:
- ✅ All references resolve correctly
- ✅ Evidence/claims boundary maintained
- ✅ Tier assignments correct
- ✅ No extraction quality degradation

**Phase B-1 Pass Criteria**:
- ✅ All RDMAP patterns applied
- ✅ RD classification accurate
- ✅ Reasoning approach correct
- ✅ Fieldwork patterns extracted
- ✅ Quality maintained vs baseline

**Phase B-2 Pass Criteria**:
- ✅ Claims hierarchy correctly extracted
- ✅ Analytical views created appropriately
- ✅ RDMAP consolidation uses all 6 patterns
- ✅ Consolidation quality maintained
- ✅ No over/under consolidation vs baseline

**Phase C Pass Criteria**:
- ✅ Redundant calculation claims removed

---

## Fidelity/Comprehensiveness Risk Summary

### How Fidelity Could Be Lost

1. **Reference not read** → Pattern/framework not applied → Lower quality extraction
   - **Mitigation**: Prominent references, brief reminders in prompts, comprehensive reference files

2. **Incomplete migration** → Reference file missing edge cases → Some patterns missed
   - **Mitigation**: Ensure reference files MORE comprehensive than prompt versions, add examples

3. **Over-abstraction** → Prompts too abstract → Extraction unclear
   - **Mitigation**: Keep workflow orchestration in prompts, move only conceptual content

### How Comprehensiveness Could Be Lost

1. **Content accidentally dropped** → Framework incomplete in reference
   - **Mitigation**: Careful migration, verify all content preserved

2. **Examples lost** → Reference file less illustrative than prompt
   - **Mitigation**: Add MORE examples in references than prompts had

3. **Context lost** → Framework separated from application
   - **Mitigation**: Keep application workflow in prompts, enhance context in references

### Overall Assessment

**Fidelity Risk**: MANAGEABLE
- Phase A: VERY LOW (duplication removal)
- Phase B-1: LOW-MEDIUM (existing files, lower complexity)
- Phase B-2: MEDIUM (new files, complex patterns)
- Mitigation: Comprehensive references + testing

**Comprehensiveness Risk**: LOW
- We control migration → can ensure reference files MORE comprehensive
- Add examples, decision trees, worked cases
- Test against baseline to verify

---

## Recommendation Summary

### Proceed With Confidence

1. **Phase A**: APPROVE - Genuinely low-risk, high-value duplication removal
2. **Phase B-1**: APPROVE - Lower-risk framework migrations, enhancing existing files
3. **Phase B-2**: APPROVE with caution - Higher-risk but manageable, creates new comprehensive references
4. **Phase C**: OPTIONAL - Low-risk polish, implement if time permits

### Implementation Order

```text
Phase A (LOW risk)
  ↓ TEST → pass?
  ↓ YES
Phase B-1 (LOW-MEDIUM risk)
  ↓ TEST → pass?
  ↓ YES
Phase B-2 (MEDIUM risk) ← User decision point
  ↓ TEST → pass?
  ↓ YES
Phase C (LOW risk, optional)
```

### Total Effort Estimate

| Phase | Implementation | Testing | Total | Risk |
|-------|----------------|---------|-------|------|
| A | 1-2h | 2-3h | 3-5h | LOW |
| B-1 | 3-4h | 3-4h | 6-8h | LOW-MEDIUM |
| B-2 | 4-5h | 4-5h | 8-10h | MEDIUM |
| C | 1h | 1h | 2h | LOW |
| **TOTAL** | **9-12h** | **10-13h** | **19-25h** | **Manageable** |

### Key Success Factors

1. ✅ **Comprehensive reference files** - Make them BETTER than prompts
2. ✅ **Prominent references** - Ensure Claude sees pointers
3. ✅ **Incremental testing** - Catch issues early
4. ✅ **Baseline comparison** - Use Sobotkova et al. 2023
5. ✅ **Reversibility** - Can restore if needed

### Risk Acceptance

**Is the risk worth it?**

**YES** - Because:
- ✅ Eliminates 89 lines of duplication (CRITICAL)
- ✅ Centralises decision frameworks (maintainability)
- ✅ Reduces prompt size by 13% (efficiency)
- ✅ Creates reusable, comprehensive references
- ✅ Better separation of concerns
- ✅ Risk is manageable with testing
- ✅ Phased approach allows stopping if issues arise

**The gains justify the carefully managed risk.**

---

## Questions for User Decision

1. **Risk tolerance confirmation**: Does this risk assessment align with your comfort level? Any concerns about the MEDIUM-risk items in Phase B-2?

2. **Testing approach approval**: Is using Sobotkova et al. 2023 as baseline acceptable? Should we test on multiple papers?

3. **Phased approval**: Should we proceed with:
   - Phase A immediately (LOW risk)?
   - Phase B-1 after A passes (LOW-MEDIUM risk)?
   - Phase B-2 after user review of B-1 results (MEDIUM risk)?
   - Phase C as optional polish?

4. **Stop points**: If Phase B-1 testing reveals unexpected issues, should we stop or continue to B-2?

5. **Success criteria**: Are the defined pass criteria sufficient, or should we add additional verification steps?

---

## Conclusion

The proposed prompt-to-skill migration carries **acceptable, manageable risk** when implemented in phases with proper mitigations and testing.

**Key findings**:
- Phase A (duplications): Genuinely LOW risk - should proceed
- Phase B-1 (lower-risk frameworks): LOW-MEDIUM risk - manageable
- Phase B-2 (higher-risk frameworks): MEDIUM risk - requires care but worthwhile
- Phase C (optional): LOW risk

**Fidelity/comprehensiveness concerns are addressable** through:
- Comprehensive reference files (MORE content than prompts)
- Prominent references with brief reminders
- Incremental testing with baseline comparison
- Reversibility if issues arise

**Recommendation**: **PROCEED** with revised phased approach (A → B-1 → B-2 → C) with testing checkpoints between phases.
