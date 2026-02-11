# Open Science Compliance Study — Pilot Protocol

**Version:** 1.0
**Date:** 2025-01-09
**Phase:** 1 (Exploratory Pilot)
**Status:** Pre-registered via git commit

---

## 1. Study Overview

### 1.1 Research Goals

**(a) Publication:** Empirical study of open science/FAIR compliance in Q1 archaeology journal articles

**(b) Reproduction Feasibility:** Test whether papers with good open science apparatus can have results semi-automatically reproduced

### 1.2 Target Journal

**Journal of Archaeological Science (JAS)**

- Q1 ranking (SJR 1.242, H-index 159)
- Mandatory reproducibility reviews since January 2024
- Reproducibility Specialist position (Ben Marwick)
- Data availability statement requirements
- Reproducibility Prize programme (launched 2023)

### 1.3 Study Design

| Phase | Papers | Purpose |
|-------|--------|---------|
| **Phase 1: Exploratory Pilot** | 5 | Develop methodology, identify patterns |
| **Phase 2: Confirmatory Study** | 15-25 | Test preregistered hypotheses |

This protocol covers **Phase 1 only**. Phase 2 hypotheses will be developed from Phase 1 observations and preregistered on OSF before corpus selection.

---

## 2. Corpus

### 2.1 Selection Criteria

Papers must meet ALL of:

1. **Journal:** Journal of Archaeological Science (main journal)
2. **Publication window:** 2023-2025 (post-reproducibility-policy)
3. **Open Access:** Gold OA or accessible via repository/preprint
4. **Computational component:** Code and/or data mentioned in methods
5. **Language:** English

### 2.2 Phase 1 Papers

| # | Slug | Title (abbreviated) | Year | Code Status |
|---|------|---------------------|------|-------------|
| 1 | crema-et-al-2024 | Diffusion curves using radiocarbon | 2024 | GitHub ✅ |
| 2 | marwick-2025 | Archaeology as science (meta-analysis) | 2025 | Zenodo ✅ |
| 3 | key-et-al-2024 | Artefact morphological ranges | 2024 | Verify |
| 4 | herskind-riede-2024 | Semiotic structure in prehistoric art | 2024 | Verify |
| 5 | dye-et-al-2023 | Bayesian chronology construction | 2023 | CRAN ✅ |

### 2.3 Sampling Rationale

- **Method diversity:** Bayesian inference, morphometrics, computational linguistics, chronological modelling, meta-analysis
- **Recognition diversity:** 1 award winner (JAS-SAS 2024), 1 established CRAN package
- **Verification opportunity:** 3 confirmed repositories, 2 to verify from paper text

---

## 3. Extraction Methodology

### 3.1 Pipeline Overview

Each paper undergoes full extraction using the `research-assessor` skill:

```
PDF → Plain text → Pass 0-7 extraction → Classification → Quality gating → Credibility assessment → FAIR assessment
```

### 3.2 Extraction Passes

| Pass | Focus | Output |
|------|-------|--------|
| 0 | Document structure, metadata | Section map |
| 1 | Evidence items | `evidence[]` |
| 2 | Claims | `claims[]` |
| 3 | Implicit arguments | `implicit_arguments[]` |
| 4 | Research designs | `research_designs[]` |
| 5 | Methods | `methods[]` |
| 6 | Protocols | `protocols[]` |
| 7 | Reproducibility infrastructure | `reproducibility_infrastructure{}` |

### 3.3 Classification (Post-Extraction)

- **Paper type:** empirical | methodological | theoretical | review
- **Research approach:** deductive | inductive | abductive
- **Expressed vs revealed approach alignment**

### 3.4 Quality Gating

Papers proceed to credibility assessment only if extraction quality is HIGH:
- Sufficient evidence items extracted
- Claims properly linked to evidence
- Methods documented
- No major structural issues

### 3.5 Credibility Assessment

Three signal clusters assessed (repliCATS-adapted for HASS):

