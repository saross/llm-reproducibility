#!/usr/bin/env python3
"""
Section 6 Extraction: Discussion
Liberal Pass 1 extraction following 40-50% over-extraction target
Pages 4-5, ~1200 words
"""

import json

# New items for Section 6 - Continue from E073, C070, IA013

new_evidence = [
    {
        "id": "E074",
        "content": "Genetic homogeneity observed in and across four CA sites (PIE, YUN, PTK, VAR) of fifth millennium BC",
        "evidence_type": "genetic_observation",
        "verbatim_quote": "The genetic homogeneity observed in and across the four CA sites (PIE, YUN, PTK and VAR) of the fifth millennium bc",
        "page": 4,
        "supports_claims": ["C071"]
    },
    {
        "id": "E075",
        "content": "Shared shorter IBD tracts between sites consistent with transregional connectivity in material culture",
        "evidence_type": "genetic_observation",
        "verbatim_quote": "Shared shorter IBD tracts between sites are consistent with the transregional connectivity visible in the material culture.",
        "page": 4,
        "supports_claims": ["C072"]
    },
    {
        "id": "E076",
        "content": "No evidence for pathogens among CA individuals apart from two HBV-positive individuals (YUN048, VAR021)",
        "evidence_type": "pathogen_screening",
        "verbatim_quote": "Despite the systematic screening of teeth, we found no evidence for pathogens among the CA individuals of the fifth and fourth millennium bc, apart from two individuals (YUN048 and VAR021), who were positive for the Hepatitis B virus (HBV)52",
        "page": 4,
        "supports_claims": ["C073"]
    },
    {
        "id": "E077",
        "content": "VAR021 also positive for Salmonella enterica",
        "evidence_type": "pathogen_screening",
        "verbatim_quote": "while individual VAR021 was also positive for Salmonella enterica",
        "page": 4,
        "supports_claims": ["C073"]
    },
    {
        "id": "E078",
        "content": "Archaeological evidence shows early CA Gumelniţa groups settled deep into steppe zone by mid-fifth millennium BC",
        "evidence_type": "archaeological_observation",
        "verbatim_quote": "Archaeological evidence shows that the early CA Gumelniţa groups had already settled deep into the steppe zone by the mid-fifth millennium bc",
        "page": 4,
        "supports_claims": ["C074"]
    },
    {
        "id": "E079",
        "content": "Heterogeneity of individuals from Kartal site stands out",
        "evidence_type": "genetic_observation",
        "verbatim_quote": "Here, the heterogeneity of the individuals from the site Kartal stands out",
        "page": 4,
        "supports_claims": ["C075"]
    },
    {
        "id": "E080",
        "content": "Kartal located on Danube delta at northern end of former Gumelniţa–Kodžadermen–Karanovo VI complex distribution",
        "evidence_type": "geographical_observation",
        "verbatim_quote": "which is located on the Danube delta at the northern end of the former distribution of the Chalcolithic Gumelniţa–Kodžadermen–Karanovo VI complex",
        "page": 4,
        "supports_claims": ["C075"]
    },
    {
        "id": "E081",
        "content": "Majaky and Usatove groups more homogenous, located north of Dniester River",
        "evidence_type": "genetic_observation",
        "verbatim_quote": "By contrast, the more homogenous Majaky and Usatove groups, located north of the Dniester River",
        "page": 4,
        "supports_claims": ["C076"]
    },
    {
        "id": "E082",
        "content": "Variable cultural influences attested by archaeological record traceable genetically",
        "evidence_type": "interdisciplinary_observation",
        "verbatim_quote": "Moreover, variable cultural influences attested by the archaeological record40,41,53 are also traceable genetically.",
        "page": 4,
        "supports_claims": ["C077"]
    },
    {
        "id": "E083",
        "content": "EBA individuals from YUN and PIE from fourth/third millennia BC do not show traces of steppe-like ancestry",
        "evidence_type": "genetic_observation",
        "verbatim_quote": "In fact, EBA individuals from the fourth and third millennia bc from YUN and PIE do not show traces of steppe-like ancestry",
        "page": 4,
        "supports_claims": ["C078"]
    },
    {
        "id": "E084",
        "content": "Resurgence of HG ancestry observed widely in Europe during fourth millennium BC",
        "evidence_type": "comparative_observation",
        "verbatim_quote": "but instead a resurgence of HG ancestry observed widely in Europe during the fourth millennium bc (refs. 4,29,54,55)",
        "page": 4,
        "supports_claims": ["C079"]
    },
    {
        "id": "E085",
        "content": "Appearance of Yamnaya migrants traced in local time transect at Majaky and at Boyanovo",
        "evidence_type": "genetic_observation",
        "verbatim_quote": "we can trace the appearance of migrants from the steppe, clearly attributed to Yamnaya culturally and genetically, in the local time transect at Majaky but also at Boyanovo in the Bulgarian lowlands of the Thracian Plain.",
        "page": 4,
        "supports_claims": ["C080"]
    },
    {
        "id": "E086",
        "content": "Two outlier individuals from EBA YUN and BOY bear witness to occasional admixture",
        "evidence_type": "genetic_observation",
        "verbatim_quote": "Two outlier individuals from EBA YUN and BOY bear witness to occasional admixture between inhabitants of EBA tells and incoming steppe pastoralists.",
        "page": 4,
        "supports_claims": ["C081"]
    }
]

