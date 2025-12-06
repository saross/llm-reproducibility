# Cluster 2: Evidential Strength Assessment

**Paper:** sobotkova-et-al-2016
**Assessment Date:** 2025-12-04
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** inductive (confidence: high)
**Paper Type:** methodological
**Context Flag:** 📦 Software/Methodological paper (descriptive/artefact genre)

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Plausibility | 75 | Good | inductive/methodological |
| Validity | 68 | Good | inductive/methodological |
| Robustness | 52 | Moderate | methodological (📦 genre-appropriate) |
| Generalisability | 70 | Good | inductive |

**Cluster Rating:** Adequate

---

## Signal 3: Plausibility

**Score:** 75/100 (Good)

**Approach anchors applied:** inductive/methodological

### Assessment

The paper's claims demonstrate good plausibility within the field computing and digital archaeology domain. Claims are grounded in established principles of software development (generalisation vs. customisation trade-offs, co-development models, total cost of ownership) and archaeological practice (importance of flexibility for diverse field conditions, data quality concerns, paperwork reduction benefits).

The three-case structure provides comparative evidence consistent with known patterns in archaeological field recording. The claim that generalised tools offer cost advantages over bespoke development (C001, C012) aligns with software engineering best practice. The time-savings claims from post-fieldwork data processing (C022-C030) are consistent with documented experiences from other digital recording initiatives.

However, some claims involve unstated assumptions. IA003 notes the implicit assumption that three case studies are representative of "typical" archaeological projects. IA004 assumes project directors' self-reports accurately reflect actual costs and benefits. These assumptions are plausible but not explicitly argued, representing a minor plausibility gap.

### Evidence

**Strengths:**
- C001: "Generalised, open-source tools designed for field research bring the advantages of bespoke software within reach of 'typical' projects" - Grounded in software engineering principles and consistent with domain experience
- E018: "All three project directors provided feedback that they experienced significant time savings during post-excavation processing" - Consistent with digital recording literature
- RD002: Explicit positioning of FAIMS between commercial and bespoke alternatives reflects established taxonomy in field computing

**Weaknesses:**
- IA003: "Three case study projects are representative of typical archaeological field projects" - Plausible but assumed rather than argued
- IA004: "Project directors' self-reported experiences accurately reflect actual costs and benefits" - Recall bias and positivity bias not addressed

### Scoring Rationale

Score of 75 (Good for inductive) reflects: patterns generally consistent with domain frameworks (60-79), classifications reasonable (FAIMS positioned appropriately in software landscape), major interpretations have comparative basis (other digital recording initiatives). Falls short of Excellent (80-100) because: some implicit assumptions not explicitly justified; anomalies (e.g., variations in adoption success across projects) addressed but not deeply analysed.

---

## Signal 4: Validity

**Score:** 68/100 (Good)

**Approach anchors applied:** inductive/methodological

### Assessment

The paper provides good evidence sufficiency for a methodological case study. The 35 evidence items support 50 claims through explicit cross-references. Data collection methods (post-project questionnaires, emails, chat messages) are appropriate for capturing deployment experiences. The three case studies provide sufficient coverage for pattern identification across different project contexts (Turkey, Malawi, Peru).

Evidence directly supports main claims. E013-E015 provide specific cost data supporting claims about deployment affordability. E018-E021 document time savings claims. E032 documents the open-source licensing model. The evidence-claim mappings are explicit and traceable.

However, validity limitations exist. The sample of three projects, while providing coverage across regions, is limited for robust pattern generalisation. Evidence is primarily self-reported (IA004), introducing potential recall and positivity bias. Quantitative claims (cost savings, time savings) rely on project estimates rather than systematic measurement. Alternative interpretations (e.g., selection bias in willing adopters, novelty effects) are not explicitly considered.

### Evidence

**Strengths:**
- E013-E015: Specific cost data ($16,000-$30,000 for customisation) provides concrete evidence for affordability claims
- E018-E021: Multiple project directors reporting time savings provides convergent evidence
- M001-M004: Methods appropriate for capturing deployment experiences (questionnaires, case documentation, thematic analysis)

**Weaknesses:**
- Sample size: Three case studies limit pattern generalisation
- E032 evidences open-source claim but verification depends on external repository access
- Alternative explanations not considered (early adopter bias, research team relationship effects)

