# Research Credibility Metrics Scorecard

**Paper ID:** connor-et-al-2013
**Assessment Date:** 2025-11-15
**Corpus Size:** 10 papers

---

## Paper Metadata

**Title:** Environmental conditions in the SE Balkans since the Last Glacial Maximum: New evidence from the Straldzha Mire, Bulgaria

**Authors:** Simon E. Connor, Ivailo Arabadjiev, Ivanka Stevenson et al.

**Year:** 2013

**DOI:** 10.1016/j.quascirev.2013.03.031

**Corpus Percentile Summary:** 31th percentile overall

---

## Metric Scores Overview

| Metric | Score | Max | Percentile | Rating | Interpretation |
|--------|-------|-----|------------|--------|----------------|
| **ESD** | 0.77 | — | 90% | ⭐⭐⭐⭐ | Lower is better (more evidence per claim) |
| **TCI** | 1.00 | 1.0 | 10% | ⭐ | Higher is better (RDMAP coverage) |
| **SCS** | 7 | — | 30% | ⭐⭐ | Higher is better (limitations acknowledged) |
| **RTI** | 3.68 | — | 80% | ⭐⭐⭐⭐ | Higher is better (evidence diversity) |
| **RIS** | 1 | 10 | 10% | ⭐ | Higher is better (replicability infrastructure) |
| **PGCS** | 1 | 10 | 0% | ⭐ | Higher is better (PID connectivity) |
| **FCS** | 10 | 15 | 20% | ⭐ | Higher is better (FAIR compliance) |
| **MDD** | 125.6 | — | 10% | ⭐ | Higher is better (methods detail) |

**Rating scale:** ⭐ Bottom 25% | ⭐⭐ 25-50% | ⭐⭐⭐ 50-75% | ⭐⭐⭐⭐ Top 25%

---

## Detailed Metric Breakdown

### 1. ESD: Evidential Support Density

**Score:** 0.77 (Claims:Evidence ratio)
**Corpus Percentile:** 90% (Top 25%)
**Rating:** ⭐⭐⭐⭐

**Visual indicator:** ○○○○○

**Breakdown:**
- Claims count: 0
- Evidence count: 0
- Ratio: 0.77

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

**Score:** 7 (count of limitations)
**Corpus Percentile:** 30% (Below median)
**Rating:** ⭐⭐

**Visual indicator:** ●●○○○

**Breakdown:**
- Limitations acknowledged: 7

**Interpretation:**
Moderate limitation discussion. Above corpus median.

**Corpus context:**
- Corpus mean: 7.3
- Corpus median: 7.5
- Corpus range: 1 - 17

**⚠️ Note:** This metric counts limitations, not quality. Review actual limitation content for severity and whether limitations are resolved.

---

### 4. RTI: Robustness Triangulation Index

**Score:** 3.68 (Shannon H)
**Corpus Percentile:** 80% (Top 25%)
**Rating:** ⭐⭐⭐⭐

**Visual indicator:** ●●●●●

**Breakdown:**
- Evidence types present: 0
- Evidence diversity (Shannon H): 3.68
- Top evidence types: No evidence types extracted

**Interpretation:**
Very high diversity: Extensive triangulation across many evidence types.

**Corpus context:**
- Corpus mean: 2.26
- Corpus median: 2.53
- Corpus range: 0.22 - 3.81

---

### 5. RIS: Replicability Infrastructure Score

**Score:** 1 / 10
**Corpus Percentile:** 10% (Bottom 25%)
**Rating:** ⭐

**Visual indicator:** ○○○○○

**Breakdown:**
- Paper DOI: ✓ (1 pt)
- Author ORCIDs: ✗ (1 pt)
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

**Score:** 1 / 10
**Corpus Percentile:** 0% (Bottom 25%)
**Rating:** ⭐ (minimal)

**Visual indicator:** ○○○○○

**Breakdown:**
- Total PIDs: 2
- PID types:
  - Paper DOI: 1
  - Author ORCIDs: 0
  - Dataset PIDs: 0
  - Software PIDs: 0
  - Sample PIDs: 0
  - Project PID: 1
  - Vocabulary PIDs: 0

