# Cluster 2: Evidential Strength (Credibility Pillar)

**Paper:** Ballsun-Stanton et al. (2018) - FAIMS Mobile
**Run:** run-04
**Date:** 2025-12-03
**Paper Type:** Methodological (Software Publication)

---

## Signals Assessed

- **Validity:** Do the methods and evidence support the claims made?
- **Robustness:** Would findings hold under different conditions or analyses?
- **Generalisability:** Do findings apply beyond the immediate study context?

---

## Signal 3: Validity

### Rating: **ADEQUATE** (70/100)

### Assessment

For software publications, validity concerns whether evidence supports claims about the software's effectiveness and impact.

**Strengths:**

1. **Technical claims well-supported:**
   - Architecture descriptions verified by code availability
   - Feature claims directly testable via open-source code
   - Technology stack enumerated and verifiable

2. **Deployment evidence:**
   - 40+ customisations documented
   - 300 users across 60 projects cited
   - 20,000+ fieldwork hours reported
   > "Over 5 years, we have customised FAIMS Mobile over 40 times for 60 projects with over 300 users..."

3. **Cross-project diversity:**
   - Seven disciplines mentioned (archaeology, ecology, geoscience, oral history, linguistics, biology, history)
   - Provides breadth evidence for generalisability claims

4. **External validation reference:**
   - Sobotkova et al. (2016) cited for user feedback analysis
   - Independent publication strengthens validity

**Weaknesses:**

1. **Self-reported metrics:** Deployment statistics lack methodology documentation. How were hours tracked? How were users counted?

2. **No independent verification:** Impact claims rest on project team's own data collection.

3. **Selection bias potential:** Case studies may represent successful deployments; failures not discussed.

4. **User satisfaction evidence:** Feedback quoted but selection criteria for testimonials not documented.

### Scoring Rationale (Software Publication)

For software papers, Validity assesses:
- Technical accuracy of descriptions (strong ✅)
- Evidence for effectiveness claims (moderate ⚠️)
- Methodological rigour of impact assessment (weak ⚠️)

**Score: 70/100**

---

## Signal 4: Robustness

### Rating: **ADEQUATE** (65/100)

### Assessment

For software publications, robustness concerns whether the software would perform similarly across different contexts and implementations.

**Strengths:**

1. **Cross-platform consistency:**
   - Single Android codebase serves diverse projects
   - Consistent architecture across 40+ customisations

2. **Technology maturity:**
   - Five years of development history
   - Version 2.5 indicates iterative refinement
   - "Born-digital data quality" terminology suggests mature conceptualisation

3. **Diverse deployment contexts:**
   > "...used for archaeology, ecology, geoscience, oral history..."
   - Successful operation across disciplines suggests robustness

4. **Offline capability testing:**
   - "Robust offline-capable storage and synchronisation" claimed
   - Critical for field conditions reliability

**Weaknesses:**

1. **No systematic testing reported:** Paper does not describe testing methodology, stress testing, or failure modes.

2. **Edge case documentation absent:** How does system handle data conflicts, sync failures, or device limitations?

3. **No comparative performance data:** Claims of robustness not benchmarked against alternatives.

4. **Version history not detailed:** Whether v2.5 resolved earlier issues is not documented.

### Scoring Rationale (Software Publication)

For software papers, Robustness assesses:
- Evidence of performance across contexts (moderate ✅)
- Testing and validation documentation (weak ⚠️)
- Failure mode handling (not documented ❌)

**Score: 65/100**

---

## Signal 5: Generalisability

### Rating: **ADEQUATE** (72/100)

### Assessment

For software publications, generalisability concerns whether the software applies beyond its original development context.

**Strengths:**

1. **Explicit cross-disciplinary claims:**
   > "FAIMS Mobile brings born-digital data quality to any field-based research project"
   - Broad applicability stated

2. **Demonstrated multi-disciplinary use:**
   - Archaeology (primary)
   - Ecology, geoscience, oral history, linguistics, biology, history
   - Seven disciplines provides reasonable breadth

3. **Customisation architecture:**
   - Definition packet system enables domain adaptation
   - Module library facilitates reuse
   - DSL allows field-specific customisation

4. **Infrastructure independence:**
   - Offline operation suits diverse field conditions
   - No internet dependency broadens applicability

**Weaknesses:**

1. **Archaeology-dominant evidence:** Most detailed examples and case studies from archaeology. Other disciplines mentioned but not elaborated.

2. **No systematic adoption analysis:** Which disciplines have adopted successfully? Which have not? Why?

3. **Resource requirements unclear:** What technical capacity do research teams need? Does this limit generalisability to well-resourced projects?

4. **Cultural/workflow barriers:** No discussion of barriers to adoption in different disciplinary cultures.

### Scoring Rationale (Software Publication)

For software papers, Generalisability assesses:
- Breadth of demonstrated application (moderate ✅)
- Evidence quality across domains (weak ⚠️)
- Barrier and limitation documentation (minimal ⚠️)

**Score: 72/100**

---

## Cluster 2 Summary

| Signal | Rating | Score |
|--------|--------|-------|
| Validity | Adequate | 70 |
| Robustness | Adequate | 65 |
| Generalisability | Adequate | 72 |
| **Cluster Average** | **Adequate** | **69** |

### Key Findings

1. **Strong technical validity:** Code availability allows verification of technical claims.

2. **Impact evidence limitations:** Deployment statistics and user feedback lack methodological transparency.

3. **Demonstrated breadth:** Multi-disciplinary deployment supports generalisability claims, though archaeology dominates evidence.

4. **Testing gap:** No systematic testing or failure mode documentation weakens robustness assessment.

### Cluster Rating: **ADEQUATE**

