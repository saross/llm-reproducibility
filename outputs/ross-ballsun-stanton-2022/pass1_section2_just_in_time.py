#!/usr/bin/env python3
"""
Pass 1: Liberal Claims & Evidence Extraction
Section Group 2: The Problem of "Just-in-Time" Archaeology
Pages: 5-6 (PDF pages, section 2)

Extraction Strategy:
- Evidence from processual archaeology literature (1970s)
- Claims about current archaeological practice problems
- Evidence from FAIMS project experience
- Implicit arguments about proper research practice
- Focus on sociotechnical barriers and data quality issues

Word count estimate: ~1000 words
"""

import json
from datetime import datetime

# Load existing extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'r') as f:
    data = json.load(f)

# Section Group 2: "Just-in-Time" Archaeology Problem
# Pages 5-6 of PDF

# ============================================================================
# EVIDENCE ITEMS
# ============================================================================

evidence_items = [
    {
        "id": "E005",
        "content": "In the 1970s, Hole criticised archaeologists for focusing on fieldwork and analytical methods rather than research design and hypothesis development, calling for more 'thought' before methodological manipulations.",
        "evidence_type": "historical_source",
        "source_type": "published_research",
        "verbatim_quote": "In the 1970s, Hole criticized archaeologists' tendency to focus on fieldwork and analytical methods rather than research design, especially the development of hypotheses or models. He called for more 'thought' before the archaeologist turned to 'methodological manipulations' (Hole 1973:32).",
        "page_number": 5,
        "context": "Establishing historical precedent for research design critique",
        "interpretation_notes": "Shows problem recognized 50 years ago in processual archaeology"
    },
    {
        "id": "E006",
        "content": "French (1973) observed that problems must be defined before developing means to collect data, and that questions dictate recovery methods.",
        "evidence_type": "historical_source",
        "source_type": "published_research",
        "verbatim_quote": "[I]t is essential and (?) obligatory to define the problems before developing or choosing the means used to collect the data necessary to examine these problems and the hypotheses explicit in them. In other words, the questions asked dictate the methods of recovery; one selects the recovery technique to suit the problem in hand",
        "page_number": 5,
        "context": "1970s processual archaeology on research design",
        "interpretation_notes": "Long-standing recognition that data collection should follow research questions"
    },
    {
        "id": "E007",
        "content": "French (1973) emphasised the importance of data provenance documentation and recommended archaeologists specify programs and standards governing data collection for quality and comparability assessment.",
        "evidence_type": "historical_source",
        "source_type": "published_research",
        "verbatim_quote": "French went on to emphasize the importance of what would now be termed data provenance... He further recommended that archaeologists specify the program and standards governing data collection. Only by doing so can the quantity, quality, and comparability of archaeological data be assessed.",
        "page_number": 5,
        "context": "1970s call for data documentation standards",
        "interpretation_notes": "Data provenance concerns pre-date digital archaeology"
    },
    {
        "id": "E008",
        "content": "The lack of shared or articulated standards of data acquisition and documentation that French described in 1973 remains widespread today, undermining data comparability.",
        "evidence_type": "literature_synthesis",
        "source_type": "published_research",
        "verbatim_quote": "The situation French described – a lack of shared (or at least articulated) standards of data acquisition and documentation – remains widespread today, undermining the comparability of data from different projects (French 1973:106; Atici et al. 2013; Faniel et al. 2013; Holub et al. 2018).",
        "page_number": 5,
        "context": "Persistent problem in archaeological data practice",
        "interpretation_notes": "Problem identified 50 years ago still exists - citations from 2013-2018 confirm"
    },
    {
        "id": "E009",
        "content": "The FAIMS project has customised field data collection systems for over 60 workflows at more than 40 projects in archaeology, ecology, geoscience, and history since 2014.",
        "evidence_type": "project_data",
        "source_type": "authors_research",
        "verbatim_quote": "Our information infrastructure work, related to the Field Acquired Information Management Systems (FAIMS) project, has customized field data collection systems for over sixty workflows at more than forty projects in archaeology, ecology, geoscience, history, and other disciplines since 2014",
        "page_number": 6,
        "context": "Establishing authors' empirical basis for claims",
        "interpretation_notes": "Authors draw on substantial practical experience implementing digital field systems"
    },
    {
        "id": "E010",
        "content": "FAIMS project work has found that field researchers broadly, and archaeologists particularly, under-invest in planning and preparation in three specific ways.",
        "evidence_type": "empirical_observation",
        "source_type": "authors_research",
        "verbatim_quote": "We have found that field researchers broadly, and archaeologists particularly, under-invest in planning and preparation in three ways.",
        "page_number": 6,
        "context": "Empirical findings from FAIMS implementations",
        "interpretation_notes": "Direct observational evidence from authors' field experience"
    }
]

