# Research Approach Classification Framework
## Expressed vs Revealed Methodology with HARKing Detection

**Document Purpose:** Framework for classifying research approach (inductive/deductive/abductive) with awareness of stated vs actual methodology

**Date Created:** 2025-11-16
**Status:** Implementation-ready framework
**Phase:** Pre-credibility assessment (Pass 6.5 or early Pass 7)

---

## Executive Summary

### Key Principles

1. **Classification timing:** After extraction complete (Pass 6), before credibility assessment (Pass 7)
2. **Dual classification:** Expressed approach (what paper says) vs Revealed approach (what paper does)
3. **HARKing detection:** Flag mismatches between expressed and revealed approaches
4. **No expressed method is significant:** Absence of methodological statement indicates naivete/weak research design
5. **Mixed-method flexibility:** Qualitative descriptions, not false precision percentages
6. **Iterative refinement:** Learn classification patterns across corpus

---

## Classification Taxonomy

### Three Primary Research Approaches

#### Deductive (Hypothesis-Testing, Confirmatory)

**Definition:** Research that tests pre-specified hypotheses against empirical data

**Characteristic Features:**
- **Explicit hypotheses** stated before data analysis
- **Statistical testing** or systematic comparison
- **Falsification logic** (can the hypothesis be rejected?)
- **Confirmatory** research design (stated explicitly or implied by structure)

**Evidence from Extraction:**
- Research designs: "hypothesis-testing", "confirmatory", "experimental", "controlled comparison"
- Methods: Statistical tests, systematic sampling for hypothesis testing
- Claims: Framed as hypothesis confirmation/rejection ("we hypothesised X... data support/reject X")
- Structure: Hypotheses in introduction, tests in results, confirmation/rejection in discussion

**Example Papers:**
- "We hypothesised that Bronze Age settlements would cluster near water sources. Survey data confirm..."
- Experimental archaeology testing tool efficiency hypotheses
- Comparative studies with a priori predictions

---

#### Inductive (Pattern-Finding, Exploratory, Descriptive)

**Definition:** Research that discovers patterns in data without pre-specified hypotheses

