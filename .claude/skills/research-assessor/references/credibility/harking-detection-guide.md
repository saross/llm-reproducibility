# HARKing Detection Guide: Expressed vs Revealed Methodology Comparison

**Purpose:** Guide detection of mismatches between stated research approach and actual research conduct

**Date:** 2025-11-17

---

## Overview

**HARKing** (Hypothesising After Results are Known) occurs when researchers frame post-hoc observations as confirmatory hypothesis tests. This represents a methodological transparency issue that affects credibility assessment.

This guide provides a framework for detecting expressed vs revealed methodology mismatches through systematic comparison of what papers say they do versus what they actually do.

---

## Core Concepts

### Expressed Approach

**Definition:** The research approach stated or implied in the paper's methodological statements

**Sources:**

- Introduction/Background methodological statements
- Research questions and stated aims
- Methods section design declarations
- Extracted research designs from RDMAP

**Key Phrases:**

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

---

### Revealed Approach

**Definition:** The research approach actually conducted, inferred from what the paper does (independent of what it says)

**Sources:**

- Extracted claims structure
- Extracted methods and their application
- Evidence-claim relationships
- Analytical workflow
- Results presentation structure

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

---

## HARKing Detection Process

### Step 1: Extract Expressed Approach

**Search for explicit methodological statements:**

1. Read Introduction/Background for research aims and design statements
2. Read Methods section for design type declarations
3. Review extracted RDMAP research designs
4. Document expressed approach with supporting quotes

**Output:**

```yaml
expressed_approach: "deductive|inductive|abductive|mixed|none_stated"
expressed_evidence:
  - "Quote from paper stating approach"
  - "Research design from RDMAP"
expressed_source_sections: ["introduction", "methods"]
```

**CRITICAL: "None Stated" Cases**

If no methodological approach is stated:

```yaml
expressed_approach: "none_stated"
significance: "No explicit methodological framework stated. Indicates potential methodological naivete, weak research design, or implicit assumptions about appropriate methods for the discipline."
```

**Do NOT:**

- Strain to find an expressed approach where none exists
- Assume unstated = inductive
- Treat absence as irrelevant

**DO:**

- Document absence explicitly
- Flag for Track A monitoring
- Interpret contextually (see approach-taxonomy.md)

---

### Step 2: Determine Revealed Approach

**Analyse what the paper actually does:**

1. Review claims structure: Are they hypotheses, patterns, or explanations?
2. Analyse methods application: Exploratory, confirmatory, or interpretive?
3. Examine evidence-claim relationships: Testing, discovering, or explaining?
4. Assess analytical workflow: Pre-specified or emergent?

**Output:**

```yaml
revealed_approach: "deductive|inductive|abductive|mixed"
revealed_evidence:
  claims_structure: "Pattern descriptions, not hypothesis tests"
  methods_application: "Exploratory survey methodology"
  analytical_workflow: "Pattern discovery → interpretation, not hypothesis → test → confirmation"
revealed_confidence: "high|medium|low"
```

**Example Analysis:**

```yaml
# Paper claims hypothesis-testing but actually pattern-finding

revealed_approach: "inductive"
revealed_evidence:
  claims_structure: "Descriptive pattern claims ('settlements concentrate in X'), not hypothesis tests"
  methods_application: "Systematic survey with no pre-specified predictions"
  analytical_workflow: "Survey → observe patterns → interpret patterns (inductive sequence)"
  structure_analysis: "'Hypothesis' appears only in discussion, after results presented"
revealed_confidence: "high"
```

---

### Step 3: Compare Expressed vs Revealed

**Three Possible Outcomes:**

#### Outcome A: Alignment (Expressed = Revealed)

```yaml
expressed_approach: "inductive"
revealed_approach: "inductive"
expressed_vs_revealed: "matched"
harking_flag: false
confidence: "high"
justification: "Paper explicitly states exploratory design and actually conducts exploratory research. Methodological transparency high."
```

**No special action required.** Proceed with credibility assessment using appropriate framework.

