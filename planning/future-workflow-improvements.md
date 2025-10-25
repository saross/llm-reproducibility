# Future Workflow Improvements - Deferred from Implicit Arguments Fix
## Based on Chatbot's Extraction Performance Analysis

**Date:** 2025-10-25
**Source:** reports/implicit-arguments/Extraction_Performance_Analysis.md
**Status:** DEFERRED - To be implemented after testing implicit arguments fix
**Context:** Chatbot identified several successful practices that could improve CC autonomous extraction

---

## Overview

During analysis of successful implicit argument extraction, the chatbot provided detailed introspection on what practices enabled high-quality extraction. Several improvements were identified as valuable but deferred to avoid over-complicating the immediate implicit arguments fix.

These improvements should be tested incrementally after validating the implicit arguments fix works.

---

## Deferred Improvements

### 1. Make Fundamentals Reading Mandatory and Early

**Priority:** HIGH
**Source:** Chatbot report lines 200-217
**Estimated Impact:** Prevents 40-50% of sourcing failures

**Current State:**
```markdown
🚨 CRITICAL: Sourcing Requirements
READ FIRST: `/mnt/skills/user/research-assessor/references/extraction-fundamentals.md`
```

**Problem:** Easy to skip or defer reading until hitting an issue.

**Proposed Change (Pass 1 prompt):**
```markdown
## STEP 0: MANDATORY Pre-Extraction (DO THIS FIRST)

Before extraction begins, you MUST:

1. **Read extraction fundamentals:**
   - File: `references/extraction-fundamentals.md`
   - Focus: Internalize the sourcing test: "Can I point to exact text?"

2. **Acknowledge understanding:**
   - State in your first message: "I have read extraction fundamentals and understand the sourcing discipline"
   - Demonstrate: Articulate the sourcing test in your own words

3. **Only then proceed to extraction**

**WITHOUT completing Step 0, extraction will fail sourcing requirements.**

---
```

**Testing Plan:**
- Add to Pass 1 prompt
- Verify CC reads and acknowledges before extracting
- Check if sourcing quality improves

**Success Metric:** 100% of extractions acknowledge fundamentals reading before extraction begins

---

### 2. Strengthen Liberal Extraction Mental Model

**Priority:** MEDIUM
**Source:** Chatbot report lines 235-254
**Estimated Impact:** Reduces over-consolidation and missed items in Pass 1

**Current State:**
```markdown
When uncertain whether something qualifies: INCLUDE IT.
```

**Chatbot's Insight:**
> "The mental model that worked: 'Pass 2 can merge things. Pass 1 cannot recover missed items.'"

**Proposed Addition (Pass 1 prompt, early in Extraction Workflow section):**
```markdown
## Liberal Extraction Mental Model

**Pass 1 job:** CAPTURE (comprehensively)
**Pass 2 job:** CONSOLIDATE (rationally)

**Active rules during Pass 1:**
✓ When uncertain: EXTRACT IT
✓ When granular: KEEP IT SEPARATE
✓ When related items: DON'T CONSOLIDATE YET

**Never think during Pass 1:**
✗ "This seems too detailed for final output"
✗ "These should probably merge"
✗ "I'm over-extracting"

**Remember:** Pass 2 can merge. Pass 1 cannot recover missed items.

---
```

**Testing Plan:**
- Add mental model framing early in Pass 1 prompt
- Monitor Pass 1 extraction counts (should increase slightly)
- Monitor Pass 2 consolidation patterns (should have more to work with)

**Success Metric:** Pass 1 extracts 40-50% more items than final output (current target)

---

### 3. Emphasize Relationship Mapping During Extraction

**Priority:** MEDIUM
**Source:** Chatbot report lines 256-275
**Estimated Impact:** Improves extraction quality and coverage

**Chatbot's Insight:**
> "Relationship mapping during extraction improves item selection quality."
> "Mapping relationships forced me to understand the argumentative structure, not just extract isolated items."

