# Phase 1: Template Validation Plan

**Date:** 2025-11-30
**Purpose:** Validate the new Pass 10 credibility report template works across diverse paper types
**Scope:** Run Passes 8-10 on 4 papers with existing extractions
**Status:** COMPLETED

---

## Objective

Test the unified credibility report template (created in previous session) on 4 papers representing different paper types and research approaches. Confirm the template generalises beyond the initial test case (ross-ballsun-stanton-2022).

---

## Target Papers

| Paper | Type | Approach | Extraction Status |
|-------|------|----------|-------------------|
| **sobotkova-et-al-2024** | Empirical | Quantitative validation | Complete (100 items) |
| **penske-et-al-2023** | Empirical | Archaeogenetics (complex) | Complete (248 items) |
| **ballsun-stanton-et-al-2018** | Methodological | Software tool | Complete (95 items) |
| **ross-2005** | Interpretive | Philological/literary | Complete (128 items) |

**Diversity coverage:**
- 2 empirical papers (quantitative + complex multi-method)
- 1 methodological paper (software)
- 1 interpretive/theoretical paper (philology)

---

## Passes to Execute

For each paper, run the following passes in sequence:

| Pass | Name | Input | Output |
|------|------|-------|--------|
| **8** | Research Approach Classification | `extraction.json` | `assessment/classification.md` |
| **8.5** | Track A Quality Gating | `extraction.json`, `classification.md` | `assessment/track-a-quality.md` |
| **9.1** | Cluster 1: Foundational Clarity | `extraction.json`, `classification.md` | `assessment/cluster-1-foundational-clarity.md` |
| **9.2** | Cluster 2: Evidential Strength | `extraction.json`, `classification.md` | `assessment/cluster-2-evidential-strength.md` |
| **9.3** | Cluster 3: Reproducibility | `extraction.json`, `classification.md` | `assessment/cluster-3-reproducibility.md` |
| **10** | Final Report | All cluster outputs | `assessment/credibility-report.md` |

**Total:** 4 papers × 6 passes = 24 pass invocations

---

## Execution Strategy

**Per-paper sequential execution:**
1. Complete all passes for Paper 1
2. Complete all passes for Paper 2
3. Complete all passes for Paper 3
4. Complete all passes for Paper 4

**Rationale:** Each pass depends on previous outputs; completing one paper fully before moving to the next allows early detection of template issues.

**Commit strategy:** Batch commit after all 4 papers complete (single commit).

**Variant detection:** Let the system detect whether to apply Methodological Transparency variant for ross-2005 (tests system capability).

---

## Prompt Files

- `assessment-system/prompts/classify-research-approach.md` (Pass 8)
- `assessment-system/prompts/track-a-quality-gating.md` (Pass 8.5)
- `assessment-system/prompts/cluster-1-foundational-clarity.md` (Pass 9.1)
- `assessment-system/prompts/cluster-2-evidential-strength.md` (Pass 9.2)
- `assessment-system/prompts/cluster-3-reproducibility.md` (Pass 9.3)
- `assessment-system/prompts/10-final-report-prompt.md` (Pass 10)

---

## Validation Criteria

For each paper, verify:

1. **Classification output** - Paper type and approach correctly identified
2. **Quality gating** - Quality state determined (HIGH/MODERATE/LOW)
3. **All 7 signals scored** - No missing scores in cluster outputs
4. **JSON valid** - Structured output in credibility report parseable with jq/python
5. **Context flags appropriate** - Paper-type-specific flags applied correctly
6. **Verdict reasonable** - Overall verdict aligns with signal scores

---

## Success Metrics

| Metric | Target |
|--------|--------|
| Papers completed | 4/4 |
| JSON validation | 100% valid |
| Signal coverage | All 7 signals for all papers |
| Template errors | 0 blocking issues |
| Classification accuracy | Manual review confirms reasonable |

---

## Output Summary

After completion, generate a comparison table:

| Paper | Type | Quality State | Verdict | Aggregate | Signals Range |
|-------|------|---------------|---------|-----------|---------------|
| sobotkova-et-al-2024 | ? | ? | ? | ? | ? |
| penske-et-al-2023 | ? | ? | ? | ? | ? |
| ballsun-stanton-et-al-2018 | ? | ? | ? | ? | ? |
| ross-2005 | ? | ? | ? | ? | ? |

