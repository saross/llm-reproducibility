# Credibility Assessment Frameworks by Research Approach

**Purpose:** Guide selection of appropriate assessment framework and signal emphasis based on research approach classification

**Date:** 2025-11-17

---

## Overview

Different research approaches require different credibility assessment priorities. This document provides framework selection logic and signal emphasis guidance based on research approach classification (deductive/inductive/abductive).

**Key Principle:** Avoid category error — do not assess inductive research by deductive standards, or vice versa. Use approach-appropriate criteria.

### Three Pillars Framework

The seven signals are organised into three pillars (see `assessment-pillars.md`):

| Pillar | Signals | Applies To |
|--------|---------|------------|
| **Transparency** | Comprehensibility, Transparency | All papers |
| **Credibility** | Plausibility, Validity, Robustness, Generalisability | All papers |
| **Reproducibility** | Reproducibility | Computational components only |

Approach-specific emphasis varies signal priority within each pillar.

---

## Framework Selection Logic

### Deductive Research (Hypothesis-Testing, Confirmatory)

**Assessment Framework:** Confirmatory research evaluation

**Primary Assessment Emphasis:**

- **Validity** - Evidence adequacy for hypothesis tests
- **Robustness** - Sensitivity to analytical choices
- **Reproducibility** - Code/data for reproduction

**Secondary Assessment Emphasis:**

- **Transparency** - Pre-registration, methods documentation
- **Comprehensibility** - Hypothesis clarity
- **Plausibility** - Theoretical grounding

**De-emphasised (but still assessed):**

- **Generalisability** - Assessed but not primary concern for single studies

**Rationale:**

Deductive research makes explicit, testable predictions. The core credibility question is: "Are the hypothesis tests valid, robust, and reproducible?" Emphasis falls on evidential adequacy (Validity), analytical soundness (Robustness), and reproducibility of confirmatory tests (Reproducibility).

**Example Assessment Priority:**

For a deductive archaeological study testing the hypothesis that "settlements cluster near water sources":

1. **Validity (Primary):** Is evidence sufficient to test the hypothesis? Are alternative hypotheses considered?
2. **Robustness (Primary):** Would results hold with different clustering algorithms or distance thresholds?
3. **Reproducibility (Primary):** Are settlement coordinates and analysis code available?
4. **Transparency (Secondary):** Was hypothesis pre-specified? Are methods documented?
5. **Comprehensibility (Secondary):** Is hypothesis clearly bounded?
6. **Plausibility (Secondary):** Is hypothesis grounded in theory?
7. **Generalisability (Assessed):** Are scope limits stated?

---

### Inductive Research (Exploratory, Pattern-Finding, Descriptive)

**Assessment Framework:** Exploratory research evaluation

**Primary Assessment Emphasis:**

- **Transparency** - Research design clarity, workflow documentation
- **Comprehensibility** - Pattern descriptions clarity
- **Generalisability** - Appropriate scope constraints

**Secondary Assessment Emphasis:**

- **Validity** - Evidence sufficiency for pattern claims
- **Reproducibility** - Data archiving and workflow documentation
- **Plausibility** - Consistency with domain knowledge

**De-emphasised (but still assessed):**

- **Robustness** - Assessed but expectations differ (triangulation, not sensitivity analysis)

**Rationale:**

Inductive research discovers patterns without pre-specified hypotheses. The core credibility question is: "Are patterns clearly described, appropriately scoped, and transparently derived?" Emphasis falls on workflow transparency (Transparency), pattern clarity (Comprehensibility), and appropriate scope constraint (Generalisability).

**Key Adaptation:** Pre-registration not expected. Emphasis shifts from confirmatory testing to transparent exploration and appropriate constraint.

**Example Assessment Priority:**

For an inductive regional survey documenting settlement patterns:

1. **Transparency (Primary):** Are survey goals, coverage, and sampling strategy documented?
2. **Comprehensibility (Primary):** Are pattern descriptions clear and bounded?
3. **Generalisability (Primary):** Are spatial/temporal scope and sampling limitations explicit?
4. **Validity (Secondary):** Is coverage adequate for pattern claims?
5. **Reproducibility (Secondary):** Are survey data archived with metadata?
6. **Plausibility (Secondary):** Do patterns align with regional chronologies?
7. **Robustness (Assessed):** Is there convergent evidence (multiple indicators)?

---

### Abductive Research (Inference to Best Explanation, Interpretive)

**Assessment Framework:** Explanatory inference evaluation

**Primary Assessment Emphasis:**

