# Credibility Assessment Report

**Paper:** Sobotkova, A., Ross, S.A., Ballsun-Stanton, B., Fairbairn, A., Thompson, J., & VanValkenburgh, P. (2016). Measure Twice, Cut Once: Cooperative Deployment of a Generalized, Archaeology-Specific Field Data Collection System.

**Run ID:** run-02
**Assessment Date:** 2025-12-04
**Framework:** repliCATS Seven Signals (HASS Adaptation)
**Quality Gate:** MODERATE (Caveated Assessment)

---

## Executive Summary

This methodological paper presents a compelling case for generalised software co-development in archaeology through three FAIMS deployment case studies. The paper achieves **moderate-high credibility** with particular strength in software transparency and practical applicability. Quantitative claims should be interpreted as indicative rather than precise due to informal measurement methodology.

### Overall Credibility Score: 68/100

| Pillar | Score | Weight | Weighted |
|--------|-------|--------|----------|
| Transparency | 72 | 0.30 | 21.6 |
| Credibility | 64 | 0.40 | 25.6 |
| Reproducibility | 72 | 0.30 | 21.6 |
| **Total** | | | **68.8** |

**Interpretation:** Moderate-high credibility for a methodological paper. Strong practical guidance for digital archaeology adoption, with appropriate caveats on quantitative claims.

---

## Three Pillars Assessment

### Pillar 1: Transparency (72/100)

**Cluster 1: Foundational Clarity**

| Signal | Score | Notes |
|--------|-------|-------|
| Comprehensibility | 75 | Clear presentation; minor terminology gaps |
| Transparency | 70 | Strong code availability; informal metrics |

**Key Strengths:**
- Open source software with clear licensing (GPLv3)
- Communication logs preserved as supplementary materials
- Dual-perspective authorship (developers + users) explicitly acknowledged

**Key Weaknesses:**
- Authors' conflict of interest (as FAIMS developers) not disclosed
- Supplementary materials lack persistent identifiers
- Case study selection criteria unstated

---

### Pillar 2: Credibility (64/100)

**Cluster 2: Evidential Strength**

| Signal | Score | Notes |
|--------|-------|-------|
| Plausibility | 78 | Claims align with domain knowledge |
| Validity | 65 | Appropriate design; informal quantitative methods |
| Robustness | 58 | Limited by sample size and positive selection |
| Generalisability | 55 | Diverse contexts but resource-intensive model |

**Key Strengths:**
- Coherent theoretical framing (generalised vs bespoke software spectrum)
- Consistent with established software engineering and archaeological fieldwork knowledge
- Multiple perspectives and diverse deployment contexts

**Key Weaknesses:**
- Three case studies insufficient for robust generalisation
- Self-reported metrics without independent verification
- Absence of failure cases or abandoned deployments

---

### Pillar 3: Reproducibility (72/100)

**Cluster 3: Reproducibility**

| Component | Score | Notes |
|-----------|-------|-------|
| Software Reproducibility | 85 | Excellent open-source availability |
| Process Reproducibility | 70 | Good documentation; tacit knowledge gaps |
| Analytical Reproducibility | 62 | Informal quantitative methodology |

**Key Strengths:**
- FAIMS software genuinely open and accessible
- Module customisation process documented
- Evidence of successful independent deployments (doctoral students)

**Key Weaknesses:**
- No DOI for software or data
- Support dependency for full deployment
- Cost/time calculations methodology unstated

---

## Signal Summary

| Signal | Score | Confidence |
|--------|-------|------------|
| Comprehensibility | 75 | High |
| Transparency | 70 | Moderate |
| Plausibility | 78 | High |
| Validity | 65 | Moderate |
| Robustness | 58 | Moderate |
| Generalisability | 55 | Low-Moderate |
| Reproducibility | 72 | Moderate |

---

## Critical Caveats

### Caveat 1: Author Conflict of Interest

The authors include FAIMS development team members who have financial and professional stakes in FAIMS success. While their dual positioning as developers and archaeological users enables unique insights, it also creates potential bias. The paper does not include a conflict of interest declaration.

**Impact:** May affect objectivity of cost-benefit assessments and selection of evidence.

### Caveat 2: Quantitative Claims Basis

Time savings (E021-E025), cost figures (E008-E012), and performance metrics (E026-E027) are self-reported estimates without documented measurement methodology. Claims like "95% labour saving" and "at least eight person-days saved" should be interpreted as indicative orders of magnitude rather than precise measurements.

**Impact:** Reduces confidence in specific quantitative claims; directional conclusions remain plausible.

### Caveat 3: Selection Bias

The three case studies represent early adopters who volunteered for FAIMS partnership. Projects that evaluated and rejected FAIMS, or that attempted deployment and failed, are not represented. This positive selection may overstate benefits and understate challenges.

**Impact:** Generalisation to reluctant adopters or resource-constrained projects should be made cautiously.

---

## Contextual Interpretation

### Paper Type: Methodological

This is appropriately assessed as a methods paper rather than an empirical study. The relevant reproducibility question is "Can others deploy FAIMS?" rather than "Can others reproduce the archaeological findings?"

### Research Approach: Inductive

The paper works from specific deployment experiences to general claims about software co-development. This is appropriate for exploratory methodological work but limits the confidence of generalised claims.

### Domain Context: Digital Archaeology

The paper represents important early documentation of archaeological software co-development. As a 2016 publication, it predates current best practices in research software citation and open science, which should be considered when evaluating infrastructure practices.

---

## Recommendations

### For Readers

1. **Trust software availability claims:** FAIMS is genuinely open and accessible
2. **Use caution with specific numbers:** Treat quantitative claims as illustrative rather than precise
3. **Consider context:** Resource requirements may limit applicability to smaller projects
4. **Verify current status:** 2016 software and costs will have evolved

### For Future Research

1. **Systematic evaluation:** Independent assessment with controlled comparison groups
2. **Failure case documentation:** Learning from unsuccessful deployments
3. **Longitudinal tracking:** Multi-season deployment outcomes
4. **Broader sampling:** Non-partner projects using FAIMS independently

### For Replication

1. **Start with current FAIMS:** Software has evolved since 2016
2. **Budget for support:** Self-deployment possible but support recommended
3. **Allow customisation time:** 3-15 weeks depending on complexity
4. **Test on target hardware:** Android fragmentation requires device-specific testing

---

## Assessment Metadata

| Field | Value |
|-------|-------|
| Assessment Framework | repliCATS Seven Signals (HASS) v2.6 |
| Quality Gate | MODERATE |
| Paper Classification | Methodological |
| Research Approach | Inductive |
| Assessor | claude-opus-4-5-20251101 |
| Assessment Date | 2025-12-04 |
| Run ID | run-02 |

---

*Assessment complete. This caveated report reflects moderate extraction quality and methodological paper standards.*
