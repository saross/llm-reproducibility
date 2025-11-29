# Multi-Run Extraction Comparison

**Paper:** Sobotkova et al. (2023) - Creating large, high-quality geospatial datasets from historical maps using novice volunteers

**Runs Compared:** RUN-01, RUN-02, RUN-03, RUN-04, RUN-05, RUN-07, RUN-08

**Current Run:** RUN-08 (outputs/sobotkova-et-al-2023/extraction.json)

**Comparison Date:** 2025-10-28

---

## 1. Item Count Comparison Across All Runs

| Run | Evidence | Claims | Implicit Args | Designs | Methods | Protocols | **Total** |
|-----|----------|--------|---------------|---------|---------|-----------|-----------|
| RUN-01 | 36 | 31 | 0 | 2 | 6 | 10 | **85** |
| RUN-02 | 33 | 46 | 7 | 2 | 9 | 15 | **112** |
| RUN-03 | 63 | 26 | 0 | 6 | 6 | 8 | **109** |
| RUN-04 | 108 | 89 | 6 | 2 | 5 | 11 | **221** |
| RUN-05 | 107 | 78 | 6 | 15 | 29 | 40 | **275** |
| RUN-07 | 10 | 19 | 7 | 4 | 8 | 14 | **62** |
| RUN-08 **†** | 53 | 61 | 16 | 4 | 8 | 17 | **159** |

**†** Current run (RUN-08)

### Rankings by Total Items

1. **RUN-05**: 275 items
2. **RUN-04**: 221 items
3. **RUN-08**: 159 items ← Current
4. **RUN-02**: 112 items
5. **RUN-03**: 109 items
6. **RUN-01**: 85 items
7. **RUN-07**: 62 items

### Key Observations