### Scoring Rationale

Score of 68 (Good for inductive) reflects: data sufficient for main patterns (60-79), sampling systematic (three diverse projects), coverage adequate for exploratory goals. Falls short of Excellent (80-100) because: limited sample size, reliance on self-reported data, alternative interpretations not explicitly considered. Scope of claims generally matches evidence but some generalisations may exceed three-project base.

---

## Signal 5: Robustness

**Score:** 52/100 (Moderate)

**Approach anchors applied:** methodological (📦 genre-appropriate)

### Assessment

This is a **methodological/software paper (📦)**, a descriptive genre that documents artefacts rather than testing hypotheses. For software papers, robustness assessment focuses on whether the paper honestly documents what it claims to document, not whether it systematically compares alternatives.

The paper provides moderate robustness, appropriate for its genre. Multiple case studies provide some triangulation - patterns that appear across Turkey, Malawi, and Peru deployments are more robust than single-site observations. The three themes (costs, trade-offs, interpretation) represent convergent findings across cases.

However, the paper does not conduct sensitivity analysis or test findings against different analytical frameworks - this is expected for descriptive software papers. Theme derivation process is implicit (P004), meaning another analyst might identify different themes. Cost calculations lack documented methodology (P005), limiting verification. These are transparency gaps rather than robustness failures per se.

The paper honestly acknowledges limitations: "Our three case studies are not 'archaeological' sites in a conventional sense" (acknowledging scope constraints), and "High-quality support still carries costs" (acknowledging ongoing resource requirements). This honest limitation acknowledgement is good practice for software description.

### Evidence

**Strengths:**
- Three geographically diverse case studies provide triangulation (Turkey, Malawi, Peru)
- Multiple data sources (questionnaires, emails, chat messages) support pattern identification
- E028-E031: Different project directors reporting similar experiences provides convergent evidence

**Weaknesses:**
- P004 (implicit): Theme derivation not documented - patterns may depend on analyst choices
- P005 (implicit): Cost calculation methodology not specified - figures difficult to verify
- No formal inter-coder reliability for thematic analysis

### Scoring Rationale

Score of 52 (Moderate, genre-appropriate for 📦 software paper) reflects: limited triangulation present (multiple cases, multiple sources), pattern robustness unclear due to implicit analytical procedures, minimal reliability assessment, few alternatives explored (expected for descriptive paper). A moderate score for a software paper indicates honest description, not a deficiency. The paper documents its artefact appropriately; readers should independently evaluate alternatives.

---

## Signal 7: Generalisability

**Score:** 70/100 (Good)

**Approach anchors applied:** inductive

### Assessment

The paper demonstrates good scope awareness and appropriate limitation acknowledgement. Claims are explicitly bounded to "typical" archaeological projects using mobile field recording, with clear recognition that the three case studies have specific characteristics that may not generalise universally.

The paper explicitly positions its lessons as applicable to "any field software development project" while acknowledging constraints. C047 notes that success depends on "quality technical support" - a transfer condition. C048 acknowledges ongoing support costs. C050 offers general guidance to "future users of generalised software." These represent appropriate qualification of claims.

Temporal and technological constraints are implicit but relevant - 2016 mobile technology represents a specific moment in hardware/software evolution. The paper's lessons about customisation vs. generalisation trade-offs may apply beyond this specific technology generation, but this temporal scope is not explicitly addressed.

### Evidence

**Strengths:**
- RD001: "Case study methodology to examine co-development experiences through thematic analysis" - Design acknowledges exploratory scope
- C050: "We hope this paper offers a few guideposts to future users of generalised software" - Appropriately qualified generalisation
- C047-C049: Explicit conditions for successful adoption (support quality, cost management, realistic expectations)

**Weaknesses:**
- "Typical" projects undefined - boundary conditions for generalisation unclear
- Temporal scope (2016 technology context) not explicitly bounded
- Three case studies all involve research-affiliated teams - may not generalise to commercial or CRM contexts

### Scoring Rationale

Score of 70 (Good for inductive) reflects: pattern claims bounded to mobile field recording context (60-79), sampling limitations acknowledged (three specific projects), scope generally matched to coverage, extrapolations qualified with conditions. Falls short of Excellent (80-100) because: "typical project" criteria undefined, temporal bounds not explicit, transfer conditions to non-research contexts not specified.