new_claims = [
    {
        "id": "C071",
        "content": "Genetic homogeneity in CA sites matches cultural homogeneity of archaeological records",
        "claim_type": "interdisciplinary_interpretation",
        "verbatim_quote": "The genetic homogeneity observed in and across the four CA sites (PIE, YUN, PTK and VAR) of the fifth millennium bc matches the cultural homogeneity of the archaeological records",
        "page": 4,
        "supporting_evidence": ["E074"]
    },
    {
        "id": "C072",
        "content": "CA genetic homogeneity suggests extended period of stable sociopolitical network without large-scale transformations",
        "claim_type": "sociopolitical_interpretation",
        "verbatim_quote": "suggests an extended period of a relative stable sociopolitical network and absence of large-scale cultural and genetic transformations",
        "page": 4,
        "supporting_evidence": ["E074", "E075"]
    },
    {
        "id": "C073",
        "content": "Systematic pathogen screening found limited evidence among CA individuals",
        "claim_type": "methodological_result",
        "verbatim_quote": "Despite the systematic screening of teeth, we found no evidence for pathogens among the CA individuals of the fifth and fourth millennium bc, apart from two individuals",
        "page": 4,
        "supporting_evidence": ["E076", "E077"]
    },
    {
        "id": "C074",
        "content": "Principal finding indicates early contact and admixture between CA farming groups from SEE and Eneolithic steppe groups",
        "claim_type": "major_finding",
        "verbatim_quote": "A principal finding from our study indicates early contact and admixture between CA farming groups from SEE and Eneolithic groups from the steppe zone in today's southern Ukraine, possibly starting in the middle of the fifth millennium bc",
        "page": 4,
        "supporting_evidence": ["E078"]
    },
    {
        "id": "C075",
        "content": "Kartal heterogeneity represents transformative nature and dynamics of fourth millennium BC",
        "claim_type": "historical_interpretation",
        "verbatim_quote": "Here, the heterogeneity of the individuals from the site Kartal stands out, which is located on the Danube delta at the northern end of the former distribution of the Chalcolithic Gumelniţa–Kodžadermen–Karanovo VI complex and thus represents the transformative nature and dynamics of the fourth millennium bc in action.",
        "page": 4,
        "supporting_evidence": ["E079", "E080"]
    },
    {
        "id": "C076",
        "content": "Majaky and Usatove homogeneity suggests assimilation processes had already occurred",
        "claim_type": "demographic_interpretation",
        "verbatim_quote": "By contrast, the more homogenous Majaky and Usatove groups, located north of the Dniester River, show that such assimilation processes had already occurred",
        "page": 4,
        "supporting_evidence": ["E081"]
    },
    {
        "id": "C077",
        "content": "Variable cultural influences from archaeological record traceable in genetic data",
        "claim_type": "interdisciplinary_interpretation",
        "verbatim_quote": "Moreover, variable cultural influences attested by the archaeological record40,41,53 are also traceable genetically.",
        "page": 4,
        "supporting_evidence": ["E082"]
    },
    {
        "id": "C078",
        "content": "Livestock, innovations and technological advances exchanged through zones of interaction",
        "claim_type": "cultural_interpretation",
        "verbatim_quote": "We argue that livestock, innovations and technological advances were exchanged through these zones of interaction, which then led to the establishment of fully developed pastoralism in the steppe by the end of the fourth millennium BC.",
        "page": 4,
        "supporting_evidence": []
    },
    {
        "id": "C079",
        "content": "Early Eneolithic admixture local to northwestern Black Sea region, did not affect SEE hinterland",
        "claim_type": "geographical_interpretation",
        "verbatim_quote": "The early admixture during the Eneolithic presented in this study appears to be local to the northwestern Black Sea region of the fourth millennium bc and did not affect the hinterland in SEE.",
        "page": 4,
        "supporting_evidence": ["E083", "E084"]
    },
    {
        "id": "C080",
        "content": "Resurgence of HG ancestry in EBA indicates presence of remnant HG groups in non-farmed regions",
        "claim_type": "demographic_interpretation",
        "verbatim_quote": "This indicates the presence of remnant HG groups in various non-farmed regions, for example, highlands and uplands or densely forested zones and wetlands and a mosaic of ancestries rather than a genetically uniform CA and EBA Europe.",
        "page": 4,
        "supporting_evidence": ["E084"]
    },
    {
        "id": "C081",
        "content": "Yamnaya migrants traced at Majaky and Boyanovo sites",
        "claim_type": "demographic_interpretation",
        "verbatim_quote": "we can trace the appearance of migrants from the steppe, clearly attributed to Yamnaya culturally and genetically, in the local time transect at Majaky but also at Boyanovo",
        "page": 4,
        "supporting_evidence": ["E085"]
    },
    {
        "id": "C082",
        "content": "Subtle genetic ancestry differences reflect geographical locations and assimilation stages",
        "claim_type": "demographic_interpretation",
        "verbatim_quote": "The subtle differences in genetic ancestries between these two when compared to different Yamnaya-associated groups account for their geographical locations and different stages of genetic and perhaps, cultural assimilation.",
        "page": 4,
        "supporting_evidence": []
    },
    {
        "id": "C083",
        "content": "Occasional admixture occurred between EBA tell inhabitants and incoming steppe pastoralists",
        "claim_type": "demographic_interpretation",
        "verbatim_quote": "Two outlier individuals from EBA YUN and BOY bear witness to occasional admixture between inhabitants of EBA tells and incoming steppe pastoralists.",
        "page": 4,
        "supporting_evidence": ["E086"]
    },
    {
        "id": "C084",
        "content": "Interaction in SEE did not result in archaeologically visible conflicts or near-complete genetic turnover",
        "claim_type": "comparative_interpretation",
        "verbatim_quote": "The interaction between local and incoming groups in SEE did not result in archaeologically visible conflicts or a near-complete autosomal genetic turnover as observed in Britain or a replacement of the Y-chromosome lineages in the Iberian Peninsula36,56.",
        "page": 4,
        "supporting_evidence": []
    }
]

