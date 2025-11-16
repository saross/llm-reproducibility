# Research Credibility Metrics Scorecard

**Paper ID:** sobotkova-et-al-2021
**Assessment Date:** 2025-11-15
**Corpus Size:** 10 papers

---

## Paper Metadata

**Title:** Deploying an Offline, Multi-User, Mobile System for Digital Recording in the Perachora Peninsula, Greece

**Authors:** Adela Sobotkova, Shawn A. Ross, Petra Hermankova et al.

**Year:** 2021

**DOI:** 10.1080/00934690.2021.1969837

**Corpus Percentile Summary:** 68th percentile overall

---

## Metric Scores Overview

| Metric | Score | Max | Percentile | Rating | Interpretation |
|--------|-------|-----|------------|--------|----------------|
| **ESD** | 1.11 | — | 60% | ⭐⭐⭐ | Lower is better (more evidence per claim) |
| **TCI** | 1.00 | 1.0 | 10% | ⭐ | Higher is better (RDMAP coverage) |
| **SCS** | 4 | — | 20% | ⭐ | Higher is better (limitations acknowledged) |
| **RTI** | 3.81 | — | 90% | ⭐⭐⭐⭐ | Higher is better (evidence diversity) |
| **RIS** | 6 | 10 | 90% | ⭐⭐⭐⭐ | Higher is better (replicability infrastructure) |
| **PGCS** | 10 | 10 | 90% | ⭐⭐⭐⭐ | Higher is better (PID connectivity) |
| **FCS** | 15 | 15 | 90% | ⭐⭐⭐⭐ | Higher is better (FAIR compliance) |
| **MDD** | 386.3 | — | 90% | ⭐⭐⭐⭐ | Higher is better (methods detail) |

**Rating scale:** ⭐ Bottom 25% | ⭐⭐ 25-50% | ⭐⭐⭐ 50-75% | ⭐⭐⭐⭐ Top 25%

---

## Detailed Metric Breakdown

### 1. ESD: Evidential Support Density

**Score:** 1.11 (Claims:Evidence ratio)
**Corpus Percentile:** 60% (Above median)
**Rating:** ⭐⭐⭐

**Visual indicator:** ●●○○○

**Breakdown:**
- Claims count: 0
- Evidence count: 0
- Ratio: 1.11

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

**Score:** 4 (count of limitations)
**Corpus Percentile:** 20% (Bottom 25%)
**Rating:** ⭐

**Visual indicator:** ●○○○○

**Breakdown:**
- Limitations acknowledged: 4

**Interpretation:**
Moderate limitation discussion. Above corpus median.

**Corpus context:**
- Corpus mean: 7.3
- Corpus median: 7.5
- Corpus range: 1 - 17

**⚠️ Note:** This metric counts limitations, not quality. Review actual limitation content for severity and whether limitations are resolved.

---

### 4. RTI: Robustness Triangulation Index

**Score:** 3.81 (Shannon H)
**Corpus Percentile:** 90% (Top 25%)
**Rating:** ⭐⭐⭐⭐

**Visual indicator:** ●●●●●

**Breakdown:**
- Evidence types present: 0
- Evidence diversity (Shannon H): 3.81
- Top evidence types: No evidence types extracted

**Interpretation:**
Very high diversity: Extensive triangulation across many evidence types.

**Corpus context:**
- Corpus mean: 2.26
- Corpus median: 2.53
- Corpus range: 0.22 - 3.81

---

### 5. RIS: Replicability Infrastructure Score

**Score:** 6 / 10
**Corpus Percentile:** 90% (Top 25%)
**Rating:** ⭐⭐⭐⭐

**Visual indicator:** ●●●○○

**Breakdown:**
- Paper DOI: ✓ (1 pt)
- Author ORCIDs: ✓ (1 pt)
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

**Score:** 10 / 10
**Corpus Percentile:** 90% (Top 25%)
**Rating:** ⭐⭐⭐⭐ (excellent)

**Visual indicator:** ●●●●●

**Breakdown:**
- Total PIDs: 10
- PID types:
  - Paper DOI: 1
  - Author ORCIDs: 6
  - Dataset PIDs: 0
  - Software PIDs: 3
  - Sample PIDs: 0
  - Project PID: 0
  - Vocabulary PIDs: 0

**Rationale:** Paper DOI (1) + 6 author ORCIDs (6) + 3 software GitHub repositories (3) = 10. Strong PID connectivity with high ORCID coverage and open code sharing.

