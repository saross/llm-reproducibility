# Cluster 1: Foundational Clarity (Transparency Pillar)

**Paper:** Dye et al. (2023) - Bayesian Chronology Construction and Substance Time

**Signals assessed:** Comprehensibility, Transparency

**Research approach:** Abductive (methodological paper)

---

## Signal 1: Comprehensibility

### Score: 88/100 (Excellent)

### Assessment

Using **abductive research anchors** for a methodological paper:

**Strengths meeting 80-100 band criteria:**

1. **Explanatory claims explicitly stated and bounded:**
   - C001: "Two views of archaeological time can be distinguished: an event view modelling stratigraphic relations and a substance view modelling genealogical relations among artifacts"
   - C002: "Chronology construction is more complex in substance time than in event time, which only concerns transformation"
   - Core distinction (event time vs substance time) is clear, well-defined, and consistently applied

2. **Theoretical framework clear:**
   - Three modes of change (branching, transformation, reticulation) explicitly defined with mathematical properties
   - Allen's interval algebra framework clearly specified with 13 basic relations
   - Hierarchy from research designs (WHY) through methods (WHAT) to protocols (HOW) is traceable

3. **Alternative explanations articulated:**
   - Paper explicitly contrasts substance time approach with event time approach (Bayliss et al. 2013)
   - RD006 (comparative analysis design) structures this comparison
   - Critique of phase deposition model assumptions is well-articulated

4. **Inference logic transparent:**
   - Mathematical derivation of Allen relations for each mode is fully explicit (M008)
   - Probability estimation logic for mode inference is clearly documented (M004)
   - Step-by-step workflow from data to conclusions traceable

5. **Key concepts well-defined:**
   - "Event time," "substance time," "branching," "transformation," "reticulation" all operationally defined
   - Allen relations (oFD, mos, etc.) mathematically specified
   - Genealogical vs stratigraphic relations distinguished

**Minor limitations preventing higher score:**

- Some implicit assumptions about similarity estimation (P008 status: implicit)
- Mode inference thresholds not fully quantified (when is probability "sufficient" for confident inference?)
- Paper assumes familiarity with OxCal and Bayesian chronology (reasonable for target audience)

### Justification

Comprehensibility scored 88 (Excellent band for abductive/methodological research). The paper clearly articulates the event time vs substance time distinction (C001, C002), provides explicit theoretical framework with well-defined modes of change, and transparently documents the inference logic from Allen's interval algebra through to probability estimation. Alternative frameworks (event time analysis) are explicitly contrasted (RD006). The only limitations are minor: some implicit protocols and assumed familiarity with domain-specific tools.

---

## Signal 2: Transparency

### Score: 85/100 (Excellent)

### Assessment

Using **abductive research anchors** for a methodological paper:

**Strengths meeting 80-100 band criteria:**

1. **Theoretical framework explicitly stated:**
   - RD001: Theoretical framework distinguishing event time from substance time with three modes of change
   - RD002: Application of Allen's interval algebra to chronological relations
   - Framework rationale clearly argued (why substance time matters for historical inference)

2. **Alternative explanations considered and documented:**
   - Explicit comparison with Bayliss et al. (2013) event time analysis
   - Phase deposition model critique documented with specific issues identified
   - Rationale for constraint removal documented (P005)

3. **Evidence selection criteria transparent:**
   - Uses published Archaeological Data Service dataset (DOI: 10.5284/1018290)
   - Constraint removal decisions justified with chi-squared test rationale
   - Model assumptions explicitly stated

4. **Reasoning process traceable:**
   - 8 methods documented with clear purpose
   - 10 protocols documented (7 explicit, 3 implicit)
   - Mathematical derivations fully provided
   - Mode probability calculations documented

5. **Data/sources accessible:**
   - ArchaeoPhases R package on CRAN (stable infrastructure)
   - OxCal model code in supplement
   - R scripts in supplement
   - Original data from ADS with DOI

6. **Scope and limitations of inference clearly bounded:**
   - C006: "This paper intends to start the discussion of best practices"
   - Case study explicitly positioned as illustrative, not definitive
   - Limitations of occurrence seriation clearly articulated

**Minor limitations preventing higher score:**

1. **Supplement lacks independent DOI** - code/model attached to journal rather than archived in repository with persistent identifier
2. **Three implicit protocols** (P008, P009, P010) indicate some procedural underdocumentation:
   - Similarity estimation from type descriptions not fully specified
   - Transformation and reticulation inference less detailed than branching
3. **No explicit licence for supplement code** - ArchaeoPhases is open source, but supplement scripts' reuse conditions unclear

### Justification

Transparency scored 85 (Excellent band for abductive/methodological research). The theoretical framework is explicitly articulated (RD001, RD002), alternative approaches are systematically compared (RD006), and the reasoning process is traceable through documented methods and protocols. Code and data are available (ArchaeoPhases on CRAN, ADS dataset, supplement materials). The main transparency gaps are: supplement lacks independent DOI, three protocols remain implicit, and supplement code licence is unclear. These are minor issues that prevent a score in the 90s but do not undermine the overall excellent transparency.

---

## Cluster 1 Summary

| Signal | Score | Band |
|--------|-------|------|
| Comprehensibility | 88 | Excellent (80-100) |
| Transparency | 85 | Excellent (80-100) |
| **Cluster Mean** | **86.5** | **Excellent** |

### Foundational Clarity Assessment

The paper demonstrates **excellent foundational clarity**. The theoretical framework (event time vs substance time) is clearly articulated and consistently applied. Key concepts are operationally defined, the argument structure is traceable, and alternative approaches are explicitly compared. Documentation quality is high with 8 methods and 10 protocols captured. Minor transparency gaps (implicit protocols, supplement without DOI) are acknowledged but do not significantly impair understanding or evaluation of the work.

### Primary Signals Assessment (for Methodological Paper)

As a methodological paper, Comprehensibility and Transparency are **primary signals**. Both scoring in the Excellent band indicates strong foundational quality that supports reliable assessment of other signals.
