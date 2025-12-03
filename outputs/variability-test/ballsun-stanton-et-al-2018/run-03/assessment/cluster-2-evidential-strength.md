# Cluster 2: Evidential Strength Assessment

**Paper:** ballsun-stanton-et-al-2018
**Assessment Date:** 2025-12-02
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** inductive (confidence: high)
**Paper Type:** methodological (software_tool)

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Plausibility | 80 | Excellent | inductive |
| Validity | 75 | Good | inductive |
| Robustness | 55 | Moderate | inductive (📦 software paper context) |
| Generalisability | 70 | Good | inductive |

**Cluster Rating:** Adequate-to-Strong

---

## Signal 3: Plausibility

**Score:** 80/100 (Excellent)

**Approach anchors applied:** inductive

### Assessment

FAIMS Mobile claims are highly plausible given established knowledge about field research software, mobile technology, and archaeological data collection. The paper's claims about software capabilities align with known technical possibilities of Android development (offline storage, sync, GIS). Claims about deployment outcomes (40 customisations, 29 deployments, 300 users) are consistent with expectations for specialised research software over 5 years.

The theoretical grounding is sound: the paper explicitly positions FAIMS within existing landscape (ARK, Heurist, Kora) and identifies the gap it addresses (generalised offline-capable field data collection). Interpretations of user feedback align with established knowledge about field research challenges - "minimizing errors, enhancing data quality, and streamlining traditionally labor-intensive data collection processes" (C012) reflects documented field research pain points.

No anomalies are ignored. The paper honestly acknowledges tradeoffs: "the system now supports many use cases it was never designed for, so some refactoring to improve future customisation and modernisation would benefit the module creation process" (IA002). This transparency about technical debt enhances plausibility.

### Evidence

**Strengths:**

- C001: "FAIMS Mobile is mature, production-ready software" - Plausible given 5 years development (v2.5) and documented deployments
- E010: "40 custom modules representing 29 distinct research deployments" - Concrete metrics consistent with specialised research software adoption curves
- IA002: Honest acknowledgment of technical debt enhances overall plausibility of claims

**Weaknesses:**

- Case study details rely on external publication (Sobotkova et al., 2016) - plausibility assessable but less directly

### Scoring Rationale

Score of 80 (Excellent for inductive). Observed patterns consistent with known frameworks for research software development (80-100 criterion). Claims well-contextualised within existing software landscape (80-100). Anomalies/tradeoffs acknowledged and contextualised (80-100). Interpretations grounded in comparative understanding of field research challenges.

---

## Signal 4: Validity

**Score:** 75/100 (Good)

**Approach anchors applied:** inductive

### Assessment

Evidence is sufficient for the claims made. Software capability claims are supported by technical specification (architecture, code availability, documentation). Deployment claims supported by concrete metrics: "40 unique customized modules," "29 distinct research deployments," "approximately 300 archaeologists plus researchers in ecology, geoscience, and oral history" (E007). User feedback claims supported by reference to published case studies (E005).

Sampling is systematic within the deployment population - the paper reports on all documented FAIMS deployments rather than cherry-picking successes. Coverage is appropriate for pattern claims about software capabilities and user satisfaction.

Some limitations: detailed case study evidence relies on external publication, and user feedback is qualitative rather than systematically measured. The paper claims efficiency improvements but precise quantification is in external sources. However, for a software paper in SoftwareX, the evidence base is appropriate and sufficient.

### Evidence

**Strengths:**

- E007: "FAIMS has been used to collect data in Australia and around the world by approximately 300 archaeologists plus researchers in ecology, geoscience, and oral history" - Specific, verifiable deployment metrics
- E010: "40 custom modules representing 29 distinct research deployments" - Complete deployment census, not selective sampling
- E015-E020: Technical evidence (SQLite, GIS, offline sync) supports capability claims directly

**Weaknesses:**