---

## Cluster Synthesis

**Overall Evidential Strength:** Adequate

The paper demonstrates adequate evidential strength overall, with consistent Good scores for Plausibility (75), Validity (68), and Generalisability (70), and a genre-appropriate Moderate score for Robustness (52). The pattern across signals indicates a well-grounded case study that makes defensible claims within appropriate scope.

The primary strength is the convergent evidence from multiple case studies and data sources. Claims about generalised software benefits are supported by specific cost data, time-savings reports, and project director feedback across diverse deployment contexts. The paper's positioning within established software development and digital archaeology frameworks provides theoretical grounding.

The primary limitations are reliance on self-reported data, limited sample size, and implicit analytical procedures. These are typical for case study methodology and do not undermine the paper's contribution, but they constrain the precision and generalisability of claims.

### Pattern Summary

Scores are reasonably consistent across signals (68-75 for three signals, 52 for genre-appropriate Robustness). The paper exhibits a coherent credibility profile: well-grounded claims (Plausibility), adequate evidence for exploratory goals (Validity), appropriate scope qualification (Generalisability), with expected limitations in analytical robustness for a descriptive methodological paper.

### Implications for Cluster 3

- **For Reproducibility:** The paper's strong software transparency (open-source, GitHub) supports computational reproducibility. Methodological reproducibility is limited by implicit analytical procedures. Cluster 3 should assess software reproducibility as a strength while noting limitations in analytical workflow reproducibility.

---

## Structured Output

```yaml
cluster_2_evidential_strength:
  paper_slug: "sobotkova-et-al-2016"
  assessment_date: "2025-12-04"
  quality_state: "high"
  research_approach: "inductive"
  paper_type: "methodological"
  context_flag: "📦 software/methodological paper"

  plausibility:
    score: 75
    band: "good"
    strengths:
      - "Claims grounded in established software engineering and digital archaeology principles"
      - "Three-case comparative evidence consistent with domain knowledge"
      - "Cost-benefit patterns align with documented digital recording experiences"
    weaknesses:
      - "Representativeness of case studies assumed not argued (IA003)"
      - "Accuracy of self-reported experiences assumed (IA004)"
    rationale: "Good plausibility for inductive case study. Patterns consistent with domain frameworks, interpretations have comparative basis. Minor gaps in explicit justification of assumptions."

  validity:
    score: 68
    band: "good"
    strengths:
      - "Specific cost and time data support main claims"
      - "Multiple data sources (questionnaires, communications) provide convergent evidence"
      - "Methods appropriate for capturing deployment experiences"
    weaknesses:
      - "Limited sample size (three projects)"
      - "Reliance on self-reported data without independent verification"
      - "Alternative interpretations not explicitly considered"
    rationale: "Good validity for exploratory case study. Data sufficient for main patterns, sampling systematic across diverse contexts. Limited by sample size and self-report methodology."

  robustness:
    score: 52
    band: "moderate"
    strengths:
      - "Three geographically diverse case studies provide triangulation"
      - "Multiple data sources support pattern identification"
      - "Honest acknowledgement of limitations"
    weaknesses:
      - "Theme derivation process not documented"
      - "Cost calculation methodology not specified"
      - "No formal inter-coder reliability assessment"
    rationale: "Moderate robustness, genre-appropriate for 📦 software paper. Descriptive papers document artefacts rather than test alternatives. Score reflects honest description, not deficiency."

  generalisability:
    score: 70
    band: "good"
    strengths:
      - "Claims bounded to mobile field recording context"
      - "Transfer conditions specified (support quality, cost management)"
      - "Appropriately qualified extrapolations"
    weaknesses:
      - "'Typical project' criteria undefined"
      - "Temporal bounds (2016 technology) not explicit"
      - "Non-research contexts not addressed"
    rationale: "Good generalisability for inductive case study. Scope generally matched to coverage, limitations acknowledged. Some boundary conditions implicit."

  cluster_synthesis:
    overall_rating: "adequate"
    pattern_summary: "Coherent credibility profile with consistent Good scores across three signals and genre-appropriate Moderate robustness. Well-grounded case study with typical methodological limitations."
    consistency_check: "consistent"
    implications:
      cluster_3: "Strong software reproducibility (open-source, GitHub); limited methodological reproducibility (implicit analytical procedures)"
```
