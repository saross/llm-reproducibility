# Cluster 2: Evidential Strength Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-12-04
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** deductive (confidence: high)
**Paper Type:** empirical

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Plausibility | 75 | Good | deductive |
| Validity | 82 | Excellent | deductive |
| Robustness | 62 | Good | deductive |
| Generalisability | 80 | Excellent | deductive |

**Cluster Rating:** Strong

---

## Signal 3: Plausibility

**Score:** 75/100 (Good)

**Approach anchors applied:** deductive

### Assessment

The paper's hypothesis that curated training data would improve CNN performance is theoretically grounded in established ML principles. Transfer learning from ImageNet is a well-documented approach, and the intuition that cleaner training data (images where mounds are visible to humans) should improve model performance aligns with standard ML practice.

The counterintuitive finding - that curated data performed worse - is honestly reported rather than explained away. The authors offer plausible explanations grounded in domain knowledge: the curated dataset (249 visible mounds vs 773 total) may have created bias toward larger, more prominent mounds visible in imagery, while the landscape heterogeneity and mound variability may exceed what ImageNet pre-training can capture.

The findings are consistent with the broader ML literature showing that transfer learning works best when source and target domains are similar. Archaeological satellite imagery of burial mounds in heterogeneous Bulgarian landscapes differs substantially from ImageNet's photographic categories.

### Evidence

**Strengths:**
- C002: "The challenge centres around the variability of the appearance of the mounds themselves, combined with the heterogeneous landscape" - Explanation grounded in domain-specific knowledge
- E016: Reference to comparable studies in uniform environments (Egyptian sites) contextualises why transfer learning worked there but not here
- Anomalous result (curation made things worse) is acknowledged and explained rather than ignored

**Weaknesses:**
- IA003: Assumption that ImageNet pre-training transfers to satellite imagery of archaeological features is not fully theorised
- IA005: Assumption that F1 score is reliable proxy for real-world detection capability challenged by results but not fully resolved theoretically

### Scoring Rationale

Score: 75 (Good for deductive). Hypothesis theoretically motivated via standard ML principles (60-79). Findings generally consistent with domain knowledge about transfer learning limitations (60-79). Major anomaly (curated data worse) acknowledged and explained (60-79). Framework coherent. Some implicit assumptions about transfer domain similarity prevent excellent rating.

---

## Signal 4: Validity

**Score:** 82/100 (Excellent)

**Approach anchors applied:** deductive

### Assessment

This paper demonstrates excellent validity for its core hypothesis test. The evidence directly addresses the hypothesis through systematic comparison of two model configurations (2021 uncurated, 2022 curated) validated against independent field data from 773 ground-truthed mounds.

The sample is strong: 773 mounds documented via pedestrian survey over 85 sq km during 2009-2011 fieldwork, each with GPS coordinates, dimensions, land use, and preservation status. This provides a robust ground-truth dataset against which to validate model predictions.

Methods are appropriate for the research question. The quasi-experimental design (comparing uncurated baseline to curated intervention) tests the curation hypothesis. Field validation against independently collected ground truth (not just held-out model data) is the gold standard for ML evaluation in archaeological applications.

Alternative explanations are explicitly considered. The paper discusses why curation might have reduced performance (selection bias toward visible mounds, reduced dataset size). The paper also acknowledges that model architecture, hyperparameter tuning, or different augmentation strategies might produce different results.

### Evidence

**Strengths:**
- E004: "773 mounds collected by TRAP during 2009-2011 field survey... Each mound was recorded with GPS point, height, diameter, and surface and surrounding land use" - Comprehensive ground truth
- E010/E011: Complete validation metrics for both runs (true positives, false positives, false negatives) - Evidence directly addresses hypothesis
- RD003: Field validation design explicitly tests predictions against independent ground truth
- Alternative explanations for curation result considered (selection bias, dataset size)

**Weaknesses:**
- Single geographic study area (Kazanlak Valley) - though appropriate for hypothesis test
- No held-out test set separate from validation (though field validation compensates)

### Scoring Rationale

