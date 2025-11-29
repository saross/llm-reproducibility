# Research Approach Taxonomy for HASS Research

**Purpose:** Define characteristics of inductive, deductive, and abductive research approaches to inform credibility assessment

**Date:** 2025-11-17

---

## Overview

Research approaches in Humanities, Arts, and Social Sciences (HASS) vary in their logical structure, goals, and appropriate credibility criteria. This taxonomy provides a framework for classifying research approaches and understanding how they inform assessment priorities.

**Two-stage classification (v2.1):**

1. **Paper type:** Empirical, methodological, theoretical, or meta-research (see Section: Paper Type Classification)
2. **Research approach:** Deductive, inductive, or abductive (for empirical papers) OR validation approach (for methodological papers)

Different paper types require different assessment frameworks. Determine paper type before classifying research approach.

---

## Three Primary Research Approaches

### Deductive (Hypothesis-Testing, Confirmatory)

**Definition:** Research that tests pre-specified hypotheses against empirical data

**Characteristic Features:**

- **Explicit hypotheses** stated before data analysis
- **Statistical testing** or systematic comparison
- **Falsification logic** (can the hypothesis be rejected?)
- **Confirmatory** research design (stated explicitly or implied by structure)

**Evidence Indicators:**

- Research designs: "hypothesis-testing", "confirmatory", "experimental", "controlled comparison"
- Methods: Statistical tests, systematic sampling for hypothesis testing
- Claims: Framed as hypothesis confirmation/rejection ("we hypothesised X... data support/reject X")
- Structure: Hypotheses in introduction, tests in results, confirmation/rejection in discussion

**Example Research:**

- "We hypothesised that Bronze Age settlements would cluster near water sources. Survey data confirm..."
- Experimental archaeology testing tool efficiency hypotheses
- Comparative studies with a priori predictions

---

### Inductive (Pattern-Finding, Exploratory, Descriptive)

**Definition:** Research that discovers patterns in data without pre-specified hypotheses

**Characteristic Features:**

