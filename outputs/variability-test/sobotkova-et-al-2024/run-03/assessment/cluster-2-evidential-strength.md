# Cluster 2: Evidential Strength Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-12-05
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** deductive (confidence: high)
**Paper Type:** empirical

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Plausibility | 85 | Excellent | deductive |
| Validity | 82 | Excellent | deductive |
| Robustness | 75 | Good | deductive |
| Generalisability | 68 | Adequate | deductive |

**Cluster Rating:** Strong

---

## Signal 3: Plausibility

**Score:** 85/100 (Excellent)

**Approach anchors applied:** deductive

### Assessment

This paper demonstrates excellent plausibility for deductive hypothesis-testing research. The central question — whether low-touch transfer learning with pre-trained CNNs can effectively detect burial mounds in satellite imagery — is grounded in established machine learning theory and addresses a practical problem in archaeological heritage management.

The theoretical framework integrates transfer learning principles (leveraging ImageNet pre-training) with archaeological prospection needs. The expectation that transfer learning might work is reasonable given successes in related domains, making the negative results genuinely informative rather than trivially predictable. The paper explicitly situates itself against a growing literature showing ML successes (21 papers in 2023, up from zero in 2014), establishing why testing this approach was warranted.

Domain knowledge is appropriately integrated: the authors draw on extensive fieldwork experience (2,000+ mounds surveyed across two Bulgarian provinces) and cite comparative examples (Can et al. 2021 spending 1,250 hours on training data). The "cautionary tale" framing is epistemically appropriate — testing a plausible hypothesis that turns out to be unsupported.

### Evidence

**Strengths:**
- E07, E36: Literature review establishes ML is becoming popular (21 publications in 2023, 17% of archaeological remote sensing)
- RD03: Transfer learning rationale explicitly stated — "potentially obviates the need to have large, high-quality, and representative datasets"
- C31-C32: Background claims establish why testing transfer learning was reasonable
- E06: Authors' domain expertise (2,000+ mounds surveyed) grounds their interpretation

**Weaknesses:**
- Some ML theoretical background (overfitting, feature detection) assumed rather than explicitly developed

### Scoring Rationale

Score: 85 (Excellent for deductive). Hypothesis grounded in established ML theory and addressed genuine uncertainty about transfer learning applicability (80-100 criterion: "Core questions/hypotheses well-grounded in existing knowledge"). Domain knowledge appropriately integrated through extensive fieldwork experience. Theoretical framework connects ML capabilities to archaeological feature characteristics (variable visibility, heterogeneous landscapes). Literature review establishes why the question was worth testing. Minor limitation: ML theoretical background somewhat assumed.

---

## Signal 4: Validity

**Score:** 82/100 (Excellent)

**Approach anchors applied:** deductive

### Assessment

Evidence adequacy for testing the hypothesis is excellent. The 773 ground-truthed burial mounds from TRAP pedestrian survey constitute a robust validation dataset — independently collected field data providing external benchmark against which ML predictions could be tested. This is the gold standard for evaluating feature detection claims.

The two-run comparative design (Run 1: all 773 mounds; Run 2: 249 highly visible mounds) provides internal comparison testing the hypothesis that training data curation affects detection. Both runs were validated against the same independent field data, with comprehensive metrics calculated (F1 scores, false positive/negative rates, true positive rates).

Evidence quality is high: 45 evidence items include precise quantitative measurements (95-96% false negative rates, 87-95% false positive rates, 5-13% true positives). Evidence-claim relationships are direct — E01 directly supports C01-C03 through validated detection metrics. The gap between self-reported F1 (0.87) and actual field-validated detection (4.9% of mounds) demonstrates why external validation is essential.

### Evidence

**Strengths:**
- E10-E12: 773 mounds from 85 sq km pedestrian survey provides robust ground truth
- E22-E31: Comprehensive validation metrics from both model runs with exact counts
- P05: Field Data Validation Protocol explicitly documented with 60% probability threshold
- M05-M06: Methods for field validation and pedestrian survey fully specified

**Weaknesses:**
- Validation limited to TRAP study area (85 sq km within 600 sq km imagery)
- No independent validation of the ground truth itself (though excavation confirmed some mounds — E45)

### Scoring Rationale

