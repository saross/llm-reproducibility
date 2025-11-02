# Research Assessment Schema v2.5 - Complete Guide

## Overview

This schema defines six object types for extracting research methodology and argumentation:

**Claims & Evidence:**
- `evidence` - Raw observations, measurements, data
- `claims` - Assertions that interpret or generalize
- `implicit_arguments` - Unstated assumptions and logical implications

**RDMAP (Research Design, Methods, Protocols):**
- `research_designs` - Strategic decisions (WHY research framed this way)
- `methods` - Tactical approaches (WHAT was done at high level)
- `protocols` - Operational procedures (HOW specifically implemented)

---

## Schema v2.5 Updates: Hallucination Prevention

**Version 2.5 introduces mandatory sourcing requirements to prevent fabricated content.**

### Critical Changes

**For Evidence & Claims (Explicit Content):**
- `verbatim_quote` now **REQUIRED** (was optional in v2.4)
- Must contain exact text from paper stating this content
- If quote doesn't exist → don't extract the item
- Verification: Can you point to the exact sentence that says this?

**For Implicit Arguments (Implicit Content):**
- `trigger_text` array **REQUIRED** - verbatim passages that imply the argument
- `trigger_locations` array **REQUIRED** - parallel to trigger_text, one location per passage
- `inference_reasoning` **REQUIRED** - explanation connecting triggers to argument
- Must have passages that together imply the argument
- Verification: Can you point to specific passages that together support this inference?

**For RDMAP Objects (Design/Method/Protocol):**

*Explicit RDMAP (status = "explicit"):*
- Documented in Methods section with procedural details
- Requires `verbatim_quote` from Methods section
- Status field: `design_status`, `method_status`, or `protocol_status` = `"explicit"`

*Implicit RDMAP (status = "implicit"):*
- NOT documented in Methods section
- Either mentioned but undocumented, OR inferred from Results/Discussion
- Requires `trigger_text` + `trigger_locations` + `inference_reasoning`
- Requires `implicit_metadata` object (basis, transparency_gap, assessability_impact, reconstruction_confidence)
- Status field set to `"implicit"`

**Source Verification:**
- All items have `source_verification` object for Pass 3 validation
- Tracks: location_verified, quote_verified, content_aligned
- Enables automated quality checks

### Why This Matters

**The hallucination problem:** LLMs may fabricate plausible-sounding details rather than faithfully extracting what papers state. v2.5 requires rigorous sourcing discipline:

- **Cannot extract without source:** Every item must have verbatim_quote OR trigger_text
- **Location tracking:** Every source must have precise location
- **Verification enabled:** Pass 3 can validate all extractions systematically
- **Zero tolerance:** Fabricated content is catastrophic for credibility assessment

---

## Complete JSON Structure

```json
{
  "schema_version": "2.5",
  "extraction_timestamp": "ISO 8601 datetime",
  "extractor": "Claude Sonnet 4.5",
  
  "evidence": [evidence_object],
  "claims": [claim_object],
  "implicit_arguments": [implicit_argument_object],
  
  "research_designs": [research_design_object],
  "methods": [method_object],
  "protocols": [protocol_object],
  
  "project_metadata": {
    "timeline": {},
    "location": {},
    "resources": {},
    "track_record": {}
  },
  
  "extraction_notes": {
    "pass": 1 | 2 | 3,
    "section_extracted": "string",
    "known_uncertainties": ["string"]
  }
}
```

## Evidence Object

**Purpose:** Raw observations, measurements, or data requiring minimal interpretation

**Required fields (v2.5):**
- `evidence_id`: String matching pattern `E###` (E001, E002, ...)
- `evidence_text`: String describing the observation
- `evidence_type`: Enum of observation types
- `verbatim_quote`: **REQUIRED** - Exact text from paper stating this observation

**Key fields:**
- `location`: `{section, page, start_paragraph, end_paragraph}` - Where the verbatim_quote appears
- `source_verification`: Populated in Pass 3 (location_verified, quote_verified, content_aligned)
- `declared_uncertainty`: Author-stated uncertainty (ranges, confidence intervals)
- `expected_uncertainty_missing`: Uncertainty we would expect but is absent
- `supports_claims`: Array of claim IDs `["C001", "C005"]`
- `related_evidence`: Array for analytical views `["E002"]`
- `consolidation_metadata`: Traceability for consolidated items

**v2.5 Sourcing Rule:** If you cannot find a verbatim quote stating this observation, DO NOT extract it.

