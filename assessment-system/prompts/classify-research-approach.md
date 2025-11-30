# Research Approach Classification - Pass 8

**Version:** v1.0
**Last Updated:** 2025-11-17
**Workflow Stage:** Pass 8 - Research approach classification
**Schema Version:** classification-schema.md v2.1

---

## Your Task

Classify the research approach of the paper to inform credibility assessment framework selection. This involves determining paper type (empirical/methodological/theoretical/meta-research), classifying the research approach or validation strategy, comparing expressed vs revealed methodology (HARKing detection), and evaluating taxonomy fit.

**Input:** Complete extraction.json from Pass 0-6 (all arrays populated, validation passed)

**Your responsibility:** Classify paper type, determine research approach, detect methodological mismatches, select appropriate credibility framework, and provide taxonomy feedback

**Output:** NEW file `assessment/classification.json` with complete classification

---

## 🚨 CRITICAL: Two-Stage Classification with Taxonomy Feedback

**STAGE 1:** Determine paper type (empirical/methodological/theoretical/meta-research)

**STAGE 2:** Classify research approach based on paper type:
  - **Empirical papers:** Deductive/inductive/abductive classification
  - **Methodological papers:** Validation approach classification
  - **Theoretical papers:** Theory development approach
  - **Meta-research papers:** Study design approach

**STAGE 3:** Evaluate taxonomy fit and propose new categories if needed

**This is iterative taxonomy development** - your honest assessment of category fit helps improve the system. Choose the closest category but document limitations when fit is poor.

---

## Classification Workflow

### STEP 1: Determine Paper Type

**Question:** What is the primary purpose of this paper?

**Read from extraction.json:**
- `project_metadata` - Title, journal, year for context
- `claims` - What kinds of claims does the paper make?
- `research_designs` - What is the design trying to accomplish?
- `methods` - Are methods tools for investigation or subjects of investigation?

**Paper Type Decision Tree:**

**Question 1.1:** Does the paper collect or analyse new empirical data about phenomena (not methods)?

- Research question targets phenomena in the world (settlements, artefacts, environments, societies)
- Claims describe, explain, or predict phenomena
- Methods are tools used to investigate (not the subject being investigated)

**YES** → **Type 1: Empirical Research Paper**
- Use standard deductive/inductive/abductive classification
- All seven credibility signals apply

**NO** → Continue to Question 1.2

**Question 1.2:** Is the primary contribution a method, tool, protocol, or framework?

- Paper presents software, analytical technique, field protocol, or theoretical framework
- Claims are about method properties (capabilities, advantages, limitations)
- If empirical application included, it's demonstrative (not the main contribution)
- "Results" section describes method performance (not substantive findings)

**YES** → **Type 2: Methodological Paper**
- Classify validation approach (how method is demonstrated/validated)
- Emphasise Transparency, Reproducibility, Comprehensibility signals
- Deemphasise Generalisability, Robustness (of demonstration cases)

**NO** → Continue to Question 1.3

**Question 1.3:** Does the paper synthesise existing research or develop theory?

- No new empirical data collection
- Literature synthesis, meta-analysis, or theoretical development
- Theoretical arguments or conceptual framework building

**YES** → **Type 3: Theoretical/Review Paper**
- Classify theory development approach
- Emphasise Comprehensibility, Plausibility, Transparency

**NO** → Continue to Question 1.4

**Question 1.4:** Does the paper study research practices or scientific processes?

- Research papers themselves are the data
- Studies how research is conducted, reported, or assessed
- Scientometrics, reproducibility studies, methodological critiques

**YES** → **Type 4: Meta-Research Paper**
- Often mixed classification (empirical study OF research)
- Use appropriate framework based on specific design

**NO** → **TAXONOMY GAP DETECTED**
- This paper doesn't fit existing 4-type taxonomy
- Proceed to Step 2 to evaluate fit and propose new category
- Choose CLOSEST existing type for now

**Output for Step 1:**

```json
{
  "paper_type": "[empirical|methodological|theoretical|meta_research]",
  "paper_type_justification": "Detailed explanation of why this type assigned, citing evidence from extraction"
}
```

**For methodological papers, also populate:**

```json
{
  "methodological_characterisation": {
    "subtype": "[software_tool|analytical_method|field_protocol|theoretical_framework|data_paper|infrastructure|resource|protocol]",
    "validation_approach": "[will determine in later steps]",
    "validation_notes": "[will populate after classifying validation approach]"
  }
}
```

---

### Paper Subtypes and Context Flags

**When assessing Robustness (Cluster 2) and generating the final report (Pass 10), these subtypes trigger context flags that explain genre-appropriate expectations:**

#### 📦 Descriptive/Artefact Papers (Robustness context flag)

These describe artefacts rather than test hypotheses. Moderate Robustness is expected, not a deficiency:

| Subtype | Description | Expected Robustness |
|---------|-------------|---------------------|
| `software_tool` | Software papers (e.g., FAIMS, archaeological GIS tools) | Moderate (40-60) |
| `data_paper` | Dataset descriptions | Moderate (40-60) |
| `infrastructure` | Platform/system descriptions | Moderate (40-60) |
| `protocol` | Method protocol descriptions | Moderate-Good (50-70) |
| `resource` | Database/ontology/vocabulary papers | Moderate (40-60) |

#### 📐 Synthesis/Framework Papers (Robustness context flag)

These argue for positions rather than test hypotheses systematically:

| Subtype | Description | Expected Robustness |
|---------|-------------|---------------------|
| `theoretical_framework` | Conceptual framework papers | Moderate-Good (50-70) |
| `position_paper` | Papers arguing a viewpoint | Moderate (40-60) |
| `commentary` | Response/commentary papers | Moderate (40-60) |
| `narrative_review` | Non-systematic literature reviews | Moderate-Good (50-70) |

**Note:** Systematic reviews are different — they DO require robustness checks and should NOT receive 📐 flag.

#### 🔧 Methodological Transparency (Reproducibility context flag)

For papers without computational workflows to reproduce:

| Subtype | Reproducibility Question |
|---------|-------------------------|
| `software_tool` | Can users install, use, and extend the software? |
| `interpretive` | Can readers access sources and follow reasoning? |
| `theoretical_framework` | Can readers trace the argument? |

**Capture the subtype in classification.json** so downstream passes can apply appropriate context flags.

---

### STEP 2: Evaluate Taxonomy Fit and Provide Feedback

**As you completed Step 1, how well did the paper fit the chosen category?**

**Assess category fit quality:**

**Excellent fit:** Paper clearly matches one category, no ambiguity, classification feels natural
- Set `category_fit_quality = "excellent"`
- No taxonomy proposal needed

**Good fit:** Paper fits one category with minor reservations, slight edge case but reasonable
- Set `category_fit_quality = "good"`
- No taxonomy proposal needed

**Acceptable fit:** Paper can be classified but feels like edge case, requires caveats
- Set `category_fit_quality = "acceptable"`
- CONSIDER proposing new category if you see clear pattern

**Poor fit:** Paper doesn't fit well, forced into closest category, extensive qualifications needed
- Set `category_fit_quality = "poor"`
- MUST propose new category with detailed rationale