- **Highest evidence count:** RUN-04 (108 items)
- **Highest claims count:** RUN-04 (89 items)
- **Highest total count:** RUN-05 (275 items)
- **RUN-08 total:** 159 items (ranked #3 of 7)


---

## 2. RDMAP Extraction Comparison

### RDMAP Item Counts

| Run | Total RDMAP | Designs | Methods | Protocols | Implicit RDMAP |
|-----|-------------|---------|---------|-----------|----------------|
| RUN-01 | 18 | 2 | 6 | 10 | 5 |
| RUN-02 | 26 | 2 | 9 | 15 | 3 |
| RUN-03 | 20 | 6 | 6 | 8 | 0 |
| RUN-04 | 18 | 2 | 5 | 11 | 1 |
| RUN-05 | 84 | 15 | 29 | 40 | 0 |
| RUN-07 | 26 | 4 | 8 | 14 | 14 |
| RUN-08 **†** | 29 | 4 | 8 | 17 | 5 |

**†** Current run (RUN-08)

### RDMAP Rankings

1. **RUN-05**: 84 RDMAP items
2. **RUN-08**: 29 RDMAP items ← Current
3. **RUN-02**: 26 RDMAP items
4. **RUN-07**: 26 RDMAP items
5. **RUN-03**: 20 RDMAP items
6. **RUN-01**: 18 RDMAP items
7. **RUN-04**: 18 RDMAP items

### Implicit RDMAP Extraction

| Run | Implicit Designs | Implicit Methods | Implicit Protocols | Total Implicit |
|-----|------------------|------------------|--------------------|-----------------|
| RUN-01 | 1 | 0 | 4 | 5 |
| RUN-02 | 0 | 1 | 2 | 3 |
| RUN-03 | 0 | 0 | 0 | 0 |
| RUN-04 | 0 | 0 | 1 | 1 |
| RUN-05 | 0 | 0 | 0 | 0 |
| RUN-07 | 2 | 4 | 8 | 14 |
| RUN-08 **†** | 0 | 2 | 3 | 5 |

**†** Current run (RUN-08)

**Observations:**

- Runs with implicit RDMAP: RUN-01, RUN-02, RUN-04, RUN-07, RUN-08
- Highest implicit RDMAP count: RUN-07 (14 items)
- RUN-08 implicit RDMAP: 5 items


---

## 3. Evidence-Claim Relationship Coverage

| Run | Ev→Claim Links | Claims w/ Evidence | Evidence Coverage % | Avg Evidence/Claim |
|-----|----------------|--------------------|--------------------|-------------------|
| RUN-01 | 0 | 0/31 | 0.0% | 0.0 |
| RUN-02 | 0 | 0/46 | 0.0% | 0.0 |
| RUN-03 | 0 | 24/26 | 92.3% | 2.1 |
| RUN-04 | 0 | 0/89 | 0.0% | 0.0 |
| RUN-05 | 0 | 57/78 | 73.1% | 2.5 |
| RUN-07 | 0 | 0/19 | 0.0% | 0.0 |
| RUN-08 **†** | 83 | 35/61 | 57.4% | 1.4 |

**†** Current run (RUN-08)

### Evidence Coverage Rankings

1. **RUN-03**: 92.3% coverage (24/26 claims)
2. **RUN-05**: 73.1% coverage (57/78 claims)
3. **RUN-08**: 57.4% coverage (35/61 claims) ← Current
4. **RUN-01**: 0.0% coverage (0/31 claims)
5. **RUN-02**: 0.0% coverage (0/46 claims)
6. **RUN-04**: 0.0% coverage (0/89 claims)
7. **RUN-07**: 0.0% coverage (0/19 claims)


---

## 4. RDMAP Relationship Completeness

| Run | Methods→Designs | Protocols→Methods | Bidirectional? |
|-----|-----------------|-------------------|----------------|
| RUN-01 | 6/6 | 0/10 | ✓ Yes |
| RUN-02 | 9/9 | 0/15 | ✓ Yes |
| RUN-03 | 0/6 | 0/8 | ✓ Yes |
| RUN-04 | 0/5 | 11/11 | ✓ Yes |
| RUN-05 | 0/29 | 0/40 | ✓ Yes |
| RUN-07 | 6/8 | 14/14 | ✓ Yes |
| RUN-08 **†** | 8/8 | 17/17 | ✓ Yes |

**†** Current run (RUN-08)



---

## 5. Quality Metrics Summary

### RUN-08 Position in Rankings

- **Total items:** #3 of 7 runs (159 items)
- **RDMAP coverage:** #2 of 7 runs (29 items)
- **Evidence coverage:** #3 of 7 runs (57.4%)

### RUN-08 Strengths

- Strong overall coverage (#3 in total items)
- Good RDMAP extraction (#2 in RDMAP coverage)
- High evidence-claim linkage (#3 in evidence coverage)
- Successful implicit RDMAP extraction (5 items)
- Complete bidirectional RDMAP relationships
- Balanced evidence-claim extraction

### Comparison to Best Runs

- **Highest total items:** RUN-05 with 275 items (RUN-08: 159 items, -116)
- **Highest RDMAP coverage:** RUN-05 with 84 items (RUN-08: 29 items, -55)
- **Highest evidence coverage:** RUN-03 with 92.3% (RUN-08: 57.4%, -34.9%)


---

## 6. Evolution Across Runs

### Trends in Extraction Quality

**Total Items Trend:**

- RUN-01: █████████████████ 85
- RUN-02: ██████████████████████ 112
- RUN-03: █████████████████████ 109
- RUN-04: ████████████████████████████████████████████ 221
- RUN-05: ███████████████████████████████████████████████████████ 275
- RUN-07: ████████████ 62
- RUN-08: ███████████████████████████████ 159 ← Current

**RDMAP Coverage Trend:**

- RUN-01: █████████ 18
- RUN-02: █████████████ 26
- RUN-03: ██████████ 20
- RUN-04: █████████ 18
- RUN-05: ██████████████████████████████████████████ 84
- RUN-07: █████████████ 26
- RUN-08: ██████████████ 29 ← Current

**Implicit RDMAP Trend:**

- RUN-01: ███████████████ 5
- RUN-02: █████████ 3
- RUN-03:  0
- RUN-04: ███ 1
- RUN-05:  0
- RUN-07: ██████████████████████████████████████████ 14
- RUN-08: ███████████████ 5 ← Current


---

## 7. Overall Assessment

**Status:** ✓ RUN-08 is a high-quality extraction

RUN-08 shows good extraction quality with consistent performance across metrics. While not the highest in all categories, it provides comprehensive coverage (ranked #3 overall).

### Recommendations

- **Use RUN-08 for implicit RDMAP validation:** Successfully identifies implicit methodological elements
- **Consider RUN-05 for comprehensive coverage:** Significantly higher item count
- **Use RUN-08 for evidence-claim analysis:** Good relationship coverage


---

*Comparison generated: 2025-10-28*

*Comparison script: compare_all_runs.py*

*Runs analysed: 7 complete runs*
