# Cluster 2: Evidential Strength Assessment

**Paper:** ballsun-stanton-et-al-2018
**Assessment Date:** 2025-12-03
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** inductive (confidence: high)
**Paper Type:** methodological (subtype: software_tool)

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Plausibility | 82 | Excellent | inductive/methodological |
| Validity | 75 | Good | inductive/methodological |
| Robustness | 55 | Moderate | methodological (📦 flag) |
| Generalisability | 72 | Good | inductive/methodological |

**Cluster Rating:** Adequate-to-Strong

---

## Signal 3: Plausibility

**Score:** 82/100 (Excellent)

**Approach anchors applied:** inductive/methodological

### Assessment

FAIMS Mobile's claims are highly plausible given established knowledge about field research software challenges. The paper correctly identifies known problems: field data often collected using "ad-hoc mix of hard copy, data fragments in various formats, and bespoke databases" (E012, citing Borgman 2015, Kansa & Bissell 2010, Kintigh 2006, Snow et al. 2006). The solution approach — generalised customisable software with offline capability — aligns with established e-research infrastructure patterns.

The theoretical framework draws appropriately on prior literature: comparison with ODK (E017), acknowledgement of alternatives (ARK, Heurist, Kora), citation of open-source revenue models (Kelly 2008), and quality assurance literature (Might 2010, Sun 2012). Claims about feature needs (offline capability, bidirectional sync, deep customisation) are grounded in documented field research requirements.

Anomalies and limitations are acknowledged: "customisation is more entailed" than ODK (honest trade-off), the challenge of "reallocation of time from the end of a project... to the beginning" (documented adoption barrier). The paper does not overclaim — it explicitly states "Field research projects... would be wise to evaluate both platforms" when comparing to ODK.

### Evidence

**Strengths:**

- E011-E014: Extensive literature grounding in field data collection challenges (Borgman, Kansa & Bissell, Kintigh, Snow et al., Blanke & Hedges)
- C018: "FAIMS is more customisable and has more fieldwork-specific features than ODK, but as a result customisation is more entailed" — Honest acknowledgement of trade-offs
- E042-E045: Case study evidence grounding claims in empirical deployment experience

**Weaknesses:**

- Some efficiency claims (E039: "20,000+ hours") lack comparative baseline — what would have been expected without FAIMS?
- No systematic review of field data collection software landscape; comparison relies on author knowledge

### Scoring Rationale

Score of 82 reflects Excellent band (80-100) for inductive research. Patterns consistent with established frameworks: field research challenges well-documented in literature, software solution approach theoretically grounded in e-research infrastructure patterns. Anomalies (trade-offs, adoption challenges) acknowledged and contextualised. Interpretations have strong comparative basis from prior FAIMS publications and case studies. Minor deductions for lack of systematic comparison and absence of comparative baseline for adoption metrics.

---

## Signal 4: Validity

**Score:** 75/100 (Good)

**Approach anchors applied:** inductive/methodological

### Assessment

Evidence sufficiency is adequate for the claims made. The paper supports capability claims with technical specifications (E001-E010) and supports impact claims with adoption metrics (E036-E039: 40+ customisations, 29 deployments, ~300 users, 20,000+ hours). Case study evidence (Sobotkova et al. 2016) provides empirical validation through three archaeological deployments.

Methods are appropriate for a software description paper: technical architecture documentation demonstrates capability claims; adoption metrics demonstrate uptake; qualitative case studies demonstrate user benefits. The validation approach (inductive demonstration rather than hypothesis-testing) is appropriate for the paper type.

However, scope of claims sometimes exceeds evidence scope. Claims about efficiency gains ("The time saved by avoiding digitisation and data cleaning more than offset the time required to implement FAIMS") are based on case studies, not systematic measurement. User benefit claims are largely qualitative — "Researchers reported more complete, consistent, and granular data" — without quantified comparison.

### Evidence

**Strengths:**

- E001-E010: Technical specifications directly support capability claims
- E036-E039: Adoption metrics provide quantitative evidence for uptake claims
- E042: Case studies provide empirical validation of user benefits

**Weaknesses:**

- Efficiency claims based on qualitative case study reports, not systematic measurement
- User benefit claims lack quantified comparison to alternative approaches
- Self-reported user benefits may have positive bias

### Scoring Rationale

