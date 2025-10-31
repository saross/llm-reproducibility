#!/usr/bin/env python3
"""
Pass 1: Liberal Claims & Evidence Extraction
Section Group 4: Introducing Preregistration to Archaeological Practice
Pages: 8-11 (PDF pages, section 4)

Extraction Strategy:
- Evidence from OSF registry search
- Claims about existing archaeological preregistration (or lack thereof)
- Evidence from Marwick and Selden examples
- Detailed claims about OSF template recommendations
- Implicit assumptions about what archaeologists should register

Word count estimate: ~1800 words (longest section)
"""

import json
from datetime import datetime

# Load existing extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'r') as f:
    data = json.load(f)

# Section Group 4: Introducing Preregistration to Practice
# Pages 8-11 of PDF

# ============================================================================
# EVIDENCE ITEMS
# ============================================================================

evidence_items = [
    {
        "id": "E011",
        "content": "A search of OSF's 304,904 registrations (as of March 19, 2020) produced only four non-teaching-related hits for 'archaeology'.",
        "evidence_type": "quantitative_data",
        "source_type": "database_search",
        "verbatim_quote": "A search of OSF's 304,904 registrations (as of March 19, 2020) produced only four non-teaching-related hits for 'archaeology'",
        "page_number": 8,
        "context": "Demonstrating lack of archaeological preregistration",
        "interpretation_notes": "Systematic search of largest preregistration registry shows minimal archaeology adoption"
    },
    {
        "id": "E012",
        "content": "The four archaeological OSF registrations were by Marwick (2017a, 2017c), Selden (2016), and Schmid (2019), all using Open-Ended Registration to submit data and code supporting papers.",
        "evidence_type": "empirical_observation",
        "source_type": "database_search",
        "verbatim_quote": "The authors of the four preregistrations, Marwick (2017a, 2017c), Selden (2016), and Schmid (2019) used the 'Open-Ended Registration' method to submit data and code in support of papers they had written.",
        "page_number": 8,
        "context": "Characterising existing archaeological registrations",
        "interpretation_notes": "Existing registrations are data deposits, not prospective preregistrations"
    },
    {
        "id": "E013",
        "content": "Selden's pottery laser-scanning metadata is incomplete - spot checks indicate metadata like intra-site find location and artifact type do not accompany some scans.",
        "evidence_type": "empirical_observation",
        "source_type": "data_inspection",
        "verbatim_quote": "Spot checks indicate that data documentation is incomplete; metadata like intra-site find location and artifact type do not accompany some scans (e. g. https://zenodo.org/search?q=41NA49).",
        "page_number": 9,
        "context": "Evaluating existing archaeological registration",
        "interpretation_notes": "Even exemplary data sharing has documentation gaps"
    }
]

# ============================================================================
# CLAIMS ITEMS
# ============================================================================