Score: 82 (Excellent for deductive). Evidence directly addresses hypothesis via systematic comparison (80-100). Sample of 773 ground-truthed mounds is adequate for hypothesis testing (80-100). Methods appropriate - field validation against independent ground truth (80-100). Alternative hypotheses explicitly considered (80-100). Confounds addressed through clear experimental design (80-100). Limitations prominently stated (80-100).

---

## Signal 5: Robustness

**Score:** 62/100 (Good)

**Approach anchors applied:** deductive

### Assessment

The paper demonstrates moderate-to-good robustness. The comparison of two model configurations (2021 uncurated, 2022 curated) constitutes a form of sensitivity analysis showing how results vary with training data selection. The consistent pattern of poor field validation across both runs (despite different training approaches and self-reported F1 scores) suggests the finding is robust to this analytical choice.

However, several robustness limitations exist. Only one model architecture (ResNet-50) was systematically evaluated, though brief mention is made of experiments with other architectures. Hyperparameters are not documented, so it's unclear whether results are sensitive to learning rate, epoch count, or batch size choices. The 60% probability threshold for detection is used throughout without sensitivity analysis testing other thresholds.

The paper uses a single dataset split approach without cross-validation or multiple random splits, so it's unclear whether results are sensitive to the specific train/validation division. Data augmentation is mentioned but not fully specified.

### Evidence

**Strengths:**
- E008/E011: Two model runs with different training data configurations show consistent pattern (both fail field validation despite different F1 scores) - Results robust to curation intervention
- E020: "ResNet-50 seemed to perform best for our data" - Suggests some architecture comparison occurred
- Consistent finding across runs: self-reported F1 scores don't predict field validation success

**Weaknesses:**
- P-IMP-002: Hyperparameters not documented - sensitivity to these choices unknown
- Single threshold (60%) used without threshold sensitivity analysis
- No cross-validation or multiple data splits documented
- Single study area - no geographic sensitivity analysis

### Scoring Rationale

Score: 62 (Good for deductive). Some sensitivity analysis via two training configurations (60-79). Results appear robust across this variation (60-79). Some alternatives tested (architecture experiments mentioned) (60-79). Assumptions stated but not fully tested (hyperparameters, threshold) (40-59 aspect). Dependencies partially documented (60-79). Would need hyperparameter sensitivity analysis, threshold variation, and cross-validation for excellent rating.

---

## Signal 7: Generalisability

**Score:** 80/100 (Excellent)

**Approach anchors applied:** deductive

### Assessment

The paper demonstrates excellent generalisability practice - not by claiming broad applicability, but by carefully constraining claims to the evidence and explicitly discussing transfer conditions.

Scope boundaries are clearly stated throughout. The authors explicitly limit their claims to "detecting varied features of different sizes within a heterogeneous landscape that contains confounding natural and modern features." They contrast their case (Bulgarian valley with mound variability, vegetation, roads, forests) with cases where ML has succeeded (uniform features in homogeneous landscapes like Egyptian deserts).

Limitations are prominently acknowledged. The paper explicitly states that results may not generalise to: (1) more homogeneous landscapes, (2) more uniform target features, (3) purpose-built models rather than transfer learning, (4) larger/better-curated training datasets.

Transfer conditions are specified. The authors suggest ML approaches may work better for "uniform features situated in environments with little variation in terrain or vegetation" - effectively specifying the conditions under which transfer to other contexts might succeed.

### Evidence

**Strengths:**
- C002: Claims explicitly bounded to "varied features of different sizes within a heterogeneous landscape"
- E016: Contrast with successful applications in uniform landscapes specifies transfer conditions
- Paper explicitly discusses what would need to change for different results (homogeneous landscape, uniform features, more data)
- IA001: "Single geographic context constraint" - implicit but reinforced throughout

**Weaknesses:**
- Single study area limits ability to test claimed constraints empirically
- No quantitative characterisation of landscape heterogeneity for transfer predictions

### Scoring Rationale

Score: 80 (Excellent for deductive). Scope of hypothesis clearly bounded (80-100). Limitations to external validity explicitly stated (80-100). Population, context, temporal bounds clear (80-100). Extrapolations qualified carefully (80-100). Threats to generalisation discussed prominently (80-100). Transfer conditions specified (what would need to differ) (80-100).