---

## Execution Checklist

### Paper 1: sobotkova-et-al-2024
- [x] Pass 8: Classification
- [x] Pass 8.5: Quality gating
- [x] Pass 9.1: Cluster 1
- [x] Pass 9.2: Cluster 2
- [x] Pass 9.3: Cluster 3
- [x] Pass 10: Final report
- [x] Validation: JSON valid, scores complete

### Paper 2: penske-et-al-2023
- [x] Pass 8: Classification
- [x] Pass 8.5: Quality gating
- [x] Pass 9.1: Cluster 1
- [x] Pass 9.2: Cluster 2
- [x] Pass 9.3: Cluster 3
- [x] Pass 10: Final report
- [x] Validation: JSON valid, scores complete

### Paper 3: ballsun-stanton-et-al-2018
- [x] Pass 8: Classification
- [x] Pass 8.5: Quality gating
- [x] Pass 9.1: Cluster 1
- [x] Pass 9.2: Cluster 2
- [x] Pass 9.3: Cluster 3
- [x] Pass 10: Final report
- [x] Validation: JSON valid, scores complete

### Paper 4: ross-2005
- [x] Pass 8: Classification
- [x] Pass 8.5: Quality gating
- [x] Pass 9.1: Cluster 1
- [x] Pass 9.2: Cluster 2
- [x] Pass 9.3: Cluster 3
- [x] Pass 10: Final report
- [x] Validation: JSON valid, scores complete

---

## Post-Validation Analysis

After all 4 papers complete:
1. Compare verdicts and scores across paper types
2. Review context flag application (especially ross-2005 variant detection)
3. Identify any template improvements needed
4. Document findings for Phase 2 planning
5. **Create summary file:** `outputs/phase-1-validation-summary.md`

---

## Files to Create/Modify

**New files (per paper):**
- `outputs/{slug}/assessment/classification.md`
- `outputs/{slug}/assessment/track-a-quality.md`
- `outputs/{slug}/assessment/cluster-1-foundational-clarity.md`
- `outputs/{slug}/assessment/cluster-2-evidential-strength.md`
- `outputs/{slug}/assessment/cluster-3-reproducibility.md`
- `outputs/{slug}/assessment/credibility-report.md`

**Summary output (confirmed):**
- `outputs/phase-1-validation-summary.md` — comparison table, findings, template observations

---

## Estimated Effort

- Per paper: ~20-30 minutes (6 passes)
- Total: ~2 hours for 4 papers
- Plus validation and summary: ~30 minutes

**Total estimated time:** 2.5 hours

---

## Decisions Confirmed

| Decision | Choice |
|----------|--------|
| Summary file | Yes — create `phase-1-validation-summary.md` |
| Variant handling | Let system detect (test capability) |
| Commit strategy | Batch at end (single commit) |
| Paper selection | 4 papers as listed above |

---

## Completion Notes

**Completed:** 2025-11-30

**Results:**

| Paper | Type | Quality State | Verdict | Aggregate |
|-------|------|---------------|---------|-----------|
| sobotkova-et-al-2024 | Empirical/Deductive | HIGH | Good | 76 |
| penske-et-al-2023 | Empirical/Inductive | HIGH | Good | 79 |
| ballsun-stanton-et-al-2018 | Methodological | HIGH | Good | 72 |
| ross-2005 | Empirical/Interpretive | HIGH | Good | 71 |

**Key findings:**
- Template works across all 4 paper types
- Context flags (📦, 🔧) applied correctly
- Era calibration functional
- All scores in Good band (71-79)

**Follow-up actions:**
- Reframed "advocacy" → "software paper genre expectations" for ballsun-stanton-et-al-2018
- Updated prompts with expanded context flag guidance (📦, 📐, 🔧)

**Commits:**
- `2cfd52c` - Phase 1 template validation (4 papers)
- `afaba61` - Reframe software paper context
- `90d50d8` - Add context flags for specialised paper types
