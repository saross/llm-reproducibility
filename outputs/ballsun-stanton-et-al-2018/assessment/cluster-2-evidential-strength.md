# Cluster 2: Evidential Strength Assessment

**Paper:** ballsun-stanton-et-al-2018
**Assessment Date:** 2025-11-30
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** Methodological (confidence: high)
**Paper Type:** Methodological (software paper)

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Plausibility | 74 | Good | Methodological |
| Validity | 62 | Good | Methodological |
| Robustness | 55 | Moderate | Methodological 📦 |
| Generalisability | 70 | Good | Methodological |

**Cluster Rating:** Adequate

---

## Signal 3: Plausibility

**Score:** 74/100 (Good)

**Approach anchors applied:** Methodological

### Assessment

The paper demonstrates good plausibility for its software design claims. The architecture decisions are consistent with established software engineering practice: modular design for customisation, offline-first for fieldwork, open source for academic sustainability. Claims about field data quality problems (C003-C008) are grounded in cited literature and field experience.

The iterative co-development approach (RD001) is consistent with participatory design literature. Claims about five years of deployment experience align with the project timeline and cited case studies. The software's cross-disciplinary applicability is plausibly supported by documented deployments in archaeology, geoscience, history, and ecology.

However, some claims about software benefits lack detailed supporting evidence in this paper. Efficiency gains, data quality improvements, and workflow benefits are asserted but detailed evidence is in cited papers rather than presented here.

### Evidence

**Strengths:**
- Architecture decisions consistent with software engineering best practice
- Problem framing (C003-C008) grounded in literature
- RD001: Five years of deployment experience documented
- Cross-disciplinary deployments cited

**Weaknesses:**
- Benefit claims rely on cited evidence rather than primary data
- Some efficiency/quality claims lack detailed support in paper

### Scoring Rationale

Score of 74 (Good) reflects: design decisions consistent with domain knowledge (60-79); theoretical grounding in software engineering practice present (60-79); claims generally plausible but some rely on external evidence.

---

## Signal 4: Validity

**Score:** 62/100 (Good)

**Approach anchors applied:** Methodological

### Assessment

The paper demonstrates moderate-to-good validity for a software description paper. Case studies (RD002) provide evidence of deployment impact, though details are in the cited Sobotkova et al. 2016 paper rather than presented here. This citation-based evidence is appropriate for a short software paper but limits independent validity assessment.

The claim that "three case studies involving archaeological deployments showed that users benefited from increased efficiency of fieldwork" (E018-E020) is supported by citation but not detailed methodology. User uptake statistics (E021) provide quantitative evidence of adoption though not effectiveness.

For methodological papers, validity is about whether claims are adequately supported. The architecture claims are validated by the existence of working software. The benefit claims rely on cited evidence and deployment experience.

### Evidence

**Strengths:**
- Case studies cited (Sobotkova et al. 2016)
- Uptake statistics provided
- Working software validates architecture claims
- Five years of deployment validates stability

**Weaknesses:**
- Case study methodology not detailed in this paper
- Benefit claims rely on cited rather than primary evidence
- User satisfaction data not presented

### Scoring Rationale

Score of 62 (Good) reflects: evidence supports main claims (60-79); methods appropriate for software paper format; alternatives not extensively considered; some reliance on external evidence.

---

## Signal 5: Robustness

**Score:** 55/100 (Moderate) 📦

**Approach anchors applied:** Methodological

> 📦 **Context Flag:** Software and data papers describe artefacts rather than testing hypotheses. They do not typically include systematic comparisons, sensitivity analyses, or robustness checks. A Moderate Robustness score reflects genre expectations — it is not a criticism of the paper.

### Assessment

The paper demonstrates moderate robustness, appropriate for a software description paper. FAIMS is described as a solution to field data collection problems; the paper documents what the software does rather than testing it against alternatives. This is exactly what software papers in venues like SoftwareX are meant to do.

The paper acknowledges some limitations: development challenges (E006-E012) including testing infrastructure needs, GUI creation difficulties, and complexity costs. This honest acknowledgement of trade-offs is good practice for software documentation.

Alternative approaches are mentioned but not systematically compared. The paper notes that other tools exist (commercial software, ad-hoc solutions) but does not provide detailed comparison. This is appropriate: comparative evaluation would be a different paper type (e.g., a review or benchmark study).

### Evidence

**Strengths:**
- Limitations acknowledged (E006-E012)
- Design trade-offs discussed qualitatively
- Five years of evolution suggests iterative refinement

**Weaknesses:**
- Limited comparison to alternative software
- Design choices not systematically tested against alternatives
- No sensitivity analysis of architecture decisions