- **Pattern discovery** from systematic observation
- **Exploratory** research design
- **Descriptive** emphasis (documenting what's there)
- **Hypothesis-generating** rather than hypothesis-testing

**Evidence Indicators:**

- Research designs: "exploratory", "survey", "descriptive", "systematic documentation"
- Methods: Systematic observation, classification, pattern description
- Claims: Pattern descriptions ("settlements concentrate in X locations", "artefact types correlate with Y")
- Structure: Observations → patterns → interpretations (not hypothesis → test → result)

**Example Research:**

- Regional surveys documenting settlement distributions
- Artefact typology studies
- Stratigraphic descriptions and pattern identification
- Grounded theory qualitative research

---

### Abductive (Inference to Best Explanation, Interpretive)

**Definition:** Research that infers explanatory frameworks from observed patterns

**Characteristic Features:**

- **Explanatory inference** (why do we see this pattern?)
- **Comparative assessment** of alternative explanations
- **Theoretical interpretation** of empirical patterns
- **Retroductive reasoning** (from consequence to cause)

**Evidence Indicators:**

- Research designs: "interpretive", "explanatory", "comparative", "case study"
- Methods: Contextual analysis, comparative frameworks, theoretical application
- Claims: Explanatory ("best explanation for X pattern is Y process")
- Structure: Pattern observation → alternative explanations → inference to best explanation

**Example Research:**

- "The distinctive artefact assemblage is best explained by..."
- Landscape interpretation through multiple theoretical lenses
- Historical narrative reconstruction
- Inference of past social processes from material patterns

---

## Mixed-Method Characterisation

**Approach:** Qualitative description, not quantitative percentages

Many HASS papers employ multiple approaches across different research phases or components. Characterise mixed-method research using qualitative descriptions rather than false precision percentages.

**Note:** Methodological papers can also have mixed validation approaches (e.g., theoretical justification + empirical performance testing). Apply the same characterisation principles to validation approach classification.

### Characterisation Template

```yaml
primary_approach: "[dominant approach]"
secondary_approaches: ["[approach 1]", "[approach 2]"]
characterisation: "[qualitative description]"
```

### Examples

**Example 1: Primarily Inductive**

```yaml
primary_approach: "inductive"
characterisation: "Overall inductive exploratory survey. Includes confirmatory statistical analysis of observed patterns as secondary validation."
```

**Example 2: Primarily Abductive**

```yaml
primary_approach: "abductive"
secondary_approaches: ["inductive"]
characterisation: "Primarily interpretive/explanatory. Uses inductively identified material patterns as basis for abductive inference about past social processes."
```

**Example 3: Genuinely Mixed**

```yaml
primary_approach: "mixed_deductive_inductive"
characterisation: "Phase 1: Deductive hypothesis testing through experimental archaeology (tool efficiency). Phase 2: Inductive pattern discovery in archaeological assemblages to identify tool use traces. Appropriately mixed design with clear phase separation."
```

**AVOID:**

- Percentage precision ("60% inductive, 40% deductive") - implies false precision
- Rigid categorisation where flexibility is appropriate
- Forcing papers into single category when mixed is more accurate

---

## Absence of Expressed Methodology

### Critical Principle: "No Expressed Method = Significant"

If **no methodological approach is stated**, this is **meaningful information**:

```yaml
expressed_approach: "none_stated"
significance: "No explicit methodological framework stated. Indicates potential methodological naivete, weak research design, or implicit assumptions about appropriate methods for the discipline."
transparency_implication: "Lack of explicit research design statement reduces transparency and makes it difficult to assess methodological appropriateness."
```

### Context-Sensitive Interpretation (v2.0 Enhancement)

The absence of an expressed methodology should be interpreted contextually, not automatically penalised:

**Consider:**

- **Publication year:** Older publications may follow different methodological norms
- **Discipline conventions:** Some disciplines historically assumed implicit methodologies
- **Journal standards:** Field-specific journals may not require explicit method statements
- **Paper type:** Methodological papers, software papers, short communications may differ

**Do NOT:**

- Strain to find an expressed approach where none exists
- Assume unstated = inductive (could be unstated deductive or unstated abductive)
- Treat absence as irrelevant
- Automatically penalise all "none_stated" cases equally

**DO:**

- Document absence explicitly in classification
- Flag as transparency/design consideration (not necessarily weakness)
- Evaluate in context (compare to contemporary disciplinary norms)
- Note in credibility assessment (affects Transparency signal interpretation)
- Trigger Track A quality monitoring (medium confidence classification)

---

## Paper Type Classification (v2.1)

### Critical Principle: Paper Type Determines Assessment Framework

Not all research papers investigate substantive empirical questions. Some papers present methods themselves, synthesise theory, or study research practices. **Paper type must be determined before research approach classification.**

### Four Paper Types

#### Type 1: Empirical Research Papers

**Definition:** Papers that use methods to investigate substantive research questions about phenomena in the world

**Characteristic Features:**

- Research question targets phenomena (not methods/theory themselves)
- Claims describe, explain, or predict phenomena
- Methods are tools for investigation (not the subject of investigation)

**Examples:**

- Archaeological surveys documenting settlement patterns
- Ethnographic studies of community practices
- Palaeoecological reconstructions of past environments
- Historical analyses of social change

**Classification:** Use standard deductive/inductive/abductive taxonomy

**Credibility emphasis:** All seven signals relevant

---

#### Type 2: Methodological Papers

**Definition:** Papers that present, develop, validate, or compare research methods, tools, protocols, or frameworks

**Characteristic Features:**

- Primary contribution is the method itself (not findings from using it)
- Claims are about method properties (capabilities, advantages, limitations)
- If empirical application included, it's demonstrative/illustrative (not the main contribution)
- "Results" section describes method performance (not substantive findings)

**Methodological Subtypes:**

1. **Software tools:** Platforms, applications, analytical software
2. **Analytical methods:** Statistical techniques, computational algorithms, data processing methods
3. **Field protocols:** Data collection procedures, sampling strategies, documentation systems
4. **Theoretical frameworks:** Conceptual models, interpretive frameworks, taxonomies

**Examples:**

- ballsun-stanton-et-al-2018: FAIMS Mobile software platform for field research
- Papers presenting new radiocarbon calibration methods
- Studies proposing new artefact classification frameworks
- Guides to field survey protocols

**Classification:**

- **Paper type:** "methodological"
- **Validation approach:** Classify how the method is presented/validated (inductive/deductive/abductive/mixed/none)
  - Inductive validation: Descriptive demonstration through case examples
  - Deductive validation: Hypothesis-testing of method performance
  - Abductive validation: Inference about method appropriateness
  - None: Pure technical specification without validation

**Credibility emphasis:**

- **Primary signals:** Transparency (design decisions documented), Reproducibility (method reproducible), Comprehensibility (clear specification)
- **Secondary signals:** Validity (of claims about method properties), Plausibility (of method rationale)
- **Deemphasised:** Generalisability (of demonstration cases), Robustness (of substantive findings - not applicable)

**Critical distinction:** A paper USING a new method to study phenomena (with method development as secondary contribution) is EMPIRICAL with mixed approach. A paper PRESENTING a new method (with demonstration as illustrative) is METHODOLOGICAL.

---

#### Type 3: Theoretical/Review Papers

**Definition:** Papers that synthesise literature, develop theory, or provide conceptual frameworks without new empirical data

**Characteristic Features:**

- No new empirical data collection
- Synthesis of existing research
- Theoretical development or conceptual framework building
- Systematic reviews, meta-analyses, theoretical arguments

**Examples:**

- Literature reviews synthesising settlement pattern research
- Theoretical papers on social complexity
- Meta-analyses of radiocarbon dates
- Conceptual frameworks for landscape archaeology

**Classification:**

- **Paper type:** "theoretical"
- **Theory approach:** Classify how theory is developed/tested
  - Deductive: Testing theoretical predictions against existing evidence
  - Abductive: Building theory from synthesis of patterns
  - Inductive: Systematic aggregation to identify meta-patterns

**Credibility emphasis:** Comprehensibility, Plausibility, Transparency (of selection criteria, synthesis logic)

**Note:** Systematic reviews with meta-analysis may have deductive components (hypothesis-testing across studies)

---

#### Type 4: Meta-Research Papers

**Definition:** Papers that study research practices, methodologies, or scientific processes themselves

**Characteristic Features:**

- Research papers are the data
- Questions about how research is conducted, reported, or assessed
- May include scientometrics, reproducibility studies, methodological critiques

**Examples:**

- Studies of reporting practices in archaeology
- Reproducibility assessments of published analyses
- Bibliometric analyses of research trends
- Studies of research infrastructure adoption

**Classification:** Often requires mixed classification (empirical study OF research practices)

**Credibility emphasis:** Depends on specific design (use empirical or methodological framework as appropriate)

---

### Paper Type Decision Tree

**Question 1:** Does the paper collect or analyse new empirical data about phenomena (not methods)?

- **YES** → Type 1: Empirical
- **NO** → Continue to Question 2

**Question 2:** Is the primary contribution a method, tool, protocol, or framework?

- **YES** → Type 2: Methodological
- **NO** → Continue to Question 3

**Question 3:** Does the paper synthesise existing research or develop theory?

- **YES** → Type 3: Theoretical/Review
- **NO** → Continue to Question 4

**Question 4:** Does the paper study research practices or scientific processes?

- **YES** → Type 4: Meta-research
- **NO** → **TAXONOMY GAP - Propose new category (see Section 2.5)**

---

### Validation Approach Classification (For Methodological Papers)

When classifying Type 2 (Methodological) papers, classify the **validation approach** rather than substantive research approach:

**How is the method presented and validated in the paper?**

**Inductive/Descriptive validation:**

- Method demonstrated through illustrative case examples
- Descriptive presentation of method capabilities
- No hypothesis-testing of method performance
- Example: FAIMS paper shows software features through case studies

**Deductive/Hypothesis-testing validation:**

- Explicit hypotheses about method performance
- Systematic testing against performance criteria
- Comparative evaluation with pre-specified predictions
- Example: New calibration method tested against known-age samples

**Abductive/Inference-based validation:**

- Method justified through inference to best design
- Theoretical argumentation for method appropriateness
- Comparative assessment of design alternatives
- Example: Framework proposed as best explanation for classification needs

**Mixed validation:**

- Combines multiple validation strategies
- Example: Theoretical justification + illustrative examples + performance testing

**None (Technical specification only):**

- Pure technical documentation
- No validation or demonstration provided
- Rare in published research (more common in grey literature)

---

## Taxonomy Evolution and Feedback (v2.1)

### Taxonomy Status: Under Iterative Development

This taxonomy (v2.1) represents current understanding based on papers encountered to date. **It is expected to evolve through testing and application.**

### Feedback Mechanism: When Existing Categories Don't Fit

**During classification, you may encounter papers that don't fit existing categories well.** This is valuable information for taxonomy refinement.

**When existing categories feel inadequate:**

1. **Choose the closest existing category** (don't fail classification)
2. **Document the poor fit** using taxonomy_feedback object
3. **Propose a new category** with detailed rationale
4. **Continue with classification** using closest available framework

### Criteria for Proposing New Paper Types

**Propose a new category when:**

- Paper has characteristics fundamentally different from existing 4 types
- Classification requires extensive qualifications/caveats that undermine utility
- Paper serves a purpose not captured by existing taxonomy
- You can identify 2+ papers in corpus that would fit the new category
- New category would have distinct credibility criteria

**Do NOT propose new categories for:**

- Minor variations within existing types (handle with subtypes or notes)
- Single unique paper (handle as edge case in closest category)
- Disciplinary variations of existing types (note in justification)

### Example Potential Categories (To Watch For)

**Comparative Methods Papers:**

- Systematic comparison of 2+ existing methods
- Distinct from methodological papers (which present single method)
- Distinct from empirical papers (methods are subject, not tools)
- Credibility criteria: Fair comparison, appropriate evaluation metrics

**Data Papers:**

- Present new datasets without extensive analysis
- Increasingly common with open data movement
- Distinct from empirical (no research question) and methodological (data not a method)
- Credibility criteria: Documentation quality, accessibility, completeness

**Replication Studies:**

- Reproduce published analyses to assess replicability
- Distinct from meta-research (focus on specific study) and empirical (no new data)
- Credibility criteria: Fidelity to original, transparency about deviations

**Null Result Papers:**

- Report negative or inconclusive findings
- May have specific reporting practices distinct from positive findings
- Credibility criteria: Evidence of adequate power, transparency about stopping rules

### Taxonomy Feedback Object Structure

```json
"taxonomy_feedback": {
  "category_fit_quality": "excellent|good|acceptable|poor",
  "proposed_new_category": "string or null",
  "rationale_for_proposal": "Why existing taxonomy inadequate",
  "characteristics_of_proposed_category": "Defining features of proposed category",
  "alternative_papers_that_might_fit": ["Papers in corpus that might share this category"]
}
```

### Your Role in Taxonomy Development

**During Phase 1 testing (v2.1-alpha):**

- You are helping identify taxonomy gaps
- Honest assessment of category fit is valuable
- Proposing new categories improves the system
- User reviews proposals and refines taxonomy between test cycles

**Expected outcomes:**

- Most papers will fit existing 4 types (excellent/good fit)
- 10-20% may have acceptable fit with caveats
- 0-5% may have poor fit requiring new categories

**After taxonomy stabilises (v2.2+):**

- Poor fit becomes rarer (taxonomy covers observed variation)
- Feedback mechanism remains for genuinely novel paper types
- Established taxonomy enables consistent assessment

---

## Integration with Credibility Assessment

### Approach-Specific Assessment Emphasis

Different research approaches require different credibility assessment priorities:

**For Deductive Research:**

- **Emphasise:** Validity (evidence adequacy for hypothesis tests), Robustness (sensitivity to analytical choices), Reproducibility (code/data for reproduction)
- **Key questions:** Were hypotheses specified a priori? Are tests appropriate? Are alternative hypotheses considered?

**For Inductive Research:**

- **Emphasise:** Transparency (research design clarity), Comprehensibility (pattern descriptions), Generalisability (appropriate scope)
- **Key questions:** Is sampling systematic? Are patterns representative? Are limitations acknowledged?

**For Abductive Research:**

- **Emphasise:** Plausibility (explanatory coherence), Validity (adequacy of evidence for inference), Robustness (alternative explanations considered)
- **Key questions:** Are alternative explanations compared? Is inference well-grounded? Is theoretical framework appropriate?

---

## Related References

- `harking-detection-guide.md` - Detecting mismatches between expressed and revealed approaches
- `signal-definitions-hass.md` - repliCATS Seven Signals adapted for HASS with approach-specific anchors
- `assessment-frameworks.md` - Signal emphasis and framework selection logic by research approach
