#!/usr/bin/env python3
"""
Section 4 Extraction: Early Eneolithic Contacts
Liberal Pass 1 extraction following 40-50% over-extraction target
"""

import json

# New items for Section 4 (pages 2-3)
# Continue from E046, C044, IA008

new_evidence = [
    {
        "id": "E047",
        "content": "Ukraine Eneolithic individuals dated from around 4500-3500 BC, associated with Cernavodă I and Usatove cultures",
        "evidence_type": "chronological_identification",
        "verbatim_quote": "Eneolithic individuals from Ukraine (Ukraine Eneolithic), dated from around 4500–3500 bc, associated with the Cernavodă I and Usatove cultures",
        "page": 3,
        "supports_claims": ["C045", "C046"]
    },
    {
        "id": "E048",
        "content": "Ukraine Eneolithic individuals form genetic cline in PCA space between Neolithic/SEE CA and Eneolithic steppe individuals",
        "evidence_type": "genetic_statistic",
        "verbatim_quote": "form a genetic cline in PCA space (Fig. 1b) between Neolithic/SEE CA individuals and published Eneolithic steppe individuals from the North Caucasus39 and Khvalynsk in western Russia32",
        "page": 3,
        "supports_claims": ["C046", "C047"]
    },
    {
        "id": "E049",
        "content": "Genetic cline reflects developments over wide chronological range of around 1,000 years",
        "evidence_type": "temporal_observation",
        "verbatim_quote": "The observed genetic cline reflects developments over a wide chronological range of around 1,000 years",
        "page": 3,
        "supports_claims": ["C048"]
    },
    {
        "id": "E050",
        "content": "Some newly reported 14C dates could be affected by freshwater reservoir effect",
        "evidence_type": "methodological_caveat",
        "verbatim_quote": "Some of the newly reported 14C dates could be affected by a freshwater reservoir effect43, common in Steppe Eneolithic sites44,45 and could therefore be several centuries younger than their reported dates.",
        "page": 3,
        "supports_claims": ["C049"]
    },
    {
        "id": "E051",
        "content": "Offset of around 500 years would still date most Ukraine Eneolithic individuals to fourth millennium BC",
        "evidence_type": "chronological_analysis",
        "verbatim_quote": "However, accounting for this possibility, an offset of around 500 years would still date most of the Ukraine Eneolithic individuals to the fourth millennium bc",
        "page": 3,
        "supports_claims": ["C050"]
    },
    {
        "id": "E052",
        "content": "Kartal individuals dated around 4150-3400 BC, associated with Cernavodă I culture",
        "evidence_type": "chronological_identification",
        "verbatim_quote": "Individuals from Kartal (around 4150–3400 bc), associated with the Cernavodă I culture",
        "page": 3,
        "supports_claims": ["C051"]
    },
    {
        "id": "E053",
        "content": "Kartal individuals genetically highly heterogeneous",
        "evidence_type": "genetic_observation",
        "verbatim_quote": "are genetically highly heterogeneous",
        "page": 3,
        "supports_claims": ["C051"]
    },
    {
        "id": "E054",
        "content": "No correlation found between Ukraine Eneolithic PC2 positions and 14C dates (Spearman's ρ = 0.113, P = 0.6656)",
        "evidence_type": "statistical_test",
        "verbatim_quote": "We tested for a correlation between positions of the Ukraine Eneolithic individuals in PC2 and their 14C dates and found none (Spearman's ρ = 0.113, P = 0.6656).",
        "page": 3,
        "supports_claims": ["C052"]
    },
    {
        "id": "E055",
        "content": "Broadscale shift in genetic affinities from SEE to steppe zone visible in outgroup f3 statistics when mapped geographically",
        "evidence_type": "genetic_statistic",
        "verbatim_quote": "The broadscale shift in genetic affinities between the CA and the Eneolithic, from SEE to the steppe zone, is also clearly visible in outgroup f3 statistics when mapped geographically",
        "page": 3,
        "supports_claims": ["C053"]
    },
    {
        "id": "E056",
        "content": "f4-symmetry statistics tested for excess shared ancestry with four Holocene cornerstone populations (Turkey_N, WHG, EHG/WSHG, CHG)",
        "evidence_type": "analytical_procedure",
        "verbatim_quote": "we tested for excess shared ancestry with four Holocene 'cornerstone' populations (Turkey_N, WHG, EHG/WSHG and CHG) (Supplementary Information 1.2), using f4-symmetry statistics",
        "page": 3,
        "supports_claims": ["C054"]
    },
    {
        "id": "E057",
        "content": "Ukraine Eneolithic shows excess affinity to all HG groups compared to Turkey_N, indicated by significantly negative f4 statistics (|Z| ≥ 3)",
        "evidence_type": "genetic_statistic",
        "verbatim_quote": "compared to Turkey_N, Ukraine Eneolithic individuals show excess affinity to all HG groups, as indicated by significantly negative f4 statistics (|Z| ≥ 3)",
        "page": 3,
        "supports_claims": ["C055"]
    },
    {
        "id": "E058",
        "content": "Conditioning on Steppe Eneolithic, Ukraine Eneolithic shows excess affinity to Turkey_N, symmetrical relatedness to CHG and WHG",
        "evidence_type": "genetic_statistic",
        "verbatim_quote": "conditioning on Steppe Eneolithic (Extended Data Fig. 6b), we observe excess affinity of Ukraine Eneolithic to Turkey_N, a symmetrical relatedness to CHG and WHG, while Steppe Eneolithic",
        "page": 3,
        "supports_claims": ["C056"]
    }
]

