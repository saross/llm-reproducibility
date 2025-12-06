# Cluster 2: Evidential Strength Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-12-05
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** deductive
**Paper Type:** empirical

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Plausibility | 75 | Good | deductive |
| Validity | 78 | Good | deductive |
| Robustness | 68 | Good | deductive |
| Generalisability | 65 | Good | deductive |

**Cluster Rating:** Strong

---

## Signal 3: Plausibility

**Score:** 75/100 (Good)

**Approach anchors applied:** deductive

### Assessment

The paper demonstrates good plausibility for its deductive hypothesis test. The central hypothesis - that transfer learning with pre-trained CNNs can detect archaeological features - is grounded in established ML literature and prior archaeological applications (Can et al. 2018, Caspari and Crespo 2019, Davis 2019). The theoretical framework appropriately acknowledges that CNN feature detectors trained on natural images may transfer to archaeological features, while also recognising potential limitations in heterogeneous landscapes.

Anomalous results are thoroughly acknowledged and explained. The counterintuitive finding (curated training data performed worse) is explicitly addressed: "Counterintuitively, the model provided with training data selected for highly visible mounds (rather than all mounds) performed worse." The paper contextualises this within broader ML archaeology literature, noting publication bias (63% of abstracts fail to mention negative aspects).

Minor plausibility gaps exist around auxiliary assumptions - the paper assumes that mound visibility in satellite imagery correlates with mound detectability by CNNs, and that ground-truth data from 2009-2011 fieldwork remains valid for 2021-2022 imagery analysis. These assumptions are reasonable but not explicitly justified.

### Evidence

**Strengths:**
- C003: Theoretical grounding in established ML limitations: "Pre-trained CNNs struggle with varied features of different sizes within heterogeneous landscapes containing confounding natural and modern features"
- RD001: Clear theoretical rationale for transfer learning approach with acknowledgment of known constraints
- Anomaly handling: Publication bias analysis (RD006) contextualises findings within field-wide patterns

**Weaknesses:**
- IA002/IA004: Implicit assumptions about training data sufficiency and transferability not fully justified
- Ground-truth temporal gap (2009-2011 fieldwork vs 2021-2022 imagery) not explicitly addressed

### Scoring Rationale

Score of 75 reflects Good plausibility: hypothesis theoretically motivated by prior ML archaeology work, interpretations consistent with domain knowledge, major anomalies (curated data performing worse) acknowledged and explained. Falls short of Excellent due to some implicit auxiliary assumptions about data validity and transferability.

---

## Signal 4: Validity

**Score:** 78/100 (Good)

**Approach anchors applied:** deductive

### Assessment

The paper demonstrates strong validity for hypothesis-testing research. The evidence directly addresses the hypothesis: 773 field-verified mounds provide robust ground truth for validation, and model predictions are systematically compared against this dataset. Quantitative results (95-96% false negative, 87-95% false positive) directly support the central claim of model failure.

The two-run comparative design (2021 vs 2022) with controlled variable (training data curation) strengthens validity by enabling causal inference about data preparation effects. Sample size is substantial - 773 mounds, 400+ tiles - providing statistical power for the validation claims. Methods are appropriate: field-verified coordinates from systematic archaeological survey, tile-based CNN prediction, spatial validation using GIS.

Potential confounds are addressed but not fully controlled. The paper acknowledges landscape heterogeneity, mound preservation variability, and satellite imagery resolution constraints. The comparison with Can et al. (2018) reference provides external benchmark context. Evidence sufficiency is high for the central claims.

### Evidence

**Strengths:**
- E001: Comprehensive quantitative results - "tile-based false negative rates were 95–96%, false positive rates were 87–95%"
- RD003: Field validation design with independent ground-truth - 773 mounds from TRAP survey
- E020: Comparative second run results enabling controlled comparison

**Weaknesses:**
- No blind validation (model developers also conducted field validation)
- Single study area limits ability to separate landscape effects from model effects
- P013 (implicit): Mound visibility assessment criteria for 2022 training data undocumented

### Scoring Rationale

Score of 78 reflects Good validity: evidence directly addresses hypothesis, substantial sample (773 mounds), appropriate methods, controlled comparison design. Falls short of Excellent due to lack of blind validation, single study area, and some undocumented selection criteria.

---

## Signal 5: Robustness

**Score:** 68/100 (Good)

**Approach anchors applied:** deductive

### Assessment

The paper demonstrates moderate-to-good robustness through its two-run comparative design, which tests sensitivity to training data curation (the main analytical choice examined). The fact that both runs produced similarly poor results (4.9% vs <1% detection rate) strengthens confidence that findings are not dependent on specific analytical choices.

However, limited systematic robustness testing is documented. The paper does not report sensitivity analyses for: detection threshold (fixed at 60%), data augmentation parameters, learning rate, or model architecture. The choice of ResNet-50 over other architectures is justified narratively (P014 implicit) but not through systematic comparison. Random seed documentation is absent, affecting exact reproducibility.

The comparative literature review adds interpretive robustness by contextualising findings within broader ML archaeology patterns. The two-run design provides more robustness than single-run studies but falls short of comprehensive sensitivity analysis.

### Evidence

**Strengths:**
- RD002: Two-run comparison tests training data curation sensitivity
- E001/E020: Consistent poor performance across both runs suggests robust finding
- Literature review contextualisation strengthens interpretation robustness

