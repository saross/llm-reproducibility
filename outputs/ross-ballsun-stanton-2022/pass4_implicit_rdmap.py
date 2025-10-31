#!/usr/bin/env python3
"""
Pass 4: Implicit RDMAP Extraction
Extract research designs, methods, and protocols that are mentioned/apparent but not fully described

Target: 20-40% of total RDMAP should be implicit
Current explicit RDMAP: 4 RD, 15 M, 13 P = 32 items
Target implicit: ~8-13 items

Patterns to look for:
1. Mentioned procedures without description (how did they do X?)
2. Inferred from argumentation (operational details not documented)
3. Undocumented selection/classification decisions
4. Implied strategic framing choices
"""

import json

# Load existing extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'r') as f:
    data = json.load(f)

# ============================================================================
# IMPLICIT RESEARCH DESIGNS
# ============================================================================

implicit_research_designs = [
    {
        "id": "RD005_implicit",
        "content": "Case study selection design choosing specific disciplinary examples (Fraser et al. ecology HARKing survey, Ocean Health Index environmental science) to illustrate transferability of preregistration principles",
        "design_type": "illustrative_case_selection",
        "scope": "paper",
        "design_status": "implicit",
        "trigger_text": [
            "In a 2018 paper surveying over eight hundred ecologists and evolutionary biologists, Fraser et al. [24] found that 51% admitted to some form of HARKing",
            "In a review of the development of the Ocean Health Index, environmental scientists Lowndes et al. [90] describe research conditions that closely parallel the circumstances in which most archaeologists work"
        ],
        "trigger_locations": [
            {"section": "Section 1", "subsection": "Predictive and Postdictive Inquiry", "paragraph": None},
            {"section": "Section 5", "subsection": "Slow Archaeology", "paragraph": None}
        ],
        "inference_reasoning": "Paper uses specific case studies (Fraser et al., Ocean Health Index) to support arguments, implying selection criteria for choosing these examples over others. Selection logic not stated: why these specific studies? Fraser demonstrates HARKing prevalence, Ocean Health Index demonstrates parallel 'small data' problems. Selection pattern suggests criterion of 'problems parallel to archaeology' but design for choosing examples not documented.",
        "implicit_metadata": {
            "implicitness_basis": "selection_criteria_undocumented",
            "assessment_implication": "Affects argument strength—different examples might support or weaken claims differently. Selection bias possible if examples cherry-picked rather than systematically chosen."
        },
        "location": {"section": "Multiple", "subsection": None, "paragraph": None},
        "target_population": "interdisciplinary_case_studies",
        "sampling_strategy": "not_documented",
        "data_collection_approach": "purposive_example_selection"
    }
]

# ============================================================================
# IMPLICIT METHODS
# ============================================================================