new_claims = [
    {
        "id": "C045",
        "content": "Ukraine Eneolithic individuals associated with Cernavodă I and Usatove cultures",
        "claim_type": "cultural_identification",
        "verbatim_quote": "Eneolithic individuals from Ukraine (Ukraine Eneolithic), dated from around 4500–3500 bc, associated with the Cernavodă I and Usatove cultures",
        "page": 3,
        "supporting_evidence": ["E047"]
    },
    {
        "id": "C046",
        "content": "Ukraine Eneolithic forms genetic cline between Neolithic/SEE CA and Eneolithic steppe populations",
        "claim_type": "genetic_interpretation",
        "verbatim_quote": "form a genetic cline in PCA space (Fig. 1b) between Neolithic/SEE CA individuals and published Eneolithic steppe individuals from the North Caucasus39 and Khvalynsk in western Russia32",
        "page": 3,
        "supporting_evidence": ["E047", "E048"]
    },
    {
        "id": "C047",
        "content": "Genetic cline indicates possible admixture between CA farmer-related groups and Eneolithic steppe groups",
        "claim_type": "genetic_interpretation",
        "verbatim_quote": "This indicates possible admixture between CA farmer-related groups and Eneolithic steppe groups",
        "page": 3,
        "supporting_evidence": ["E048"]
    },
    {
        "id": "C048",
        "content": "Genetic cline in line with cultural interactions described in archaeological record",
        "claim_type": "interdisciplinary_interpretation",
        "verbatim_quote": "as in line with cultural interactions described in the archaeological record40–42",
        "page": 3,
        "supporting_evidence": ["E049"]
    },
    {
        "id": "C049",
        "content": "Freshwater reservoir effect common in Steppe Eneolithic sites could make dates several centuries younger",
        "claim_type": "methodological_interpretation",
        "verbatim_quote": "Some of the newly reported 14C dates could be affected by a freshwater reservoir effect43, common in Steppe Eneolithic sites44,45 and could therefore be several centuries younger than their reported dates.",
        "page": 3,
        "supporting_evidence": ["E050"]
    },
    {
        "id": "C050",
        "content": "Even accounting for 500 year offset, Ukraine Eneolithic considerably earlier than Yamnaya expansion",
        "claim_type": "temporal_interpretation",
        "verbatim_quote": "However, accounting for this possibility, an offset of around 500 years would still date most of the Ukraine Eneolithic individuals to the fourth millennium bc and thus considerably earlier than the Yamnaya-associated steppe pastoralist expansion.",
        "page": 3,
        "supporting_evidence": ["E051"]
    },
    {
        "id": "C051",
        "content": "Kartal individuals from Cernavodă I culture are genetically highly heterogeneous",
        "claim_type": "genetic_interpretation",
        "verbatim_quote": "Individuals from Kartal (around 4150–3400 bc), associated with the Cernavodă I culture, are genetically highly heterogeneous",
        "page": 3,
        "supporting_evidence": ["E052", "E053"]
    },
    {
        "id": "C052",
        "content": "No temporal trend in genetic cline position for Ukraine Eneolithic individuals",
        "claim_type": "statistical_interpretation",
        "verbatim_quote": "We tested for a correlation between positions of the Ukraine Eneolithic individuals in PC2 and their 14C dates and found none",
        "page": 3,
        "supporting_evidence": ["E054"]
    },
    {
        "id": "C053",
        "content": "Broadscale shift in genetic affinities from SEE to steppe zone visible geographically",
        "claim_type": "genetic_interpretation",
        "verbatim_quote": "The broadscale shift in genetic affinities between the CA and the Eneolithic, from SEE to the steppe zone, is also clearly visible in outgroup f3 statistics when mapped geographically",
        "page": 3,
        "supporting_evidence": ["E055"]
    },
    {
        "id": "C054",
        "content": "Ukraine Eneolithic characterized using four Holocene cornerstone populations",
        "claim_type": "methodological_approach",
        "verbatim_quote": "To formally characterize the Ukraine Eneolithic individuals, we tested for excess shared ancestry with four Holocene 'cornerstone' populations (Turkey_N, WHG, EHG/WSHG and CHG)",
        "page": 3,
        "supporting_evidence": ["E056"]
    },
    {
        "id": "C055",
        "content": "Ukraine Eneolithic shows excess hunter-gatherer ancestry compared to Turkey_N",
        "claim_type": "genetic_interpretation",
        "verbatim_quote": "compared to Turkey_N, Ukraine Eneolithic individuals show excess affinity to all HG groups",
        "page": 3,
        "supporting_evidence": ["E057"]
    },
    {
        "id": "C056",
        "content": "Ukraine Eneolithic shows intermediate ancestry between Steppe Eneolithic and Turkey_N",
        "claim_type": "genetic_interpretation",
        "verbatim_quote": "conditioning on Steppe Eneolithic (Extended Data Fig. 6b), we observe excess affinity of Ukraine Eneolithic to Turkey_N, a symmetrical relatedness to CHG and WHG",
        "page": 3,
        "supporting_evidence": ["E058"]
    }
]

