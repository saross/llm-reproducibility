# Cluster 2: Evidential Strength Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-11-30
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** Deductive (confidence: high)
**Paper Type:** Empirical

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Plausibility | 75 | Good | Deductive |
| Validity | 80 | Excellent | Deductive |
| Robustness | 68 | Good | Deductive |
| Generalisability | 78 | Good | Deductive |

**Cluster Rating:** Strong

---

## Signal 3: Plausibility

**Score:** 75/100 (Good)

**Approach anchors applied:** Deductive

### Assessment

The paper demonstrates good theoretical grounding for its hypothesis testing. The research tests a well-established claim in the ML literature: that transfer learning with pre-trained CNNs can effectively detect archaeological features with minimal additional training. This hypothesis has theoretical basis in published ML archaeology literature, which the authors review extensively.

The paper is particularly strong in handling anomalous results. When the CNN failed to perform as expected, the authors provided coherent explanations grounded in ML theory: detection of incidental background features rather than target features, tile boundary effects, and the challenge of varied feature sizes in heterogeneous landscapes. These explanations are consistent with known ML failure modes.

The theoretical framework is coherent: the paper tests whether transfer learning promises hold in a challenging but representative archaeological context. The authors do not require implausible auxiliary assumptions — they test a mainstream claim with appropriate methods and honestly report failure.

### Evidence

**Strengths:**
- C017: "Transfer learning is promoted as a solution to limited training data problems" — tests an established theoretical claim
- IA002: Recognition that human visual interpretation skills don't straightforwardly transfer to CNN capabilities — acknowledges theoretical limitation
- Discussion section provides mechanistic explanation for failure grounded in ML theory (background feature detection, tile boundaries)

**Weaknesses:**
- The implicit hypothesis (transfer learning will work) could have been stated more explicitly as a formal theoretical prediction

### Scoring Rationale

Score of 75 (Good for deductive) reflects: hypotheses theoretically motivated in ML literature (60-79); consistent with domain knowledge about both archaeology and ML (60-79); anomalous results (model failure) thoroughly addressed (60-79). Score is Good rather than Excellent because hypotheses are implied rather than formally derived from theory.

---

## Signal 4: Validity

**Score:** 80/100 (Excellent)

**Approach anchors applied:** Deductive

### Assessment

This paper demonstrates excellent validity through rigorous external validation. The core methodological contribution is comparing self-reported ML metrics (F1 scores) to performance validated against independent field data. This external validation with 773 field-verified mounds provides robust evidence that directly addresses the research question: "Does this CNN approach work for burial mound detection?"

Evidence sufficiency is strong. The validation dataset (773 mounds from systematic pedestrian survey) provides adequate coverage of the study area. The comparison is comprehensive: false positive rates, false negative rates, and true positive rates are all reported. The evidence directly addresses whether the model works, not just whether internal metrics look good.

The two-run experimental design tests an alternative hypothesis: whether curated training data (visible mounds only) would improve performance. Finding that it actually worsened performance addresses a plausible alternative explanation. Methods are clearly appropriate for the research question — comparing predictions to ground truth is the gold standard for validation.

### Evidence

**Strengths:**
- E013: "Survey registered 773 burial mounds – whose presence was confirmed by personal inspection" — robust validation dataset
- M004: Validation method explicitly compares predictions to field-verified locations — appropriate for hypothesis testing
- RD003: Two-run design tests alternative (curated training data) — addresses plausible alternative hypothesis
- Extensive limitation acknowledgement in Discussion

**Weaknesses:**
- Single study area (Kazanlak Valley) — though acknowledged as limitation
- No comparison to other detection methods (crowdsourcing, expert manual inspection) — alternative approaches mentioned but not directly tested

### Scoring Rationale

Score of 80 (Excellent for deductive) reflects: evidence directly addresses hypothesis through external validation (80-100); sample adequate with 773 field-verified mounds (80-100); methods appropriate (80-100); alternative hypothesis tested through two-run design (80-100); limitations explicitly stated (80-100). Excellent threshold met through rigorous external validation.

---

## Signal 5: Robustness

**Score:** 68/100 (Good)

**Approach anchors applied:** Deductive

### Assessment

The paper demonstrates good robustness for deductive research. The two-run experimental design provides meaningful sensitivity analysis by testing whether training data selection strategy affects model performance. Finding consistent poor performance across both approaches (all mounds: 4.9% detection; visible mounds only: 2.7% detection) strengthens the conclusion that the approach is fundamentally limited, not dependent on a single analytical choice.

However, robustness testing is limited in scope. Only a single probability threshold (60%) is reported in detail. The paper mentions that different thresholds were explored but does not systematically report sensitivity to threshold selection. Similarly, tile size (150×150 pixels) is fixed without testing alternatives.

The two-run design represents good practice but could be strengthened by additional sensitivity analyses: threshold sensitivity, tile size effects, or comparison across different imagery subsets. The consistent failure across both runs does provide confidence that results are not artefactual.

### Evidence

**Strengths:**
- RD003: Two-run design with different training data selection — provides robustness evidence
- Results consistent across both analytical approaches (poor performance in both) — strengthens conclusions
- E008 and E009: Both runs show similar failure pattern — convergent evidence

**Weaknesses:**
- P002: Only 60% threshold reported in detail — limited threshold sensitivity analysis
- No tile size sensitivity testing (150×150 fixed)
- No cross-validation or hold-out testing described

### Scoring Rationale