implicit_methods = [
    {
        "id": "M016_implicit",
        "content": "Literature scoping method identifying relevant preregistration literature across multiple disciplines (biomedical research, psychology, ecology, archaeology) to establish knowledge base",
        "method_type": "scoping_review",
        "method_status": "implicit",
        "trigger_text": [
            "Preregistration arose as a means to improve the quality, replicability, and credibility of biomedical research... Its use has since been extended to psychology, ecology and evolutionary biology, and is gaining traction in other fields including political science and economics",
            "The so-called 'reproducibility crisis' – a variety of interrelated problems that undermine confidence in scientific findings – has now been documented in fields ranging from economics to medicine"
        ],
        "trigger_locations": [
            {"section": "Introduction", "subsection": None, "paragraph": 1},
            {"section": "Introduction", "subsection": None, "paragraph": 2}
        ],
        "inference_reasoning": "Paper synthesises preregistration literature across multiple disciplines, implying search and selection process, but search strategy not documented. No mention of: databases searched, search terms, inclusion/exclusion criteria, time period. Cross-disciplinary scope implies systematic scoping but method undocumented.",
        "implicit_metadata": {
            "implicitness_basis": "search_strategy_undocumented",
            "assessment_implication": "Affects comprehensiveness—systematic search would capture more/different literature than informal/selective approach. Replicability impossible without documented strategy."
        },
        "location": {"section": "Introduction", "subsection": None, "paragraph": None},
        "purpose": "Identify relevant preregistration literature for synthesis",
        "inputs": "multidisciplinary_academic_literature",
        "outputs": "curated_reference_set",
        "assumptions": "Literature identified is representative of preregistration discourse"
    },
    {
        "id": "M017_implicit",
        "content": "Argument construction method structuring methodological case by moving from problem diagnosis (just-in-time archaeology) through suitability demonstration to practical implementation",
        "method_type": "rhetorical_structure",
        "method_status": "implicit",
        "trigger_text": [
            "This paper introduces the concept and practice of preregistration to archaeology",
            "We begin by introducing the distinction between predictive and postdictive inquiry...",
            "We then explain the suitability of preregistration for archaeology...",
            "We then provide practical guidance for archaeologists..."
        ],
        "trigger_locations": [
            {"section": "Introduction", "subsection": None, "paragraph": 1},
            {"section": "Introduction", "subsection": None, "paragraph": 2}
        ],
        "inference_reasoning": "Paper follows structured argumentation pattern (problem→suitability→implementation) signposted in introduction, but rationale for this specific structure not explained. Why this sequence rather than implementation→problems→solutions? Structure implies pedagogical/persuasive method but design choice undocumented.",
        "implicit_metadata": {
            "implicitness_basis": "argumentative_strategy_undocumented",
            "assessment_implication": "Affects persuasiveness—different argument structures might be more/less effective for archaeological audience. Transparency about rhetorical choices would strengthen methodological contribution."
        },
        "location": {"section": "Introduction", "subsection": None, "paragraph": None},
        "purpose": "Construct persuasive methodological argument",
        "inputs": "evidence_and_conceptual_framework",
        "outputs": "structured_methodological_case",
        "assumptions": "Problem-first structure is effective for archaeological audience"
    },
    {
        "id": "M018_implicit",
        "content": "Typology construction method classifying archaeologists' under-investment into three types (imprecise documentation, implicit knowledge, late development) based on FAIMS project experience",
        "method_type": "classification_framework",
        "method_status": "implicit",
        "trigger_text": [
            "Our understanding of just-in-time archaeology is informed by a decade of experience implementing the Field Acquired Information Management Systems (FAIMS) project",
            "These circumstances lead archaeologists to under-invest in a public good in three ways. First, they under-invest in producing precise documentation... Second, they under-invest in making implicit knowledge explicit... Third, they under-invest in developing data structures"
        ],
        "trigger_locations": [
            {"section": "Section 2", "subsection": "Just-in-Time Archaeology", "paragraph": None}
        ],
        "inference_reasoning": "Paper presents three-way classification of under-investment types but doesn't explain how this typology was derived. FAIMS experience mentioned as basis but analytical process not documented: How did 60+ workflows yield exactly three categories? Inductive thematic analysis? Deductive framework application? Classification method implicit.",
        "implicit_metadata": {
            "implicitness_basis": "classification_derivation_undocumented",
            "assessment_implication": "Affects validity—different analytical approaches might yield different typologies. Completeness uncertain: are there other under-investment types not captured by three-way classification?"
        },
        "location": {"section": "Section 2", "subsection": "Just-in-Time Archaeology", "paragraph": None},
        "purpose": "Systematically classify patterns in archaeological practice",
        "inputs": "faims_project_observations",
        "outputs": "three_type_classification_framework",
        "assumptions": "Three types are exhaustive and mutually exclusive"
    },
    {
        "id": "M019_implicit",
        "content": "Historical synthesis method characterising evolution of archaeological planning from 1970s processual ideals to contemporary just-in-time approaches based on literature review",
        "method_type": "historical_synthesis",
        "method_status": "implicit",
        "trigger_text": [
            "In the 1970s, processual archaeologists like Hole and Heizer [58] and French [25] promoted 'research design' as an explicit plan formulated in advance of fieldwork",
            "By the mid-1980s this ideal had largely been abandoned in favour of ad hoc planning"
        ],
        "trigger_locations": [
            {"section": "Section 2", "subsection": "Just-in-Time Archaeology", "paragraph": None}
        ],
        "inference_reasoning": "Paper traces historical shift in archaeological practice (1970s processual→mid-1980s abandonment→contemporary just-in-time) but synthesis method not documented. How did authors determine 'mid-1980s' timing? What evidence for 'largely abandoned'? Literature analysis method implicit.",
        "implicit_metadata": {
            "implicitness_basis": "synthesis_method_undocumented",
            "assessment_implication": "Affects historical claim credibility—timing and characterisation depend on source selection and interpretation criteria. Different scholars might date transitions differently based on different evidence."
        },
        "location": {"section": "Section 2", "subsection": "Just-in-Time Archaeology", "paragraph": None},
        "purpose": "Document historical change in archaeological methodology",
        "inputs": "archaeological_methodology_literature",
        "outputs": "periodised_historical_narrative",
        "assumptions": "Selected literature represents broader disciplinary trends"
    },
    {
        "id": "M020_implicit",
        "content": "Template evaluation method assessing OSF preregistration templates for archaeological suitability by comparing template structures to archaeological research characteristics",
        "method_type": "template_assessment",
        "method_status": "implicit",
        "trigger_text": [
            "The OSF offers several templates, including ones designed for qualitative and quantitative studies, for clinical trials, and for secondary analysis",
            "The qualitative preregistration template is closer to the kinds of questions that most archaeologists would ask"
        ],
        "trigger_locations": [
            {"section": "Section 4", "subsection": "Introducing Preregistration to Archaeological Practice", "paragraph": None}
        ],
        "inference_reasoning": "Paper evaluates OSF templates and recommends qualitative template for archaeology, implying assessment criteria and comparison process. How was 'closer to' determined? What made qualitative better fit than quantitative or other templates? Evaluation method not documented.",
        "implicit_metadata": {
            "implicitness_basis": "evaluation_criteria_undocumented",
            "assessment_implication": "Affects recommendation validity—different evaluation criteria might yield different template recommendations. Readers cannot assess whether qualitative template is indeed best fit for their archaeological work."
        },
        "location": {"section": "Section 4", "subsection": "Introducing Preregistration to Archaeological Practice", "paragraph": None},
        "purpose": "Identify most suitable template for archaeological adaptation",
        "inputs": "osf_template_structures_and_archaeological_practice_knowledge",
        "outputs": "template_recommendation",
        "assumptions": "Qualitative archaeology characteristics align with qualitative template structure"
    }
]