new_implicit_arguments = [
    {
        "id": "IA009",
        "content": "Genetic clines in PCA space directly reflect biological admixture processes rather than statistical artifacts",
        "argument_type": "methodological_assumption",
        "trigger_text": "form a genetic cline in PCA space (Fig. 1b) between Neolithic/SEE CA individuals and published Eneolithic steppe individuals",
        "page": 3,
        "related_claims": ["C046", "C047"],
        "rationale": "The interpretation of a cline as indicating 'possible admixture' assumes that intermediate PCA positions reflect biological mixing. This bridges from statistical pattern (cline in PC space) to biological process (admixture) without explicitly addressing alternative explanations such as shared ancestral structure, differential drift, or methodological effects of projecting ancient samples onto modern PCA axes."
    },
    {
        "id": "IA010",
        "content": "Genetic patterns align with and validate archaeological interpretations of cultural contact",
        "argument_type": "bridging_claim",
        "trigger_text": "as in line with cultural interactions described in the archaeological record",
        "page": 3,
        "related_claims": ["C048"],
        "rationale": "The phrase 'in line with' implies mutual validation between genetic and archaeological evidence, assuming both datasets independently capture the same historical processes. This bridges genetic admixture patterns to cultural interactions without explicitly stating the relationship between biological gene flow and cultural exchange (which may be correlated but not identical)."
    },
    {
        "id": "IA011",
        "content": "Absence of temporal correlation in genetic variation indicates ongoing contact rather than single admixture event",
        "argument_type": "interpretive_assumption",
        "trigger_text": "We tested for a correlation between positions of the Ukraine Eneolithic individuals in PC2 and their 14C dates and found none",
        "page": 3,
        "related_claims": ["C052"],
        "rationale": "The lack of temporal trend is presented as meaningful (tested explicitly), implying it informs our understanding of the contact process. This assumes that constant genetic variation across time reflects sustained admixture rather than alternative scenarios (rapid mixing followed by stasis, sampling gaps masking trends, or insufficient statistical power). The bridging assumption is that temporal patterns in genetic data directly reflect demographic process dynamics."
    }
]

# Load existing extraction
with open('/home/shawn/Code/llm-reproducibility/outputs/penske-et-al-2023/extraction.json', 'r') as f:
    data = json.load(f)

# Append new items
data['evidence'].extend(new_evidence)
data['claims'].extend(new_claims)
data['implicit_arguments'].extend(new_implicit_arguments)

# Update extraction notes
data['extraction_notes']['pass1_chunking']['section4'] = {
    "section_number": 4,
    "section_title": "Early Eneolithic Contacts",
    "page_range": "3",
    "estimated_words": 1400,
    "natural_boundary": "Before 'Genetic ancestries during the Bronze Age' section",
    "items_extracted": {
        "evidence": 12,
        "claims": 12,
        "implicit_arguments": 3
    }
}

# Save updated extraction
with open('/home/shawn/Code/llm-reproducibility/outputs/penske-et-al-2023/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Section 4 extraction complete:")
print(f"  Added: {len(new_evidence)} evidence, {len(new_claims)} claims, {len(new_implicit_arguments)} implicit arguments")
print(f"  New totals: {len(data['evidence'])} evidence, {len(data['claims'])} claims, {len(data['implicit_arguments'])} implicit arguments")