# ============================================================================
# CLAIMS ITEMS
# ============================================================================

claims_items = [
    {
        "id": "C026",
        "content": "The biases and perverse incentives that preregistration addresses in other disciplines also exist in archaeology.",
        "claim_type": "empirical",
        "reasoning_type": "analogical",
        "evidence_links": [],
        "verbatim_quote": "The biases and perverse incentives that preregistration was designed to combat in other disciplines also exist in archaeology.",
        "page_number": 5,
        "context": "Opening of Section 2",
        "certainty_qualifier": "asserted without specific archaeological evidence"
    },
    {
        "id": "C027",
        "content": "Processual archaeology's scientific approach has recognized problems of biases and the need to reveal aims for half a century.",
        "claim_type": "empirical",
        "reasoning_type": "historical",
        "evidence_links": ["E005"],
        "verbatim_quote": "Processual archaeology's 'scientific approach', with its emphasis on revealing aims and biases and its problem-orientation, has recognized these problems for half a century",
        "page_number": 5,
        "context": "Historical precedent in archaeology",
        "certainty_qualifier": "documented in 1970s literature"
    },
    {
        "id": "C028",
        "content": "The relevance of early processual thought to the current problem is striking.",
        "claim_type": "evaluative",
        "reasoning_type": "interpretive",
        "evidence_links": ["E005", "E006"],
        "verbatim_quote": "Indeed, the relevance of early processual thought to the current problem is striking.",
        "page_number": 5,
        "context": "Authors' evaluation of historical literature",
        "certainty_qualifier": "authors' judgement"
    },
    {
        "id": "C029",
        "content": "Merely collecting more data does not automatically support the syntheses needed to understand the past; data-recovery techniques must harmonise with theoretical approaches.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": ["E006"],
        "verbatim_quote": "In short, merely collecting more data does not automatically support the syntheses needed to produce a better understanding of the past, and data-recovery techniques must harmonize with theoretical approaches",
        "page_number": 5,
        "context": "Why planning matters",
        "certainty_qualifier": "asserted as principle"
    },
    {
        "id": "C030",
        "content": "Preregistration encourages the planning and preparation necessary to collect data appropriate to project aims now and useful to others in the future.",
        "claim_type": "methodological",
        "reasoning_type": "pragmatic",
        "evidence_links": [],
        "verbatim_quote": "Preregistration encourages the planning and preparation necessary to collect data appropriate to a project's aims now and useful to others in the future.",
        "page_number": 5,
        "context": "Connection to preregistration solution",
        "certainty_qualifier": "encourages (modal)"
    },
    {
        "id": "C031",
        "content": "Preregistration can help researchers articulate their specific theoretical approach and research tradition.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Preregistration can, moreover, help researchers articulate their specific theoretical approach and research tradition.",
        "page_number": 5,
        "context": "Additional benefit of preregistration",
        "certainty_qualifier": "can (modal)"
    },
    {
        "id": "C032",
        "content": "Processualism and post-processualism are examples of competing Lakatosian research programs with their own hard-core truths and soft outer shell of current research.",
        "claim_type": "theoretical",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "They are examples of competing Lakatosian research programs, each with their own 'hard-core' of truths which they take to be self-evident and 'soft outer shell' of current, unproven, research questions (Lakatos 1978).",
        "page_number": 5-6,
        "context": "Philosophical framing of theoretical traditions",
        "certainty_qualifier": "applies Lakatosian framework"
    },
    {
        "id": "C033",
        "content": "Preregistration makes researcher assumptions more explicit, allowing them to be scrutinised.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Preregistration makes such researcher assumptions more explicit (Johnson 2010:3).",
        "page_number": 6,
        "context": "Transparency benefit of preregistration",
        "certainty_qualifier": "stated as fact"
    },
    {
        "id": "C034",
        "content": "Preregistration mitigates the sociotechnical barrier of substituting remedial work at the end of a project for proper planning at the beginning.",
        "claim_type": "methodological",
        "reasoning_type": "pragmatic",
        "evidence_links": [],
        "verbatim_quote": "Preregistration also mitigates a specific sociotechnical barrier to the adoption of digital approaches in archaeology. Archaeologists tend to substitute remedial work at the end of a project for proper planning and preparation at the beginning (Sobotkova et al. 2016).",
        "page_number": 6,
        "context": "Sociotechnical problem preregistration addresses",
        "certainty_qualifier": "documented in Sobotkova et al."
    },
    {
        "id": "C035",
        "content": "The tendency to underinvest in planning, along with print publication of datasets, impedes production of comprehensive reusable datasets and undermines cultivation of deeper digital practice.",
        "claim_type": "empirical",
        "reasoning_type": "observational",
        "evidence_links": [],
        "verbatim_quote": "This tendency, along with the continuing prevalence of print publication of datasets like artifact catalogs, impedes the production of comprehensive, reusable datasets in archaeology. It also undermines the cultivation of deeper digital practice more generally.",
        "page_number": 6,
        "context": "Consequences of poor planning",
        "certainty_qualifier": "stated as observed pattern"
    },
    {
        "id": "C036",
        "content": "Archaeologists tolerate lack of detail or precision in documentation, not taking time to build controlled vocabularies or leaving important information for free-text fields.",
        "claim_type": "empirical",
        "reasoning_type": "observational",
        "evidence_links": ["E009", "E010"],
        "verbatim_quote": "First, archaeologists tolerate a lack of detail or precision in their documentation. For example, they do not take the time to build and deploy controlled vocabularies or they leave important and recurring information for 'notes' or other free-text fields.",
        "page_number": 6,
        "context": "First way archaeologists under-invest - FAIMS observation",
        "certainty_qualifier": "observed in FAIMS implementations"
    },
    {
        "id": "C037",
        "content": "Haste and imprecision in paper-based recording reduces up-front investment but adds a larger burden of post-fieldwork data cleaning.",
        "claim_type": "empirical",
        "reasoning_type": "observational",
        "evidence_links": ["E010"],
        "verbatim_quote": "This haste and imprecision reduces the up-front investment in data and workflow modeling for harried academics and consultants but adds an implicit cost: a much larger burden of post-fieldwork data cleaning.",
        "page_number": 6,
        "context": "Consequences of imprecise documentation",
        "certainty_qualifier": "observed pattern"
    },
    {
        "id": "C038",
        "content": "Forms and protocols assume implicit knowledge transmitted orally, reducing transparency and failing to record metadata needed for data reuse.",
        "claim_type": "empirical",
        "reasoning_type": "observational",
        "evidence_links": ["E010"],
        "verbatim_quote": "Second, forms and protocols assume a great deal of implicit knowledge transmitted orally, often informally, at the project. This practice reduces the transparency of fieldwork and fails to record important metadata needed later for data reuse.",
        "page_number": 6,
        "context": "Second way archaeologists under-invest",
        "certainty_qualifier": "observed in FAIMS implementations"
    },
    {
        "id": "C039",
        "content": "Implicit methods and metadata are lost through epistemic turnover when team members forget, become uncontactable, or move to other projects.",
        "claim_type": "empirical",
        "reasoning_type": "observational",
        "evidence_links": [],
        "verbatim_quote": "Implicit methods and metadata are lost by team members, volunteers, and students who forget just how things were done, are uncontactable, or who have moved onto other projects. This epistemic turnover impedes later understanding and reuse",
        "page_number": 6,
        "context": "Consequences of implicit knowledge",
        "certainty_qualifier": "observed pattern"
    },
    {
        "id": "C040",
        "content": "Project leaders develop record-keeping practices late, leaving insufficient time to test and refine them with realistic trial data.",
        "claim_type": "empirical",
        "reasoning_type": "observational",
        "evidence_links": ["E010"],
        "verbatim_quote": "Third, project leaders tend to develop record-keeping or documentation practices like forms and protocols late, shortly before fieldwork begins, leaving insufficient time to test and refine them with realistic trial data.",
        "page_number": 6,
        "context": "Third way archaeologists under-invest",
        "certainty_qualifier": "observed in FAIMS implementations"
    },
    {
        "id": "C041",
        "content": "Late development of protocols contributes to emergent research design where researchers elaborate and modify approaches during fieldwork.",
        "claim_type": "empirical",
        "reasoning_type": "observational",
        "evidence_links": [],
        "verbatim_quote": "It also contributes to a feature common to many fieldwork-based domains, a tendency for research design to be 'emergent' – for researchers to elaborate and modify approaches, methods, tools, technologies, and practices during fieldwork when working with real data (Borgman 2015:106–107).",
        "page_number": 6-7,
        "context": "Consequences of late planning",
        "certainty_qualifier": "documented by Borgman for fieldwork domains"
    },
    {
        "id": "C042",
        "content": "Emergent design produces datasets not consistent or comparable across a single season without manual reconciliation, let alone more broadly.",
        "claim_type": "empirical",
        "reasoning_type": "observational",
        "evidence_links": [],
        "verbatim_quote": "the practice produces datasets that are not even consistent or comparable across a single season at a single project without considerable manual reconciliation, let alone more broadly.",
        "page_number": 7,
        "context": "Data quality consequences of emergent design",
        "certainty_qualifier": "observed outcome"
    },
    {
        "id": "C043",
        "content": "These practices constitute a sociotechnical hurdle: underinvestment in early stages and accrual of technical debt requiring much more time to fix data at project end.",
        "claim_type": "empirical",
        "reasoning_type": "synthetic",
        "evidence_links": ["E009", "E010"],
        "verbatim_quote": "Together, these practices constitute a sociotechnical hurdle to effective digital archaeology: underinvestment in the early stages of a project and subsequent accrual of technical debt, requiring the expenditure of much more time and effort to 'fix' data at the end of a project",
        "page_number": 7,
        "context": "Summary of problem",
        "certainty_qualifier": "synthesising FAIMS observations"
    }
]

