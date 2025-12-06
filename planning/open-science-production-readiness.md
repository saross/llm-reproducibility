# Open Science Assessment: Production Readiness Analysis

**Created:** 2025-12-06
**Source:** Assessment system review + variability test observations
**Purpose:** Evaluate readiness for corpus-level production runs

---

## Context

The research-assessor pipeline includes comprehensive **open science assessment** capabilities through the repliCATS Seven Signals framework, FAIR principles evaluation, and infrastructure assessment. After completing the 25-run variability test, we want to evaluate production readiness for running assessments on a coherent corpus (e.g., all OA papers from a Q1 archaeological science journal).

---

## Current Implementation Status

### Fully Implemented Components

| Component | Location | Status |
|-----------|----------|--------|
| **10-pass extraction pipeline** | `extraction-system/prompts/00-07` | ✅ Complete |
| **Classification (Pass 8)** | `assessment-system/prompts/08-classification-prompt.md` | ✅ Complete |
| **Track A Quality Gate (Pass 8.5)** | `assessment-system/prompts/08.5-track-a-quality-prompt.md` | ✅ Complete |
| **Cluster 1: Foundational Clarity** | `assessment-system/prompts/cluster-1-foundational-clarity.md` | ✅ Complete |
| **Cluster 2: Evidential Strength** | `assessment-system/prompts/cluster-2-evidential-strength.md` | ✅ Complete |
| **Cluster 3: Reproducibility** | `assessment-system/prompts/cluster-3-reproducibility.md` | ✅ Complete |
| **Final Report (Pass 10)** | `assessment-system/prompts/10-final-report-prompt.md` | ✅ Complete |
| **repliCATS Seven Signals** | `.claude/skills/research-assessor/references/credibility/` | ✅ 6 reference files |
| **FAIR Principles Guide** | `.claude/skills/research-assessor/references/infrastructure/fair-principles-guide.md` | ✅ Complete |
| **Infrastructure Assessment** | `.claude/skills/research-assessor/references/infrastructure/` | ✅ 4 reference files |

### Assessment Outputs Produced (from variability test)

Each run produces:
- `extraction.json` - Structured extraction with all arrays
- `assessment/classification.json` - Paper type, approach, quality state
- `assessment/track-a-quality.md` - Quality gate assessment
- `assessment/cluster-1-foundational-clarity.md` - C1 signal scores
- `assessment/cluster-2-evidential-strength.md` - C2 signal scores
- `assessment/cluster-3-reproducibility.md` - C3 signal scores + FAIR
- `assessment/credibility-report.md` - Final integrated report

---

## Issues Identified

### Issue 1: FAIR Score Denominator Inconsistency 🔴 BLOCKING

**Problem:** FAIR scores across the 25 variability runs use inconsistent denominators.

| Paper | FAIR Scores Observed | Denominators |
|-------|---------------------|--------------|
| penske-et-al-2023 | 35/40, 12/16, 14/15, 14/16 | 40, 16, 15, 16 |
| ballsun-stanton-2018 | 37/40, 35/40, 15/16 | 40, 16 |
| ross-2005 | 8/40, 7/16, 11/40, 11/40 | 40, 16 |
| sobotkova-et-al-2024 | 24/40 (run-04 only) | 40 |
| sobotkova-et-al-2016 | 8/16, 29/40, 9/16, 22/40 | 16, 40 |

**Impact:** Cannot compare FAIR scores across papers or aggregate corpus-level statistics.

**Root Cause:** The FAIR assessment guidance allows flexibility in which dimensions are applicable, but doesn't standardise scoring output. Some runs score all 40 indicators, others score applicable subset.

**Resolution Options:**
1. **Normalise to percentage:** Report FAIR as percentage (score/max × 100)
2. **Standardise to 40-point scale:** Always score all 40 indicators, mark N/A as 0
3. **Report both:** Raw score + normalised percentage

**Recommendation:** Option 1 (percentage) for production runs, with raw scores preserved in structured output.

---

### Issue 2: No Batch Processing Capability 🟡 EFFICIENCY

**Problem:** Each paper requires manual session initiation. No automation for processing multiple papers.

**Current Workflow:**
1. User starts fresh session
2. User runs `/variability-run` or invokes research-assessor skill
3. Claude processes single paper
4. User clears context
5. Repeat

**Impact:** Processing 20-50 papers manually is labour-intensive.

**Resolution Options:**
1. **Scripted invocation:** Shell script looping through papers with context clearing
2. **Queue automation:** Enhance `queue.yaml` with batch mode
3. **Accept manual:** Document efficient manual workflow

**Recommendation:** For initial production run (10-20 papers), manual processing is acceptable. Automation can follow if corpus size increases.

---

### Issue 3: Corpus Acquisition Strategy Undocumented 🟡 PLANNING

**Problem:** No documented strategy for acquiring and preparing papers for corpus-level analysis.

**Requirements for production corpus:**
1. **Source selection:** Journal, date range, inclusion/exclusion criteria
2. **PDF acquisition:** OA access, licence compliance
3. **Text extraction:** Convert PDFs to analysable format
4. **Metadata capture:** DOI, title, authors, year for output organisation

**Candidate Journals (Q1 Archaeological Science):**

| Journal | OA Policy | Articles/Year | Suitability |
|---------|-----------|---------------|-------------|
| Journal of Archaeological Science | Hybrid (many Gold OA) | ~200 | High |
| Journal of Archaeological Method and Theory | Hybrid | ~40 | Medium |
| Archaeological and Anthropological Sciences | Hybrid | ~150 | High |
| Internet Archaeology | Full OA | ~30 | Excellent |
| Open Archaeology | Full OA | ~50 | Excellent |

