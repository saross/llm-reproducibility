#!/usr/bin/env python3
"""
Pass 3: RDMAP Extraction - Section 3 (Suitability of Preregistration for Archaeology)
Pages 7-8 (~1000 words)

Liberal extraction: Over-extract by 40-50%, will rationalize in Pass 5
Focus: Methods and protocols for applying preregistration to diverse archaeological contexts
"""

import json

# Load existing extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'r') as f:
    data = json.load(f)

# ============================================================================
# RESEARCH DESIGNS
# ============================================================================

research_designs = [
    # No explicit research designs in this section - focuses on methodological frameworks
]

# ============================================================================
# METHODS
# ============================================================================

methods = [
    {
        "id": "M007",
        "content": "Methodological taxonomy characterising archaeology as incorporating deductive, inductive, and abductive modes of inference",
        "method_type": "conceptual_framework",
        "verbatim_quote": "Archaeological research in fact features all three modes of inference: deductive, inductive, and abductive",
        "page_number": 7,
        "context": "Characterising archaeological reasoning diversity",
        "purpose": "Map the full range of inferential approaches in archaeology",
        "inputs": "archaeological_research_examples",
        "outputs": "three_part_methodological_classification",
        "assumptions": "Archaeological methods can be meaningfully classified by inferential mode"
    },
    {
        "id": "M008",
        "content": "Definitional method characterising abductive inference as 'inference to the best explanation' where hypotheses are generated and evaluated based on explanatory power",
        "method_type": "conceptual_framework",
        "verbatim_quote": "Abductive inference – so-called 'inference to the best explanation' – involves the generation, selection, and evaluation of candidate hypotheses based on their explanatory power",
        "page_number": 7,
        "context": "Defining key mode of archaeological reasoning",
        "purpose": "Clarify nature of abductive reasoning in archaeology",
        "inputs": "logical_and_philosophical_definitions",
        "outputs": "operational_definition_of_abduction",
        "assumptions": "Abduction is distinct from deduction and induction"
    },
    {
        "id": "M009",
        "content": "Methodological diversity framework characterising archaeological approaches along multiple axes: quantitative/qualitative, idiographic/nomothetic, inductive/deductive/abductive",
        "method_type": "conceptual_framework",
        "verbatim_quote": "Archaeological research is conducted along a quantitative–qualitative continuum and along an idiographic–nomothetic continuum, as well as featuring the three kinds of inference we have discussed",
        "page_number": 8,
        "context": "Comprehensive mapping of methodological diversity",
        "purpose": "Capture full complexity of archaeological method space",
        "inputs": "methodological_literature_and_practice_examples",
        "outputs": "multi_axis_methodological_classification",
        "assumptions": "Methodological diversity can be mapped along multiple independent dimensions"
    }
]

# ============================================================================
# PROTOCOLS
# ============================================================================

protocols = [
    {
        "id": "P005",
        "content": "Protocol for applying preregistration to abductive research: articulate in advance what candidate hypotheses will be generated, how they will be selected, and how they will be evaluated for explanatory power",
        "protocol_type": "methodological_procedure",
        "verbatim_quote": "Abductive inference – so-called 'inference to the best explanation' – involves the generation, selection, and evaluation of candidate hypotheses based on their explanatory power... Although the actual hypotheses cannot be predicted (otherwise it would not be a postdictive form of inquiry), the criteria of selection and evaluation can be articulated in advance",
        "page_number": 7,
        "context": "Adapting preregistration to abductive inquiry",
        "procedure_steps": [
            "Identify that research will use abductive inference",
            "Specify criteria for hypothesis generation",
            "Specify criteria for hypothesis selection",
            "Specify criteria for evaluating explanatory power",
            "Register criteria in advance (not actual hypotheses)"
        ],
        "inputs": "research_objectives_and_inferential_approach",
        "outputs": "preregistered_abductive_framework",
        "quality_control": "verification_of_criterion_articulation"
    },
    {
        "id": "P006",
        "content": "Protocol for preregistering research on methodological diversity continuum: articulate chosen position on quantitative-qualitative and idiographic-nomothetic axes, and specify inferential mode",
        "protocol_type": "methodological_procedure",
        "verbatim_quote": "Preregistration does not privilege any particular approach. Rather, it demands that researchers articulate the approach they have chosen... diversity of approaches makes it all the more important to articulate which approach is being taken",
        "page_number": 8,
        "context": "Applying preregistration across methodological diversity",
        "procedure_steps": [
            "Identify position on quantitative-qualitative continuum",
            "Identify position on idiographic-nomothetic continuum",
            "Identify primary inferential mode (deductive/inductive/abductive)",
            "Articulate chosen approach in registration",
            "Specify how approach affects research design"
        ],
        "inputs": "research_design_and_methodological_choices",
        "outputs": "explicit_methodological_positioning_statement",
        "quality_control": "completeness_of_methodological_articulation"
    }
]

# ============================================================================
# ADD TO EXTRACTION
# ============================================================================

data['research_designs'].extend(research_designs)
data['methods'].extend(methods)
data['protocols'].extend(protocols)

# Update metadata
data['extraction_notes']['pass3_rdmap_section3'] = {
    'section': 'Suitability for Archaeology (pages 7-8)',
    'research_designs': len(research_designs),
    'methods': len(methods),
    'protocols': len(protocols)
}

# Save
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✓ Section 3 RDMAP extraction complete")
print(f"  Research Designs: {len(research_designs)} items")
print(f"  Methods: {len(methods)} items")
print(f"  Protocols: {len(protocols)} items")
print(f"  Running totals: RD={len(data['research_designs'])}, M={len(data['methods'])}, P={len(data['protocols'])}")