# ============================================================================
# IMPLICIT PROTOCOLS
# ============================================================================

implicit_protocols = [
    {
        "id": "P014_implicit",
        "content": "Protocol for evaluating whether existing OSF archaeology registrations are prospective preregistrations or retrospective deposits: review registration content and timing to classify type",
        "protocol_type": "classification_procedure",
        "protocol_status": "implicit",
        "trigger_text": [
            "examination shows that none of them are preregistrations in the sense we have described. Rather, they are registrations of projects already underway, or in some cases already complete"
        ],
        "trigger_locations": [
            {"section": "Section 4", "subsection": "Introducing Preregistration to Archaeological Practice", "paragraph": None}
        ],
        "inference_reasoning": "Paper classifies four OSF registrations as non-preregistrations but classification procedure not documented. What criteria distinguished prospective from retrospective? How was project timing determined? Manual review implied but protocol not described.",
        "implicit_metadata": {
            "implicitness_basis": "classification_procedure_undocumented",
            "assessment_implication": "Affects classification reliability—different reviewers might classify same registrations differently without explicit criteria. Reproducibility limited."
        },
        "location": {"section": "Section 4", "subsection": "Introducing Preregistration to Archaeological Practice", "paragraph": None},
        "procedure_steps": ["Review registration content", "Determine project timing", "Classify as prospective or retrospective", "Document rationale"],
        "inputs": "osf_registration_metadata_and_content",
        "outputs": "prospective_vs_retrospective_classification",
        "quality_control": "undocumented"
    },
    {
        "id": "P015_implicit",
        "content": "Protocol for assessing metadata completeness in Selden's OSF registration: compare actual fields completed against template requirements to identify omissions",
        "protocol_type": "metadata_quality_assessment",
        "protocol_status": "implicit",
        "trigger_text": [
            "Only Selden fills out most of the suggested fields, but even this relatively complete registration leaves several of the template fields blank, and does not fill in key details"
        ],
        "trigger_locations": [
            {"section": "Section 4", "subsection": "Introducing Preregistration to Archaeological Practice", "paragraph": None}
        ],
        "inference_reasoning": "Paper evaluates Selden registration as incomplete but assessment protocol not documented. What constitutes 'most fields'? What are 'key details'? Which fields were blank? Completeness assessment implies comparison protocol but procedure undocumented.",
        "implicit_metadata": {
            "implicitness_basis": "assessment_criteria_undocumented",
            "assessment_implication": "Affects completeness evaluation credibility—what seems incomplete to authors might seem adequate to others. Explicit criteria would strengthen assessment."
        },
        "location": {"section": "Section 4", "subsection": "Introducing Preregistration to Archaeological Practice", "paragraph": None},
        "procedure_steps": ["Identify template required fields", "Review registration content", "Identify blank fields", "Assess detail adequacy", "Document completeness gaps"],
        "inputs": "registration_content_and_template_structure",
        "outputs": "completeness_assessment",
        "quality_control": "undocumented"
    },
    {
        "id": "P016_implicit",
        "content": "Protocol for identifying archaeological projects in OSF database: search for 'archaeology' classification, apply filters, review results to ensure relevance",
        "protocol_type": "database_search_procedure",
        "protocol_status": "implicit",
        "trigger_text": [
            "A search for projects classified as 'archaeology' on OSF yields 304,904 results. Filtering this list for registrations yields just four"
        ],
        "trigger_locations": [
            {"section": "Section 4", "subsection": "Introducing Preregistration to Archaeological Practice", "paragraph": None}
        ],
        "inference_reasoning": "Paper reports OSF search yielding 304,904 projects but search protocol not fully documented. Was search term exactly 'archaeology' or broader? Were results reviewed for false positives? Search date not stated. Basic search described but full protocol implicit.",
        "implicit_metadata": {
            "implicitness_basis": "search_procedure_partially_documented",
            "assessment_implication": "Affects search completeness—different search strategies might yield different result counts. Reproducibility limited without exact search protocol and date."
        },
        "location": {"section": "Section 4", "subsection": "Introducing Preregistration to Archaeological Practice", "paragraph": None},
        "procedure_steps": ["Access OSF search interface", "Enter 'archaeology' classification", "Apply registration filter", "Review and count results", "Document search date"],
        "inputs": "osf_database_search_interface",
        "outputs": "list_of_archaeological_registrations",
        "quality_control": "undocumented"
    },
    {
        "id": "P017_implicit",
        "content": "Protocol for adapting TOP Guidelines Level 2 badge criteria to archaeological preregistration: interpret general criteria in archaeological context to establish compliance pathway",
        "protocol_type": "standards_adaptation_procedure",
        "protocol_status": "implicit",
        "trigger_text": [
            "Level 2 of the Transparency and Openness Promotion (TOP) Guidelines encourages preregistration of studies... journals adhering to these guidelines would award a badge to papers that report the existence and location of a registration"
        ],
        "trigger_locations": [
            {"section": "Section 4", "subsection": "Introducing Preregistration to Archaeological Practice", "paragraph": None}
        ],
        "inference_reasoning": "Paper recommends TOP Level 2 compliance for archaeology but adaptation protocol not documented. TOP guidelines were developed for experimental sciences—how do criteria translate to archaeological contexts (observational, excavation, survey, mixed methods)? Interpretation protocol implicit.",
        "implicit_metadata": {
            "implicitness_basis": "adaptation_criteria_undocumented",
            "assessment_implication": "Affects applicability—archaeologists need guidance on how to interpret TOP criteria for their specific research types. Different interpretations might lead to different compliance approaches."
        },
        "location": {"section": "Section 4", "subsection": "Introducing Preregistration to Archaeological Practice", "paragraph": None},
        "procedure_steps": ["Review TOP Level 2 criteria", "Identify archaeological research types", "Interpret criteria for each type", "Document compliance pathway", "Identify adaptation challenges"],
        "inputs": "top_guidelines_and_archaeological_research_characteristics",
        "outputs": "archaeology_specific_compliance_guidance",
        "quality_control": "undocumented"
    },
    {
        "id": "P018_implicit",
        "content": "Protocol for determining registration content priorities for archaeology: identify which elements (theoretical tradition, approach, hypotheses, data collection plans, workflows, data models) are most important given archaeological challenges",
        "protocol_type": "prioritisation_procedure",
        "protocol_status": "implicit",
        "trigger_text": [
            "a registration might include theoretical tradition, approach (qualitative, quantitative, deductive, inductive, abductive, idiographic, nomothetic), stated hypotheses or expectations, data collection plans (including what will be recorded, and in what ways), workflows, and data models",
            "Priority areas should be theoretical approach and hypotheses (to combat biases like HARKing) and data models and workflows (to overcome just-in-time archaeology)"
        ],
        "trigger_locations": [
            {"section": "Section 4", "subsection": "Introducing Preregistration to Archaeological Practice", "paragraph": None}
        ],
        "inference_reasoning": "Paper identifies priorities (approach/hypotheses to combat bias, models/workflows to overcome just-in-time) but prioritisation method not documented. How were these selected as priorities over other elements? Cost-benefit analysis? Problem-solution mapping? Prioritisation logic implied but procedure undocumented.",
        "implicit_metadata": {
            "implicitness_basis": "prioritisation_rationale_partially_documented",
            "assessment_implication": "Affects recommendation uptake—different archaeological contexts might benefit from different priorities. Explicit prioritisation framework would help researchers adapt to their circumstances."
        },
        "location": {"section": "Section 4", "subsection": "Introducing Preregistration to Archaeological Practice", "paragraph": None},
        "procedure_steps": ["List possible registration elements", "Identify archaeological problems", "Map elements to problems", "Prioritise elements addressing most critical problems", "Document rationale"],
        "inputs": "registration_template_elements_and_archaeological_challenges",
        "outputs": "prioritised_registration_content_recommendations",
        "quality_control": "problem_solution_alignment"
    }
]