**Recommendation:** Start with **Internet Archaeology** or **Open Archaeology** (full OA, manageable volume, no access barriers).

---

### Issue 4: Output Standardisation for Comparative Analysis 🟡 ANALYSIS

**Problem:** Current outputs optimised for single-paper assessment, not corpus-level comparison.

**Gaps:**
1. No aggregated CSV/JSON for cross-paper statistics
2. No comparative visualisation capability
3. No standard corpus-level report template

**Resolution:**
1. **Post-processing script:** Extract key metrics from all credibility-report.md files into aggregated CSV
2. **Standard fields:** Paper slug, verdict, aggregate score, 7 signal scores, FAIR%, cluster ratings
3. **Comparative report template:** Summary statistics, distribution charts, outlier identification

**Recommendation:** Create `scripts/aggregate-corpus-results.py` after first production run.

---

## Production Readiness Assessment

### Summary Table

| Aspect | Status | Blocker? | Action Required |
|--------|--------|----------|-----------------|
| Extraction pipeline | ✅ Ready | No | None |
| Assessment prompts | ✅ Ready | No | None |
| Signal scoring | ✅ Ready | No | None |
| FAIR scoring | ⚠️ Inconsistent | **Yes** | Standardise denominator |
| Batch processing | ⚠️ Manual | No | Accept for initial run |
| Corpus acquisition | ⚠️ Undocumented | No | Document strategy |
| Output aggregation | ⚠️ Missing | No | Build after first run |

**Overall Status:** CONDITIONALLY READY

---

## Recommended Path Forward

### Option A: Minimal Preparation (Recommended)

**Effort:** 2-3 hours preparation

**Steps:**

1. **Standardise FAIR output** (1 hour)
   - [ ] Add normalisation guidance to `cluster-3-reproducibility.md` prompt
   - [ ] Specify: "Report FAIR as X/Y (Z%)" format
   - [ ] Test on 1 paper to verify consistency

2. **Select corpus** (30 min)
   - [ ] Choose journal: Internet Archaeology or Open Archaeology
   - [ ] Define date range (e.g., 2020-2024)
   - [ ] Set target: 10-15 papers

3. **Acquire papers** (1 hour)
   - [ ] Download OA PDFs
   - [ ] Extract text using existing pipeline
   - [ ] Create queue.yaml entries

4. **Run production** (10-15 papers × 30 min = 5-8 hours)
   - [ ] Process each paper with context clearing
   - [ ] Document any edge cases

5. **Post-hoc aggregation** (1 hour)
   - [ ] Manually compile key metrics to CSV
   - [ ] Identify patterns for script development

**Total effort:** 2-3 hours prep + 5-8 hours processing + 1 hour analysis = 8-12 hours

---

### Option B: Full Automation First

**Effort:** 10-15 hours preparation

**Steps:**

1. All steps from Option A, plus:

2. **Build batch processing** (4-6 hours)
   - [ ] Create `scripts/batch-assess.sh`
   - [ ] Integrate with queue.yaml
   - [ ] Add progress tracking

3. **Build aggregation script** (3-4 hours)
   - [ ] Create `scripts/aggregate-corpus-results.py`
   - [ ] Parse credibility-report.md files
   - [ ] Output standardised CSV

4. **Build comparative report template** (2-3 hours)
   - [ ] Summary statistics
   - [ ] Distribution visualisations
   - [ ] Outlier identification

**Total effort:** 10-15 hours prep + 5-8 hours processing = 15-23 hours

---

## Recommendation

**Start with Option A.**

The pipeline is production-ready for the primary use case (single-paper assessment). For an initial corpus run of 10-15 papers:

1. Fix the FAIR denominator issue (blocking)
2. Accept manual processing (efficient enough for 10-15 papers)
3. Build aggregation tools after the first run based on actual needs

This approach:
- Gets results quickly
- Validates the workflow on real corpus
- Informs automation requirements
- Minimises upfront investment before proving value

---

## Action Items (Option A)

- [ ] Add FAIR normalisation guidance to Cluster 3 prompt
- [ ] Select target journal and date range
- [ ] Download 10-15 OA papers
- [ ] Create queue.yaml entries
- [ ] Run production assessments
- [ ] Compile results to CSV
- [ ] Write corpus summary report
- [ ] Decide on automation investment

---

## Candidate Corpus Details

### Internet Archaeology (Recommended)

- **URL:** https://intarch.ac.uk/
- **OA Status:** Full Open Access (no APC, no paywall)
- **Licence:** CC-BY
- **Volume:** ~30 articles/year
- **Advantages:**
  - Archaeology-focused
  - Often includes data supplements
  - Digital-first publication
  - Good mix of methods papers and case studies
- **Date range suggestion:** 2020-2024 (5 years, ~150 papers total)
- **Sample corpus:** 15-20 papers from 2023-2024

### Open Archaeology (Alternative)

- **URL:** https://www.degruyter.com/journal/key/opar/html
- **OA Status:** Full Open Access (APC model)
- **Licence:** CC-BY
- **Volume:** ~50 articles/year
- **Advantages:**
  - Broad archaeological scope
  - Strong methods focus
  - Good FAIR practices in recent years
- **Date range suggestion:** 2022-2024

---

## Related Documentation

- `outputs/variability-test/variability-analysis-report.md` — Pipeline stability analysis
- `planning/extraction-as-data-improvements.md` — Extraction consistency improvements
- `assessment-system/prompts/` — All 7 assessment prompts
- `.claude/skills/research-assessor/references/` — Skill reference documentation

---

*Document created from assessment system review, 2025-12-06*
