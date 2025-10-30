#!/usr/bin/env python3
"""
Pass 1 Section 1: Extract claims, evidence, and implicit arguments
from Abstract + Introduction (pages 1-2)

Liberal extraction philosophy: When uncertain, include it.
Mandatory sourcing: All explicit items require verbatim_quote.
All implicit arguments require trigger_text + trigger_locations + inference_reasoning.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Load current extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

# Populate project_metadata
data["schema_version"] = "2.5"
data["extraction_timestamp"] = datetime.now(timezone.utc).isoformat()
data["extractor"] = "Claude Code + research-assessor skill"
data["project_metadata"] = {
    "paper_title": "The impact of land use and depopulation on burial mounds in the Kazanlak Valley, Bulgaria: An ordered logit predictive model",
    "authors": ["Martin Eftimoski", "Shawn A. Ross", "Adela Sobotkova"],
    "publication_year": 2017,
    "journal": "Journal of Cultural Heritage",
    "doi": "10.1016/j.culher.2016.10.002",
    "paper_type": "research article",
    "discipline": "archaeology",
    "research_context": "Predictive modelling of burial mound vulnerability to anthropogenic threats using ordered logistic regression on large dataset (n=773) from Kazanlak Valley, Bulgaria"
}

# Initialize extraction_notes
data["extraction_notes"] = {
    "claims_evidence_extraction_complete": False,
    "rdmap_extraction_complete": False,
    "sections_extracted": ["Pass 1 section 1: Abstract + Introduction (pages 1-2)"],
    "known_limitations": [],
    "assessment_blockers": []
}

print("Extracting evidence from Abstract + Introduction...")

# EVIDENCE items (E001-E010)
evidence = [
    {
        "evidence_id": "E001",
        "evidence_text": "Visual condition assessments of 773 burial mounds combined with location and land use data",
        "evidence_type": "dataset_description",
        "evidence_basis": "author_assertion",
        "supports_claims": ["C001", "C006", "C007"],
        "location": {
            "section": "Abstract",
            "page": 1,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "This model yields probabilities of damage to burial mounds subject to changing conditions, based on the present condition and situation of a large dataset of mounds (n = 773), as estimated through direct visual assessment.",
        "extraction_confidence": "high"
    },
    {
        "evidence_id": "E002",
        "evidence_text": "In 2008, burial mounds comprised 57 of 257 (nearly a quarter) of all excavations in Bulgaria",
        "evidence_type": "quantitative_observation",
        "evidence_basis": "statistical_output",
        "supports_claims": ["C017", "C018", "C019"],
        "location": {
            "section": "1.1. Threats to burial mounds in Bulgaria",
            "page": 2,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "In 2008, the last year for which data is available, burial mounds comprised nearly a quarter (57 of 257) of all excavations in Bulgaria",
        "extraction_confidence": "high"
    },
    {
        "evidence_id": "E003",
        "evidence_text": "Authors inventoried over 1000 burial mounds in two Bulgarian provinces during three years of fieldwork",
        "evidence_type": "field_observation",
        "evidence_basis": "observational_record",
        "supports_claims": ["C017"],
        "location": {
            "section": "1.1. Threats to burial mounds in Bulgaria",
            "page": 2,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "The authors saw few examples mounds that had not been damaged either by development, looting, or agriculture during three years of ﬁeldwork, despite having inventoried over 1000 of them in two Bulgarian provinces.",
        "extraction_confidence": "high"
    },
    {
        "evidence_id": "E004",
        "evidence_text": "Few examples of undamaged mounds observed during three years of fieldwork despite inventorying over 1000 mounds",
        "evidence_type": "field_observation",
        "evidence_basis": "observational_record",
        "supports_claims": ["C017"],
        "location": {
            "section": "1.1. Threats to burial mounds in Bulgaria",
            "page": 2,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "The authors saw few examples mounds that had not been damaged either by development, looting, or agriculture during three years of ﬁeldwork",
        "extraction_confidence": "high"
    },
    {
        "evidence_id": "E005",
        "evidence_text": "Tundzha Regional Archaeology Project (TRAP) investigated Kazanlak Valley between 2009 and 2011",
        "evidence_type": "project_description",
        "evidence_basis": "author_assertion",
        "supports_claims": ["C024"],
        "location": {
            "section": "1.2. Study area: the Kazanlak Valley",
            "page": 2,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "The Tundzha Regional Archaeology Project (TRAP) investigated the archaeology of the Kazanlak Valley, located in the Stara Zagora province of Bulgaria, between 2009 and 2011",
        "extraction_confidence": "high"
    },
    {
        "evidence_id": "E006",
        "evidence_text": "Thracian Tomb of Kazanlak declared UNESCO World Heritage Site in 1979",
        "evidence_type": "historical_fact",
        "evidence_basis": "archival_document",
        "supports_claims": ["C24", "C026", "C027"],
        "location": {
            "section": "1.2. Study area: the Kazanlak Valley",
            "page": 2,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "The fourth-century BC 'Thracian Tomb of Kazanlak' was declared a UNESCO World Heritage Site in 1979",
        "extraction_confidence": "high"
    },
    {
        "evidence_id": "E007",
        "evidence_text": "Natural erosion rates in Kazanlak Valley are high (>0.40 mm/year) only in few areas at higher elevations; typical rates are ca. 0.17-0.22 mm/year",
        "evidence_type": "quantitative_measurement",
        "evidence_basis": "statistical_output",
        "supports_claims": ["C028", "C029", "C030"],
        "location": {
            "section": "1.2. Study area: the Kazanlak Valley",
            "page": 2,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "Natural erosion rates are high (> 0.40 mm/year) in only a few areas of the valley, mostly at higher elevations; typical rates are only ca. 0.17–0.22 mm/year",
        "extraction_confidence": "high"
    },
    {
        "evidence_id": "E008",
        "evidence_text": "Large number of small mounds (<0.5 m high) survive in Kazanlak Valley",
        "evidence_type": "field_observation",
        "evidence_basis": "observational_record",
        "supports_claims": ["C028"],
        "location": {
            "section": "1.2. Study area: the Kazanlak Valley",
            "page": 2,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "The Kazanlak Valley does not experience catastrophic natural events that destroy mounds, as attested by the large number of small mounds (< 0.5 m high) that survive.",
        "extraction_confidence": "high"
    },
    {
        "evidence_id": "E009",
        "evidence_text": "Burial mounds range in size from <10 m diameter and <0.5 m high to >50 m diameter and >20 m high",
        "evidence_type": "descriptive_observation",
        "evidence_basis": "observational_record",
        "supports_claims": ["C015", "C016"],
        "location": {
            "section": "1.1. Threats to burial mounds in Bulgaria",
            "page": 2,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "They are earthen constructions ranging in size from < 10 m diameter and < 0.5 m high, to > 50 m diameter and > 20 m high.",
        "extraction_confidence": "high"
    },
    {
        "evidence_id": "E010",
        "evidence_text": "Burial mound contents vary from nothing (cenotaphs) to simple burials to elaborate stone/brick tombs with architectural refinement and valuable burial goods",
        "evidence_type": "descriptive_observation",
        "evidence_basis": "observational_record",
        "supports_claims": ["C015", "C016"],
        "location": {
            "section": "1.1. Threats to burial mounds in Bulgaria",
            "page": 2,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Their contents vary from nothing (cenotaphs), to a simple burial with or without an enclosure, to elaborate stone or brick tombs with much architectural and artistic reﬁnement and intrinsically valuable burial goods",
        "extraction_confidence": "high"
    }
]

print(f"  Added {len(evidence)} evidence items (E001-E010)")

print("Extracting claims from Abstract + Introduction...")

# CLAIMS items (C001-C030)
claims = [
    {
        "claim_id": "C001",
        "claim_text": "Ordered logistic regression model can assess vulnerability of burial mounds to human activity",
        "claim_type": "methodological_argument",
        "claim_role": "core",
        "primary_function": "methodological_justification",
        "claim_nature": "evaluative",
        "supported_by": ["E001"],
        "supports_claims": [],
        "implicit_assumptions": ["IA001", "IA002"],
        "location": {
            "section": "Abstract",
            "page": 1,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "This article uses an ordered logistic regression (logit) model to assess the vulnerability of ancient burial mounds to human activity in the Kazanlak Valley, Bulgaria.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C002",
        "claim_text": "Changing land use (conversion of pasture to arable land) degrades burial mounds in Kazanlak Valley",
        "claim_type": "empirical",
        "claim_role": "core",
        "primary_function": "empirical_pattern",
        "claim_nature": "causal",
        "supported_by": ["E001"],
        "supports_claims": [],
        "implicit_assumptions": ["IA003"],
        "location": {
            "section": "Abstract",
            "page": 1,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "Results for the Kazanlak Valley indicate that changing land use (conversion of pasture to arable land) and depopulation or de-urbanisation (increased distance to the nearest city, town, or village) represent two anthropogenic factors that degrade burial mounds.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C003",
        "claim_text": "Depopulation/de-urbanisation (increased distance to urban areas) degrades burial mounds in Kazanlak Valley",
        "claim_type": "empirical",
        "claim_role": "core",
        "primary_function": "empirical_pattern",
        "claim_nature": "causal",
        "supported_by": ["E001"],
        "supports_claims": [],
        "implicit_assumptions": ["IA004", "IA005"],
        "location": {
            "section": "Abstract",
            "page": 1,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "Results for the Kazanlak Valley indicate that changing land use (conversion of pasture to arable land) and depopulation or de-urbanisation (increased distance to the nearest city, town, or village) represent two anthropogenic factors that degrade burial mounds.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C004",
        "claim_text": "Land use factor likely represents threat from ploughing related to annual agriculture",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "primary_function": "mechanism_proposal",
        "claim_nature": "causal",
        "supported_by": [],
        "supports_claims": ["C002"],
        "implicit_assumptions": [],
        "location": {
            "section": "Abstract",
            "page": 1,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "These factors likely represent threats from ploughing related to annual agriculture",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C005",
        "claim_text": "Proximity factor likely represents looting threat fostered by decreased scrutiny associated with remoteness",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "primary_function": "mechanism_proposal",
        "claim_nature": "causal",
        "supported_by": [],
        "supports_claims": ["C003"],
        "implicit_assumptions": ["IA004"],
        "location": {
            "section": "Abstract",
            "page": 1,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "and looting fostered by the decreased scrutiny associated with remoteness",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C006",
        "claim_text": "This approach allows cultural heritage personnel to predict mound vulnerability response to changing circumstances and direct resources to most vulnerable monuments",
        "claim_type": "methodological_argument",
        "claim_role": "core",
        "primary_function": "methodological_justification",
        "claim_nature": "evaluative",
        "supported_by": ["E001"],
        "supports_claims": [],
        "implicit_assumptions": [],
        "location": {
            "section": "Abstract",
            "page": 1,
            "start_paragraph": 3,
            "end_paragraph": 3
        },
        "verbatim_quote": "After an initial survey to acquire the requisite data, local cultural heritage personnel can use this approach to predict quickly and continuously how mound vulnerability will respond to changing circumstances, and then direct resources to the most vulnerable monuments.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C007",
        "claim_text": "This approach quantifies probable impact of changing circumstances on monuments without relying on site location models, prior knowledge of specific hazards, or forecasts of future development",
        "claim_type": "methodological_argument",
        "claim_role": "core",
        "primary_function": "methodological_justification",
        "claim_nature": "comparative",
        "supported_by": ["E001"],
        "supports_claims": [],
        "implicit_assumptions": [],
        "location": {
            "section": "Abstract",
            "page": 1,
            "start_paragraph": 3,
            "end_paragraph": 3
        },
        "verbatim_quote": "Unlike typical predictive modelling for cultural heritage management, use of a logit regression on a large dataset quantiﬁes the probable impact of changing circumstances on monuments without relying on site location models, prior knowledge of speciﬁc hazards, or forecasts of future development.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C008",
        "claim_text": "This approach can be applied widely wherever sufficient observational data are available",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "primary_function": "methodological_justification",
        "claim_nature": "evaluative",
        "supported_by": [],
        "supports_claims": ["C006", "C007"],
        "implicit_assumptions": [],
        "location": {
            "section": "Abstract",
            "page": 1,
            "start_paragraph": 3,
            "end_paragraph": 3
        },
        "verbatim_quote": "This approach can be applied widely, wherever sufﬁcient observational data are available.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C009",
        "claim_text": "Agriculture is not wholly benign to cultural heritage",
        "claim_type": "interpretation",
        "claim_role": "core",
        "primary_function": "theoretical_interpretation",
        "claim_nature": "evaluative",
        "supported_by": [],
        "supports_claims": [],
        "implicit_assumptions": ["IA006"],
        "location": {
            "section": "Abstract",
            "page": 1,
            "start_paragraph": 3,
            "end_paragraph": 3
        },
        "verbatim_quote": "Our results also provide a reminder that agriculture is not wholly benign",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C010",
        "claim_text": "Depopulation, not just urban sprawl, can threaten cultural heritage",
        "claim_type": "interpretation",
        "claim_role": "core",
        "primary_function": "theoretical_interpretation",
        "claim_nature": "evaluative",
        "supported_by": [],
        "supports_claims": [],
        "implicit_assumptions": [],
        "location": {
            "section": "Abstract",
            "page": 1,
            "start_paragraph": 3,
            "end_paragraph": 3
        },
        "verbatim_quote": "and that depopulation – not just urban sprawl – can threaten cultural heritage.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C011",
        "claim_text": "Two factors predict mound vulnerability: land use and proximity to urban boundary",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "primary_function": "empirical_pattern",
        "claim_nature": "correlational",
        "supported_by": [],
        "supports_claims": ["C002", "C003"],
        "implicit_assumptions": [],
        "location": {
            "section": "1. Introduction",
            "page": 1,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Two factors in particular predict mound vulnerability: land use and proximity to an urban boundary.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C012",
        "claim_text": "Conversion from pasture to annual agriculture increases likelihood of damage to mounds",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "primary_function": "empirical_pattern",
        "claim_nature": "causal",
        "supported_by": [],
        "supports_claims": ["C002"],
        "implicit_assumptions": [],
        "location": {
            "section": "1. Introduction",
            "page": 1,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Predictions of the model regarding changes to land use were therefore unsurprising; conversion from pasture to annual agriculture increases the likelihood of damage.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C013",
        "claim_text": "Mounds further from urban boundaries are more likely to be damaged",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "primary_function": "empirical_pattern",
        "claim_nature": "correlational",
        "supported_by": [],
        "supports_claims": ["C003"],
        "implicit_assumptions": [],
        "location": {
            "section": "1. Introduction",
            "page": 1,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "The effects of proximity to an urban boundary, however, proved counterintuitive; mounds further from such a boundary are more likely to be damaged.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C014",
        "claim_text": "Degradation associated with remoteness reveals that de-urbanisation and regional depopulation, not only urban sprawl, threatens cultural heritage, a finding relevant to Eastern Europe, former Soviet Union, and elsewhere where cities are shrinking",
        "claim_type": "interpretation",
        "claim_role": "core",
        "primary_function": "theoretical_interpretation",
        "claim_nature": "evaluative",
        "supported_by": [],
        "supports_claims": ["C010"],
        "implicit_assumptions": [],
        "location": {
            "section": "1. Introduction",
            "page": 1,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Degradation associated with remoteness reveals that de-urbanisation and regional depopulation, and not only urban sprawl, threatens cultural heritage, a ﬁnding relevant to much of Eastern Europe, the former Soviet Union, and elsewhere where cities are shrinking or villages are being abandoned.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C015",
        "claim_text": "Ancient burial mounds are ubiquitous feature of Bulgarian cultural landscape",
        "claim_type": "empirical",
        "claim_role": "supporting",
        "primary_function": "empirical_pattern",
        "claim_nature": "descriptive",
        "supported_by": ["E009", "E010"],
        "supports_claims": [],
        "implicit_assumptions": [],
        "location": {
            "section": "1.1. Threats to burial mounds in Bulgaria",
            "page": 2,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Ancient burial mounds are a ubiquitous feature of the Bulgarian cultural landscape",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C016",
        "claim_text": "Thousands of burial mounds were built from Early Bronze Age through Middle Ages in western extensions of Asian steppes and surrounding areas including Kazanlak Valley",
        "claim_type": "empirical",
        "claim_role": "supporting",
        "primary_function": "empirical_pattern",
        "claim_nature": "descriptive",
        "supported_by": ["E009", "E010"],
        "supports_claims": ["C015"],
        "implicit_assumptions": [],
        "location": {
            "section": "1.1. Threats to burial mounds in Bulgaria",
            "page": 2,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Thousands of such mounds were built from the Early Bronze Age through the Middle Ages in the western extensions of the Asian steppes and surrounding areas, including the Kazanlak Valley.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C017",
        "claim_text": "Burial mounds are an endangered class of monument in Bulgaria",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "primary_function": "empirical_pattern",
        "claim_nature": "evaluative",
        "supported_by": ["E002", "E003", "E004"],
        "supports_claims": [],
        "implicit_assumptions": [],
        "location": {
            "section": "1.1. Threats to burial mounds in Bulgaria",
            "page": 2,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "Despite the number of burial mounds, they are an endangered class of monument.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C018",
        "claim_text": "Development in Bulgaria destroys dozens of mounds annually",
        "claim_type": "empirical",
        "claim_role": "supporting",
        "primary_function": "empirical_pattern",
        "claim_nature": "descriptive",
        "supported_by": ["E002"],
        "supports_claims": ["C017"],
        "implicit_assumptions": [],
        "location": {
            "section": "1.1. Threats to burial mounds in Bulgaria",
            "page": 2,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "Development in Bulgaria destroys dozens of mounds annually.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C019",
        "claim_text": "Most known and regulated destructions result from formal rescue excavation in anticipation of housing or infrastructure construction",
        "claim_type": "empirical",
        "claim_role": "supporting",
        "primary_function": "empirical_pattern",
        "claim_nature": "descriptive",
        "supported_by": ["E002"],
        "supports_claims": ["C018"],
        "implicit_assumptions": [],
        "location": {
            "section": "1.1. Threats to burial mounds in Bulgaria",
            "page": 2,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "Most known and regulated destructions result from formal rescue excavation in anticipation of housing or infrastructure construction.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C020",
        "claim_text": "Looting probably still compromises more mounds than development",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "primary_function": "comparative_assessment",
        "claim_nature": "comparative",
        "supported_by": [],
        "supports_claims": ["C017"],
        "implicit_assumptions": [],
        "location": {
            "section": "1.1. Threats to burial mounds in Bulgaria",
            "page": 2,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "Despite administrative and legal measures to combat illicit artefact trafﬁcking, such as a 2013 Memorandum of Understanding with the United States, looting probably still compromises more mounds that development",
        "extraction_confidence": "medium",
        "extraction_notes": "Typo in source: 'that' should be 'than'"
    },
    {
        "claim_id": "C021",
        "claim_text": "Burial landscapes suffer slow and continuous wear from agricultural activities",
        "claim_type": "empirical",
        "claim_role": "supporting",
        "primary_function": "empirical_pattern",
        "claim_nature": "descriptive",
        "supported_by": [],
        "supports_claims": ["C017"],
        "implicit_assumptions": [],
        "location": {
            "section": "1.1. Threats to burial mounds in Bulgaria",
            "page": 2,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "Burial landscapes also suffer slow and continuous wear from agricultural activities",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C022",
        "claim_text": "Farmers plough and harrow arable fields annually, potentially affecting thousands of mounds across Bulgaria",
        "claim_type": "empirical",
        "claim_role": "supporting",
        "primary_function": "empirical_pattern",
        "claim_nature": "descriptive",
        "supported_by": [],
        "supports_claims": ["C021"],
        "implicit_assumptions": [],
        "location": {
            "section": "1.1. Threats to burial mounds in Bulgaria",
            "page": 2,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "Farmers plough and harrow arable ﬁelds annually, potentially affecting thousands of mounds across Bulgaria.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C023",
        "claim_text": "Unlike looting and development, gradual damage from agriculture generally goes unremarked",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "primary_function": "comparative_assessment",
        "claim_nature": "comparative",
        "supported_by": [],
        "supports_claims": ["C021"],
        "implicit_assumptions": [],
        "location": {
            "section": "1.1. Threats to burial mounds in Bulgaria",
            "page": 2,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "Unlike looting (and to a lesser extent development), which captures public attention, gradual damage from agriculture generally goes unremarked.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C024",
        "claim_text": "Kazanlak Valley hosts a rich and varied archaeological record dating from Neolithic through Ottoman times",
        "claim_type": "empirical",
        "claim_role": "supporting",
        "primary_function": "empirical_pattern",
        "claim_nature": "descriptive",
        "supported_by": ["E005"],
        "supports_claims": [],
        "implicit_assumptions": [],
        "location": {
            "section": "1.2. Study area: the Kazanlak Valley",
            "page": 2,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "The Kazanlak Valley, promoted as the 'Valley of the Thracian Kings', hosts a rich and varied archaeological record dating from the Neolithic through Ottoman times",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C025",
        "claim_text": "Burial mounds are the most recognisable feature of Kazanlak Valley archaeology",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "primary_function": "empirical_pattern",
        "claim_nature": "evaluative",
        "supported_by": [],
        "supports_claims": [],
        "implicit_assumptions": [],
        "location": {
            "section": "1.2. Study area: the Kazanlak Valley",
            "page": 2,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "but burial mounds are its most recognisable feature",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C026",
        "claim_text": "Thracian tombs attract crowds of tourists to Kazanlak Valley",
        "claim_type": "empirical",
        "claim_role": "supporting",
        "primary_function": "empirical_pattern",
        "claim_nature": "descriptive",
        "supported_by": ["E006"],
        "supports_claims": [],
        "implicit_assumptions": [],
        "location": {
            "section": "1.2. Study area: the Kazanlak Valley",
            "page": 2,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "and, alongside the tomb of the Thracian King Seuthes II excavated at Golyama Kosmatka in 2004, attracts crowds of tourists to the valley.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C027",
        "claim_text": "Decorated burial chambers and rich finds foster archaeological research and cultural tourism in Kazanlak Valley",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "primary_function": "causal_explanation",
        "claim_nature": "causal",
        "supported_by": ["E006"],
        "supports_claims": ["C026"],
        "implicit_assumptions": [],
        "location": {
            "section": "1.2. Study area: the Kazanlak Valley",
            "page": 2,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Decorated burial chambers and rich ﬁnds from tombs like these foster archaeological research and cultural tourism in the Kazanlak Valley.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C028",
        "claim_text": "Kazanlak Valley does not experience catastrophic natural events that destroy mounds",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "primary_function": "empirical_pattern",
        "claim_nature": "descriptive",
        "supported_by": ["E007", "E008"],
        "supports_claims": ["C030"],
        "implicit_assumptions": [],
        "location": {
            "section": "1.2. Study area: the Kazanlak Valley",
            "page": 2,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "The Kazanlak Valley does not experience catastrophic natural events that destroy mounds, as attested by the large number of small mounds (< 0.5 m high) that survive.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C029",
        "claim_text": "Erosion of mounds is retarded by use of fieldstones in construction",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "primary_function": "causal_explanation",
        "claim_nature": "causal",
        "supported_by": ["E007"],
        "supports_claims": ["C028"],
        "implicit_assumptions": [],
        "location": {
            "section": "1.2. Study area: the Kazanlak Valley",
            "page": 2,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "and erosion of mounds is retarded by the use of ﬁeldstones in their construction.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C030",
        "claim_text": "People cause most of the damage to mounds in Kazanlak",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "primary_function": "causal_explanation",
        "claim_nature": "causal",
        "supported_by": ["E007"],
        "supports_claims": [],
        "implicit_assumptions": [],
        "location": {
            "section": "1.2. Study area: the Kazanlak Valley",
            "page": 2,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "Consequently, people cause most of the damage to mounds in Kazanlak, as elsewhere in Bulgaria.",
        "extraction_confidence": "high"
    }
]

print(f"  Added {len(claims)} claims (C001-C030)")

print("Extracting implicit arguments from core claims...")

# IMPLICIT ARGUMENTS (IA001-IA006)
implicit_arguments = [
    {
        "implicit_id": "IA001",
        "implicit_text": "Visual condition assessments accurately represent actual mound deterioration",
        "type": "unstated_assumption",
        "connects_evidence": ["E001"],
        "enables_claim": ["C001"],
        "reasoning": "The model's validity depends on visual assessments accurately capturing true mound condition, but no validation against ground truth or inter-rater reliability is mentioned in this section",
        "verbatim_quote": None,
        "trigger_text": [
            "based on the present condition and situation of a large dataset of mounds (n = 773), as estimated through direct visual assessment"
        ],
        "trigger_locations": [
            {
                "section": "Abstract",
                "subsection": None,
                "start_paragraph": 1,
                "end_paragraph": 1
            }
        ],
        "inference_reasoning": "The paper uses visual assessments as the basis for the predictive model without discussing accuracy or reliability of visual assessment method. This assumes visual assessment is an adequate measure of actual condition, which is a prerequisite assumption for the model's validity.",
        "extraction_confidence": "high",
        "location": {
            "section": "Abstract",
            "page": 1,
            "start_paragraph": 1,
            "end_paragraph": 1
        }
    },
    {
        "implicit_id": "IA002",
        "implicit_text": "Current relationships between circumstances and mound condition will persist into future",
        "type": "unstated_assumption",
        "connects_evidence": ["E001"],
        "enables_claim": ["C001", "C006"],
        "reasoning": "Predictive use of the model assumes temporal stability of relationships between predictors (land use, proximity) and outcomes (damage), but this assumption is not explicitly stated or tested",
        "verbatim_quote": None,
        "trigger_text": [
            "yields probabilities of damage to burial mounds subject to changing conditions",
            "predict quickly and continuously how mound vulnerability will respond to changing circumstances"
        ],
        "trigger_locations": [
            {
                "section": "Abstract",
                "subsection": None,
                "start_paragraph": 1,
                "end_paragraph": 1
            },
            {
                "section": "Abstract",
                "subsection": None,
                "start_paragraph": 3,
                "end_paragraph": 3
            }
        ],
        "inference_reasoning": "The model is presented as predictive tool for future vulnerability, but this assumes the current correlations between land use/proximity and damage will remain stable over time. No discussion of temporal validation or stability is provided in this section.",
        "extraction_confidence": "high",
        "location": {
            "section": "Abstract",
            "page": 1,
            "start_paragraph": 1,
            "end_paragraph": 3
        }
    },
    {
        "implicit_id": "IA003",
        "implicit_text": "Observed correlations between land use and mound condition represent causal relationships",
        "type": "bridging_claim",
        "connects_evidence": ["E001"],
        "enables_claim": ["C002"],
        "reasoning": "The paper states that land use changes 'degrade' mounds, implying causation, but this section does not explain how correlation was distinguished from causation (e.g., through temporal ordering, controlled comparison, or mechanism testing)",
        "verbatim_quote": None,
        "trigger_text": [
            "Results for the Kazanlak Valley indicate that changing land use (conversion of pasture to arable land) and depopulation or de-urbanisation (increased distance to the nearest city, town, or village) represent two anthropogenic factors that degrade burial mounds."
        ],
        "trigger_locations": [
            {
                "section": "Abstract",
                "subsection": None,
                "start_paragraph": 2,
                "end_paragraph": 2
            }
        ],
        "inference_reasoning": "The use of causal language ('degrade', 'represent...factors that') implies the authors are making a causal claim, not just a correlational one. However, the logical steps from observing correlation to inferring causation are not made explicit in this section.",
        "extraction_confidence": "high",
        "location": {
            "section": "Abstract",
            "page": 1,
            "start_paragraph": 2,
            "end_paragraph": 2
        }
    },
    {
        "implicit_id": "IA004",
        "implicit_text": "Remoteness from settlements reduces protective surveillance of mounds",
        "type": "logical_implication",
        "connects_evidence": [],
        "enables_claim": ["C003", "C005"],
        "reasoning": "The mechanism explanation implies that proximity to settlements provides surveillance that deters looting, but this protective mechanism is stated as fact rather than empirically demonstrated",
        "verbatim_quote": None,
        "trigger_text": [
            "looting fostered by the decreased scrutiny associated with remoteness"
        ],
        "trigger_locations": [
            {
                "section": "Abstract",
                "subsection": None,
                "start_paragraph": 2,
                "end_paragraph": 2
            }
        ],
        "inference_reasoning": "The phrase 'decreased scrutiny associated with remoteness' implies that remoteness → less scrutiny → more looting. The intermediate step (less scrutiny) is stated but the causal chain (remoteness causes less scrutiny which enables looting) is presented as self-evident rather than demonstrated.",
        "extraction_confidence": "high",
        "location": {
            "section": "Abstract",
            "page": 1,
            "start_paragraph": 2,
            "end_paragraph": 2
        }
    },
    {
        "implicit_id": "IA005",
        "implicit_text": "Prior expectation that proximity to urban areas poses risk to mounds through peri-urban processes",
        "type": "unstated_assumption",
        "connects_evidence": [],
        "enables_claim": ["C003"],
        "reasoning": "The characterization of remoteness-damage finding as 'counterintuitive' reveals prior assumption that urban proximity endangers monuments through peri-urban processes, an assumption apparently shared by researchers and local personnel but not empirically grounded in this section",
        "verbatim_quote": None,
        "trigger_text": [
            "we and our colleagues believed that proximity to a city, town, or village would also represent a risk, since it would expose mounds to a nexus of complex and destructive peri-urban processes",
            "The effects of proximity to an urban boundary, however, proved counterintuitive"
        ],
        "trigger_locations": [
            {
                "section": "1. Introduction",
                "subsection": None,
                "start_paragraph": 1,
                "end_paragraph": 1
            }
        ],
        "inference_reasoning": "The explicit statement that the finding was 'counterintuitive' and contradicted researchers' and colleagues' expectations reveals an unstated prior assumption. This assumption (urban proximity = threat) apparently shaped research expectations but is not presented as empirically derived.",
        "extraction_confidence": "high",
        "location": {
            "section": "1. Introduction",
            "page": 1,
            "start_paragraph": 1,
            "end_paragraph": 1
        }
    },
    {
        "implicit_id": "IA006",
        "implicit_text": "Agriculture is widely perceived as benign to cultural heritage",
        "type": "unstated_assumption",
        "connects_evidence": [],
        "enables_claim": ["C009"],
        "reasoning": "The framing as 'reminder' implies agriculture's threat to heritage is known but overlooked, suggesting a gap between knowledge and perception that motivates stating this 'reminder'",
        "verbatim_quote": None,
        "trigger_text": [
            "Our results also provide a reminder that agriculture is not wholly benign"
        ],
        "trigger_locations": [
            {
                "section": "Abstract",
                "subsection": None,
                "start_paragraph": 3,
                "end_paragraph": 3
            }
        ],
        "inference_reasoning": "The word 'reminder' implies this is information that was previously known but has been forgotten or is not widely appreciated. This suggests an assumption that agriculture is generally perceived as benign or neutral, making it necessary to 'remind' readers of its threats.",
        "extraction_confidence": "medium",
        "location": {
            "section": "Abstract",
            "page": 1,
            "start_paragraph": 3,
            "end_paragraph": 3
        }
    }
]

print(f"  Added {len(implicit_arguments)} implicit arguments (IA001-IA006)")

# Add arrays to data
data["evidence"] = evidence
data["claims"] = claims
data["implicit_arguments"] = implicit_arguments

# Save updated extraction
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print(f"\n✓ Section 1 extraction complete")
print(f"  - {len(evidence)} evidence items")
print(f"  - {len(claims)} claims")
print(f"  - {len(implicit_arguments)} implicit arguments")
print(f"✓ Saved to extraction.json")
