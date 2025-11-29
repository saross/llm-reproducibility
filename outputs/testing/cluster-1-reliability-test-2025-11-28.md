# Cluster 1 Foundational Clarity - Reliability Test Results

**Test Date:** 2025-11-28
**Cluster Version:** v1.0
**Paper Tested:** sobotkova-et-al-2024
**Test Protocol:** 3 independent runs

---

## Summary

**Test-Retest Reliability: EXCELLENT**

| Signal | Run 1 | Run 2 | Run 3 | Mean | SD | Range |
|--------|-------|-------|-------|------|-----|-------|
| Comprehensibility | 78 | 76 | 77 | 77.0 | 0.82 | 2 |
| Transparency | 78 | 77 | 79 | 78.0 | 0.82 | 2 |

**Reliability threshold:** SD < 10 points
**Result:** Both signals PASS with SD < 1 point

---

## Detailed Results

### Comprehensibility

| Run | Score | Band | Key Reasoning |
|-----|-------|------|---------------|
| 1 | 78 | Good | Clear validation framework, quantified claims, implicit hypotheses |
| 2 | 76 | Good | Prediction → test → result structure, missing formal hypotheses |
| 3 | 77 | Good | Transparent logical structure, hypotheses not formally stated |

**Mean:** 77.0
**Standard Deviation:** 0.82
**Range:** 76-78 (2 points)
**Band Consistency:** 100% (all Good)

---

### Transparency

| Run | Score | Band | Key Reasoning |
|-----|-------|------|---------------|
| 1 | 78 | Good | 3 GitHub repos, no DOIs, no data sharing |
| 2 | 77 | Good | Excellent code sharing, lacking persistent identifiers |
| 3 | 79 | Good | High FAIR score, code available, data not deposited |

**Mean:** 78.0
**Standard Deviation:** 0.82
**Range:** 77-79 (2 points)
**Band Consistency:** 100% (all Good)

---

## Cluster-Level Results

| Run | Cluster Rating | Scores Pattern |
|-----|----------------|----------------|
| 1 | Strong | 78, 78 |
| 2 | Strong | 76, 77 |
| 3 | Strong | 77, 79 |

**Rating Consistency:** 100% (all Strong)

---

## Reliability Analysis

### Score Stability

Both signals demonstrate excellent score stability:
- **Comprehensibility:** SD = 0.82 (well below 10-point threshold)
- **Transparency:** SD = 0.82 (well below 10-point threshold)

### Band Stability

All scores fall within the Good band (60-79) across all runs:
- No band transitions observed
- All scores cluster in upper Good band (76-79)

### Qualitative Consistency

Key findings consistent across all runs:
1. **Code availability acknowledged** in all runs (3 GitHub repos)
2. **Missing formal hypotheses** noted in all runs
3. **Lack of persistent identifiers** noted in all runs
4. **Strong methods documentation** acknowledged in all runs
5. **Cluster rating: Strong** in all runs

---

## Notes on Run Variation

### Run 1 vs Run 2 Discrepancy

Run 1 initially (incorrectly) stated "No code repository or data access statement identified." This was corrected after user verification revealed the extraction.json correctly captured 3 GitHub repositories. The corrected Run 1 scores (78, 78) align with Runs 2 and 3.

**Lesson learned:** Assessment prompts should more explicitly direct attention to `reproducibility_infrastructure.code_availability` section of extraction.json.

### Minor Score Variations

Score variations of 2 points across runs reflect:
- Slightly different weighting of strengths/weaknesses
- Different emphasis on edge-of-band considerations
- Normal variation in qualitative assessment

All variations fall well within acceptable reliability bounds.

---

## Reliability Verdict

**PASS - Cluster 1 prompt demonstrates excellent test-retest reliability**

| Metric | Result | Threshold | Status |
|--------|--------|-----------|--------|
| Comprehensibility SD | 0.82 | < 10 | ✅ PASS |
| Transparency SD | 0.82 | < 10 | ✅ PASS |
| Band consistency | 100% | ≥ 80% | ✅ PASS |
| Rating consistency | 100% | ≥ 80% | ✅ PASS |

---

## Recommendations

1. **Enhance prompt guidance** for reproducibility infrastructure review — ensure assessors check `code_availability` and `data_availability` sections explicitly
2. **Consider single-paper reliability sufficient** given very low SD scores
3. **Proceed with remaining cluster prompts** — Cluster 1 demonstrates prompt stability

---

## Files Generated

```text
outputs/sobotkova-et-al-2024/assessment/
├── cluster-1-foundational-clarity.md  # Run 1 (corrected)
├── cluster-1-run2.md                  # Run 2
└── cluster-1-run3.md                  # Run 3
```