**Characteristic Features:**
- **Pattern discovery** from systematic observation
- **Exploratory** research design
- **Descriptive** emphasis (documenting what's there)
- **Hypothesis-generating** rather than hypothesis-testing

**Evidence from Extraction:**
- Research designs: "exploratory", "survey", "descriptive", "systematic documentation"
- Methods: Systematic observation, classification, pattern description
- Claims: Pattern descriptions ("settlements concentrate in X locations", "artifact types correlate with Y")
- Structure: Observations → patterns → interpretations (not hypothesis → test → result)

**Example Papers:**
- Regional surveys documenting settlement distributions
- Artifact typology studies
- Stratigraphic descriptions and pattern identification
- Grounded theory qualitative research

---

#### Abductive (Inference to Best Explanation, Interpretive)

**Definition:** Research that infers explanatory frameworks from observed patterns

**Characteristic Features:**
- **Explanatory inference** (why do we see this pattern?)
- **Comparative assessment** of alternative explanations
- **Theoretical interpretation** of empirical patterns
- **Retroductive reasoning** (from consequence to cause)

**Evidence from Extraction:**
- Research designs: "interpretive", "explanatory", "comparative", "case study"
- Methods: Contextual analysis, comparative frameworks, theoretical application
- Claims: Explanatory ("best explanation for X pattern is Y process")
- Structure: Pattern observation → alternative explanations → inference to best explanation

**Example Papers:**
- "The distinctive artifact assemblage is best explained by..."
- Landscape interpretation through multiple theoretical lenses
- Historical narrative reconstruction
- Inference of past social processes from material patterns

---

## Classification Process (Pass 6.5 or Early Pass 7)

### Step 1: Extract Expressed Approach

**Sources:**
- **Introduction/Background:** Methodological statements, research questions, stated aims
- **Methods section:** Explicit design statements ("this study employs an exploratory approach")
- **Research Designs (from RDMAP):** Extracted design types

**Key Phrases to Detect:**

**Deductive indicators:**
- "We hypothesised that..."
- "To test the hypothesis..."
- "Confirmatory analysis"
- "We predicted..."
- "Experimental design"

**Inductive indicators:**
- "Exploratory study"
- "To document patterns of..."
- "Systematic survey"
- "Descriptive analysis"
- "To identify..."

**Abductive indicators:**
- "To explain..."
- "Inference to best explanation"
- "Interpretive framework"
- "To understand why..."
- "Comparative case study"

**CRITICAL: Absence of Expressed Approach**

If **no methodological approach is stated**, this is **meaningful information**:

```yaml
expressed_approach: "none_stated"
significance: "No explicit methodological framework stated. Indicates potential methodological naivete, weak research design, or implicit assumptions about appropriate methods for the discipline."
transparency_implication: "Lack of explicit research design statement reduces transparency and makes it difficult to assess methodological appropriateness."
```

**Do NOT:**
- Strain to find an expressed approach where none exists
- Assume unstated = inductive (could be unstated deductive or unstated abductive)
- Treat absence as irrelevant

**DO:**
- Document absence explicitly
- Flag as transparency/design weakness in Track A assessment
- Note in credibility assessment (affects Transparency signal score)

---

### Step 2: Determine Revealed Approach

**Sources:**
- **What the paper actually does** (independent of what it says it does)
- Extracted claims structure
- Extracted methods and their use
- Evidence-claim relationships
- Analytical workflow

**Analysis Questions:**

**Deductive indicators (revealed):**
- Are claims framed as hypothesis tests?
- Are methods applied to test predictions?
- Is there a priori specification of expected patterns?
- Is analysis structured as confirmation/falsification?

**Inductive indicators (revealed):**
- Are claims descriptive of observed patterns?
- Are methods exploratory or systematic observation?
- Is analysis pattern-finding rather than hypothesis-testing?
- Are interpretations generated from data rather than tested against data?

**Abductive indicators (revealed):**
- Are claims explanatory ("X explains Y")?
- Are alternative explanations explicitly compared?
- Is reasoning retroductive (from effect to cause)?
- Is interpretation theoretical/contextual rather than statistical?

**Example Analysis:**

```yaml
# Example: Paper claims to be "hypothesis-testing" but actually pattern-finding

expressed_approach: "deductive"
expressed_evidence:
  - "We hypothesised that settlement size correlates with agricultural productivity"
  - Methods section uses term "hypothesis-testing"

revealed_approach: "inductive"
revealed_evidence:
  - No a priori hypothesis stated in introduction
  - Survey conducted first, patterns observed post-hoc
  - "Hypothesis" appears only in discussion as post-hoc interpretation
  - Methods are exploratory survey, not designed to test specific prediction
  - Claims are pattern descriptions, not hypothesis tests

mismatch: true
mismatch_type: "HARKing_potential"
mismatch_explanation: "Paper frames post-hoc pattern observations as hypothesis tests. Actual research design is exploratory survey with pattern discovery, but results are presented using hypothesis-testing rhetoric. Potential unintentional HARKing (Hypothesising After Results are Known)."
```

---

### Step 3: Compare Expressed vs Revealed

**Three Outcomes:**

#### Outcome A: Alignment (Expressed = Revealed)
```yaml
expressed_approach: "inductive"
revealed_approach: "inductive"
alignment: "matched"
confidence: "high"
justification: "Paper explicitly states exploratory design and actually conducts exploratory research. Methodological transparency high."
```

#### Outcome B: Partial Mismatch (Mixed Methods)
```yaml
expressed_approach: "mixed_deductive_inductive"
revealed_approach: "primarily_inductive_with_deductive_components"
alignment: "partial"
qualifications:
  - "Overall inductive survey design"
  - "Includes confirmatory statistical analysis of observed patterns (chi-square tests)"
  - "Deductive element is secondary validation of inductively discovered patterns"
justification: "Paper accurately represents mixed-method approach. Primary phase is inductive pattern discovery; secondary phase is statistical testing of observed patterns. Appropriate mixed design."
```

#### Outcome C: Clear Mismatch (HARKing Risk)
```yaml
expressed_approach: "deductive"
revealed_approach: "inductive"
alignment: "mismatched"
mismatch_type: "HARKing_risk"
harking_flag: true
confidence: "medium-high"
justification: "Paper uses hypothesis-testing rhetoric but shows no evidence of a priori hypothesis specification. Survey design is exploratory, patterns discovered post-hoc, then framed as hypothesis confirmations. Likely unintentional HARKing - presenting exploratory findings using confirmatory language to fit publication norms."
transparency_concern: "High - methodological confusion or deliberate reframing reduces transparency and makes it difficult to assess actual research quality."
```

---

### Step 4: Mixed-Method Characterisation

**Approach:** Qualitative description, not quantitative percentages

**Template:**
```yaml
primary_approach: "[dominant approach]"
secondary_approaches: ["[approach 1]", "[approach 2]"]
characterisation: "[qualitative description]"
section_breakdown: # Optional, if helpful
  - section: "Survey design and data collection"
    approach: "inductive"
  - section: "Statistical analysis of survey patterns"
    approach: "deductive"
  - section: "Landscape interpretation"
    approach: "abductive"
```

**Examples:**

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

## Classification Output Schema

```yaml
research_approach_classification:
  # Timing
  classified_after_pass: 6
  classification_date: "2025-11-16"

  # Expressed Approach
  expressed_approach: "deductive|inductive|abductive|mixed|none_stated"
  expressed_evidence:
    - "Quote or paraphrase from paper stating approach"
    - "Research design extracted from RDMAP"
  expressed_source_sections: ["introduction", "methods"]

  # Revealed Approach (Actual)
  revealed_approach: "deductive|inductive|abductive|mixed"
  revealed_evidence:
    claims_structure: "Pattern descriptions, not hypothesis tests"
    methods_application: "Exploratory survey methodology"
    analytical_workflow: "Pattern discovery → interpretation, not hypothesis → test → confirmation"
  revealed_confidence: "high|medium|low"

  # Comparison
  expressed_vs_revealed: "matched|partial|mismatched"

  # If mismatched
  harking_flag: true|false
  mismatch_type: "HARKing_potential|methodological_confusion|disciplinary_convention|legitimately_mixed"
  mismatch_explanation: "Detailed explanation of discrepancy"

  # Mixed-Method Characterisation (if applicable)
  primary_approach: "inductive"
  secondary_approaches: ["deductive"]
  qualifications:
    - "Overall inductive in design"
    - "Includes reproducible statistical analysis of observed patterns"
    - "Statistical tests are post-hoc validation, not a priori hypothesis tests"

  # Methodological Transparency Assessment
  transparency_quality: "high|moderate|low"
  transparency_notes: "Explicit research design statement present|Implicit design, must be inferred|No methodological framework stated"

  # Justification
  classification_justification: |
    Detailed narrative explaining classification decisions, evidence consulted,
    and confidence in classification. Should cite specific claims, methods,
    and research designs from extraction.

  # Implications for Credibility Assessment
  credibility_framework_to_use: "deductive_emphasis|inductive_emphasis|abductive_emphasis|mixed_assessment"
  signal_prioritisation:
    primary_signals: ["transparency", "validity", "generalisability"]
    secondary_signals: ["robustness", "replicability"]
    deemphasised_signals: []
```

---

## Integration with Credibility Assessment

### How Classification Informs Assessment

**For Deductive Research:**
- **Emphasise:** Validity (evidence adequacy for hypothesis tests), Robustness (sensitivity to analytical choices), Replicability (code/data for reproduction)
- **Key questions:** Were hypotheses specified a priori? Are tests appropriate? Are alternative hypotheses considered?

**For Inductive Research:**
- **Emphasise:** Transparency (research design clarity), Comprehensibility (pattern descriptions), Generalisability (appropriate scope)
- **Key questions:** Is sampling systematic? Are patterns representative? Are limitations acknowledged?

**For Abductive Research:**
- **Emphasise:** Plausibility (explanatory coherence), Validity (adequacy of evidence for inference), Robustness (alternative explanations considered)
- **Key questions:** Are alternative explanations compared? Is inference well-grounded? Is theoretical framework appropriate?

**For HARKing-Flagged Papers:**
- **Additional scrutiny:** Transparency assessment (was design appropriate for claims?), Validity (are post-hoc patterns treated as confirmatory evidence inappropriately?)
- **Note in report:** Methodological alignment issues should be explicitly discussed

---

## Implementation Plan

### Step 1: Build Classifier (1-2 hours)

**Action:** Create classification prompt/workflow that:
1. Reads extracted RDMAP, claims, methods
2. Searches for expressed approach statements
3. Analyses revealed approach from actual content
4. Compares expressed vs revealed
5. Outputs structured classification

**Tool:** Claude autonomous workflow (not Python script)

**Output:** Structured YAML classification appended to extraction.json or separate classification.json

---

### Step 2: Test Classifier (1-2 hours)

**Action:** Run classifier on 3 diverse papers:
- **Paper 1:** Well-aligned (expressed = revealed) - e.g., sobotkova-et-al-2024
- **Paper 2:** Mixed-method - e.g., ballsun-stanton-et-al-2018 (software development + empirical validation)
- **Paper 3:** Potential mismatch - TBD from corpus

**Validation:** Manual review of classifications - do they make sense?

---

### Step 3: Refine Heuristics (ongoing)

**Action:** As we classify more papers, document:
- Common patterns (what indicates inductive vs deductive in archaeology?)
- Edge cases (hard-to-classify papers)
- Disciplinary conventions (is "survey" always inductive? Not necessarily)
- HARKing indicators (what signals post-hoc hypothesis framing?)

**Output:** Refined classification guidance

---

### Step 4: Integrate with Credibility Assessment (next phase)

**Action:** Use classification to:
- Select appropriate credibility assessment framework
- Prioritise relevant signals
- Contextualise assessment (inductive research shouldn't be judged by deductive standards)

---

## Validation and Quality Tracking (Track A)

### Track A: Classifier Quality Assessment

**Questions to monitor:**
1. **Consistency:** Do multiple classifications of same paper agree?
2. **Face validity:** Do classifications match expert intuitions?
3. **Completeness:** Are all necessary fields populated?
4. **Justification quality:** Are classifications well-explained?

**Quality indicators:**
- Classification confidence scores
- Presence of supporting evidence for classifications
- Explicit handling of "none_stated" cases
- Clear justification narratives

**Tracking approach:**
- Document classification decisions in planning/classification-log.md
- Note difficult cases and resolution
- Build empirical understanding of corpus patterns

---

## Examples from Corpus (Predicted Classifications)

### sobotkova-et-al-2024 (Journal of Documentation)
```yaml
expressed_approach: "mixed"
revealed_approach: "primarily_inductive"
characterisation: "Primarily inductive systematic survey documentation with quantitative description of patterns. Includes some deductive elements in statistical analysis."
alignment: "matched"
```

### ballsun-stanton-et-al-2018 (SoftwareX)
```yaml
expressed_approach: "mixed_development_empirical"
revealed_approach: "abductive_and_inductive"
characterisation: "Software development (design inference) combined with empirical validation through field use. Mixed methodological paper."
alignment: "partial"
note: "Software development papers may not fit cleanly into deductive/inductive/abductive taxonomy - may need 'methodological/development' category"
```

### penske-et-al-2023 (Nature)
```yaml
expressed_approach: "deductive"
revealed_approach: "deductive"
characterisation: "Hypothesis-testing genomic analysis. Clear a priori predictions, systematic testing, confirmatory design."
alignment: "matched"
```

---

## Document Status

**Version:** 1.0 (implementation-ready)
**Next Update:** After testing classifier on 3 papers
**Related Documents:**
- `planning/paper-credibility-analysis-framework.md` (parent framework)
- `planning/active-todo-list.md` (Task 10.2, implementation tracking)
- `docs/background-research/replicats-seven-signals-hass-adaptation.md` (credibility signals)

**Implementation Priority:** HIGH (foundational for credibility assessment)