- **Plausibility** - Explanatory coherence and theoretical fit
- **Validity** - Adequacy of evidence for inference
- **Robustness** - Consideration of alternative explanations

**Secondary Assessment Emphasis:**

- **Transparency** - Framework clarity and reasoning traceability
- **Comprehensibility** - Explanatory claim clarity
- **Generalisability** - Inference scope constraints

**De-emphasised (but still assessed):**

- **Reproducibility** - Assessed as reasoning traceability, not code/data sharing

**Rationale:**

Abductive research infers explanatory frameworks from observed patterns. The core credibility question is: "Is the proposed explanation plausible, well-evidenced, and robust to alternatives?" Emphasis falls on explanatory coherence (Plausibility), evidential grounding (Validity), and consideration of alternative explanations (Robustness).

**Key Adaptation:** Reproducibility means "can others trace the reasoning?" not "can others rerun the code?" Focus on interpretive transparency, not computational reproducibility.

**Example Assessment Priority:**

For an abductive study inferring social organisation from burial patterns:

1. **Plausibility (Primary):** Is the social organisation model coherent with anthropological theory?
2. **Validity (Primary):** Is burial evidence sufficient for the inference?
3. **Robustness (Primary):** Are alternative interpretations (e.g., different kinship models) explicitly considered?
4. **Transparency (Secondary):** Is the theoretical framework explicit?
5. **Comprehensibility (Secondary):** Is the explanatory claim clear?
6. **Generalisability (Secondary):** Are scope limits of the inference stated?
7. **Reproducibility (Assessed):** Can others trace the reasoning from evidence to inference?

---

## Mixed-Method Research

### Framework Selection for Mixed-Method Studies

For papers with mixed research approaches:

1. **Identify primary approach** from classification.json
2. **Use primary approach framework** as baseline
3. **Note secondary approaches** in assessment
4. **Apply appropriate criteria** to each component

**Example:** A study with:

- Phase 1: Deductive hypothesis testing (experimental archaeology)
- Phase 2: Inductive pattern discovery (archaeological assemblage analysis)

**Assessment approach:**

- **Classify as:** Mixed deductive-inductive, primarily deductive
- **Primary framework:** Deductive (emphasis on Validity, Robustness, Reproducibility for experimental phase)
- **Secondary framework:** Inductive (emphasis on Transparency, Comprehensibility for pattern phase)
- **Overall assessment:** Evaluate each phase by appropriate criteria, weight primary approach more heavily in overall credibility profile

---

## Signal Emphasis by Research Approach

### Summary Table: Signal Priority by Approach

| Signal | Deductive | Inductive | Abductive |
|--------|-----------|-----------|-----------|
| **Comprehensibility** | Secondary | **Primary** | Secondary |
| **Transparency** | Secondary | **Primary** | Secondary |
| **Plausibility** | Secondary | Secondary | **PRIMARY** |
| **Validity** | **PRIMARY** | Secondary | **PRIMARY** |
| **Robustness** | **PRIMARY** | Assessed* | **PRIMARY** |
| **Reproducibility** | **PRIMARY** | Secondary | Assessed** |
| **Generalisability** | Assessed | **Primary** | Secondary |

*Inductive robustness = triangulation, convergent evidence (not sensitivity analysis)

**Abductive reproducibility = reasoning traceability (not code/data sharing)

---

## Signal Weighting Guidance

### Narrative Emphasis (for Reports)

**Deductive Research:**

Report structure should emphasise:

1. Evidence adequacy for hypothesis tests (Validity)
2. Analytical robustness and sensitivity (Robustness)
3. Reproducibility of confirmatory analyses (Reproducibility)
4. Methods transparency and pre-registration (Transparency)

De-emphasise (but still mention):

- Generalisability (unless multi-site comparative study)

**Inductive Research:**

Report structure should emphasise:

1. Research design and workflow transparency (Transparency)
2. Pattern description clarity and scope (Comprehensibility + Generalisability)
3. Sampling strategy and coverage adequacy (Validity)
4. Data archiving and accessibility (Reproducibility)

De-emphasise (but still mention):

- Robustness (focus on triangulation, not sensitivity testing)

**Abductive Research:**

Report structure should emphasise:

1. Explanatory coherence and theoretical fit (Plausibility)
2. Evidence adequacy for inference (Validity)
3. Alternative explanation consideration (Robustness)
4. Framework clarity and reasoning traceability (Transparency + Reproducibility)

De-emphasise (but still mention):

- Computational reproducibility (unless quantitative modelling involved)

---