**When to propose new paper types:**

- Paper has characteristics fundamentally different from existing 4 types
- You find yourself writing extensive qualifications/caveats in justification
- Paper serves purpose not captured by existing taxonomy
- Classification feels forced or misleading
- You can identify 2+ papers in corpus that might fit proposed category
- New category would have distinct credibility criteria

**When NOT to propose:**

- Minor variations within existing types (note in justification instead)
- Single unique paper (handle as edge case in closest category)
- Disciplinary variations (note contextual differences)

**How to propose new paper types:**

```json
{
  "taxonomy_feedback": {
    "category_fit_quality": "poor",
    "proposed_new_category": "descriptive_name_for_category",
    "rationale_for_proposal": "Explain why existing 4 types inadequate. What fundamental characteristics does this paper have that don't fit? Why does classification feel forced?",
    "characteristics_of_proposed_category": "Define what makes this category distinct. What are its defining features? How does it differ from empirical, methodological, theoretical, and meta-research?",
    "alternative_papers_that_might_fit": [
      "List other papers in corpus that might share this category",
      "Include paper slugs if known, or descriptions if not yet extracted"
    ]
  }
}
```

**Your role in taxonomy development:**

- You are helping iteratively refine the taxonomy during Phase 1 testing
- Proposing new categories is VALUABLE feedback (not extra work to avoid)
- Choose closest existing category but document poor fit honestly
- User will review proposals and update taxonomy between test cycles
- Expected: Most papers fit well (excellent/good), 10-20% acceptable, 0-5% poor

**Output for Step 2:**

Always populate `taxonomy_feedback` object, even if fit is excellent (use null values for proposal fields).

---

### STEP 3: Classify Research Approach (Paper Type-Specific)

**Branch based on paper_type:**

#### For Empirical Papers: Detect Expressed Approach

**Where to look (in extraction.json):**
- `project_metadata.paper_title` - Title often hints at approach
- `research_designs[].design_text` - Explicit design statements
- `research_designs[].design_status` - "explicit" designs are expressed
- First ~500 words of paper (Introduction/Background) for methodological framing

**Key phrases to identify:**

**Deductive indicators:**
- "We hypothesised that..."
- "To test the hypothesis..."
- "Confirmatory analysis"
- "Predicted that..."
- "Hypothesis-testing"
- Research designs with "hypothesis", "test", "confirm"

**Inductive indicators:**
- "Exploratory study"
- "To document patterns of..."
- "Systematic survey"
- "Descriptive analysis"
- "Pattern discovery"
- Research designs with "exploratory", "survey", "descriptive"

**Abductive indicators:**
- "To explain..."
- "Inference to best explanation"
- "Interpretive framework"
- "Best explanation for..."
- "Comparative assessment of alternative explanations"
- Research designs with "interpretive", "explanatory", "case study"

**What to extract:**
- Direct quotes or close paraphrases
- Research design types from RDMAP
- Sections where evidence found

**Output:**

```json
{
  "expressed_approach": {
    "approach": "[deductive|inductive|abductive|mixed|none_stated]",
    "evidence": [
      "Quote 1 with specific methodological statement",
      "RDMAP research_design: 'exploratory survey'"
    ],
    "source_sections": ["introduction", "methods"],
    "confidence": "[high|medium|low]"
  }
}
```

**Confidence levels:**
- **HIGH:** Clear, explicit methodological framework stated
- **MEDIUM:** Implied through design language but not explicitly stated
- **LOW:** Ambiguous or requires inference from design type alone

---

#### For Empirical Papers: Infer Revealed Approach

**Analyse what the paper actually does (independent of what it says):**

**Examine claims structure:**

- Are claims **hypotheses** ("We hypothesise X will correlate with Y") → Deductive
- Are claims **pattern descriptions** ("Settlements cluster in valleys") → Inductive
- Are claims **explanations** ("Best explanation for pattern X is process Y") → Abductive

**Read from `claims[]` array:**
- Look at `claim_text` fields
- Identify whether claims test predictions, describe patterns, or explain phenomena
- Note: 30-50 claims is typical, sample broadly (early, middle, late claims)

**Examine methods application:**

- Are methods used for **hypothesis testing** (confirmatory) → Deductive
- Are methods used for **pattern discovery** (exploratory) → Inductive
- Are methods used for **comparative inference** (interpretive) → Abductive

**Read from `methods[]` array:**
- Look at `method_text` and `application_context` fields
- Identify whether methods test predictions, document systematically, or interpret comparatively

**Examine analytical workflow:**

- **Deductive workflow:** Hypothesis → test → confirmation/rejection
- **Inductive workflow:** Observation → pattern identification → interpretation
- **Abductive workflow:** Pattern observation → alternative explanations → inference to best

**Reconstruct from:**
- Sequence of `research_designs`, `methods`, `protocols` in RDMAP hierarchy
- Flow of `evidence` → `claims` relationships
- Narrative structure in paper

**Output:**

```json
{
  "revealed_approach": {
    "approach": "[deductive|inductive|abductive|mixed]",
    "evidence": {
      "claims_structure": "Description of claim types with examples from claims array",
      "methods_application": "Description of how methods actually used with examples from methods array",
      "analytical_workflow": "Description of actual analytical sequence reconstructed from RDMAP and evidence-claim relationships"
    },
    "confidence": "[high|medium|low]"
  }
}
```

**Confidence levels:**
- **HIGH:** Clear, unambiguous workflow with consistent patterns
- **MEDIUM:** Mostly clear but some mixed elements
- **LOW:** Ambiguous or difficult to reconstruct from extraction

---

#### For Methodological Papers: Classify Validation Approach

**For papers with `paper_type = "methodological"`, classify the validation strategy instead:**

**How is the method presented and validated?**

**Inductive/Descriptive validation:**
- Method demonstrated through illustrative case examples
- Descriptive presentation of capabilities and features
- No hypothesis-testing of method performance
- Example: "FAIMS demonstrated through three case studies showing data collection workflow"

**Deductive/Hypothesis-testing validation:**
- Explicit hypotheses about method performance
- Systematic testing against performance criteria or benchmarks
- Comparative evaluation with pre-specified predictions
- Example: "New calibration method tested against 50 known-age samples; hypothesis: error < 5%"

**Abductive/Inference-based validation:**
- Method justified through theoretical argumentation
- Inference to best design solution for stated problem
- Comparative assessment of design alternatives
- Example: "Framework proposed as best explanation for classification requirements given theoretical constraints"

**Mixed validation:**
- Combines multiple strategies (e.g., theoretical justification + performance testing)
- Example: "Method rationale explained theoretically, then demonstrated through examples, then tested against benchmark"

**None (Technical specification only):**
- Pure technical documentation without validation
- Rare in published research (more common in software manuals or grey literature)

**Populate in methodological_characterisation:**

```json
{
  "methodological_characterisation": {
    "subtype": "[software_tool|analytical_method|field_protocol|theoretical_framework]",
    "validation_approach": "[inductive|deductive|abductive|mixed|none]",
    "validation_notes": "Detailed description of how method is validated, citing evidence from paper"
  }
}
```

