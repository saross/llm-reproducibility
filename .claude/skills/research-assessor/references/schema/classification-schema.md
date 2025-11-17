# Research Approach Classification Schema

**Purpose:** Define output structure for research approach classification (Pass 8)

**Date:** 2025-11-17

---

## Output File

**Filename:** `classification.json`

**Location:** `outputs/{paper-slug}/assessment/classification.json`

**Format:** JSON

---

## Complete Schema

```json
{
  "classification_metadata": {
    "classified_after_pass": 6,
    "classification_date": "2025-11-17",
    "classifier_version": "v0.2-alpha"
  },

  "paper_type": "empirical|methodological|theoretical|meta_research",
  "paper_type_justification": "Explanation of why this paper type assigned based on paper characteristics and purpose",

  "methodological_characterisation": {
    "subtype": "software_tool|analytical_method|field_protocol|theoretical_framework",
    "validation_approach": "inductive|deductive|abductive|mixed|none",
    "validation_notes": "Description of how the method is presented, demonstrated, or validated in the paper"
  },

  "expressed_approach": {
    "approach": "deductive|inductive|abductive|mixed|none_stated",
    "evidence": [
      "Direct quote or paraphrase from paper stating methodological approach",
      "Research design type extracted from RDMAP"
    ],
    "source_sections": ["introduction", "methods"],
    "confidence": "high|medium|low"
  },

  "revealed_approach": {
    "approach": "deductive|inductive|abductive|mixed",
    "evidence": {
      "claims_structure": "Description of claim types (hypotheses, patterns, explanations)",
      "methods_application": "Description of how methods are actually used",
      "analytical_workflow": "Description of actual analytical sequence"
    },
    "confidence": "high|medium|low"
  },

  "expressed_vs_revealed": {
    "alignment": "matched|partial|mismatched",
    "harking_flag": true,
    "mismatch_type": "HARKing_potential|methodological_confusion|disciplinary_convention|legitimately_mixed",
    "mismatch_explanation": "Detailed explanation of discrepancy between expressed and revealed approaches"
  },

  "primary_classification": {
    "approach": "deductive|inductive|abductive",
    "confidence": "high|medium|low",
    "justification": "Narrative explanation of classification decision with evidence from extraction"
  },

  "mixed_method_characterisation": {
    "is_mixed": true,
    "primary_approach": "inductive",
    "secondary_approaches": ["deductive"],
    "qualifications": [
      "Overall inductive in design",
      "Includes reproducible statistical analysis of observed patterns",
      "Statistical tests are post-hoc validation, not a priori hypothesis tests"
    ],
    "section_breakdown": [
      {
        "section": "Survey design and data collection",
        "approach": "inductive"
      },
      {
        "section": "Statistical analysis of survey patterns",
        "approach": "deductive"
      }
    ]
  },

  "transparency_assessment": {
    "expressed_methodology_present": true,
    "transparency_quality": "high|moderate|low",
    "transparency_notes": "Explicit research design statement present | Implicit design, must be inferred | No methodological framework stated"
  },

  "credibility_framework": {
    "framework_to_use": "deductive_emphasis|inductive_emphasis|abductive_emphasis|mixed_assessment|methodological_paper",
    "signal_prioritisation": {
      "primary_signals": ["transparency", "validity", "generalisability"],
      "secondary_signals": ["robustness", "replicability"],
      "deemphasised_signals": [],
      "rationale": "Explanation of why these signals prioritised for this research approach and paper type"
    }
  },

  "taxonomy_feedback": {
    "category_fit_quality": "excellent|good|acceptable|poor",
    "proposed_new_category": "string or null",
    "rationale_for_proposal": "Why existing taxonomy inadequate for this paper",
    "characteristics_of_proposed_category": "Defining features that distinguish this from existing categories",
    "alternative_papers_that_might_fit": ["List of other papers in corpus that might fit this proposed category"]
  },

  "classification_notes": "Any additional contextual notes about classification decisions, edge cases, or ambiguities"
}
```

---

## Field Definitions

### classification_metadata

**Purpose:** Track when and how classification was performed

**Fields:**

- `classified_after_pass`: Always 6 (classification happens after extraction complete)
- `classification_date`: ISO date
- `classifier_version`: System version for reproducibility

---

### paper_type

**Purpose:** Classify the type of research paper before determining research approach

**Values:**