### Scoring Rationale

Score of 55 (Moderate) with 📦 flag reflects: software paper describes artefact (genre expectation); limitations honestly acknowledged (positive); alternatives mentioned but not systematically compared (appropriate for type). Robustness is assessed against software paper expectations, not empirical study standards.

---

## Signal 6: Generalisability

**Score:** 70/100 (Good)

**Approach anchors applied:** Methodological

### Assessment

The paper demonstrates good scope constraint with cross-disciplinary applicability claims. FAIMS is explicitly designed for field research across disciplines, with documented deployments in archaeology, geoscience, history, and ecology. This cross-disciplinary design is central to the software's value proposition.

The paper appropriately acknowledges limitations. The focus on large multi-year projects reflects uptake demographics. The modular architecture is designed to accommodate disciplinary differences through customisation rather than one-size-fits-all design.

However, transfer conditions are implicit. The paper doesn't systematically specify what conditions would make FAIMS suitable or unsuitable for a particular field research context. Hardware requirements (Android devices), connectivity constraints (offline-first design), and customisation needs are discussed but not formalised.

### Evidence

**Strengths:**
- Cross-disciplinary design explicit
- Multiple discipline deployments documented
- Modular architecture accommodates variation
- Large multi-year project focus acknowledged

**Weaknesses:**
- Transfer conditions implicit
- Hardware/infrastructure requirements not formalised
- Customisation complexity may limit some uptake

### Scoring Rationale

Score of 70 (Good) reflects: claims bounded to field research context; disciplinary scope appropriate; limitations acknowledged; transfer conditions implicit rather than formalised.

---

## Cluster Synthesis

**Overall Evidential Strength:** Adequate

This methodological software paper demonstrates adequate evidential strength with scores ranging from 55-74 (Moderate to Good). The pattern reflects the descriptive nature of software papers: clear design rationale with documentation rather than systematic comparison to alternatives.

The Robustness score (55, Moderate 📦) requires contextual interpretation. For a software description paper, this score reflects genre expectations rather than a deficiency. Software papers in venues like SoftwareX are meant to document software, not conduct comparative evaluations. The paper honestly acknowledges limitations and discusses design trade-offs — this is good practice for the genre.

### Pattern Summary

The dominant pattern is software description with honest limitation acknowledgement. Plausibility is good (design decisions sensible), Validity is adequate (case studies cited), Robustness is moderate (limited comparison, expected for type), Generalisability is good (cross-disciplinary design). Similar patterns should be expected for other software papers and data papers.

### Implications for Cluster 3

- **For Reproducibility:** Excellent code availability (GitHub, GPLv3) suggests high software reproducibility. Methodological Transparency variant (🔧) applies as this is software being described, not analytical workflow.

---

## Structured Output

```yaml
cluster_2_evidential_strength:
  paper_slug: "ballsun-stanton-et-al-2018"
  assessment_date: "2025-11-30"
  quality_state: "high"
  research_approach: "methodological"

  plausibility:
    score: 74
    band: "good"
    strengths:
      - "Architecture decisions consistent with software engineering practice"
      - "Problem framing grounded in literature"
      - "Cross-disciplinary deployments documented"
    weaknesses:
      - "Some benefit claims rely on cited evidence"
    rationale: "Good plausibility. Design decisions sensible, claims grounded, some reliance on external evidence."

  validity:
    score: 62
    band: "good"
    strengths:
      - "Case studies cited"
      - "Working software validates architecture"
      - "Five years deployment validates stability"
    weaknesses:
      - "Case study methodology not detailed"
      - "Benefit claims rely on cited evidence"
    rationale: "Good validity for software paper. Evidence supports claims, some external reliance."

  robustness:
    score: 55
    band: "moderate"
    context_flag: "software_paper"
    strengths:
      - "Limitations acknowledged"
      - "Design trade-offs discussed"
    weaknesses:
      - "Limited comparison to alternatives"
      - "No systematic sensitivity analysis"
    rationale: "Moderate robustness reflects software paper genre. Describes artefact rather than testing alternatives."

  generalisability:
    score: 70
    band: "good"
    strengths:
      - "Cross-disciplinary design explicit"
      - "Multiple discipline deployments"
      - "Modular architecture accommodates variation"
    weaknesses:
      - "Transfer conditions implicit"
    rationale: "Good scope constraint. Cross-disciplinary applicability documented, transfer conditions informal."

  cluster_synthesis:
    overall_rating: "adequate"
    pattern_summary: "Software description with honest limitations. Moderate robustness expected for genre."
    consistency_check: "consistent"
    implications:
      cluster_3: "Excellent code availability; Methodological Transparency variant applies"
```