---

#### Outcome B: Partial Mismatch (Mixed Methods)

```yaml
expressed_approach: "mixed_deductive_inductive"
revealed_approach: "primarily_inductive_with_deductive_components"
expressed_vs_revealed: "partial"
harking_flag: false
mismatch_type: "legitimately_mixed"
qualifications:
  - "Overall inductive survey design"
  - "Includes confirmatory statistical analysis of observed patterns (chi-square tests)"
  - "Deductive element is secondary validation of inductively discovered patterns"
justification: "Paper accurately represents mixed-method approach. Primary phase is inductive pattern discovery; secondary phase is statistical testing of observed patterns. Appropriate mixed design."
```

**Action:** Assess using mixed-method framework (see assessment-frameworks.md). Note methodological complexity but do not penalise transparency.

---

#### Outcome C: Clear Mismatch (HARKing Risk)

```yaml
expressed_approach: "deductive"
revealed_approach: "inductive"
expressed_vs_revealed: "mismatched"
mismatch_type: "HARKing_potential"
harking_flag: true
confidence: "medium-high"
justification: "Paper uses hypothesis-testing rhetoric but shows no evidence of a priori hypothesis specification. Survey design is exploratory, patterns discovered post-hoc, then framed as hypothesis confirmations. Likely unintentional HARKing - presenting exploratory findings using confirmatory language to fit publication norms."
transparency_concern: "High - methodological confusion or deliberate reframing reduces transparency and makes it difficult to assess actual research quality."
```

**Action:**

1. Flag for additional scrutiny in credibility assessment
2. Downweight Transparency score
3. Assess using revealed approach framework (not expressed)
4. Note methodological alignment issue in credibility report

---

## Mismatch Types

### Type 1: HARKing Potential (Unintentional)

**Pattern:** Exploratory research framed using confirmatory language

**Indicators:**

- "Hypothesis" appears only after results presented
- Survey or exploratory design with post-hoc "hypotheses"
- No evidence of a priori prediction
- Statistical tests applied to exploratory findings

**Likely cause:** Publication pressure ("journals prefer hypothesis-testing")

**Severity:** Moderate transparency concern

**Example:**

> Paper conducts regional survey, observes settlement clustering near rivers, then states "we hypothesised settlements would cluster near water." The "hypothesis" was generated from the data, not tested against it.

---

### Type 2: Methodological Confusion

**Pattern:** Researcher genuinely confused about research design

**Indicators:**

- Mixed use of exploratory and confirmatory terminology
- Inconsistent framing across sections
- Methods don't match stated aims
- Analytical workflow doesn't match design claims

**Likely cause:** Methodological naivete or weak training

**Severity:** Moderate to high transparency concern

**Example:**

> Paper claims "exploratory descriptive study" but applies statistical hypothesis tests without clear rationale. Unclear whether testing pre-specified hypotheses or applying tests to exploratory findings.

---

### Type 3: Disciplinary Convention

**Pattern:** Discipline uses confirmatory language for exploratory work

**Indicators:**

- Consistent with disciplinary publication norms
- Temporal pattern (older publications more likely)
- Journal-specific conventions
- Widespread in field

**Likely cause:** Disciplinary tradition, not intentional misrepresentation

**Severity:** Low transparency concern (contextual interpretation)

**Example:**

> Archaeological survey papers routinely use "research questions" language that sounds hypothesis-like but actually guides exploratory investigation. This is disciplinary convention, not HARKing.

---

### Type 4: Legitimately Mixed Methods

**Pattern:** Genuinely combined approaches with clear phase separation

**Indicators:**

- Explicit mixed-method design statement
- Clear phase/component separation
- Appropriate methods for each phase
- Transparent integration of components

**Likely cause:** Appropriate research design

**Severity:** No transparency concern

**Example:**

> Phase 1: Exploratory survey documents settlement distribution. Phase 2: Deductive statistical testing of spatial clustering hypothesis generated from Phase 1 patterns. Explicitly stated as two-phase design.