Score: 82 (Excellent for deductive). Evidence directly addresses hypothesis with appropriate data (80-100 criterion: "Appropriate evidence directly tests/addresses hypothesis"). 773 ground-truthed mounds provide independent external validation — the critical test for feature detection claims. Both quantitative (detection rates, F1 scores) and qualitative (visual inspection of model behaviour) evidence support conclusions. Evidence-claim relationships are direct and traceable. Minor limitation: validation constrained to TRAP study area.

---

## Signal 5: Robustness

**Score:** 75/100 (Good)

**Approach anchors applied:** deductive

### Assessment

Robustness is good for deductive hypothesis-testing research. The two-run comparative design provides sensitivity analysis on training data curation — testing whether filtering for highly visible mounds improves detection. The counterintuitive finding (curated Run 2 performed worse: F1 dropped from 0.87 to 0.62) suggests the negative result is robust across training data configurations.

Methodological transparency supports robustness assessment: model architecture (ResNet-50, 25.6m parameters), data split (70:20:10), probability threshold (60%), and validation procedures are fully specified. This allows evaluation of analytical choices.

However, formal robustness testing is limited. No multi-threshold sensitivity analysis (only 60% probability reported), no cross-validation across different image regions, and no testing with alternative model architectures beyond initial "preliminary experimentation". The paper acknowledges this limitation implicitly — more sophisticated approaches would require additional resources.

### Evidence

**Strengths:**
- RD01: Comparative two-run design tests sensitivity to training data curation
- E19: Different training sizes (773 vs 249 mounds) both yielded poor results
- P03: Model parameters fully specified (ResNet-50, TensorFlow 2, augmentation procedures)
- C16, C19: Counterintuitive finding (curated data performed worse) suggests robustness

**Weaknesses:**
- Single probability threshold (60%) without sensitivity analysis
- No systematic exploration of alternative model architectures
- No cross-validation across different image regions or mound subtypes

### Scoring Rationale

Score: 75 (Good for deductive). Two-run comparison constitutes meaningful sensitivity analysis on training data (60-79 criterion: "Sensitivity analysis on key parameters"). Both configurations yielded consistent negative results. Methodological choices well-documented enabling robustness evaluation. Falls short of Excellent because no multi-threshold analysis, no alternative architecture testing, and no formal uncertainty quantification. Core finding (95-96% false negative rates) consistent across runs suggests conclusion is robust to tested variations.

---

## Signal 6: Generalisability

**Score:** 68/100 (Adequate)

**Approach anchors applied:** deductive

### Assessment

Generalisability is appropriately constrained for deductive hypothesis-testing research. The paper explicitly limits claims to the tested context: Bulgarian burial mounds in IKONOS imagery using transfer learning with ResNet-50 and minimal training data curation.

The domain constraints are transparently documented: heterogeneous landscapes with variable feature visibility, mounds ranging 10-100m diameter and <1-20m height, Mediterranean agricultural context with diverse land cover. These specific conditions may not generalise to contexts with more uniform features or homogeneous landscapes.

The paper appropriately avoids overgeneralisation, instead offering methodological insights: the importance of external validation, publication bias concerns, and cost-benefit considerations. Claims about ML limitations are carefully bounded to "low-touch approaches" rather than ML in general.

The bibliometric review provides some external triangulation (63% of ML archaeology papers lack negative commentary), but direct replication in other contexts is not attempted.

### Evidence

**Strengths:**
- C03: Limitation explicitly bounded to "inconsistent and sometimes indistinct features in a varied landscape"
- C06: Domain constraints documented (visibility depends on size, terrain, land cover)
- E08-E09: Literature review provides context for broader applicability of findings
- RD04: Cost-benefit framework has potential transferability to other projects

**Weaknesses:**
- Single geographic context (Kazanlak Valley, Bulgaria)
- Single imagery type (IKONOS multispectral)
- Single model architecture tested systematically (ResNet-50)
- No direct replication attempted

### Scoring Rationale

Score: 68 (Adequate for deductive). Scope limitations clearly stated (meets 40-59 threshold minimum). Domain characteristics documented. Claims appropriately bounded to tested context. Elevated to Adequate (60-79) because methodological insights (validation importance, publication bias, cost-benefit) have broader applicability even if empirical results are context-specific. Falls short of Good because single geographic context, no replication, and findings may not generalise to contexts with more uniform features.