Score of 75 reflects Good band (60-79) for inductive research. Data sufficient for main patterns: technical specs support capability claims, adoption metrics support uptake claims. Sampling systematic within the case study approach. Coverage adequate for claims made. Some alternatives considered (comparison to ODK, acknowledgement of other tools). Limitations acknowledged (adoption challenge of front-loading time investment). Claims generally scoped to evidence, though some efficiency claims may exceed systematic measurement basis.

---

## Signal 5: Robustness

**Score:** 55/100 (Moderate)

**Approach anchors applied:** methodological (📦 Descriptive/Artefact Paper flag)

### Assessment

> **📦 Context Flag:** This is a software paper describing an artefact rather than testing hypotheses. Moderate Robustness (40-60) reflects **genre expectations**, not a deficiency. Software papers describe what the tool does; systematic comparison of alternatives is a different paper type.

The paper demonstrates moderate robustness appropriate for its genre. It does not perform systematic comparison of FAIMS against alternatives — this is not the paper's purpose. The paper describes FAIMS; readers should independently evaluate alternatives.

Within its scope, the paper provides honest documentation of limitations and trade-offs:
- Customisation is "more entailed" than ODK (trade-off acknowledged)
- "Greatest challenge... reallocation of time from end of project to beginning" (adoption barrier documented)
- Case studies represent archaeological deployments; extension to other disciplines is ongoing

The paper triangulates evidence through multiple approaches: technical specification, adoption metrics, and qualitative case studies. However, these all describe FAIMS — there is no systematic comparison with alternative tools operating on the same projects.

### Evidence

**Strengths:**

- Honest documentation of trade-offs (customisation complexity vs capability)
- Multiple evidence types (technical, quantitative, qualitative) for triangulation
- Limitations explicitly acknowledged (time front-loading, learning curve)

**Weaknesses:**

- No systematic comparison with alternatives (expected for genre)
- No sensitivity analysis of claims (e.g., what if adoption metrics measured differently?)
- Single-source validation — all evidence describes FAIMS, not comparative alternatives

### Scoring Rationale

Score of 55 reflects Moderate band (40-60) appropriate for software description papers (📦 flag). The paper honestly documents limitations and trade-offs, which is good practice for software description. It does not perform systematic comparison — readers should evaluate alternatives independently. Score reflects genre-appropriate robustness rather than deficiency. Higher scores would require comparative evaluation, which is a different paper type.

---

## Signal 7: Generalisability

**Score:** 72/100 (Good)

**Approach anchors applied:** inductive/methodological

### Assessment

The paper appropriately bounds its claims while making reasonable generalisability statements. Core claims are scoped to "human-mediated field research across disciplines" — this is broad but appropriate given evidence of deployments in archaeology, ecology, geoscience, and history (E038). The paper explicitly identifies primary adoption context (archaeology) and notes expansion to other disciplines.

Limitations are acknowledged: "Most uptake has been at large, multi-year projects" — recognising that adoption pattern may not generalise to smaller projects. The challenge of transition from paper to digital is documented as a significant socio-technical change requiring preparation.

Transfer conditions are implicit but reasonable: the paper identifies features required for field research (offline capability, GIS, synchronisation) that would apply across disciplines sharing these requirements. The modular architecture (definition packets) explicitly supports transfer to new contexts.

### Evidence

**Strengths:**

- C001: Claims bounded to "human-mediated field research across disciplines"
- E037-E038: Deployments documented across multiple disciplines (archaeology, ecology, geoscience, history)
- Explicit acknowledgement that adoption has been primarily at "large, multi-year projects"
- RD001: Iterative co-development across disciplines supports generalisability claim

**Weaknesses:**

- Primary validation from archaeology; other disciplines less extensively documented
- Transfer conditions not explicitly specified (what makes a discipline suitable for FAIMS?)
- No explicit discussion of contexts where FAIMS would NOT be appropriate

### Scoring Rationale

Score of 72 reflects Good band (60-79) for inductive research. Pattern claims bounded (field research across disciplines). Sampling limitations acknowledged (large multi-year projects, archaeology-primary). Scope generally matched to coverage — claims about cross-disciplinary use supported by evidence of deployments in 4 disciplines. Extrapolations qualified — expansion to other disciplines noted as ongoing. Constraints stated but implicit — what makes a discipline suitable for FAIMS not explicitly specified.

