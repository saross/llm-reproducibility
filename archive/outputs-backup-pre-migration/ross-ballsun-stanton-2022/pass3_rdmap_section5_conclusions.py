#!/usr/bin/env python3
"""
Pass 3: RDMAP Extraction - Section 5 (Slow Archaeology + Conclusions)
Pages 11-13 (~1400 words)

Liberal extraction: Over-extract by 40-50%, will rationalize in Pass 5
Focus: Methods and frameworks for slow archaeology approach
"""

import json

# Load existing extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'r') as f:
    data = json.load(f)

# ============================================================================
# RESEARCH DESIGNS
# ============================================================================

research_designs = [
    # No additional research designs in conclusions section
]

# ============================================================================
# METHODS
# ============================================================================

methods = [
    {
        "id": "M014",
        "content": "Analogical reasoning method drawing parallels between archaeological small data problems and Ocean Health Index environmental science challenges",
        "method_type": "analogical_analysis",
        "verbatim_quote": "In a review of the development of the Ocean Health Index, environmental scientists Lowndes et al. [90] describe research conditions that closely parallel the circumstances in which most archaeologists work",
        "page_number": 11,
        "context": "Using cross-disciplinary comparison to validate problem diagnosis",
        "purpose": "Demonstrate that archaeological challenges are not unique",
        "inputs": "ocean_health_index_case_study_and_archaeological_practice",
        "outputs": "parallel_problem_identification",
        "assumptions": "Environmental science and archaeology face comparable small data challenges"
    },
    {
        "id": "M015",
        "content": "Conceptual framework method defining 'slow archaeology' as deliberate, thoughtful research design planning in contrast to just-in-time approaches",
        "method_type": "conceptual_framework",
        "verbatim_quote": "We invoke the idea of 'slow archaeology'... The slow movement began with slow food... slow archaeology emphasises the benefits – social as well as scientific – of doing archaeology carefully and thoughtfully",
        "page_number": 12,
        "context": "Positioning preregistration within broader methodological movement",
        "purpose": "Connect preregistration to existing slow science/slow archaeology discourse",
        "inputs": "slow_movement_literature_and_archaeological_practice",
        "outputs": "slow_archaeology_conceptual_framework",
        "assumptions": "Slow movement principles are applicable to archaeological research design"
    }
]

# ============================================================================
# PROTOCOLS
# ============================================================================

protocols = [
    {
        "id": "P012",
        "content": "Protocol for implementing 'slow archaeology' approach: invest time in careful planning, develop comprehensive research design before fieldwork, prioritise thoughtfulness over speed",
        "protocol_type": "methodological_procedure",
        "verbatim_quote": "slow archaeology emphasises the benefits – social as well as scientific – of doing archaeology carefully and thoughtfully... Preregistration fosters a 'slow', rather than 'just-in-time', approach to research design",
        "page_number": 12,
        "context": "Operationalising slow archaeology principles",
        "procedure_steps": [
            "Allocate dedicated time for research design planning",
            "Develop comprehensive documentation before fieldwork",
            "Engage collaborators in design process",
            "Prioritise quality of planning over speed of execution",
            "Use preregistration to formalise slow approach"
        ],
        "inputs": "research_planning_timeline_and_team",
        "outputs": "slow_archaeology_research_design",
        "quality_control": "peer_review_of_design_before_fieldwork"
    },
    {
        "id": "P013",
        "content": "Protocol for implementing 'built-in' rather than 'bolt-on' research practices: integrate best practices into initial research design rather than retrofitting after data collection",
        "protocol_type": "methodological_procedure",
        "verbatim_quote": "Preregistration promotes 'built-in' rather than 'bolt-on' best practice",
        "page_number": 12,
        "context": "Principles for research design integration",
        "procedure_steps": [
            "Identify best practices relevant to research domain",
            "Incorporate best practices into initial research design",
            "Document integration in preregistration",
            "Avoid retrofitting practices after data collection",
            "Design infrastructure to support integrated practices"
        ],
        "inputs": "domain_best_practices_and_research_design",
        "outputs": "integrated_best_practice_design",
        "quality_control": "design_review_for_practice_integration"
    }
]

# ============================================================================
# ADD TO EXTRACTION
# ============================================================================

data['research_designs'].extend(research_designs)
data['methods'].extend(methods)
data['protocols'].extend(protocols)

# Update metadata
data['extraction_notes']['pass3_rdmap_section5'] = {
    'section': 'Slow Archaeology + Conclusions (pages 11-13)',
    'research_designs': len(research_designs),
    'methods': len(methods),
    'protocols': len(protocols)
}

data['extraction_notes']['pass3_complete'] = True

# Save
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✓ Section 5 RDMAP extraction complete")
print(f"  Research Designs: {len(research_designs)} items")
print(f"  Methods: {len(methods)} items")
print(f"  Protocols: {len(protocols)} items")
print(f"  Final Pass 3 totals: RD={len(data['research_designs'])}, M={len(data['methods'])}, P={len(data['protocols'])}")
print()
print("=" * 80)
print("PASS 3 COMPLETE - Liberal RDMAP extraction from all 5 sections")
print("=" * 80)
