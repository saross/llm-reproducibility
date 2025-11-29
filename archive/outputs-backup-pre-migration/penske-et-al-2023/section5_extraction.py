#!/usr/bin/env python3
"""
Section 5 Extraction: Genetic Ancestries during the Bronze Age
Liberal Pass 1 extraction following 40-50% over-extraction target
Pages 3-4, ~1300 words
"""

import json

# New items for Section 5 - Continue from E058, C056, IA011

new_evidence = [
    {
        "id": "E059",
        "content": "EBA individuals characterized by two contrasting clusters of genetic ancestry in PCA space",
        "evidence_type": "genetic_statistic",
        "verbatim_quote": "The EBA individuals in this study are characterized by two contrasting clusters of genetic ancestry in PCA space (Fig. 1b)",
        "page": 3,
        "supports_claims": ["C057"]
    },
    {
        "id": "E060",
        "content": "EBA individuals show different genetic affinities in outgroup f3 statistics",
        "evidence_type": "genetic_statistic",
        "verbatim_quote": "and different genetic affinities in outgroup f3 statistics (Fig. 2 and Supplementary Table C)",
        "page": 3,
        "supports_claims": ["C057"]
    },
    {
        "id": "E061",
        "content": "YUN and PIE078 individuals date to first half of third millennium BC and resemble SEE CA groups",
        "evidence_type": "genetic_observation",
        "verbatim_quote": "Individuals from YUN and individual PIE078, who date to the first half of the third millennium BC, resemble the SEE CA groups",
        "page": 3,
        "supports_claims": ["C058"]
    },
    {
        "id": "E062",
        "content": "BOY_EBA and MAJ_EBA individuals fall within 'steppe ancestry' cluster associated with Yamnaya",
        "evidence_type": "genetic_observation",
        "verbatim_quote": "whereas BOY_EBA and MAJ_EBA individuals fall within the 'steppe ancestry' cluster, commonly associated with the Yamnaya cultural complex",
        "page": 3,
        "supports_claims": ["C059"]
    },
    {
        "id": "E063",
        "content": "Two outlier individuals BOY019 and YUN041 fall in space between two EBA clusters",
        "evidence_type": "genetic_observation",
        "verbatim_quote": "Two outlier individuals, BOY019 and YUN041, fall in the space between.",
        "page": 3,
        "supports_claims": ["C060"]
    },
    {
        "id": "E064",
        "content": "Males from YUN_EBA/PIE078 carried Y-chromosome lineages I2a",
        "evidence_type": "haplogroup_observation",
        "verbatim_quote": "the males from YUN_EBA/PIE078 carried Y-chromosome lineages I2a, suggestive of a HG legacy",
        "page": 3,
        "supports_claims": ["C061"]
    },
    {
        "id": "E065",
        "content": "Males from BOY/MAJ_EBA carried R1b-Z2103 or derived lineages",
        "evidence_type": "haplogroup_observation",
        "verbatim_quote": "while the males from BOY/MAJ_EBA carried R1b-Z2103 or derived lineages, a characteristic hallmark of Yamnaya-associated ancestry",
        "page": 3,
        "supports_claims": ["C062"]
    },
    {
        "id": "E066",
        "content": "f4(CA, EBA; HGs, Mbuti) confirmed excess HG ancestry in YUN and PIE EBA individuals with significant negative results (|Z| ≤ 3)",
        "evidence_type": "genetic_statistic",
        "verbatim_quote": "by using f4(CA, EBA; HGs, Mbuti) and confirmed the excess HG ancestry in EBA individuals from YUN and PIE with significant negative results (|Z| ≤ 3)",
        "page": 3,
        "supports_claims": ["C063"]
    },
    {
        "id": "E067",
        "content": "Only outlier individual YUN041 has higher affinity to VAR_CA than to other EBA groups",
        "evidence_type": "genetic_statistic",
        "verbatim_quote": "Here, only the outlier individual YUN041 has a higher affinity to VAR_CA than to other EBA groups",
        "page": 3,
        "supports_claims": ["C064"]
    },
    {
        "id": "E068",
        "content": "PIE078 and YUN_EBA can be modelled with Turkey_N, CHG and WHG in distal qpAdm",
        "evidence_type": "genetic_modelling",
        "verbatim_quote": "PIE078 and YUN_EBA can be modelled with Turkey_N, CHG and WHG (Fig. 3c and Supplementary Table X)",
        "page": 3,
        "supports_claims": ["C065"]
    },
    {
        "id": "E069",
        "content": "MAJ_EBA, BOY_EBA, BOY019 and YUN041 require EHG ancestry as additional source in distal qpAdm",
        "evidence_type": "genetic_modelling",
        "verbatim_quote": "whereas MAJ_EBA, BOY_EBA, BOY019 and YUN041 require EHG ancestry as an additional source (Fig. 3c)",
        "page": 3,
        "supports_claims": ["C066"]
    },
    {
        "id": "E070",
        "content": "All EBA individuals show excess affinity to Turkey_N compared to Steppe Eneolithic (except Yamnaya Caucasus)",
        "evidence_type": "genetic_statistic",
        "verbatim_quote": "With the exception of Yamnaya Caucasus, all EBA individuals show an excess affinity to Turkey_N when compared to Steppe Eneolithic",
        "page": 3,
        "supports_claims": ["C067"]
    },
    {
        "id": "E071",
        "content": "All EBA individuals share drift with WHG and EHG/WSHG compared to Caucasus Eneolithic/Maykop",
        "evidence_type": "genetic_statistic",
        "verbatim_quote": "Further, when compared to Caucasus Eneolithic/Maykop all EBA individuals share drift with WHG and EHG/WSHG",
        "page": 3,
        "supports_claims": ["C068"]
    },
    {
        "id": "E072",
        "content": "All f4 statistics non-significant (|Z| ≤ 3) for Yamnaya-associated individuals indicating genetic similarity",
        "evidence_type": "genetic_statistic",
        "verbatim_quote": "Here, with the exception of outlier individual Ukraine_Ozera_EBA_Yamnaya, all f4 statistics are non-significant (|Z| ≤ 3) (Supplementary Table W), which indicates that all Yamnaya-associated individuals including those from Ukraine and Bulgaria are genetically highly similar.",
        "page": 3,
        "supports_claims": ["C069"]
    },
    {
        "id": "E073",
        "content": "BOY_EBA and Yamnaya Samara can be modelled as three-way mixture in proximal qpAdm",
        "evidence_type": "genetic_modelling",
        "verbatim_quote": "we find that BOY_EBA and Yamnaya Samara can be modelled as a three-way",
        "page": 3,
        "supports_claims": ["C070"]
    }
]

