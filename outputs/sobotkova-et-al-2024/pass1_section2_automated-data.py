#!/usr/bin/env python3
"""
Pass 1 Liberal Extraction - Section Group 2
Paper: Sobotkova et al. 2024 - Validating predictions of burial mounds
Section: Automated approaches + Data (lines 255-373)
Estimated words: ~1,500

This script extracts evidence, claims, and implicit arguments from the literature
review on automated approaches and the data description sections.
"""

import json
from pathlib import Path

extraction_file = Path("/home/shawn/Code/llm-reproducibility/outputs/sobotkova-et-al-2024/extraction.json")
with open(extraction_file, 'r') as f:
    extraction = json.load(f)

# Core Claims for this section:
# C013: AI/ML approaches to archaeological remote sensing are crossing adoption chasm (17% of 2023 publications)
# C014: ML literature lacks critical assessment - 63% of abstracts fail to mention negative aspects
# C015: Publication bias toward positive results exists in ML-for-archaeology

evidence_items = [
    {
        "evidence_id": "E014",
        "evidence_text": "Annual count of ML+archaeology publications increased from zero in 2014-2015 to 21 in 2023",
        "evidence_type": "quantitative_measurement",
        "evidence_status": "explicit",
        "verbatim_quote": "This search reveals that the annual count of relevant publications has increased from zero in 2014 and 2015 to 21 in 2023.",
        "location": {"section": "Automated approaches to remotely sensed data", "subsection": None, "paragraph": 3},
        "uncertainty_declared": False,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C013"]
    },
    {
        "evidence_id": "E015",
        "evidence_text": "21 ML publications in 2023 represent 17% of total archaeological remote sensing publications (n=125)",
        "evidence_type": "quantitative_measurement",
        "evidence_status": "explicit",
        "verbatim_quote": "These 21 publications represent about 17% of the 2023 total (n 5 125) for archaeological remote sensing",
        "location": {"section": "Automated approaches to remotely sensed data", "subsection": None, "paragraph": 3},
        "uncertainty_declared": False,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C013"]
    },
    {
        "evidence_id": "E016",
        "evidence_text": "63% of ML-for-archaeology paper abstracts fail to mention any negative aspects",
        "evidence_type": "quantitative_measurement",
        "evidence_status": "explicit",
        "verbatim_quote": "Considering the 70 papers from the Web of Science mentioned above, 44 abstracts (63%) fail to mention any negative aspects of AI/ML approaches at all.",
        "location": {"section": "Automated approaches to remotely sensed data", "subsection": None, "paragraph": 5},
        "uncertainty_declared": False,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C014", "C015"]
    },
    {
        "evidence_id": "E017",
        "evidence_text": "Of 26 papers mentioning challenges, 11 state challenges were overcome (unqualified successes)",
        "evidence_type": "quantitative_measurement",
        "evidence_status": "explicit",
        "verbatim_quote": "Of the 26 papers (37%) with abstracts that mention some challenge or limitation, 11 state that they were overcome by the researchers, representing unqualified successes.",
        "location": {"section": "Automated approaches to remotely sensed data", "subsection": None, "paragraph": 5},
        "uncertainty_declared": False,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C014", "C015"]
    },
    {
        "evidence_id": "E018",
        "evidence_text": "Only 6% of papers (4 of 70) discuss attempts ending in partial or complete failures",
        "evidence_type": "quantitative_measurement",
        "evidence_status": "explicit",
        "verbatim_quote": "Of those 15, seven (10% of the corpus) present qualified successes, while four (6%) discuss attempts to deploy ML that ended in partial or complete failures",
        "location": {"section": "Automated approaches to remotely sensed data", "subsection": None, "paragraph": 5},
        "uncertainty_declared": False,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C014", "C015"]
    },
    {
        "evidence_id": "E019",
        "evidence_text": "TRAP survey collected dataset of 773 mounds during 2009-2011 fieldwork in Kazanlak Valley",
        "evidence_type": "quantitative_measurement",
        "evidence_status": "explicit",
        "verbatim_quote": "In this study we used a dataset of 773 mounds, collected by TRAP during 2009 – 2011 field survey in the Kazanlak Valley, Bulgaria",
        "location": {"section": "Data", "subsection": "Pedestrian survey", "paragraph": 1},
        "uncertainty_declared": False,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C016"]
    },
    {
        "evidence_id": "E020",
        "evidence_text": "TRAP fieldwork covered 85 sq km via pedestrian survey",
        "evidence_type": "quantitative_measurement",
        "evidence_status": "explicit",
        "verbatim_quote": "This fieldwork covered some 85 sq km, inspected directly via pedestrian survey.",
        "location": {"section": "Data", "subsection": "Pedestrian survey", "paragraph": 1},
        "uncertainty_declared": False,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C016"]
    },
    {
        "evidence_id": "E021",
        "evidence_text": "Satellite imagery consists of two IKONOS scenes covering 600 sq km",
        "evidence_type": "quantitative_measurement",
        "evidence_status": "explicit",
        "verbatim_quote": "The satellite imagery used in this study consists of two IKONOS scenes covering 600 sq km delivered in geoTIFF format",
        "location": {"section": "Data", "subsection": "Satellite imagery", "paragraph": 1},
        "uncertainty_declared": False,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C016"]
    },
    {
        "evidence_id": "E022",
        "evidence_text": "IKONOS imagery included panchromatic band at 1m resolution and multispectral (RGBNIR) at 4m resolution",
        "evidence_type": "technical_specification",
        "evidence_status": "explicit",
        "verbatim_quote": "The scenes included a panchromatic band at 1 m resolution and a multispectral image (RGBNIR) at 4 m resolution.",
        "location": {"section": "Data", "subsection": "Satellite imagery", "paragraph": 1},
        "uncertainty_declared": False,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C016"]
    }
]