**Proposed Addition (Pass 1 prompt, in Extraction Workflow section):**
```markdown
### Relationship Mapping Discipline

**For EACH evidence item, immediately ask:**
- "What claims does this support?" → populate `supports_claims`
- "What other evidence is related?" → populate `related_evidence`

**For EACH claim, immediately ask:**
- "What evidence supports this?" → populate `supported_by_evidence`
- "What claims does this support/connect to?" → populate `supports_claims`, `supported_by_claims`

**Why map relationships during extraction (not after):**
- Understand each item's argumentative role
- Notice gaps in support (missing evidence)
- Prepare for efficient Pass 2 consolidation (see clusters)

**Do NOT defer relationship mapping to Pass 2.** Map as you extract.

---
```

**Testing Plan:**
- Add to Pass 1 workflow section
- Check extraction.json for populated relationship fields
- Verify relationships aren't added as afterthought

**Success Metric:** 90%+ of items have relationship fields populated in Pass 1

---

### 4. Add Verbatim Quote Quality Standards

**Priority:** MEDIUM
**Source:** Chatbot report lines 303-321
**Estimated Impact:** Prevents paraphrasing drift and improves validation pass rates

**Chatbot's Insight:**
> "Verbatim quote requirement prevented hallucinated evidence, over-interpreted claims, and synthetic aggregations."
> "Copy quotes verbatim (even the 'ca.' in E024). Slight pain, but prevented paraphrasing drift."

**Proposed Addition (Pass 1 prompt, in Sourcing section):**
```markdown
## Verbatim Quote Quality Standards

**What "verbatim" means:**
✓ EXACT reproduction (including "ca.", "about", "perhaps")
✓ Include hedging language ("may", "likely", "suggests")
✓ Include uncertainty markers (ranges, qualifiers)
✓ Copy punctuation precisely

**What to NEVER do:**
✗ Paraphrase (even slightly)
✗ "Clean up" awkward phrasing
✗ Omit qualifiers to make claims stronger
✗ Modernize spelling or terminology

**Self-check:** Could someone find this exact quote by Ctrl+F in the PDF?
**If NO** → You paraphrased. Start over.

**Example of correct verbatim extraction:**
- Paper text: "ca. AUD $2,000"
- Correct quote: "ca. AUD $2,000"
- Incorrect: "approximately AUD $2,000" ❌
- Incorrect: "$2,000" ❌

The "ca." indicates declared uncertainty—capture it exactly.

---
```

**Testing Plan:**
- Add quality standards to Pass 1 prompt
- Run Ctrl+F validation test on sample extraction
- Check validation pass rates improve

**Success Metric:** 100% of verbatim_quotes findable via exact-text search in source PDF

---

### 5. Add Scope Management Guidance

**Priority:** LOW
**Source:** Chatbot report lines 219-232
**Estimated Impact:** Reduces cognitive overload in long papers

**Chatbot's Insight:**
> "Section-by-section extraction isn't just about token limits—it's about cognitive load management."
> "Maintaining sourcing discipline and relationship mapping requires focused attention."

**Proposed Addition (WORKFLOW.md or Pass 1 prompt):**
```markdown
## Extraction Scope Management

**Optimal scope per pass:** 10-20 pages or 2-3 major sections

**For papers >30 pages:**
- Extract section-by-section (already standard)
- Consider mid-extraction breaks between major sections
- Use extraction_notes to track coverage

**For papers <15 pages:**
- May extract multiple sections in single pass
- Still maintain section groupings for cognitive focus

**Why scope matters:**
- Sourcing discipline requires focused attention
- Relationship mapping needs working memory
- Quality degrades beyond cognitive capacity limits

**Warning signs of scope overload:**
- Skipping verbatim quotes (taking shortcuts)
- Deferring relationship mapping ("I'll do it later")
- Consolidating during Pass 1 (trying to reduce cognitive load)

**If you notice these signs:** Take a break, save progress, resume with fresh focus.

---
```

**Testing Plan:**
- Add to WORKFLOW.md or Pass 1 prompt
- Monitor extraction quality across papers of different lengths
- Check if break patterns correlate with quality

**Success Metric:** Consistent quality maintained across long papers (>30 pages)

---

## Implementation Strategy

### Phase 1: Testing Implicit Arguments Fix (Current)
- Implement systematic implicit argument extraction (Pass 1 + Pass 2)
- Validate on 2-3 papers
- Measure: Implicit arguments extracted, quality maintained

