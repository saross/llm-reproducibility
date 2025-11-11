# Spot-Check Analysis: Extraction Rate Comparison

## Executive Summary

**Finding:** The lower extraction rate for Sobotkova 2024 (4.3 items/page, 2.96 E+C/page) compared to similar papers appears **JUSTIFIED** based on paper structure and content nature.

## Quantitative Comparison

| Paper | Pages | Total | Items/Pg | Evid. | Claims | E+C/Pg | Paper Type |
|-------|-------|-------|----------|-------|--------|--------|------------|
| **Sobotkova 2024** | 23 | 100 | 4.3 | 38 | 30 | **2.96** | ML failure |
| **Sobotkova 2021** | 25 | 175 | 7.0 | 66 | 73 | **5.56** | System impl. |
| **Eftimoski 2017** | 10 | 153 | 15.3 | 32 | 97 | **12.9** | Statistical |

**Gap:** Sobotkova 2024 is extracting at 53% of Sobotkova 2021 rate and 23% of Eftimoski 2017 rate.

---

## Paper Structure Analysis

### Content Breakdown (Sobotkova 2024, ~11,762 words)

**Literature Review Heavy:**
- "Automated approaches to remotely sensed data" section: ~1,500 words
- Publication bias analysis: Detailed literature synthesis
- Multiple cited studies: Low extraction density (literature context, not findings)

**Limited Empirical Scope:**
- **Only 2 model runs** (2021 and 2022)
- Each run produces: 5-6 distinct performance metrics
- Compare to Eftimoski 2017: Multiple hypotheses, regression models, coefficients

**Negative Results Nature:**
- Much of paper describes **what failed** and **why it failed**
- Technical explanations (tile boundaries, background noise) are **supporting detail**
- Fewer positive findings = fewer extractable claims

**Discussion Structure:**
- Heavy on recommendations and alternatives ("Building a better model")
- Many recommendations are **potential solutions not tested** (lower extraction priority)
- Comparative discussion of other studies (contextual, not findings)

---

## Spot-Check: Missing Claims Review

### Discussion Section Review

I reviewed lines 562-721 (Discussion section) and found:

**Currently Extracted (9 claims from Discussion):**
- ✓ C021: Fixed tile size inappropriate
- ✓ C022: Pre-trained weights bias
- ✓ C023: Model detecting wrong features
- ✓ C024: Alternative strategies possible
- ✓ C025: Custom model requires more resources
- ✓ C026: Experimentation requirements
- ✓ C027: Cost-benefit analysis conclusion
- ✓ C028: Manual timing comparison
- ✓ C030: Manual validation always required

**Potential Additional Claims Identified:**

1. **Line 642-645:** "even a 1:2 (positive:negative) ratio was not sufficient"
   - **Assessment:** This is **supporting detail** for C021/C024
   - **Verdict:** Appropriately consolidated

2. **Line 652-656:** "Overlapping tiles would impose substantial computational overhead"
   - **Assessment:** This is **supporting detail** for C024 (alternatives)
   - **Verdict:** Appropriately consolidated into C024

3. **Line 688-701:** Verschoof-van der Vaart comparison (sophisticated approach still had false positives)
   - **Assessment:** This is **contextual comparison**, not a finding about this study
   - **Verdict:** Correctly excluded (literature context)

4. **Line 700-701:** "models never reached the performance of crowdsourcing"
   - **Assessment:** External study finding, not this paper's claim
   - **Verdict:** Correctly excluded

5. **Line 709-710:** "Two of the authors have had excellent large-scale results from crowdsourcing"
   - **Assessment:** This is **track record/context**, not a finding
   - **Verdict:** Should go in project_metadata, not claims (correctly excluded)

**Conclusion:** No substantive claims missed. Discussion extraction is appropriate.

---

## Spot-Check: Results Section

**Currently Extracted (Evidence from Results):**
- E028-E032: 2021 model metrics (5 items)
- E033-E038: 2022 model metrics (6 items)

**Are these sufficient?**
- ✓ F1 scores captured (both runs)
- ✓ False positive rates captured
- ✓ False negative rates captured
- ✓ True positive counts captured
- ✓ Tile counts captured

**Potential gaps:** None identified. All quantitative findings extracted.

---

## Why This Paper Has Lower Density

### Justified Structural Reasons

