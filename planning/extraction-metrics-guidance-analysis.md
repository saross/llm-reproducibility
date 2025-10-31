# Extraction Metrics Guidance Analysis

**Date:** 2025-10-31
**Status:** Analysis / Awaiting Empirical Validation
**Context:** Post-10-extraction reflection on whether numeric targets help or harm extraction quality
**Priority:** MEDIUM - Affects extraction thoroughness and consistency

---

## Overview

This document analyses whether providing specific numeric targets (e.g., "expect 40-50 claims") in extraction prompts helps achieve thorough, consistent extraction or creates perverse incentives that undermine quality.

**Core tension:** We want liberal over-extraction (include borderline items), but numeric targets may cause either premature stopping ("I hit the target, I'm done") or forced extraction ("I need 15 more to hit the target").

---

## The Problem: Two Failure Modes

### 1. Premature Stopping
**Behaviour:** "I found 50 claims, that's the target, I'm done"
**Issue:** Legitimate claims remain unextracted because the count target was reached
**Impact:** Under-extraction despite appearing thorough by numeric standards

### 2. Forced Extraction
**Behaviour:** "I only found 35 claims, I need to find 15 more"
**Issue:** Marginal or inappropriate items extracted just to hit the number
**Impact:** Over-extraction of low-quality items, noise in dataset

### 3. Observed Behaviour
User observation: "I have seen instances of you going back once or twice after seemingly completing a Pass 1 prompt to 'find more' since you hadn't hit the metrics"

**Critical question:** When this happens, am I finding genuinely missed items, or forcing extraction to hit targets?

---

## When Metrics Help vs Harm

### Metrics Are Useful For:

1. **Catching gross under-extraction**
   - 5 claims from a 30-page empirical paper = something is clearly wrong
   - Calibration check that extraction process is working

2. **Calibration across paper types**
   - Helps understand what "thorough" means for this domain
   - Provides context: methodological vs empirical vs theory papers differ

3. **Quality control checks after extraction**
   - Post-hoc anomaly detection
   - Triggers review of outliers, not automatic re-extraction

4. **Progress validation during development**
   - Early extractions: "Are we in the right ballpark?"
   - Workflow refinement: "Did this change improve thoroughness?"

### Metrics Are Harmful When:

1. **Creating implicit ceilings**
   - "Enough" becomes the goal instead of "all relevant items"
   - Satisficing behaviour rather than maximising

2. **Pressuring extraction of borderline items**
   - Quality judgment overridden by numeric goals
   - "I need more, so this marginal statement must count"

3. **Ignoring legitimate paper variation**
   - Short methodological papers genuinely have fewer items
   - Heavy empirical papers genuinely have more items
   - Attempting to normalize ignores real differences

4. **Creating anxiety about "correctness"**
   - Focus shifts from content judgment to count matching
   - Second-guessing legitimate extraction decisions

---

## Alternative Approaches

### Option 1: Lower Bounds Only (Red Flags)

**Approach:** Provide minimum thresholds to catch failures, no upper bounds

```markdown
Expect AT LEAST 30-40 claims for a paper of this length/type.
If you find fewer than 30, review carefully for under-extraction.

NO UPPER LIMIT - extract everything claim-worthy.
80 claims from a dense empirical paper is fine if all are legitimate.
```

**Pros:**
- Catches gross failures
- No ceiling effect
- Still provides calibration context

**Cons:**
- Still creates a number to "beat"
- May encourage extraction of marginal items to clear threshold

---

### Option 2: Density Guidance + Principles

**Approach:** Give rate-based guidance plus qualitative principles

```markdown
Aim for ~2-3 claims per page for empirical papers.
More for dense argumentative papers, fewer for descriptive sections.

Principle: Liberal over-extraction. When in doubt, extract it.
Pass 2 consolidation will rationalise, so err on the side of inclusion.
```

**Pros:**
- Scales naturally with paper length
- Emphasises judgment over counting
- Reinforces workflow design (Pass 2 handles over-extraction)

**Cons:**
- Density estimates can still become targets
- Requires mental arithmetic during extraction

---

### Option 3: Qualitative Guidance Only

**Approach:** Define what to extract by type, no numbers

```markdown
Extract all:
- Interpretations of empirical results
- Methodological assertions and justifications
- Theoretical positions and arguments
- Empirical generalisations and patterns
- Comparative statements across contexts

Include borderline cases - Pass 2 consolidation will handle redundancy.
Better to extract 100 items and consolidate to 60 than to miss 20 items.
```

**Pros:**
- No numeric anchoring
- Focuses on content judgment
- Emphasises extraction principles

**Cons:**
- No calibration check during extraction
- Harder to catch gross under-extraction in progress
- Requires strong qualitative judgment

---

### Option 4: Post-Hoc Calibration Check

**Approach:** No guidance during extraction, check afterwards

```markdown
[No numeric guidance in Pass 1 prompt]

After Pass 1 completion:
1. Count extracted items
2. Compare to expected ranges for paper type/length
3. If anomalous (very high/low), investigate why
4. Review extraction process, not just add/remove to hit target
```

**Pros:**
- No influence on extraction decisions
- Allows natural paper variation
- Diagnostic rather than prescriptive

**Cons:**
- Catches problems after the fact (costly to fix)
- Requires well-calibrated expected ranges
- May miss systematic under-extraction patterns

---

### Option 5: Contextual Ranges with "Why" Thresholds

**Approach:** Provide ranges with explicit reasoning and anti-target warnings

