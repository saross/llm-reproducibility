# Claims Extraction Prompt v2.1
**For extracting evidence, claims, and implicit arguments from research papers**
**Last updated:** October 16, 2025 (v2.1 - Post-calibration refinements)

## Overview

You are extracting structured information from a research paper to enable credibility assessment. Your task is to identify:
1. **Evidence** - observations, measurements, data points
2. **Claims** - assertions that require interpretation or evidence
3. **Implicit arguments** - unstated assumptions and logical implications

Work through the paper systematically, section by section. Focus on WHAT is claimed and HOW it's supported.

---

## Core Extraction Principles

### 1. Evidence vs. Claims Distinction

**EVIDENCE** = Minimal inference from raw data
- Direct observations, measurements, counts
- Raw data points
- Statements requiring little interpretation

**Examples:**
- "Students worked 189.4 hours" (from timestamps)
- "2567 BP Â±87" (radiocarbon date)
- "Pottery sherds from Layer 3"

**CLAIMS** = Require interpretive framing
- Bundle multiple observations
- Make causal/instrumental assertions
- Require boundary decisions or categorization

**Examples:**
- "The crowdsourcing approach produced 10,827 features with 57 staff-hours" (bundles evidence + frames causally)
- "The site was occupied in the Iron Age" (interprets pottery evidence)
- "This approach is more efficient" (evaluative interpretation)

**Key rule:** If an assertion requires you to make or recognize an interpretive move, it's a CLAIM. If it's a direct observation/measurement, it's EVIDENCE.

### 2. Dual-Layer Uncertainty Tracking

Track TWO types of uncertainty:

**LAYER 1: Author-Declared Uncertainty** (what the paper says)
- Bounded ranges: "800-600 BC", "50-65 hours"
- Error margins: "2567 BP Â±87", "14.2m Â±0.3m"
- Hedging language: "approximately", "ca.", "about", "estimated", "roughly"
- Confidence levels: "95% CI", "p<0.05", "high confidence"

