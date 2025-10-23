# Research Assessment Schema v2.4 - Complete Guide

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

## Complete JSON Structure

```json
{
  "schema_version": "2.4",
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

**Required fields:**
- `evidence_id`: String matching pattern `E###` (E001, E002, ...)
- `evidence_text`: String describing the observation
- `evidence_type`: String (will evolve into controlled vocabulary)

**Key fields:**
- `evidence_basis`: Observable basis (`direct_measurement`, `statistical_output`, `observational_record`, etc.)
- `declared_uncertainty`: Author-stated uncertainty (ranges, confidence intervals)
- `expected_information_missing`: Information we would expect but is absent
- `supports_claims`: Array of claim IDs `["C001", "C005"]`
- `related_evidence`: Array for analytical views `["E002"]`
- `validates_methods`: Array of method IDs (NEW v2.4)
- `validates_protocols`: Array of protocol IDs (NEW v2.4)
- `location`: `{section, page, paragraph}`
- `verbatim_quote`: Exact text from paper
- `consolidation_metadata`: Traceability for consolidated items

**Example:**
```json
{
  "evidence_id": "E001",
  "evidence_text": "Survey collected 8,343 features across 22 sites",
  "evidence_type": "quantitative_observation",
  "evidence_basis": "direct_measurement",
  "supports_claims": ["C015"],
  "location": {"section": "Results", "page": 8, "paragraph": 2},
  "verbatim_quote": "The mobile platform enabled collection of 8,343 features across 22 sites"
}
```

## Claim Object

**Purpose:** Assertions that interpret, frame, or generalize from evidence

**Required fields:**
- `claim_id`: String matching pattern `C###`
- `claim_text`: String stating the assertion
- `claim_type`: `empirical | interpretation | methodological_argument | theoretical`

**Key fields:**
- `claim_role`: `core | intermediate | supporting | synthesis` (important but not required)
- `primary_function`: Purpose of claim (`empirical_pattern`, `causal_explanation`, `methodological_justification`, etc.)
- `claim_nature`: Nature of claim (`descriptive`, `comparative`, `causal`, `evaluative`, etc.)
- `supported_by`: Array of evidence IDs `["E001", "E003"]`
- `supported_by_claims`: Array of supporting claim IDs
- `supports_claims`: Array of claims this supports
- `supports_method`: Method ID this justifies (NEW v2.4, for methodological_argument type)
- `supports_protocol`: Protocol ID this justifies (NEW v2.4)
- `supports_design`: Design ID this justifies (NEW v2.4)
- `implicit_assumptions`: Array of implicit argument IDs `["IA001"]`
- `author_confidence`: `definite | probable | speculative | hedged`
- `expected_information_missing`: Gaps in justification
- `location`: `{section, page, paragraph}`
- `verbatim_quote`: Exact text from paper
- `consolidation_metadata`: Traceability for consolidated items

**Example:**
```json
{
  "claim_id": "C015",
  "claim_text": "Mobile platform enabled large-scale data collection with minimal supervision",
  "claim_type": "interpretation",
  "claim_role": "intermediate",
  "primary_function": "empirical_pattern",
  "supported_by": ["E001", "E012"],
  "supports_claims": ["C001"],
  "location": {"section": "Discussion", "page": 12, "paragraph": 1},
  "verbatim_quote": "The FAIMS platform enabled large-scale collection across sites with minimal supervision"
}
```

## Implicit Argument Object

**Purpose:** Unstated assumptions, logical implications, bridging claims

**Required fields:**
- `implicit_id`: String matching pattern `IA###` (IA001, IA002, ...)
- `implicit_text`: Statement of the implicit content
- `type`: Enum of implicit argument types

**Types:**
- `logical_implication`: IF explicit claims true THEN X must be true
- `unstated_assumption`: Prerequisites assumed without acknowledgment
- `bridging_claim`: Missing links between evidence and conclusions
- `design_assumption`: Assumptions about research design choices (NEW v2.4)
- `methodological_assumption`: Assumptions about method validity (NEW v2.4)
- `disciplinary_assumption`: Shared disciplinary knowledge or paradigmatic commitments

**Key fields:**
- `enables_claim`: Array of claim IDs this argument enables
- `connects_evidence`: Array of evidence IDs this argument connects
- `supports_design`: Design ID this assumes (NEW v2.4)
- `supports_method`: Method ID this assumes (NEW v2.4)
- `supports_protocol`: Protocol ID this assumes (NEW v2.4)
- `reasoning`: Why we infer this implicit content
- `necessity`: `critical | important | minor`
- `author_awareness`: `likely_aware | possibly_aware | likely_unaware`
- `disciplinary_context`: Relevant discipline if applicable
- `conflicts_of_interest`: Array of potential COIs
- `extraction_confidence`: `high | medium | low`

**Example:**
```json
{
  "implicit_id": "IA001",
  "implicit_text": "GPS accuracy is sufficient for archaeological survey purposes at this scale",
  "type": "methodological_assumption",
  "enables_claim": ["C008"],
  "supports_method": "M003",
  "reasoning": "Claim asserts GPS-based mapping was accurate, but never states precision requirements or validates adequacy",
  "necessity": "important",
  "author_awareness": "likely_aware",
  "disciplinary_context": "archaeology",
  "extraction_confidence": "high"
}
```

## Research Design Object

**Purpose:** Strategic decisions about WHY research was framed this way

**Required fields:**
- `design_id`: String matching pattern `RD###`
- `design_text`: Description of the design decision
- `design_type`: `research_framing | theoretical_framework | study_design | scope_definition | positionality`

**Design types explained:**
- `research_framing`: Research questions, hypotheses, emergent findings
- `theoretical_framework`: Conceptual framework guiding research
- `study_design`: Overall research design (comparative, case study, etc.)
- `scope_definition`: Geographic, temporal, or topical boundaries
- `positionality`: Researcher stance and reflexivity

