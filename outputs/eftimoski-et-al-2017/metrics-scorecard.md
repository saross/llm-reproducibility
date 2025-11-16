# Research Credibility Metrics Scorecard

**Paper ID:** eftimoski-et-al-2017
**Assessment Date:** 2025-11-15
**Corpus Size:** 10 papers

---

## Paper Metadata

**Title:** The impact of land use and depopulation on burial mounds in the Kazanlak Valley, Bulgaria: An ordered logit predictive model

**Authors:** Martin Eftimoski, Shawn A. Ross, Adela Sobotkova

**Year:** 2017

**DOI:** 10.1016/j.culher.2016.10.002

**Corpus Percentile Summary:** 31th percentile overall

---

## Metric Scores Overview

| Metric | Score | Max | Percentile | Rating | Interpretation |
|--------|-------|-----|------------|--------|----------------|
| **ESD** | 3.03 | — | 20% | ⭐ | Lower is better (more evidence per claim) |
| **TCI** | 0.94 | 1.0 | 0% | ⭐ | Higher is better (RDMAP coverage) |
| **SCS** | 9 | — | 60% | ⭐⭐⭐ | Higher is better (limitations acknowledged) |
| **RTI** | 2.53 | — | 40% | ⭐⭐ | Higher is better (evidence diversity) |
| **RIS** | 2 | 10 | 30% | ⭐⭐ | Higher is better (replicability infrastructure) |
| **PGCS** | 1 | 10 | 0% | ⭐ | Higher is better (PID connectivity) |
| **FCS** | 10 | 15 | 20% | ⭐ | Higher is better (FAIR compliance) |
| **MDD** | 230.6 | — | 80% | ⭐⭐⭐⭐ | Higher is better (methods detail) |

**Rating scale:** ⭐ Bottom 25% | ⭐⭐ 25-50% | ⭐⭐⭐ 50-75% | ⭐⭐⭐⭐ Top 25%

---

## Detailed Metric Breakdown

### 1. ESD: Evidential Support Density

**Score:** 3.03 (Claims:Evidence ratio)
**Corpus Percentile:** 20% (Bottom 25%)
**Rating:** ⭐

**Visual indicator:** ●●●●○

**Breakdown:**
- Claims count: 0
- Evidence count: 0
- Ratio: 3.03

**Interpretation:**
Limited support: Many claims per evidence item. Flag for review of claim support.

**Corpus context:**
- Corpus mean: 2.32
- Corpus median: 1.25
- Corpus range: 0.77 - 6.60

---

### 2. TCI: Transparency Completeness Index

**Score:** 0.94 (0-1 scale)
**Corpus Percentile:** 0% (Bottom 25%)
**Rating:** ⭐

**Visual indicator:** ●●●●●

**Breakdown:**
- Research Designs: 0 (expected: 2)
- Methods: 0 (expected: 5)
- Protocols: 0 (expected: 8)
- Total RDMAP items: 0 / 15

**Interpretation:**
Strong: Most expected RDMAP components documented.

**Corpus context:**
- Corpus mean: 0.99
- Corpus median: 1.00
- Corpus range: 0.94 - 1.00

---

### 3. SCS: Scope Constraint Score

**Score:** 9 (count of limitations)
**Corpus Percentile:** 60% (Above median)
**Rating:** ⭐⭐⭐

**Visual indicator:** ●●●○○

**Breakdown:**
- Limitations acknowledged: 9

**Interpretation:**
Extensive limitation discussion (9 items). Review for quality vs quantity.

**Corpus context:**
- Corpus mean: 7.3
- Corpus median: 7.5
- Corpus range: 1 - 17

**⚠️ Note:** This metric counts limitations, not quality. Review actual limitation content for severity and whether limitations are resolved.

---

### 4. RTI: Robustness Triangulation Index

**Score:** 2.53 (Shannon H)
**Corpus Percentile:** 40% (Below median)
**Rating:** ⭐⭐

**Visual indicator:** ●●●●○

**Breakdown:**
- Evidence types present: 0
- Evidence diversity (Shannon H): 2.53
- Top evidence types: No evidence types extracted

**Interpretation:**
High diversity: Many evidence types with balanced distribution.

**Corpus context:**
- Corpus mean: 2.26
- Corpus median: 2.53
- Corpus range: 0.22 - 3.81

---

### 5. RIS: Replicability Infrastructure Score

**Score:** 2 / 10
**Corpus Percentile:** 30% (Below median)
**Rating:** ⭐⭐

**Visual indicator:** ●○○○○

**Breakdown:**
- Paper DOI: ✓ (1 pt)
- Author ORCIDs: ✗ (1 pt)
- Dataset PIDs: ✗ (2 pts)
- Software PIDs: ✗ (2 pts)
- Data availability statement: ✓ (1 pt)
- Code availability statement: ✗ (1 pt)
- Supplementary materials: ✗ (1 pt)
- Preregistration: ✗ (1 pt)

**Interpretation:**
Minimal infrastructure: Paper DOI and/or ORCIDs only. Data/code sharing absent.