**1. Literature Review Heavy (~20% of paper)**
- Extensive discussion of other ML studies
- Publication bias analysis with abstract counts
- This content is **contextual**, not **findings**
- **Expected low extraction density**

**2. Limited Empirical Scope**
- 2 model runs vs. multi-hypothesis papers
- Binary outcome (failure) vs. multiple positive findings
- Negative results inherently produce fewer claims
- **Appropriately lower density**

**3. Technical Explanation Heavy**
- Much of Discussion explains **mechanisms of failure**
- Tile boundary issues, background confusion, etc.
- These are **supporting elaborations** of core failure claims
- **Appropriately consolidated**

**4. Recommendation-Heavy**
- "Building a better model" section lists potential improvements
- These are **untested alternatives**, not findings
- Lower extraction priority than actual findings
- **Appropriately selective**

### Comparison with Eftimoski 2017 (High Density)

**Why Eftimoski extracts at 12.9 E+C/page:**
- Ordered logit regression with **multiple coefficients**
- Each coefficient = separate finding
- Multiple hypotheses tested
- Dense statistical claims ("X increases odds by Y")
- Very compact paper (10 pages, no literature review bloat)

**Sobotkova 2024 is fundamentally different paper type.**

---

## Specific Checks Against Similar Papers

### Check 1: Compare to Sobotkova 2021 (Same Authors)

**Why 2021 has higher density:**
- System implementation with **multiple workflows**
- Each workflow step = extractable protocol
- Multiple **positive outcomes** (efficiency gains, error rates, completion times)
- Field deployment produced **many measurable results**

**2024 paper is narrower:** Just 2 failed ML runs with limited metrics.

### Check 2: Literature Review Density

Let me check if we're under-extracting from literature sections...

**Sobotkova 2024 "Automated approaches" section:**
- Describes adoption trends (17% of publications)
- Publication bias analysis (63% mention no challenges)
- Multiple study comparisons

**Currently extracted:**
- E014-E018: Publication analysis (5 items) ✓
- C013-C015: Adoption and bias claims (3 items) ✓

**Verdict:** Literature section appropriately extracted.

---

## Final Assessment

### Is 2.96 E+C/page appropriate? **YES**

**Reasons:**

1. **Paper Structure Justified:**
   - 20% literature review (low-density content)
   - Heavy technical explanation (consolidated appropriately)
   - Recommendation-heavy discussion (untested alternatives)

2. **Empirical Scope Limited:**
   - Only 2 model runs
   - Each run: ~6 distinct metrics
   - Negative results = fewer findings

3. **Comparison Validated:**
   - Eftimoski 2017 is statistical with many coefficients (naturally denser)
   - Sobotkova 2021 is implementation with many workflows (naturally denser)
   - Sobotkova 2024 is failure documentation (naturally sparser)

4. **No Substantive Gaps:**
   - All quantitative results captured
   - All core interpretive claims extracted
   - Supporting details appropriately consolidated
   - Literature context correctly handled

### Recommendation

**NO CHANGES NEEDED.** The extraction rate is appropriate for this paper type.

The lower density reflects:
- ✓ Proper consolidation of supporting detail
- ✓ Appropriate exclusion of untested alternatives
- ✓ Correct handling of literature context
- ✓ Intrinsic properties of negative-results paper

**RUN-10 extraction is SOUND.**

---

## Could We Extract More?

**Technically yes, but should we?**

We could extract:
- Individual recommendations from "Building a better model" (6-8 additional claims)
- Detailed comparisons with each cited study (10+ additional claims)
- Individual technical explanations (tile boundaries, pixel ratios, etc.)

**But this would:**
- Violate consolidation principles (over-granular)
- Treat recommendations equal to findings (incorrect)
- Treat literature context as findings (incorrect)
- Create noise that obscures core findings

**Current extraction properly prioritizes:**
- Actual findings > potential improvements
- This study's claims > other studies' claims
- Core interpretations > supporting mechanisms

---

## Conclusion

The extraction rate of **4.3 items/page** for Sobotkova 2024 is **APPROPRIATE AND JUSTIFIED**.

The lower rate compared to similar papers reflects:
1. Intrinsic paper structure (literature-heavy, recommendation-heavy)
2. Limited empirical scope (2 model runs, negative results)
3. Proper extraction methodology (appropriate consolidation, correct prioritization)

**No re-extraction needed. RUN-10 is complete and sound.**
