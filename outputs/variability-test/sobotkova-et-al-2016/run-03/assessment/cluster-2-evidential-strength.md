# Cluster 2: Evidential Strength Assessment

**Paper:** sobotkova-et-al-2016
**Assessment Date:** 2025-12-04
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** inductive (confidence: high)
**Paper Type:** methodological (software_tool)

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Plausibility | 75 | Good | inductive/methodological |
| Validity | 62 | Good | inductive/methodological |
| Robustness | 48 | Moderate | 📦 software paper |
| Generalisability | 70 | Good | inductive/methodological |

**Cluster Rating:** Adequate

---

## Signal 3: Plausibility

**Score:** 75/100 (Good)

**Approach anchors applied:** inductive/methodological

### Assessment

The paper's claims are highly plausible and well-grounded in domain knowledge. The central thesis — that co-development partnerships with domain experts produce better field recording software than either off-the-shelf or custom-built approaches — aligns with established software engineering principles (user-centred design, iterative development) and archaeological computing literature (challenges of one-size-fits-all solutions).

The case studies demonstrate patterns consistent with known deployment realities: device limitations (GPS accuracy, battery life, screen visibility), user learning curves, data quality trade-offs (speed vs precision), and institutional constraints (training requirements, support needs). The three archaeological projects span different research types (excavation, survey, regional analysis) and geographic contexts (Turkey, Malawi, Peru), showing pattern consistency across varied settings.

The thematic observations are grounded in comparative evidence from multiple deployments. The "upfront costs vs backend payoffs" pattern is consistent with software adoption literature. The "importance of high-quality support" finding aligns with known technology adoption barriers. The "open-source sustainability model" addresses recognised challenges in research software maintenance.

No anomalies are ignored — the paper acknowledges limitations (single-context recording approach, GPS accuracy issues, learning curve challenges).

### Evidence

**Strengths:**

- C006: "The approach that best bridges the gap between off-the-shelf and bespoke software is a generalised approach" — Consistent with software engineering literature on platform-based development
- E007: Three case studies from different archaeological contexts (excavation, survey, regional) — Pattern consistency across varied research types
- RD003: Co-development model grounded in established participatory design practices

**Weaknesses:**

