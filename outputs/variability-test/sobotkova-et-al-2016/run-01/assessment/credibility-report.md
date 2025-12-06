# Credibility Assessment Report

**Paper:** Sobotkova et al. 2016 — "Measure Twice, Cut Once: Cooperative Deployment of a Generalized, Archaeology-Specific Field Data Collection System"
**Assessment Date:** 2025-12-04
**Assessor Version:** v1.0 (Opus 4.5)
**Run:** run-01 (variability test)

---

## Executive Summary

| Dimension | Score | Rating |
|-----------|-------|--------|
| **Foundational Clarity (C1)** | 75 | Strong |
| **Evidential Strength (C2)** | 66 | Adequate |
| **Reproducibility (C3)** | 62 | Adequate |
| **Aggregate** | 68 | **GOOD** |

**Verdict:** This methodological case study demonstrates **GOOD** credibility overall. The paper presents clear claims about generalised field recording software with adequate evidential support from three deployment case studies. Software transparency is exemplary (open source, GitHub). Analytical methodology has typical qualitative research limitations.

---

## Paper Classification

| Attribute | Value |
|-----------|-------|
| Paper Type | Methodological |
| Research Approach | Inductive (case study) |
| Context Flags | 📦 Software/methodological paper |
| Quality State | HIGH |

**Classification Summary:** Inductive case study evaluating FAIMS mobile platform deployments. Authors are FAIMS team members (positionality noted but not formally disclosed in paper).

---

## Cluster Assessments

### Cluster 1: Foundational Clarity (Transparency Pillar)

| Signal | Score | Band |
|--------|-------|------|
| Comprehensibility | 78 | Good |
| Transparency | 72 | Good |

**Rating: Strong**

The paper achieves strong foundational clarity. Research goals are explicit, claims are well-bounded, and the three-theme structure facilitates comprehension. Software transparency is exemplary (GPLv3, GitHub). Minor gaps include implicit theme derivation and undisclosed positionality.

### Cluster 2: Evidential Strength (Credibility Pillar)

| Signal | Score | Band |
|--------|-------|------|
| Plausibility | 75 | Good |
| Validity | 68 | Good |
| Robustness | 52 | Moderate (📦) |
| Generalisability | 70 | Good |

**Rating: Adequate**

The paper demonstrates adequate evidential strength. Claims are plausible within software engineering and digital archaeology frameworks. Three case studies provide sufficient evidence for pattern identification, though sample size limits generalisation. Robustness is moderate, appropriate for descriptive software papers that document artefacts rather than test hypotheses.

### Cluster 3: Reproducibility (Reproducibility Pillar)

| Signal | Score | Band |
|--------|-------|------|
| Reproducibility | 62 | Good |

**Rating: Adequate**

Using the methodological transparency variant (paper has no computational analysis), reproducibility is adequate. The software itself is fully reproducible (open source). The case study evaluation methodology can be approximated but not precisely reproduced due to implicit analytical procedures.

---

## FAIR Assessment Summary

| Dimension | Score | Notes |
|-----------|-------|-------|
| Findable | 2/4 | No persistent DOI for paper or data |
| Accessible | 3/4 | Software on GitHub; questionnaires in supplementary |
| Interoperable | 2/4 | Standard formats; no formal schemas |
| Reusable | 1/4 | GPLv3 licence; limited metadata |
| **Total** | 8/16 (50%) | **Minimally FAIR** |

**FAIR Context:** 2016 publication predates widespread FAIR adoption. Score reflects era-appropriate practices rather than deficiency relative to contemporaries.

---

## Aggregate Score Calculation

```
Cluster 1 (Transparency):     avg(78, 72) = 75
Cluster 2 (Credibility):      avg(75, 68, 52, 70) = 66
Cluster 3 (Reproducibility):  62

Aggregate = round((75 + 66 + 62) / 3) = 68
```

---

## Strengths

1. **Software Transparency**: Exemplary open-source practices (GPLv3, GitHub, comprehensive documentation)
2. **Clear Claims**: Well-bounded claims with explicit scope and transfer conditions
3. **Convergent Evidence**: Three diverse case studies provide triangulated support
4. **Practical Utility**: Concrete cost data and time-savings evidence for practitioners
5. **Honest Limitations**: Trade-offs and ongoing costs acknowledged

---

## Limitations

1. **Sample Size**: Three case studies limit pattern generalisation
2. **Self-Reported Data**: Reliance on project director reports introduces potential bias
3. **Implicit Analytical Procedures**: Thematic coding and cost calculations not documented
4. **Undisclosed Positionality**: Authors' role as FAIMS developers not formally disclosed
5. **Era-Appropriate Archiving**: No formal data DOIs (pre-FAIR mainstream adoption)

---

## Recommendations

### For Readers

- Claims about FAIMS capabilities can be independently verified via GitHub repository
- Cost figures should be treated as indicative rather than precise (methodology not documented)
- Consider author positionality when evaluating software effectiveness claims

### For Authors (Future Work)

- Document thematic analysis procedures (coding scheme, inter-coder reliability)
- Archive raw questionnaire data with DOI
- Formally disclose author relationships to evaluated software
- Provide cost calculation methodology

### For Citation

This paper provides credible evidence for the benefits of generalised field recording software in archaeology. Claims are appropriately scoped and supported by multi-site case evidence. Readers should evaluate the software directly (open source) and consider the authors' dual role as developers and evaluators.

---

## Classification for Variability Queue

```yaml
verdict: GOOD
aggregate_score: 68
cluster_ratings:
  c1_foundational_clarity: strong
  c2_evidential_strength: adequate
  c3_reproducibility: adequate
fair_score: 8/16
notes: "Full 10-pass extraction + assessment. Methodological case study with exemplary software transparency. Typical qualitative research limitations. 📦 context flag applied."
```

---

## Structured Output

```yaml
credibility_report:
  paper_slug: "sobotkova-et-al-2016"
  assessment_date: "2025-12-04"
  run_id: "run-01"

  classification:
    paper_type: "methodological"
    research_approach: "inductive"
    context_flags: ["📦"]
    quality_state: "high"

  scores:
    c1_comprehensibility: 78
    c1_transparency: 72
    c2_plausibility: 75
    c2_validity: 68
    c2_robustness: 52
    c2_generalisability: 70
    c3_reproducibility: 62

  cluster_ratings:
    c1_foundational_clarity: "strong"
    c2_evidential_strength: "adequate"
    c3_reproducibility: "adequate"

  aggregate:
    c1_average: 75
    c2_average: 66
    c3_average: 62
    overall_score: 68
    verdict: "GOOD"

  fair_assessment:
    total_score: 8
    max_score: 16
    percentage: 50
    rating: "minimally_fair"

  extraction_counts:
    evidence: 35
    claims: 50
    implicit_arguments: 8
    research_designs: 5
    methods: 4
    protocols: 5
```