Score of 68 (Good for deductive) reflects: some sensitivity analysis through two-run design (60-79); results appear robust across training strategies (60-79); dependencies documented (60-79). Score is Good rather than Excellent because threshold and tile size sensitivity analyses are limited; would need more comprehensive robustness testing for 80+ score.

---

## Signal 6: Generalisability

**Score:** 78/100 (Good)

**Approach anchors applied:** Deductive

### Assessment

The paper demonstrates strong scope constraint and limitation acknowledgement. Claims are carefully bounded to the specific context: pre-trained CNN with low-touch training, IKONOS satellite imagery, burial mounds in the Kazanlak Valley's heterogeneous landscape. The authors explicitly avoid overgeneralising, presenting results as a "cautionary tale" for similar projects rather than universal conclusions.

Limitations are extensively discussed. The paper acknowledges that results might differ with: different training approaches (more curation, larger datasets), different imagery (resolution, spectral bands), different feature types (more uniform features), or different landscapes (more homogeneous backgrounds). Transfer conditions are clearly specified: the limitations apply particularly to "varied features of different sizes within a heterogeneous landscape."

The scope of claims is well-matched to evidence. Core claims (model failure, metric/performance mismatch) are supported by evidence from this specific context. Broader claims (ML literature positivity bias, manual alternatives may be more efficient) are appropriately qualified.

### Evidence

**Strengths:**
- C003: "limitations of this approach when it is used to detect varied features of different sizes within a heterogeneous landscape" — explicit scope constraints
- C018: Lists specific improvements required, implicitly bounding current claims
- RD004: Case study design explicitly positioned as representative but bounded
- Discussion section extensively addresses limitations and transfer conditions

**Weaknesses:**
- Single study area limits empirical generalisation (acknowledged by authors)
- No comparative data from other regions to test scope boundaries

### Scoring Rationale

Score of 78 (Good for deductive) reflects: hypothesis scope clearly bounded (60-79 to 80-100 threshold); limitations to external validity comprehensively stated (80-100); extrapolations carefully qualified (80-100); transfer conditions specified (80-100). Score is Good-to-Excellent because scope constraint and limitation acknowledgement are strong; single study area prevents Excellent rating.

---

## Cluster Synthesis

**Overall Evidential Strength:** Strong

### Pattern Summary

This paper demonstrates consistently strong evidential strength across all four signals, with scores ranging from 68-80 (Good to Excellent). The strongest aspect is Validity (80) — the external validation against field data is the paper's key methodological contribution and is well-executed. Plausibility (75) and Generalisability (78) are both Good, reflecting solid theoretical grounding and appropriate scope constraint. Robustness (68) is the weakest signal but still Good, limited primarily by the scope of sensitivity analyses rather than fundamental concerns.

### Score Consistency

Scores are highly consistent across signals, reflecting a well-designed study. The paper achieves strong credibility through rigorous external validation, honest reporting of failure, and careful scope constraint. No signal falls below 65, indicating balanced evidential strength without major gaps.

### Implications for Cluster 3

- **Reproducibility expectations:** Strong Transparency (from Cluster 1) and Validity suggest the computational workflow should be reproducible. The three GitHub repositories provide code infrastructure.
- **Data access:** Main limitation will be satellite imagery (commercial) and field data (reference-only). Computational reproducibility is likely strong; full analytical reproducibility may be limited by data access.

---

## Structured Output

```yaml
cluster_2_evidential_strength:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-11-30"
  quality_state: "high"
  research_approach: "deductive"

  plausibility:
    score: 75
    band: "good"
    strengths:
      - "Hypothesis grounded in established ML transfer learning literature"
      - "Anomalous results (model failure) thoroughly explained with mechanistic reasoning"
      - "Theoretical framework coherent"
    weaknesses:
      - "Implicit rather than formally stated hypothesis"
    rationale: "Good for deductive. Hypotheses theoretically motivated, anomalies thoroughly addressed, framework coherent. Good rather than Excellent because hypothesis is implied not formally derived."

  validity:
    score: 80
    band: "excellent"
    strengths:
      - "External validation against 773 field-verified mounds"
      - "Two-run design tests alternative hypothesis"
      - "Methods directly appropriate for research question"
      - "Comprehensive limitation acknowledgement"
    weaknesses:
      - "Single study area"
      - "No direct comparison to alternative methods"
    rationale: "Excellent for deductive. Evidence directly addresses hypothesis through rigorous external validation. Sample adequate, methods appropriate, alternative tested, limitations stated."

  robustness:
    score: 68
    band: "good"
    strengths:
      - "Two-run experimental design provides sensitivity analysis"
      - "Consistent failure across both approaches strengthens conclusions"
    weaknesses:
      - "Limited threshold sensitivity analysis (only 60% reported in detail)"
      - "No tile size sensitivity testing"
    rationale: "Good for deductive. Some sensitivity analysis through two-run design, results appear robust. Limited by scope of sensitivity analyses."

  generalisability:
    score: 78
    band: "good"
    strengths:
      - "Claims carefully bounded to specific context"
      - "Extensive limitation discussion"
      - "Transfer conditions clearly specified"
    weaknesses:
      - "Single study area limits empirical generalisation"
    rationale: "Good for deductive. Scope clearly bounded, limitations comprehensively stated, extrapolations qualified. Single study area prevents Excellent rating."

  cluster_synthesis:
    overall_rating: "strong"
    pattern_summary: "Consistently strong evidential strength across all signals (68-80). External validation is key strength. Robustness limited by sensitivity analysis scope."
    consistency_check: "consistent"
    implications:
      cluster_3: "Strong code availability suggests good computational reproducibility; data access may limit full analytical reproducibility"
```