**Note:** For methodological papers, `expressed_approach` and `revealed_approach` may be set to describe how the METHOD is discussed, or may be omitted if not applicable. Use judgement based on paper structure.

---

### STEP 4: Compare Expressed vs Revealed (HARKing Detection)

**For empirical papers only** (methodological papers skip this step or apply to validation approach):

**Compare `expressed_approach.approach` with `revealed_approach.approach`:**

**Three outcomes:**

**1. Matched:** Expressed = Revealed (no issues)
- Paper says deductive, actually does deductive
- Paper says inductive, actually does inductive
- Paper says abductive, actually does abductive

```json
{
  "expressed_vs_revealed": {
    "alignment": "matched",
    "harking_flag": false,
    "mismatch_explanation": "Paper explicitly states [approach] and actually conducts [approach]. Methodological transparency is high."
  }
}
```

**2. Partial:** Mixed methods or minor discrepancies
- Paper states one primary approach, uses mixed approaches
- Appropriate mixed-method design with clear phase separation
- Minor discrepancies that don't indicate HARKing

```json
{
  "expressed_vs_revealed": {
    "alignment": "partial",
    "harking_flag": false,
    "mismatch_type": "legitimately_mixed",
    "mismatch_explanation": "Paper states primarily inductive design but includes confirmatory statistical tests. This is appropriate mixed-method research with clear phase separation (inductive survey → post-hoc statistical validation)."
  }
}
```

**3. Mismatched:** Clear mismatch (potential HARKing or methodological confusion)
- Paper says deductive (hypothesis-testing) but actually does inductive (pattern discovery)
- Paper frames exploratory findings as confirmatory tests
- "Hypothesis" appears only after results presented

**Mismatch types:**

- `HARKing_potential`: Post-hoc hypotheses framed as confirmatory (most serious)
- `methodological_confusion`: Researcher unclear about their own design
- `disciplinary_convention`: Normal practice in this field/era (not problematic)
- `legitimately_mixed`: Appropriate mixed methods (not actually problematic)

```json
{
  "expressed_vs_revealed": {
    "alignment": "mismatched",
    "harking_flag": true,
    "mismatch_type": "HARKing_potential",
    "mismatch_explanation": "Paper uses hypothesis-testing rhetoric ('we hypothesised that settlements would cluster near water') but shows no evidence of a priori hypothesis specification. 'Hypothesis' first appears in Discussion section after all results presented. Survey methods were exploratory (systematic transects without pre-specified predictions). Likely post-hoc framing of exploratory findings as confirmatory."
  }
}
```

**When to flag HARKing:**
- Clear discrepancy between stated confirmatory design and actual exploratory methods
- "Hypothesis" appears only in Discussion, not Introduction/Methods
- No evidence of pre-registration, protocol, or a priori predictions
- Exploratory methods (systematic survey, pattern discovery) with confirmatory framing

**When NOT to flag:**
- Mixed methods with clear phase separation
- Disciplinary convention (some fields use "hypothesis" more loosely)
- Abductive research (inference to best explanation is legitimate)
- Minor terminological imprecision

---

### STEP 5: Handle "none_stated" with Contextual Interpretation

**If `expressed_approach.approach = "none_stated"` (no explicit methodological framework stated):**

**Do not automatically penalise.** Absence of methodology section may indicate:

1. Methodological naivete or weak research design (common for contemporary papers - **problematic**)
2. Disciplinary genre conventions (some fields/eras don't use methodology sections - **acceptable**)
3. Methodological commitments expressed through narrative rather than explicit section (**partially acceptable**)

**Contextual interpretation required:**

**Consider (from extraction.json):**
- `project_metadata.publication_year` - Older publications may follow different norms
- `project_metadata.journal` - Field-specific journals may not require explicit methods statements
- `project_metadata.discipline` - Some disciplines historically assumed implicit methodologies
- Paper length/type - Short communications, notes, or book chapters may differ

**Classification for none_stated:**

```json
{
  "expressed_approach": {
    "approach": "none_stated",
    "evidence": ["No explicit methodological framework stated in Introduction, Methods, or Research Design sections"],
    "source_sections": [],
    "confidence": "high",
    "significance": "[Contextual interpretation here]"
  },

  "expressed_vs_revealed": {
    "alignment": "partial",
    "harking_flag": false,
    "mismatch_type": "disciplinary_convention",
    "mismatch_explanation": "Cannot compare expressed vs revealed when no expressed approach stated. Classification based entirely on revealed approach from methods and claims. [Include contextual interpretation: publication year, journal norms, whether absence appears to be oversight or convention]."
  }
}
```

**Examples of contextual interpretations:**

**Problematic absence (contemporary paper):**
```
"significance": "2018 publication in major international journal with no methodological framework statement. Contemporary research standards expect explicit research design. Absence indicates potential methodological naivete or weak transparency."
```

**Acceptable absence (historical paper):**
```
"significance": "1987 publication in regional archaeology bulletin. Disciplinary conventions of this era and venue did not require explicit methodology sections. Implicit inductive survey design inferred from methods description."
```

**Partial absence (narrative methods):**
```
"significance": "2020 ethnographic study. No formal 'Methods' section but methodological commitments expressed through narrative: 'We conducted participant observation over 18 months'. Approach inferred from narrative rather than explicit statement."
```

**Impact on credibility assessment:**
- Flags for Track A quality monitoring (triggers medium/low classification confidence)
- Affects Transparency signal baseline (absence reduces transparency score)
- Noted in credibility report methodological considerations section

---

### STEP 6: Characterise Mixed Methods (if applicable)

**If research uses multiple approaches across phases or components:**

**Use qualitative characterisation, NOT percentages**

**Identify:**
- Primary approach (dominant)
- Secondary approaches (additional elements)
- Qualitative description of how approaches combine

**AVOID:**
- Percentage precision ("60% inductive, 40% deductive") - implies false precision
- Forcing single category when mixed is more accurate
- Rigid categorisation where flexibility is appropriate

**Example characterisations:**

**Primarily inductive with deductive validation:**
```json
{
  "mixed_method_characterisation": {
    "is_mixed": true,
    "primary_approach": "inductive",
    "secondary_approaches": ["deductive"],
    "qualifications": [
      "Overall inductive exploratory survey design",
      "Includes confirmatory statistical analysis of observed patterns as secondary validation",
      "Statistical tests are post-hoc, not a priori hypothesis tests",
      "Mixed design is appropriate and well-executed"
    ]
  }
}
```

**Genuinely mixed with phase separation:**
```json
{
  "mixed_method_characterisation": {
    "is_mixed": true,
    "primary_approach": "mixed_deductive_inductive",
    "secondary_approaches": [],
    "qualifications": [
      "Phase 1: Deductive hypothesis testing through experimental archaeology (tool efficiency hypotheses)",
      "Phase 2: Inductive pattern discovery in archaeological assemblages to identify tool use traces",
      "Appropriately mixed design with clear phase separation and distinct research questions per phase"
    ],
    "section_breakdown": [
      {"section": "Experimental archaeology (Phase 1)", "approach": "deductive"},
      {"section": "Archaeological survey (Phase 2)", "approach": "inductive"}
    ]
  }
}
```

**If NOT mixed:**
```json
{
  "mixed_method_characterisation": {
    "is_mixed": false
  }
}
```

**Note:** Methodological papers can also have mixed validation approaches - apply same principles.

---

### STEP 7: Determine Primary Classification

**Synthesise Steps 1-6 to produce authoritative classification:**

**Decision rules:**

1. If expressed ≠ revealed, **use revealed approach as primary** (what paper actually does trumps what it says)
2. If mixed methods, **specify primary + note mixed character** in justification
3. If methodological paper, **primary classification is validation approach** (not substantive research approach)
4. If "none_stated", **use revealed approach** (can't use what isn't stated)

**Confidence levels:**

- **HIGH:** Clear classification, no ambiguity, strong evidence
- **MEDIUM:** Reasonable classification with some caveats or minor ambiguity
- **LOW:** Ambiguous, significant uncertainty, forced choice between alternatives

**Confidence affects Track A quality gating:**
- **LOW confidence** → MODERATE quality state (caveated assessment)
- **HIGH/MEDIUM confidence** → Enables HIGH quality state (if other factors good)

**Output:**

```json
{
  "primary_classification": {
    "approach": "[deductive|inductive|abductive]",
    "confidence": "[high|medium|low]",
    "justification": "Narrative explanation of classification decision with specific evidence from extraction. For empirical papers: explain approach. For methodological papers: explain validation approach. Cite claims, methods, designs, workflow evidence. Explain why this classification chosen. Note any caveats or edge cases."
  }
}
```

**Example empirical paper:**
```json
{
  "primary_classification": {
    "approach": "inductive",
    "confidence": "high",
    "justification": "This is clearly inductive research. The paper explicitly states an exploratory aim ('systematic survey to document previously unknown sites'). Methods are appropriate for pattern discovery (20m transect field walking with opportunistic documentation). Claims are framed as pattern descriptions ('settlements cluster within 2km of rivers', 'site density increases in valley bottoms') rather than hypothesis tests. No pre-specified predictions; patterns emerge from survey data. Revealed approach matches expressed approach. Classification is unambiguous."
  }
}
```

**Example methodological paper:**
```json
{
  "primary_classification": {
    "approach": "inductive",
    "confidence": "high",
    "justification": "FAIMS Mobile software tool paper. Validation approach is inductive/descriptive: method capabilities demonstrated through three illustrative case studies from archaeological fieldwork. No hypothesis-testing of software performance or systematic comparison with alternatives. Primary contribution is technical specification of platform architecture and features, with case studies serving demonstrative function. Classification based on validation approach (inductive demonstration), not substantive research approach (method itself is the contribution, not findings from using it)."
  }
}
```

---

### STEP 8: Select Credibility Assessment Framework

**Based on primary classification AND paper type, specify which signals to emphasise:**

**Framework selection matrix:**

| Paper Type | Primary Approach | Framework | Primary Signals |
|------------|------------------|-----------|-----------------|
| Empirical | Deductive | deductive_emphasis | Validity, Robustness, Reproducibility |
| Empirical | Inductive | inductive_emphasis | Transparency, Comprehensibility, Generalisability |
| Empirical | Abductive | abductive_emphasis | Plausibility, Validity, Robustness |
| Empirical | Mixed | mixed_assessment | Balanced (depends on primary approach) |
| Methodological | Any | methodological_paper | Transparency, Reproducibility, Comprehensibility |
| Theoretical | Any | theoretical_assessment | Comprehensibility, Plausibility, Transparency |
| Meta-research | Varies | [Use empirical or methodological as appropriate] | |

**Signal prioritisation guidance:**

**Deductive emphasis (hypothesis-testing research):**
```json
{
  "framework_to_use": "deductive_emphasis",
  "signal_prioritisation": {
    "primary_signals": ["validity", "robustness", "reproducibility"],
    "secondary_signals": ["transparency", "comprehensibility", "plausibility"],
    "deemphasised_signals": ["generalisability"],
    "rationale": "Deductive research prioritises: (1) Validity - evidence adequacy for hypothesis tests, (2) Robustness - sensitivity to analytical choices, (3) Reproducibility - code/data sharing for reproduction. Generalisability assessed but not emphasised (single study rarely generalises alone)."
  }
}
```

**Inductive emphasis (exploratory/descriptive research):**
```json
{
  "framework_to_use": "inductive_emphasis",
  "signal_prioritisation": {
    "primary_signals": ["transparency", "comprehensibility", "generalisability"],
    "secondary_signals": ["validity", "reproducibility", "plausibility"],
    "deemphasised_signals": [],
    "rationale": "Inductive research prioritises: (1) Transparency - research design clarity and workflow documentation, (2) Comprehensibility - pattern descriptions and interpretations, (3) Generalisability - appropriate scope and acknowledged limitations. All signals relevant but transparency is foundation for exploratory research assessment."
  }
}
```

**Abductive emphasis (interpretive/explanatory research):**
```json
{
  "framework_to_use": "abductive_emphasis",
  "signal_prioritisation": {
    "primary_signals": ["plausibility", "validity", "robustness"],
    "secondary_signals": ["comprehensibility", "transparency", "generalisability"],
    "deemphasised_signals": ["reproducibility"],
    "rationale": "Abductive research prioritises: (1) Plausibility - explanatory coherence and theoretical grounding, (2) Validity - evidence adequacy for inference, (3) Robustness - alternative explanations considered. Reproducibility deemphasised (interpretive inference has different reproducibility expectations than analytical reproduction)."
  }
}
```

**Methodological paper emphasis:**
```json
{
  "framework_to_use": "methodological_paper",
  "signal_prioritisation": {
    "primary_signals": ["transparency", "reproducibility", "comprehensibility"],
    "secondary_signals": ["validity", "plausibility"],
    "deemphasised_signals": ["generalisability", "robustness"],
    "rationale": "Methodological papers prioritise: (1) Transparency - design decisions documented, (2) Reproducibility - method reproducible, (3) Comprehensibility - clear technical specification. Validity and Plausibility apply to claims ABOUT the method. Generalisability and Robustness (of demonstration cases) deemphasised - demonstration cases are illustrative, not meant to generalise."
  }
}
```

**See `assessment-frameworks.md` in research-assessor skill for detailed framework guidance.**

---

### STEP 9: Assess Transparency

**Evaluate methodological transparency as input to Track A and Transparency signal:**

**Questions:**

1. Is an expressed methodology present? (yes/no from Step 3)
2. What is the transparency quality? (high/moderate/low)

**Transparency quality levels:**

**HIGH:**
- Explicit research design statement present
- Clear methodological framework described
- Research approach unambiguous
- Example: "Methods section explicitly states 'exploratory survey design' with clear rationale"

**MODERATE:**
- Methodology implicit but can be inferred
- Design elements present but not synthesised into coherent framework
- Requires reader to reconstruct approach
- Example: "Methods describe survey procedures but don't explicitly state exploratory design; must be inferred"

**LOW:**
- No methodological framework stated
- Methods described but not contextualised in research design
- Significant ambiguity about approach
- Example: "No methodology section; field procedures described but research design unclear"

**Output:**

```json
{
  "transparency_assessment": {
    "expressed_methodology_present": true,
    "transparency_quality": "high",
    "transparency_notes": "Explicit research design statement present in Introduction and Methods. Methodology clearly described as exploratory regional survey. Transparency is high."
  }
}
```

**Affects:**
- Track A classification confidence dimension (LOW quality → reduces confidence)
- Transparency signal baseline (starts higher if methodology explicit)
- Credibility report methodological considerations

---

### STEP 10: Verify Error Conditions

**Before generating output, check for error conditions:**

**Error 1: Incomplete extraction**

**Check extraction.json for:**
- `claims[]` array populated (length > 0)
- `methods[]` array populated (length > 0)
- `research_designs[]` array populated (length > 0)

**If any array empty or missing:**

```
ERROR: Incomplete extraction. Missing: [list missing arrays]. Complete Pass 0-6 before running classification (Pass 8).

Required arrays:
- claims[] (for revealed approach inference)
- methods[] (for methods application analysis)
- research_designs[] (for expressed approach detection)

Cannot classify research approach without complete extraction.
```

**Error 2: Missing assessment directory**

**Check that directory exists:**
- `outputs/{paper-slug}/assessment/`

**If directory missing:**

```
ERROR: assessment/ directory not found at outputs/{paper-slug}/assessment/

Classification output must be written to assessment/ subdirectory.

Create directory before running Pass 8:
  mkdir -p outputs/{paper-slug}/assessment/
```

**If either error condition met, STOP. Do not proceed with classification.**

---

### STEP 11: Generate classification.json

**Compile all outputs from Steps 1-9 into complete classification.json**

**Required fields (always present):**
- `classification_metadata` (with date, version)
- `paper_type` and `paper_type_justification`
- `taxonomy_feedback` (with category_fit_quality)
- `expressed_approach` (for empirical papers)
- `revealed_approach` (for empirical papers)
- `expressed_vs_revealed` (for empirical papers)
- `primary_classification`
- `credibility_framework`
- `transparency_assessment`

**Conditional fields:**
- `methodological_characterisation` (only if paper_type = "methodological")
- `mixed_method_characterisation` (only if is_mixed = true; otherwise `{"is_mixed": false}`)

**Optional fields:**
- `classification_notes` (any additional context, edge cases, ambiguities)

**Write to:** `outputs/{paper-slug}/assessment/classification.json`

**Format:** Valid JSON with proper indentation

---

## Self-Validation Checklist

**Before finalizing classification.json, verify:**

- [ ] `paper_type` determined with justification
- [ ] `taxonomy_feedback.category_fit_quality` assessed (excellent/good/acceptable/poor)
- [ ] If category_fit_quality = "poor", taxonomy proposal populated with rationale and characteristics
- [ ] If paper_type = "methodological", `methodological_characterisation` populated
- [ ] `expressed_approach` populated (or explained why not applicable for methodological papers)
- [ ] `revealed_approach` populated (or validation approach for methodological papers)
- [ ] `expressed_vs_revealed` comparison completed
- [ ] If alignment = "mismatched", `harking_flag` and `mismatch_type` present
- [ ] If alignment = "matched", explanation provided
- [ ] If `expressed_approach` = "none_stated", contextual interpretation provided in significance field
- [ ] `primary_classification` with approach, confidence, and detailed justification
- [ ] If is_mixed = true, `mixed_method_characterisation` complete with qualifications
- [ ] `credibility_framework.signal_prioritisation` matches BOTH approach AND paper type
- [ ] `credibility_framework.rationale` explains why these signals prioritised
- [ ] `transparency_assessment` completed
- [ ] Justification cites specific evidence from extraction (claims, methods, designs)
- [ ] Confidence levels assigned consistently across fields
- [ ] Output directory `assessment/` exists (error if not)
- [ ] Extraction complete (claims, methods, designs arrays populated)
- [ ] Valid JSON syntax (no trailing commas, proper quotes, correct structure)
- [ ] classifier_version = "v0.2-alpha"

---

## Output Format

**File:** `outputs/{paper-slug}/assessment/classification.json`

**Complete schema specification:** See `.claude/skills/research-assessor/references/schema/classification-schema.md`

**Minimum structure:**

```json
{
  "classification_metadata": {
    "classified_after_pass": 6,
    "classification_date": "2025-11-17",
    "classifier_version": "v0.2-alpha"
  },

  "paper_type": "empirical",
  "paper_type_justification": "...",

  "taxonomy_feedback": {
    "category_fit_quality": "excellent",
    "proposed_new_category": null,
    "rationale_for_proposal": null,
    "characteristics_of_proposed_category": null,
    "alternative_papers_that_might_fit": []
  },

  "expressed_approach": { ... },
  "revealed_approach": { ... },
  "expressed_vs_revealed": { ... },
  "primary_classification": { ... },
  "mixed_method_characterisation": { ... },
  "transparency_assessment": { ... },
  "credibility_framework": { ... },

  "classification_notes": "..."
}
```

---

## Error Handling

**If extraction.json incomplete (missing claims/methods/designs):**
- STOP with error message
- Do NOT proceed with classification
- Error format: "ERROR: Incomplete extraction. Missing: [arrays]. Complete Pass 0-6 before classification."

**If assessment/ directory missing:**
- STOP with error message
- Error format: "ERROR: assessment/ directory not found. Create outputs/{paper-slug}/assessment/ before running Pass 8."

**Do NOT:**
- Guess or infer missing data
- Proceed with partial extraction
- Create assessment/ directory yourself (user must create)
- Output classification.json to wrong location

---

## Examples

### Example 1: Empirical Inductive (Matched, Excellent Fit)

**Paper:** Archaeological field survey documenting settlement patterns

```json
{
  "classification_metadata": {
    "classified_after_pass": 6,
    "classification_date": "2025-11-17",
    "classifier_version": "v0.2-alpha"
  },

  "paper_type": "empirical",
  "paper_type_justification": "This paper uses field survey methods to investigate substantive research question about settlement patterns in the Vardar valley. Claims describe phenomena (settlement locations, density patterns). Methods are tools for investigation (field walking, site documentation). Primary contribution is understanding settlement distribution, not presenting survey methodology.",

  "taxonomy_feedback": {
    "category_fit_quality": "excellent",
    "proposed_new_category": null,
    "rationale_for_proposal": null,
    "characteristics_of_proposed_category": null,
    "alternative_papers_that_might_fit": []
  },

  "expressed_approach": {
    "approach": "inductive",
    "evidence": [
      "Introduction states: 'This exploratory study documents settlement patterns in the Vardar valley'",
      "Methods: 'Systematic field survey to identify previously unknown sites'",
      "RDMAP research_design RD001: 'exploratory regional survey'"
    ],
    "source_sections": ["introduction", "methods"],
    "confidence": "high"
  },

  "revealed_approach": {
    "approach": "inductive",
    "evidence": {
      "claims_structure": "Pattern descriptions dominate: C012 'settlements cluster within 2km of rivers', C015 'site density increases in valley bottoms', C023 'bronze age sites more dispersed than iron age'. No hypothesis tests. Claims describe emergent patterns.",
      "methods_application": "Methods M003-M008 describe systematic field walking at 20m transect intervals with opportunistic site documentation. No pre-specified predictions or hypothesis testing procedures. Survey designed for comprehensive coverage and pattern discovery.",
      "analytical_workflow": "Survey → site documentation → GIS mapping → spatial pattern analysis → interpretation. Inductive sequence: data collection → pattern identification → explanation. No hypothesis → test → result sequence."
    },
    "confidence": "high"
  },

  "expressed_vs_revealed": {
    "alignment": "matched",
    "harking_flag": false,
    "mismatch_explanation": "Paper explicitly states exploratory survey design and actually conducts exploratory research. Methodological transparency is high. No discrepancy between stated and actual approach."
  },

  "primary_classification": {
    "approach": "inductive",
    "confidence": "high",
    "justification": "This is clearly inductive research. The paper explicitly states an exploratory aim, uses systematic survey methods appropriate for pattern discovery, and frames claims as pattern descriptions rather than hypothesis tests. No pre-specified predictions; patterns emerge from survey data. Revealed approach matches expressed approach. Classification is unambiguous."
  },

  "mixed_method_characterisation": {
    "is_mixed": false
  },

  "transparency_assessment": {
    "expressed_methodology_present": true,
    "transparency_quality": "high",
    "transparency_notes": "Explicit research design statement present. Methodology clearly described as exploratory survey."
  },

  "credibility_framework": {
    "framework_to_use": "inductive_emphasis",
    "signal_prioritisation": {
      "primary_signals": ["transparency", "comprehensibility", "generalisability"],
      "secondary_signals": ["validity", "reproducibility", "plausibility"],
      "deemphasised_signals": [],
      "rationale": "Inductive research emphasis: workflow transparency, pattern clarity, and appropriate scope constraint are most critical for exploratory survey research."
    }
  },

  "classification_notes": "Straightforward inductive survey. No ambiguities or edge cases."
}
```

---

### Example 2: Empirical Deductive (HARKing Mismatch, Good Fit)

**Paper:** Archaeological survey with post-hoc hypothesis framing

```json
{
  "classification_metadata": {
    "classified_after_pass": 6,
    "classification_date": "2025-11-17",
    "classifier_version": "v0.2-alpha"
  },

  "paper_type": "empirical",
  "paper_type_justification": "Empirical archaeological research investigating settlement patterns. Uses survey methods to study phenomena.",

  "taxonomy_feedback": {
    "category_fit_quality": "good",
    "proposed_new_category": null,
    "rationale_for_proposal": null,
    "characteristics_of_proposed_category": null,
    "alternative_papers_that_might_fit": []
  },

  "expressed_approach": {
    "approach": "deductive",
    "evidence": [
      "Discussion section: 'We hypothesised that settlements would cluster near water sources'",
      "Discussion: 'Results confirm the hypothesis'"
    ],
    "source_sections": ["discussion"],
    "confidence": "medium"
  },

  "revealed_approach": {
    "approach": "inductive",
    "evidence": {
      "claims_structure": "Claims are pattern descriptions, not hypothesis tests. No a priori predictions stated.",
      "methods_application": "Systematic regional survey with no pre-specified predictions or confirmatory testing procedures.",
      "analytical_workflow": "Survey → pattern observation → post-hoc 'hypothesis' formulation in discussion. Inductive sequence."
    },
    "confidence": "high"
  },

  "expressed_vs_revealed": {
    "alignment": "mismatched",
    "harking_flag": true,
    "mismatch_type": "HARKing_potential",
    "mismatch_explanation": "Paper uses hypothesis-testing rhetoric in Discussion section ('we hypothesised', 'results confirm') but shows no evidence of a priori hypothesis specification. 'Hypothesis' appears only in Discussion, not in Introduction or Methods. Survey methodology was exploratory (systematic transects without pre-specified predictions). No protocol, pre-registration, or methods description indicating confirmatory design. Likely post-hoc framing of exploratory findings as confirmatory."
  },

  "primary_classification": {
    "approach": "inductive",
    "confidence": "medium",
    "justification": "Despite deductive rhetoric in Discussion, revealed approach is clearly inductive. Survey methods are exploratory, claims are pattern descriptions, and analytical workflow follows inductive sequence. Classification based on revealed approach (what paper actually does) rather than expressed approach (post-hoc framing). Confidence reduced to medium due to HARKing concern."
  },

  "mixed_method_characterisation": {
    "is_mixed": false
  },

  "transparency_assessment": {
    "expressed_methodology_present": false,
    "transparency_quality": "moderate",
    "transparency_notes": "No explicit research design in Introduction or Methods. Hypothesis appears only in Discussion (post-hoc). Transparency reduced by lack of a priori methodological framing."
  },

  "credibility_framework": {
    "framework_to_use": "inductive_emphasis",
    "signal_prioritisation": {
      "primary_signals": ["transparency", "comprehensibility", "generalisability"],
      "secondary_signals": ["validity", "reproducibility", "plausibility"],
      "deemphasised_signals": [],
      "rationale": "Inductive framework selected based on revealed approach. Transparency signal particularly important given HARKing concern and lack of a priori design statement."
    }
  },

  "classification_notes": "HARKing detected. Post-hoc hypothesis framing of exploratory research. Not necessarily problematic if understood as exploratory, but framing as confirmatory is misleading."
}
```

---

### Example 3: Empirical "none_stated" (Contextual, Acceptable Fit)

**Paper:** 1987 regional survey with no explicit methodology

```json
{
  "classification_metadata": {
    "classified_after_pass": 6,
    "classification_date": "2025-11-17",
    "classifier_version": "v0.2-alpha"
  },

  "paper_type": "empirical",
  "paper_type_justification": "Archaeological field survey investigating settlement distribution. Empirical research using survey methods.",

  "taxonomy_feedback": {
    "category_fit_quality": "acceptable",
    "proposed_new_category": null,
    "rationale_for_proposal": null,
    "characteristics_of_proposed_category": null,
    "alternative_papers_that_might_fit": []
  },

  "expressed_approach": {
    "approach": "none_stated",
    "evidence": ["No explicit methodological framework stated in any section"],
    "source_sections": [],
    "confidence": "high",
    "significance": "1987 publication in regional archaeology bulletin (Fasti archaeologici). Disciplinary conventions of this era and venue did not require explicit methodology sections. Older publications in regional journals commonly reported results without methodological framing. Absence reflects historical genre conventions rather than methodological weakness."
  },

  "revealed_approach": {
    "approach": "inductive",
    "evidence": {
      "claims_structure": "Descriptive pattern claims about site distribution and chronology.",
      "methods_application": "Systematic regional survey methods described in practical terms (transects, recording procedures) without theoretical framing.",
      "analytical_workflow": "Survey → site catalogue → chronological/spatial patterns → interpretation. Inductive workflow."
    },
    "confidence": "high"
  },

  "expressed_vs_revealed": {
    "alignment": "partial",
    "harking_flag": false,
    "mismatch_type": "disciplinary_convention",
    "mismatch_explanation": "Cannot directly compare expressed vs revealed when no expressed approach stated. Classification based entirely on revealed approach inferred from methods and claims. Absence of explicit methodology is disciplinary convention for 1987 regional survey publication, not methodological weakness. Contemporary standards would expect explicit design statement, but this is not applicable to 1987 publication norms."
  },

  "primary_classification": {
    "approach": "inductive",
    "confidence": "high",
    "justification": "Inductive exploratory survey. Classification based on revealed approach (expressed approach absent). Methods and claims clearly indicate pattern discovery research. Confidence remains high because inductive classification is unambiguous from methods and claims, even though not explicitly stated."
  },

  "mixed_method_characterisation": {
    "is_mixed": false
  },

  "transparency_assessment": {
    "expressed_methodology_present": false,
    "transparency_quality": "moderate",
    "transparency_notes": "No explicit research design statement. However, 1987 publication date and regional journal context mean this is acceptable for the era and venue. Transparency assessed relative to contemporary norms, not current standards."
  },

  "credibility_framework": {
    "framework_to_use": "inductive_emphasis",
    "signal_prioritisation": {
      "primary_signals": ["transparency", "comprehensibility", "generalisability"],
      "secondary_signals": ["validity", "reproducibility", "plausibility"],
      "deemphasised_signals": [],
      "rationale": "Inductive framework. Transparency signal will contextualise absence of explicit methodology relative to 1987 disciplinary norms."
    }
  },

  "classification_notes": "Historical publication with implicit methodology. Classified based on revealed approach with contextual consideration of publication era and venue norms."
}
```

---

### Example 4: Methodological Paper (Software Tool, Good Fit)

**Paper:** FAIMS Mobile software platform

```json
{
  "classification_metadata": {
    "classified_after_pass": 6,
    "classification_date": "2025-11-17",
    "classifier_version": "v0.2-alpha"
  },

  "paper_type": "methodological",
  "paper_type_justification": "Primary contribution is FAIMS Mobile software platform for archaeological field data collection. Paper presents tool capabilities, technical architecture, and design decisions. Results section describes software features and workflows, not substantive archaeological findings. Three archaeological case studies included but serve demonstrative/illustrative function, not as primary contribution. This is a paper ABOUT a method (software tool), not a paper USING a method to study archaeological phenomena.",

  "methodological_characterisation": {
    "subtype": "software_tool",
    "validation_approach": "inductive",
    "validation_notes": "FAIMS capabilities demonstrated through three descriptive case studies from archaeological fieldwork (Malawi rock art survey, Australian excavation, Scandinavian survey). Case studies show software features and data collection workflows in practice. No formal hypothesis-testing of software performance, no systematic comparison with alternative tools, no benchmark testing. Validation is purely descriptive/demonstrative - shows what the tool can do through examples."
  },

  "taxonomy_feedback": {
    "category_fit_quality": "good",
    "proposed_new_category": null,
    "rationale_for_proposal": null,
    "characteristics_of_proposed_category": null,
    "alternative_papers_that_might_fit": []
  },

  "expressed_approach": {
    "approach": "none_stated",
    "evidence": ["No research approach stated - paper is methodological, not empirical research"],
    "source_sections": [],
    "confidence": "high",
    "significance": "Not applicable for methodological paper presenting software tool. Paper does not conduct research using FAIMS; paper presents FAIMS itself."
  },

  "revealed_approach": {
    "approach": "inductive",
    "evidence": {
      "claims_structure": "Claims are about software capabilities: 'FAIMS supports offline data collection', 'Platform enables bidirectional sync'. Not research claims about phenomena.",
      "methods_application": "Not applicable - software features demonstrated, not methods applied to research question.",
      "analytical_workflow": "Not applicable - validation workflow is: software development → case study demonstration → feature description."
    },
    "confidence": "high"
  },

  "expressed_vs_revealed": {
    "alignment": "matched",
    "harking_flag": false,
    "mismatch_explanation": "Not applicable for methodological paper. No empirical research approach to compare. Validation approach (inductive demonstration) is appropriate for software tool presentation."
  },

  "primary_classification": {
    "approach": "inductive",
    "confidence": "high",
    "justification": "Classification is based on validation approach, not empirical research approach. FAIMS validation is inductive/descriptive: software capabilities demonstrated through illustrative case studies. No deductive hypothesis-testing of tool performance or abductive inference about design. Primary contribution is technical specification and descriptive demonstration. Confidence is high because validation strategy is clear and appropriate for software tool paper."
  },

  "mixed_method_characterisation": {
    "is_mixed": false
  },

  "transparency_assessment": {
    "expressed_methodology_present": true,
    "transparency_quality": "high",
    "transparency_notes": "Software architecture, design decisions, and technical specifications clearly documented. Validation approach (case study demonstration) is explicit. High transparency for methodological paper."
  },

  "credibility_framework": {
    "framework_to_use": "methodological_paper",
    "signal_prioritisation": {
      "primary_signals": ["transparency", "reproducibility", "comprehensibility"],
      "secondary_signals": ["validity", "plausibility"],
      "deemphasised_signals": ["generalisability", "robustness"],
      "rationale": "Methodological paper framework. Primary signals: (1) Transparency of design decisions and technical architecture (HIGH in this paper), (2) Reproducibility of software (open source, dependencies documented), (3) Comprehensibility of technical specification (clear documentation). Validity and Plausibility apply to claims ABOUT the software. Generalisability and Robustness of case studies deemphasised - demonstrations are illustrative, not meant to generalise beyond showing tool capabilities."
    }
  },

  "classification_notes": "Software tool paper. Classification based on validation approach (inductive demonstration), not substantive research approach. Different signal priorities apply compared to empirical research papers."
}
```

---

### Example 5: Poor Fit with Taxonomy Proposal

**Paper:** Hypothetical systematic comparison of radiocarbon calibration methods

```json
{
  "classification_metadata": {
    "classified_after_pass": 6,
    "classification_date": "2025-11-17",
    "classifier_version": "v0.2-alpha"
  },

  "paper_type": "methodological",
  "paper_type_justification": "Classified as 'methodological' (closest fit) because paper focuses on methods themselves rather than using methods to study phenomena. However, this paper COMPARES multiple existing calibration methods rather than PRESENTING a single new method, which makes it an edge case for the methodological category.",

  "methodological_characterisation": {
    "subtype": "analytical_method",
    "validation_approach": "deductive",
    "validation_notes": "Comparison of five radiocarbon calibration methods against 100 known-age samples. Systematic evaluation using pre-specified performance criteria (accuracy, precision, computational efficiency). Deductive testing of method performance."
  },

  "taxonomy_feedback": {
    "category_fit_quality": "poor",
    "proposed_new_category": "comparative_methods_paper",
    "rationale_for_proposal": "This paper systematically compares multiple existing methods rather than presenting a single new method. It doesn't fit 'methodological' well because methodological papers typically present/develop ONE method with demonstrations. It doesn't fit 'empirical' because methods themselves are the subject of study, not tools for studying phenomena. It doesn't fit 'theoretical' or 'meta-research'. Systematic method comparison is a distinct research genre with specific goals (fair comparison, performance benchmarking, method selection recommendations) and distinct credibility criteria (evaluation fairness, appropriate metrics, comprehensive coverage of alternatives).",
    "characteristics_of_proposed_category": "Systematic comparison of 2+ existing methods (not presenting new method). Evaluation criteria explicitly defined and justified. Performance assessment across methods using common benchmark. Recommendations for method selection based on use case characteristics. No new method development (distinguishes from 'methodological'). No substantive research question about phenomena (distinguishes from 'empirical'). Focus is evaluative/comparative, not presentational.",
    "alternative_papers_that_might_fit": [
      "penske-et-al-2023 (if it systematically compares DNA extraction protocols rather than just using one)",
      "Any papers comparing pottery classification frameworks",
      "Papers benchmarking spatial analysis algorithms",
      "Systematic comparisons of survey methods or sampling strategies"
    ]
  },

  "expressed_approach": {
    "approach": "deductive",
    "evidence": [
      "Introduction: 'We evaluate five calibration methods against known-age samples to test which performs best'",
      "Methods: 'Benchmark test using 100 samples with independently verified ages'"
    ],
    "source_sections": ["introduction", "methods"],
    "confidence": "high"
  },

  "revealed_approach": {
    "approach": "deductive",
    "evidence": {
      "claims_structure": "Comparative performance claims: 'Method A more accurate than Method B for samples >5000 BP'. Claims test pre-specified evaluation criteria.",
      "methods_application": "Systematic benchmark testing with hypothesis-like predictions about relative performance.",
      "analytical_workflow": "Define evaluation criteria → test all methods on same samples → compare performance → recommend best method for specific use cases. Deductive evaluation workflow."
    },
    "confidence": "high"
  },

  "expressed_vs_revealed": {
    "alignment": "matched",
    "harking_flag": false,
    "mismatch_explanation": "Comparative evaluation approach is consistent between expressed and revealed. Systematic benchmarking with pre-specified criteria."
  },

  "primary_classification": {
    "approach": "deductive",
    "confidence": "medium",
    "justification": "Deductive comparative evaluation. Confidence reduced to medium because paper type classification is uncertain (methodological is closest fit but not ideal). Validation approach is clearly deductive (systematic testing against criteria), but the overall paper type doesn't map cleanly to existing taxonomy."
  },

  "mixed_method_characterisation": {
    "is_mixed": false
  },

  "transparency_assessment": {
    "expressed_methodology_present": true,
    "transparency_quality": "high",
    "transparency_notes": "Evaluation criteria and benchmark testing methodology explicitly stated. Comparison is transparent and systematic."
  },

  "credibility_framework": {
    "framework_to_use": "methodological_paper",
    "signal_prioritisation": {
      "primary_signals": ["transparency", "validity", "robustness"],
      "secondary_signals": ["comprehensibility", "reproducibility"],
      "deemphasised_signals": ["generalisability"],
      "rationale": "Using methodological framework but with modified emphasis. For comparative methods papers, key signals are: (1) Transparency of evaluation criteria and comparison fairness, (2) Validity of performance metrics for stated purpose, (3) Robustness to evaluation choices (sensitivity of recommendations). Differs from typical methodological paper which emphasises reproducibility more strongly."
    }
  },

  "classification_notes": "TAXONOMY GAP: This paper is a methods comparison/benchmark study, which doesn't fit existing taxonomy well. Forced into 'methodological' as closest fit, but ideally would have dedicated 'comparative_methods' category with distinct credibility criteria emphasising evaluation fairness and metric appropriateness."
}
```

---

## Common Pitfalls

**❌ Forcing methodological papers into empirical taxonomy**
- FAIMS software paper is NOT inductive archaeological research
- It's a methodological paper with inductive VALIDATION approach

**✅ Recognise paper type, classify validation approach separately**
- Methodological papers: classify how method is validated
- Empirical papers: classify research approach

---

**❌ Assuming "none_stated" always means weak research**
- 1987 regional survey with no methods section is not necessarily problematic
- Historical publications followed different genre conventions

**✅ Consider publication year, discipline, journal conventions**
- Contextual interpretation required
- Distinguish methodological naivete from disciplinary convention

---

**❌ Using percentages for mixed methods**
- "60% inductive, 40% deductive" implies false precision
- Mixed methods are qualitative, not quantitative

**✅ Use qualitative characterisation with primary/secondary**
- "Primarily inductive survey with post-hoc statistical validation"
- Describe HOW approaches combine

---

**❌ Hiding poor taxonomy fit to avoid proposing categories**
- Forcing poor fit undermines utility of classification
- Taxonomy proposals help project improve

**✅ Document poor fit honestly, propose new category**
- Comparative methods papers don't fit existing 4 types
- Proposing "comparative_methods" category is valuable feedback

---

**❌ Flagging HARKing for appropriate mixed methods**
- Phase 1: exploratory survey, Phase 2: confirmatory testing = legitimate
- Clear phase separation with distinct research questions = not HARKing

**✅ Distinguish HARKing from legitimately mixed methods**
- HARKing: post-hoc hypotheses framed as a priori
- Mixed: appropriate combination of approaches with transparency

---

**❌ Ignoring confidence levels**
- All classifications are not equally certain
- Ambiguous cases need reduced confidence

**✅ Assign confidence honestly, affects Track A gating**
- Low confidence → moderate quality assessment (caveated)
- High confidence → enables high quality assessment

---

## References

**For detailed guidance, consult these files in research-assessor skill:**

→ See `references/credibility/approach-taxonomy.md` (Paper types, approach definitions, taxonomy evolution)

→ See `references/credibility/harking-detection-guide.md` (Expressed vs revealed comparison, mismatch types)

→ See `references/credibility/assessment-frameworks.md` (Signal prioritisation and framework selection)

→ See `references/schema/classification-schema.md` (Complete output format specification with examples)

→ See `references/credibility/track-a-quality-criteria.md` (How classification confidence affects quality gating)

---

## Remember

- **Paper type matters:** Different types need different assessment frameworks
- **Context matters:** "none_stated" isn't always problematic - consider era, discipline, journal
- **Revealed trumps expressed:** When they mismatch, classify based on what paper actually does
- **Fail fast:** Don't guess if extraction incomplete - error clearly
- **Taxonomy is iterative:** Propose new categories when fit is poor - this helps improve the system
- **Choose closest + document:** When unsure, pick closest category but explain limitations in justification
- **Confidence matters:** Low confidence affects Track A gating - assign honestly
- **Validation ≠ Research:** Methodological papers have validation approaches, not research approaches
- **HARKing detection is important:** But distinguish from legitimately mixed methods
- **classifier_version = "v0.2-alpha":** Track version for reproducibility