# ============================================================================
# IMPLICIT ARGUMENTS ITEMS
# ============================================================================

implicit_arguments = [
    {
        "id": "IA007",
        "content": "Early processual archaeology's methodological insights remain valid and should inform current practice.",
        "reasoning": "Authors invoke 1970s processual literature approvingly without acknowledging subsequent critiques or changed disciplinary context.",
        "trigger_text": "Indeed, the relevance of early processual thought to the current problem is striking.",
        "page_number": 5,
        "context": "Citing Hole and French from 1973",
        "theoretical_significance": "Selectively draws on processual legacy while paper elsewhere acknowledges post-processual approaches"
    },
    {
        "id": "IA008",
        "content": "Data should be designed for future reuse and large-scale synthesis, not just immediate project needs.",
        "reasoning": "Implicit value judgement that data comparability and aggregation should be prioritised over project-specific documentation approaches.",
        "trigger_text": "impedes the production of comprehensive, reusable datasets... undermines the cultivation of deeper digital practice",
        "page_number": 6,
        "context": "Critique of current practices",
        "theoretical_significance": "Assumes synthesis and reuse are more important than flexible, responsive fieldwork documentation"
    },
    {
        "id": "IA009",
        "content": "Digital data collection is inherently superior to paper-based approaches.",
        "reasoning": "Authors criticise practices that 'exploit the forgiving nature' of paper without acknowledging any advantages of paper recording.",
        "trigger_text": "These practices exploit the forgiving nature of the medium, relying on the ability to write 'in the margins' or 'on the back of the page'.",
        "page_number": 6,
        "context": "Critique of paper recording",
        "theoretical_significance": "Implicitly privileges digital over analog approaches"
    },
    {
        "id": "IA010",
        "content": "Oral transmission of methodological knowledge is inadequate and must be replaced by formal documentation.",
        "reasoning": "Treats oral/apprenticeship transmission as simply a loss rather than recognising it as traditional disciplinary practice with own advantages.",
        "trigger_text": "forms and protocols assume a great deal of implicit knowledge transmitted orally, often informally, at the project",
        "page_number": 6,
        "context": "Second type of under-investment",
        "theoretical_significance": "Devalues craft knowledge and oral training traditions in archaeology"
    },
    {
        "id": "IA011",
        "content": "Tinkering and emergent design during fieldwork are problems to be minimised rather than necessary adaptations to fieldwork contingencies.",
        "reasoning": "Authors acknowledge tinkering may be 'necessary' but frame it primarily as a problem rather than considering benefits of adaptive approaches.",
        "trigger_text": "Although a certain amount of 'tinkering'... may be necessary to mitigate the unpredictability of fieldwork, the practice produces datasets that are not even consistent or comparable",
        "page_number": 6-7,
        "context": "Critique of emergent design",
        "theoretical_significance": "Tensions between standardisation/planning and fieldwork flexibility"
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
    'section_extracted': 'Groups 1-2: Introduction through Just-in-Time Problem, pages 2-6',
    'extraction_strategy': 'Section 2: Liberal extraction focusing on: (1) historical evidence from 1970s processual archaeology, (2) empirical observations from FAIMS project, (3) claims about archaeological practice problems, (4) implicit assumptions about digital vs analog and planning vs emergence. Three types of under-investment documented: imprecise documentation, implicit knowledge, late development.',
    'known_uncertainties': [
        'Some FAIMS observations might be better coded as evidence rather than claims',
        'Distinction between documented problems (E008) and observed problems (C036-C042) may need refinement',
        'Several implicit arguments about craft knowledge and fieldwork flexibility'
    ],
    'section_word_count_estimate': 2600
}

data['extraction_timestamp'] = datetime.now().isoformat() + 'Z'

# Save updated extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print("=" * 80)
print("PASS 1 - SECTION GROUP 2 EXTRACTION COMPLETE")
print("=" * 80)
print()
print(f"Section: The Problem of 'Just-in-Time' Archaeology")
print(f"Pages: 5-6")
print(f"Estimated word count: ~1000 words")
print()
print("Items extracted:")
print(f"  Evidence: {len(evidence_items)} items (E005-E010)")
print(f"  Claims: {len(claims_items)} items (C026-C043)")
print(f"  Implicit Arguments: {len(implicit_arguments)} items (IA007-IA011)")
print()
print(f"Total this section: {len(evidence_items) + len(claims_items) + len(implicit_arguments)} items")
print()
print("Cumulative extraction:")
print(f"  Evidence: 10 items total")
print(f"  Claims: 43 items total")
print(f"  Implicit Arguments: 11 items total")
print(f"  TOTAL: 64 items extracted so far")
print()
print("✓ Section 2 extraction complete")
print()