---

## Cluster Synthesis

**Overall Evidential Strength:** Adequate-to-Strong

This paper demonstrates solid evidential strength for a methodological software publication. Plausibility is high (82) due to strong theoretical grounding in field research challenges and honest acknowledgement of trade-offs. Validity is good (75) with technical specifications and adoption metrics supporting claims, though some efficiency claims exceed systematic measurement basis. Generalisability is good (72) with appropriate scoping to field research disciplines and acknowledged adoption patterns.

Robustness (55) is moderate, which is **appropriate for the genre** (📦 flag). Software description papers describe artefacts; they do not perform systematic comparative evaluation. The paper honestly documents limitations and trade-offs, meeting expectations for this paper type.

### Pattern Summary

Signals form a coherent pattern appropriate for methodological software papers:
- **High Plausibility:** Strong theoretical grounding and honest trade-off acknowledgement
- **Good Validity:** Adequate evidence for claims with appropriate caveats
- **Moderate Robustness:** Genre-appropriate (📦 flag) — describes artefact, not test alternatives
- **Good Generalisability:** Appropriate scoping with acknowledged limitations

The overall pattern reflects a well-executed software description paper with appropriate evidential grounding.

### Implications for Cluster 3

- **For Reproducibility:** Strong infrastructure supports high reproducibility score. The paper's transparency and artefact availability (open source code, multiple distribution channels, comprehensive documentation) directly enable reproducibility assessment. The software itself is the reproducible artefact — and it is exceptionally well-documented and accessible.

---

## Structured Output

```yaml
cluster_2_evidential_strength:
  paper_slug: "ballsun-stanton-et-al-2018"
  assessment_date: "2025-12-03"
  quality_state: "high"
  research_approach: "inductive"
  paper_type: "methodological"
  paper_subtype: "software_tool"

  plausibility:
    score: 82
    band: "excellent"
    strengths:
      - "Strong theoretical grounding in field research literature"
      - "Honest acknowledgement of trade-offs (customisation complexity)"
      - "Appropriate comparison with alternatives (ODK)"
      - "Anomalies and limitations documented"
    weaknesses:
      - "Adoption metrics lack comparative baseline"
      - "No systematic review of software landscape"
    rationale: "Exceeds Excellent threshold. Patterns consistent with established frameworks, anomalies acknowledged, interpretations well-grounded in comparative literature and case studies."

  validity:
    score: 75
    band: "good"
    strengths:
      - "Technical specifications directly support capability claims"
      - "Adoption metrics provide quantitative evidence"
      - "Case studies provide empirical validation"
    weaknesses:
      - "Efficiency claims based on qualitative reports, not systematic measurement"
      - "User benefit claims lack quantified comparison"
    rationale: "Good band achieved. Data sufficient for main patterns, sampling systematic within case study approach, limitations acknowledged. Some claims may slightly exceed systematic evidence basis."

  robustness:
    score: 55
    band: "moderate"
    context_flag: "📦 Descriptive/Artefact Paper"
    strengths:
      - "Honest documentation of trade-offs"
      - "Multiple evidence types for triangulation"
      - "Limitations explicitly acknowledged"
    weaknesses:
      - "No systematic comparison with alternatives (expected for genre)"
      - "Single-source validation"
    rationale: "Moderate score appropriate for software description papers (📦 flag). Paper describes artefact, not tests alternatives. Honest limitation documentation meets genre expectations."

  generalisability:
    score: 72
    band: "good"
    strengths:
      - "Claims bounded to field research across disciplines"
      - "Deployments documented across 4 disciplines"
      - "Adoption limitations acknowledged"
    weaknesses:
      - "Primary validation from archaeology"
      - "Transfer conditions not explicitly specified"
    rationale: "Good band achieved. Pattern claims appropriately bounded, sampling limitations acknowledged, scope matched to coverage. Constraints stated but implicit."

  cluster_synthesis:
    overall_rating: "adequate-to-strong"
    pattern_summary: "Coherent pattern appropriate for methodological software papers. High plausibility, good validity, genre-appropriate moderate robustness, good generalisability."
    consistency_check: "consistent"
    implications:
      cluster_3: "Strong infrastructure supports high reproducibility. Open source code, multiple distribution channels, comprehensive documentation enable excellent reproducibility assessment."
```