claims_items = [
    {
        "id": "C066",
        "content": "Despite its potential utility, no examples of rigorous preregistration in archaeology could be found.",
        "claim_type": "empirical",
        "reasoning_type": "observational",
        "evidence_links": ["E011", "E012"],
        "verbatim_quote": "Despite its potential utility, we could find no examples of rigorous preregistration in archaeology.",
        "page_number": 8,
        "context": "Opening of Section 4",
        "certainty_qualifier": "based on systematic search"
    },
    {
        "id": "C067",
        "content": "While FAIR data registrations supporting replication of computational results are laudable, they do not represent preregistration of approaches and methods as suggested in this chapter.",
        "claim_type": "evaluative",
        "reasoning_type": "definitional",
        "evidence_links": ["E012"],
        "verbatim_quote": "While the submission of code in support of scientific papers is laudable, these FAIR data 'registrations', which support replication of computational results, do not represent the preregistration of approaches and methods we suggest.",
        "page_number": 9,
        "context": "Clarifying what counts as preregistration",
        "certainty_qualifier": "definitional distinction"
    },
    {
        "id": "C068",
        "content": "Selden's laser-scanning project (2017) would be a good candidate for preregistration of an inductive, postdictive project.",
        "claim_type": "evaluative",
        "reasoning_type": "pragmatic",
        "evidence_links": ["E012"],
        "verbatim_quote": "Selden's pottery laser-scanning project (2017), for example, would be a good candidate for the preregistration of an inductive, postdictive project.",
        "page_number": 9,
        "context": "Suggesting how existing work could be improved",
        "certainty_qualifier": "would be (counterfactual)"
    },
    {
        "id": "C069",
        "content": "A more complete preregistration for Selden's project could include protocols for laser-scanning methodology and creation and publication of metadata.",
        "claim_type": "methodological",
        "reasoning_type": "prescriptive",
        "evidence_links": ["E013"],
        "verbatim_quote": "A more complete preregistration effort, in this case, could include a protocol for the laser-scanning methodology and, crucially, a protocol for the creation and publication of metadata.",
        "page_number": 9,
        "context": "Specific recommendation for improvement",
        "certainty_qualifier": "could (modal)"
    },
    {
        "id": "C070",
        "content": "Marwick et al.'s lithic trampling experiment (2017a) represents an opportunity for preregistration of more deductive, predictive research.",
        "claim_type": "evaluative",
        "reasoning_type": "pragmatic",
        "evidence_links": ["E012"],
        "verbatim_quote": "Likewise, Marwick et al.'s lithic trampling experiment (2017a) represents an opportunity for the preregistration of more deductive, predictive research.",
        "page_number": 9,
        "context": "Example of deductive archaeology",
        "certainty_qualifier": "represents opportunity (counterfactual)"
    },
    {
        "id": "C071",
        "content": "Preregistration for Marwick's trampling study could articulate hypotheses, methodology, analytical approach, and even early versions of code.",
        "claim_type": "methodological",
        "reasoning_type": "prescriptive",
        "evidence_links": [],
        "verbatim_quote": "Preregistration could articulate hypotheses, methodology, and an analytical approach. Perhaps, this preregistration could even include early versions of code.",
        "page_number": 9,
        "context": "What preregistration could include",
        "certainty_qualifier": "could (modal)"
    },
    {
        "id": "C072",
        "content": "With moderate effort, especially if a grant application exists, research could be elaborated to a full preregistration plan or even a registered report.",
        "claim_type": "methodological",
        "reasoning_type": "pragmatic",
        "evidence_links": [],
        "verbatim_quote": "With moderate effort, especially if a grant application exists for this research, it could be elaborated to a full preregistration plan, or even a 'registered report', in which a journal accepts or rejects the paper on the strength of its hypothesis, methodology, and proposed analysis before results are known",
        "page_number": 9,
        "context": "Suggesting registered reports",
        "certainty_qualifier": "could (modal)"
    },
    {
        "id": "C073",
        "content": "Selden's laser scan data presentation exceeds standard archaeological practice and should be commended.",
        "claim_type": "evaluative",
        "reasoning_type": "normative",
        "evidence_links": [],
        "verbatim_quote": "We note that Selden's presentation of the laser scan data with licensing information exceeds standard practice in archaeology, complements the associated paper (2017), and should be commended.",
        "page_number": 9,
        "context": "Positive evaluation despite critique",
        "certainty_qualifier": "evaluative judgement"
    },
    {
        "id": "C074",
        "content": "Marwick's publication of containerised code is exceptional, confirming his status as a leader in computational reproducibility.",
        "claim_type": "evaluative",
        "reasoning_type": "normative",
        "evidence_links": [],
        "verbatim_quote": "Likewise, Marwick's publication of containerized code is exceptional, confirming his status as a leader in computational reproducibility.",
        "page_number": 9,
        "context": "Positive evaluation",
        "certainty_qualifier": "evaluative judgement"
    },
    {
        "id": "C075",
        "content": "These examples highlight that even archaeologists committed to transparency and reproducibility have not adopted comprehensive preregistration of approach, method, and data management.",
        "claim_type": "empirical",
        "reasoning_type": "observational",
        "evidence_links": ["E012", "E013"],
        "verbatim_quote": "Rather, these examples highlight that (1) even archaeologists committed to transparency and reproducibility have not adopted comprehensive preregistration of approach, method, and data management",
        "page_number": 9,
        "context": "Interpreting significance of examples",
        "certainty_qualifier": "observational claim"
    },
    {
        "id": "C076",
        "content": "Undertaking preregistration would reinforce other efforts to improve transparency and reproducibility, like FAIR datasets and publication of analytical code.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "undertaking preregistration would reinforce other efforts to improve transparency and reproducibility, like FAIR datasets and publication of analytical code.",
        "page_number": 9,
        "context": "Synergy with existing transparency efforts",
        "certainty_qualifier": "would (modal)"
    },
    {
        "id": "C077",
        "content": "Templates, examples, and models could facilitate the introduction of preregistration into archaeology.",
        "claim_type": "methodological",
        "reasoning_type": "pragmatic",
        "evidence_links": [],
        "verbatim_quote": "Templates, examples, and models could facilitate the introduction of preregistration into archaeology.",
        "page_number": 9,
        "context": "Practical implementation needs",
        "certainty_qualifier": "could (modal)"
    },
    {
        "id": "C078",
        "content": "Good practice around execution of preregistration is still evolving.",
        "claim_type": "empirical",
        "reasoning_type": "observational",
        "evidence_links": [],
        "verbatim_quote": "good practice around the execution of preregistration is still evolving (c.f. Nosek et al. 2018a; Ledgerwood 2018; Nosek et al. 2018b)",
        "page_number": 9,
        "context": "Acknowledging uncertain state of field",
        "certainty_qualifier": "documented in literature"
    },
    {
        "id": "C079",
        "content": "A distinction is sometimes made between preregistration of research questions/hypotheses and plans for analysis.",
        "claim_type": "empirical",
        "reasoning_type": "observational",
        "evidence_links": [],
        "verbatim_quote": "A distinction is sometimes made between preregistration of research questions or hypotheses on the one hand, and plans for analysis on the other",
        "page_number": 9-10,
        "context": "Different types of preregistration",
        "certainty_qualifier": "documented practice"
    },
    {
        "id": "C080",
        "content": "Preregistration of theoretical predictions helps calibrate confidence that a study tests versus informs a theory; preregistration of analysis plans helps calibrate confidence that findings are not due to chance.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "preregistration of theoretical predictions helps researchers know how to correctly calibrate their confidence that a study tests (versus informs) a theory, whereas preregistration of analysis plans helps researchers know how to correctly calibrate their confidence that a specific finding is unlikely to be due to chance",
        "page_number": 10,
        "context": "Ledgerwood quote on two types",
        "certainty_qualifier": "cited from Ledgerwood"
    },
    {
        "id": "C081",
        "content": "FAIMS Project experience indicates two additional aspects of archaeological research might be registered profitably: data models and data workflows including data capture, manipulation, and analysis.",
        "claim_type": "methodological",
        "reasoning_type": "empirical",
        "evidence_links": ["E009"],
        "verbatim_quote": "In the case of archaeology, experience with the FAIMS Project indicates that two additional aspects of archaeological research might also be registered profitably: data models and data workflows including data capture, manipulation, and analysis.",
        "page_number": 10,
        "context": "Archaeology-specific recommendation",
        "certainty_qualifier": "based on FAIMS experience"
    },
    {
        "id": "C082",
        "content": "Recording data models and workflows will help archaeologists meet emerging standards like TOP Level 2 Guidelines requiring full account of data procedures and description of procedures necessary for independent replication.",
        "claim_type": "methodological",
        "reasoning_type": "pragmatic",
        "evidence_links": [],
        "verbatim_quote": "Recording these aspects of research will help archaeologists meet emerging standards such as the TOP Level 2 Guidelines, which require 'a full account of the procedures used to collect, preprocess, clean, or generate the data' (data provenance) and a 'description of procedures' necessary for an 'independent replication of the research'",
        "page_number": 10,
        "context": "Compliance with transparency standards",
        "certainty_qualifier": "will help (modal)"
    },
    {
        "id": "C083",
        "content": "The abductive and serendipitous nature of archaeology may often make transparency the goal of preregistration, rather than replication.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Thereby acknowledging that the abductive and serendipitous nature of the discipline may often make transparency the goal of preregistration, rather than replication.",
        "page_number": 10,
        "context": "Realistic goal for archaeology",
        "certainty_qualifier": "may often (qualified)"
    },
    {
        "id": "C084",
        "content": "The perfect should not be made the enemy of the good - a best-effort attempt at preregistration would mark an improvement over the present lack of any at all.",
        "claim_type": "methodological",
        "reasoning_type": "normative",
        "evidence_links": [],
        "verbatim_quote": "As noted above, the perfect should not be made the enemy of the good, and a best-effort attempt at preregistration would mark an improvement over the present lack of any at all.",
        "page_number": 10,
        "context": "Pragmatic standard",
        "certainty_qualifier": "normative principle"
    },
    {
        "id": "C085",
        "content": "Preregistration in archaeology could include declarations of research tradition, approach, hypotheses, fieldwork and analysis plans, workflows, and/or data models.",
        "claim_type": "methodological",
        "reasoning_type": "prescriptive",
        "evidence_links": [],
        "verbatim_quote": "Preregistration in archaeology could therefore include declarations of research tradition (e.g., theoretical framework), approach (e.g., inductive, deductive, idiographic, nomothetic, etc.), hypotheses or research questions, fieldwork and analysis plans, workflows, and/or data models.",
        "page_number": 10,
        "context": "What archaeologists could register",
        "certainty_qualifier": "could (modal)"
    },
    {
        "id": "C086",
        "content": "Compared to current state of affairs, articulation of any aspect of research design would mark an improvement.",
        "claim_type": "evaluative",
        "reasoning_type": "comparative",
        "evidence_links": [],
        "verbatim_quote": "Compared to the current state of affairs, articulation of any aspect of research design would mark an improvement.",
        "page_number": 10,
        "context": "Low bar for improvement",
        "certainty_qualifier": "comparative evaluation"
    },
    {
        "id": "C087",
        "content": "An explicit commitment to approach plus either hypotheses or research questions would do the most to combat researcher biases.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "An explicit commitment to a particular approach plus either hypotheses or research questions would do the most to combat researcher biases.",
        "page_number": 10,
        "context": "Priority recommendation",
        "certainty_qualifier": "would do most (comparative)"
    },
    {
        "id": "C088",
        "content": "Articulation of data models and workflows would do the most to overcome just-in-time fieldwork and produce reusable, widely comparable data.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Articulation of data models and workflows would do the most to overcome 'just-in-time' fieldwork and produce reusable, widely comparable data at the end of the project.",
        "page_number": 10,
        "context": "Priority recommendation for data quality",
        "certainty_qualifier": "would do most (comparative)"
    },
    {
        "id": "C089",
        "content": "In choosing a preregistration protocol, archaeologists will face a trade-off between time spent defining approach and resulting loss of flexibility.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "In choosing a preregistration protocol, archaeologists will face a trade-off between the amount of time spent defining their approach and the resulting loss of flexibility.",
        "page_number": 10,
        "context": "Acknowledging costs of preregistration",
        "certainty_qualifier": "will face (prediction)"
    },
    {
        "id": "C090",
        "content": "A stricter preregistration will maximise benefits, whereas a looser preregistration is faster and less constraining but also less effective at avoiding bias or just-in-time fieldwork.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "A 'stricter' preregistration will maximize the benefits of preregistration, whereas a 'looser' preregistration is faster and less constraining – but also less effective at avoiding bias or 'just-in-time' fieldwork.",
        "page_number": 10,
        "context": "Trade-off between strictness and practicality",
        "certainty_qualifier": "stated as principle"
    },
    {
        "id": "C091",
        "content": "A preregistration regime in archaeology could be built using existing knowledge infrastructures like the Open Science Framework.",
        "claim_type": "methodological",
        "reasoning_type": "pragmatic",
        "evidence_links": [],
        "verbatim_quote": "A preregistration regime in archaeology could be built using existing knowledge infrastructures, like the Open Science Framework",
        "page_number": 10,
        "context": "Implementation recommendation",
        "certainty_qualifier": "could (modal)"
    },
    {
        "id": "C092",
        "content": "OSF provides a range of preregistration templates that could be adapted for archaeological use, including templates for qualitative research that accommodate the abductive nature of archaeology.",
        "claim_type": "methodological",
        "reasoning_type": "pragmatic",
        "evidence_links": [],
        "verbatim_quote": "OSF provides a range of preregistration templates that could be adapted for archaeological use (Mellor and DeHaven 2016), including templates for 'qualitative research' that accommodate the nature of archaeology as an abductive discipline while 'providing a check on subjectivity'",
        "page_number": 10,
        "context": "Specific template recommendation",
        "certainty_qualifier": "could (modal)"
    },
    {
        "id": "C093",
        "content": "Archaeology would benefit from the development of domain-specific registration templates, such as those for Social Psychology or replication recipes for various disciplines.",
        "claim_type": "methodological",
        "reasoning_type": "pragmatic",
        "evidence_links": [],
        "verbatim_quote": "Archaeology would benefit from the development of domain-specific registration templates, such as that for Social Psychology (van 't Veer and Giner-Sorolla 2016), or perhaps for specific types of research, on the model of the 'replication recipe' for conducting replication experiments in various disciplines",
        "page_number": 10-11,
        "context": "Future development needs",
        "certainty_qualifier": "would benefit (modal)"
    },
    {
        "id": "C094",
        "content": "Until archaeology-specific templates exist, starting with the OSF Qualitative Research Preregistration template is recommended.",
        "claim_type": "methodological",
        "reasoning_type": "prescriptive",
        "evidence_links": [],
        "verbatim_quote": "Until archaeology-specific templates and protocols exist, we recommend starting with the OSF 'Qualitative Research Preregistration' template",
        "page_number": 11,
        "context": "Interim recommendation",
        "certainty_qualifier": "we recommend (directive)"
    },
    {
        "id": "C095",
        "content": "Key fields from OSF qualitative template relevant to archaeology include: all Study information items, research question typical moments of modification, and indication of inductive vs deductive approach.",
        "claim_type": "methodological",
        "reasoning_type": "prescriptive",
        "evidence_links": [],
        "verbatim_quote": "key fields from this template that are relevant to archaeology include: All 'Study information' items (points 1-5), which provide basic project metadata and commitment to particular research questions should be included. 'Typical moments' of research-question modification represents a useful concept that accommodates the emergent and serendipitous nature of archaeological research.",
        "page_number": 11,
        "context": "Detailed template guidance (beginning)",
        "certainty_qualifier": "prescriptive recommendation"
    }
]