**Example:**
```json
{
  "evidence_id": "E001",
  "evidence_text": "Survey collected 8,343 features across 22 sites",
  "evidence_type": "quantitative_observation",
  "verbatim_quote": "We collected 8,343 features across 22 sites during the survey",
  "location": {"section": "Results", "page": 8, "start_paragraph": 2, "end_paragraph": 2},
  "supports_claims": ["C015"],
  "source_verification": {
    "location_verified": true,
    "quote_verified": true,
    "content_aligned": true,
    "verified_by": "validator"
  }
}
```

## Claim Object

**Purpose:** Assertions that interpret, frame, or generalize from evidence

**Required fields (v2.5):**
- `claim_id`: String matching pattern `C###`
- `claim_text`: String stating the assertion
- `claim_type`: `empirical | interpretation | methodological_argument | theoretical`
- `claim_role`: `core | intermediate | supporting`
- `verbatim_quote`: **REQUIRED** - Exact text from paper stating this claim

**Key fields:**
- `location`: Where the verbatim_quote appears
- `source_verification`: Populated in Pass 3
- `supported_by_evidence`: Array of evidence IDs `["E001", "E003"]`
- `supported_by_claims`: Array of supporting claim IDs
- `supports_claims`: Array of claims this supports
- `implicit_assumptions`: Array of implicit argument IDs `["IA001"]`
- `author_confidence`: `definite | probable | speculative | hedged`
- `expected_information_missing`: Gaps in justification

**v2.5 Sourcing Rule:** If you cannot find a verbatim quote stating this claim, DO NOT extract it.

**Example:**
```json
{
  "claim_id": "C015",
  "claim_text": "Mobile platform enabled large-scale data collection with minimal supervision",
  "claim_type": "interpretation",
  "claim_role": "intermediate",
  "verbatim_quote": "The mobile platform enabled us to collect data on a large scale with minimal field supervision",
  "location": {"section": "Discussion", "page": 12, "start_paragraph": 1, "end_paragraph": 1},
  "supported_by_evidence": ["E001", "E012"],
  "supports_claims": ["C001"],
  "source_verification": {
    "location_verified": true,
    "quote_verified": true,
    "content_aligned": true,
    "verified_by": "validator"
  }
}
```

## Implicit Argument Object

**Purpose:** Unstated assumptions, logical implications, bridging claims

**Required fields (v2.5):**
- `implicit_argument_id`: String matching pattern `IA###`
- `argument_text`: The unstated argument
- `type`: Type of implicit argument (see below)
- `trigger_text`: **REQUIRED** - Array of verbatim passages that together imply this argument
- `trigger_locations`: **REQUIRED** - Array of locations (parallel to trigger_text)
- `inference_reasoning`: **REQUIRED** - Explanation of how triggers support this inference

**Types:**
- `logical_implication`: IF explicit claims true THEN X must be true
- `unstated_assumption`: Prerequisites assumed without acknowledgment
- `bridging_claim`: Missing links between evidence and conclusions
- `design_assumption`: Assumptions about research design choices
- `methodological_assumption`: Assumptions about method validity

**Key fields:**
- `supports_claims`: Array of claim IDs this argument supports
- `disciplinary_context`: Domain where this assumption holds
- `source_verification`: Populated in Pass 3 (trigger verification)
- `confidence_in_inference`: How strongly triggers support inference

**v2.5 Sourcing Rule:** Must have multiple trigger passages that together imply (not state) the argument. If explicitly stated anywhere → extract as Claim, not Implicit Argument.

**Example:**
```json
{
  "implicit_argument_id": "IA001",
  "argument_text": "GPS accuracy is sufficient for archaeological survey purposes",
  "type": "methodological_assumption",
  "trigger_text": [
    "GPS units were used to record artifact locations",
    "spatial analysis conducted at site level",
    "precision adequate for landscape-scale interpretation"
  ],
  "trigger_locations": [
    {"section": "Methods", "start_paragraph": 2, "end_paragraph": 2},
    {"section": "Methods", "start_paragraph": 5, "end_paragraph": 5},
    {"section": "Discussion", "start_paragraph": 3, "end_paragraph": 3}
  ],
  "inference_reasoning": "Methods mentions GPS use without stating accuracy. Analysis at 'site level' and 'landscape-scale' interpretation suggest moderate precision sufficient for archaeological purposes. Together these passages imply GPS accuracy adequate, though never explicitly stated.",
  "supports_claims": ["C008"],
  "disciplinary_context": "archaeology",
  "source_verification": {
    "location_verified": true,
    "quote_verified": true,
    "content_aligned": true,
    "verified_by": "validator"
  }
}
```