- E005: Case study evidence relies on external publication - sufficient for claims but not fully self-contained
- User satisfaction claims based on qualitative feedback, not systematic measurement

### Scoring Rationale

Score of 75 (Good for inductive). Data sufficient for main patterns (60-79 criterion): deployment metrics comprehensive, capability claims technically documented. Sampling systematic (60-79): all deployments reported. Claims generally scoped to evidence (60-79). Deduction for reliance on external publication for detailed case study evidence.

---

## Signal 5: Robustness

**Score:** 55/100 (Moderate)

**Approach anchors applied:** inductive

### 📦 Software Paper Context

This is a software paper describing an artefact. Software papers describe what tools do, not systematically test alternatives. A Moderate Robustness score (40-60) reflects **genre expectations**, not a deficiency. Comparative evaluation against alternative tools is a different paper type.

### Assessment

As a software description, FAIMS paper demonstrates moderate robustness appropriate for its genre. The paper documents multiple independent deployments (29) across disciplines (archaeology, ecology, geoscience, oral history) showing software performs consistently across contexts. Multiple evidence types support claims: technical specifications, deployment metrics, and user feedback triangulate around software capabilities.

The paper does not perform formal comparative testing against alternatives (ARK, Heurist, Kora, ODK) - this would be a different paper type. However, it positions FAIMS honestly within the software landscape and identifies its distinctive capabilities (offline-first, deeply customisable, generalised).

Some triangulation is present: user feedback from case studies aligns with deployment metrics; technical architecture documentation aligns with claimed capabilities. The paper honestly documents limitations and technical debt (IA002).

### Evidence

**Strengths:**

- E010: Multiple independent deployments (29) across diverse contexts suggest consistent performance
- E007: Cross-disciplinary adoption (archaeology, ecology, geoscience, oral history) shows pattern robustness
- Triangulation: technical specs + deployment metrics + user feedback converge

**Weaknesses:**

- No formal comparative testing against alternatives (appropriate for genre but limits robustness)
- Single development team perspective - no independent evaluation

### Scoring Rationale

Score of 55 (Moderate for inductive, 📦 software paper context). Limited triangulation present (40-59 criterion): multiple evidence types but no independent evaluation. Pattern robustness supported by cross-disciplinary deployment (40-59). Appropriate for software paper genre - readers should independently evaluate alternatives.

---

## Signal 7: Generalisability

**Score:** 70/100 (Good)

**Approach anchors applied:** inductive

### Assessment

The paper demonstrates good generalisability with appropriate scope boundaries. Claims are explicitly bounded by software version (2.5), development era (2012-2017), and deployment context (field research). The paper does not overclaim - it presents FAIMS as a solution for "human-mediated field research" rather than all research contexts.

Scope is explicitly matched to evidence. Claims about cross-disciplinary applicability are supported by documented deployments in archaeology, ecology, geoscience, and oral history. Geographic scope (Australia and internationally) matches deployment evidence.

Limitations are acknowledged: technical debt needs addressing (IA002), some features need modernisation, and the paper notes "some refactoring to improve future customisation." The paper appropriately constrains claims to demonstrated capabilities rather than hypothetical future possibilities.

Transfer conditions are implicit but clear: the software requires Android devices, Ubuntu server, and substantial customisation effort. The paper honestly notes complexity: "moderate-complexity systems with arbitrarily customized data entry" require 1-2 developer-days.

### Evidence

**Strengths:**

- C007: Claims bounded to "human-mediated field research" - appropriate scope
- E007: Cross-disciplinary and international deployment supports generalisability claims
- IA002: Limitations honestly acknowledged (technical debt, modernisation needs)

**Weaknesses:**

- Transfer conditions (technical requirements, customisation effort) implicit rather than explicitly specified as constraints

### Scoring Rationale

