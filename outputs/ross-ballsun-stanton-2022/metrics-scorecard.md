# Research Credibility Metrics Scorecard

**Paper ID:** ross-ballsun-stanton-2022
**Assessment Date:** 2025-11-15
**Corpus Size:** 10 papers

---

## Paper Metadata

**Title:** Introducing Preregistration of Research Design to Archaeology

**Authors:** Shawn A. Ross, Brian Ballsun-Stanton

**Year:** 2021

**DOI:** 10.31235/osf.io/sbwcq

**Corpus Percentile Summary:** 41th percentile overall

---

## Metric Scores Overview

| Metric | Score | Max | Percentile | Rating | Interpretation |
|--------|-------|-----|------------|--------|----------------|
| **ESD** | 6.60 | — | 0% | ⭐ | Lower is better (more evidence per claim) |
| **TCI** | 1.00 | 1.0 | 10% | ⭐ | Higher is better (RDMAP coverage) |
| **SCS** | 10 | — | 80% | ⭐⭐⭐⭐ | Higher is better (limitations acknowledged) |
| **RTI** | 1.90 | — | 30% | ⭐⭐ | Higher is better (evidence diversity) |
| **RIS** | 2 | 10 | 30% | ⭐⭐ | Higher is better (replicability infrastructure) |
| **PGCS** | 4 | 10 | 70% | ⭐⭐⭐ | Higher is better (PID connectivity) |
| **FCS** | 14 | 15 | 70% | ⭐⭐⭐ | Higher is better (FAIR compliance) |
| **MDD** | 159.5 | — | 40% | ⭐⭐ | Higher is better (methods detail) |

**Rating scale:** ⭐ Bottom 25% | ⭐⭐ 25-50% | ⭐⭐⭐ 50-75% | ⭐⭐⭐⭐ Top 25%

---

## Detailed Metric Breakdown

### 1. ESD: Evidential Support Density

**Score:** 6.60 (Claims:Evidence ratio)
**Corpus Percentile:** 0% (Bottom 25%)
**Rating:** ⭐

**Visual indicator:** ●●●●●

**Breakdown:**
- Claims count: 0
- Evidence count: 0
- Ratio: 6.60

**Interpretation:**
Limited support: Many claims per evidence item. Flag for review of claim support.

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

**Score:** 10 (count of limitations)
**Corpus Percentile:** 80% (Top 25%)
**Rating:** ⭐⭐⭐⭐

**Visual indicator:** ●●●○○

**Breakdown:**
- Limitations acknowledged: 10

**Interpretation:**
Extensive limitation discussion (10 items). Review for quality vs quantity.

**Corpus context:**
- Corpus mean: 7.3
- Corpus median: 7.5
- Corpus range: 1 - 17

**⚠️ Note:** This metric counts limitations, not quality. Review actual limitation content for severity and whether limitations are resolved.

---

### 4. RTI: Robustness Triangulation Index

**Score:** 1.90 (Shannon H)
**Corpus Percentile:** 30% (Below median)
**Rating:** ⭐⭐

**Visual indicator:** ●●●○○

**Breakdown:**
- Evidence types present: 0
- Evidence diversity (Shannon H): 1.90
- Top evidence types: No evidence types extracted

**Interpretation:**
Moderate diversity: Multiple evidence types, some dominant.

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
- Author ORCIDs: ✓ (1 pt)
- Dataset PIDs: ✗ (2 pts)
- Software PIDs: ✗ (2 pts)
- Data availability statement: ✗ (1 pt)
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

**Score:** 4 / 10
**Corpus Percentile:** 70% (Above median)
**Rating:** ⭐⭐⭐ (good)

**Visual indicator:** ●●○○○

**Breakdown:**
- Total PIDs: 3
- PID types:
  - Paper DOI: 1
  - Author ORCIDs: 2
  - Dataset PIDs: 0
  - Software PIDs: 0
  - Sample PIDs: 0
  - Project PID: 0
  - Vocabulary PIDs: 0