- `empirical`: Papers using methods to investigate substantive research questions about phenomena
- `methodological`: Papers presenting/developing methods, tools, protocols, or frameworks
- `theoretical`: Papers synthesising literature or developing theory without new empirical data
- `meta_research`: Papers studying research practices or scientific processes themselves

**Required:** Always present (all papers must be typed)

**See `approach-taxonomy.md` Section "Paper Type Classification" for detailed guidance**

**Example:**

```json
{
  "paper_type": "methodological",
  "paper_type_justification": "Primary contribution is FAIMS Mobile software platform for field research. Paper presents tool capabilities and technical architecture. Empirical applications are illustrative demonstrations, not the main contribution."
}
```

---

### methodological_characterisation

**Purpose:** For methodological papers, describe method subtype and validation approach

**Conditional:** Only populate if `paper_type = "methodological"`. Omit for empirical/theoretical/meta-research papers.

**Fields:**

- `subtype`: Type of method presented
  - `software_tool`: Platforms, applications, analytical software
  - `analytical_method`: Statistical techniques, computational algorithms
  - `field_protocol`: Data collection procedures, sampling strategies
  - `theoretical_framework`: Conceptual models, interpretive frameworks
- `validation_approach`: How the method is validated/demonstrated
  - `inductive`: Descriptive demonstration through case examples
  - `deductive`: Hypothesis-testing of method performance
  - `abductive`: Inference about method appropriateness
  - `mixed`: Multiple validation strategies
  - `none`: Pure technical specification without validation
- `validation_notes`: Detailed description of validation strategy

**Example:**

```json
{
  "methodological_characterisation": {
    "subtype": "software_tool",
    "validation_approach": "inductive",
    "validation_notes": "FAIMS capabilities demonstrated through three archaeological case studies. Descriptive presentation of features and workflows. No formal hypothesis-testing of software performance or comparative evaluation."
  }
}
```

**For empirical papers:** Omit this object entirely

---

### expressed_approach

**Purpose:** Document what the paper explicitly states about its methodology

**Fields:**

- `approach`: The stated or implied approach (use "none_stated" if absent)
- `evidence`: Array of quotes/paraphrases supporting classification
- `source_sections`: Sections where evidence found
- `confidence`: How clear the expressed approach is

**Special case: "none_stated"**

```json
{
  "approach": "none_stated",
  "evidence": ["No explicit methodological framework stated in Introduction or Methods"],
  "source_sections": [],
  "confidence": "high",
  "significance": "Absence of methodological statement indicates potential methodological naivete or disciplinary convention"
}
```

---

### revealed_approach

**Purpose:** Document what the paper actually does, independent of what it says

**Fields:**

- `approach`: The actual approach inferred from content
- `evidence`: Structured evidence from extraction:
  - `claims_structure`: Are claims hypotheses, patterns, or explanations?
  - `methods_application`: How are methods actually used?
  - `analytical_workflow`: What is the actual analytical sequence?
- `confidence`: How clear the revealed approach is

**Example:**

```json
{
  "approach": "inductive",
  "evidence": {
    "claims_structure": "Pattern descriptions ('settlements concentrate in valleys'), not hypothesis tests",
    "methods_application": "Systematic regional survey without pre-specified predictions",
    "analytical_workflow": "Survey → map settlements → observe clustering patterns → interpret (inductive sequence)"
  },
  "confidence": "high"
}
```

---

### expressed_vs_revealed

**Purpose:** Compare stated vs actual methodology to detect HARKing or methodological confusion

**Fields:**

- `alignment`: Degree of match between expressed and revealed
  - `matched`: Expressed = Revealed (no issues)
  - `partial`: Mixed methods or minor discrepancies
  - `mismatched`: Clear mismatch (HARKing concern)
- `harking_flag`: Boolean flag for mismatches requiring additional scrutiny
- `mismatch_type`: Type of mismatch (only if alignment = "mismatched" or "partial")
  - `HARKing_potential`: Post-hoc hypotheses framed as confirmatory
  - `methodological_confusion`: Researcher unclear about design
  - `disciplinary_convention`: Normal disciplinary practice
  - `legitimately_mixed`: Appropriate mixed-method design
- `mismatch_explanation`: Detailed narrative explaining the discrepancy

**When alignment = "matched":**

```json
{
  "alignment": "matched",
  "harking_flag": false,
  "mismatch_explanation": "Paper explicitly states exploratory design and actually conducts exploratory research. No discrepancy."
}
```

---

