#!/usr/bin/env python3
"""
Pass 1, Section 2: Liberal Claims/Evidence Extraction
Ross et al. 2009 - Remote Sensing and Archaeological Prospection in Apulia, Italy

Section: L'Amastuola Archaeological Project + Satellite Image Data (~1100 words, pages 424-425)

Approach: Liberal extraction, cast wide net, aim for over-extraction.
Items will be consolidated in Pass 2. When uncertain, include it.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Load current extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

# ============================================================================
# EVIDENCE - Liberal extraction
# ============================================================================

evidence_items = [
    {
        "evidence_id": "E010",
        "content": "The L'Amastuola Archaeological Project target area corresponds to a 100 square kilometre area, designed by Crielaard and Burgers of Vrije Universiteit Amsterdam and begun in 2003.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "The area investigated in the present project corresponds to the target area of the L'Amastuola Archaeological Project, designed by Jan Paul Crielaard and Gert-Jan Burgers of Vrije Universiteit Amsterdam and begun in 2003",
        "page": 424,
        "relevance": "Establishes project context and timeline",
        "supports_claims": ["C027"]
    },
    {
        "evidence_id": "E011",
        "content": "The MTS sister project was conducted between 2003 and 2007, involving systematic survey of a transect from the coastal plain of Taranto into the karstic Murge uplands.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "The MTS, a sister project conducted between 2003 and 2007, involved systematic survey of a transect extending from the coastal plain of Taranto into the karstic Murge uplands.",
        "page": 424,
        "relevance": "Describes MTS survey design and extent",
        "supports_claims": ["C028"]
    },
    {
        "evidence_id": "E012",
        "content": "In 2007, MTS members assisted with ground control and systematic investigation of features located through remote sensing.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "In 2007, members of this survey also assisted with ground control and systematic investigation of selected features located through remote sensing.",
        "page": 424,
        "relevance": "Documents collaboration between projects",
        "supports_claims": ["C029"]
    },
    {
        "evidence_id": "E013",
        "content": "Vrije Universiteit's research program in Salento began in 1981, encompassing an area from the Salento Isthmus between Taranto and Brindisi.",
        "evidence_type": "historical_observation",
        "verbatim_quote": "Both the L'Amastuola Archaeological Project and the MTS fit into a research program started by Vrije Universiteit in 1981 and encompassing a much wider area—from the Salento Isthmus between Taranto on the Ionian Sea and Brindisi on the Adriatic",
        "page": 424,
        "relevance": "Establishes long-term research program context",
        "supports_claims": ["C030"]
    },
    {
        "evidence_id": "E014",
        "content": "From the beginning, Vrije Universiteit fieldwork combined excavation, field survey, environmental research, and remote sensing.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "From the beginning, the Vrije Universiteit fieldwork in Salento combined excavation, field survey, environmental research, and remote sensing to investigate settlement and landscape evolution in the study region.",
        "page": 424,
        "relevance": "Documents integrated methodological approach tradition",
        "supports_claims": ["C031"]
    },
    {
        "evidence_id": "E015",
        "content": "The research program initially focused on effects of Romanization on regional societies (3rd-1st centuries BC), but gradually widened to include early Greek colonization (8th-7th centuries BC) and subsequent urbanization.",
        "evidence_type": "historical_observation",
        "verbatim_quote": "Initially, Vrije Universiteit fieldwork focused on the effects of Romanization on regional societies (3rd–1st centuries B.C.), but gradually the scope was widened to include the impact of early Greek colonization (8th–7th centuries B.C.) and subsequent urbanization",
        "page": 424,
        "relevance": "Documents evolution of research questions",
        "supports_claims": ["C032"]
    },
    {
        "evidence_id": "E016",
        "content": "L'Amastuola occupies one of the most prominent hill peaks in the entire Taranto region.",
        "evidence_type": "environmental_observation",
        "verbatim_quote": "Setting aside the historical debate, the site occupies one of the most prominent hill peaks in the entire Taranto region.",
        "page": 424,
        "relevance": "Documents site's topographic prominence",
        "supports_claims": ["C033", "C034"]
    },
    {
        "evidence_id": "E017",
        "content": "The catchment area of L'Amastuola offers both fertile inland soils for cereal cultivation and a coastal lagoon zone amenable to animal husbandry.",
        "evidence_type": "environmental_observation",
        "verbatim_quote": "its catchment area offers both fertile inland soils for cereal cultivation and a coastal lagoon zone amenable to animal husbandry.",
        "page": 425,
        "relevance": "Documents resource diversity around site",
        "supports_claims": ["C035"]
    },
    {
        "evidence_id": "E018",
        "content": "Early archaeological prospection culminating with the intensive MTS established that the area was densely inhabited throughout antiquity.",
        "evidence_type": "archaeological_observation",
        "verbatim_quote": "It comes as no surprise that early archaeological prospection culminating with the intensive MTS has established that the area was densely inhabited throughout antiquity.",
        "page": 425,
        "relevance": "Documents settlement density in study area",
        "supports_claims": ["C036"]
    },
    {
        "evidence_id": "E019",
        "content": "The region was much more settled in antiquity than during later periods, with very few later habitation sites identified.",
        "evidence_type": "archaeological_observation",
        "verbatim_quote": "Indeed, the region was much more settled in antiquity than during later periods, for which very few habitation sites have been identified.",
        "page": 425,
        "relevance": "Contrasts ancient vs. modern settlement patterns",
        "supports_claims": ["C037"]
    },
    {
        "evidence_id": "E020",
        "content": "Early prospection discovered dozens of small ancient rural sites spread evenly over the landscape, with clustering in some places in village-like settlements.",
        "evidence_type": "archaeological_observation",
        "verbatim_quote": "Early prospection discovered dozens of small, ancient, rural sites that are spread evenly over the landscape, but clustering in some places in village-like settlements.",
        "page": 425,
        "relevance": "Describes settlement pattern characteristics",
        "supports_claims": ["C038"]
    },
    {
        "evidence_id": "E021",
        "content": "The MTS recorded large amounts of ancient off-site material suggesting intensive exploitation, particularly during late Classical and early Hellenistic periods (late 5th through 3rd centuries BC).",
        "evidence_type": "archaeological_observation",
        "verbatim_quote": "The large amount of ancient off-site material recorded by the MTS also suggests that the area was exploited intensively, in particular during the late Classical and early Hellenistic periods (late 5th through 3rd centuries B.C.).",
        "page": 425,
        "relevance": "Documents peak period of landscape exploitation",
        "supports_claims": ["C039"]
    },
    {
        "evidence_id": "E022",
        "content": "QuickBird was the highest-resolution satellite imagery commercially available at project initiation, with optimal panchromatic resolution of 0.61 m and multispectral resolution of 2.44 m.",
        "evidence_type": "technical_specification",
        "verbatim_quote": "At the time the project was initiated, QuickBird was the highest-resolution satellite imagery commercially available, with optimal panchromatic resolution of 0.61 m and multispectral resolution of 2.44 m.",
        "page": 425,
        "relevance": "Documents imagery resolution capabilities",
        "supports_claims": ["C040", "C041"]
    },
    {
        "evidence_id": "E023",
        "content": "QuickBird's multispectral information includes separate red, green, blue, and near-infrared (NIR) bands.",
        "evidence_type": "technical_specification",
        "verbatim_quote": "QuickBird's multispectral information includes separate red, green, blue, and near-infrared (NIR) bands.",
        "page": 425,
        "relevance": "Specifies spectral band capabilities",
        "supports_claims": ["C042"]
    },
    {
        "evidence_id": "E024",
        "content": "The image used was archival rather than newly tasked, collected on 18 March 2004.",
        "evidence_type": "technical_specification",
        "verbatim_quote": "Our image was archival rather than newly tasked, collected on 18 March 2004",
        "page": 425,
        "relevance": "Documents image acquisition date and type",
        "supports_claims": ["C043", "C044"]
    },
    {
        "evidence_id": "E025",
        "content": "There were only modest changes in the landscape over the three-year interval between image acquisition (March 2004) and the beginning of the project (2007).",
        "evidence_type": "environmental_observation",
        "verbatim_quote": "the cost savings offered by archival imagery was justified because there were only modest changes in the landscape over the three-year interval between image acquisition and the beginning of our project",
        "page": 425,
        "relevance": "Justifies use of archival imagery",
        "supports_claims": ["C043"]
    },
    {
        "evidence_id": "E026",
        "content": "The early spring date (18 March) captured vigorous plant growth, increasing contrast between healthy and stressed vegetation that can reveal archaeological remains.",
        "evidence_type": "technical_observation",
        "verbatim_quote": "The early spring date of the image captured vigorous plant growth, increasing the contrast between healthy and stressed vegetation that can reveal archaeological remains.",
        "page": 426,
        "relevance": "Explains seasonal timing advantages",
        "supports_claims": ["C045"]
    },
    {
        "evidence_id": "E027",
        "content": "By mid-March, plant growth had not proceeded so far as to entirely obscure the ground, allowing for detection of soil marks.",
        "evidence_type": "technical_observation",
        "verbatim_quote": "At the same time, plant growth had not proceeded so far by mid-March as to entirely obscure the ground, allowing for the detection of soil marks.",
        "page": 426,
        "relevance": "Explains ground visibility at acquisition date",
        "supports_claims": ["C046"]
    },
    {
        "evidence_id": "E028",
        "content": "A combination of clear sky, excellent environmental quality, and low off-nadir angle combined to produce an unobstructed image with relatively little distortion.",
        "evidence_type": "technical_observation",
        "verbatim_quote": "A combination of factors including clear sky, excellent environmental quality, and a low off-nadir angle combined to produce an unobstructed image with relatively little distortion.",
        "page": 426,
        "relevance": "Documents image quality factors",
        "supports_claims": ["C047"]
    }
]

# ============================================================================
# CLAIMS - Liberal extraction
# ============================================================================

claims_items = [
    {
        "claim_id": "C027",
        "content": "The L'Amastuola Archaeological Project aims to investigate the material culture, settlement patterns, and landscape archaeology of L'Amastuola.",
        "claim_type": "research_objective",
        "verbatim_quote": "with the aim of investigating the material culture, settlement patterns, and landscape archaeology of the site of L'Amastuola",
        "page": 424,
        "supporting_evidence": ["E010"],
        "confidence": "high",
        "relevance": "Defines project research objectives"
    },
    {
        "claim_id": "C028",
        "content": "The MTS provides a comparative dataset for the present remote sensing project.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "The MTS provides a comparative dataset for the present remote sensing project.",
        "page": 424,
        "supporting_evidence": ["E011", "E012"],
        "confidence": "high",
        "relevance": "Establishes role of MTS in study design"
    },
    {
        "claim_id": "C029",
        "content": "Collaboration between the MTS team and remote sensing project enabled ground control of remotely sensed features.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "In 2007, members of this survey also assisted with ground control and systematic investigation of selected features located through remote sensing.",
        "page": 424,
        "supporting_evidence": ["E012"],
        "confidence": "high",
        "relevance": "Documents methodological collaboration"
    },
    {
        "claim_id": "C030",
        "content": "The L'Amastuola and MTS projects fit into a long-term research program in Salento that connects the peninsula to the rest of Italy.",
        "claim_type": "contextual_claim",
        "verbatim_quote": "Both the L'Amastuola Archaeological Project and the MTS fit into a research program started by Vrije Universiteit in 1981 and encompassing a much wider area—from the Salento Isthmus between Taranto on the Ionian Sea and Brindisi on the Adriatic, which connects the Salento Peninsula to the rest of Italy.",
        "page": 424,
        "supporting_evidence": ["E013"],
        "confidence": "high",
        "relevance": "Provides long-term research context"
    },
    {
        "claim_id": "C031",
        "content": "An integrated approach combining excavation, survey, environmental research, and remote sensing has characterized Vrije Universiteit's Salento fieldwork from the beginning.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "From the beginning, the Vrije Universiteit fieldwork in Salento combined excavation, field survey, environmental research, and remote sensing to investigate settlement and landscape evolution in the study region.",
        "page": 424,
        "supporting_evidence": ["E014"],
        "confidence": "high",
        "relevance": "Establishes tradition of methodological integration"
    },
    {
        "claim_id": "C032",
        "content": "The research program's scope has expanded from Romanization to include Greek colonization and urbanization issues.",
        "claim_type": "historical_claim",
        "verbatim_quote": "Initially, Vrije Universiteit fieldwork focused on the effects of Romanization on regional societies (3rd–1st centuries B.C.), but gradually the scope was widened to include the impact of early Greek colonization (8th–7th centuries B.C.) and subsequent urbanization—issues that have also motivated research around L'Amastuola.",
        "page": 424,
        "supporting_evidence": ["E015"],
        "confidence": "high",
        "relevance": "Documents evolution of research questions"
    },
    {
        "claim_id": "C033",
        "content": "L'Amastuola is considered a key site for studying early Greek colonization, a much-debated phenomenon among classical archaeologists and ancient historians.",
        "claim_type": "significance_claim",
        "verbatim_quote": "L'Amastuola is considered a key site for the study of early Greek colonization, a much-debated phenomenon among modern classical archaeologists and ancient historians.",
        "page": 424,
        "supporting_evidence": ["E016"],
        "confidence": "high",
        "relevance": "Establishes site significance for broader debates"
    },
    {
        "claim_id": "C034",
        "content": "The site's location on a prominent hilltop was selected with strategic or visibility considerations.",
        "claim_type": "interpretive_claim",
        "verbatim_quote": "Setting aside the historical debate, the site occupies one of the most prominent hill peaks in the entire Taranto region. Apart from its dominant location",
        "page": 424,
        "supporting_evidence": ["E016"],
        "confidence": "medium",
        "relevance": "Interprets site location choice"
    },
    {
        "claim_id": "C035",
        "content": "The settlement location was selected with a view to exploiting a range of resource zones.",
        "claim_type": "interpretive_claim",
        "verbatim_quote": "the settlement seems to have been selected with a view to exploiting a range of resource zones",
        "page": 424,
        "supporting_evidence": ["E017"],
        "confidence": "high",
        "relevance": "Interprets settlement location strategy"
    },
    {
        "claim_id": "C036",
        "content": "Dense ancient habitation in the area is unsurprising given the site's characteristics and resource base.",
        "claim_type": "interpretive_claim",
        "verbatim_quote": "It comes as no surprise that early archaeological prospection culminating with the intensive MTS has established that the area was densely inhabited throughout antiquity.",
        "page": 425,
        "supporting_evidence": ["E018"],
        "confidence": "high",
        "relevance": "Connects settlement density to environmental factors"
    },
    {
        "claim_id": "C037",
        "content": "Settlement patterns changed dramatically from antiquity to later periods, with much lower habitation density in post-ancient times.",
        "claim_type": "comparative_claim",
        "verbatim_quote": "Indeed, the region was much more settled in antiquity than during later periods, for which very few habitation sites have been identified.",
        "page": 425,
        "supporting_evidence": ["E019"],
        "confidence": "high",
        "relevance": "Documents diachronic settlement pattern change"
    },
    {
        "claim_id": "C038",
        "content": "Ancient settlement in the region consisted of numerous small rural sites with both dispersed and nucleated patterns.",
        "claim_type": "descriptive_claim",
        "verbatim_quote": "Early prospection discovered dozens of small, ancient, rural sites that are spread evenly over the landscape, but clustering in some places in village-like settlements.",
        "page": 425,
        "supporting_evidence": ["E020"],
        "confidence": "high",
        "relevance": "Characterizes settlement pattern"
    },
    {
        "claim_id": "C039",
        "content": "The area experienced peak intensive exploitation during the late Classical and early Hellenistic periods.",
        "claim_type": "interpretive_claim",
        "verbatim_quote": "The large amount of ancient off-site material recorded by the MTS also suggests that the area was exploited intensively, in particular during the late Classical and early Hellenistic periods (late 5th through 3rd centuries B.C.).",
        "page": 425,
        "supporting_evidence": ["E021"],
        "confidence": "high",
        "relevance": "Identifies period of peak land use"
    },
    {
        "claim_id": "C040",
        "content": "The existing body of settlement information from survey offered an ideal test case for remote sensing.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "This existing body of settlement information acquired through survey offered an ideal test case for remote sensing.",
        "page": 425,
        "supporting_evidence": ["E018", "E021"],
        "confidence": "high",
        "relevance": "Justifies study area selection for methodological testing"
    },
    {
        "claim_id": "C041",
        "content": "The results of remote sensing investigation contribute to a fuller understanding of settlement patterns and environmental conditions underpinning them.",
        "claim_type": "significance_claim",
        "verbatim_quote": "The results of the present investigation contribute to a fuller understanding of settlement patterns and the environmental conditions underpinning them.",
        "page": 425,
        "supporting_evidence": [],
        "confidence": "medium",
        "relevance": "Claims contribution to settlement understanding"
    },
    {
        "claim_id": "C042",
        "content": "QuickBird was the optimal choice for archaeological prospection at the time of project initiation due to its high resolution.",
        "claim_type": "methodological_justification",
        "verbatim_quote": "At the time the project was initiated, QuickBird was the highest-resolution satellite imagery commercially available",
        "page": 425,
        "supporting_evidence": ["E022"],
        "confidence": "high",
        "relevance": "Justifies imagery selection"
    },
    {
        "claim_id": "C043",
        "content": "The cost savings of archival imagery were justified by modest landscape changes over the three-year interval.",
        "claim_type": "methodological_justification",
        "verbatim_quote": "the cost savings offered by archival imagery was justified because there were only modest changes in the landscape over the three-year interval between image acquisition and the beginning of our project",
        "page": 425,
        "supporting_evidence": ["E024", "E025"],
        "confidence": "high",
        "relevance": "Justifies use of archival vs. tasked imagery"
    },
    {
        "claim_id": "C044",
        "content": "Archival imagery offers cost savings compared to newly tasked imagery.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "the cost savings offered by archival imagery",
        "page": 425,
        "supporting_evidence": ["E024"],
        "confidence": "high",
        "relevance": "Notes economic advantage of archival imagery"
    },
    {
        "claim_id": "C045",
        "content": "Early spring image acquisition optimizes the contrast between healthy and stressed vegetation for detecting archaeological remains.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "The early spring date of the image captured vigorous plant growth, increasing the contrast between healthy and stressed vegetation that can reveal archaeological remains.",
        "page": 426,
        "supporting_evidence": ["E026"],
        "confidence": "high",
        "relevance": "Explains seasonal timing strategy"
    },
    {
        "claim_id": "C046",
        "content": "Mid-March timing allows both crop mark and soil mark detection by balancing vegetation growth with ground visibility.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "At the same time, plant growth had not proceeded so far by mid-March as to entirely obscure the ground, allowing for the detection of soil marks.",
        "page": 426,
        "supporting_evidence": ["E027"],
        "confidence": "high",
        "relevance": "Explains optimal timing for dual detection"
    },
    {
        "claim_id": "C047",
        "content": "Multiple favorable acquisition factors (clear sky, environmental quality, low off-nadir angle) produced high-quality imagery with minimal distortion.",
        "claim_type": "technical_assertion",
        "verbatim_quote": "A combination of factors including clear sky, excellent environmental quality, and a low off-nadir angle combined to produce an unobstructed image with relatively little distortion.",
        "page": 426,
        "supporting_evidence": ["E028"],
        "confidence": "high",
        "relevance": "Documents image quality advantages"
    }
]

# ============================================================================
# IMPLICIT ARGUMENTS
# ============================================================================

implicit_arguments = [
    {
        "implicit_argument_id": "IA007",
        "content": "Sites with prominent locations and diverse resource zones were strategically important in antiquity (implied by emphasis on L'Amastuola's characteristics).",
        "argument_type": "unstated_premise",
        "trigger_text": "the site occupies one of the most prominent hill peaks... the settlement seems to have been selected with a view to exploiting a range of resource zones",
        "page": 424,
        "reconstruction_confidence": "high",
        "related_claims": ["C034", "C035"],
        "critical_for_logic": True,
        "notes": "Strategic site selection argument implicit in site characterization"
    },
    {
        "implicit_argument_id": "IA008",
        "content": "Areas with known dense settlement are appropriate for testing remote sensing methodology (implied by characterizing it as 'ideal test case').",
        "argument_type": "unstated_premise",
        "trigger_text": "This existing body of settlement information acquired through survey offered an ideal test case for remote sensing.",
        "page": 425,
        "reconstruction_confidence": "high",
        "related_claims": ["C040"],
        "critical_for_logic": True,
        "notes": "Methodological testing requires known ground truth"
    },
    {
        "implicit_argument_id": "IA009",
        "content": "Early spring is the optimal season for archaeological remote sensing in Mediterranean environments (implied by seasonal timing justification).",
        "argument_type": "unstated_assumption",
        "trigger_text": "The early spring date of the image captured vigorous plant growth... At the same time, plant growth had not proceeded so far by mid-March",
        "page": 426,
        "reconstruction_confidence": "medium",
        "related_claims": ["C045", "C046"],
        "critical_for_logic": False,
        "notes": "Seasonality argument based on vegetation-archaeology relationship"
    },
    {
        "implicit_argument_id": "IA010",
        "content": "Integration of multiple methods has been productive for long-term Vrije Universiteit research (implied by continuation of integrated approach).",
        "argument_type": "unstated_premise",
        "trigger_text": "From the beginning, the Vrije Universiteit fieldwork in Salento combined excavation, field survey, environmental research, and remote sensing",
        "page": 424,
        "reconstruction_confidence": "medium",
        "related_claims": ["C031"],
        "critical_for_logic": False,
        "notes": "Continuation implies past success of integrated approach"
    }
]

# ============================================================================
# UPDATE EXTRACTION FILE
# ============================================================================

data['evidence'].extend(evidence_items)
data['claims'].extend(claims_items)
data['implicit_arguments'].extend(implicit_arguments)
data['extraction_timestamp'] = datetime.now(timezone.utc).isoformat()

data['extraction_notes']['pass1_sections'].append({
    'section': 'Section 2: L\'Amastuola Project + Satellite Image Data',
    'pages': '424-426',
    'word_count_estimate': 1100,
    'items_extracted': {
        'evidence': len(evidence_items),
        'claims': len(claims_items),
        'implicit_arguments': len(implicit_arguments)
    },
    'notes': 'Liberal extraction from project context and imagery specifications. High density of evidence about site characteristics, settlement patterns, and technical specifications. Claims include methodological justifications, site significance, and seasonal timing rationale.'
})

with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print(f"✓ Pass 1, Section 2 complete: L'Amastuola Project + Satellite Image Data")
print(f"  - Evidence items: {len(evidence_items)}")
print(f"  - Claims: {len(claims_items)}")
print(f"  - Implicit arguments: {len(implicit_arguments)}")
print(f"  - Total items this section: {len(evidence_items) + len(claims_items) + len(implicit_arguments)}")
print(f"  - Running total: {len(data['evidence'])} evidence, {len(data['claims'])} claims, {len(data['implicit_arguments'])} implicit arguments")
