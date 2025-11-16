# Research Credibility Metrics Scorecard

**Paper ID:** {paper_id}
**Assessment Date:** {assessment_date}
**Corpus Size:** {corpus_size} papers

---

## Paper Metadata

**Title:** {title}

**Authors:** {authors}

**Year:** {publication_year}

**DOI:** {doi}

**Corpus Percentile Summary:** {percentile_summary}

---

## Metric Scores Overview

| Metric | Score | Max | Percentile | Rating | Interpretation |
|--------|-------|-----|------------|--------|----------------|
| **ESD** | {esd_score} | — | {esd_percentile} | {esd_rating} | Lower is better (more evidence per claim) |
| **TCI** | {tci_score} | 1.0 | {tci_percentile} | {tci_rating} | Higher is better (RDMAP coverage) |
| **SCS** | {scs_score} | — | {scs_percentile} | {scs_rating} | Higher is better (limitations acknowledged) |
| **RTI** | {rti_score} | — | {rti_percentile} | {rti_rating} | Higher is better (evidence diversity) |
| **RIS** | {ris_score} | 10 | {ris_percentile} | {ris_rating} | Higher is better (replicability infrastructure) |
| **PGCS** | {pgcs_score} | 10 | {pgcs_percentile} | {pgcs_rating} | Higher is better (PID connectivity) |
| **FCS** | {fcs_score} | 15 | {fcs_percentile} | {fcs_rating} | Higher is better (FAIR compliance) |
| **MDD** | {mdd_score} | — | {mdd_percentile} | {mdd_rating} | Higher is better (methods detail) |

**Rating scale:** ⭐ Bottom 25% | ⭐⭐ 25-50% | ⭐⭐⭐ 50-75% | ⭐⭐⭐⭐ Top 25%

---

## Detailed Metric Breakdown

### 1. ESD: Evidential Support Density

**Score:** {esd_score} (Claims:Evidence ratio)
**Corpus Percentile:** {esd_percentile} ({esd_percentile_description})
**Rating:** {esd_rating}

**Visual indicator:** {esd_visual}

**Breakdown:**
- Claims count: {claims_count}
- Evidence count: {evidence_count}
- Ratio: {esd_ratio}

**Interpretation:**
{esd_interpretation}

**Corpus context:**
- Corpus mean: {esd_corpus_mean}
- Corpus median: {esd_corpus_median}
- Corpus range: {esd_corpus_min} - {esd_corpus_max}

---

### 2. TCI: Transparency Completeness Index

**Score:** {tci_score} (0-1 scale)
**Corpus Percentile:** {tci_percentile} ({tci_percentile_description})
**Rating:** {tci_rating}

**Visual indicator:** {tci_visual}

**Breakdown:**
- Research Designs: {rd_count} (expected: {rd_expected})
- Methods: {methods_count} (expected: {methods_expected})
- Protocols: {protocols_count} (expected: {protocols_expected})
- Total RDMAP items: {rdmap_total} / {rdmap_expected}

**Interpretation:**
{tci_interpretation}

**Corpus context:**
- Corpus mean: {tci_corpus_mean}
- Corpus median: {tci_corpus_median}
- Corpus range: {tci_corpus_min} - {tci_corpus_max}

---

### 3. SCS: Scope Constraint Score

**Score:** {scs_score} (count of limitations)
**Corpus Percentile:** {scs_percentile} ({scs_percentile_description})
**Rating:** {scs_rating}

**Visual indicator:** {scs_visual}

**Breakdown:**
- Limitations acknowledged: {limitations_count}

**Interpretation:**
{scs_interpretation}

**Corpus context:**
- Corpus mean: {scs_corpus_mean}
- Corpus median: {scs_corpus_median}
- Corpus range: {scs_corpus_min} - {scs_corpus_max}

**⚠️ Note:** This metric counts limitations, not quality. Review actual limitation content for severity and whether limitations are resolved.

---

### 4. RTI: Robustness Triangulation Index

**Score:** {rti_score} (Shannon H)
**Corpus Percentile:** {rti_percentile} ({rti_percentile_description})
**Rating:** {rti_rating}

**Visual indicator:** {rti_visual}

**Breakdown:**
- Evidence types present: {evidence_types_count}
- Evidence diversity (Shannon H): {rti_score}
- Top evidence types: {top_evidence_types}

**Interpretation:**
{rti_interpretation}

**Corpus context:**
- Corpus mean: {rti_corpus_mean}
- Corpus median: {rti_corpus_median}
- Corpus range: {rti_corpus_min} - {rti_corpus_max}

---

### 5. RIS: Replicability Infrastructure Score

**Score:** {ris_score} / 10
**Corpus Percentile:** {ris_percentile} ({ris_percentile_description})
**Rating:** {ris_rating}

**Visual indicator:** {ris_visual}

**Breakdown:**
- Paper DOI: {ris_paper_doi} (1 pt)
- Author ORCIDs: {ris_author_orcids} (1 pt)
- Dataset PIDs: {ris_dataset_pids} (2 pts)
- Software PIDs: {ris_software_pids} (2 pts)
- Data availability statement: {ris_data_statement} (1 pt)
- Code availability statement: {ris_code_statement} (1 pt)
- Supplementary materials: {ris_supplementary} (1 pt)
- Preregistration: {ris_preregistration} (1 pt)