### primary_classification

**Purpose:** Provide the single authoritative classification for framework selection

**Fields:**

- `approach`: The primary research approach (deductive/inductive/abductive)
- `confidence`: Classification confidence (affects Track A gating)
- `justification`: Detailed narrative with evidence citations

**Notes:**

- If expressed ≠ revealed, use revealed approach as primary
- If mixed methods, specify primary + note mixed character
- Confidence affects Track A quality gating:
  - LOW confidence → MODERATE quality state (caveated assessment)
  - HIGH/MEDIUM confidence → Enables HIGH quality state (if other factors good)

---

### mixed_method_characterisation

**Purpose:** Provide qualitative description of mixed-method research

**Fields:**

- `is_mixed`: Boolean indicating if characterisation applies
- `primary_approach`: Dominant approach
- `secondary_approaches`: Array of additional approaches
- `qualifications`: Qualitative descriptions (NOT percentages)
- `section_breakdown`: Optional section-by-section breakdown

**When is_mixed = false:**

```json
{
  "is_mixed": false
}
```

**AVOID:**

- Percentage precision ("60% inductive, 40% deductive")
- Forcing single category when mixed is more accurate

---

### transparency_assessment

**Purpose:** Assess methodological transparency as input to Track A and Transparency signal

**Fields:**

- `expressed_methodology_present`: Boolean
- `transparency_quality`: HIGH/MODERATE/LOW
- `transparency_notes`: Explanation

**Affects:**

- Track A classification confidence dimension
- Transparency signal baseline assessment
- Credibility report methodological considerations section

---

### credibility_framework

**Purpose:** Specify which assessment framework and signal priorities to use

**Fields:**

- `framework_to_use`: The assessment framework for this paper
- `signal_prioritisation`: Which signals to emphasise
  - `primary_signals`: 3-4 signals most relevant to this approach
  - `secondary_signals`: 2-3 signals of moderate importance
  - `deemphasised_signals`: Signals to assess but not emphasise (may be empty)
  - `rationale`: Why this prioritisation

**See `assessment-frameworks.md` for framework selection logic.**

---

### taxonomy_feedback

**Purpose:** Enable iterative taxonomy refinement by documenting category fit quality and proposing new categories

**Optional:** Always present but may have null values if fit is excellent/good

**Fields:**

- `category_fit_quality`: How well paper fits existing taxonomy
  - `excellent`: Paper clearly matches one category, no ambiguity
  - `good`: Paper fits one category with minor reservations
  - `acceptable`: Paper can be classified but feels like edge case
  - `poor`: Paper doesn't fit well, forced into closest category
- `proposed_new_category`: Name for proposed category (null if fit ≥ acceptable)
- `rationale_for_proposal`: Why existing taxonomy inadequate
- `characteristics_of_proposed_category`: Defining features of proposed type
- `alternative_papers_that_might_fit`: Papers in corpus that might share this category

**When to propose new categories:**

- Paper has characteristics fundamentally different from existing 4 types
- Classification requires extensive qualifications that undermine utility
- Paper serves purpose not captured by existing taxonomy
- Can identify 2+ papers that would fit new category
- New category would have distinct credibility criteria

**Example (Excellent Fit):**

```json
{
  "taxonomy_feedback": {
    "category_fit_quality": "excellent",
    "proposed_new_category": null,
    "rationale_for_proposal": null,
    "characteristics_of_proposed_category": null,
    "alternative_papers_that_might_fit": []
  }
}
```

**Example (Poor Fit with Proposal):**

```json
{
  "taxonomy_feedback": {
    "category_fit_quality": "poor",
    "proposed_new_category": "comparative_methods_paper",
    "rationale_for_proposal": "This paper systematically compares multiple existing radiocarbon calibration methods. It's distinct from methodological papers (which present single methods) and empirical papers (methods are subject, not tools). Systematic method comparison is a distinct research genre with specific credibility criteria (fair comparison, appropriate evaluation metrics).",
    "characteristics_of_proposed_category": "Systematic comparison of 2+ existing methods. Evaluation criteria explicitly defined. Performance assessment across methods. Recommendations for method selection based on use case. No new method development (distinguishes from methodological). No substantive research question (distinguishes from empirical).",
    "alternative_papers_that_might_fit": [
      "penske-et-al-2023 (if it compares DNA extraction protocols)",
      "Any papers comparing pottery classification frameworks",
      "Papers benchmarking spatial analysis methods"
    ]
  }
}
```