## Experimental Scoring Weights (for Future Aggregate Scores)

**Note:** Current implementation does NOT use weighted aggregate scores. All signals scored 0-100. This section provides guidance for potential future aggregate scoring if needed.

### Deductive Research Weights

- Validity: 25%
- Robustness: 25%
- Reproducibility: 20%
- Transparency: 15%
- Comprehensibility: 10%
- Plausibility: 5%
- Generalisability: Not weighted (assessed qualitatively)

### Inductive Research Weights

- Transparency: 25%
- Comprehensibility: 20%
- Generalisability: 20%
- Validity: 15%
- Reproducibility: 15%
- Plausibility: 5%
- Robustness: Not weighted (assessed qualitatively)

### Abductive Research Weights

- Plausibility: 25%
- Validity: 25%
- Robustness: 20%
- Transparency: 15%
- Comprehensibility: 10%
- Generalisability: 5%
- Reproducibility: Not weighted (assessed qualitatively)

**IMPORTANT:** These weights are EXPERIMENTAL and should NOT be used mechanically. They are provided for:

1. Guiding narrative emphasis in reports
2. Informing human judgment about relative importance
3. Potential future aggregate scoring (if validated)

**Current practice:** Assess all 7 signals, report all scores, emphasise appropriate signals in narrative without computing weighted aggregates.

---

## Special Cases

### HARKing-Flagged Papers (Expressed ≠ Revealed Approach)

**Additional Scrutiny:**

When `harking_flag: true` in classification.json:

1. **Assess by revealed approach** (not expressed approach)
2. **Flag methodological alignment issues** in Transparency assessment
3. **Note in credibility report** under "Methodological Considerations"
4. **Apply stricter Validity criteria** (post-hoc patterns framed as confirmatory)

**Example:**

Paper claims to be deductive (hypothesis-testing) but revealed approach is inductive (pattern-finding):

- **Framework:** Use inductive framework (primary: Transparency, Comprehensibility, Generalisability)
- **Transparency:** Downweight score for methodological confusion or misrepresentation
- **Note in report:** "The paper frames exploratory findings using confirmatory language, which reduces methodological transparency and makes it difficult to assess whether hypotheses were specified a priori."

---

### "None Stated" Research Approach

When `expressed_approach: "none_stated"` in classification.json:

1. **Use revealed approach** for framework selection
2. **Trigger Track A monitoring** (medium confidence assessment)
3. **Note in Transparency assessment:** Absence of methodological statement
4. **Contextual interpretation:** Consider publication year, disciplinary norms, journal standards

**Do NOT automatically penalise.** Absence of methodology section may reflect:

- Disciplinary conventions (older publications)
- Journal format constraints (short communications)
- Methodological naivete (genuine weakness)
- Implicit methodology (methods evident from content)

Assess contextually and note in report.

---

### Methodological Papers and Software Papers

**Special consideration:** Papers describing methods or software may not fit standard research approach taxonomy.

**Assessment approach:**

1. **Classify as:** "Methodological" or "Abductive" (method/software as proposed solution)
2. **Emphasise:** Transparency (method documentation), Validity (empirical validation), Reproducibility (code/data for reproduction)
3. **De-emphasise:** Generalisability (method scope should be clearly bounded, but transfer is goal)

**Example:** FAIMS Mobile software paper (ballsun-stanton-et-al-2018):

- **Classification:** Abductive (software as solution to field data collection problem)
- **Primary signals:** Transparency (software documentation), Validity (empirical case studies), Reproducibility (code availability)
- **De-emphasised:** Standard hypothesis testing criteria (category error)

---

## Integration with Track A Quality Gating

Framework selection interacts with Track A quality gating:

**HIGH quality state:**

- Apply full framework with approach-specific anchors
- Assess all 7 signals rigorously
- Use precise scores (within 5-point bands)

**MODERATE quality state:**

- Apply framework with caveats
- Assess all 7 signals with confidence bands (20-point ranges)
- Note classification uncertainty in signal selection

**LOW quality state:**

- Do not apply credibility framework
- Generate Track A report only
- Explain why assessment not viable

See `track-a-quality-criteria.md` for quality gating decision logic.

---

## Related References

- `assessment-pillars.md` - Three pillars framework (Transparency, Credibility, Reproducibility)
- `approach-taxonomy.md` - Research approach definitions
- `signal-definitions-hass.md` - Signal definitions with approach-specific anchors
- `harking-detection-guide.md` - Detecting expressed vs revealed mismatches
- `track-a-quality-criteria.md` - Quality gating for assessments