**Weaknesses:**
- P014 (implicit): Model selection protocol undocumented - architecture sensitivity not tested
- No sensitivity analysis for detection threshold (60%), augmentation parameters, or learning rate
- Random seeds not documented - exact reproducibility uncertain

### Scoring Rationale

Score of 68 reflects Good robustness at lower end of band: two-run comparison provides meaningful sensitivity test, consistent results across runs strengthen confidence. Falls short of higher Good or Excellent due to limited systematic robustness testing beyond the data curation variable.

---

## Signal 6: Generalisability

**Score:** 65/100 (Good)

**Approach anchors applied:** deductive

### Assessment

The paper demonstrates appropriate generalisability by clearly bounding scope claims and explicitly discussing limitations. Core claims are appropriately scoped to the study context: "the promise and reality of machine learning" framing signals this is a cautionary case study, not a universal claim about ML archaeology.

Explicit limitations acknowledged include: landscape heterogeneity ("confounding natural and modern features"), mound variability (7-40m diameter range), and resolution constraints. The paper avoids overgeneralising - conclusions focus on what transfer learning approaches struggle with rather than claiming ML never works.

However, single-case inference limits generalisability. The study examines one landscape (Kazanlak Valley), one image source (IKONOS), one model family (ResNet-50 with transfer learning), and one feature type (burial mounds). The paper appropriately acknowledges these limitations but cannot address them empirically. The claim that "curated training data performs worse" may be context-specific.

### Evidence

**Strengths:**
- Appropriate scope bounding: "the promise and reality" framing signals case study nature
- Explicit limitations discussion: landscape heterogeneity, resolution, mound variability
- Comparative context: Can et al. (2018) provides external reference point

**Weaknesses:**
- Single study area (Kazanlak Valley) limits landscape generalisability
- Single model family (ResNet-50) limits architecture generalisability
- Counterintuitive curation finding may not generalise to other contexts

### Scoring Rationale

Score of 65 reflects Good generalisability at lower end of band: scope appropriately bounded, limitations explicitly acknowledged, overgeneration avoided. Score reflects inherent limitations of single-case study design rather than methodological deficiency.

---

## Cluster Synthesis

**Overall Evidential Strength:** Strong

All four signals score in the Good band (65-78), with validity (78) and plausibility (75) strongest. The paper demonstrates solid credibility as hypothesis-testing research: theoretical grounding is adequate, evidence directly tests hypothesis, two-run comparison provides meaningful robustness test, and generalisability limitations are appropriately acknowledged.

### Pattern Summary

The pattern across Cluster 2 signals reflects well-executed empirical research with appropriate epistemic humility. Strengths concentrate in validity (direct evidence-hypothesis connection) and plausibility (theoretical grounding, anomaly handling). Relative weaknesses in robustness (limited sensitivity testing) and generalisability (single-case design) reflect study design constraints rather than methodological failures.

### Implications for Subsequent Assessment

- **For Cluster 3 (Reproducibility):** Strong validity and transparency foundation support reproducibility assessment. Asymmetric reproducibility profile (code available, data not) will be primary consideration.
- **For Final Report:** Aggregate score in Good range (65-78) indicates credible research with appropriate limitations. Negative findings (hypothesis rejection) are well-supported.

---

## Structured Output

```yaml
cluster_2_evidential_strength:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-12-05"
  quality_state: "high"
  research_approach: "deductive"

  plausibility:
    score: 75
    band: "good"
    strengths:
      - "Hypothesis grounded in established ML and archaeological theory"
      - "Anomalous results (curated data worse) explicitly addressed"
      - "Publication bias analysis contextualises findings"
    weaknesses:
      - "Some auxiliary assumptions implicit (ground-truth temporal validity)"
    rationale: "Good plausibility with theoretical grounding and anomaly acknowledgment. Minor gaps in auxiliary assumption justification."

  validity:
    score: 78
    band: "good"
    strengths:
      - "Evidence directly addresses hypothesis (773 field-verified mounds)"
      - "Two-run comparative design enables controlled inference"
      - "Quantitative results clearly support central claims"
    weaknesses:
      - "No blind validation"
      - "Single study area limits confound control"
    rationale: "Good validity with direct evidence-hypothesis connection and controlled comparison. Falls short of excellent due to validation design limitations."

  robustness:
    score: 68
    band: "good"
    strengths:
      - "Two-run comparison tests sensitivity to training data curation"
      - "Consistent poor performance across runs strengthens findings"
    weaknesses:
      - "Limited systematic sensitivity analysis"
      - "Model architecture sensitivity not tested"
      - "Random seeds not documented"
    rationale: "Good robustness through two-run comparison but limited systematic sensitivity testing beyond the focal variable."

  generalisability:
    score: 65
    band: "good"
    strengths:
      - "Scope appropriately bounded (case study framing)"
      - "Limitations explicitly acknowledged"
      - "Comparative context provided"
    weaknesses:
      - "Single study area, model, and feature type"
      - "Counterintuitive curation finding may be context-specific"
    rationale: "Good generalisability through appropriate scope bounding and limitation acknowledgment. Inherent single-case design constraints limit score."

  cluster_synthesis:
    overall_rating: "strong"
    pattern_summary: "All signals in Good band (65-78) with validity and plausibility strongest. Pattern reflects well-executed empirical research with appropriate epistemic constraints."
    consistency_check: "consistent"
    implications:
      cluster_3: "Strong validity supports reproducibility assessment; asymmetric code/data profile primary consideration"
      final_report: "Good aggregate score indicates credible research with well-supported negative findings"
```