## Research Design Object

**Purpose:** Strategic decisions about WHY research was framed this way

**Required fields:**
- `design_id`: String matching pattern `RD###`
- `design_text`: Description of the design decision
- `design_type`: `research_question | theoretical_framework | study_design | scope_definition | positionality`

**Schema v2.6.2 Simplification:**
Conditional objects (`research_framing`, `theoretical_framework`, `study_design`, `scope`, `positionality`) are **FULLY OPTIONAL**. You can create minimal Research Designs with just the three required fields above. Only populate conditional objects when detail is present and beneficial for assessment. This reduces consolidation pressure while preserving assessment capability for hypothesis timing, theoretical grounding, and design rationale.

**Key fields:**
- `enables_methods`: Array of method IDs this design enables
- `reasoning_approach`: `inductive | deductive | abductive | mixed`
- `hypothesis_timing`: When hypotheses were formulated
- `implicit_assumptions`: Design assumptions

**Example:**
```json
{
  "design_id": "RD001",
  "design_text": "Comparative study of mobile vs traditional data collection",
  "design_type": "study_design",
  "study_design": {
    "design_type": "comparative",
    "rationale": "Test mobile platform effectiveness"
  },
  "enables_methods": ["M003", "M008"],
  "reasoning_approach": {"approach": "abductive"}
}
```

## Method Object

**Purpose:** Tactical approaches about WHAT was done at high level

**Required fields:**
- `method_id`: String matching pattern `M###`
- `method_text`: Description of the method
- `method_type`: `data_collection | sampling | analysis | quality_control | validation`

**Key fields:**
- `implements_designs`: Which designs this method implements
- `realized_through_protocols`: Which protocols implement this method
- `validated_by_evidence`: Evidence of method effectiveness
- `justification_claim`: Claim justifying method choice

**Example:**
```json
{
  "method_id": "M008",
  "method_text": "Mobile platform (FAIMS) for field data collection",
  "method_type": "data_collection",
  "implements_designs": ["RD001"],
  "realized_through_protocols": ["P023", "P024"],
  "validated_by_evidence": ["E046"]
}
```

## Protocol Object

**Purpose:** Operational procedures about HOW specifically it was done

**Required fields:**
- `protocol_id`: String matching pattern `P###`
- `protocol_text`: Detailed procedure description
- `protocol_type`: Type of protocol

**Key fields:**
- `implements_methods`: Which method(s) this protocol implements
- `produces_evidence`: Evidence produced by this protocol
- `tools`: Array of tools/instruments used
- `measurement_specification`: Detailed measurement parameters

**Example:**
```json
{
  "protocol_id": "P023",
  "protocol_text": "FAIMS Mobile v2.6 configured for archaeological survey",
  "protocol_type": "recording",
  "tools": [{
    "tool_name": "FAIMS Mobile",
    "version": "2.6",
    "configuration": "Custom archaeological module"
  }],
  "implements_methods": ["M008"],
  "produces_evidence": ["E045"]
}
```

---

## Canonical Field Names (Schema v2.5)

**IMPORTANT:** Use these canonical field names. Do not use variants from older extractions or schema versions.

### RDMAP Relationship Fields

**Research Design → Method connections:**

✓ **Correct:** `implemented_by_methods` (array of method IDs)
❌ **Deprecated:** `child_methods`, `enables_methods`, `supported_by_methods`

```json
{
  "design_id": "RD001",
  "implemented_by_methods": ["M003", "M008"]
}
```

**Method → Design connections (reverse):**

✓ **Correct:** `implements_designs` (array of design IDs)
❌ **Deprecated:** `linked_designs`, `design_context`

**Method → Protocol connections:**

✓ **Correct:** `realized_through_protocols` (array of protocol IDs)
❌ **Deprecated:** `child_protocols`, `implemented_by_protocols`

```json
{
  "method_id": "M008",
  "implements_designs": ["RD001"],
  "realized_through_protocols": ["P023"]
}
```

**Protocol → Method connections (reverse):**

✓ **Correct:** `implements_methods` (array of method IDs, PLURAL)
❌ **Deprecated:** `implements_method` (singular), `linked_methods`

```json
{
  "protocol_id": "P023",
  "implements_methods": ["M008"]
}
```