**Do NOT implement deferred improvements yet.**

---

### Phase 2: Selective Testing (After Phase 1 Success)

**Test one improvement at a time:**

1. **Start with highest-priority, lowest-risk:**
   - Add: Fundamentals reading requirement (STEP 0)
   - Measure: Sourcing quality improvement
   - Test: 1-2 papers

2. **If successful, add next:**
   - Add: Liberal extraction mental model framing
   - Measure: Pass 1 extraction counts, Pass 2 consolidation patterns
   - Test: 1-2 papers

3. **Continue incrementally:**
   - Add: Relationship mapping emphasis
   - Add: Verbatim quote quality standards
   - Add: Scope management guidance

**After each addition:**
- Validate quality maintained or improved
- Check for unintended side effects
- Document lessons learned

---

### Phase 3: Integration Testing (After All Improvements Tested)

**Full workflow test:**
- Run complete 5-pass extraction on new paper
- Compare quality to baseline (current Sobotkova extraction)
- Assess: Coverage, sourcing quality, relationship mapping, consolidation appropriateness

**Success criteria:**
- Equal or better evidence/claims coverage
- 100% sourcing pass rate (validation)
- Implicit arguments extracted systematically
- No quality degradation from additional requirements

---

## Risks and Mitigation

### Risk 1: Prompt Bloat
**Concern:** Too many requirements overwhelm CC, reduce compliance

**Mitigation:**
- Add improvements incrementally
- Test each individually
- If quality degrades, roll back
- Consider skill refinement vs prompt additions

---

### Risk 2: Diminishing Returns
**Concern:** Later improvements provide minimal benefit

**Mitigation:**
- Measure impact of each improvement
- Stop if marginal gains < implementation cost
- Not all improvements may be necessary

---

### Risk 3: Conflicting Guidance
**Concern:** New requirements contradict existing workflow

**Mitigation:**
- Review full prompt after each addition
- Check for contradictions
- Resolve tensions before testing

---

## Success Metrics Summary

| Improvement | Metric | Target |
|-------------|--------|--------|
| Fundamentals reading | Acknowledgment rate | 100% before extraction |
| Liberal extraction | Pass 1 over-extraction | 40-50% reduction in Pass 2 |
| Relationship mapping | Fields populated in Pass 1 | 90%+ of items |
| Verbatim quotes | Ctrl+F findability | 100% exact matches |
| Scope management | Quality consistency | No degradation in long papers |

---

## Documentation Requirements

For each improvement implemented:

1. **Before:** Baseline measurements on 2-3 papers
2. **After:** Same measurements on 2-3 papers
3. **Analysis:** Impact assessment, trade-offs observed
4. **Decision:** Keep, modify, or revert
5. **Update:** Document final state in WORKFLOW.md

---

## Open Questions

1. **Is STEP 0 too bureaucratic?**
   - Alternative: Inline fundamentals content vs requiring separate read
   - Trade-off: Prompt length vs guaranteed understanding

2. **Should relationship mapping be required or encouraged?**
   - Alternative: Optional vs mandatory field population
   - Trade-off: Quality vs flexibility

3. **Do all improvements belong in prompts?**
   - Alternative: Some might be better in WORKFLOW.md or skill description
   - Trade-off: Visibility vs prompt length

4. **How to test "zone" factors?**
   - Chatbot mentioned being "in the zone" during extraction
   - Can we create conditions for flow state?
   - Or is this inherently variable?

---

## Notes for Future Review

**Chatbot's meta-lesson (lines 325-336):**
> "The extraction went well not despite the constraints but because of them."
> "Each constraint removed a decision burden."
> "The prompt should embrace and strengthen constraints, not apologize for them."

**Implication:** These improvements add constraints (fundamentals reading, verbatim quotes, relationship mapping). Constraints enable quality by reducing cognitive load on decision-making.

**Philosophy:** Clear rules > flexible judgment (for reproducible quality)

---

**Document Status:** Deferred improvements captured for future implementation
**Next Action:** Phase 1 - Test implicit arguments fix
**Review Date:** After successful implicit arguments validation
**Owner:** Shawn + CC collaborative testing
