# Research Credibility Metrics Scorecard

**Paper ID:** ross-et-al-2009
**Assessment Date:** 2025-11-15
**Corpus Size:** 10 papers

---

## Paper Metadata

**Title:** Remote Sensing and Archaeological Prospection in Apulia, Italy

**Authors:** Shawn A. Ross, Adela Sobotkova, Gert-Jan Burgers

**Year:** 2009

**DOI:** None

**Corpus Percentile Summary:** 29th percentile overall

---

## Metric Scores Overview

| Metric | Score | Max | Percentile | Rating | Interpretation |
|--------|-------|-----|------------|--------|----------------|
| **ESD** | 1.21 | — | 50% | ⭐⭐⭐ | Lower is better (more evidence per claim) |
| **TCI** | 1.00 | 1.0 | 10% | ⭐ | Higher is better (RDMAP coverage) |
| **SCS** | 9 | — | 60% | ⭐⭐⭐ | Higher is better (limitations acknowledged) |
| **RTI** | 2.53 | — | 40% | ⭐⭐ | Higher is better (evidence diversity) |
| **RIS** | 0 | 10 | 0% | ⭐ | Higher is better (replicability infrastructure) |
| **PGCS** | 1 | 10 | 0% | ⭐ | Higher is better (PID connectivity) |
| **FCS** | 8 | 15 | 0% | ⭐ | Higher is better (FAIR compliance) |
| **MDD** | 207.4 | — | 70% | ⭐⭐⭐ | Higher is better (methods detail) |

**Rating scale:** ⭐ Bottom 25% | ⭐⭐ 25-50% | ⭐⭐⭐ 50-75% | ⭐⭐⭐⭐ Top 25%

---

## Detailed Metric Breakdown

### 1. ESD: Evidential Support Density

**Score:** 1.21 (Claims:Evidence ratio)
**Corpus Percentile:** 50% (Above median)
**Rating:** ⭐⭐⭐

**Visual indicator:** ●●○○○

**Breakdown:**
- Claims count: 0
- Evidence count: 0
- Ratio: 1.21

**Interpretation:**
Moderate support: Fewer evidence items than claims. May warrant review.

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

**Score:** 0 / 10
**Corpus Percentile:** 0% (Bottom 25%)
**Rating:** ⭐

**Visual indicator:** ○○○○○

**Breakdown:**
- Paper DOI: ✗ (1 pt)
- Author ORCIDs: ✗ (1 pt)
- Dataset PIDs: ✗ (2 pts)
- Software PIDs: ✗ (2 pts)
- Data availability statement: ✗ (1 pt)
- Code availability statement: ✗ (1 pt)
- Supplementary materials: ✗ (1 pt)
- Preregistration: ✗ (1 pt)

**Interpretation:**
No replicability infrastructure. Consider archiving data/code and obtaining PIDs.

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
  - Paper DOI: 0
  - Author ORCIDs: 0
  - Dataset PIDs: 0
  - Software PIDs: 0
  - Sample PIDs: 0
  - Project PID: 1
  - Vocabulary PIDs: 0

**Rationale:** JSTOR stable URL only (1). No author ORCIDs visible, no paper DOI, no dataset PIDs (QuickBird imagery commercial/proprietary), no software PIDs.

**Interpretation:**
Minimal PID connectivity: Few PIDs, limited connections.

**Corpus context:**
- Corpus mean: 2.8
- Corpus median: 2.0
- Corpus range: 1 - 10

---

### 7. FCS: FAIR Compliance Score

**Score:** 8 / 15
**Corpus Percentile:** 0% (Bottom 25%)
**Rating:** ⭐

**Visual indicator:** ●●●○○

**Breakdown by FAIR dimension:**

**Findable:** 2 / 4
- F1: JSTOR stable URL (persistent but not DOI) = 1. F2: Rich metadata on JSTOR = 1. F3-F4: No dataset PIDs (QuickBird imagery proprietary, ground control data not deposited) = 0.

**Accessible:** 2 / 4
- A1: Accessible via JSTOR with HTTPS = 1. A1.1: Subscription access (JSTOR/Maney Publishing) = 0. A1.2: Authentication required (institutional or individual subscription) = 0. A2: JSTOR committed to long-term preservation = 1.

**Interoperable:** 2 / 3
- I1: PDF format, methods described (structured but not semantic) = 1. I2: No controlled vocabularies used = 0. I3: References to other work but limited DOI usage = 0.5 (rounded to 1). Standard citation practices for 2009.

**Reusable:** 2 / 4
- R1: Rich metadata (title, authors, abstract, keywords, affiliations) = 1. R1.1: Copyright (Maney Publishing/Trustees of Boston University, all rights reserved) = 0. R1.2: Clear provenance (peer-reviewed journal, JSTOR archive) = 1. R1.3: Follows archaeology/remote sensing community standards = 1 (total exceeds 4, capped at max).

**Interpretation:**
Moderate FAIR compliance: Some FAIR components present.

**Corpus context:**
- Corpus mean: 11.5
- Corpus median: 11.5
- Corpus range: 8 - 15

---

### 8. MDD: Methods Documentation Density

**Score:** 207.4 chars/item (mean verbatim quote length)
**Corpus Percentile:** 70% (Above median)
**Rating:** ⭐⭐⭐

**Visual indicator:** ●●●○○

**Breakdown by RDMAP tier:**
- Research Designs: 4 items, mean 311.8 chars
- Methods: 12 items, mean 243.4 chars
- Protocols: 25 items, mean 173.5 chars
- Overall: 41 items, mean 207.4 chars

**Interpretation:**
Detailed documentation: Multi-paragraph RDMAP descriptions.

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
- Improve replicability infrastructure (PIDs, data/code sharing)
- Strengthen PID connectivity (link PIDs in infrastructure)
- Enhance FAIR compliance (metadata, accessibility, licensing)

### Corpus Position

**Overall Ranking:** Below median overall

**Top Quartile Metrics:** None

**Bottom Quartile Metrics:** TCI, RIS, PGCS, FCS

### Flags and Notes

⚠️ No replicability infrastructure: Critical concern for reproducibility

---

## Recommendations

### For Authors

- Archive data and code in repositories with PIDs (e.g., Zenodo, OSF)
- Enhance FAIR compliance: add rich metadata, clear licences, standard formats

### For Reviewers

- Metrics suggest solid methodological foundation; focus on qualitative assessment

### For Replication Attempts

- Contact authors for data/code (not publicly available)
- Data may not be accessible or in standard formats; prepare for preprocessing

---

## Appendix: Corpus Comparison

### Percentile Distribution Across All Metrics

| Metric | 25th | 50th (Median) | 75th | This Paper |
|--------|------|---------------|------|------------|
| ESD | 1.02 | 1.25 | 2.98 | **1.21** (50%) |
| TCI | 1.00 | 1.00 | 1.00 | **1.00** (10%) |
| SCS | 4.75 | 7.50 | 9.00 | **9** (60%) |
| RTI | 1.24 | 2.53 | 3.14 | **2.53** (40%) |
| RIS | 1.25 | 3.00 | 4.00 | **0** (0%) |
| PGCS | 1.00 | 2.00 | 3.50 | **1** (0%) |
| FCS | 10.00 | 11.50 | 13.75 | **8** (0%) |
| MDD | 132.12 | 174.70 | 204.88 | **207.4** (70%) |

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