claims_items = [
    {
        "claim_id": "C013",
        "claim_text": "AI/ML approaches to archaeological remote sensing are on cusp of crossing the chasm from early adopters to early majority",
        "claim_type": "finding",
        "claim_role": "intermediate",
        "claim_status": "explicit",
        "verbatim_quote": "If publication counts are used a proxy for research, this 17% figure indicates that AI/ML is on the cusp of \\\"crossing the chasm\\\" separating \\\"innovators\\\" and \\\"early adopters\\\" (together 16% of the population) from the \\\"early majority\\\", according to Rogers' diffusion of innovations paradigm as modified by Moore",
        "location": {"section": "Automated approaches to remotely sensed data", "subsection": None, "paragraph": 3},
        "supported_by_evidence": ["E014", "E015"],
        "supported_by_claims": [],
        "supports_claims": ["C005"],
        "alternatives_mentioned": False,
        "qualifications": [],
        "contradicts": []
    },
    {
        "claim_id": "C014",
        "claim_text": "Critical assessment has been neglected in ML-for-archaeology literature",
        "claim_type": "methodological_critique",
        "claim_role": "intermediate",
        "claim_status": "explicit",
        "verbatim_quote": "As these approaches spread to a broader cohort of researchers, potential adopters need to recognise their challenges and limitations. Critical assessment has, however, been somewhat neglected in the literature.",
        "location": {"section": "Automated approaches to remotely sensed data", "subsection": None, "paragraph": 5},
        "supported_by_evidence": ["E016", "E017", "E018"],
        "supported_by_claims": [],
        "supports_claims": ["C005"],
        "alternatives_mentioned": False,
        "qualifications": ["somewhat neglected"],
        "contradicts": []
    },
    {
        "claim_id": "C015",
        "claim_text": "Overwhelmingly positive tone of ML papers indicates publication bias and rhetorical shift toward less qualified presentation",
        "claim_type": "methodological_critique",
        "claim_role": "intermediate",
        "claim_status": "explicit",
        "verbatim_quote": "The overwhelmingly positive tone of these papers likely indicates a certain degree of \\\"publication bias\\\", where positive results are more likely to be published than negative (Brown et al., 2017; Dickersin et al., 1987; Harrison et al., 2017; Ioannidis, 2005; Kühberger et al., 2014; Møller and Jennions, 2001), or at the very least a reflection of the rhetorical shift in scientific research towards less qualified or uncertain presentation of outcomes",
        "location": {"section": "Automated approaches to remotely sensed data", "subsection": None, "paragraph": 5},
        "supported_by_evidence": ["E016", "E017", "E018"],
        "supported_by_claims": [],
        "supports_claims": ["C005"],
        "alternatives_mentioned": True,
        "qualifications": ["likely indicates"],
        "contradicts": []
    },
    {
        "claim_id": "C016",
        "claim_text": "Study used comprehensive field and satellite data from Kazanlak Valley for validation",
        "claim_type": "methodological",
        "claim_role": "supporting",
        "claim_status": "explicit",
        "verbatim_quote": "In this study we used a dataset of 773 mounds, collected by TRAP during 2009 – 2011 field survey in the Kazanlak Valley, Bulgaria",
        "location": {"section": "Data", "subsection": "Pedestrian survey", "paragraph": 1},
        "supported_by_evidence": ["E019", "E020", "E021", "E022"],
        "supported_by_claims": [],
        "supports_claims": ["C003"],
        "alternatives_mentioned": False,
        "qualifications": [],
        "contradicts": []
    }
]