---

## Assessment Integration

### Impact on Credibility Assessment

**When `harking_flag: true`:**

1. **Use revealed approach framework** (not expressed) for signal emphasis
2. **Downweight Transparency signal** (methodological alignment issue)
3. **Apply stricter Validity criteria** (post-hoc patterns treated as confirmatory?)
4. **Note in credibility report** under "Methodological Considerations"

**Transparency Penalty:**

- **HARKing potential:** Reduce Transparency score by 10-20 points
- **Methodological confusion:** Reduce Transparency score by 15-25 points
- **Disciplinary convention:** Note but do not penalise (context-dependent)
- **Legitimately mixed:** No penalty (appropriate design)

---

### Example HARKing Detection and Assessment

**Paper:** "Bronze Age Settlement Clustering Study"

**Step 1: Expressed Approach**

```yaml
expressed_approach: "deductive"
expressed_evidence:
  - "We hypothesised that Bronze Age settlements would cluster within 2km of major rivers"
  - Methods section: "hypothesis-testing design"
```

**Step 2: Revealed Approach**

```yaml
revealed_approach: "inductive"
revealed_evidence:
  claims_structure: "Descriptive: 'settlements concentrate near rivers'"
  methods_application: "Systematic regional survey, no pre-specified distance threshold"
  analytical_workflow: "Survey → map settlements → observe clustering → calculate mean distance to rivers → frame as 'hypothesis confirmation'"
  critical_observation: "'Hypothesis' first appears in Discussion section, after all results presented"
revealed_confidence: "high"
```

**Step 3: Comparison**

```yaml
expressed_vs_revealed: "mismatched"
mismatch_type: "HARKing_potential"
harking_flag: true
mismatch_explanation: "Paper frames post-hoc pattern observation as hypothesis test. Survey was exploratory; '2km threshold' was derived from observed data, not predicted a priori. Actual research is inductive (pattern discovery) presented using deductive rhetoric (hypothesis confirmation)."
```

**Step 4: Assessment Impact**

- **Framework:** Use inductive framework (Transparency, Comprehensibility, Generalisability primary)
- **Transparency:** Score reduced from potential 70 to 55 (15-point penalty for methodological confusion)
- **Note in report:** "Methodological alignment concern: research framed as hypothesis-testing but actually exploratory pattern-finding. Reduces transparency and makes it difficult to assess whether analytical choices were pre-specified or data-driven."

---

## Quality Considerations

### When to Flag HARKing

**Flag when:**

- Clear mismatch between expressed and revealed approaches
- "Hypothesis" appears only after results
- Exploratory methods with confirmatory framing
- Post-hoc statistical tests framed as a priori predictions

**Do NOT flag when:**

- Mixed methods with clear phase separation
- Disciplinary convention (exploratory "research questions")
- Abductive inference (explanatory, not confirmatory)
- Hypothesis refinement explicitly acknowledged

---

### Confidence in HARKing Detection

**High confidence:**

- Clear temporal sequence evidence (hypothesis stated after results)
- Explicit mismatch between design and claims
- Multiple indicators converge

**Medium confidence:**

- Some indicators present
- Mismatch could be mixed methods or HARKing
- Requires contextual interpretation

**Low confidence:**

- Ambiguous indicators
- Disciplinary convention uncertain
- Insufficient evidence for definitive classification

**Action by confidence:**

- **High:** Flag HARKing, penalise Transparency, note in report
- **Medium:** Flag for Track A monitoring, note concern with caveat, minor Transparency penalty
- **Low:** Note potential concern, no penalty, mention in Track A quality assessment

---

## Related References

- `approach-taxonomy.md` - Research approach definitions and "none_stated" handling
- `assessment-frameworks.md` - Framework selection by approach (including HARKing-flagged cases)
- `signal-definitions-hass.md` - Transparency signal with methodological clarity criteria
- `track-a-quality-criteria.md` - Quality monitoring for low-confidence classifications