# ============================================================================
# IMPLICIT ARGUMENTS ITEMS
# ============================================================================

implicit_arguments = [
    {
        "id": "IA017",
        "content": "Leading archaeological practitioners in reproducibility should be doing preregistration if the practice is truly important.",
        "reasoning": "Authors critique Marwick and Selden despite praising them - implication is that if preregistration is essential, even leaders should be doing it.",
        "trigger_text": "even archaeologists committed to transparency and reproducibility have not adopted comprehensive preregistration",
        "page_number": 9,
        "context": "Critique of existing examples",
        "theoretical_significance": "Sets high bar for adequate transparency practice"
    },
    {
        "id": "IA018",
        "content": "Metadata incompleteness is a documentation failure rather than a research decision.",
        "reasoning": "Authors treat incomplete metadata (E013) as evidence of poor practice without considering whether complete documentation was research goal.",
        "trigger_text": "Spot checks indicate that data documentation is incomplete; metadata like intra-site find location and artifact type do not accompany some scans",
        "page_number": 9,
        "context": "Evaluating Selden's work",
        "theoretical_significance": "Assumes comprehensive documentation is always appropriate goal"
    },
    {
        "id": "IA019",
        "content": "Grant applications can and should be converted into preregistrations.",
        "reasoning": "Authors suggest using existing grant text for preregistration, assuming alignment between funding requirements and preregistration goals.",
        "trigger_text": "With moderate effort, especially if a grant application exists for this research, it could be elaborated to a full preregistration plan",
        "page_number": 9,
        "context": "Practical suggestion for implementation",
        "theoretical_significance": "Assumes grant proposals adequately specify research design"
    },
    {
        "id": "IA020",
        "content": "Transparency is an acceptable substitute for replication as a goal in abductive disciplines.",
        "reasoning": "Authors retreat from stronger replication goal to transparency goal for archaeology without fully defending this compromise.",
        "trigger_text": "the abductive and serendipitous nature of the discipline may often make transparency the goal of preregistration, rather than replication",
        "page_number": 10,
        "context": "Accommodating archaeological practice",
        "theoretical_significance": "Significant epistemological compromise from original preregistration goals"
    },
    {
        "id": "IA021",
        "content": "OSF qualitative research template is appropriate for archaeology despite being designed for social sciences.",
        "reasoning": "Authors recommend this template without detailed consideration of archaeology-specific requirements or mismatches.",
        "trigger_text": "we recommend starting with the OSF 'Qualitative Research Preregistration' template... It is intended for a range of social science research",
        "page_number": 11,
        "context": "Template recommendation",
        "theoretical_significance": "Assumes sufficient similarity between archaeology and social sciences"
    }
]