implicit_arguments = [
    {
        "implicit_argument_id": "IA007",
        "implicit_argument_text": "Widespread ML adoption will occur despite limited critical literature unless failures are documented",
        "implicit_argument_type": "logical_implication",
        "trigger_text": [
            "If publication counts are used a proxy for research, this 17% figure indicates that AI/ML is on the cusp of \\\"crossing the chasm\\\"",
            "As these approaches spread to a broader cohort of researchers, potential adopters need to recognise their challenges and limitations.",
            "In this context, it is important to document unsuccessful attempts to apply ML techniques to archaeological remote sensing"
        ],
        "trigger_locations": [
            {"section": "Automated approaches to remotely sensed data", "subsection": None, "paragraph": 3},
            {"section": "Automated approaches to remotely sensed data", "subsection": None, "paragraph": 5},
            {"section": "Automated approaches to remotely sensed data", "subsection": None, "paragraph": 5}
        ],
        "inference_reasoning": "The paper connects adoption trajectory ('crossing the chasm') with need for critical information ('potential adopters need to recognise challenges') and documentation imperative ('important to document failures'). The implicit argument is that adoption will proceed regardless—crossing the chasm is presented as inevitable or already occurring—therefore failure documentation becomes urgent. Without stating this explicitly, the paper implies that technology diffusion momentum makes critical literature time-sensitive: if early majority adopt based on incomplete information, systematic problems may be replicated at scale.",
        "location": {"section": "Automated approaches to remotely sensed data", "subsection": None, "paragraph": 5},
        "supports_claims": ["C013", "C014", "C015"],
        "assessment_implication": "Affects urgency assessment. Suggests timing matters—documentation of limitations must occur before widespread adoption embeds problematic practices. Relevant for assessing whether early-stage critical assessment is adequate."
    }
]

# Add items
extraction["evidence"].extend(evidence_items)
extraction["claims"].extend(claims_items)
extraction["implicit_arguments"].extend(implicit_arguments)

# Update extraction notes
extraction["extraction_metadata"]["extraction_notes"].append({
    "pass1_section2": {
        "section_group": "Automated approaches + Data",
        "word_count_estimate": 1500,
        "sections_combined": ["Automated approaches to remotely sensed data", "Data (Pedestrian survey, Satellite imagery)"],
        "extraction_date": "2025-10-30",
        "items_extracted": {"evidence": len(evidence_items), "claims": len(claims_items), "implicit_arguments": len(implicit_arguments)},
        "core_claims_identified": 0,
        "intermediate_claims": 4,
        "implicit_argument_scan_completed": True,
        "notes": "Liberal extraction applied. Quantitative publication analysis evidence extracted. Implicit argument IA007 identified through systematic scan connecting adoption trajectory with documentation urgency."
    }
})

# Save
with open(extraction_file, 'w') as f:
    json.dump(extraction, f, indent=2, ensure_ascii=False)

print(f"✓ Pass 1 Section 2 extraction complete")
print(f"  Evidence: {len(evidence_items)} items")
print(f"  Claims: {len(claims_items)} items")
print(f"  Implicit Arguments: {len(implicit_arguments)} items")
print(f"  Total: {len(evidence_items) + len(claims_items) + len(implicit_arguments)} items")