```markdown
## Expected Extraction Scope

### Paper Type: Methodological (15-20 pages)

**Claims:** 20-40 typical range
- If <15: Likely missed argumentative claims in discussion/conclusions
- If >60: May be extracting background statements or general literature claims

**Evidence:** 10-30 typical range
- Methodological papers argue more than they measure
- Evidence often comes from case studies or worked examples
- If <5: May have missed supporting examples or comparative data

### Critical Principle
These ranges are CALIBRATION CHECKS, not targets.
- Do NOT extract or remove items just to hit these numbers
- Paper variation is normal and expected
- Focus on extraction quality, not count matching
- When reviewing anomalous counts, ask "why?" before adjusting
```

**Pros:**
- Provides calibration context
- Explains reasoning behind ranges
- Explicitly warns against using as targets
- Helps catch systematic errors

**Cons:**
- Numbers are still visible and may exert subtle influence
- More complex guidance to process
- Requires paper-type-specific ranges

---

## Recommended Approach

**Combine Option 5 (contextual ranges) + Option 3 (qualitative guidance) + explicit anti-target instruction**

### Structure for Extraction Prompts

```markdown
## Extraction Guidance

### 1. What to Extract (PRIMARY)
[Detailed qualitative guidance on claim/evidence types]

Principle: Liberal over-extraction
- When in doubt, include it
- Pass 2 consolidation handles redundancy and over-extraction
- Better to extract 100 items and rationalize to 60 than miss 20

### 2. Calibration Context (SECONDARY - for self-assessment only)
Based on [paper type] and [length]:
- Claims: [range] expected
- Evidence: [range] expected

**How to use these ranges:**
- DURING extraction: Ignore these numbers, focus on content
- AFTER extraction: If your counts are far outside ranges, review process
  - Very low: Did I miss a section? Under-extract a specific type?
  - Very high: Did I include trivial statements? Extract background lit?

**What NOT to do:**
- Do not extract items just to reach a number
- Do not stop extracting when you hit a number
- Do not treat ranges as targets or goals

### 3. Paper Variation is Normal
- Methodological papers: More claims, less evidence
- Heavy empirical papers: More evidence, fewer interpretive claims
- Long papers: Naturally have more items
- Short papers: Naturally have fewer items

Trust your content judgment over count matching.
```

---

## Questions for Empirical Validation

Before implementing changes, analyse the 10 completed extractions:

### Count Distribution Analysis
1. What are the actual claim/evidence counts across the 10 papers?
2. Do they cluster or vary widely?
3. Can we identify paper-type patterns (methodological vs empirical)?

### Quality Assessment
4. Which extractions feel "goldilocks" (thorough but not inflated)?
5. Which feel under-extracted (obvious gaps)?
6. Which feel over-extracted (trivial items included)?

### Granularity Assessment
7. Are some extractions more granular than others?
8. Is there consistency in what counts as "one claim" vs "one evidence item"?
9. Do consolidation rates (Pass 2) reveal over-extraction patterns?

### Correlation Analysis
10. Do higher counts correlate with better quality, or just more noise?
11. Does paper length predict item counts linearly, or do other factors matter more?

### Prompt Influence Assessment
12. Can we identify extractions where numeric targets influenced decisions?
13. Are there cases of obvious "stopping at the target" behaviour?
14. Are there cases of forced extraction to hit targets?

---

## Implementation Considerations

### If Dropping Numeric Guidance:

**Benefits:**
- Removes perverse incentives
- Allows natural paper variation
- Focuses on content quality

**Risks:**
- May lose calibration check during extraction
- Harder to catch systematic under-extraction
- Requires strong post-hoc quality assessment

**Mitigation:**
- Develop robust post-Pass 1 anomaly detection
- Use qualitative completeness checks (did I cover all sections equally?)
- Periodic spot-checking across extractions

### If Keeping Numeric Guidance:

**Requirements:**
- Explicit anti-target framing
- Contextualized by paper type
- Positioned as secondary to qualitative judgment
- Accompanied by "why" reasoning for ranges

**Risks:**
- Numbers still exert subtle influence
- Requires ongoing calibration as corpus diversifies
- May create false precision (ranges are estimates)

**Mitigation:**
- Test different framing approaches
- Monitor for target-seeking behaviour
- Regular review of whether guidance helps or harms

---

## Related Work

This connects to:
- **Sobotkova-specific metrics removal** (planning/active-todo-list.md, Section 5): Are current ranges calibrated to one paper?
- **Liberal over-extraction principle** (input/WORKFLOW.md, Mandatory Component #4): How do we balance "extract more" with "not everything"?
- **Pass 2 consolidation** (WORKFLOW.md, Pass 2): Designed to handle over-extraction, so numeric precision in Pass 1 may be unnecessary

---

## Next Steps

1. **Empirical analysis of 10 completed extractions:**
   - Count distributions by paper type
   - Quality assessment (goldilocks, under-, over-extraction)
   - Granularity consistency check
   - Evidence of target-seeking behaviour

2. **Decision based on evidence:**
   - If extractions are consistent and thorough → current approach working, keep ranges
   - If extractions show target-seeking → reframe or remove numeric guidance
   - If extractions are inconsistent → may need clearer qualitative guidance

3. **Implementation:**
   - Update extraction prompts based on empirical findings
   - Test revised approach on 2-3 new papers
   - Monitor for improvement/degradation

4. **Documentation:**
   - Record decision rationale
   - Update WORKFLOW.md if guidance changes
   - Add to EXTRACTION_PLAN_UNIFIED_MODEL.md

---

## Key Principle

**Metrics should serve extraction quality, not define it.**

If numeric guidance helps achieve thorough, consistent extraction → keep it with careful framing
If numeric guidance creates perverse incentives → remove it in favour of qualitative principles

The 10-extraction corpus provides empirical evidence to make this decision wisely.