| Cluster | Signals | Focus |
|---------|---------|-------|
| C1: Foundational Clarity | Comprehensibility, Transparency | Can the work be understood? |
| C2: Evidential Strength | Validity, Robustness, Plausibility | Is the evidence adequate? |
| C3: Reproducibility | Reproducibility, Generalisability | Can the work be reproduced? |

---

## 4. FAIR Compliance Assessment

> **Scale standardised in v1.1 (2026-02-11)** after Phase 1 pilot identified
> inconsistency across papers. Original protocol specified 0-10 per dimension
> (0-40 total); standardised to 15 binary GO-FAIR sub-principles with
> independent data and code scoring.

### 4.1 FAIR Dimensions

Assessment based on Pass 6 extraction (`reproducibility_infrastructure.fair_assessment`), using 15 binary sub-principles from the GO-FAIR specification. Data and code scored independently (/15 each); do NOT aggregate into a single composite.

| Dimension | Sub-principles | Natural Max |
|-----------|----------------|-------------|
| **F**indable | F1 (PID), F2 (rich metadata), F3 (metadata includes PID), F4 (indexed) | /4 |
| **A**ccessible | A1 (standard protocol), A1.1 (open/free), A1.2 (auth where needed), A2 (metadata persistent) | /4 |
| **I**nteroperable | I1 (formal language), I2 (FAIR vocabularies), I3 (qualified references) | /3 |
| **R**eusable | R1 (rich description), R1.1 (clear licence), R1.2 (provenance), R1.3 (community standards) | /4 |
| **Total** | | **/15** |

**Rating thresholds (applied independently to data and code):**

| Score | Percentage | Rating |
|-------|------------|--------|
| 13-15 | 87-100% | Highly FAIR |
| 9-12 | 60-80% | Moderately FAIR |
| 5-8 | 33-53% | Minimally FAIR |
| 0-4 | 0-27% | Not FAIR |

### 4.2 Infrastructure Fields

From `reproducibility_infrastructure`:

```yaml
data_availability:
  statement_present: boolean
  statement_type: available | on_request | restricted | not_available
  repository: string
  pid: string (DOI, accession number)
  licence: string

code_availability:
  statement_present: boolean
  repository: string (GitHub, Zenodo, OSF)
  pid: string
  licence: string
  language: string
  dependencies_documented: boolean

materials_availability:
  statement_present: boolean
  description: string
```

### 4.3 PID Graph Connectivity

Score based on linkages between:

- Paper DOI ↔ Data DOI
- Paper DOI ↔ Code DOI
- Code DOI ↔ Data DOI
- ORCID linkages

Scale: 0-6 (count of verified bidirectional links)

---

## 5. Reproduction Feasibility Assessment

### 5.1 Scope

For papers with code + data available, assess feasibility of computational reproduction.

### 5.2 Feasibility Checklist

| Item | Assessment |
|------|------------|
| Repository resolves | ✅/❌ |
| Repository archived (Zenodo/OSF) | ✅/❌ |
| Code language identified | Language |
| Dependencies specified | Full/Partial/None |
| Data files present | ✅/❌ |
| Data format documented | ✅/❌ |
| README present | ✅/❌ |
| Execution instructions | Full/Partial/None |
| Estimated effort | Hours |

### 5.3 Reproduction Attempt

For feasible papers, attempt reproduction:

1. Clone/download repository
2. Set up environment (if specified)
3. Run analysis code
4. Compare outputs to published results

### 5.4 Outcome Categories

| Category | Definition |
|----------|------------|
| ✅ **Full reproduction** | Code runs, outputs match published results |
| ⚠️ **Partial reproduction** | Code runs with modifications, outputs similar |
| ❌ **Failed reproduction** | Code doesn't run or outputs differ significantly |
| 🔒 **Blocked** | Data/code inaccessible despite claims |

### 5.5 Documentation

Each reproduction attempt documented in:
`studies/open-science-compliance/outputs/{paper-slug}/reproduction-log.md`

---

## 6. Analysis Plan

### 6.1 Phase 1 Outputs (Descriptive)

No hypothesis testing in Phase 1. Outputs are descriptive:

1. **FAIR compliance summary table** — scores across all 5 papers
2. **Reproduction feasibility log** — attempt documentation
3. **Pattern observations** — qualitative notes on compliance patterns
4. **Hypothesis candidates** — testable predictions for Phase 2

### 6.2 Metrics to Report

| Metric | Description |
|--------|-------------|
| FAIR total score | Sum of F+A+I+R (0-40) |
| FAIR dimension scores | Individual F, A, I, R (0-10 each) |
| PID connectivity | 0-6 scale |
| Code availability | Yes/No/Partial |
| Data availability | Yes/No/Partial |
| Reproduction outcome | Full/Partial/Failed/Blocked |
| Credibility cluster ratings | Strong/Adequate/Weak per cluster |

### 6.3 Visualisations

- FAIR radar charts per paper
- Compliance comparison table
- Reproduction outcome summary

---

## 7. Preregistration Strategy

### 7.1 Phase 1 (This Protocol)

- **Registration method:** Git commit (timestamped)
- **What is registered:** Methodology, analysis plan, corpus
- **What is NOT registered:** Hypotheses (exploratory phase)

### 7.2 Phase 2 (Future)

- **Registration method:** OSF preregistration
- **Timing:** After Phase 1 findings, before Phase 2 corpus selection
- **Content:** Specific hypotheses derived from Phase 1 patterns

### 7.3 Example Hypothesis Development

**Phase 1 observation:** "Papers with reproducibility badges had higher FAIR scores (mean 12.3) than non-badge papers (mean 7.8)"

**Phase 2 hypothesis:** "H1: JAS papers published after the reproducibility review policy (2024+) will have significantly higher FAIR scores than papers published 2023 (α = 0.05, two-tailed t-test)"

---

## 8. Workflow

### 8.1 Per-Paper Workflow

```
1. Obtain PDF
   └── Check OA status, download from publisher/repository

2. Extract text
   └── PDF → plain text conversion

3. Run extraction pipeline
   └── Pass 0-7 → extraction.json

4. Classify paper
   └── Pass 8 → classification.json

5. Quality gating
   └── Assess extraction quality

6. Credibility assessment (if HIGH quality)
   └── Clusters 1-3 → assessment files

7. FAIR assessment
   └── Score F/A/I/R dimensions from infrastructure fields

8. Reproduction feasibility
   └── Assess code/data availability

9. Reproduction attempt (if feasible)
   └── Run code, compare outputs

10. Document findings
    └── Update queue.yaml, write reproduction-log.md
```

### 8.2 Output Structure

```
studies/open-science-compliance/outputs/{paper-slug}/
├── {paper-slug}.txt          # Extracted plain text
├── extraction.json           # Pass 0-7 output
├── classification.json       # Pass 8 output
├── assessment/
│   ├── cluster-1-foundational-clarity.md
│   ├── cluster-2-evidential-strength.md
│   └── cluster-3-reproducibility.md
├── fair-assessment.yaml      # FAIR dimension scores
└── reproduction-log.md       # Reproduction attempt documentation
```

---

## 9. Limitations

### 9.1 Phase 1 Limitations

- Small sample size (n=5) — descriptive only
- Single journal — may not generalise
- Selection bias — papers with visible code/data more likely selected
- Assessor bias — single assessor (LLM-assisted)

### 9.2 Mitigation

- Phase 2 will use larger corpus with preregistered hypotheses
- Consider inter-rater reliability check on 1-2 papers
- Document all selection decisions transparently

---

## 10. Timeline

| Step | Status |
|------|--------|
| Protocol commit | ⏳ Pending |
| Paper 1 extraction + assessment | ⏳ Pending |
| Paper 2 extraction + assessment | ⏳ Pending |
| Paper 3 extraction + assessment | ⏳ Pending |
| Paper 4 extraction + assessment | ⏳ Pending |
| Paper 5 extraction + assessment | ⏳ Pending |
| Pilot findings report | ⏳ Pending |
| Hypothesis development | ⏳ Pending |

---

## 11. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-01-09 | Initial protocol |
