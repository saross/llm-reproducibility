#!/usr/bin/env python3
"""
Pass 3: RDMAP Extraction - Section 2 (Just-in-Time Archaeology)
Pages 5-6 (~1000 words)

Liberal extraction: Over-extract by 40-50%, will rationalize in Pass 5
Focus: Research designs, methods, and protocols related to archaeological planning
"""

import json

# Load existing extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'r') as f:
    data = json.load(f)

# ============================================================================
# RESEARCH DESIGNS
# ============================================================================

research_designs = [
    {
        "id": "RD003",
        "content": "Historical analysis design examining archaeological practice evolution from 1970s processual archaeology planning ideals to contemporary just-in-time approaches",
        "design_type": "historical_analysis",
        "scope": "section",
        "verbatim_quote": "Hole and Heizer promoted 'research design' as an explicit plan formulated in advance of fieldwork... By the mid-1980s this ideal had largely been abandoned in favour of ad hoc planning... we call this widespread approach 'just-in-time' archaeology",
        "page_number": 5,
        "context": "Section 2 tracing evolution of archaeological planning practices",
        "justification": "Examines change in archaeological methodology over time",
        "target_population": "archaeological_planning_practices_1970s_to_present",
        "sampling_strategy": "historical_literature_review",
        "data_collection_approach": "document_analysis"
    }
]

# ============================================================================
# METHODS
# ============================================================================

methods = [
    {
        "id": "M004",
        "content": "Characterisation method defining 'just-in-time archaeology' as an approach where critical research decisions are deferred until field operations are underway",
        "method_type": "conceptual_framework",
        "verbatim_quote": "we call this widespread approach 'just-in-time' archaeology, to evoke the practice of deferring important decisions – including what to record and how to record it – until data collection is underway",
        "page_number": 5,
        "context": "Defining key concept for critique",
        "purpose": "Name and characterise contemporary archaeological practice pattern",
        "inputs": "observations_of_archaeological_practice",
        "outputs": "conceptual_label_and_definition",
        "assumptions": "Deferral of decisions is widespread and identifiable pattern"
    },
    {
        "id": "M005",
        "content": "Evidence synthesis method drawing on FAIMS project experience (60+ workflows at 40+ projects) to document just-in-time archaeology consequences",
        "method_type": "case_study_synthesis",
        "verbatim_quote": "Our understanding of just-in-time archaeology is informed by a decade of experience implementing the Field Acquired Information Management Systems (FAIMS) project, which has now deployed over sixty separate data-collection workflows at more than forty archaeological projects",
        "page_number": 5,
        "context": "Grounding analysis in empirical experience",
        "purpose": "Use accumulated project experience as evidence base",
        "inputs": "faims_project_implementation_records",
        "outputs": "patterns_and_problems_in_archaeological_practice",
        "assumptions": "FAIMS experience is representative of broader archaeological practice"
    },
    {
        "id": "M006",
        "content": "Theoretical framework method adapting economic concept of 'under-investment in a public good' to analyse archaeological research design decisions",
        "method_type": "theoretical_framework",
        "verbatim_quote": "These circumstances lead archaeologists to under-invest in a public good in three ways",
        "page_number": 6,
        "context": "Applying economic framework to archaeological practice",
        "purpose": "Explain systematic patterns in archaeologists' planning behaviour",
        "inputs": "public_goods_theory",
        "outputs": "three_types_of_underinvestment_classification",
        "assumptions": "Archaeological research design functions as a public good"
    }
]

# ============================================================================
# PROTOCOLS
# ============================================================================

protocols = [
    {
        "id": "P003",
        "content": "Protocol for identifying just-in-time archaeology: check whether critical research design decisions (what to record, how to record) are made during field operations rather than in advance",
        "protocol_type": "classification_procedure",
        "verbatim_quote": "we call this widespread approach 'just-in-time' archaeology, to evoke the practice of deferring important decisions – including what to record and how to record it – until data collection is underway",
        "page_number": 5,
        "context": "Operationalising just-in-time concept",
        "procedure_steps": [
            "Identify timing of critical research design decisions",
            "Determine whether decisions made before or during data collection",
            "Classify as just-in-time if decisions deferred to field operations"
        ],
        "inputs": "project_planning_documentation_and_fieldwork_records",
        "outputs": "classification_as_just_in_time_or_planned_in_advance",
        "quality_control": "temporal_documentation_of_decision_points"
    },
    {
        "id": "P004",
        "content": "Protocol for classifying types of archaeologist under-investment: categorise whether under-investment involves imprecise documentation, implicit knowledge, or late development of data structures",
        "protocol_type": "classification_procedure",
        "verbatim_quote": "These circumstances lead archaeologists to under-invest in a public good in three ways. First, they under-invest in producing precise documentation... Second, they under-invest in making implicit knowledge explicit... Third, they under-invest in developing data structures",
        "page_number": 6,
        "context": "Three-way classification of under-investment types",
        "procedure_steps": [
            "Examine archaeological project planning and documentation",
            "Identify instances of under-investment in research design",
            "Classify as Type 1 (imprecise documentation), Type 2 (implicit knowledge), or Type 3 (late development)"
        ],
        "inputs": "project_documentation_and_data_structures",
        "outputs": "classified_under_investment_types",
        "quality_control": "comparison_to_ideal_processual_standards"
    }
]

# ============================================================================
# ADD TO EXTRACTION
# ============================================================================

data['research_designs'].extend(research_designs)
data['methods'].extend(methods)
data['protocols'].extend(protocols)

# Update metadata
data['extraction_notes']['pass3_rdmap_section2'] = {
    'section': 'Just-in-Time Archaeology (pages 5-6)',
    'research_designs': len(research_designs),
    'methods': len(methods),
    'protocols': len(protocols)
}

# Save
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✓ Section 2 RDMAP extraction complete")
print(f"  Research Designs: {len(research_designs)} items")
print(f"  Methods: {len(methods)} items")
print(f"  Protocols: {len(protocols)} items")
print(f"  Running totals: RD={len(data['research_designs'])}, M={len(data['methods'])}, P={len(data['protocols'])}")