new_claims = [
    {
        "id": "C057",
        "content": "EBA individuals show two contrasting genetic ancestry clusters",
        "claim_type": "genetic_interpretation",
        "verbatim_quote": "The EBA individuals in this study are characterized by two contrasting clusters of genetic ancestry in PCA space (Fig. 1b) and different genetic affinities in outgroup f3 statistics",
        "page": 3,
        "supporting_evidence": ["E059", "E060"]
    },
    {
        "id": "C058",
        "content": "YUN and PIE078 from first half of third millennium BC resemble SEE CA groups genetically",
        "claim_type": "genetic_interpretation",
        "verbatim_quote": "Individuals from YUN and individual PIE078, who date to the first half of the third millennium BC, resemble the SEE CA groups",
        "page": 3,
        "supporting_evidence": ["E061"]
    },
    {
        "id": "C059",
        "content": "BOY_EBA and MAJ_EBA have steppe ancestry associated with Yamnaya",
        "claim_type": "genetic_interpretation",
        "verbatim_quote": "BOY_EBA and MAJ_EBA individuals fall within the 'steppe ancestry' cluster, commonly associated with the Yamnaya cultural complex",
        "page": 3,
        "supporting_evidence": ["E062"]
    },
    {
        "id": "C060",
        "content": "BOY019 and YUN041 are genetic outliers with intermediate ancestry",
        "claim_type": "genetic_interpretation",
        "verbatim_quote": "Two outlier individuals, BOY019 and YUN041, fall in the space between.",
        "page": 3,
        "supporting_evidence": ["E063"]
    },
    {
        "id": "C061",
        "content": "I2a Y-chromosome lineages in YUN_EBA/PIE078 males suggestive of HG legacy",
        "claim_type": "genetic_interpretation",
        "verbatim_quote": "the males from YUN_EBA/PIE078 carried Y-chromosome lineages I2a, suggestive of a HG legacy",
        "page": 3,
        "supporting_evidence": ["E064"]
    },
    {
        "id": "C062",
        "content": "R1b-Z2103 lineages in BOY/MAJ_EBA males characteristic hallmark of Yamnaya ancestry",
        "claim_type": "genetic_interpretation",
        "verbatim_quote": "the males from BOY/MAJ_EBA carried R1b-Z2103 or derived lineages, a characteristic hallmark of Yamnaya-associated ancestry",
        "page": 3,
        "supporting_evidence": ["E065"]
    },
    {
        "id": "C063",
        "content": "YUN_EBA and PIE078 have excess HG ancestry compared to CA predecessors",
        "claim_type": "genetic_interpretation",
        "verbatim_quote": "we tested for additional attraction towards HG-related groups in YUN_EBA and PIE078 compared to their CA predecessors by using f4(CA, EBA; HGs, Mbuti) and confirmed the excess HG ancestry",
        "page": 3,
        "supporting_evidence": ["E066"]
    },
    {
        "id": "C064",
        "content": "YUN041 outlier has higher farmer ancestry than other Yamnaya-associated EBA groups",
        "claim_type": "genetic_interpretation",
        "verbatim_quote": "only the outlier individual YUN041 has a higher affinity to VAR_CA than to other EBA groups",
        "page": 3,
        "supporting_evidence": ["E067"]
    },
    {
        "id": "C065",
        "content": "PIE078 and YUN_EBA have ancestry composition similar to Neolithic/CA groups",
        "claim_type": "genetic_interpretation",
        "verbatim_quote": "Distal qpAdm modelling with cornerstone populations confirms the contrasting ancestries of the two main EBA clusters. PIE078 and YUN_EBA can be modelled with Turkey_N, CHG and WHG",
        "page": 3,
        "supporting_evidence": ["E068"]
    },
    {
        "id": "C066",
        "content": "Yamnaya-associated EBA groups require EHG ancestry component",
        "claim_type": "genetic_interpretation",
        "verbatim_quote": "whereas MAJ_EBA, BOY_EBA, BOY019 and YUN041 require EHG ancestry as an additional source",
        "page": 3,
        "supporting_evidence": ["E069"]
    },
    {
        "id": "C067",
        "content": "EBA Yamnaya-associated individuals have excess Turkey_N affinity compared to Steppe Eneolithic",
        "claim_type": "genetic_interpretation",
        "verbatim_quote": "With the exception of Yamnaya Caucasus, all EBA individuals show an excess affinity to Turkey_N when compared to Steppe Eneolithic",
        "page": 3,
        "supporting_evidence": ["E070"]
    },
    {
        "id": "C068",
        "content": "EBA individuals share more drift with HG groups than Caucasus Eneolithic/Maykop",
        "claim_type": "genetic_interpretation",
        "verbatim_quote": "when compared to Caucasus Eneolithic/Maykop all EBA individuals share drift with WHG and EHG/WSHG",
        "page": 3,
        "supporting_evidence": ["E071"]
    },
    {
        "id": "C069",
        "content": "All Yamnaya-associated individuals from Ukraine and Bulgaria are genetically highly similar",
        "claim_type": "genetic_interpretation",
        "verbatim_quote": "all f4 statistics are non-significant (|Z| ≤ 3) (Supplementary Table W), which indicates that all Yamnaya-associated individuals including those from Ukraine and Bulgaria are genetically highly similar",
        "page": 3,
        "supporting_evidence": ["E072"]
    },
    {
        "id": "C070",
        "content": "BOY_EBA and Yamnaya Samara show similar three-way ancestry mixture",
        "claim_type": "genetic_interpretation",
        "verbatim_quote": "we find that BOY_EBA and Yamnaya Samara can be modelled as a three-way mixture",
        "page": 3,
        "supporting_evidence": ["E073"]
    }
]