---

## Cluster Synthesis

**Overall Evidential Strength:** Strong

This paper demonstrates strong evidential strength for deductive hypothesis-testing research. The signature strength is the 773-mound ground truth dataset providing robust external validation — the critical test for feature detection claims. The gap between self-reported metrics (F1 = 0.87) and field-validated performance (4.9% detection rate) exemplifies why external validation is essential.

The two-run comparative design provides meaningful robustness testing, showing that the negative result is consistent across different training data configurations. Both Plausibility (85) and Validity (82) score in the Excellent range, with Robustness (75) in Good range and Generalisability (68) appropriately constrained.

### Pattern Summary

Evidential strength follows a pattern typical of well-conducted hypothesis-testing research: strong foundation in established theory, appropriate evidence for testing the hypothesis, meaningful sensitivity analysis, and appropriately bounded generalisation claims. The explicit negative result format ("cautionary tale") is itself an evidential strength — the paper tests a hypothesis, finds it unsupported, and transparently reports this.

### Consistency Check

Scores are internally consistent:
- Plausibility (85) and Validity (82) both Excellent: well-grounded hypothesis tested with appropriate evidence
- Robustness (75) Good: comparative design provides sensitivity analysis but limited to tested parameters
- Generalisability (68) Adequate: appropriately bounded to tested context

No anomalous patterns. The 17-point gap between Validity (82) and Generalisability (68) reflects the paper's strength in testing its specific hypothesis versus the inherent limitations of single-context research.

---

## Structured Output

```yaml
cluster_2_evidential_strength:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-12-05"
  quality_state: "high"
  research_approach: "deductive"

  plausibility:
    score: 85
    band: "excellent"
    strengths:
      - "Hypothesis grounded in established ML theory (transfer learning) and addresses genuine uncertainty"
      - "Literature review establishes why testing this approach was warranted (21 papers in 2023)"
      - "Domain expertise (2,000+ mounds surveyed) grounds interpretation"
    weaknesses:
      - "Some ML theoretical background assumed rather than explicitly developed"
    rationale: "Well-grounded hypothesis testing a plausible proposition about transfer learning applicability. The negative result is genuinely informative rather than trivially predictable."

  validity:
    score: 82
    band: "excellent"
    strengths:
      - "773 ground-truthed mounds from pedestrian survey provides robust external validation"
      - "Two-run comparative design with comprehensive validation metrics"
      - "Evidence-claim relationships direct and traceable (45 evidence items)"
      - "Gap between F1 (0.87) and field-validated detection (4.9%) demonstrates validation importance"
    weaknesses:
      - "Validation limited to 85 sq km TRAP study area"
      - "No independent validation of ground truth itself"
    rationale: "Excellent evidence adequacy — independent field data provides gold standard benchmark for testing feature detection claims."

  robustness:
    score: 75
    band: "good"
    strengths:
      - "Two-run comparison tests sensitivity to training data curation"
      - "Consistent negative results across both configurations"
      - "Full methodological specification enables robustness evaluation"
    weaknesses:
      - "Single probability threshold (60%) without sensitivity analysis"
      - "No alternative architecture testing"
      - "No cross-validation across image regions"
    rationale: "Good robustness through comparative design. Falls short of Excellent due to limited formal sensitivity analysis beyond training data comparison."

  generalisability:
    score: 68
    band: "adequate"
    strengths:
      - "Scope limitations explicitly stated and bounded"
      - "Domain constraints documented (feature variability, landscape heterogeneity)"
      - "Methodological insights (validation importance, publication bias) have broader applicability"
    weaknesses:
      - "Single geographic context (Bulgaria)"
      - "Single imagery type and model architecture"
      - "No direct replication attempted"
    rationale: "Appropriately constrained generalisability for context-specific hypothesis test. Methodological insights transfer even if empirical results are context-bound."

  cluster_synthesis:
    overall_rating: "strong"
    pattern_summary: "Well-conducted hypothesis-testing with excellent evidence adequacy (773-mound ground truth), good robustness (comparative two-run design), and appropriately bounded generalisation. Signature strength: external validation demonstrating gap between self-reported and actual performance."
    consistency_check: "consistent"
    evidence_claim_alignment: "strong"
```
