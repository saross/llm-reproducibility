# Research Design Anchoring: Assessment and Low-Risk Solution

**Created:** 2025-12-06
**Source:** Variability test analysis (25 runs) + prompt review
**Purpose:** Document findings on potential RD count anchoring; propose low-risk adjustment
**Priority:** LOW — bundle with future extraction-as-data work if undertaken

---

## Context

During variability analysis, research design (RD) extraction showed notably tighter clustering than other arrays. This document assesses whether the "4-6 research designs per paper" guidance in `research-design-operational-guide.md` is creating anchoring effects.

---

## Findings

### Observed Count Distribution

| Paper | RD Counts (5 runs) | CV% | Pattern |
|-------|-------------------|-----|---------|
| sobotkova-et-al-2024 | 6, 6, 5, 6, 6 | ~7% | Very tight at 6 |
| penske-et-al-2023 | 4, 5, 4, 4, 4 | ~10% | Very tight at 4 |
| ballsun-stanton-2018 | 3, 3, 4, 4, 4 | ~15% | Tight at 3-4 |
| ross-2005 | 2, 2, 2, 2, 2 | 0% | Perfect stability at 2 |
| sobotkova-et-al-2016 | 5, 5, 6, 5, 1 | ~45% | Mostly tight, one outlier |

### Comparison with Other Arrays

| Array | CV% Range | Interpretation |
|-------|-----------|----------------|
| **Research Designs** | 0-45% | Tightest clustering |
| Implicit Arguments | 0-18% | Also tight (high abstraction) |
| Methods | 12-35% | Moderate |
| Evidence | 7-31% | Moderate |
| Claims | 3-28% | Moderate |
| Protocols | 25-138% | Highest variability |

Research designs and implicit arguments (both high-abstraction arrays) show tighter clustering than granular arrays like evidence and claims. This pattern is expected — strategic decisions are inherently less granular than data points.

### Current Guidance Language

From `research-design-operational-guide.md`:

**Line 3 (Purpose statement):**
> "Operational guidance for extracting 4-6 research designs per paper (vs common under-extraction of 1-2)"

**Lines 262-278 (Quality checks):**
> "If <3 Research Designs: [review checklist]"
> "If >10 Research Designs: [review checklist]"
> "Quality Over Count: Extract what's genuinely present in the paper"

The "4-6" appears prominently in the purpose statement, potentially creating anchoring.

---

## Assessment

### Evidence AGAINST Damaging Anchoring

| Observation | Implication |
|-------------|-------------|
| ross-2005 consistently extracts 2 RDs | Model respects content over targets |
| sobotkova-et-al-2016 run-05 extracted 1 RD | Model can go very low |
| Papers get different counts (2, 4, 5, 6) | Not uniform clustering at single value |
| "Quality Over Count" messaging present | Guidance already includes counter-anchoring |

### Evidence FOR Mild Anchoring

| Observation | Implication |
|-------------|-------------|
| CV% much lower than other variable arrays | Tighter than expected from independence |
| No paper exceeds 6 RDs | Possible ceiling effect |
| "4-6" prominent in purpose statement | Strong anchoring cue |

### Impact on Assessment Outcomes

**Cluster 1 (Foundational Clarity)** ratings were stable across runs despite RD count variation:

| Paper | RD Range | C1 Rating Stability |
|-------|----------|---------------------|
| sobotkova-et-al-2024 | 5-6 | 100% Strong |
| penske-et-al-2023 | 4-5 | 100% Strong |
| ballsun-stanton-2018 | 3-4 | 100% Strong |
| ross-2005 | 2 | 80% Adequate, 20% Adequate-to-Strong |
| sobotkova-et-al-2016 | 1-6 | 80% Strong/Adequate, 20% Moderate-High |

Even the sobotkova-et-al-2016 run with 1 RD produced coherent assessment. **Assessment outcomes are not sensitive to RD count variability.**

### Conclusion

**Mild anchoring likely exists but is not causing measurable harm to assessments.**

The model appropriately extracts fewer RDs for papers with fewer strategic decisions (ross-2005). The tight clustering may reflect:
1. Genuine convergence (papers actually have 4-6 RDs)
2. Mild anchoring (model stops looking after ~6)
3. Both factors combined

Without expert baseline comparison, we cannot definitively distinguish these explanations.

---

## Recommendation

### Overall: No Urgent Action Required

For the primary use case (credibility assessment), current RD extraction is adequate. Assessment outcomes are stable regardless of count variation.

### If Undertaking Extraction-as-Data Work: Low-Risk Adjustment

Bundle the following changes with other extraction-as-data improvements (see `planning/extraction-as-data-improvements.md`):

#### Change 1: Soften Purpose Statement

**Current (`research-design-operational-guide.md` line 3):**
```markdown
**Purpose:** Operational guidance for extracting 4-6 research designs per paper (vs common under-extraction of 1-2)
```

**Proposed:**
```markdown
**Purpose:** Operational guidance for extracting all strategic research decisions (typically 3-8, varies significantly by paper type)
```

#### Change 2: Adjust Quality Check Thresholds

**Current (lines 262-269):**
```markdown
**If <3 Research Designs:**
- [ ] Re-scan Abstract/Introduction for research questions/aims
...

**If >10 Research Designs:**
- [ ] Check: Does each RD have independent justification?
...
```

**Proposed:**
```markdown
**If <2 Research Designs:**
- [ ] Re-scan Abstract/Introduction for research questions/aims
...

**If >12 Research Designs:**
- [ ] Check: Does each RD have independent justification?
...
```

#### Change 3: Add Paper-Type Guidance

**Add after quality checks:**
```markdown
### Paper-Type Expectations (Guidelines, Not Targets)

| Paper Type | Typical RD Range | Notes |
|------------|------------------|-------|
| Empirical (deductive) | 4-8 | Hypothesis, study design, scope, framework |
| Empirical (inductive) | 3-6 | Research questions, study design, scope |
| Methodological | 4-7 | Design rationale, comparative framework, scope |
| Interpretive/Theoretical | 2-5 | Research framing, theoretical positioning |

These are descriptive observations, not prescriptive targets. Extract what is present.
```

---

## Risk Assessment

**Risk Level:** 🟢 **LOW**

| Factor | Assessment |
|--------|------------|
| **Additive vs breaking** | Additive — loosens constraints, doesn't change logic |
| **Regression risk** | Minimal — may increase RD counts slightly |
| **Spillover** | None — RD extraction is independent of other arrays |
| **Testability** | High — can compare CV% before/after on same papers |

---

## Action Items (Conditional)

**Only if undertaking extraction-as-data improvements:**

- [ ] Update purpose statement in `research-design-operational-guide.md`
- [ ] Adjust quality check thresholds (<2 and >12)
- [ ] Add paper-type expectations table
- [ ] Test on 2 papers from variability corpus
- [ ] Compare RD CV% before/after

**Do NOT prioritise independently** — bundle with other extraction-as-data work.

---

## Related Documentation

- `planning/extraction-as-data-improvements.md` — Parent improvement plan
- `outputs/variability-test/variability-analysis-report.md` — Full variability analysis
- `.claude/skills/research-assessor/references/research-design-operational-guide.md` — Current guidance

---

*Document created from variability analysis discussion, 2025-12-06*