### Claims-Evidence Relationship Fields

**Claims → Evidence connections:**

✓ **Correct:** `supported_by` (array of evidence IDs)
❌ **Deprecated:** `supported_by_evidence`, `supporting_evidence`

```json
{
  "claim_id": "C001",
  "supported_by": ["E001", "E002"]
}
```

**Evidence → Claims connections (reverse):**

✓ **Correct:** `supports_claims` (array of claim IDs)

```json
{
  "evidence_id": "E001",
  "supports_claims": ["C001", "C005"]
}
```

### Bidirectional Consistency Requirements

**All relationship fields must be bidirectionally consistent:**

**Rule:** If A references B in forward direction, then B must reference A in reverse direction.

**Examples:**

If `C001.supported_by = ["E001"]`
Then `E001.supports_claims` must include `"C001"`

If `M003.implements_designs = ["RD001"]`
Then `RD001.implemented_by_methods` must include `"M003"`

If `P023.implements_methods = ["M008"]`
Then `M008.realized_through_protocols` must include `"P023"`

**Validation:** Run `extraction-system/scripts/validate_bidirectional.py` to check consistency before finalising extraction. This validator will catch:
- Forward references without reverse references
- Reverse references without forward references
- References to non-existent IDs
- Inconsistent mappings after consolidation

**Consolidation Impact:** When consolidating items (Pass 2+), you MUST update both forward and reverse references. See `consolidation-patterns.md` "Cross-Reference Repair" section for detailed procedure.

---

## RDMAP Explicit vs Implicit (v2.5)

**All RDMAP objects (Research Design, Method, Protocol) have status fields in v2.5:**
- `design_status`, `method_status`, or `protocol_status`
- Values: `"explicit"` | `"implicit"`

### Explicit RDMAP (status = "explicit")

**Documented in Methods section with procedural details**

**Sourcing requirements:**
- Must have `verbatim_quote` from Methods section
- Location should be in Methods (or subsections)
- Verification: Same 3-step process as Evidence & Claims

**Example - Explicit Method:**
```json
{
  "method_id": "M003",
  "method_text": "Systematic pedestrian survey using 50m wide transects with complete surface coverage",
  "method_type": "data_collection",
  "method_status": "explicit",
  "verbatim_quote": "Teams conducted systematic pedestrian survey walking 50m wide transects to ensure complete surface coverage of each site",
  "location": {"section": "Methods", "subsection": "Survey Strategy", "start_paragraph": 2, "end_paragraph": 2},
  "source_verification": {
    "location_verified": true,
    "quote_verified": true,
    "content_aligned": true,
    "verified_by": "validator"
  }
}
```

### Implicit RDMAP (status = "implicit")

**NOT documented in Methods section**

Two types of implicit RDMAP:
1. **mentioned_undocumented**: Tool/approach named but details not provided
2. **inferred_from_results**: Never mentioned, inferred from outputs/results

**Sourcing requirements:**
- Must have `trigger_text` array (passages implying procedure)
- Must have `trigger_locations` array (parallel to trigger_text)
- Must have `inference_reasoning` (explanation of inference)
- Must have `implicit_metadata` object (basis, transparency_gap, assessability_impact, reconstruction_confidence)
- Verification: Same 3-step process as Implicit Arguments

**Example - Implicit Protocol (mentioned_undocumented):**
```json
{
  "protocol_id": "P015",
  "protocol_text": "Standard consumer GPS procedures with estimated ±5-10m horizontal accuracy typical of handheld units without differential correction",
  "protocol_type": "recording",
  "protocol_status": "implicit",
  "trigger_text": [
    "handheld GPS units were used",
    "Spatial accuracy adequate for site-level analysis"
  ],
  "trigger_locations": [
    {"section": "Methods", "start_paragraph": 1, "end_paragraph": 1},
    {"section": "Discussion", "start_paragraph": 3, "end_paragraph": 3}
  ],
  "inference_reasoning": "Methods mentions handheld GPS but provides no accuracy specifications, calibration procedures, or equipment models. Discussion states accuracy 'adequate for site-level analysis' suggesting general-purpose consumer GPS. Standard consumer handheld GPS (without differential correction) provides ±5-10m accuracy, consistent with 'site-level' spatial resolution.",
  "implicit_metadata": {
    "basis": "mentioned_undocumented",
    "transparency_gap": "GPS units mentioned but no documentation of: equipment models, accuracy requirements, calibration procedures, differential correction use, or quality control checks",
    "assessability_impact": "Cannot verify equipment specifications or assess data quality procedures. Cannot determine if accuracy claims match equipment capabilities.",
    "reconstruction_confidence": "medium"
  },
  "implements_methods": ["M003"],
  "source_verification": {
    "location_verified": true,
    "quote_verified": true,
    "content_aligned": true,
    "verification_notes": "Implicit protocol reasonably inferred from triggers. Conservative reconstruction appropriate.",
    "verified_by": "validator"
  }
}
```

