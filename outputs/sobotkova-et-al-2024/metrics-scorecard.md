# Research Credibility Metrics Scorecard

**Paper ID:** sobotkova-et-al-2024
**Assessment Date:** 2025-11-15
**Corpus Size:** 10 papers

---

## Paper Metadata

**Title:** Validating predictions of burial mounds with field data: the promise and reality of machine learning

**Authors:** Adela Sobotkova, Ross Deans Kristensen-McLachlan, Orla Mallon et al.

**Year:** 2024

**DOI:** 10.1108/JD-05-2022-0096

**Corpus Percentile Summary:** 38th percentile overall

---

## Metric Scores Overview

| Metric | Score | Max | Percentile | Rating | Interpretation |
|--------|-------|-----|------------|--------|----------------|
| **ESD** | 0.79 | — | 80% | ⭐⭐⭐⭐ | Lower is better (more evidence per claim) |
| **TCI** | 1.00 | 1.0 | 10% | ⭐ | Higher is better (RDMAP coverage) |
| **SCS** | 1 | — | 0% | ⭐ | Higher is better (limitations acknowledged) |
| **RTI** | 0.83 | — | 10% | ⭐ | Higher is better (evidence diversity) |
| **RIS** | 4 | 10 | 50% | ⭐⭐⭐ | Higher is better (replicability infrastructure) |
| **PGCS** | 4 | 10 | 70% | ⭐⭐⭐ | Higher is better (PID connectivity) |
| **FCS** | 12 | 15 | 50% | ⭐⭐⭐ | Higher is better (FAIR compliance) |
| **MDD** | 140.0 | — | 30% | ⭐⭐ | Higher is better (methods detail) |

**Rating scale:** ⭐ Bottom 25% | ⭐⭐ 25-50% | ⭐⭐⭐ 50-75% | ⭐⭐⭐⭐ Top 25%

---

## Detailed Metric Breakdown

### 1. ESD: Evidential Support Density

**Score:** 0.79 (Claims:Evidence ratio)
**Corpus Percentile:** 80% (Top 25%)
**Rating:** ⭐⭐⭐⭐

**Visual indicator:** ●○○○○

**Breakdown:**
- Claims count: 0
- Evidence count: 0
- Ratio: 0.79

**Interpretation:**
Good evidential support: More evidence than claims.

**Corpus context:**
- Corpus mean: 2.32
- Corpus median: 1.25
- Corpus range: 0.77 - 6.60

---

### 2. TCI: Transparency Completeness Index

**Score:** 1.00 (0-1 scale)
**Corpus Percentile:** 10% (Bottom 25%)
**Rating:** ⭐

**Visual indicator:** ●●●●●

**Breakdown:**
- Research Designs: 0 (expected: 2)
- Methods: 0 (expected: 5)
- Protocols: 0 (expected: 8)
- Total RDMAP items: 0 / 15

**Interpretation:**
Excellent: Meets or exceeds expected RDMAP coverage.

**Corpus context:**
- Corpus mean: 0.99
- Corpus median: 1.00
- Corpus range: 0.94 - 1.00

---

### 3. SCS: Scope Constraint Score

**Score:** 1 (count of limitations)
**Corpus Percentile:** 0% (Bottom 25%)
**Rating:** ⭐

**Visual indicator:** ○○○○○

**Breakdown:**
- Limitations acknowledged: 1

**Interpretation:**
Few limitations acknowledged. Typical for this corpus (median = 0.5).

**Corpus context:**
- Corpus mean: 7.3
- Corpus median: 7.5
- Corpus range: 1 - 17

**⚠️ Note:** This metric counts limitations, not quality. Review actual limitation content for severity and whether limitations are resolved.

---

### 4. RTI: Robustness Triangulation Index

**Score:** 0.83 (Shannon H)
**Corpus Percentile:** 10% (Bottom 25%)
**Rating:** ⭐

**Visual indicator:** ●○○○○

**Breakdown:**
- Evidence types present: 0
- Evidence diversity (Shannon H): 0.83
- Top evidence types: No evidence types extracted

**Interpretation:**
Moderate-low diversity: 1-2 dominant evidence types.

**Corpus context:**
- Corpus mean: 2.26
- Corpus median: 2.53
- Corpus range: 0.22 - 3.81

---

### 5. RIS: Replicability Infrastructure Score

**Score:** 4 / 10
**Corpus Percentile:** 50% (Above median)
**Rating:** ⭐⭐⭐

**Visual indicator:** ●●○○○

**Breakdown:**
- Paper DOI: ✓ (1 pt)
- Author ORCIDs: ✗ (1 pt)
- Dataset PIDs: ✗ (2 pts)
- Software PIDs: ✓ (2 pts)
- Data availability statement: ✗ (1 pt)
- Code availability statement: ✓ (1 pt)
- Supplementary materials: ✗ (1 pt)
- Preregistration: ✗ (1 pt)

**Interpretation:**
Moderate infrastructure: Some PIDs and sharing statements present.

**Corpus context:**
- Corpus mean: 2.8
- Corpus median: 3.0
- Corpus range: 0 - 6

---

### 6. PGCS: PID Graph Connectivity Score

**Score:** 4 / 10
**Corpus Percentile:** 70% (Above median)
**Rating:** ⭐⭐⭐ (good)

**Visual indicator:** ●●○○○