**Corpus context:**
- Corpus mean: 2.8
- Corpus median: 3.0
- Corpus range: 0 - 6

---

### 6. PGCS: PID Graph Connectivity Score

**Score:** 1 / 10
**Corpus Percentile:** 0% (Bottom 25%)
**Rating:** ⭐ (minimal)

**Visual indicator:** ○○○○○

**Breakdown:**
- Total PIDs: 1
- PID types:
  - Paper DOI: 1
  - Author ORCIDs: 0
  - Dataset PIDs: 0
  - Software PIDs: 0
  - Sample PIDs: 0
  - Project PID: 0
  - Vocabulary PIDs: 0

**Rationale:** Paper DOI only (1). No author ORCIDs visible, no dataset DOI (dataset in supplementary materials without DOI), no software DOIs.

**Interpretation:**
Minimal PID connectivity: Few PIDs, limited connections.

**Corpus context:**
- Corpus mean: 2.8
- Corpus median: 2.0
- Corpus range: 1 - 10

---

### 7. FCS: FAIR Compliance Score

**Score:** 10 / 15
**Corpus Percentile:** 20% (Bottom 25%)
**Rating:** ⭐

**Visual indicator:** ●●●○○

**Breakdown by FAIR dimension:**

**Findable:** 2 / 4
- F1: Paper has DOI = 1. F2: Rich metadata on ScienceDirect = 1. F3-F4: Dataset in supplementary materials but no independent DOI or deposit in data repository = 0.

**Accessible:** 2 / 4
- A1: Paper accessible via DOI with HTTPS = 1. A1.1: Subscription access (Elsevier) = 0. A1.2: Authentication required = 0. A2: Elsevier committed to preservation = 1.

**Interoperable:** 3 / 3
- I1: Structured format (dataset in supplementary, methods described) = 1. I2: No controlled vocabularies = 0. I3: References other work via DOIs extensively = 1. Statistical model well-documented = 1.

**Reusable:** 3 / 4
- R1: Rich metadata and detailed methods = 1. R1.1: No explicit data licence = 0. R1.2: Good provenance (TRAP 2009-2011, GPS coordinates, standardised protocols) = 1. R1.3: Follows community standards (archaeological survey, statistical modeling) = 1.

**Interpretation:**
Moderate FAIR compliance: Some FAIR components present.

**Corpus context:**
- Corpus mean: 11.5
- Corpus median: 11.5
- Corpus range: 8 - 15

---

### 8. MDD: Methods Documentation Density

**Score:** 230.6 chars/item (mean verbatim quote length)
**Corpus Percentile:** 80% (Top 25%)
**Rating:** ⭐⭐⭐⭐

**Visual indicator:** ●●●○○

**Breakdown by RDMAP tier:**
- Research Designs: 2 items, mean 228.5 chars
- Methods: 4 items, mean 334.8 chars
- Protocols: 10 items, mean 189.3 chars
- Overall: 16 items, mean 230.6 chars

**Interpretation:**
Detailed documentation: Multi-paragraph RDMAP descriptions.

**Corpus context:**
- Corpus mean: 187.1
- Corpus median: 174.7
- Corpus range: 104.6 - 386.3

---

## Summary Assessment

### Strengths

- Detailed methodological documentation (top quartile)

### Areas for Improvement

- Consider increasing evidential support for claims (high claims:evidence ratio)
- Expand RDMAP documentation (sparse methods/protocols)
- Strengthen PID connectivity (link PIDs in infrastructure)
- Enhance FAIR compliance (metadata, accessibility, licensing)

### Corpus Position

**Overall Ranking:** Below median overall

**Top Quartile Metrics:** MDD

**Bottom Quartile Metrics:** ESD, TCI, PGCS, FCS

### Flags and Notes

No critical flags

---

## Recommendations

### For Authors

- Archive data and code in repositories with PIDs (e.g., Zenodo, OSF)
- Enhance FAIR compliance: add rich metadata, clear licences, standard formats

### For Reviewers

- Review whether claims are adequately supported by evidence

### For Replication Attempts

- Contact authors for data/code (not publicly available)

---

## Appendix: Corpus Comparison

### Percentile Distribution Across All Metrics

| Metric | 25th | 50th (Median) | 75th | This Paper |
|--------|------|---------------|------|------------|
| ESD | 1.02 | 1.25 | 2.98 | **3.03** (20%) |
| TCI | 1.00 | 1.00 | 1.00 | **0.94** (0%) |
| SCS | 4.75 | 7.50 | 9.00 | **9** (60%) |
| RTI | 1.24 | 2.53 | 3.14 | **2.53** (40%) |
| RIS | 1.25 | 3.00 | 4.00 | **2** (30%) |
| PGCS | 1.00 | 2.00 | 3.50 | **1** (0%) |
| FCS | 10.00 | 11.50 | 13.75 | **10** (20%) |
| MDD | 132.12 | 174.70 | 204.88 | **230.6** (80%) |

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
