# Research Credibility Metrics Scorecard

**Paper ID:** sobotkova-et-al-2016
**Assessment Date:** 2025-11-15
**Corpus Size:** 10 papers

---

## Paper Metadata

**Title:** Measure Twice, Cut Once: Cooperative Deployment of a Generalized, Archaeology-Specific Field Data Collection System

**Authors:** Adela Sobotkova, Shawn A. Ross, Brian Ballsun-Stanton et al.

**Year:** 2016

**DOI:** None

**Corpus Percentile Summary:** 46th percentile overall

---

## Metric Scores Overview

| Metric | Score | Max | Percentile | Rating | Interpretation |
|--------|-------|-----|------------|--------|----------------|
| **ESD** | 2.85 | — | 30% | ⭐⭐ | Lower is better (more evidence per claim) |
| **TCI** | 1.00 | 1.0 | 10% | ⭐ | Higher is better (RDMAP coverage) |
| **SCS** | 17 | — | 90% | ⭐⭐⭐⭐ | Higher is better (limitations acknowledged) |
| **RTI** | 1.02 | — | 20% | ⭐ | Higher is better (evidence diversity) |
| **RIS** | 4 | 10 | 50% | ⭐⭐⭐ | Higher is better (replicability infrastructure) |
| **PGCS** | 2 | 10 | 40% | ⭐⭐ | Higher is better (PID connectivity) |
| **FCS** | 14 | 15 | 70% | ⭐⭐⭐ | Higher is better (FAIR compliance) |
| **MDD** | 197.3 | — | 60% | ⭐⭐⭐ | Higher is better (methods detail) |

**Rating scale:** ⭐ Bottom 25% | ⭐⭐ 25-50% | ⭐⭐⭐ 50-75% | ⭐⭐⭐⭐ Top 25%

---

## Detailed Metric Breakdown

### 1. ESD: Evidential Support Density

**Score:** 2.85 (Claims:Evidence ratio)
**Corpus Percentile:** 30% (Below median)
**Rating:** ⭐⭐

**Visual indicator:** ●●●●○

**Breakdown:**
- Claims count: 0
- Evidence count: 0
- Ratio: 2.85

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

**Score:** 17 (count of limitations)
**Corpus Percentile:** 90% (Top 25%)
**Rating:** ⭐⭐⭐⭐

**Visual indicator:** ●●●●●

**Breakdown:**
- Limitations acknowledged: 17

**Interpretation:**
Extensive limitation discussion (17 items). Review for quality vs quantity.

**Corpus context:**
- Corpus mean: 7.3
- Corpus median: 7.5
- Corpus range: 1 - 17

**⚠️ Note:** This metric counts limitations, not quality. Review actual limitation content for severity and whether limitations are resolved.

---

### 4. RTI: Robustness Triangulation Index

**Score:** 1.02 (Shannon H)
**Corpus Percentile:** 20% (Bottom 25%)
**Rating:** ⭐

**Visual indicator:** ●○○○○

**Breakdown:**
- Evidence types present: 0
- Evidence diversity (Shannon H): 1.02
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
- Paper DOI: ✗ (1 pt)
- Author ORCIDs: ✗ (1 pt)
- Dataset PIDs: ✗ (2 pts)
- Software PIDs: ✓ (2 pts)
- Data availability statement: ✓ (1 pt)
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

**Score:** 2 / 10
**Corpus Percentile:** 40% (Below median)
**Rating:** ⭐⭐ (moderate)

**Visual indicator:** ●○○○○

**Breakdown:**
- Total PIDs: 2
- PID types:
  - Paper DOI: 0
  - Author ORCIDs: 0
  - Dataset PIDs: 0
  - Software PIDs: 1
  - Sample PIDs: 0
  - Project PID: 1
  - Vocabulary PIDs: 0

**Rationale:** UWM Digital Commons URL (1) + FAIMS GitHub repository (1) = 2. No author ORCIDs visible, no paper DOI (book chapter with ISBN instead), no dataset PIDs (methods paper).

**Interpretation:**
Moderate PID connectivity: Some PIDs connected.

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

**Findable:** 3 / 4
- F1: UWM Digital Commons URL and ISBN (not DOI, but persistent identifiers) = 1. F2: Rich metadata on UWM Digital Commons = 1. F3: Software on GitHub with clear organization = 1. F4: No independent paper DOI (book chapter with ISBN) = 0.

**Accessible:** 4 / 4
- A1: Accessible via UWM Digital Commons with HTTPS = 1. A1.1: CC BY 4.0 open access = 1. A1.2: No authentication required = 1. A2: UWM Digital Commons committed to preservation = 1.

**Interoperable:** 3 / 3
- I1: PDF format, software uses structured formats (Android, Linux, XML, BeanShell) = 1. I2: No controlled vocabularies used = 0. I3: References other work with some DOIs = 1. Software documentation and GitHub organization exemplary = 1.

**Reusable:** 4 / 4
- R1: Rich metadata, extensive methods description = 1. R1.1: CC BY 4.0 license for paper, GPLv.3 for software = 1. R1.2: Excellent provenance (three case studies with detailed documentation) = 1. R1.3: Follows open source software development community standards = 1.

**Interpretation:**
Exemplary FAIR compliance: Nearly perfect or perfect alignment.

**Corpus context:**
- Corpus mean: 11.5
- Corpus median: 11.5
- Corpus range: 8 - 15

---

### 8. MDD: Methods Documentation Density

**Score:** 197.3 chars/item (mean verbatim quote length)
**Corpus Percentile:** 60% (Above median)
**Rating:** ⭐⭐⭐

**Visual indicator:** ●●○○○

**Breakdown by RDMAP tier:**
- Research Designs: 6 items, mean 223.2 chars
- Methods: 12 items, mean 238.9 chars
- Protocols: 23 items, mean 168.8 chars
- Overall: 41 items, mean 197.3 chars

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
- Consider triangulation with additional evidence types

### Corpus Position

**Overall Ranking:** Below median overall

**Top Quartile Metrics:** SCS

**Bottom Quartile Metrics:** TCI, RTI

### Flags and Notes

No critical flags

---

## Recommendations

### For Authors

- Archive data and code in repositories with PIDs (e.g., Zenodo, OSF)

### For Reviewers

- Review whether claims are adequately supported by evidence

### For Replication Attempts

- Good infrastructure and documentation; replication attempt should be feasible

---

## Appendix: Corpus Comparison

### Percentile Distribution Across All Metrics

| Metric | 25th | 50th (Median) | 75th | This Paper |
|--------|------|---------------|------|------------|
| ESD | 1.02 | 1.25 | 2.98 | **2.85** (30%) |
| TCI | 1.00 | 1.00 | 1.00 | **1.00** (10%) |
| SCS | 4.75 | 7.50 | 9.00 | **17** (90%) |
| RTI | 1.24 | 2.53 | 3.14 | **1.02** (20%) |
| RIS | 1.25 | 3.00 | 4.00 | **4** (50%) |
| PGCS | 1.00 | 2.00 | 3.50 | **2** (40%) |
| FCS | 10.00 | 11.50 | 13.75 | **14** (70%) |
| MDD | 132.12 | 174.70 | 204.88 | **197.3** (60%) |

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
