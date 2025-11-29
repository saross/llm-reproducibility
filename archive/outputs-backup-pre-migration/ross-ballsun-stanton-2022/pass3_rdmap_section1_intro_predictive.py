#!/usr/bin/env python3
"""
Pass 3: RDMAP Extraction - Section 1 (Introduction + Predictive/Postdictive Inquiry)
Pages 2-4 (~1600 words)

Liberal extraction: Over-extract by 40-50%, will rationalize in Pass 5
Focus: Research designs, methods, and protocols for the preregistration framework
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
        "id": "RD001",
        "content": "Methodological argument design combining theoretical analysis, literature review, and practical recommendations to introduce preregistration to archaeology",
        "design_type": "argumentative_synthesis",
        "scope": "paper",
        "verbatim_quote": "This paper introduces the concept and practice of preregistration to archaeology... We argue that many, but by no means all, archaeological projects could benefit from preregistration.",
        "page_number": 2,
        "context": "Overall paper structure outlined in introduction",
        "justification": "States that paper will make an argument and provide practical guidance",
        "target_population": "archaeological researchers and projects",
        "sampling_strategy": "not_applicable",
        "data_collection_approach": "literature_review_and_conceptual_analysis"
    },
    {
        "id": "RD002",
        "content": "Comparative analysis design examining preregistration practices across disciplines (biomedical research, psychology, ecology) to identify transferable principles for archaeology",
        "design_type": "comparative_analysis",
        "scope": "section",
        "verbatim_quote": "Preregistration arose as a means to improve the quality, replicability, and credibility of biomedical research... Its use has since been extended to psychology, ecology and evolutionary biology...",
        "page_number": 2,
        "context": "Introduction reviewing preregistration across disciplines",
        "justification": "Analyses practices in other fields to extract lessons for archaeology",
        "target_population": "preregistration_practices_across_disciplines",
        "sampling_strategy": "purposive_selection_of_disciplines",
        "data_collection_approach": "literature_review"
    }
]

# ============================================================================
# METHODS
# ============================================================================

methods = [
    {
        "id": "M001",
        "content": "Conceptual analysis method distinguishing predictive (a priori hypothesis generation) from postdictive (post hoc interpretation) inquiry",
        "method_type": "conceptual_framework",
        "verbatim_quote": "'Predictive' inquiry (from prediction, a priori hypothesis generation) allows a researcher to announce the exact questions they plan to ask prior to asking them. 'Postdictive' inquiry (from postdiction, post hoc interpretation) is characterised by asking questions in response to seeing the evidence.",
        "page_number": 3,
        "context": "Defining core conceptual distinction for understanding preregistration",
        "purpose": "Establish analytical framework for distinguishing types of inquiry",
        "inputs": "definitions_and_conceptual_distinctions",
        "outputs": "binary_classification_of_inquiry_types",
        "assumptions": "Prediction and postdiction are meaningful and separable categories"
    },
    {
        "id": "M002",
        "content": "Literature review method examining reproducibility crisis evidence across multiple disciplines to establish problem context",
        "method_type": "systematic_literature_review",
        "verbatim_quote": "The so-called 'reproducibility crisis' – a variety of interrelated problems that undermine confidence in scientific findings – has now been documented in fields ranging from economics to medicine...",
        "page_number": 2,
        "context": "Establishing evidence base for reproducibility problems",
        "purpose": "Document breadth of reproducibility problems across disciplines",
        "inputs": "published_literature_on_reproducibility",
        "outputs": "synthesis_of_crisis_evidence",
        "assumptions": "Reproducibility crisis is real and documented across disciplines"
    },
    {
        "id": "M003",
        "content": "Survey data analysis method examining rates of questionable research practices (HARKing) in ecology and evolutionary biology",
        "method_type": "quantitative_synthesis",
        "verbatim_quote": "In a 2018 paper surveying over eight hundred ecologists and evolutionary biologists, Fraser et al. [24] found that 51% admitted to some form of HARKing",
        "page_number": 4,
        "context": "Using empirical evidence to demonstrate prevalence of HARKing",
        "purpose": "Quantify extent of questionable research practices",
        "inputs": "fraser_et_al_2018_survey_data",
        "outputs": "prevalence_estimates_for_harking",
        "assumptions": "Self-reported survey data accurately reflects actual practices"
    }
]

# ============================================================================
# PROTOCOLS
# ============================================================================

protocols = [
    {
        "id": "P001",
        "content": "Protocol for distinguishing prediction from postdiction: assess whether hypotheses/questions were formulated before or after seeing the evidence",
        "protocol_type": "classification_procedure",
        "verbatim_quote": "'Predictive' inquiry (from prediction, a priori hypothesis generation) allows a researcher to announce the exact questions they plan to ask prior to asking them. 'Postdictive' inquiry (from postdiction, post hoc interpretation) is characterised by asking questions in response to seeing the evidence.",
        "page_number": 3,
        "context": "Defining how to classify types of inquiry",
        "procedure_steps": [
            "Determine timing of hypothesis formulation relative to data observation",
            "Classify as predictive if formulated before seeing evidence",
            "Classify as postdictive if formulated after seeing evidence"
        ],
        "inputs": "research_hypothesis_and_timeline",
        "outputs": "classification_as_predictive_or_postdictive",
        "quality_control": "temporal_priority_verification"
    },
    {
        "id": "P002",
        "content": "Protocol for identifying HARKing (Hypothesizing After Results are Known): check whether researchers present post hoc hypotheses as if they were a priori predictions",
        "protocol_type": "detection_procedure",
        "verbatim_quote": "In HARKing (Hypothesising After the Results are Known), a researcher generates a hypothesis or research question after seeing the data, but reports it as if it had been predicted in advance.",
        "page_number": 4,
        "context": "Defining questionable research practice",
        "procedure_steps": [
            "Identify hypotheses presented in research report",
            "Determine actual timing of hypothesis formulation",
            "Compare presented timing to actual timing",
            "Flag discrepancies as potential HARKing"
        ],
        "inputs": "research_reports_and_methodology_descriptions",
        "outputs": "harking_detection_classification",
        "quality_control": "temporal_documentation_review"
    }
]

# ============================================================================
# ADD TO EXTRACTION
# ============================================================================

data['research_designs'].extend(research_designs)
data['methods'].extend(methods)
data['protocols'].extend(protocols)

# Update metadata
data['extraction_notes']['pass3_rdmap_section1'] = {
    'section': 'Introduction + Predictive/Postdictive Inquiry (pages 2-4)',
    'research_designs': len(research_designs),
    'methods': len(methods),
    'protocols': len(protocols)
}

# Save
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✓ Section 1 RDMAP extraction complete")
print(f"  Research Designs: {len(research_designs)} items")
print(f"  Methods: {len(methods)} items")
print(f"  Protocols: {len(protocols)} items")
print(f"  Running totals: RD={len(data['research_designs'])}, M={len(data['methods'])}, P={len(data['protocols'])}")
