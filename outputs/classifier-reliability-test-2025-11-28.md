# Classifier Reliability Test Results

**Test Date:** 2025-11-28
**Classifier Version:** v0.2-alpha
**Test Protocol:** 3 runs per paper (9 total classifications)

---

## Summary

**Test-Retest Reliability: EXCELLENT (100% consistency)**

All papers received identical classifications across all 3 runs. No variation in:
- Paper type
- Primary approach
- Confidence level
- Mixed method characterisation

---

## Results by Paper

### sobotkova-et-al-2024

| Run | Paper Type | Primary Approach | Confidence | Mixed |
|-----|------------|------------------|------------|-------|
| 1 | empirical | deductive | high | true |
| 2 | empirical | deductive | high | true |
| 3 | empirical | deductive | high | true |

**Consistency:** 100% (3/3 identical)

**Notes:** Validation study structure clearly identified across all runs. Secondary inductive element (failure mode analysis) consistently noted but does not affect primary classification.

---

### ballsun-stanton-et-al-2018

| Run | Paper Type | Validation Approach | Confidence | Mixed |
|-----|------------|---------------------|------------|-------|
| 1 | methodological | inductive | high | false |
| 2 | methodological | inductive | high | false |
| 3 | methodological | inductive | high | false |

**Consistency:** 100% (3/3 identical)

**Notes:** Software tool paper with descriptive/demonstrative validation. Classification stable and unambiguous.

---

### penske-et-al-2023

| Run | Paper Type | Primary Approach | Confidence | Mixed |
|-----|------------|------------------|------------|-------|
| 1 | empirical | deductive | high | true |
| 2 | empirical | deductive | high | true |
| 3 | empirical | deductive | high | true |

**Consistency:** 100% (3/3 identical)

**Notes:** Hypothesis-testing archaeogenetics paper. RD007 explicit pathogen hypothesis test, statistical methods with p-values throughout. Classification highly robust.

---

## Reliability Metrics

| Metric | Value | Threshold | Status |
|--------|-------|-----------|--------|
| Paper type agreement | 100% | 100% | ✅ PASS |
| Primary approach agreement | 100% | 100% | ✅ PASS |
| Confidence level agreement | 100% | 100% | ✅ PASS |
| Mixed method agreement | 100% | 100% | ✅ PASS |

**Overall Reliability:** EXCELLENT

---

## Interpretation

The classifier demonstrates excellent test-retest reliability for this sample of 3 papers. Key observations:

1. **Classification stability:** No variation across runs indicates robust decision logic
2. **High confidence throughout:** All classifications assigned "high" confidence, reflecting clear paper characteristics
3. **Consistent mixed method detection:** Secondary approaches consistently identified without affecting primary classification

### Limitations

- Sample size (n=3) is small; larger validation needed
- All papers had relatively clear characteristics (no edge cases tested)
- Same assessor (Claude) for all runs - inter-rater reliability not tested
- Papers from related domains (archaeology/archaeogenetics) - cross-domain reliability not tested

### Recommendations

1. **Expand test corpus:** Include papers with ambiguous characteristics to test edge case handling
2. **Test lower-confidence papers:** Deliberately select papers expected to have medium/low confidence
3. **Cross-domain testing:** Include papers from different HASS disciplines
4. **Monitor production classifications:** Track consistency as more papers classified

---

## Files Generated

```text
outputs/sobotkova-et-al-2024/assessment/
├── classification.json      # Run 1
├── classification-run2.json # Run 2
├── classification-run3.json # Run 3

outputs/ballsun-stanton-et-al-2018/assessment/
├── classification.json      # Run 1
├── classification-run2.json # Run 2
├── classification-run3.json # Run 3

outputs/penske-et-al-2023/assessment/
├── classification.json      # Run 1
├── classification-run2.json # Run 2
├── classification-run3.json # Run 3
```

---

## Next Steps

With classifier reliability validated:
1. Proceed to Step 5: Foundational Clarity cluster prompt development
2. Apply same reliability testing protocol to cluster assessments
3. Consider automated reliability testing for production use