---

## Cluster Synthesis

**Overall Evidential Strength:** Strong

This paper demonstrates strong evidential strength overall. Three of four signals score in the Good-Excellent range (Plausibility 75, Validity 82, Generalisability 80), with only Robustness (62) in the moderate-Good range. The scores are consistent and reveal a coherent pattern.

### Pattern Summary

The paper's evidential strength lies in its core validity: the hypothesis test is well-designed with appropriate methods and adequate sample. The field validation against independent ground truth is the gold standard for ML evaluation. The paper's greatest strength is arguably its transparency about failure - the honest reporting of poor results enhances credibility.

The Robustness score (62) is the lowest, reflecting limited sensitivity analysis. However, the consistency of failure across two training configurations (both achieving misleading F1 scores but failing field validation) actually demonstrates robustness of the core finding - transfer learning CNN models produce misleading self-reported metrics.

The excellent Generalisability score (80) reflects the paper's careful constraint of claims rather than overreach. The authors specify exactly when their findings apply (heterogeneous landscapes, varied features) and when they may not (uniform landscapes, uniform features).

### Implications for Cluster 3

- **For Reproducibility:** The strong code availability (3 repositories) combined with weak data availability (no deposited data) creates an asymmetric reproducibility profile. Analytical reproducibility is partially supported; exact replication is not feasible. Environment documentation gaps (no software versions) will further limit reproducibility score.

---

## Structured Output

```yaml
cluster_2_evidential_strength:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-12-04"
  quality_state: "high"
  research_approach: "deductive"

  plausibility:
    score: 75
    band: "good"
    strengths:
      - "Hypothesis grounded in established ML principles (transfer learning, data quality)"
      - "Counterintuitive result (curated data worse) acknowledged and explained"
      - "Findings contextualised within broader ML literature on domain transfer"
    weaknesses:
      - "Transfer learning assumption (ImageNet→archaeology) not fully theorised"
    rationale: "Good for deductive research. Hypothesis theoretically motivated, anomalous results acknowledged and explained, framework coherent. Some implicit domain transfer assumptions."

  validity:
    score: 82
    band: "excellent"
    strengths:
      - "773 ground-truthed mounds provide comprehensive validation dataset"
      - "Field validation against independent ground truth (gold standard for ML)"
      - "Alternative explanations for curation result explicitly considered"
    weaknesses:
      - "Single geographic study area"
    rationale: "Excellent for deductive research. Evidence directly addresses hypothesis through systematic comparison validated against independent field data. Sample adequate, methods appropriate, alternatives considered, limitations stated."

  robustness:
    score: 62
    band: "good"
    strengths:
      - "Two model configurations show consistent pattern of field validation failure"
      - "Some architecture comparison mentioned"
      - "Core finding (misleading F1 scores) robust across training variations"
    weaknesses:
      - "Hyperparameters not documented"
      - "Single threshold (60%) without sensitivity analysis"
      - "No cross-validation documented"
    rationale: "Good for deductive research. Some sensitivity analysis via two configurations. Results robust across this variation. Missing hyperparameter sensitivity, threshold variation, and cross-validation for excellent rating."

  generalisability:
    score: 80
    band: "excellent"
    strengths:
      - "Claims explicitly bounded to heterogeneous landscape with varied features"
      - "Transfer conditions specified (uniform landscape, uniform features may differ)"
      - "Limitations prominently acknowledged throughout"
    weaknesses:
      - "Single study area limits empirical testing of claimed constraints"
    rationale: "Excellent for deductive research. Scope clearly bounded, limitations stated, extrapolations qualified, transfer conditions specified. Paper models appropriate constraint rather than overreach."

  cluster_synthesis:
    overall_rating: "strong"
    pattern_summary: "Strong evidential strength with excellent validity (82) and generalisability (80), good plausibility (75), and moderate-good robustness (62). Paper's credibility enhanced by transparent reporting of failure and careful constraint of claims."
    consistency_check: "consistent"
    implications:
      cluster_3: "Asymmetric reproducibility profile: strong code availability (3 repos) but weak data availability and environment documentation will limit score."
```
