# Cluster 2: Evidential Strength (Credibility Pillar)

**Paper:** Sobotkova et al. (2016) - Measure Twice, Cut Once
**Run ID:** run-02
**Assessment Date:** 2025-12-04

## Signal 2.1: Plausibility

### Score: 78/100

### Assessment

**Methodological Paper Anchors Applied**

Claims about software co-development benefits and challenges are highly plausible given established knowledge of software engineering and digital archaeology. The paper builds sensibly on existing work.

### Strengths

1. **Coherent theoretical framing:** The generalised-vs-bespoke spectrum aligns with established software engineering concepts
2. **Consistent with prior work:** References to Raymond (2001) open-source models and existing archaeological software literature
3. **Internally consistent:** Benefits and trade-offs presented as balanced, acknowledging both strengths and weaknesses
4. **Domain-appropriate claims:** Conclusions about field conditions, offline requirements, and workflow improvements align with archaeological fieldwork realities

### Weaknesses

1. **Optimistic framing:** Authors are FAIMS developers; critique sections briefer than benefits sections
2. **Limited negative evidence:** Performance problems (E026) presented as learning opportunities rather than fundamental limitations
3. **Extrapolation risk:** Three case studies used to make general claims about co-development

### Plausibility Mapping

| Claim Type | Plausibility |
|------------|--------------|
| Technical claims (offline operation, sync issues) | HIGH - consistent with known mobile computing challenges |
| Cost-benefit claims | MODERATE - plausible but self-reported |
| Generalisation claims (C010, C037) | MODERATE - small sample limits confidence |

---

## Signal 2.2: Validity

### Score: 65/100

### Assessment

**Methodological Paper Anchors Applied**

Mixed validity: qualitative case studies are appropriate for the research questions, but quantitative claims rest on informal measurement.

### Strengths

1. **Appropriate design:** Multi-case study design suitable for exploring software deployment experiences
2. **Multiple perspectives:** Both developer and user perspectives included through author team composition
3. **Rich description:** Detailed deployment narratives enable contextual understanding
4. **Document preservation:** Communication logs archived as verifiable evidence

### Weaknesses

1. **Convenience sampling:** Three projects are early adopters who volunteered; not systematically selected
2. **Self-selection bias:** Projects that failed or abandoned FAIMS not represented
3. **Measurement informality:** "At least eight person-days saved" (E022) - methodology for estimation unclear
4. **Comparative baseline weakness:** Paper-based workflow comparison relies on memory/estimation rather than concurrent measurement

### Validity Assessment by Claim Type

| Claim Category | Validity Level | Notes |
|----------------|---------------|-------|
| Software functionality | HIGH | Verifiable through open-source code |
| Cost figures | MODERATE | Self-reported, methodology unstated |
| Time savings | LOW-MODERATE | Retrospective estimates without time-on-task data |
| User satisfaction | LOW | "Universal" agreement claimed without systematic collection |

---

## Signal 2.3: Robustness

### Score: 58/100

### Assessment

**Methodological Paper Anchors Applied**

Limited robustness assessment possible due to single deployment per site and lack of systematic sensitivity analysis.

### Strengths

1. **Multiple contexts:** Three diverse contexts (Turkey, Malawi, Peru) provide some triangulation
2. **Iterative refinement:** FAIMS 2.0 incorporates lessons from deployments, suggesting responsiveness to feedback
3. **Acknowledged limitations:** Performance issues (E026) and field recording speed concerns (E033) documented

### Weaknesses

1. **No sensitivity analysis:** Effect of varying contexts, team sizes, or site types not systematically explored
2. **Single deployment design:** Each project used FAIMS once; no longitudinal tracking
3. **Positive selection:** Only successful deployments featured; no discussion of failures
4. **Limited sample:** Three case studies insufficient for robust generalisation

### Robustness Indicators

| Indicator | Status |
|-----------|--------|
| Multiple sites | ✅ Three diverse contexts |
| Longitudinal data | ⚠️ Limited (one season per project) |
| Failure cases | ❌ Not included |
| Sensitivity analysis | ❌ Not conducted |
| Alternative explanations | ⚠️ Limited consideration |

---

## Signal 2.4: Generalisability

### Score: 55/100

### Assessment

**Methodological Paper Anchors Applied**

Moderate generalisability within similar contexts; uncertain applicability to broader archaeological practice.

### Strengths

1. **Diverse site types:** Neolithic Turkey, Stone Age Malawi, Colonial Peru represent varied archaeological contexts
2. **Transferable lessons:** Themes (upfront costs, trade-offs, interpretive impacts) likely relevant across projects
3. **Open-source model:** Generalisability enhanced by software availability for other projects to test

### Weaknesses

1. **Resource requirements:** Partner universities with ARC funding may not represent typical archaeological project resources
2. **Technology access:** Assumes tablet availability, technical support access, and infrastructure grants
3. **Team characteristics:** Project directors had prior digital literacy; generalisability to less tech-savvy teams uncertain
4. **Sample size:** Three projects insufficient for confident generalisation

### Generalisability Assessment

| Target Population | Transferability |
|-------------------|-----------------|
| Well-funded Australian projects | HIGH |
| International university projects | MODERATE |
| Commercial archaeology | UNCERTAIN |
| Community archaeology | LOW (resource constraints) |
| Non-English projects | MODERATE (Spanish demonstrated) |

---

## Cluster 2 Summary

### Aggregate Score: 64/100

### Interpretation (Methodological Paper Framework)

Evidential strength is moderate. Claims are plausible and internally consistent, but validity is weakened by informal measurement approaches and the robustness/generalisability signals suffer from small sample size and positive selection bias.

### Key Findings

1. **Plausibility (78):** Claims align with domain knowledge and are internally consistent
2. **Validity (65):** Appropriate qualitative design but quantitative claims informally measured
3. **Robustness (58):** Limited by single deployments and absence of failure cases
4. **Generalisability (55):** Diverse contexts help but small sample and resource requirements limit confidence

### Signal Weighting (Inductive Framework)

For inductive methodological papers, plausibility and validity are weighted more heavily than robustness/generalisability, which depend on larger samples:

| Signal | Weight | Weighted Score |
|--------|--------|----------------|
| Plausibility | 0.30 | 23.4 |
| Validity | 0.30 | 19.5 |
| Robustness | 0.20 | 11.6 |
| Generalisability | 0.20 | 11.0 |
| **Weighted Total** | | **65.5** |

### Caveats Applied

- Authors' vested interest in FAIMS success may influence evidence presentation
- Quantitative claims should be interpreted as indicative rather than precise
- Generalisation beyond similar project contexts should be made cautiously

---

*Cluster 2 assessment complete. Proceeding to Cluster 3: Reproducibility.*
