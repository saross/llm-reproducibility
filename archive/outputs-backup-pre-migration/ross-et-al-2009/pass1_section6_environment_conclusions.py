#!/usr/bin/env python3
"""
Pass 1, Section 6: Liberal Claims/Evidence Extraction
Ross et al. 2009 - Remote Sensing and Archaeological Prospection in Apulia, Italy

Section: Environment/Geology + Conclusions (~1100 words, pages 434-437)

Approach: Liberal extraction, cast wide net, aim for over-extraction.
Focus on geological interpretations, environmental factors, and methodological conclusions.
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
        "evidence_id": "E100",
        "content": "The study area comprises a section of the western coastal plain of Apulia, extending inland through the transitional zone to the Murge Tableland.",
        "evidence_type": "environmental_observation",
        "verbatim_quote": "In geological terms, our study area comprises a section of the western coastal plain of Apulia, extending inland through the transitional zone to the Murge Tableland.",
        "page": 435,
        "relevance": "Defines geological context of study area",
        "supports_claims": ["C124"]
    },
    {
        "evidence_id": "E101",
        "content": "The Murge belongs to the Apulian karst and is marked by rolling hills and ridges with an average altitude of 420 masl.",
        "evidence_type": "environmental_observation",
        "verbatim_quote": "The Murge belongs to the Apulian karst and is marked by rolling hills and ridges with an average altitude of 420 masl",
        "page": 435,
        "relevance": "Describes topographic characteristics",
        "supports_claims": ["C125"]
    },
    {
        "evidence_id": "E102",
        "content": "The Murge was formed by tectonic uplift that separated it from the coastal plain and created a network of gravine (canyon-like valleys).",
        "evidence_type": "geological_observation",
        "verbatim_quote": "It was formed by tectonic uplift that separated it from the coastal plain and in the process created a network of gravine, impressive canyon-like valleys",
        "page": 435,
        "relevance": "Explains geological formation process",
        "supports_claims": ["C126"]
    },
    {
        "evidence_id": "E103",
        "content": "The plateau is only marginally exploited, suited neither for olive nor cereal cultivation, with viticulture and orchards in accessible areas.",
        "evidence_type": "land_use_observation",
        "verbatim_quote": "Nowadays, the plateau is only marginally exploited, as it is neither suited for olive nor cereal cultivation. Viticulture and orchards prevail in the accessible areas, while the rest is covered by macchia and pine groves.",
        "page": 435,
        "relevance": "Documents modern land use patterns",
        "supports_claims": ["C127"]
    },
    {
        "evidence_id": "E104",
        "content": "Quaternary sediments display a sandwich profile: two permeable layers (calcarenite sandstone and limestone) bracket an impermeable clay layer.",
        "evidence_type": "geological_observation",
        "verbatim_quote": "Quaternary sediments in the study area display a profile resembling a sandwich: two permeable layers (calcarenite sandstone and limestone) bracket an impermeable clay layer.",
        "page": 435,
        "relevance": "Describes critical geological structure",
        "supports_claims": ["C128"]
    },
    {
        "evidence_id": "E105",
        "content": "Water percolates through upper sandstone, is blocked by clay, and where clay approaches the surface provides low-volume but reliable near-surface water sources.",
        "evidence_type": "hydrological_observation",
        "verbatim_quote": "Water that falls on the surface percolates through the upper sandstone layer and is blocked by the clay (argile di Bradano). Wherever this layer of clay approaches the surface (as a result of uplift and erosion), it provides low-volume but reliable near-surface water sources",
        "page": 435,
        "relevance": "Explains water source mechanism critical for interpretation",
        "supports_claims": ["C129", "C130"]
    },
    {
        "evidence_id": "E106",
        "content": "Such water phenomena are abundant within the study area, especially northeast of Taranto.",
        "evidence_type": "environmental_observation",
        "verbatim_quote": "Such phenomena are abundant within our study area, especially to the NE of Taranto",
        "page": 435,
        "relevance": "Locates water source distribution",
        "supports_claims": ["C131"]
    },
    {
        "evidence_id": "E107",
        "content": "Climate in the Salentine region is meso-Mediterranean and the soil regime is xeric, indicating water deficiency for more than 90 days per year.",
        "evidence_type": "environmental_observation",
        "verbatim_quote": "Climate in the Salentine region is meso-Mediterranean and the soil regime is xeric, indicating water deficiency for more than 90 days a year.",
        "page": 435,
        "relevance": "Establishes water scarcity context",
        "supports_claims": ["C132"]
    },
    {
        "evidence_id": "E108",
        "content": "The Brindisi region mean annual precipitation is 548 mm, but evaporation exceeds precipitation during hot summer months.",
        "evidence_type": "climate_measurement",
        "verbatim_quote": "The Brindisi region mean annual precipitation is 548 mm, but evaporation exceeds precipitation during hot summer months",
        "page": 435,
        "relevance": "Quantifies precipitation-evaporation balance",
        "supports_claims": ["C133"]
    },
    {
        "evidence_id": "E109",
        "content": "Surface material recovered during ground control generally reflected habitation rather than burials.",
        "evidence_type": "archaeological_observation",
        "verbatim_quote": "Surface material recovered during ground control generally reflected habitation rather than burials.",
        "page": 435,
        "relevance": "Documents site type bias in discovery",
        "supports_claims": ["C134"]
    },
    {
        "evidence_id": "E110",
        "content": "In some cases, sites did not lie within features visible in the image, but instead were clustered nearby, particularly for smaller scatters (under 1 ha).",
        "evidence_type": "spatial_observation",
        "verbatim_quote": "In some cases, sites did not lie within features visible in the image, but instead were clustered nearby, a pattern particularly true for smaller scatters (under 1 ha).",
        "page": 435,
        "relevance": "Documents spatial relationship between features and sites",
        "supports_claims": ["C135"]
    },
    {
        "evidence_id": "E111",
        "content": "In relatively moist regions, the majority of sites discovered through field survey were also located through remote sensing along with some new sites.",
        "evidence_type": "comparative_observation",
        "verbatim_quote": "In relatively moist regions, the majority of sites discovered through field survey were also located through remote sensing (along with some \"new\" sites).",
        "page": 435,
        "relevance": "Documents environmental effect on detection success",
        "supports_claims": ["C136"]
    },
    {
        "evidence_id": "E112",
        "content": "Areas lacking near-surface water sources or low soil moisture showed much lower correlation between remote sensing and MTS results, with more false positives and false negatives.",
        "evidence_type": "comparative_observation",
        "verbatim_quote": "Areas lacking near-surface water sources or marked by low soil moisture showed a much lower correlation between our results and those of the MTS, with more false positives and false negatives.",
        "page": 435,
        "relevance": "Documents environmental control on method performance",
        "supports_claims": ["C137"]
    }
]

# ============================================================================
# CLAIMS - Liberal extraction
# ============================================================================

claims_items = [
    {
        "claim_id": "C124",
        "content": "Geological and pedological expertise are essential for conducting archaeological remote sensing focused on buried remains.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Geological and pedological expertise are essential for conducting archaeological remote sensing focused on buried remains",
        "page": 434,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Core methodological requirement claim"
    },
    {
        "claim_id": "C125",
        "content": "Geological and pedological knowledge is key to understanding processes mediating between surface reflectance and subsurface archaeological strata.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "they are the keys to understanding the processes that mediate between the surface, which produces the reflection patterns visible in the image, and subsurface strata potentially containing archaeological remains.",
        "page": 435,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Explains role of earth science knowledge"
    },
    {
        "claim_id": "C126",
        "content": "The geological structure of the Murge region directly affects both ancient settlement patterns and modern remote sensing detection capabilities.",
        "claim_type": "interpretive_claim",
        "verbatim_quote": "The geology and associated water cycle of the Murge region affects the distribution of archaeological remains.",
        "page": 435,
        "supporting_evidence": ["E100", "E101", "E102"],
        "confidence": "high",
        "relevance": "Connects geology to archaeology and detection"
    },
    {
        "claim_id": "C127",
        "content": "Modern marginal exploitation of the Murge affects surface visibility and land cover patterns relevant to remote sensing.",
        "claim_type": "interpretive_claim",
        "verbatim_quote": "Nowadays, the plateau is only marginally exploited... Viticulture and orchards prevail in the accessible areas, while the rest is covered by macchia and pine groves.",
        "page": 435,
        "supporting_evidence": ["E103"],
        "confidence": "medium",
        "relevance": "Explains modern conditions affecting detection"
    },
    {
        "claim_id": "C128",
        "content": "The sandwich structure of permeable-impermeable-permeable sediment layers controls water availability in the study area.",
        "claim_type": "geological_explanation",
        "verbatim_quote": "Quaternary sediments in the study area display a profile resembling a sandwich: two permeable layers (calcarenite sandstone and limestone) bracket an impermeable clay layer.",
        "page": 435,
        "supporting_evidence": ["E104"],
        "confidence": "high",
        "relevance": "Explains hydrological mechanism"
    },
    {
        "claim_id": "C129",
        "content": "Near-surface water sources created by geological structure were critical for ancient settlement location.",
        "claim_type": "interpretive_claim",
        "verbatim_quote": "Wherever this layer of clay approaches the surface (as a result of uplift and erosion), it provides low-volume but reliable near-surface water sources... proved to be important factors in interpreting the satellite imagery for archaeological purposes.",
        "page": 435,
        "supporting_evidence": ["E105"],
        "confidence": "high",
        "relevance": "Links geology to settlement patterns"
    },
    {
        "claim_id": "C130",
        "content": "Geological water sources are readily apparent in multispectral satellite imagery through vegetation and soil moisture effects.",
        "claim_type": "technical_assertion",
        "verbatim_quote": "At the same time, near-surface water sources affect vegetation growth and soil moisture, and as a result are readily apparent in multispectral satellite imagery.",
        "page": 435,
        "supporting_evidence": ["E105"],
        "confidence": "high",
        "relevance": "Explains detection mechanism"
    },
    {
        "claim_id": "C131",
        "content": "The abundance of near-surface water phenomena in the study area made it particularly suitable for this remote sensing approach.",
        "claim_type": "interpretive_claim",
        "verbatim_quote": "Such phenomena are abundant within our study area, especially to the NE of Taranto, and proved to be important factors in interpreting the satellite imagery for archaeological purposes.",
        "page": 435,
        "supporting_evidence": ["E106"],
        "confidence": "medium",
        "relevance": "Explains study area suitability"
    },
    {
        "claim_id": "C132",
        "content": "Water deficiency for more than 90 days per year makes water the limiting resource for habitation.",
        "claim_type": "environmental_assertion",
        "verbatim_quote": "Climate in the Salentine region is meso-Mediterranean and the soil regime is xeric, indicating water deficiency for more than 90 days a year.",
        "page": 435,
        "supporting_evidence": ["E107"],
        "confidence": "high",
        "relevance": "Establishes water as critical factor"
    },
    {
        "claim_id": "C133",
        "content": "During antiquity, access to water was likely the principle factor limiting human habitation in the region.",
        "claim_type": "interpretive_claim",
        "verbatim_quote": "Given these data, it is likely that during antiquity access to water was the principle factor limiting human habitation in the region.",
        "page": 435,
        "supporting_evidence": ["E107", "E108"],
        "confidence": "high",
        "relevance": "Key interpretive claim about settlement determinants"
    },
    {
        "claim_id": "C134",
        "content": "The majority of sites discovered through remote sensing were detected due to association with easily accessible water sources rather than direct detection of structures.",
        "claim_type": "interpretive_claim",
        "verbatim_quote": "Thus, our image analysis mostly revealed locations amenable to human settlement rather than buried archaeological remains. The majority of sites or off-site scatters discovered through remote sensing were detected due to their association with easily accessible sources of water, the limiting resource in the region.",
        "page": 435,
        "supporting_evidence": ["E109"],
        "confidence": "high",
        "relevance": "Core finding about what remote sensing detects"
    },
    {
        "claim_id": "C135",
        "content": "Small settlements or seasonal camps were likely supported by reliable but low-volume near-surface water sources.",
        "claim_type": "interpretive_claim",
        "verbatim_quote": "Reliable but low-volume near-surface sources produced by the geology of the region likely supported small settlements or seasonal camps.",
        "page": 435,
        "supporting_evidence": ["E110"],
        "confidence": "medium",
        "relevance": "Interprets settlement types near water sources"
    },
    {
        "claim_id": "C136",
        "content": "Image analysis was most successful at finding sites in well-watered areas of a broadly xeric region.",
        "claim_type": "methodological_finding",
        "verbatim_quote": "Compared to surface survey, image analysis was most successful at finding sites in well-watered areas of a broadly xeric region",
        "page": 435,
        "supporting_evidence": ["E111"],
        "confidence": "high",
        "relevance": "Identifies environmental control on success"
    },
    {
        "claim_id": "C137",
        "content": "Image analysis produces less successful and more erratic results in areas lacking near-surface water sources.",
        "claim_type": "methodological_finding",
        "verbatim_quote": "Image analysis produced less successful and more erratic results in areas lacking such water sources.",
        "page": 435,
        "supporting_evidence": ["E112"],
        "confidence": "high",
        "relevance": "Identifies environmental limitation on method"
    },
    {
        "claim_id": "C138",
        "content": "Through a combination of propitious factors, image features associated with ancient material generally represent environmental conditions conducive to habitation rather than subsurface remains.",
        "claim_type": "interpretive_synthesis",
        "verbatim_quote": "In short, through a combination of the nature of remote sensing, the propitious date of image capture, the fact that water is the limiting resource in the region, and the particular geological formations that produce near-surface water sources in the study area, image features associated with ancient surface material generally represent environmental conditions conducive to human habitation rather than subsurface archaeological remains.",
        "page": 435,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Synthesizes key interpretation"
    },
    {
        "claim_id": "C139",
        "content": "The project used satellite image analysis to assess a large, archaeologically rich study area quickly and efficiently.",
        "claim_type": "summary_claim",
        "verbatim_quote": "Our project used satellite image analysis based on high-resolution multispectral imagery to assess a large, archaeologically rich study area quickly and efficiently",
        "page": 435,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Summarizes project achievement"
    },
    {
        "claim_id": "C140",
        "content": "The project produced positive associations of image features and artifact scatters at a rate over three times higher than random chance.",
        "claim_type": "effectiveness_claim",
        "verbatim_quote": "extending and complementing the results of surface survey. It produced positive associations of features visible in the satellite image and artifact scatters on the ground at a rate over three times higher than would be expected by random chance.",
        "page": 435,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Restates key effectiveness finding"
    },
    {
        "claim_id": "C141",
        "content": "Most detected features represent environments conducive to settlement (zones of near-surface groundwater or moisture-retaining soils) rather than subsurface remains.",
        "claim_type": "interpretive_claim",
        "verbatim_quote": "Although some of the features identified in the image were the product of subsurface archaeological remains, most represent environments conducive to settlement, particularly zones of near-surface groundwater or moisture-retaining soils.",
        "page": 436,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Restates core interpretation"
    },
    {
        "claim_id": "C142",
        "content": "Image analysis was more successful in places containing near-surface water sources than in uniformly dry areas.",
        "claim_type": "methodological_finding",
        "verbatim_quote": "Image analysis was more successful in places containing such water sources than in uniformly dry areas.",
        "page": 436,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Restates environmental dependency"
    },
    {
        "claim_id": "C143",
        "content": "Habitation sites were more amenable to detection than funerary sites based on surface finds.",
        "claim_type": "methodological_finding",
        "verbatim_quote": "Judging from surface finds, habitation sites were more amenable to detection than funerary sites.",
        "page": 436,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Identifies site type bias"
    },
    {
        "claim_id": "C144",
        "content": "The differential ability to locate various site types in different environments must be considered when assessing remote sensing capacity and limitations.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "The differential ability of satellite image analysis to locate various types of sites in different environments must be considered when assessing its capacity and limitations for archaeological reconnaissance.",
        "page": 436,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Methodological implication for assessment"
    },
    {
        "claim_id": "C145",
        "content": "Image analysis works best in combination with other prospection methods, particularly archaeological surface survey.",
        "claim_type": "methodological_recommendation",
        "verbatim_quote": "Image analysis works best in combination with other methods of prospection, particularly archaeological surface survey.",
        "page": 436,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Core methodological recommendation"
    },
    {
        "claim_id": "C146",
        "content": "Image analysis reflects multiple varying factors including cultural residues, environmental and geological characteristics, land cover propensity, and others that vary by culture and region.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Image analysis reflects a multitude of factors, including the nature of cultural residues present, the environmental and geological characteristics of the study area, the propensity of the land cover to reveal subsurface structures, and other phenomena that vary by culture and region.",
        "page": 436,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Explains complexity of remote sensing"
    },
    {
        "claim_id": "C147",
        "content": "Season and time of day of image acquisition may affect subsurface feature visibility through variations in vegetation growth, soil moisture, and surface reflectance.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "The season and time of day in which the image is taken may affect the visibility of subsurface features through variations in vegetation growth, soil moisture, and surface reflectance.",
        "page": 436,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Identifies temporal factors affecting detection"
    },
    {
        "claim_id": "C148",
        "content": "Differential recovery of archaeological sites argues for remote sensing and systematic surface survey as complementary methods.",
        "claim_type": "methodological_recommendation",
        "verbatim_quote": "In short, remote sensing has its limitations; differential recovery of archaeological sites argues for remote sensing and systematic surface survey as complementary methods of reconnaissance.",
        "page": 436,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Key methodological conclusion"
    },
    {
        "claim_id": "C149",
        "content": "Satellite image analysis still lacks a mature, rigorous, and systematic methodology despite producing results.",
        "claim_type": "methodological_critique",
        "verbatim_quote": "Although satellite image analysis can produce results (in terms of the discovery of sites, even some missed by conventional surface survey) it still lacks a mature, rigorous, and systematic methodology.",
        "page": 436,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Identifies field-wide methodological gap"
    },
    {
        "claim_id": "C150",
        "content": "Image analysis needs to be deployed at larger scale and comprehensively assessed to determine recovery rates and variations across cultures and environments.",
        "claim_type": "methodological_recommendation",
        "verbatim_quote": "Image analysis needs to be deployed on a larger scale and comprehensively assessed to determine rates of site recovery and their variations across different archaeological cultures and natural environments.",
        "page": 436,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Identifies research need"
    },
    {
        "claim_id": "C151",
        "content": "Until large-scale assessment occurs, remote sensing is best used to complement other prospection means such as surface survey.",
        "claim_type": "methodological_recommendation",
        "verbatim_quote": "Until then (and perhaps even after) remote sensing is best used to complement other means of prospection, such as surface survey.",
        "page": 436,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Practical methodological guidance"
    },
    {
        "claim_id": "C152",
        "content": "The project demonstrated that remote sensing allows rapid and efficient identification of some subsurface remains and especially of environmental conditions amenable to ancient habitation.",
        "claim_type": "summary_claim",
        "verbatim_quote": "Despite these limitations, our project has demonstrated that remote sensing allows the rapid and efficient identification of some subsurface archaeological remains and, especially, of particular environmental conditions amenable to ancient habitation.",
        "page": 436,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Summarizes dual capability"
    },
    {
        "claim_id": "C153",
        "content": "One of the most useful applications of archaeological remote sensing may be predicting areas of human activity near critical resources like water in otherwise deficient environments.",
        "claim_type": "methodological_recommendation",
        "verbatim_quote": "These results suggest that one of the most useful applications of archaeological remote sensing may be to predict areas of human activity near places where a critical resource such as water exists in an otherwise deficient environment.",
        "page": 436,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Proposes optimal application scenario"
    },
    {
        "claim_id": "C154",
        "content": "An approach combining surface survey, geological and environmental analysis, site location modeling, and remote sensing will produce a powerful tool for regional archaeological prospection.",
        "claim_type": "methodological_recommendation",
        "verbatim_quote": "An approach which combines surface survey, geological and environmental analysis, site location modeling, and remote sensing will produce a powerful tool for regional archaeological prospection.",
        "page": 437,
        "supporting_evidence": [],
        "confidence": "high",
        "relevance": "Proposes integrated methodological framework"
    }
]

# ============================================================================
# IMPLICIT ARGUMENTS
# ============================================================================

implicit_arguments = [
    {
        "implicit_argument_id": "IA027",
        "content": "Detecting environmental suitability for habitation is valuable for archaeology even when subsurface remains aren't directly detected (implied by framing this as useful finding rather than failure).",
        "argument_type": "unstated_value_judgment",
        "trigger_text": "image features associated with ancient surface material generally represent environmental conditions conducive to human habitation rather than subsurface archaeological remains",
        "page": 435,
        "reconstruction_confidence": "high",
        "related_claims": ["C134", "C138", "C141"],
        "critical_for_logic": True,
        "notes": "Reframes indirect detection as positive finding"
    },
    {
        "implicit_argument_id": "IA028",
        "content": "Ancient settlement patterns were primarily determined by water availability in xeric environments (implied by using water to explain site locations).",
        "argument_type": "unstated_premise",
        "trigger_text": "it is likely that during antiquity access to water was the principle factor limiting human habitation in the region",
        "page": 435,
        "reconstruction_confidence": "high",
        "related_claims": ["C133", "C134"],
        "critical_for_logic": True,
        "notes": "Environmental determinism of settlement patterns"
    },
    {
        "implicit_argument_id": "IA029",
        "content": "Ancient water needs and sources were similar to modern hydrology patterns (implied by using modern geological water sources to explain ancient settlement).",
        "argument_type": "uniformitarian_assumption",
        "trigger_text": "near-surface water sources... proved to be important factors in interpreting the satellite imagery for archaeological purposes",
        "page": 435,
        "reconstruction_confidence": "medium",
        "related_claims": ["C129", "C130"],
        "critical_for_logic": True,
        "notes": "Assumes geological water sources stable over time"
    },
    {
        "implicit_argument_id": "IA030",
        "content": "The limitations identified are intrinsic to remote sensing, not specific to this study's implementation (implied by generalizing to method recommendations).",
        "argument_type": "unstated_premise",
        "trigger_text": "remote sensing has its limitations; differential recovery of archaeological sites argues for remote sensing and systematic surface survey as complementary methods",
        "page": 436,
        "reconstruction_confidence": "medium",
        "related_claims": ["C144", "C145", "C148"],
        "critical_for_logic": False,
        "notes": "Generalizes from specific study to method-level conclusions"
    },
    {
        "implicit_argument_id": "IA031",
        "content": "Complementarity between methods adds more value than either method alone (implied by advocating integration).",
        "argument_type": "unstated_premise",
        "trigger_text": "An approach which combines surface survey, geological and environmental analysis, site location modeling, and remote sensing will produce a powerful tool",
        "page": 437,
        "reconstruction_confidence": "high",
        "related_claims": ["C154"],
        "critical_for_logic": True,
        "notes": "Synergistic integration assumption"
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
    'section': 'Section 6: Environment/Geology + Conclusions',
    'pages': '434-437',
    'word_count_estimate': 1100,
    'items_extracted': {
        'evidence': len(evidence_items),
        'claims': len(claims_items),
        'implicit_arguments': len(implicit_arguments)
    },
    'notes': 'Final section with extensive interpretation and synthesis. Extracted geological/environmental evidence and many interpretive claims about what features represent. Conclusions section rich with methodological recommendations and research directions. Completes Pass 1 liberal extraction.'
})

# Add Pass 1 completion note
data['extraction_notes']['pass1_complete'] = {
    'completion_date': datetime.now(timezone.utc).isoformat(),
    'total_sections': 6,
    'total_items': len(data['evidence']) + len(data['claims']) + len(data['implicit_arguments']),
    'breakdown': {
        'evidence': len(data['evidence']),
        'claims': len(data['claims']),
        'implicit_arguments': len(data['implicit_arguments'])
    },
    'notes': 'Liberal extraction complete across all 6 sections. Over-extracted as per strategy (40-50% more than expected final count). Ready for Pass 2 rationalization.'
}

with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print(f"✓ Pass 1, Section 6 complete: Environment/Geology + Conclusions")
print(f"  - Evidence items: {len(evidence_items)}")
print(f"  - Claims: {len(claims_items)}")
print(f"  - Implicit arguments: {len(implicit_arguments)}")
print(f"  - Total items this section: {len(evidence_items) + len(claims_items) + len(implicit_arguments)}")
print(f"")
print(f"=" * 60)
print(f"PASS 1 COMPLETE - Liberal Claims/Evidence Extraction")
print(f"=" * 60)
print(f"  - Total evidence: {len(data['evidence'])}")
print(f"  - Total claims: {len(data['claims'])}")
print(f"  - Total implicit arguments: {len(data['implicit_arguments'])}")
print(f"  - GRAND TOTAL: {len(data['evidence']) + len(data['claims']) + len(data['implicit_arguments'])} items")
print(f"=" * 60)