**Example - Implicit Protocol (inferred_from_results):**
```json
{
  "protocol_id": "P018",
  "protocol_text": "Sub-meter GPS accuracy achieved through differential correction or high-precision receivers",
  "protocol_type": "measurement",
  "protocol_status": "implicit",
  "trigger_text": [
    "coordinate accuracy of ±0.5m reported",
    "precision suitable for feature-level analysis"
  ],
  "trigger_locations": [
    {"section": "Results", "start_paragraph": 1, "end_paragraph": 1},
    {"section": "Results", "start_paragraph": 4, "end_paragraph": 4}
  ],
  "inference_reasoning": "Results report 0.5m accuracy but Methods doesn't explain how achieved. This precision exceeds standard consumer GPS (±5-10m), requiring either differential correction or survey-grade equipment. Cannot determine which without documentation.",
  "implicit_metadata": {
    "basis": "inferred_from_results",
    "transparency_gap": "Methods section completely silent on GPS procedures. Precision of 0.5m cannot be achieved with consumer GPS, implying specialized equipment or correction, but no procedures documented.",
    "assessability_impact": "Cannot assess which high-precision approach used. Cannot evaluate equipment quality, calibration practices, or whether accuracy claims realistic for chosen method.",
    "reconstruction_confidence": "low"
  },
  "source_verification": {
    "location_verified": true,
    "quote_verified": true,
    "content_aligned": true,
    "verification_notes": "Precision mentioned implies specialized procedures but inference weak. Reconstruction confidence appropriately low.",
    "verified_by": "validator"
  }
}
```

**Critical distinction:**
- Explicit RDMAP: "Here's what we did" (verbatim_quote)
- Implicit RDMAP: "Here's what they must have done based on clues" (trigger_text + inference)

---

## Cross-Reference Architecture

All cross-references use simple string ID arrays:

**Claims reference evidence:**
```json
"supported_by_evidence": ["E001", "E003", "E012"]
```

**Evidence references claims:**
```json
"supports_claims": ["C015", "C027"]
```

**RDMAP hierarchy:**
```json
// Design enables methods
"enables_methods": ["M003", "M007"]

// Method implements designs and uses protocols
"implements_designs": ["RD001"]
"realized_through_protocols": ["P011", "P012"]

// Protocol implements methods
"implements_methods": ["M003"]
```

**Cross-domain references:**
```json
// Method validated by evidence
"validated_by_evidence": ["E046"]

// Method justified by claim
"justification_claim": "C027"

// Claim supports method
"supports_method": "M003"
```

## Consolidation Metadata

All consolidated items must include:

```json
"consolidation_metadata": {
  "consolidated_from": ["P1_E001", "P1_E002"],
  "consolidation_type": "granularity_reduction | compound_finding | ...",
  "information_preserved": "complete | lossy_granularity | lossy_redundancy",
  "granularity_available": "Description of finer detail in source",
  "rationale": "Why consolidation was appropriate"
}
```

## Location Tracking

All objects include location for traceability:

```json
// Single paragraph
"location": {
  "section": "Methods",
  "page": 5,
  "start_paragraph": 2,
  "end_paragraph": 2,
  "sentence": 3  // optional
}

// Paragraph range (content spans paragraphs 2-4)
"location": {
  "section": "Results",
  "page": 8,
  "start_paragraph": 2,
  "end_paragraph": 4
}
```

**Note:** For single paragraphs, `start_paragraph` equals `end_paragraph`. For ranges, `end_paragraph` > `start_paragraph` indicates content spanning multiple consecutive paragraphs.

## For Complete Schema

Full JSON schema definitions with all fields, types, and constraints are available in:
- `extraction_schema_v2.5.json` - Complete unified schema (Evidence, Claims, Implicit Arguments, RDMAP)
- See also: `extraction-fundamentals.md` (sourcing requirements)
- See also: `verification-procedures.md` (Pass 3 validation)

The complete schema is in the project knowledge and can be consulted for comprehensive field definitions.
