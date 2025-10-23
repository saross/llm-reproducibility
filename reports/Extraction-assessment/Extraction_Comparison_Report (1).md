# Extraction Comparison: Section-by-Section vs Full-Paper

**Document:** Sobotkova et al. 2023
**Comparison Date:** 2025-10-23

---

## Executive Summary

The **section-by-section extraction is significantly more complete** than the full-paper extraction. 
Despite claiming to cover the entire paper, the full-paper extraction appears to have stopped 
early (likely due to token limits), missing substantial content from Discussion and all content 
from Conclusion. The section-by-section approach successfully completed extraction by splitting 
across two sessions.

### Key Finding
**The full-paper extraction is incomplete** - it claims to cover the entire paper but stops after 
extracting only 3 evidence items and 1 claim from Discussion, with 0 items from Conclusion.

---

## Quantitative Comparison

| Metric | Section-by-Section | Full-Paper | Difference |
|--------|-------------------|------------|------------|
| **Evidence Items** | 46 (E001-E046) | 17 (E001-E017) | +29 |
| **Claims** | 60 (C001-C098) | 12 (C001-C050) | +48 |
| **Implicit Arguments** | 8 | 4 | +4 |

### Core Claims Distribution
- Section-by-Section: 15 core claims
- Full-Paper: 7 core claims

---

## Section Coverage Comparison

### Evidence Items by Section

| Section | Section-by-Section | Full-Paper | Missing in Full-Paper |
|---------|-------------------|------------|----------------------|
| Abstract | 4 | 4 | ✓ Complete |
| Introduction | 0 | 0 | ✓ Complete |
| Results | 10 | 10 | ✓ Complete |
| Discussion | 26 | 3 | ⚠️ Missing 23 |
| Conclusion | 6 | 0 | ⚠️ Missing 6 |

### Claims by Section

| Section | Section-by-Section | Full-Paper | Missing in Full-Paper |
|---------|-------------------|------------|----------------------|
| Abstract | 6 | 6 | ✓ Complete |
| Introduction | 3 | 3 | ✓ Complete |
| Results | 2 | 2 | ✓ Complete |
| Discussion | 32 | 1 | ⚠️ Missing 31 |
| Conclusion | 17 | 0 | ⚠️ Missing 17 |

---

## Consistency Analysis (Overlapping Items)

The first 17 evidence items and 12 claims appear in both extractions. 
Checking for consistency in overlapping content:

- **Evidence Overlap:** 17 items (E001-E017)
- **Text Differences:** 0 items with different text
- **Claims Overlap:** 12 items
- **Text Differences:** 0 items with different text

✓ **Overlapping items are consistent** - no text differences detected in E001-E017 and C001-C050.


---

## Critical Gaps in Full-Paper Extraction

The full-paper extraction is **missing substantial content** from the paper's latter sections:

### Discussion Section (Section 4)
- **Section-by-Section:** 26 evidence items, 32 claims
- **Full-Paper:** 3 evidence items, 1 claim
- **Missing:** 23 evidence items, 31 claims
- **Impact:** Comparative analysis of approaches (desktop GIS vs mobile vs ML), payoff thresholds, 
  efficiency calculations, and qualitative factors are largely absent.

### Conclusion Section (Section 5)
- **Section-by-Section:** 6 evidence items, 17 claims
- **Full-Paper:** 0 evidence items, 0 claims
- **Missing:** ALL content from Conclusion
- **Impact:** Synthesis of findings, methodological recommendations by dataset size, 
  transferability claims, and quality assessments are completely absent.

---

## Assessment & Recommendations

### Findings
1. **Completeness:** The section-by-section extraction is the only complete extraction of the paper
2. **Consistency:** Where both extractions overlap (E001-E017, C001-C050), they appear consistent
3. **Token Management:** Section-by-section approach successfully handled token limits by splitting work
4. **Coverage Issue:** Full-paper extraction stopped prematurely despite claiming to be complete

### Quality Indicators
✓ **Section-by-Section:**
  - Complete coverage of all paper sections
  - Liberal extraction maintained throughout
  - 77 items extracted from Discussion & Conclusion (the full-paper extraction's gap)
  - Proper sourcing maintained (verbatim quotes, trigger text)
  - Documented split-session process

⚠️ **Full-Paper:**
  - Claims to be complete but stops early
  - Missing 65% of Discussion claims
  - Missing 100% of Conclusion content
  - No documentation of incompleteness in extraction notes
  - Likely hit token limits without continuing

### Recommendation
**Use the section-by-section extraction** (`sobotkova_extraction_pass1_COMPLETE.json`) as the 
authoritative Pass 1 extraction. It is the only complete extraction covering the entire paper.

---

## Technical Notes

- Both extractions follow schema v2.5 with mandatory sourcing requirements
- Both use liberal extraction strategy (Pass 1)
- Section-by-section handled token limits by explicit continuation
- Full-paper appears to have hit token limits without continuation mechanism
- Overlapping content shows consistency, suggesting both follow the same extraction logic