**Key fields:**
- `enables_methods`: Array of method IDs this design enables
- `reasoning_approach`: Object with `approach` field (`inductive`, `deductive`, `abductive`, `mixed`)
- `hypothesis_timing`: Object describing when hypotheses formulated
- `implicit_assumptions`: Array of implicit argument IDs
- `justification_claim`: Claim justifying this design choice
- `expected_information_missing`: Missing design documentation
- `location`: `{section, page, paragraph}`
- `verbatim_quote`: Exact text from paper

**Example:**
```json
{
  "design_id": "RD001",
  "design_text": "Comparative study of mobile vs traditional data collection effectiveness",
  "design_type": "study_design",
  "study_design": {
    "design_type": "comparative",
    "rationale": "Test mobile platform effectiveness against traditional methods"
  },
  "enables_methods": ["M003", "M008"],
  "reasoning_approach": {
    "approach": "abductive",
    "explanation": "Iterative refinement based on field observations"
  },
  "location": {"section": "Methods", "page": 4, "paragraph": 1}
}
```

## Method Object

**Purpose:** Tactical approaches about WHAT was done at high level

**Required fields:**
- `method_id`: String matching pattern `M###`
- `method_text`: Description of the method
- `method_type`: `data_collection | sampling | analysis | quality_control | validation`

**Key fields:**
- `implements_designs`: Array of design IDs this method implements
- `realized_through_protocols`: Array of protocol IDs implementing this method
- `validated_by_evidence`: Array of evidence IDs validating this method
- `complements_methods`: Array of related method IDs
- `justification_claim`: Claim ID justifying method choice
- `opportunistic_decisions`: Array describing field adaptations (NEW v2.4)
- `expected_information_missing`: Missing method documentation
- `location`: `{section, page, paragraph}`
- `verbatim_quote`: Exact text from paper

**Example:**
```json
{
  "method_id": "M008",
  "method_text": "Mobile platform (FAIMS) for field data collection",
  "method_type": "data_collection",
  "implements_designs": ["RD001"],
  "realized_through_protocols": ["P023", "P024"],
  "validated_by_evidence": ["E046"],
  "justification_claim": "C027",
  "location": {"section": "Methods", "page": 5, "paragraph": 2}
}
```

## Protocol Object

**Purpose:** Operational procedures about HOW specifically it was done

**Required fields:**
- `protocol_id`: String matching pattern `P###`
- `protocol_text`: Detailed procedure description
- `protocol_type`: Type of protocol (e.g., `recording`, `measurement`, `analysis_procedure`)

**Key fields:**
- `implements_methods`: Array of method IDs this protocol implements
- `produces_evidence`: Array of evidence IDs produced by this protocol
- `sub_protocols`: Array of protocol IDs for sub-procedures
- `tools`: Array of tool/instrument objects with `tool_name`, `version`, `configuration`
- `measurement_specification`: Object with detailed measurement parameters
- `decision_rules`: Array of decision-making procedures
- `quality_control`: Array of QC procedures
- `expected_information_missing`: Missing protocol documentation
- `location`: `{section, page, paragraph}`
- `verbatim_quote`: Exact text from paper

**Example:**
```json
{
  "protocol_id": "P023",
  "protocol_text": "FAIMS Mobile v2.6 configured for archaeological survey with custom recording module",
  "protocol_type": "recording",
  "tools": [{
    "tool_name": "FAIMS Mobile",
    "version": "2.6",
    "configuration": "Custom archaeological recording module"
  }],
  "implements_methods": ["M008"],
  "produces_evidence": ["E045"],
  "measurement_specification": {
    "domain": "Archaeological feature documentation",
    "instrument": "Samsung Galaxy Tab A tablets",
    "metric": "Structured data fields (type, dimensions, material, condition)",
    "precision": "Feature type classification, centimeter-level dimensions",
    "observer": "Trained survey team members"
  },
  "location": {"section": "Methods", "page": 6, "paragraph": 2}
}
```

## Cross-Reference Architecture

All cross-references use simple string ID arrays:

**Claims reference evidence:**
```json
"supported_by": ["E001", "E003", "E012"]
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
// Evidence validates methods/protocols
"validates_methods": ["M008"]
"validates_protocols": ["P023"]

// Method justified by claim
"justification_claim": "C027"

// Claim supports RDMAP
"supports_method": "M003"
"supports_protocol": "P015"
"supports_design": "RD001"

// Implicit arguments
"enables_claim": ["C008"]
"supports_method": "M003"
```

## Consolidation Metadata

All consolidated items must include:

```json
"consolidation_metadata": {
  "consolidation_performed": true,
  "consolidated_from": ["P1_E001", "P1_E002"],
  "consolidation_type": "granularity_reduction | compound_finding | analytical_view | ...",
  "information_preserved": "complete | lossy_granularity | lossy_redundancy",
  "granularity_available": "Description of additional detail available in source",
  "rationale": "Why consolidation was appropriate"
}
```

## Location Tracking

All objects include location for traceability:

```json
"location": {
  "section": "Methods",
  "page": 5,
  "paragraph": 2,
  "line_numbers": "45-48"  // optional
}
```

## Verbatim Quotes

All objects should include verbatim quotes from the source:

```json
"verbatim_quote": "Exact text from paper that supports this extraction"
```

## For Complete Schema

**Full JSON schema:** `extraction_schema.json` (v2.4, updated 2025-10-19)

Contains complete field definitions, types, constraints, and validation rules for all object types. Consult for:
- Comprehensive field lists
- Enum value definitions
- Conditional fields (e.g., research_framing when design_type = "research_framing")
- Complex nested structures
- Validation patterns