**Your role:** During Phase 1 testing (v2.1-alpha), honest assessment of category fit helps refine taxonomy. User reviews proposals between test cycles.

**See `approach-taxonomy.md` Section "Taxonomy Evolution and Feedback" for detailed guidance**

---

## Schema Version History

**v2.1 (2025-11-17):**

- Added `paper_type` and `paper_type_justification` fields
- Added `methodological_characterisation` object (conditional for methodological papers)
- Added `taxonomy_feedback` object for iterative taxonomy refinement
- Extended `credibility_framework.framework_to_use` to include `methodological_paper`
- Updated rationale field to reference "approach and paper type"

**v2.0 (2025-11-17):**

- Added `confidence` fields to expressed and revealed approaches
- Enhanced `transparency_assessment` structure
- Added `classification_metadata` for reproducibility
- Refined `mismatch_type` categories

**v1.0 (2025-11-16):**

- Initial schema definition

---

## Example Complete Output

```json
{
  "classification_metadata": {
    "classified_after_pass": 6,
    "classification_date": "2025-11-17",
    "classifier_version": "v0.2-alpha"
  },

  "expressed_approach": {
    "approach": "inductive",
    "evidence": [
      "Introduction states: 'This exploratory study documents settlement patterns in the Vardar valley'",
      "Methods: 'Systematic field survey to identify previously unknown sites'",
      "RDMAP research_design: 'exploratory survey'"
    ],
    "source_sections": ["introduction", "methods"],
    "confidence": "high"
  },

  "revealed_approach": {
    "approach": "inductive",
    "evidence": {
      "claims_structure": "Pattern descriptions: 'settlements cluster within 2km of rivers', 'site density increases in valley bottoms'",
      "methods_application": "Systematic field walking at 20m transect intervals; opportunistic site documentation",
      "analytical_workflow": "Survey → site documentation → spatial analysis → pattern description → interpretation"
    },
    "confidence": "high"
  },

  "expressed_vs_revealed": {
    "alignment": "matched",
    "harking_flag": false,
    "mismatch_explanation": "Paper explicitly states exploratory survey design and actually conducts exploratory research. Methodological transparency is high."
  },

  "primary_classification": {
    "approach": "inductive",
    "confidence": "high",
    "justification": "This is clearly inductive research. The paper explicitly states an exploratory aim, uses systematic survey methods appropriate for pattern discovery, and frames claims as pattern descriptions rather than hypothesis tests. No pre-specified predictions; patterns emerge from data. Classification is unambiguous."
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
      "secondary_signals": ["validity", "replicability", "plausibility"],
      "deemphasised_signals": [],
      "rationale": "Inductive research emphasis: workflow transparency, pattern clarity, and appropriate scope constraint are most critical for exploratory survey research."
    }
  },

  "classification_notes": "Straightforward inductive survey. No ambiguities or edge cases."
}
```

---

## Integration with Other Outputs

**Classification feeds into:**

1. **Track A quality assessment:** `primary_classification.confidence` affects classification confidence dimension
2. **Signal cluster prompts:** `credibility_framework.signal_prioritisation` guides emphasis
3. **Report generation:** `primary_classification.approach` determines narrative structure and anchor selection
4. **assessment.json:** Classification consolidated into canonical assessment output

---

## Validation Checklist

**Before outputting classification.json:**

- [ ] `paper_type` determined with justification
- [ ] If paper_type = "methodological", `methodological_characterisation` populated
- [ ] `taxonomy_feedback.category_fit_quality` assessed
- [ ] If category_fit_quality = "poor", taxonomy proposal populated
- [ ] All required fields populated (expressed_approach, revealed_approach, primary_classification)
- [ ] If alignment = "mismatched", harking_flag and mismatch_type present
- [ ] If is_mixed = true, mixed_method_characterisation complete
- [ ] credibility_framework.signal_prioritisation matches approach AND paper type (see assessment-frameworks.md)
- [ ] Justification cites specific evidence from extraction
- [ ] Confidence levels assigned consistently
- [ ] If expressed_approach = "none_stated", contextual interpretation provided

---

## Related References

- `approach-taxonomy.md` - Research approach definitions
- `harking-detection-guide.md` - Expressed vs revealed comparison guidance
- `assessment-frameworks.md` - Framework selection and signal prioritisation
- `track-a-quality-criteria.md` - Classification confidence affects quality gating