# ============================================================================
# UPDATE EXTRACTION DATA
# ============================================================================

# Add new items to extraction
data['evidence'].extend(evidence_items)
data['claims'].extend(claims_items)
data['implicit_arguments'].extend(implicit_arguments)

# Update extraction notes
data['extraction_notes'] = {
    'pass': 1,
    'section_extracted': 'Groups 1-4: Introduction through Introducing to Practice, pages 2-11',
    'extraction_strategy': 'Section 4: Liberal extraction focusing on: (1) OSF search evidence showing minimal archaeological preregistration, (2) evaluation of existing examples (Marwick, Selden), (3) detailed prescriptive claims about what to register, (4) OSF template recommendations with field-by-field guidance (only beginning extracted - full template list very detailed), (5) implicit assumptions about documentation standards and template appropriateness. Longest section ~1800 words.',
    'known_uncertainties': [
        'Only extracted beginning of detailed OSF template recommendations (C095) - full list continues to end of section',
        'Distinction between what "could" vs "should" be registered important for later analysis',
        'Trade-off claim (C089-C090) acknowledges costs but overall chapter minimises them'
    ],
    'section_word_count_estimate': 5400
}

data['extraction_timestamp'] = datetime.now().isoformat() + 'Z'

# Save updated extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print("=" * 80)
print("PASS 1 - SECTION GROUP 4 EXTRACTION COMPLETE")
print("=" * 80)
print()
print(f"Section: Introducing Preregistration to Archaeological Practice")
print(f"Pages: 8-11")
print(f"Estimated word count: ~1800 words")
print()
print("Items extracted:")
print(f"  Evidence: {len(evidence_items)} items (E011-E013)")
print(f"  Claims: {len(claims_items)} items (C066-C095)")
print(f"  Implicit Arguments: {len(implicit_arguments)} items (IA017-IA021)")
print()
print(f"Total this section: {len(evidence_items) + len(claims_items) + len(implicit_arguments)} items")
print()
print("Cumulative extraction:")
print(f"  Evidence: 13 items total")
print(f"  Claims: 95 items total")
print(f"  Implicit Arguments: 21 items total")
print(f"  TOTAL: 129 items extracted so far")
print()
print("✓ Section 4 extraction complete")
print()
print("NOTE: OSF template recommendations continue beyond C095 but are very detailed.")
print("Pass 2 may consolidate some detailed template claims.")
print()