Score of 70 (Good for inductive). Pattern claims bounded to demonstrated contexts (60-79 criterion). Scope generally matched to coverage (60-79): claims about cross-disciplinary use supported by evidence. Limitations present and acknowledged (60-79). Minor deduction for implicit rather than explicit transfer conditions.

---

## Cluster Synthesis

**Overall Evidential Strength:** Adequate-to-Strong

The FAIMS paper demonstrates strong credibility for a software publication. Plausibility (80) and Validity (75) are high, reflecting well-grounded claims with sufficient evidence. Robustness (55) is moderate, appropriate for a descriptive software paper genre where comparative evaluation is not expected. Generalisability (70) is good, with claims appropriately bounded to demonstrated deployments.

### Pattern Summary

Signals show expected pattern for software publication: stronger on theoretical grounding (Plausibility) and evidence sufficiency (Validity), moderate on robustness testing (expected for genre), and good on scope constraints (Generalisability). This profile reflects a well-executed software paper rather than empirical research.

The paper's key credibility strength is honest acknowledgment of limitations - technical debt, modernisation needs, and tradeoffs are explicitly discussed rather than hidden. This transparency enhances overall credibility.

### Implications for Cluster 3

- **For Reproducibility:** Strong Validity evidence (technical documentation, open source code) suggests Reproducibility assessment should find good infrastructure. The question is whether someone can install, customise, and deploy FAIMS - not whether they can reproduce empirical findings.

---

## Structured Output

```yaml
cluster_2_evidential_strength:
  paper_slug: "ballsun-stanton-et-al-2018"
  assessment_date: "2025-12-02"
  quality_state: "high"
  research_approach: "inductive"
  paper_type: "methodological_software_tool"

  plausibility:
    score: 80
    band: "excellent"
    strengths:
      - "Claims consistent with known technical possibilities and field research challenges"
      - "Well-contextualised within existing software landscape"
      - "Anomalies/tradeoffs honestly acknowledged (technical debt)"
    weaknesses:
      - "Case study details rely on external publication"
    rationale: "Excellent for inductive. Patterns consistent with frameworks, claims contextualised, anomalies acknowledged."

  validity:
    score: 75
    band: "good"
    strengths:
      - "Comprehensive deployment metrics (40 modules, 29 deployments, 300 users)"
      - "Systematic sampling - all deployments reported, not cherry-picked"
      - "Technical specification supports capability claims directly"
    weaknesses:
      - "Detailed case study evidence in external publication"
      - "User satisfaction based on qualitative feedback, not systematic measurement"
    rationale: "Good for inductive. Data sufficient, sampling systematic, claims scoped to evidence. Deduction for external source reliance."

  robustness:
    score: 55
    band: "moderate"
    context_flag: "software_paper"
    strengths:
      - "Multiple independent deployments (29) across diverse contexts"
      - "Cross-disciplinary adoption suggests pattern consistency"
      - "Triangulation present: specs + metrics + feedback converge"
    weaknesses:
      - "No formal comparative testing against alternatives (appropriate for genre)"
      - "Single development team perspective"
    rationale: "Moderate for inductive with software paper context. Limited triangulation but appropriate for genre. Readers should independently evaluate alternatives."

  generalisability:
    score: 70
    band: "good"
    strengths:
      - "Claims bounded to 'human-mediated field research'"
      - "Cross-disciplinary and international deployment supports scope claims"
      - "Limitations honestly acknowledged"
    weaknesses:
      - "Transfer conditions (technical requirements, customisation effort) implicit rather than explicit"
    rationale: "Good for inductive. Claims bounded, scope matched to coverage, limitations present."

  cluster_synthesis:
    overall_rating: "adequate_to_strong"
    pattern_summary: "Expected software paper profile: strong Plausibility/Validity, moderate Robustness (genre-appropriate), good Generalisability."
    consistency_check: "consistent"
    implications:
      cluster_3: "Strong technical documentation and open source availability suggest good Reproducibility infrastructure."
```
