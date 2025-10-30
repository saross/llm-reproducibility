#!/usr/bin/env python3
"""
Pass 1, Section 1: Liberal Claims/Evidence Extraction
Ross et al. 2009 - Remote Sensing and Archaeological Prospection in Apulia, Italy

Section: Abstract + Introduction (~1200 words, pages 423-424)

Approach: Liberal extraction, cast wide net, aim for over-extraction.
Items will be consolidated in Pass 2. When uncertain, include it.

Extraction focus:
- Evidence: Quantitative results, measurements, observations
- Claims: Methodological assertions, comparative statements, interpretations
- Implicit arguments: 4-type scan on core claims

Sourcing discipline: 100% verbatim_quote for all explicit items
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Load current extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

# ============================================================================
# EVIDENCE - Liberal extraction of empirical observations and results
# ============================================================================

evidence_items = [
    {
        "evidence_id": "E001",
        "content": "The study analyzed approximately 100 square kilometres of QuickBird satellite imagery centered on L'Amastuola, Italy, in 2007 and 2008.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "In 2007 and 2008, we analyzed ca. 100 sq km of imagery centered on L'Amastuola, Italy.",
        "page": 423,
        "relevance": "Defines scope and scale of the remote sensing study area",
        "supports_claims": ["C001", "C002"]
    },
    {
        "evidence_id": "E002",
        "content": "Ground control combined with high-resolution multispectral imagery evaluation led to the discovery of 29 sites and significant off-site scatters during approximately four weeks of fieldwork.",
        "evidence_type": "quantitative_observation",
        "verbatim_quote": "Combining the evaluation of high-resolution multispectral imagery with concurrent ground control led to the discovery of 29 sites and significant off-site scatters during about four weeks of fieldwork.",
        "page": 423,
        "relevance": "Key quantitative result showing discovery rate and efficiency",
        "supports_claims": ["C003", "C004", "C005"]
    },
    {
        "evidence_id": "E003",
        "content": "Most detected features in the satellite image reflect geological conditions amenable to past human habitation rather than subsurface archaeological remains.",
        "evidence_type": "qualitative_observation",
        "verbatim_quote": "Our analysis indicates that most of the detected features reflect geological conditions amenable to past human habitation rather than subsurface archaeological remains.",
        "page": 423,
        "relevance": "Critical finding about nature of image features detected",
        "supports_claims": ["C006", "C007"]
    },
    {
        "evidence_id": "E004",
        "content": "The Murge Tableland Survey (MTS) conducted systematic archaeological surface survey between 2003 and 2007 in a transect across the Salento Isthmus, including 10 square kilometres within the study area.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Earlier fieldwork by the Murge Tableland Survey (MTS) provided independent definitions for various types of sites and a large sample of sites and off-site scatters in the study area.",
        "page": 423,
        "relevance": "Establishes comparative dataset for evaluating remote sensing results",
        "supports_claims": ["C008", "C009"]
    },
    {
        "evidence_id": "E005",
        "content": "The success rate of remote sensing-guided site discovery was too high to be explained by random association when compared with MTS results.",
        "evidence_type": "comparative_observation",
        "verbatim_quote": "Comparison of our remote-sensing–guided efforts with the results of that survey suggests that our success rate is too high to be explained by random association",
        "page": 423,
        "relevance": "Key finding demonstrating effectiveness of remote sensing approach",
        "supports_claims": ["C010", "C011"]
    },
    {
        "evidence_id": "E006",
        "content": "Until recently, high-resolution multispectral imagery such as QuickBird has been used to analyze only relatively small areas.",
        "evidence_type": "literature_observation",
        "verbatim_quote": "Until recently, high-resolution multispectral imagery, such as QuickBird, has been used to analyze only relatively small areas (Lasaponara and Masini 2007; Masini and Lasaponara 2006: 536-537).",
        "page": 423,
        "relevance": "Establishes previous limitations in scale of high-resolution imagery applications",
        "supports_claims": ["C012", "C013"]
    },
    {
        "evidence_id": "E007",
        "content": "Larger areas have been investigated using multispectral but low-resolution imagery like Landsat, or medium- to high-resolution but panchromatic imagery like CORONA.",
        "evidence_type": "literature_observation",
        "verbatim_quote": "Larger areas have been investigated using multispectral but low-resolution imagery such as Landsat or medium- to high-resolution but panchromatic imagery like CORONA (Fowler 1996; Harrower, McCorriston, and Oches 2002; Philip et al. 2002; Wilkinson, Ur, and Casana 2004; Casana and Cothren 2008).",
        "page": 423,
        "relevance": "Documents alternative imagery types used for larger-scale studies",
        "supports_claims": ["C014", "C015"]
    },
    {
        "evidence_id": "E008",
        "content": "Few projects have combined satellite image analysis with field survey to evaluate the numbers of sites discovered with each method.",
        "evidence_type": "literature_gap",
        "verbatim_quote": "Few projects have combined satellite image analysis with field survey to evaluate the numbers of sites discovered with each method, a task necessary in order to determine the utility of satellite imagery for landscape archaeology.",
        "page": 423,
        "relevance": "Identifies methodological gap this study addresses",
        "supports_claims": ["C016", "C017"]
    },
    {
        "evidence_id": "E009",
        "content": "Madry's 2007 paper on QuickBird imagery exemplifies a trend where identified sites are never confirmed through ground control or compared with field survey results.",
        "evidence_type": "literature_observation",
        "verbatim_quote": "Madry's paper (2007) on the use of QuickBird imagery exemplifies this trend, where identified sites are never confirmed through ground control or compared with the results of field survey.",
        "page": 423,
        "relevance": "Illustrates specific methodological shortcoming in existing remote sensing studies",
        "supports_claims": ["C018", "C019"]
    }
]

# ============================================================================
# CLAIMS - Liberal extraction of interpretations, assertions, arguments
# ============================================================================

claims_items = [
    {
        "claim_id": "C001",
        "content": "When deployed in combination with ground control, archaeological surface survey, and environmental research, remote sensing based upon high-resolution multispectral satellite imagery allows large areas to be evaluated efficiently by a small team of researchers.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "When deployed in combination with ground control, archaeological surface survey, and environmental research, remote sensing based upon high-resolution multispectral satellite imagery allows large areas to be evaluated efficiently by a small team of researchers",
        "page": 423,
        "supporting_evidence": ["E001", "E002"],
        "confidence": "high",
        "relevance": "Core methodological claim about efficiency of integrated approach"
    },
    {
        "claim_id": "C002",
        "content": "Remote sensing contributes to a better understanding of an archaeological landscape.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "and contributes to a better understanding of an archaeological landscape.",
        "page": 423,
        "supporting_evidence": ["E001", "E002"],
        "confidence": "medium",
        "relevance": "General claim about value of remote sensing for landscape archaeology"
    },
    {
        "claim_id": "C003",
        "content": "Remote sensing combined with ground control can discover significant numbers of sites and off-site scatters in a relatively short fieldwork period.",
        "claim_type": "effectiveness_claim",
        "verbatim_quote": "Combining the evaluation of high-resolution multispectral imagery with concurrent ground control led to the discovery of 29 sites and significant off-site scatters during about four weeks of fieldwork.",
        "page": 423,
        "supporting_evidence": ["E002"],
        "confidence": "high",
        "relevance": "Demonstrates practical efficiency of the method"
    },
    {
        "claim_id": "C004",
        "content": "The iterative process of image analysis and ground control led to the discovery of previously unknown sites.",
        "claim_type": "effectiveness_claim",
        "verbatim_quote": "The process, built around iterative image analysis and ground control, led to the discovery of previously unknown sites",
        "page": 424,
        "supporting_evidence": ["E002"],
        "confidence": "high",
        "relevance": "Emphasizes discovery value of the methodology"
    },
    {
        "claim_id": "C005",
        "content": "Image analysis was supplemented and extended by ground control and geological investigation to improve accuracy and efficiency of site detection.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Image analysis was supplemented and extended by ground control and geological investigation to improve the accuracy and efficiency of site detection",
        "page": 424,
        "supporting_evidence": ["E002"],
        "confidence": "high",
        "relevance": "Explains how ground control improves image analysis"
    },
    {
        "claim_id": "C006",
        "content": "Most features detected in satellite imagery reflect geological conditions amenable to habitation rather than direct evidence of subsurface archaeological remains.",
        "claim_type": "interpretive_claim",
        "verbatim_quote": "Our analysis indicates that most of the detected features reflect geological conditions amenable to past human habitation rather than subsurface archaeological remains.",
        "page": 423,
        "supporting_evidence": ["E003"],
        "confidence": "high",
        "relevance": "Critical interpretation about what image features represent"
    },
    {
        "claim_id": "C007",
        "content": "Ground control and geological investigation are necessary to determine the nature of the relationship between features visible in imagery and archaeological evidence found in the field.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "as well as to determine the nature of the relationship between the features visible in the image and archaeological evidence found in the field.",
        "page": 424,
        "supporting_evidence": ["E003"],
        "confidence": "high",
        "relevance": "Emphasizes necessity of ground-truthing"
    },
    {
        "claim_id": "C008",
        "content": "The Murge Tableland Survey provides independent definitions for various types of sites and a large comparative sample.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Earlier fieldwork by the Murge Tableland Survey (MTS) provided independent definitions for various types of sites and a large sample of sites and off-site scatters in the study area.",
        "page": 423,
        "supporting_evidence": ["E004"],
        "confidence": "high",
        "relevance": "Establishes validity of comparative dataset"
    },
    {
        "claim_id": "C009",
        "content": "Comparison with MTS results allows assessment of relative utility of both approaches in extensive regional investigation.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Here, we assess the relative utility of both approaches in an extensive regional investigation, indicating how surface survey and satellite image analysis profitably complement one another.",
        "page": 424,
        "supporting_evidence": ["E004"],
        "confidence": "high",
        "relevance": "Establishes purpose of comparative analysis"
    },
    {
        "claim_id": "C010",
        "content": "The success rate of remote sensing-guided discovery is too high to be explained by random association.",
        "claim_type": "effectiveness_claim",
        "verbatim_quote": "Comparison of our remote-sensing–guided efforts with the results of that survey suggests that our success rate is too high to be explained by random association",
        "page": 423,
        "supporting_evidence": ["E005"],
        "confidence": "high",
        "relevance": "Demonstrates statistical significance of results"
    },
    {
        "claim_id": "C011",
        "content": "Comparison with surface survey results illuminates the strengths and weaknesses of respective methods.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "and also illuminates the strengths and weaknesses of the respective methods",
        "page": 423,
        "supporting_evidence": ["E005"],
        "confidence": "high",
        "relevance": "Establishes value of comparative methodology"
    },
    {
        "claim_id": "C012",
        "content": "There is a need to integrate satellite image analysis with ground control and surface survey.",
        "claim_type": "methodological_recommendation",
        "verbatim_quote": "underscoring the need to integrate satellite image analysis with ground control and surface survey.",
        "page": 423,
        "supporting_evidence": ["E005"],
        "confidence": "high",
        "relevance": "Key methodological recommendation from the study"
    },
    {
        "claim_id": "C013",
        "content": "High-resolution multispectral imagery has historically been limited to analyzing relatively small areas.",
        "claim_type": "historical_claim",
        "verbatim_quote": "Until recently, high-resolution multispectral imagery, such as QuickBird, has been used to analyze only relatively small areas",
        "page": 423,
        "supporting_evidence": ["E006"],
        "confidence": "high",
        "relevance": "Establishes historical limitation this study addresses"
    },
    {
        "claim_id": "C014",
        "content": "Lower-resolution imagery is useful for producing base maps and studying large-scale environmental and geological phenomena.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Lower-resolution imagery is useful for producing base maps and studying large-scale environmental and geological phenomena",
        "page": 423,
        "supporting_evidence": ["E007"],
        "confidence": "high",
        "relevance": "Explains capabilities of alternative imagery types"
    },
    {
        "claim_id": "C015",
        "content": "Higher-resolution panchromatic imagery can detect prominent archaeological sites such as tells.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "while higher-resolution panchromatic imagery can detect prominent archaeological sites such as tells.",
        "page": 423,
        "supporting_evidence": ["E007"],
        "confidence": "high",
        "relevance": "Describes capabilities of panchromatic imagery"
    },
    {
        "claim_id": "C016",
        "content": "Only high-resolution multispectral imagery reveals the relatively small soil marks, crop marks, and shadow marks often associated with subsurface archaeological remains.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Only high-resolution multispectral imagery reveals the relatively small soil marks, crop marks, and shadow marks often associated with subsurface archaeological remains.",
        "page": 423,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Core claim about unique capabilities of high-resolution multispectral imagery"
    },
    {
        "claim_id": "C017",
        "content": "Use of high-resolution multispectral imagery allows for the detection of smaller sites and for efficient investigation and management of large, archaeologically rich landscapes.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Use of high-resolution multispectral imagery allows for the detection of smaller sites, and for the efficient investigation and management of large, archaeologically rich landscapes (Madry 2007).",
        "page": 423,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Claims specific advantages of high-resolution multispectral approach"
    },
    {
        "claim_id": "C018",
        "content": "The use of high-resolution multispectral imagery as a primary means of archaeological prospection is methodologically underdeveloped.",
        "claim_type": "methodological_critique",
        "verbatim_quote": "The use of high-resolution multispectral imagery as a primary means of archaeological prospection is methodologically underdeveloped",
        "page": 423,
        "supporting_evidence": ["E008"],
        "confidence": "high",
        "relevance": "Identifies gap in current methodological development"
    },
    {
        "claim_id": "C019",
        "content": "An assessment of the utility of all types of imagery remains a pressing need.",
        "claim_type": "methodological_recommendation",
        "verbatim_quote": "and an assessment of the utility of all types of imagery remains a pressing need (Kantner 2008).",
        "page": 423,
        "supporting_evidence": ["E008"],
        "confidence": "high",
        "relevance": "Identifies research need this study addresses"
    },
    {
        "claim_id": "C020",
        "content": "Evaluating numbers of sites discovered with satellite analysis versus field survey is necessary to determine the utility of satellite imagery for landscape archaeology.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Few projects have combined satellite image analysis with field survey to evaluate the numbers of sites discovered with each method, a task necessary in order to determine the utility of satellite imagery for landscape archaeology.",
        "page": 423,
        "supporting_evidence": ["E008"],
        "confidence": "high",
        "relevance": "Establishes rationale for comparative approach"
    },
    {
        "claim_id": "C021",
        "content": "Rates of recovery need to be related to sensor type and resolution, accounting for different environments and various types of archaeological remains.",
        "claim_type": "methodological_recommendation",
        "verbatim_quote": "Rates of recovery also need to be related to sensor type and resolution, accounting for different environments and various types of archaeological remains.",
        "page": 423,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Identifies methodological requirement for assessing imagery utility"
    },
    {
        "claim_id": "C022",
        "content": "Many existing remote sensing studies fail to confirm identified sites through ground control or compare them with field survey results.",
        "claim_type": "methodological_critique",
        "verbatim_quote": "Madry's paper (2007) on the use of QuickBird imagery exemplifies this trend, where identified sites are never confirmed through ground control or compared with the results of field survey.",
        "page": 423,
        "supporting_evidence": ["E009"],
        "confidence": "high",
        "relevance": "Criticizes common methodological shortcoming"
    },
    {
        "claim_id": "C023",
        "content": "The study evaluated 100 square kilometres of high-resolution multispectral imagery using established methods of image analysis to discover features associated with past human activity.",
        "claim_type": "methodological_description",
        "verbatim_quote": "Our project evaluated 100 sq km of high-resolution multispectral imagery using established methods of image analysis to discover features associated with past human activity.",
        "page": 424,
        "supporting_evidence": ["E001"],
        "confidence": "high",
        "relevance": "Describes overall methodology of the project"
    },
    {
        "claim_id": "C024",
        "content": "Results from remote sensing were compared with existing data from the systematic MTS surface survey conducted between 2003 and 2007.",
        "claim_type": "methodological_description",
        "verbatim_quote": "Results were compared with existing data from the Murge Tableland Survey (MTS), a systematic archaeological surface survey that was conducted in a transect across the Salento Isthmus between 2003 and 2007 and included 10 sq km within our study area.",
        "page": 424,
        "supporting_evidence": ["E004"],
        "confidence": "high",
        "relevance": "Describes comparative framework"
    },
    {
        "claim_id": "C025",
        "content": "Variables such as rates of site recovery, time and labor costs, and overall character of results were compared between remote sensing and surface survey.",
        "claim_type": "methodological_description",
        "verbatim_quote": "Variables such as rates of site recovery, time and labor costs, and the overall character of the results were compared.",
        "page": 424,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Specifies comparison metrics"
    },
    {
        "claim_id": "C026",
        "content": "Surface survey and satellite image analysis profitably complement one another.",
        "claim_type": "interpretive_claim",
        "verbatim_quote": "indicating how surface survey and satellite image analysis profitably complement one another.",
        "page": 424,
        "supporting_evidence": [],
        "confidence": "medium",
        "relevance": "Key finding about complementary nature of methods"
    }
]

# ============================================================================
# IMPLICIT ARGUMENTS - Systematic 4-type scan on core claims
# ============================================================================

implicit_arguments = [
    {
        "implicit_argument_id": "IA001",
        "content": "Remote sensing guided by image analysis is more effective than random site selection (implied by claim that success rate 'too high to be explained by random association').",
        "argument_type": "unstated_premise",
        "trigger_text": "our success rate is too high to be explained by random association",
        "page": 423,
        "reconstruction_confidence": "high",
        "related_claims": ["C010"],
        "critical_for_logic": True,
        "notes": "Statistical comparison assumes random distribution as null hypothesis"
    },
    {
        "implicit_argument_id": "IA002",
        "content": "The MTS site definitions and sample are representative and appropriate for comparison (implied by using MTS as independent validation).",
        "argument_type": "unstated_premise",
        "trigger_text": "provided independent definitions for various types of sites and a large sample",
        "page": 423,
        "reconstruction_confidence": "high",
        "related_claims": ["C008", "C009"],
        "critical_for_logic": True,
        "notes": "Validity of comparison depends on MTS being appropriate baseline"
    },
    {
        "implicit_argument_id": "IA003",
        "content": "Four weeks of fieldwork represents an efficient time investment compared to traditional survey (implied by emphasis on time period).",
        "argument_type": "unstated_premise",
        "trigger_text": "during about four weeks of fieldwork",
        "page": 423,
        "reconstruction_confidence": "medium",
        "related_claims": ["C001", "C003"],
        "critical_for_logic": False,
        "notes": "Efficiency claim implicit in time specification"
    },
    {
        "implicit_argument_id": "IA004",
        "content": "Small teams represent a resource advantage over larger survey teams (implied by emphasis on 'small team').",
        "argument_type": "unstated_premise",
        "trigger_text": "allows large areas to be evaluated efficiently by a small team of researchers",
        "page": 423,
        "reconstruction_confidence": "medium",
        "related_claims": ["C001"],
        "critical_for_logic": False,
        "notes": "Efficiency argument assumes small team is advantageous"
    },
    {
        "implicit_argument_id": "IA005",
        "content": "Understanding what image features represent (geological conditions vs. subsurface remains) is important for methodological development (implied by emphasis on this finding).",
        "argument_type": "unstated_assumption",
        "trigger_text": "most of the detected features reflect geological conditions amenable to past human habitation rather than subsurface archaeological remains",
        "page": 423,
        "reconstruction_confidence": "high",
        "related_claims": ["C006"],
        "critical_for_logic": True,
        "notes": "Distinguishing feature types is presented as methodologically significant"
    },
    {
        "implicit_argument_id": "IA006",
        "content": "The combination of methods (remote sensing + ground control + survey + environmental research) is superior to any method used independently (implied by integrated approach).",
        "argument_type": "unstated_premise",
        "trigger_text": "When deployed in combination with ground control, archaeological surface survey, and environmental research",
        "page": 423,
        "reconstruction_confidence": "high",
        "related_claims": ["C001", "C012"],
        "critical_for_logic": True,
        "notes": "Integration argument assumes synergistic benefits"
    }
]

# ============================================================================
# UPDATE EXTRACTION FILE
# ============================================================================

# Add new items to data
data['evidence'].extend(evidence_items)
data['claims'].extend(claims_items)
data['implicit_arguments'].extend(implicit_arguments)

# Update timestamp
data['extraction_timestamp'] = datetime.now(timezone.utc).isoformat()

# Add extraction note for this section
if 'pass1_sections' not in data['extraction_notes']:
    data['extraction_notes']['pass1_sections'] = []

data['extraction_notes']['pass1_sections'].append({
    'section': 'Section 1: Abstract + Introduction',
    'pages': '423-424',
    'word_count_estimate': 1200,
    'items_extracted': {
        'evidence': len(evidence_items),
        'claims': len(claims_items),
        'implicit_arguments': len(implicit_arguments)
    },
    'notes': 'Liberal extraction from opening sections. Focus on methodological claims, efficiency arguments, and comparative framework. High density of claims about imagery capabilities and methodological gaps. Systematic 4-type implicit argument scan completed on all core claims.'
})

# Save updated extraction
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print(f"✓ Pass 1, Section 1 complete: Abstract + Introduction")
print(f"  - Evidence items: {len(evidence_items)}")
print(f"  - Claims: {len(claims_items)}")
print(f"  - Implicit arguments: {len(implicit_arguments)}")
print(f"  - Total items this section: {len(evidence_items) + len(claims_items) + len(implicit_arguments)}")
print(f"  - Running total: {len(data['evidence'])} evidence, {len(data['claims'])} claims, {len(data['implicit_arguments'])} implicit arguments")
