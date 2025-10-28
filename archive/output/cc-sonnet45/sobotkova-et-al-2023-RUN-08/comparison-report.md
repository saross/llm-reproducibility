# Extraction Comparison Report: RUN-08 vs extraction-02

**Current Run (RUN-08):** outputs/sobotkova-et-al-2023/extraction.json
**Previous Best (extraction-02):** archive/output/chatbot-sonnet45/with-skill/extraction-02/extraction.json

**Paper:** Sobotkova et al. (2023) - Creating large, high-quality geospatial datasets from historical maps using novice volunteers

**Comparison Date:** 2025-10-28

---

## 1. Item Count Comparison

| Category | RUN-08 | extraction-02 | Change | % Change |
|----------|--------|---------------|--------|----------|
| Evidence | 53 | 13 | +40 | +307.7% |
| Claims | 61 | 16 | +45 | +281.2% |
| Implicit Arguments | 16 | 10 | +6 | +60.0% |
| Research Designs | 4 | 5 | -1 | -20.0% |
| Methods | 8 | 7 | +1 | 14.285714285714285% |
| Protocols | 17 | 13 | +4 | 30.76923076923077% |
| **Total** | **159** | **64** | **+95** | **+148.4%** |

---

## 2. RDMAP Extraction Quality

### RUN-08 (Current)

| Category | Total | Explicit | Implicit |
|----------|-------|----------|----------|
| Research Designs | 4 | 4 | 0 |
| Methods | 8 | 6 | 2 |
| Protocols | 17 | 14 | 3 |
| **Total RDMAP** | **29** | **24** | **5** |

### extraction-02 (Previous)

| Category | Total | Explicit | Implicit |
|----------|-------|----------|----------|
| Research Designs | 5 | 0 | 0 |
| Methods | 7 | 0 | 0 |
| Protocols | 13 | 0 | 0 |
| **Total RDMAP** | **25** | **0** | **0** |

### RDMAP Assessment

**Total RDMAP items:** RUN-08 has +4 items compared to extraction-02

**Implicit RDMAP:**
- RUN-08: 5 implicit items
- extraction-02: 0 implicit items
- **Change:** +5 implicit items

**Significance:** ✓ RUN-08 successfully extracted implicit RDMAP (Phase 2 improvement)

---

## 3. Evidence-Claim Relationship Coverage

### RUN-08 (Current)

- Total evidence → claim links: 83
- Claims with evidence support: 35 / 61 (57.4%)
- Average evidence per claim: 1.4

### extraction-02 (Previous)

- Total evidence → claim links: 0
- Claims with evidence support: 8 / 16 (50.0%)
- Average evidence per claim: 0.9

### Coverage Comparison

- **Evidence-claim links:** +83 links (+0.0%)
- **Claims with evidence:** +27 claims (+7.4% coverage change)
- **Average evidence per claim:** +0.5 evidence items

---

## 4. RDMAP Relationship Completeness

### RUN-08 (Current)

- Methods implementing designs: 8 / 8
- Protocols implementing methods: 17 / 17
- **Bidirectional mapping:** ✓ Yes
  - Designs with reverse method links: 4 / 4
  - Methods with reverse protocol links: 7 / 8

### extraction-02 (Previous)

- Methods implementing designs: 7 / 7
- Protocols implementing methods: 0 / 13
- **Bidirectional mapping:** ✓ Yes
  - Designs with reverse method links: 0 / 5
  - Methods with reverse protocol links: 7 / 7

---

## 5. Quality Improvements Assessment

### Strengths of RUN-08


**Enhanced RDMAP coverage:** 29 items vs 25 items (+4)

**Implicit RDMAP extraction:** Successfully extracted 5 implicit items (Phase 2 improvement)

**Better evidence coverage:** 57.4% vs 50.0% (+7.4%)

**Higher evidence density:** 1.4 vs 0.9 evidence per claim

### Strengths of extraction-02


RUN-08 shows improvements across most metrics


---

## 6. Overall Assessment

### Key Findings


**Phase 2 validation:** Implicit RDMAP extraction is working (5 implicit items identified).

**Relationship completeness:** RUN-08 includes bidirectional RDMAP relationships, enabling traversal up and down the hierarchy.


### Recommendation

**Use RUN-08** - Provides comprehensive RDMAP extraction with equal or better coverage in other areas.


---

## 7. Extraction Metadata Comparison

### RUN-08 (Current)

- **Title:** Creating large, high-quality geospatial datasets from historical maps using novice volunteers
- **Authors:** Sobotkova, A., Ross, S.A., Nassif-Haynes, C., Ballsun-Stanton, B.
- **DOI:** 10.1016/j.apgeog.2023.102967
- **Research Context:** Crowdsourced georeferencing of historical maps using novice volunteers...

### extraction-02 (Previous)

- **Title:** N/A
- **Authors:** 
- **DOI:** N/A
- **Research Context:** N/A...


---

*Comparison generated: 2025-10-28*

*Comparison script: compare_extractions.py*