**Rationale:** Paper DOI only (1). No author ORCIDs visible, no dataset PIDs (pollen data mentioned as available through European Pollen Database but no specific accession), no software PIDs.

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
- F1: Paper has DOI (inferred from published version) = 1. F2: Rich metadata available = 1. F3-F4: Supplementary data mentioned but no independent DOI or accession numbers provided = 0.

**Accessible:** 2 / 4
- A1: Paper accessible via DOI with HTTPS = 1. A1.1: Subscription access (Elsevier) = 0. A1.2: Authentication required = 0. A2: Elsevier committed to preservation = 1.

**Interoperable:** 3 / 3
- I1: Structured data formats described (pollen counts, radiocarbon dates in tables) = 1. I2: European Pollen Database implies some standardization = 1. I3: References other work with some DOIs = 1. I2-controlled vocabularies only partially met = 0.

**Reusable:** 3 / 4
- R1: Rich metadata, detailed methods = 1. R1.1: No explicit data licence = 0. R1.2: Excellent provenance (TRAP project 2008-2011, radiocarbon dated, GPS coordinates) = 1. R1.3: Follows community standards (palynology, radiocarbon dating) = 1.

**Interpretation:**
Moderate FAIR compliance: Some FAIR components present.

**Corpus context:**
- Corpus mean: 11.5
- Corpus median: 11.5
- Corpus range: 8 - 15

---

### 8. MDD: Methods Documentation Density

**Score:** 125.6 chars/item (mean verbatim quote length)
**Corpus Percentile:** 10% (Bottom 25%)
**Rating:** ⭐

**Visual indicator:** ●●○○○

**Breakdown by RDMAP tier:**
- Research Designs: 9 items, mean 132.0 chars
- Methods: 22 items, mean 122.9 chars
- Protocols: 41 items, mean 125.6 chars
- Overall: 72 items, mean 125.6 chars

**Interpretation:**
Moderate documentation: Paragraph-length RDMAP descriptions.

**Corpus context:**
- Corpus mean: 187.1
- Corpus median: 174.7
- Corpus range: 104.6 - 386.3

---

## Summary Assessment

### Strengths

- High evidence diversity/triangulation (top quartile)

### Areas for Improvement

- Expand RDMAP documentation (sparse methods/protocols)
- Improve replicability infrastructure (PIDs, data/code sharing)
- Strengthen PID connectivity (link PIDs in infrastructure)
- Enhance FAIR compliance (metadata, accessibility, licensing)
- Provide more detailed methodological descriptions

### Corpus Position

**Overall Ranking:** Below median overall

**Top Quartile Metrics:** ESD, RTI

**Bottom Quartile Metrics:** TCI, RIS, PGCS, FCS, MDD

### Flags and Notes

No critical flags

---

## Recommendations

### For Authors

- Archive data and code in repositories with PIDs (e.g., Zenodo, OSF)
- Enhance FAIR compliance: add rich metadata, clear licences, standard formats

### For Reviewers

- Metrics suggest solid methodological foundation; focus on qualitative assessment

### For Replication Attempts

- Contact authors for data/code (not publicly available)
- Expect to need additional methodological clarification from authors

---

## Appendix: Corpus Comparison

### Percentile Distribution Across All Metrics

| Metric | 25th | 50th (Median) | 75th | This Paper |
|--------|------|---------------|------|------------|
| ESD | 1.02 | 1.25 | 2.98 | **0.77** (90%) |
| TCI | 1.00 | 1.00 | 1.00 | **1.00** (10%) |
| SCS | 4.75 | 7.50 | 9.00 | **7** (30%) |
| RTI | 1.24 | 2.53 | 3.14 | **3.68** (80%) |
| RIS | 1.25 | 3.00 | 4.00 | **1** (10%) |
| PGCS | 1.00 | 2.00 | 3.50 | **1** (0%) |
| FCS | 10.00 | 11.50 | 13.75 | **10** (20%) |
| MDD | 132.12 | 174.70 | 204.88 | **125.6** (10%) |

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
