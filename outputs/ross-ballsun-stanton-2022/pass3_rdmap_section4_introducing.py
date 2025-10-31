#!/usr/bin/env python3
"""
Pass 3: RDMAP Extraction - Section 4 (Introducing Preregistration to Archaeological Practice)
Pages 8-11 (~1800 words)

Liberal extraction: Over-extract by 40-50%, will rationalize in Pass 5
Focus: Protocols for implementing preregistration in archaeology, OSF templates
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
        "id": "RD004",
        "content": "Empirical survey design examining existing archaeological preregistrations in Open Science Framework (OSF) to assess current adoption and quality",
        "design_type": "descriptive_survey",
        "scope": "section",
        "verbatim_quote": "A search for projects classified as 'archaeology' on OSF yields 304,904 results. Filtering this list for registrations yields just four... examination shows that none of them are preregistrations in the sense we have described",
        "page_number": 9,
        "context": "Assessing current state of archaeological preregistration",
        "justification": "Provides empirical baseline for preregistration adoption",
        "target_population": "archaeological_projects_on_osf",
        "sampling_strategy": "complete_enumeration_of_osf_archaeology_category",
        "data_collection_approach": "database_search_and_manual_review"
    }
]

# ============================================================================
# METHODS
# ============================================================================

methods = [
    {
        "id": "M010",
        "content": "Database search method querying Open Science Framework (OSF) for archaeology projects and filtering for registrations to identify preregistration adoption",
        "method_type": "database_search",
        "verbatim_quote": "A search for projects classified as 'archaeology' on OSF yields 304,904 results. Filtering this list for registrations yields just four",
        "page_number": 9,
        "context": "Quantifying preregistration adoption in archaeology",
        "purpose": "Establish baseline for archaeological preregistration practice",
        "inputs": "osf_database_archaeology_category",
        "outputs": "count_of_archaeological_registrations",
        "assumptions": "OSF captures representative sample of open science archaeology"
    },
    {
        "id": "M011",
        "content": "Content analysis method examining existing OSF registrations to classify whether they are prospective preregistrations or retrospective data deposits",
        "method_type": "qualitative_content_analysis",
        "verbatim_quote": "examination shows that none of them are preregistrations in the sense we have described. Rather, they are registrations of projects already underway, or in some cases already complete",
        "page_number": 9,
        "context": "Assessing quality and type of existing registrations",
        "purpose": "Distinguish preregistration from other registration types",
        "inputs": "osf_registration_content",
        "outputs": "classification_as_preregistration_or_data_deposit",
        "assumptions": "Timing and content reveal whether registration is prospective"
    },
    {
        "id": "M012",
        "content": "Metadata completeness assessment method evaluating whether registrations include all recommended fields (title, authors, keywords, abstract, research questions, data collection plan, analysis plan, other)",
        "method_type": "metadata_quality_assessment",
        "verbatim_quote": "The 'prereg challenge' template used by Selden asks for a title, list of authors and their affiliations, a list of keywords, an abstract, and then asks users to describe the research questions, data collection plan, analysis plan, and 'other'",
        "page_number": 9,
        "context": "Evaluating registration metadata quality",
        "purpose": "Assess completeness of archaeological registration metadata",
        "inputs": "registration_template_fields_and_actual_content",
        "outputs": "metadata_completeness_score",
        "assumptions": "Template fields represent minimum metadata requirements"
    },
    {
        "id": "M013",
        "content": "Template evaluation method comparing OSF's qualitative preregistration template structure and fields to assess suitability for archaeological adaptation",
        "method_type": "template_assessment",
        "verbatim_quote": "The OSF offers several templates... The qualitative preregistration template is closer to the kinds of questions that most archaeologists would ask",
        "page_number": 10,
        "context": "Identifying appropriate preregistration template for archaeology",
        "purpose": "Match template structure to archaeological research characteristics",
        "inputs": "osf_template_structures_and_archaeological_practice",
        "outputs": "template_suitability_assessment",
        "assumptions": "Existing templates can be adapted for archaeology"
    }
]

# ============================================================================
# PROTOCOLS
# ============================================================================

protocols = [
    {
        "id": "P007",
        "content": "Protocol for searching OSF for archaeological preregistrations: search for projects classified as 'archaeology', filter for registrations, manually review to classify type",
        "protocol_type": "search_procedure",
        "verbatim_quote": "A search for projects classified as 'archaeology' on OSF yields 304,904 results. Filtering this list for registrations yields just four",
        "page_number": 9,
        "context": "Systematic search for existing practice",
        "procedure_steps": [
            "Search OSF for projects with 'archaeology' classification",
            "Filter search results to show only registrations",
            "Review each registration to determine type (prospective vs retrospective)",
            "Count and classify results"
        ],
        "inputs": "osf_search_interface",
        "outputs": "list_of_archaeological_registrations",
        "quality_control": "manual_review_of_all_results"
    },
    {
        "id": "P008",
        "content": "Protocol for creating archaeological preregistration on OSF: create project, select appropriate template (recommend qualitative template), complete all required fields",
        "protocol_type": "registration_procedure",
        "verbatim_quote": "Archaeologists could, right now, use OSF to create preregistrations. The OSF offers several templates... we recommend the qualitative preregistration template as an interim measure",
        "page_number": 10,
        "context": "Practical implementation guidance",
        "procedure_steps": [
            "Create new project on Open Science Framework",
            "Select preregistration template (recommend qualitative template)",
            "Complete required template fields",
            "Submit registration before data collection",
            "Link to eventual data deposit"
        ],
        "inputs": "research_design_and_osf_account",
        "outputs": "timestamped_preregistration",
        "quality_control": "osf_timestamp_verification"
    },
    {
        "id": "P009",
        "content": "Protocol for completing OSF qualitative preregistration template: provide study information, research questions, hypotheses, data collection methods, analysis plan, and other relevant details",
        "protocol_type": "documentation_procedure",
        "verbatim_quote": "The qualitative preregistration template asks for study information (title, authors, description, hypotheses), research questions, whether hypothesis testing is involved, dependent and independent variables, whether this is a replication study, procedure, analysis plan, and 'other'",
        "page_number": 10,
        "context": "Template completion guidance",
        "procedure_steps": [
            "Provide study information (title, authors, description, hypotheses)",
            "Articulate research questions",
            "Indicate whether hypothesis testing involved",
            "Specify dependent and independent variables if applicable",
            "Indicate whether replication study",
            "Describe data collection procedure",
            "Describe analysis plan",
            "Add other relevant information"
        ],
        "inputs": "research_design_documentation",
        "outputs": "completed_qualitative_preregistration_form",
        "quality_control": "template_field_completeness_check"
    },
    {
        "id": "P010",
        "content": "Protocol for adapting OSF qualitative template to archaeological contexts: provide study information, theoretical tradition, research approach, hypotheses/expectations, data collection plans, analysis workflows, data models",
        "protocol_type": "documentation_procedure",
        "verbatim_quote": "a registration might include theoretical tradition, approach (qualitative, quantitative, deductive, inductive, abductive, idiographic, nomothetic), stated hypotheses or expectations, data collection plans (including what will be recorded, and in what ways), workflows, and data models",
        "page_number": 11,
        "context": "Archaeological-specific template adaptation",
        "procedure_steps": [
            "Specify theoretical tradition and approach",
            "Indicate methodology position (qualitative/quantitative, deductive/inductive/abductive, idiographic/nomothetic)",
            "State hypotheses or expectations",
            "Describe data collection plans (what to record, how to record)",
            "Document workflows",
            "Describe data models",
            "Register before fieldwork begins"
        ],
        "inputs": "archaeological_research_design",
        "outputs": "archaeology_adapted_preregistration",
        "quality_control": "archaeological_best_practice_alignment"
    },
    {
        "id": "P011",
        "content": "Protocol for meeting Transparency and Openness Promotion (TOP) Guidelines Level 2 via preregistration: register research plan before data collection begins and report all deviations",
        "protocol_type": "compliance_procedure",
        "verbatim_quote": "journals adhering to these [TOP] guidelines would award a badge to papers that report the existence and location of a registration, helping archaeologists to meet Level 2",
        "page_number": 11,
        "context": "Linking preregistration to publication standards",
        "procedure_steps": [
            "Create and complete preregistration before data collection",
            "Obtain timestamped registration from repository (e.g., OSF)",
            "Report registration existence and location in manuscript",
            "Report all deviations from registered plan",
            "Request TOP Level 2 badge during submission"
        ],
        "inputs": "preregistration_and_manuscript",
        "outputs": "top_level_2_compliant_publication",
        "quality_control": "journal_badge_verification"
    }
]

# ============================================================================
# ADD TO EXTRACTION
# ============================================================================

data['research_designs'].extend(research_designs)
data['methods'].extend(methods)
data['protocols'].extend(protocols)

# Update metadata
data['extraction_notes']['pass3_rdmap_section4'] = {
    'section': 'Introducing to Practice (pages 8-11)',
    'research_designs': len(research_designs),
    'methods': len(methods),
    'protocols': len(protocols)
}

# Save
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✓ Section 4 RDMAP extraction complete")
print(f"  Research Designs: {len(research_designs)} items")
print(f"  Methods: {len(methods)} items")
print(f"  Protocols: {len(protocols)} items")
print(f"  Running totals: RD={len(data['research_designs'])}, M={len(data['methods'])}, P={len(data['protocols'])}")