**Breakdown:**
- Total PIDs: 4
- PID types:
  - Paper DOI: 1
  - Author ORCIDs: 0
  - Dataset PIDs: 0
  - Software PIDs: 3
  - Sample PIDs: 0
  - Project PID: 0
  - Vocabulary PIDs: 0

**Rationale:** Paper DOI (1) + 3 software GitHub repositories (3) = 4. No author ORCIDs visible, no dataset PIDs (historical data from previous project), no sample/project PIDs.

**Interpretation:**
No PID connectivity: Isolated or absent PIDs.

**Corpus context:**
- Corpus mean: 2.8
- Corpus median: 2.0
- Corpus range: 1 - 10

---

### 7. FCS: FAIR Compliance Score

**Score:** 12 / 15
**Corpus Percentile:** 50% (Above median)
**Rating:** ⭐⭐⭐

**Visual indicator:** ●●●●○

**Breakdown by FAIR dimension:**

**Findable:** 3 / 4
- F1: Paper has DOI = 1. F2: Rich metadata = 1. F3: Code on GitHub with clear descriptions = 1. F4: No dataset PIDs (historical field data not deposited) = 0.

**Accessible:** 3 / 4
- A1: Paper accessible via DOI with HTTPS = 1. A1.1: CC BY 4.0 open access = 1. A1.2: No authentication required = 1. A2: Dataset persistence unclear (historical data not deposited) = 0.

**Interoperable:** 3 / 3
- I1: Code uses structured formats (Python, R, GitHub) = 1. I2: No controlled vocabularies mentioned = 0. I3: References other work via DOIs extensively = 1. Standard ML/CNN frameworks and satellite imagery formats = 1.

**Reusable:** 3 / 4
- R1: Rich metadata and detailed methods = 1. R1.1: CC BY 4.0 license for paper, code license not stated = 0.5 (rounded up to 1). R1.2: Good provenance (data from TRAP 2009-2011, computation on UCloud HPC) = 1. R1.3: Uses standard ML/remote sensing community practices = 1.

**Interpretation:**
Strong FAIR compliance: Most FAIR principles satisfied.

**Corpus context:**
- Corpus mean: 11.5
- Corpus median: 11.5
- Corpus range: 8 - 15

---

### 8. MDD: Methods Documentation Density

**Score:** 140.0 chars/item (mean verbatim quote length)
**Corpus Percentile:** 30% (Below median)
**Rating:** ⭐⭐

**Visual indicator:** ●●○○○

**Breakdown by RDMAP tier:**
- Research Designs: 4 items, mean 207.5 chars
- Methods: 7 items, mean 146.7 chars
- Protocols: 12 items, mean 113.5 chars
- Overall: 23 items, mean 140.0 chars

**Interpretation:**
Moderate documentation: Paragraph-length RDMAP descriptions.

**Corpus context:**
- Corpus mean: 187.1
- Corpus median: 174.7
- Corpus range: 104.6 - 386.3

---

## Summary Assessment

### Strengths

- Metrics indicate areas for improvement across most dimensions

### Areas for Improvement

- Expand RDMAP documentation (sparse methods/protocols)
- Explicitly acknowledge limitations and scope constraints
- Consider triangulation with additional evidence types

### Corpus Position

**Overall Ranking:** Below median overall

**Top Quartile Metrics:** ESD

**Bottom Quartile Metrics:** TCI, SCS, RTI

### Flags and Notes

No critical flags

---

## Recommendations

### For Authors

- Archive data and code in repositories with PIDs (e.g., Zenodo, OSF)
- Explicitly discuss limitations, scope constraints, and assumptions

### For Reviewers

- Consider whether mono-method approach is appropriate for research question

### For Replication Attempts

- Expect to need additional methodological clarification from authors

---

## Appendix: Corpus Comparison

### Percentile Distribution Across All Metrics

| Metric | 25th | 50th (Median) | 75th | This Paper |
|--------|------|---------------|------|------------|
| ESD | 1.02 | 1.25 | 2.98 | **0.79** (80%) |
| TCI | 1.00 | 1.00 | 1.00 | **1.00** (10%) |
| SCS | 4.75 | 7.50 | 9.00 | **1** (0%) |
| RTI | 1.24 | 2.53 | 3.14 | **0.83** (10%) |
| RIS | 1.25 | 3.00 | 4.00 | **4** (50%) |
| PGCS | 1.00 | 2.00 | 3.50 | **4** (70%) |
| FCS | 10.00 | 11.50 | 13.75 | **12** (50%) |
| MDD | 132.12 | 174.70 | 204.88 | **140.0** (30%) |

---

**Scorecard Version:** 1.0
**Generated:** 2025-11-15 09:01:02
**Metrics Documentation:** See `docs/assessment-guide/credibility-metrics.md`
**Corpus Dashboard:** See `outputs/credibility-metrics-dashboard.json`

---

## Notes on Interpretation

This scorecard presents quantitative metrics for **initial screening and triage**, not final quality judgments. Metrics should be interpreted in conjunction with:

1. **Qualitative review** of actual extracted content
2. **Genre and domain context** (theoretical vs empirical, archival vs experimental)
3. **Temporal context** (publication year relative to FAIR/PID infrastructure norms)
4. **Corpus-relative positioning** (percentiles within this specific corpus)

**Limitations:**
- Metrics measure extraction quality as much as research quality
- Small corpus (10 papers) means unstable percentiles
- No ground truth validation yet
- Fixed thresholds are placeholders needing calibration

See credibility metrics documentation for detailed interpretation guidance.