**Interpretation:**
{ris_interpretation}

**Corpus context:**
- Corpus mean: {ris_corpus_mean}
- Corpus median: {ris_corpus_median}
- Corpus range: {ris_corpus_min} - {ris_corpus_max}

---

### 6. PGCS: PID Graph Connectivity Score

**Score:** {pgcs_score} / 10
**Corpus Percentile:** {pgcs_percentile} ({pgcs_percentile_description})
**Rating:** {pgcs_rating} ({pgcs_rating_label})

**Visual indicator:** {pgcs_visual}

**Breakdown:**
- Total PIDs: {pgcs_total_pids}
- PID types:
  - Paper DOI: {pgcs_paper_doi}
  - Author ORCIDs: {pgcs_author_orcids}
  - Dataset PIDs: {pgcs_dataset_pids}
  - Software PIDs: {pgcs_software_pids}
  - Sample PIDs: {pgcs_sample_pids}
  - Project PID: {pgcs_project_pid}
  - Vocabulary PIDs: {pgcs_vocabulary_pids}

**Rationale:** {pgcs_rationale}

**Interpretation:**
{pgcs_interpretation}

**Corpus context:**
- Corpus mean: {pgcs_corpus_mean}
- Corpus median: {pgcs_corpus_median}
- Corpus range: {pgcs_corpus_min} - {pgcs_corpus_max}

---

### 7. FCS: FAIR Compliance Score

**Score:** {fcs_score} / 15
**Corpus Percentile:** {fcs_percentile} ({fcs_percentile_description})
**Rating:** {fcs_rating}

**Visual indicator:** {fcs_visual}

**Breakdown by FAIR dimension:**

**Findable:** {fcs_findable_score} / 4
- {fcs_findable_rationale}

**Accessible:** {fcs_accessible_score} / 4
- {fcs_accessible_rationale}

**Interoperable:** {fcs_interoperable_score} / 3
- {fcs_interoperable_rationale}

**Reusable:** {fcs_reusable_score} / 4
- {fcs_reusable_rationale}

**Interpretation:**
{fcs_interpretation}

**Corpus context:**
- Corpus mean: {fcs_corpus_mean}
- Corpus median: {fcs_corpus_median}
- Corpus range: {fcs_corpus_min} - {fcs_corpus_max}

---

### 8. MDD: Methods Documentation Density

**Score:** {mdd_score} chars/item (mean verbatim quote length)
**Corpus Percentile:** {mdd_percentile} ({mdd_percentile_description})
**Rating:** {mdd_rating}

**Visual indicator:** {mdd_visual}

**Breakdown by RDMAP tier:**
- Research Designs: {mdd_rd_count} items, mean {mdd_rd_mean} chars
- Methods: {mdd_methods_count} items, mean {mdd_methods_mean} chars
- Protocols: {mdd_protocols_count} items, mean {mdd_protocols_mean} chars
- Overall: {mdd_total_items} items, mean {mdd_score} chars

**Interpretation:**
{mdd_interpretation}

**Corpus context:**
- Corpus mean: {mdd_corpus_mean}
- Corpus median: {mdd_corpus_median}
- Corpus range: {mdd_corpus_min} - {mdd_corpus_max}

---

## Summary Assessment

### Strengths

{strengths_list}

### Areas for Improvement

{improvements_list}

### Corpus Position

**Overall Ranking:** {overall_ranking}

**Top Quartile Metrics:** {top_quartile_metrics}

**Bottom Quartile Metrics:** {bottom_quartile_metrics}

### Flags and Notes

{flags_and_notes}

---

## Recommendations

### For Authors

{recommendations_authors}

### For Reviewers

{recommendations_reviewers}

### For Replication Attempts

{recommendations_replication}

---

## Appendix: Corpus Comparison

### Percentile Distribution Across All Metrics

| Metric | 25th | 50th (Median) | 75th | This Paper |
|--------|------|---------------|------|------------|
| ESD | {esd_p25} | {esd_p50} | {esd_p75} | **{esd_score}** ({esd_percentile}) |
| TCI | {tci_p25} | {tci_p50} | {tci_p75} | **{tci_score}** ({tci_percentile}) |
| SCS | {scs_p25} | {scs_p50} | {scs_p75} | **{scs_score}** ({scs_percentile}) |
| RTI | {rti_p25} | {rti_p50} | {rti_p75} | **{rti_score}** ({rti_percentile}) |
| RIS | {ris_p25} | {ris_p50} | {ris_p75} | **{ris_score}** ({ris_percentile}) |
| PGCS | {pgcs_p25} | {pgcs_p50} | {pgcs_p75} | **{pgcs_score}** ({pgcs_percentile}) |
| FCS | {fcs_p25} | {fcs_p50} | {fcs_p75} | **{fcs_score}** ({fcs_percentile}) |
| MDD | {mdd_p25} | {mdd_p50} | {mdd_p75} | **{mdd_score}** ({mdd_percentile}) |

---

**Scorecard Version:** 1.0
**Generated:** {generation_timestamp}
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