new_implicit_arguments = [
    {
        "id": "IA012",
        "content": "Y-chromosome haplogroups reliably track population ancestry and historical connections",
        "argument_type": "methodological_assumption",
        "trigger_text": "the males from YUN_EBA/PIE078 carried Y-chromosome lineages I2a, suggestive of a HG legacy",
        "page": 3,
        "related_claims": ["C061", "C062"],
        "rationale": "The interpretation of Y-chromosome lineages as 'suggestive of HG legacy' or 'characteristic hallmark of Yamnaya' assumes uniparental markers reliably indicate population history. This bridges from observing specific haplogroups to inferring ancestry sources, assuming limited male-mediated gene flow, no lineage extinction/drift in source populations, and that haplogroup geography reflects ancient rather than more recent distributions."
    },
    {
        "id": "IA013",
        "content": "Two distinct EBA genetic clusters reflect separate migration events or populations",
        "argument_type": "demographic_assumption",
        "trigger_text": "The EBA individuals in this study are characterized by two contrasting clusters of genetic ancestry",
        "page": 3,
        "related_claims": ["C057", "C058", "C059"],
        "rationale": "The description of 'two contrasting clusters' and their interpretation as representing different ancestries (farmer-like vs steppe-like) assumes genetic clustering reflects distinct demographic histories. This bridges from statistical clustering to demographic interpretation without explicitly addressing whether clusters represent separate migration streams, temporal layering, sampling from distinct social groups within mixed populations, or continuous variation artificially divided by analytical methods."
    }
]

# Load, append, update, save
with open('/home/shawn/Code/llm-reproducibility/outputs/penske-et-al-2023/extraction.json', 'r') as f:
    data = json.load(f)

data['evidence'].extend(new_evidence)
data['claims'].extend(new_claims)
data['implicit_arguments'].extend(new_implicit_arguments)

data['extraction_notes']['pass1_chunking']['section5'] = {
    "section_number": 5,
    "section_title": "Genetic Ancestries during the Bronze Age",
    "page_range": "3-4",
    "estimated_words": 1300,
    "natural_boundary": "Before 'Discussion' section",
    "items_extracted": {
        "evidence": 15,
        "claims": 14,
        "implicit_arguments": 2
    }
}

with open('/home/shawn/Code/llm-reproducibility/outputs/penske-et-al-2023/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Section 5 extraction complete:")
print(f"  Added: {len(new_evidence)} evidence, {len(new_claims)} claims, {len(new_implicit_arguments)} implicit arguments")
print(f"  New totals: {len(data['evidence'])} evidence, {len(data['claims'])} claims, {len(data['implicit_arguments'])} implicit arguments")