**LAYER 2: Assessor-Expected Uncertainty** (what SHOULD be declared but isn't)
- Missing error margins on dates (C14 dates without Â±)
- False precision (stylistic date as "725 BC" instead of "ca. 725 BC" or "750-700 BC")
- Absent bounded ranges for estimates
- Overstated precision given measurement method

**Critical distinction:** 
- "2567 BP Â±87" â†’ good documentation, no flag
- "2567 BP" â†’ missing error margin, FLAG: should_have_error_margin=true
- "Iron Age pottery dated to 725 BC" â†’ false precision, FLAG: false_precision_flag=true

### 3. Hierarchical Organization (Four Levels)

Classify each claim by its role in the argument:

**1. CORE** (5-10 claims) - Main thesis arguments
- The central conclusions the paper seeks to establish
- Highest assessment priority
- Example: "Crowdsourcing is suitable for datasets of 10,000-60,000 features"

**2. INTERMEDIATE** (10-15 claims) - Major supporting arguments
- Build toward core claims
- Substantial interpretations that support the thesis
- Example: "The approach yields 190 features per staff-hour"

**3. SUPPORTING** (15-25 claims) - Specific findings and interpretations
- Detailed results and analyses
- Direct support for intermediate claims
- Example: "In 2017, 54 seconds average per feature"

**4. EVIDENCE** (30-50 items) - Observations and measurements
- Raw data points
- Direct observations
- Example: "125.8 person-hours of digitization work"

**Additional roles:**
- **BACKGROUND** - Context from literature (assessed via citations, not paper's evidence)
- **METHODOLOGICAL** - About methods (assessed for transparency and replicability)
- **TRANSITIONAL** - Narrative scaffolding (low priority)

### 4. Implicit Arguments

Extract unstated reasoning for HIGH-PRIORITY claims only:

**TYPE 1: Logical Implications** (extract these)
- Direct inferences the paper expects readers to make
- Example: "X is 3x faster than Y" â†’ [implicit: "X is more efficient"]

**TYPE 2: Unstated Assumptions** (extract these)
- Essential assumptions never stated
- Bridge claims that link evidence to conclusions
- Example: "Students prefer touch-screens" â†’ [implicit: "Preference affects performance"]

**TYPE 3: Deep Assumptions** (extract and label clearly)
- Disciplinary background knowledge
- Foundational economic/methodological principles  
- Meta-level framing assumptions
- Example: "More features = more value" (assumes completeness > selectivity)
- Example: "Efficiency is primary selection criterion" (frames decision-making)

Extract using same JSON format but mark type: "disciplinary_assumption"

These provide valuable context for assessment but are evaluated differently than Type 1/2 - they reveal underlying paradigms and values rather than specific logical gaps.

---

## Detailed Extraction Instructions

### For EVIDENCE:

```json
{
  "evidence_id": "E###",
  "observation": "[What was observed/measured]",
  
  // AUTHOR LAYER - What paper explicitly states
  "source": "[timestamps | journals | timesheets | calculation | measurement | literature | experiment | survey | interview | observation | reconstruction | inference]",
  "source_explicitness": "[explicit | inferred | ambiguous | assumed]",
  "confidence": "[direct_measurement | proxy_measurement | bounded_estimate | reconstruction | expert_judgment]",
  "confidence_notes": "[Explain evidence quality, acknowledge any limitations authors mention]",
  
  "declared_uncertainty": {
    "uncertainty_type": "[none_stated | bounded_range | error_margin | stylistic_range | confidence_interval | hedged_language]",
    "bounded_range": "[e.g., '800-600 BC', '50-65 hours']",
    "error_margin": "[e.g., 'Â±87', 'Â±2Ïƒ']",
    "point_estimate_with_error": "[e.g., '2567 BP Â±87']",
    "hedging_language": ["approximately", "ca.", "about"],
    "confidence_level": "[e.g., '95% CI', 'p<0.05']",
    "stated_limitations": ["Any limitations authors acknowledge"]
  },
  
  // ASSESSOR LAYER - Our evaluation
  "assessor_confidence": "[high | medium | medium-low | low]",
  "assessor_notes": "[Why we are/aren't confident about this evidence]",
  "information_gaps": [
    "[List what should be explained but isn't]",
    "[e.g., 'No bounded range despite proxy measurement']"
  ],
  "extraction_confidence": "[explicit | inferred | ambiguous | assumed]",
  "credibility_flags": ["[Any flags from the list]"],
  
  "expected_uncertainty": {
    "should_have_error_margin": [true/false],
    "should_have_range": [true/false],
    "missing_uncertainty_types": ["[What's missing]"],
    "false_precision_flag": [true/false],
    "assessor_notes": "[Why we expect uncertainty that wasn't declared]"
  },
  
  "implicit_evidence": {
    "evidence_type": "[author_observation | professional_judgment | team_consensus | disciplinary_knowledge | common_knowledge]",
    "explanation_provided": [true/false],
    "assessor_notes": "[Our interpretation]"
  },
  
  "location": {"section": "", "page": #, "paragraph": #},
  "verbatim_quote": "[Exact text from paper]"
}
```

### For CLAIMS:

```json
{
  "claim_id": "C###",
  "claim_text": "[The actual claim]",
  
  // CLASSIFICATION
  "claim_type": "[EMPIRICAL | INTERPRETATION | METHODOLOGICAL | THEORETICAL]",
  "claim_role": "[core | intermediate | supporting | evidence | background | transitional | methodological]",
  "claim_function": {
    "primary_function": "[premise | finding | conclusion | recommendation]",
    "secondary_function": "[premise | finding | conclusion | recommendation | none]"
  },
  "claim_scope": "[project | domain | general]",
  
  // NATURE
  "claim_nature": "[quantitative | qualitative | mixed | definitional]",
  "quantitative_details": {
    "source": "[measurement | calculation | estimate | statistical]",
    "confidence_basis": "[What gives confidence]",
    "bounded_range": "[If provided]",
    "arithmetic_verifiable": [true/false]
  },
  
  // AUTHOR LAYER
  "author_confidence": "[definite | probable | speculative | hedged]",
  "declared_uncertainty": {
    // Same structure as evidence
  },
  
  // ASSESSOR LAYER
  "assessment_priority": "[high | medium | low | not_assessed]",
  "assessor_confidence": "[high | medium | low]",
  "assessor_notes": "[Our evaluation]",
  "information_gaps": ["[Expected information not provided]"],
  "extraction_confidence": "[explicit | inferred | ambiguous]",
  "credibility_flags": ["[Any flags]"],
  "expected_uncertainty": {
    // Same structure as evidence
  },
  
  // COMPOSITION (for complex claims)
  "composed_of": {
    "evidence": ["E###", "E###"],
    "calculations": ["[Arithmetic operations]"],
    "boundary_decisions": ["[Definitional choices made]"],
    "causal_framing": "[How causality is framed]"
  },
  
  // RELATIONSHIPS
  "supports_claims": ["C###"],
  "supported_by_claims": ["C###", "E###"],
  "related_claims": {
    "alternatives": ["C###"],
    "qualifications": ["C###"],
    "contradicts": ["[Prior literature claims]"]
  },
  "implicit_arguments": ["IA###"],
  
  "location": {"section": "", "page": #, "paragraph": #},
  "verbatim_quote": "[Exact text]"
}
```

### For IMPLICIT ARGUMENTS:

Extract for HIGH-PRIORITY claims only (core and key intermediate claims):

```json
{
  "ia_id": "IA###",
  "argument": "[The implicit argument]",
  "type": "[logical_implication | unstated_assumption | bridging_claim | disciplinary_assumption]",
  "status": "[unstated_but_implied | assumed_without_acknowledgment | disciplinary_assumption]",
  "supports_claims": ["C###"],
  "assessment_notes": "[Why this matters for credibility]",
  "coi_note": "[Optional: Note if author COI affects interpretation]",
  "location": {"section": "", "page": #, "paragraph": #}
}
```

---

## Extraction Workflow

### STEP 1: Initial Scan
- Read the abstract and conclusion
- Identify the 5-10 CORE claims (main thesis)
- Note the paper's structure
- Check for any COI declarations (author affiliations, funding sources, platform developers)

### STEP 2: Section-by-Section Extraction

For each section:

1. **Identify Evidence First**
   - Look for observations, measurements, data points
   - Check for declared uncertainty (ranges, errors, hedging)
   - Note missing uncertainty that should be present
   - Extract source and confidence information

2. **Then Identify Claims**
   - Look for assertions that interpret/frame evidence
   - Classify by role (core/intermediate/supporting/evidence)
   - Identify what evidence supports each claim
   - Check for composed claims (bundles of evidence + framing)

3. **Check for Implicit Arguments** (high-priority claims only)
   - What logical implications are unstated?
   - What assumptions must be true for this claim to hold?
   - Are there bridging claims linking evidence to conclusions?
   - What disciplinary assumptions frame the argument?

4. **Map Relationships**
   - Which claims support which other claims?
   - Are there alternative scenarios?
   - Are there qualifications?
   - Does this contradict prior literature?

5. **Apply Expected Information Checklists**
   - For quantitative claims: method? error margins? sample size? precision justified?
   - For comparative claims: basis explicit? what held constant? fair comparison?
   - For methodological claims: choices justified? limitations acknowledged? alternatives considered?
   - For causal claims: mechanism explained? confounds addressed? alternatives ruled out?
   - For generalizability claims: scope explicit? evidence supports scope? boundaries acknowledged?

### STEP 3: Build Hierarchy
- Organize claims into four levels
- Verify support relationships
- Ensure core claims have clear evidential chains

### STEP 4: Quality Check
- Does each claim have a verbatim quote?
- Is uncertainty properly documented (both declared and expected)?
- Are information gaps identified?
- Are credibility flags appropriate?
- Do implicit arguments actually support high-priority claims?
- Note any relevant conflicts of interest if they affect interpretation of implicit arguments

---

## Expected Information Checklists

Use these to identify missing information:

### Quantitative Claims
â˜ Measurement method explained
â˜ Instrument specification or calibration mentioned
â˜ Error margins or confidence intervals provided
â˜ Sample size or n stated
â˜ Bounded ranges for estimates given
â˜ Precision justified given method
â˜ Units clearly stated

### Comparative Claims
â˜ Comparison basis made explicit
â˜ What is held constant specified
â˜ Alternative explanations considered
â˜ Fairness of comparison justified
â˜ Like-for-like comparison (not apples to oranges)

### Methodological Claims
â˜ Justification for choices provided
â˜ Limitations acknowledged
â˜ Alternatives considered
â˜ Verification evidence provided (or implicit evidence explained)
â˜ Replicability information included

### Causal Claims
â˜ Mechanism explained
â˜ Confounds addressed
â˜ Temporal precedence established
â˜ Alternative causes ruled out
â˜ Strength of causal language appropriate to evidence

### Generalizability Claims
â˜ Scope of generalization made explicit
â˜ Evidence supports claimed scope
â˜ Boundary conditions acknowledged
â˜ Population or domain clearly defined

---

## Credibility Flags

Use these standardized flags in the `credibility_flags` array:

- **TRANSPARENCY_GOOD** - Exemplary documentation of evidence/methods
- **TRANSPARENCY_PARTIAL** - Some information provided but gaps remain
- **TRANSPARENCY_INCOMPLETE** - Substantial missing information
- **PRECISION_OVERSTATED** - False precision given measurement method
- **MEASUREMENT_QUALITY_VARIABLE** - Mix of high and low quality measurements
- **SOURCE_UNCLEAR** - Can't determine where evidence comes from
- **UNCERTAINTY_UNACKNOWLEDGED** - Known limitations not discussed
- **IMPLICIT_EVIDENCE_UNEXPLAINED** - Based on author observation but not explained

---

## Common Pitfalls to Avoid

1. **Don't confuse transitional statements with claims**
   - "The next section discusses..." is not a claim
   - "This suggests that..." IS a claim

2. **Don't extract methods as claims unless argued for**
   - "We used ArcGIS" = method (not claim)
   - "ArcGIS proved difficult for novices" = claim about method

3. **Don't miss implicit uncertainty**
   - "2567 BP" without Â± = RED FLAG, not acceptable
   - "About 50 hours" = declared uncertainty, document the "about"

4. **Don't over-extract background claims**
   - If it's just citing literature for context, mark as background
   - Only extract if the paper's argument depends on it

5. **Don't ignore composed claims**
   - Complex claims bundle evidence + decisions + framing
   - Decompose these to reveal interpretive moves

6. **Don't forget location and verbatim quotes**
   - Every evidence/claim needs exact source location
   - Verbatim quotes enable verification

7. **Don't skip Type 3 deep assumptions**
   - These reveal underlying paradigms and values
   - Extract them even though they're assessed differently

---

## Output Format

Produce valid JSON following the schema structure. For each paper:

```json
{
  "paper_metadata": {
    "title": "",
    "authors": [],
    "year": ,
    "doi": "",
    "extraction_date": "",
    "extractor": ""
  },
  "evidence": [/* array of evidence objects */],
  "claims": [/* array of claim objects */],
  "implicit_arguments": [/* array of implicit argument objects */]
}
```

---

## Quality Criteria

Good extraction should:
- âœ… Clearly distinguish evidence from claims
- âœ… Document both declared and expected uncertainty
- âœ… Identify information gaps systematically
- âœ… Build clear hierarchical relationships
- âœ… Extract implicit arguments (Type 1, 2, AND 3) for high-priority claims
- âœ… Apply appropriate credibility flags
- âœ… Include verbatim quotes and precise locations
- âœ… Flag when evidence quality is variable or unclear
- âœ… Note relevant conflicts of interest when they affect interpretation

Remember: **The goal is to enable credibility assessment, not to assess credibility yourself. Extract the information needed for others to make informed judgments about the paper's claims.**