new_implicit_arguments = [
    {
        "id": "IA014",
        "content": "Genetic homogeneity necessarily indicates absence of internal conflicts",
        "argument_type": "interpretive_limitation",
        "trigger_text": "given the near-identical genetic ancestry profiles of SEE CA groups, we caution that genetic analyses would be blind to internal conflicts, causing the replacement of one CA group by another",
        "page": 4,
        "related_claims": ["C072"],
        "rationale": "The authors explicitly acknowledge this limitation, noting that genetic similarity could mask internal conflicts if one CA group replaced another with similar ancestry. This implicit argument recognizes that genetic data cannot distinguish all forms of social/political change - replacement by genetically similar groups would be invisible to archaeogenetic analysis."
    },
    {
        "id": "IA015",
        "content": "Genetic variation patterns directly reflect historical cultural and demographic processes",
        "argument_type": "bridging_assumption",
        "trigger_text": "Moreover, variable cultural influences attested by the archaeological record40,41,53 are also traceable genetically",
        "page": 4,
        "related_claims": ["C077"],
        "rationale": "The claim that cultural influences are 'traceable genetically' assumes correspondence between cultural variation (from archaeology) and genetic variation. This bridges two independent data types assuming they track the same underlying historical processes, without explicit discussion of scenarios where cultural and biological exchange might be decoupled (e.g., cultural diffusion without migration, or migration with cultural assimilation)."
    },
    {
        "id": "IA016",
        "content": "Exchange networks facilitated by contact zones directly caused development of pastoralism",
        "argument_type": "causal_assumption",
        "trigger_text": "We argue that livestock, innovations and technological advances were exchanged through these zones of interaction, which then led to the establishment of fully developed pastoralism",
        "page": 4,
        "related_claims": ["C078"],
        "rationale": "The causal language ('which then led to') implies exchange through contact zones was necessary/sufficient for pastoralist development. This bridges from observing contact (genetic admixture) to technological/economic causation without explicitly addressing alternative scenarios (independent pastoralist development, earlier but archaeologically invisible exchange, or different causal mechanisms)."
    },
    {
        "id": "IA017",
        "content": "Mosaic of ancestries contradicts model of genetically uniform prehistoric Europe",
        "argument_type": "bridging_claim",
        "trigger_text": "and a mosaic of ancestries rather than a genetically uniform CA and EBA Europe",
        "page": 4,
        "related_claims": ["C080"],
        "rationale": "The phrase 'rather than' sets up an implicit alternative model being rejected. This bridges from specific observations (HG ancestry resurgence, remnant HG groups) to a broader claim about European population structure. The implicit argument assumes previous models proposed uniformity, and that the observed variation is inconsistent with such models, without explicitly defining what 'genetically uniform' would mean or citing the models being rejected."
    }
]

# Load, append, update, save
with open('/home/shawn/Code/llm-reproducibility/outputs/penske-et-al-2023/extraction.json', 'r') as f:
    data = json.load(f)

data['evidence'].extend(new_evidence)
data['claims'].extend(new_claims)
data['implicit_arguments'].extend(new_implicit_arguments)

data['extraction_notes']['pass1_chunking']['section6'] = {
    "section_number": 6,
    "section_title": "Discussion",
    "page_range": "4-5",
    "estimated_words": 1200,
    "natural_boundary": "Before 'Methods' section",
    "items_extracted": {
        "evidence": 13,
        "claims": 14,
        "implicit_arguments": 4
    }
}

with open('/home/shawn/Code/llm-reproducibility/outputs/penske-et-al-2023/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Section 6 extraction complete:")
print(f"  Added: {len(new_evidence)} evidence, {len(new_claims)} claims, {len(new_implicit_arguments)} implicit arguments")
print(f"  New totals: {len(data['evidence'])} evidence, {len(data['claims'])} claims, {len(data['implicit_arguments'])} implicit arguments")
