# Extraction Challenges - Monitoring Log

**Purpose:** Track known potential extraction issues for future monitoring and escalation if they become systematic.

**Status:** All challenges currently at acceptable risk levels with sufficient mitigations.

---

## Challenge 1: Literature Review Misattribution

**Issue:** Accidentally extracting Research Designs from descriptions of PRIOR work (others' designs) instead of current paper's designs.

**First Identified:** 2025-10-25 (during RD extraction fix planning)

**Risk Level:** Moderate
- Not high: LLMs generally good at "they" vs "we" attribution
- Not low: Lit reviews use similar design language to methods sections

### Failure Scenarios

**High Risk:**
```
Lit review: "Previous studies employed comparative case studies (Smith 2020; Jones 2021).
            We build on this tradition to evaluate..."
```
→ **Risk:** "comparative case study" extracted as current paper's design
→ **Ambiguity:** Adopting same design or just contextualizing?

**Lower Risk:**
```
Lit review: "Smith et al. used case studies but lacked quantitative validation."
Methods: "We employed mixed methods to address this gap."
```
→ **Lower risk:** Clear contrast makes attribution obvious

### Current Mitigations

1. **Pass 1 Lit Review Warning** (4 lines in prompt)
   - Explicit warning against extracting prior work
   - Test: "Does this explain strategic choice AUTHORS made?"

2. **Verbatim Quote Requirement**
   - Should capture "Smith et al." or "Prior work" context
   - Makes attribution visible in validation

3. **Location Tracking**
   - Background/Literature Review section tags are signal
   - Validation can flag RDs from lit review sections

4. **"WHY" Test in Prompts**
   - Must explain strategic choice for THIS study
   - Filters out descriptions of others' work

### Monitoring Plan

**Metrics to track:**
- % of RDs per paper that cite prior work instead of current authors
- Section distribution (how many RDs from Background/Lit Review vs Methods/Intro?)

**Escalation Triggers:**
- **Yellow (Review Needed):** >10% of RDs across 5+ papers show misattribution
- **Red (Immediate Action):** >20% of RDs in any single paper show misattribution

**Escalation Actions (if triggered):**
1. Expand to full disambiguation section in `research-design-extraction-guide.md`
2. Add worked examples showing correct vs incorrect attribution
3. Enhance Pass 5 validation checks for author vs cited work distinction
4. Add author-name extraction to project_metadata for cross-reference checking

**Current Status:** 🟢 Green - No action needed
- Mitigations in place (4-line warning + existing safeguards)
- No systematic misattribution observed yet
- Monitor in next 5-10 extractions

---

## Challenge 2: Over-Extraction from Hypothetical Scenarios

**Issue:** Papers discussing "one could also..." or "future work might..." being extracted as current paper's designs.

**Risk Level:** Low-Moderate
- Hypothetical language usually clear in verbatim quotes
- But could confuse what was PLANNED vs what COULD BE done

### Current Mitigations

1. **Verbatim Quote Requirement**
   - Hypothetical language ("could," "might," "future work") visible

2. **Pass 2 Rationalization**
   - Should catch and remove hypotheticals during quality review

### Monitoring Plan

**Metrics to track:**
- Presence of hypothetical language in RD verbatim quotes
- RDs describing future work vs current study

**Escalation Trigger:**
- If >5% of RDs contain hypothetical language across multiple papers

**Escalation Action:**
- Add explicit warning about hypothetical scenarios to Pass 1

**Current Status:** 🟢 Green - Not yet observed, likely caught by existing process

---

## Challenge 3: Limitations Confused with Design Choices

**Issue:** Distinguishing constraints ("We were limited to...") from deliberate choices ("We chose to limit...").

**Risk Level:** Low
- Design requires CHOICE, not just constraint
- But boundary can be subtle if constraints framed as decisions

### Example Ambiguity

**Constraint (Not a Design):** "Due to budget limitations, we surveyed only 50 sites"
**Design (IS a Design):** "We chose to survey 50 sites to balance coverage and depth"

**Tricky Case:** "Given time constraints, we adopted rapid assessment methodology"
→ Is this constraint-driven (not design) or strategic adaptation (is design)?

### Current Mitigations

1. **"WHY" Test**
   - Must explain strategic framing, not just describe constraints

2. **design_text Captures Context**
   - Verbatim quote shows whether justified as choice vs reported as limitation

### Monitoring Plan

**Metrics to track:**
- RDs containing limitation language ("limited to," "due to," "constrained by")
- Context: Are limitations framed as strategic adaptations?

**Escalation Trigger:**
- If constraints being systematically misclassified as designs

**Escalation Action:**
- Add constraint vs choice guidance to extraction guide

**Current Status:** 🟢 Green - Not yet observed

---

## Monitoring Schedule

**Per-extraction review:**
- Quick scan of RDs for lit review citations, hypothetical language, limitation framing
- Flag any concerning patterns

**Every 5 extractions:**
- Calculate metrics for Challenges 1-3
- Check against escalation triggers

**Every 10 extractions:**
- Comprehensive review of RD quality across papers
- Update risk levels and mitigation effectiveness

---

## Escalation Log

**Date:** 2025-10-25
**Action:** Document created, all challenges at Green status
**Next Review:** After 5 extractions completed

---

## Notes

- This document should evolve as new challenges emerge
- Add new challenges as they're identified in practice
- Archive resolved challenges to "Historical" section when mitigated
- Priority: Maintain high RD extraction quality while avoiding over-correction