- No formal comparison to alternative approaches (other mobile platforms, traditional methods) — Plausibility relies on domain intuition rather than systematic evidence
- Limited engagement with contradicting examples (projects where FAIMS didn't work well)

### Scoring Rationale

Score of 75 (Good for inductive). Observed patterns consistent with known frameworks (60-79 criterion), case studies show pattern consistency across contexts (60-79), anomalies acknowledged (learning curves, device limitations). Not Excellent because no formal theoretical framework articulated (would need explicit grounding for 80-100) and limited engagement with potential counter-examples.

---

## Signal 4: Validity

**Score:** 62/100 (Good)

**Approach anchors applied:** inductive/methodological

### Assessment

Evidence for software capability claims is strong — the case studies demonstrate that FAIMS can be customised for different archaeological contexts (excavation, survey, artefact recording), deployed with varying institutional support, and adapted to different data collection requirements. The claimed features (offline capability, customisable data structure, photo/drawing capture, GIS integration) are evidenced through three successful deployments.

However, evidence for thematic synthesis claims is weaker. The three themes (upfront costs vs payoffs, support importance, sustainability) emerge from retrospective reflections by project directors, not systematic data collection. The methodology for synthesising themes from questionnaire and communication data is undocumented (M-IMP-001, M-IMP-002), making it difficult to evaluate whether the themes represent systematic patterns or selective interpretation.

The case study sample (n=3) is appropriate for demonstrating platform capabilities but limited for generalising about deployment patterns. Alternative interpretations are not systematically considered — the paper presents positive deployment experiences without exploring conditions under which FAIMS might fail or be inappropriate.

Scope of claims generally matches evidence — claims about FAIMS capabilities are supported by case evidence, while thematic claims are framed as "observations" rather than definitive conclusions.

### Evidence

**Strengths:**

- E001-E028: 28 evidence items documenting deployment experiences across three projects — Sufficient for demonstrating platform capabilities
- M001, M002: Data collection through questionnaire and communication logs — Systematic data collection for case studies
- Claims appropriately scoped as "observations" and "lessons learned" rather than universal principles

**Weaknesses:**

- M-IMP-001, M-IMP-002: Theme identification and quote selection methodology undocumented — Cannot evaluate derivation of thematic claims
- RD-IMP-001: Retrospective design — All evidence collected post-deployment through reflective accounts
- No systematic consideration of alternative interpretations or conditions for failure
- Case study sample (n=3) limited for pattern generalisation

### Scoring Rationale

Score of 62 (Good for inductive). Data sufficient for platform capability claims (60-79 criterion), sampling appropriate for demonstration purposes (60-79), claims generally scoped to evidence (60-79). Not Excellent because qualitative analysis methodology undocumented (would need transparent methodology for 80-100), limited alternatives considered (would need systematic alternative evaluation for 80-100), and some claims may exceed evidence (thematic generalisations from three cases).

---

## Signal 5: Robustness

**Score:** 48/100 (Moderate)

**Approach anchors applied:** 📦 software paper (descriptive/artefact paper context)

### Assessment

**📦 Context Flag Applied:** This is a software description paper, not a hypothesis-testing study. Software papers describe artefacts rather than test alternatives. A Moderate Robustness score (40-60) reflects genre expectations, not a deficiency.

The paper does not systematically test FAIMS against alternative approaches (other mobile platforms, paper-based recording, commercial solutions). This is appropriate for the paper type — the contribution is FAIMS itself, not a comparative evaluation. Readers should independently evaluate alternatives.

Within its genre constraints, the paper provides some robustness elements:

- **Multiple case studies:** Three deployments show consistency across different archaeological contexts, though this is convergent evidence rather than sensitivity analysis.
- **Honest limitation acknowledgement:** Paper acknowledges device limitations (GPS accuracy, battery), learning curves, and support requirements.
- **Trade-off documentation:** Cost-benefit analyses presented with actual figures (equipment costs, time savings).

The paper does not claim that FAIMS is superior to alternatives — it claims FAIMS is a viable approach for specific use cases. The absence of systematic comparison is not a validity threat for this claim scope.

### Evidence

**Strengths:**

- Three independent case studies provide convergent evidence of platform viability
- Honest documentation of limitations and trade-offs (C012: device challenges, C019: support requirements)
- Cost-benefit analysis with specific figures provides reproducible comparison basis

**Weaknesses:**

- No comparison to alternative mobile platforms (ODK, Fulcrum, etc.)
- No comparison to traditional paper-based methods with systematic metrics
- Single platform evaluated — results dependent on FAIMS-specific implementation choices
- No inter-observer reliability assessment for qualitative analysis

### Scoring Rationale

Score of 48 (Moderate for software paper — genre-appropriate). Paper demonstrates convergent evidence from multiple deployments (40-59 criterion), acknowledges limitations honestly (40-59). Score reflects genre expectations for software description papers, which describe artefacts rather than test alternatives. Not Low because paper provides honest trade-off documentation and multiple case studies; not Good/Excellent because no systematic comparison to alternatives (which would be a different paper type).

---

## Signal 7: Generalisability

**Score:** 70/100 (Good)

**Approach anchors applied:** inductive/methodological

### Assessment

The paper appropriately bounds its claims. FAIMS is explicitly positioned for "fieldwork-based research" with specific requirements (offline capability, customisable data structures, geographic data capture). The three case studies represent archaeological contexts — the paper does not claim generalisability to all field research without qualification.

Scope limitations are acknowledged:

- Archaeological focus: All case studies are archaeological projects
- Institutional context: Deployments involved partnership with FAIMS team (not fully independent adoption)
- Resource requirements: Training and support needs documented as constraints on broader adoption
- Technical constraints: Android-only platform noted as limitation

The open-source model is presented as transferable, but with explicit sustainability requirements (service-fee model, institutional support). The paper does not claim FAIMS is universally applicable — it positions FAIMS for specific use cases where customisation requirements exceed off-the-shelf capabilities but resources don't support fully bespoke development.

Transfer conditions are partially specified — the paper discusses what institutional and technical conditions support successful deployment, though this discussion is narrative rather than systematic.

### Evidence

**Strengths:**

- RD004: "FAIMS Mobile was developed specifically to accommodate the diverse and specialised data structures and workflows that characterise fieldwork-based research" — Clear bounded scope
- Limitations acknowledged: Android-only, support requirements, learning curves
- Case studies span different archaeological types (excavation, survey, regional) — Shows generalisability within archaeology

**Weaknesses:**

- All case studies archaeological — No evidence for broader field research applicability
- All deployments involved FAIMS team partnership — Independent adoption not demonstrated
- Transfer conditions narrative rather than systematic

### Scoring Rationale

Score of 70 (Good for inductive). Pattern claims bounded by geographic and disciplinary context (60-79 criterion), sampling limitations acknowledged (60-79), scope matched to evidence (60-79). Not Excellent because transfer conditions not systematically specified (would need explicit conditions for 80-100) and all case studies are FAIMS-partnered deployments (independent adoption would strengthen generalisability).

---

## Cluster Synthesis

**Overall Evidential Strength:** Adequate

The paper demonstrates adequate evidential strength overall, with a profile typical of methodological/software papers. Plausibility is strong (75) — claims align with domain knowledge and show consistent patterns across varied contexts. Generalisability is good (70) — claims are appropriately bounded and limitations acknowledged. Validity is adequate (62) — evidence supports platform capability claims, but qualitative methodology for thematic synthesis is undocumented. Robustness is moderate (48), which is genre-appropriate for a software description paper.

The signal pattern shows consistency: all scores cluster in the Moderate-Good range (48-75), with no major outliers. This reflects a paper that is solidly documented for its type but doesn't claim more than its evidence supports.

### Pattern Summary

Strong plausibility from domain consistency and pattern convergence across case studies. Good validity for platform capability claims but weaker for thematic synthesis claims due to undocumented qualitative methodology. Moderate robustness is genre-appropriate — software papers describe artefacts rather than test alternatives. Good generalisability through appropriate scope bounding and limitation acknowledgement.

**Key credibility strength:** Honest limitation acknowledgement and appropriate claim scoping.

**Key credibility gap:** Undocumented qualitative methodology for thematic synthesis (M-IMP-001, M-IMP-002).

### Implications for Cluster 3

- **For Reproducibility:** The software itself is highly reproducible (open source on GitHub). The case study deployment methodology could be replicated in new contexts. The qualitative analysis of case study data cannot be reproduced due to methodology gaps. Reproducibility assessment should focus on software reproducibility rather than case study analysis reproducibility.

---

## Structured Output

```yaml
cluster_2_evidential_strength:
  paper_slug: "sobotkova-et-al-2016"
  assessment_date: "2025-12-04"
  quality_state: "high"
  research_approach: "inductive"

  plausibility:
    score: 75
    band: "good"
    strengths:
      - "Claims consistent with established software engineering and archaeological computing literature"
      - "Pattern consistency across three varied archaeological contexts"
      - "Anomalies acknowledged (device limitations, learning curves)"
    weaknesses:
      - "No formal theoretical framework articulated"
      - "Limited engagement with potential counter-examples"
    rationale: "Good for inductive. Patterns consistent with domain knowledge, convergent evidence from multiple deployments. Not Excellent due to informal theoretical grounding."

  validity:
    score: 62
    band: "good"
    strengths:
      - "28 evidence items documenting deployment experiences"
      - "Claims appropriately scoped as observations rather than universal principles"
      - "Systematic data collection through questionnaire and communication logs"
    weaknesses:
      - "Theme identification methodology undocumented (M-IMP-001)"
      - "Retrospective design limits causal inference"
      - "Limited consideration of alternative interpretations"
    rationale: "Good for inductive. Evidence sufficient for platform capability claims. Not Excellent due to undocumented qualitative methodology and limited alternatives considered."

  robustness:
    score: 48
    band: "moderate"
    context_flag: "software_paper"
    strengths:
      - "Convergent evidence from three independent deployments"
      - "Honest limitation and trade-off documentation"
      - "Cost-benefit analysis with specific figures"
    weaknesses:
      - "No comparison to alternative platforms"
      - "No systematic comparison to traditional methods"
      - "Results dependent on FAIMS-specific implementation"
    rationale: "Moderate for software paper (genre-appropriate). Software papers describe artefacts rather than test alternatives. Score reflects honest limitation acknowledgement and convergent case study evidence."

  generalisability:
    score: 70
    band: "good"
    strengths:
      - "Claims bounded by archaeological focus and institutional context"
      - "Limitations explicitly acknowledged (Android-only, support requirements)"
      - "Case studies span different archaeological research types"
    weaknesses:
      - "All case studies archaeological — no cross-disciplinary evidence"
      - "All deployments FAIMS-partnered — independent adoption not demonstrated"
    rationale: "Good for inductive. Claims appropriately bounded, limitations acknowledged, scope matched to evidence. Not Excellent because transfer conditions narrative rather than systematic."

  cluster_synthesis:
    overall_rating: "adequate"
    pattern_summary: "Consistent Moderate-Good scores (48-75) appropriate for methodological/software paper. Strong plausibility, good generalisability, adequate validity, genre-appropriate moderate robustness."
    consistency_check: "consistent"
    implications:
      cluster_3: "Software highly reproducible (GitHub, open source). Case study methodology not reproducible. Focus reproducibility assessment on software."
```