**Rationale:** Paper DOI (1) + 2 author ORCIDs (2) = 3, plus bonus for methodological paper citing OSF infrastructure (+1). No datasets, software, or samples (methodological/opinion paper).

**Interpretation:**
No PID connectivity: Isolated or absent PIDs.

**Corpus context:**
- Corpus mean: 2.8
- Corpus median: 2.0
- Corpus range: 1 - 10

---

### 7. FCS: FAIR Compliance Score

**Score:** 14 / 15
**Corpus Percentile:** 70% (Above median)
**Rating:** ⭐⭐⭐

**Visual indicator:** ●●●●●

**Breakdown by FAIR dimension:**

**Findable:** 4 / 4
- F1: Paper has DOI (OSF preprint DOI) = 1. F2: Rich metadata on SocArXiv/OSF = 1. F3: Metadata includes DOI = 1. F4: Indexed in OSF, ResearchGate, searchable = 1.

**Accessible:** 4 / 4
- A1: HTTPS retrieval via DOI = 1. A1.1: Open protocol, no restrictions = 1. A1.2: No authentication required, fully open preprint = 1. A2: OSF/SocArXiv committed to long-term preservation = 1.

**Interoperable:** 2 / 3
- I1: PDF format (structured but not semantic) = 1. I2: No controlled vocabularies used = 0. I3: References to other work via DOIs = 1. No dataset schemas to evaluate.

**Reusable:** 4 / 4
- R1: Rich metadata (title, authors, abstract, keywords, affiliations, ORCIDs) = 1. R1.1: CC-BY or similar open licence (OSF preprint default) = 1. R1.2: Clear provenance (preprint history, dates, version info) = 1. R1.3: Follows community standards for preprints = 1.

**Interpretation:**
Exemplary FAIR compliance: Nearly perfect or perfect alignment.

**Corpus context:**
- Corpus mean: 11.5
- Corpus median: 11.5
- Corpus range: 8 - 15

---

### 8. MDD: Methods Documentation Density

**Score:** 159.5 chars/item (mean verbatim quote length)
**Corpus Percentile:** 40% (Below median)
**Rating:** ⭐⭐

**Visual indicator:** ●●○○○

**Breakdown by RDMAP tier:**
- Research Designs: 5 items, mean 170.6 chars
- Methods: 18 items, mean 146.0 chars
- Protocols: 13 items, mean 173.8 chars
- Overall: 36 items, mean 159.5 chars

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

- Consider increasing evidential support for claims (high claims:evidence ratio)
- Expand RDMAP documentation (sparse methods/protocols)

### Corpus Position

**Overall Ranking:** Below median overall

**Top Quartile Metrics:** SCS

**Bottom Quartile Metrics:** ESD, TCI

### Flags and Notes

No critical flags

---

## Recommendations

### For Authors

- Archive data and code in repositories with PIDs (e.g., Zenodo, OSF)

### For Reviewers

- Review whether claims are adequately supported by evidence

### For Replication Attempts

- Contact authors for data/code (not publicly available)

---

## Appendix: Corpus Comparison

### Percentile Distribution Across All Metrics

| Metric | 25th | 50th (Median) | 75th | This Paper |
|--------|------|---------------|------|------------|
| ESD | 1.02 | 1.25 | 2.98 | **6.60** (0%) |
| TCI | 1.00 | 1.00 | 1.00 | **1.00** (10%) |
| SCS | 4.75 | 7.50 | 9.00 | **10** (80%) |
| RTI | 1.24 | 2.53 | 3.14 | **1.90** (30%) |
| RIS | 1.25 | 3.00 | 4.00 | **2** (30%) |
| PGCS | 1.00 | 2.00 | 3.50 | **4** (70%) |
| FCS | 10.00 | 11.50 | 13.75 | **14** (70%) |
| MDD | 132.12 | 174.70 | 204.88 | **159.5** (40%) |

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
