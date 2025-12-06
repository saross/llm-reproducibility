# Cluster 2: Evidential Strength (Credibility Pillar)

**Paper:** Sobotkova et al. (2016) - Measure Twice, Cut Once
**Run ID:** run-04
**Assessment Date:** 2025-12-04

---

## Signal Assessments

### 1. Plausibility

**Definition:** Are the claims plausible given the evidence and prior knowledge?

#### Inductive Anchors Applied

| Score Range | Description | Paper Alignment |
|-------------|-------------|-----------------|
| 80-100 | Claims well-supported by evidence, consistent with domain knowledge | **Best fit** |
| 60-79 | Most claims plausible, some require additional support | — |
| 40-59 | Mixed plausibility, some claims weakly supported | — |
| 20-39 | Claims often exceed evidence | — |
| 0-19 | Implausible or unsupported claims | — |

#### Assessment

**Strengths:**
- Core claims about time savings supported by specific quantitative evidence (E019-E023)
- Claims about co-development challenges consistent with software engineering literature
- Cost figures are detailed and internally consistent
- Case study evidence aligns with broader digital archaeology discourse
- Claims are appropriately hedged ("usually," "generally," "likely")

**Weaknesses:**
- Some claims about future adoption are speculative (C011: projects to double by 2017)
- Self-reported time savings may overestimate benefits
- Claims about data quality improvements lack independent verification
- Generalisations from three case studies may be optimistic

**Evidence Mapping:**
- C021 (eliminates digitisation) ← E019, E020 (quantified savings)
- C022 (time savings substantial) ← E019, E021 (specific AUD figures)
- C024 (tablets huge advantage) ← E022 (eight person-days)
- C039 (improved data richness) ← Qualitative testimonials only

#### Score: **78/100**

**Justification:** Claims are generally well-supported and plausible. The quantitative evidence for time/cost savings is particularly strong. Some claims about data quality rely on self-report rather than independent verification, and projections about future adoption are inherently uncertain. Overall, claims are appropriately scoped to the evidence presented.

---

### 2. Validity

**Definition:** Are the methods appropriate for the claims being made?

#### Inductive Anchors Applied

| Score Range | Description | Paper Alignment |
|-------------|-------------|-----------------|
| 80-100 | Research design well-matched to claims, appropriate methods throughout | — |
| 60-79 | Generally appropriate methods, some limitations | **Best fit** |
| 40-59 | Methods partially appropriate, significant gaps | — |
| 20-39 | Methods poorly matched to claims | — |
| 0-19 | Inappropriate methods | — |

#### Assessment

**Strengths:**
- Case study approach appropriate for exploratory evaluation of new technology
- Mixed methods (qualitative + quantitative) suitable for complex intervention
- Longitudinal tracking through deployment cycle captures temporal dynamics
- First-person practitioner accounts provide rich contextual detail

**Weaknesses:**
- Case study selection may be biased (project directors "offered to share" - volunteers)
- No comparison group (projects without FAIMS)
- Self-reported outcomes subject to social desirability bias
- Authors include FAIMS developers evaluating their own system
- Thematic analysis not systematically documented

**Evidence:**
- RD001: Multi-case study design appropriate for exploratory research
- M001: Purposive sampling based on diversity, but selection criteria opaque
- IA005: Assumption that three cases sufficient for generalisation
- IA009: Potential bias from FAIMS team authorship

#### Score: **65/100**

**Justification:** The case study approach is appropriate for this type of methodological paper, and the mixed methods design captures both qualitative experiences and quantitative outcomes. However, validity is compromised by potential selection bias (volunteer project directors), lack of comparison group, self-evaluation by developers, and absence of systematic thematic analysis documentation.

---

### 3. Robustness

**Definition:** How sensitive are the findings to analytical choices and alternative specifications?

#### Inductive Anchors Applied

| Score Range | Description | Paper Alignment |
|-------------|-------------|-----------------|
| 80-100 | Multiple analytical approaches tested, findings stable across variations | — |
| 60-79 | Some sensitivity testing, findings generally robust | — |
| 40-59 | Limited testing, robustness uncertain | **Best fit** |
| 20-39 | No sensitivity testing, findings potentially fragile | — |
| 0-19 | Findings clearly non-robust | — |

#### Assessment

**Strengths:**
- Themes identified across three different archaeological contexts (Turkey, Malawi, Peru)
- Consistent findings across different project types (excavation, survey)
- Quantitative findings from multiple projects converge on similar conclusions

**Weaknesses:**
- No explicit sensitivity analysis or alternative interpretations considered
- Single platform (FAIMS) - no comparison with alternative systems
- All projects used same "deluxe excavation" base module
- No negative cases discussed (unsuccessful deployments)
- Three case studies limits ability to assess generalisability

**Evidence:**
- E016, E017: Different iteration counts suggest some variability
- E018-E025: Convergent evidence on time savings across projects
- IA005: Limited sample size for generalisation

#### Score: **52/100**

**Justification:** The paper provides convergent evidence across three cases, which is a strength. However, there is no explicit sensitivity analysis, no consideration of alternative interpretations, and no discussion of unsuccessful deployments. The findings appear to be consistent but the limited sample size and single-platform focus make robustness difficult to assess.

---

### 4. Generalisability

**Definition:** To what extent do findings apply beyond the specific study context?

#### Inductive Anchors Applied

| Score Range | Description | Paper Alignment |
|-------------|-------------|-----------------|
| 80-100 | Clear evidence of applicability beyond study context | — |
| 60-79 | Reasonable basis for limited generalisation | — |
| 40-59 | Generalisability uncertain, significant caveats needed | **Best fit** |
| 20-39 | Findings likely context-specific | — |
| 0-19 | No basis for generalisation | — |

#### Assessment

**Strengths:**
- Diverse geographical contexts (Turkey, Malawi, Peru) support some generalisability
- Different project scales and archaeological periods represented
- Authors explicitly address applicability to "any field software development project"
- Lessons framed as general principles rather than FAIMS-specific

**Weaknesses:**
- All projects used same software platform
- All projects had relationship with FAIMS team for support
- Archaeological context limits applicability to other field sciences
- 2014 technology context may not apply to current systems
- All project directors were English-speaking academics

**Evidence:**
- C048: Explicit claim that lessons apply to "any field software development project"
- IA005: Assumption that three cases sufficient for generalisation
- E008: 17 projects total, but only 3 discussed in detail

#### Score: **55/100**

**Justification:** The paper makes explicit generalisability claims, and the diversity of archaeological contexts provides some support. However, generalisability is constrained by the single-platform focus, the consistent relationship with FAIMS developers, and the specific 2014 technology context. The lessons may apply more broadly to field software co-development but this is asserted rather than demonstrated.

---

## Cluster 2 Summary

| Signal | Score | Weight | Weighted Score |
|--------|-------|--------|----------------|
| Plausibility | 78 | 0.25 | 19.5 |
| Validity | 65 | 0.25 | 16.25 |
| Robustness | 52 | 0.25 | 13.0 |
| Generalisability | 55 | 0.25 | 13.75 |
| **Cluster 2 Total** | — | — | **62.5** |

**Cluster Assessment:** MODERATE

The paper demonstrates moderate evidential strength. Claims are plausible and generally well-supported by evidence. However, validity is compromised by potential biases (self-evaluation, volunteer participants), and robustness/generalisability are limited by the small sample size and single-platform focus. The paper's claims are appropriately scoped but the evidence base is narrow.