**Interpretation:**
No PID connectivity: Isolated or absent PIDs.

**Corpus context:**
- Corpus mean: 2.8
- Corpus median: 2.0
- Corpus range: 1 - 10

---

### 7. FCS: FAIR Compliance Score

**Score:** 15 / 15
**Corpus Percentile:** 90% (Top 25%)
**Rating:** ⭐⭐⭐⭐

**Visual indicator:** ●●●●●

**Breakdown by FAIR dimension:**

**Findable:** 4 / 4
- F1: Paper has DOI = 1. F2: Rich metadata on Taylor & Francis Online = 1. F3: Metadata includes DOI = 1. F4: Indexed in T&F, Web of Science, Scopus = 1.

**Accessible:** 3 / 4
- A1: Paper accessible via DOI with HTTPS = 1. A1.1: Subscription access (Taylor & Francis) = 0. A1.2: Authentication required = 0. A2: T&F committed to preservation, supplementary materials available = 1. Code openly accessible on GitHub = 2 (bonus for code accessibility).

**Interoperable:** 4 / 3
- I1: Structured formats (XML module definitions, GitHub code, supplementary materials) = 1. I2: Uses FAIMS vocabulary framework = 1. I3: References other work via DOIs extensively = 1. Transparent data schema via XML definition files = 1.

**Reusable:** 4 / 4
- R1: Rich metadata and extremely detailed methods = 1. R1.1: Code open-source, paper copyright standard = 1. R1.2: Excellent provenance (workflow documented, data history maintained, process transparent) = 1. R1.3: Follows community standards (archaeological survey, open-source software development) = 1.

**Interpretation:**
Exemplary FAIR compliance: Nearly perfect or perfect alignment.

**Corpus context:**
- Corpus mean: 11.5
- Corpus median: 11.5
- Corpus range: 8 - 15

---

### 8. MDD: Methods Documentation Density

**Score:** 386.3 chars/item (mean verbatim quote length)
**Corpus Percentile:** 90% (Top 25%)
**Rating:** ⭐⭐⭐⭐

**Visual indicator:** ●●●●●

**Breakdown by RDMAP tier:**
- Research Designs: 2 items, mean 249.0 chars
- Methods: 8 items, mean 244.2 chars
- Protocols: 20 items, mean 456.9 chars
- Overall: 30 items, mean 386.3 chars

**Interpretation:**
Extensive documentation: Very detailed RDMAP descriptions (> 300 chars/item).

**Corpus context:**
- Corpus mean: 187.1
- Corpus median: 174.7
- Corpus range: 104.6 - 386.3

---

## Summary Assessment

### Strengths

- Exemplary FAIR compliance (top quartile)
- High evidence diversity/triangulation (top quartile)
- Strong replicability infrastructure (top quartile)
- Detailed methodological documentation (top quartile)

### Areas for Improvement

- Expand RDMAP documentation (sparse methods/protocols)
- Explicitly acknowledge limitations and scope constraints

### Corpus Position

**Overall Ranking:** Above median overall

**Top Quartile Metrics:** RTI, RIS, PGCS, FCS, MDD

**Bottom Quartile Metrics:** TCI, SCS

### Flags and Notes

No critical flags

---

## Recommendations

### For Authors

- Continue current practices; strong performance across metrics

### For Reviewers

- Metrics suggest solid methodological foundation; focus on qualitative assessment

### For Replication Attempts

- Good infrastructure and documentation; replication attempt should be feasible

---

## Appendix: Corpus Comparison

### Percentile Distribution Across All Metrics

| Metric | 25th | 50th (Median) | 75th | This Paper |
|--------|------|---------------|------|------------|
| ESD | 1.02 | 1.25 | 2.98 | **1.11** (60%) |
| TCI | 1.00 | 1.00 | 1.00 | **1.00** (10%) |
| SCS | 4.75 | 7.50 | 9.00 | **4** (20%) |
| RTI | 1.24 | 2.53 | 3.14 | **3.81** (90%) |
| RIS | 1.25 | 3.00 | 4.00 | **6** (90%) |
| PGCS | 1.00 | 2.00 | 3.50 | **10** (90%) |
| FCS | 10.00 | 11.50 | 13.75 | **15** (90%) |
| MDD | 132.12 | 174.70 | 204.88 | **386.3** (90%) |

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