# ============================================================================
# ADD TO EXTRACTION
# ============================================================================

data['research_designs'].extend(implicit_research_designs)
data['methods'].extend(implicit_methods)
data['protocols'].extend(implicit_protocols)

# Update metadata
data['extraction_notes']['pass4_implicit_rdmap'] = {
    'implicit_research_designs': len(implicit_research_designs),
    'implicit_methods': len(implicit_methods),
    'implicit_protocols': len(implicit_protocols),
    'total_implicit_rdmap': len(implicit_research_designs) + len(implicit_methods) + len(implicit_protocols),
    'implicit_percentage': round((len(implicit_research_designs) + len(implicit_methods) + len(implicit_protocols)) / (len(data['research_designs']) + len(data['methods']) + len(data['protocols'])) * 100, 1)
}

# Save
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✓ Pass 4 implicit RDMAP extraction complete")
print(f"  Implicit Research Designs: {len(implicit_research_designs)} items")
print(f"  Implicit Methods: {len(implicit_methods)} items")
print(f"  Implicit Protocols: {len(implicit_protocols)} items")
print(f"  Total implicit RDMAP: {len(implicit_research_designs) + len(implicit_methods) + len(implicit_protocols)} items")
print()
print(f"Final RDMAP totals:")
print(f"  Research Designs: {len(data['research_designs'])} items ({len([rd for rd in data['research_designs'] if rd.get('design_status') == 'implicit'])} implicit)")
print(f"  Methods: {len(data['methods'])} items ({len([m for m in data['methods'] if m.get('method_status') == 'implicit'])} implicit)")
print(f"  Protocols: {len(data['protocols'])} items ({len([p for p in data['protocols'] if p.get('protocol_status') == 'implicit'])} implicit)")
print(f"  Total RDMAP: {len(data['research_designs']) + len(data['methods']) + len(data['protocols'])} items")
print(f"  Implicit percentage: {data['extraction_notes']['pass4_implicit_rdmap']['implicit_percentage']}%")
print()
print("=" * 80)
print("PASS 4 COMPLETE - Implicit RDMAP extraction")
print("=" * 80)
