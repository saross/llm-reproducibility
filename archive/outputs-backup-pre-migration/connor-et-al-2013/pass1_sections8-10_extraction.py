#!/usr/bin/env python3
"""
Pass 1: Liberal Extraction - Sections 8-10 (Chronology and Results)
Connor et al. 2013 - Environmental conditions in SE Balkans since LGM

Liberal over-extraction approach: 40-50% over expected targets
Sections: Chronology, Sediment description and mineral magnetics, Numerical analyses and pollen stratigraphy (start)
"""

import json

# Load current extraction
with open('/home/shawn/Code/llm-reproducibility/outputs/connor-et-al-2013/extraction.json', 'r') as f:
    data = json.load(f)

# SECTION 8: Chronology (pages 9-10)
section8_items = [
    # Evidence items
    {
        "id": "E053",
        "content": "Thirteen Accelerator Mass Spectrometer radiocarbon dates obtained for Straldzha profiles",
        "evidence_type": "chronological_data",
        "page": 9,
        "verbatim_quote": "Thirteen Accelerator Mass Spectrometer radiocarbon dates were obtained for the Straldzha profiles.",
        "supports_claims": ["C061"]
    },
    {
        "id": "E054",
        "content": "Five radiocarbon determinations made on pollen concentrates using ANSTO procedure based on Brown et al. (1989) due to absence of macrobotanical material",
        "evidence_type": "methodological_detail",
        "page": 9,
        "verbatim_quote": "In the absence of macrobotanical material for dating, five of the radiocarbon determinations were made on pollen concentrates extracted using the Australian Nuclear Science and Technology Organisation's procedure based on Brown et al. (1989).",
        "supports_claims": ["C062"]
    },
    {
        "id": "E055",
        "content": "Remaining samples cleaned to remove rootlets, pre-treated by acid washing in dilute HCl, then organic residues dated",
        "evidence_type": "laboratory_procedure",
        "page": 9,
        "verbatim_quote": "The remaining samples were cleaned to remove rootlets and pre-treated by acid washing in dilute HCl, then organic residues were dated.",
        "supports_claims": ["C062"]
    },
    {
        "id": "E056",
        "content": "Age-depth model constructed using Markov chain Monte-Carlo analysis, Bayesian statistical approach in OxCal 4.1.7 based on IntCal09 calibration curve",
        "evidence_type": "analytical_procedure",
        "page": 9,
        "verbatim_quote": "An age-depth model was constructed for the quarry section using Markov chain Monte-Carlo analysis, a Bayesian statistical approach to age modelling implemented in OxCal 4.1.7 (Bronk Ramsey, 2009), based on the IntCal09 calibration curve (Reimer et al., 2009).",
        "supports_claims": ["C063"]
    },
    {
        "id": "E057",
        "content": "Age-depth model extended by linear extrapolation to cover entire quarry section",
        "evidence_type": "analytical_procedure",
        "page": 9,
        "verbatim_quote": "The age-depth model was extended by linear extrapolation to cover the entire quarry section (Fig. 3).",
        "supports_claims": ["C063"]
    },
    {
        "id": "E058",
        "content": "Sediment accumulation rates from upper part of record applied to upper metre of canal core",
        "evidence_type": "analytical_procedure",
        "page": 9,
        "verbatim_quote": "Sediment accumulation rates in the upper part of the record were also applied to the upper metre of the canal core.",
        "supports_claims": ["C064"]
    },
    {
        "id": "E059",
        "content": "Lowermost sample in core statistically matched with beginning of palaeovegetation phase 4, intervening ages interpolated from AMS date at 110-cm depth",
        "evidence_type": "chronological_data",
        "page": 9,
        "verbatim_quote": "The lowermost sample in the core was statistically matched with the beginning of palaeovegetation phase 4 (Section 3.2) and the intervening ages interpolated from the AMS date at 110-cm depth (Fig. 3).",
        "supports_claims": ["C064"]
    },

    # Claims
    {
        "id": "C061",
        "content": "Comprehensive radiocarbon dating strategy employed using 13 AMS dates across Straldzha profiles",
        "claim_type": "methodological",
        "page": 9,
        "verbatim_quote": "Thirteen Accelerator Mass Spectrometer radiocarbon dates were obtained for the Straldzha profiles.",
        "supported_by_evidence": ["E053"]
    },
    {
        "id": "C062",
        "content": "Multiple dating materials used including pollen concentrates and organic residues to establish chronology",
        "claim_type": "methodological",
        "page": 9,
        "verbatim_quote": "In the absence of macrobotanical material for dating, five of the radiocarbon determinations were made on pollen concentrates extracted using the Australian Nuclear Science and Technology Organisation's procedure based on Brown et al. (1989). The remaining samples were cleaned to remove rootlets and pre-treated by acid washing in dilute HCl, then organic residues were dated.",
        "supported_by_evidence": ["E054", "E055"]
    },
    {
        "id": "C063",
        "content": "Bayesian age-depth modelling provides robust chronological framework for quarry section",
        "claim_type": "methodological",
        "page": 9,
        "verbatim_quote": "An age-depth model was constructed for the quarry section using Markov chain Monte-Carlo analysis, a Bayesian statistical approach to age modelling implemented in OxCal 4.1.7 (Bronk Ramsey, 2009), based on the IntCal09 calibration curve (Reimer et al., 2009).",
        "supported_by_evidence": ["E056", "E057"]
    },
    {
        "id": "C064",
        "content": "Canal core chronology established through combination of sediment accumulation rates and statistical correlation with quarry section",
        "claim_type": "methodological",
        "page": 9,
        "verbatim_quote": "Sediment accumulation rates in the upper part of the record were also applied to the upper metre of the canal core. The lowermost sample in the core was statistically matched with the beginning of palaeovegetation phase 4 (Section 3.2) and the intervening ages interpolated from the AMS date at 110-cm depth (Fig. 3).",
        "supported_by_evidence": ["E058", "E059"]
    }
]

# SECTION 9: Sediment description and mineral magnetics (page 10)
section9_items = [
    # Evidence items
    {
        "id": "E060",
        "content": "Most important sedimentary change occurred around 125 cm in quarry section: grey to orange-brown oxidising sediments (Unit III) overlaid by darker peaty silts and lighter lake marls (Units IV and V)",
        "evidence_type": "sedimentological_observation",
        "page": 10,
        "verbatim_quote": "The most important change in the sedimentary sequence occurred around 125 cm in the quarry section, where the grey to orange-brown sediments laid down under oxidising conditions (Unit III) were overlaid by darker peaty silts and lighter lake marls (Units IV and V).",
        "supports_claims": ["C065"]
    },
    {
        "id": "E061",
        "content": "Unit VII ~25 cm thicker in western part of Straldzha Mire compared to east, completely lost in several fields near quarry exposing underlying marl",
        "evidence_type": "sedimentological_observation",
        "page": 10,
        "verbatim_quote": "Additional cores collected near drainage canals showed Unit VII to be ~25 cm thicker in the western part of the Straldzha Mire compared to the east. In several fields near the quarry this top layer has been lost completely, exposing the underlying light-grey marl (Unit VI).",
        "supports_claims": ["C066"]
    },
    {
        "id": "E062",
        "content": "Magnetic susceptibility exhibits medium variable values (0.31–0.15×10⁻⁶ m³/kg) in silty units (I–III), low stable values (0.11–0.08×10⁻⁶ m³/kg) in marl sediments (IV–VI, VII in canal), very high values (1.25–0.64×10⁻⁶ m³/kg) in disturbed surface sediments",
        "evidence_type": "geophysical_measurement",
        "page": 10,
        "verbatim_quote": "Magnetic susceptibility measurements (XLF; Fig. 4) broadly follow lithological changes, exhibiting medium and variable values (0.31–0.15×10-6m3kg-1) in the silty units (I–III), low and stable values (0.11–0.08×10-6m3kg-1) in the marl sediments (IV–VI, and VII in the canal core) and very high values (1.25–0.64×10-6m3kg-1) in the disturbed surface sediments (Unit VII in the quarry record; Unit VIII in the canal core).",
        "supports_claims": ["C067"]
    },
    {
        "id": "E063",
        "content": "Magnetic mineralogy dominated by varying proportions of: (1) authigenic and detrital ferrimagnetic material (principally magnetite), and (2) paramagnetic material mainly from unoxidised iron-bearing clay minerals",
        "evidence_type": "geophysical_measurement",
        "page": 10,
        "verbatim_quote": "The magnetic mineralogy of the Straldzha sediments is dominated by varying proportions of: (1) authigenic and detrital ferrimagnetic material, principally magnetite, and (2) paramagnetic material that is mainly due to the presence of paramagnetic iron-bearing, but generally unoxidised, clay minerals (see supplementary information and Table 1).",
        "supports_claims": ["C068"]
    },
    {
        "id": "E064",
        "content": "Basal silt units have higher amounts of ferrimagnetic material (magnetite and maghaemite of likely detrital origin); marls have very little ferrimagnetic material and dominated by paramagnetic material (possibly authigenic)",
        "evidence_type": "geophysical_measurement",
        "page": 10,
        "verbatim_quote": "The basal silt units have much higher amounts of ferrimagnetic material, consisting of both magnetite and maghaemite of likely detrital origin. The marls have very little ferrimagnetic material and are dominated by paramagnetic material, possibly authigenic.",
        "supports_claims": ["C068", "C069"]
    },
    {
        "id": "E065",
        "content": "Disturbed surface sediments dominated by large amounts of ultra-fine grained magnetite consistent with ferrimagnetic enhancement via pedogenesis",
        "evidence_type": "geophysical_measurement",
        "page": 10,
        "verbatim_quote": "The disturbed surface sediments are dominated by large amounts of ultra-fine grained magnetite, consistent with ferrimagnetic enhancement via pedogenesis.",
        "supports_claims": ["C070"]
    },

    # Claims
    {
        "id": "C065",
        "content": "Major environmental transition at 125 cm depth marks shift from oxidising terrestrial conditions to lacustrine deposition",
        "claim_type": "environmental_interpretation",
        "page": 10,
        "verbatim_quote": "The most important change in the sedimentary sequence occurred around 125 cm in the quarry section, where the grey to orange-brown sediments laid down under oxidising conditions (Unit III) were overlaid by darker peaty silts and lighter lake marls (Units IV and V).",
        "supported_by_evidence": ["E060"]
    },
    {
        "id": "C066",
        "content": "Canal core provides more complete representation of upper sedimentary sequence than quarry section due to variable truncation and disturbance",
        "claim_type": "interpretive",
        "page": 10,
        "verbatim_quote": "In several fields near the quarry this top layer has been lost completely, exposing the underlying light-grey marl (Unit VI). The canal core is more likely to represent the full sedimentary sequence of this unit.",
        "supported_by_evidence": ["E061"]
    },
    {
        "id": "C067",
        "content": "Magnetic susceptibility variations closely track lithological changes across sedimentary sequence",
        "claim_type": "interpretive",
        "page": 10,
        "verbatim_quote": "Magnetic susceptibility measurements (XLF; Fig. 4) broadly follow lithological changes, exhibiting medium and variable values (0.31–0.15×10-6m3kg-1) in the silty units (I–III), low and stable values (0.11–0.08×10-6m3kg-1) in the marl sediments (IV–VI, and VII in the canal core) and very high values (1.25–0.64×10-6m3kg-1) in the disturbed surface sediments",
        "supported_by_evidence": ["E062"]
    },
    {
        "id": "C068",
        "content": "Contrasting magnetic mineralogy between basal silts and marls reflects different depositional environments and sediment sources",
        "claim_type": "environmental_interpretation",
        "page": 10,
        "verbatim_quote": "The basal silt units have much higher amounts of ferrimagnetic material, consisting of both magnetite and maghaemite of likely detrital origin. The marls have very little ferrimagnetic material and are dominated by paramagnetic material, possibly authigenic.",
        "supported_by_evidence": ["E063", "E064"]
    },
    {
        "id": "C069",
        "content": "Shift from detrital to authigenic magnetic mineral dominance marks transition in sediment sources and formation processes",
        "claim_type": "environmental_interpretation",
        "page": 10,
        "verbatim_quote": "The basal silt units have much higher amounts of ferrimagnetic material, consisting of both magnetite and maghaemite of likely detrital origin. The marls have very little ferrimagnetic material and are dominated by paramagnetic material, possibly authigenic.",
        "supported_by_evidence": ["E064"]
    },
    {
        "id": "C070",
        "content": "High magnetic susceptibility in surface sediments directly related to mire drainage and subsequent pedogenesis",
        "claim_type": "environmental_interpretation",
        "page": 10,
        "verbatim_quote": "The disturbed surface sediments are dominated by large amounts of ultra-fine grained magnetite, consistent with ferrimagnetic enhancement via pedogenesis. High magnetic susceptibility is related to the draining of the mire.",
        "supported_by_evidence": ["E065"]
    }
]

# SECTION 10: Numerical analyses and pollen stratigraphy (start) (pages 10-11)
section10_items = [
    # Evidence items
    {
        "id": "E066",
        "content": "Variable pollen preservation in sediments attributed to alkalinity, continental climate, and artificial drainage decades ago",
        "evidence_type": "taphonomic_observation",
        "page": 11,
        "verbatim_quote": "Like the core of Tonkov et al. (2008a, 2009), collected nearby, pollen preservation in the sediments was variable. We attribute this to the alkalinity of the sediments, the continental climate and the fact that the wetland was artificially drained some decades ago.",
        "supports_claims": ["C071"]
    },
    {
        "id": "E067",
        "content": "Cluster analysis used to group pollen record into five palaeovegetation phases, names based on assumed ecological preferences of indicator taxa",
        "evidence_type": "analytical_procedure",
        "page": 11,
        "verbatim_quote": "Cluster analysis (Fig. 5; supplementary information) was used to group the pollen record into five palaeovegetation phases (Fig. 4), the names of which are based on the assumed ecological preferences of the indicator taxa listed in Table 2.",
        "supports_claims": ["C072"]
    },
    {
        "id": "E068",
        "content": "DCA axes 1 and 2 explain 46% and 20% of variance respectively, producing results in strong agreement with cluster analysis",
        "evidence_type": "statistical_result",
        "page": 11,
        "verbatim_quote": "DCA axes 1 and 2 explain 46% and 20% of variance respectively and produced results in strong agreement with the cluster analysis (supplementary information).",
        "supports_claims": ["C072", "C073"]
    },
    {
        "id": "E069",
        "content": "Axis 1 gives high scores to samples abundant in deciduous tree taxa (especially Quercus) and low scores to samples with abundant coniferous taxa (especially Pinus)",
        "evidence_type": "statistical_result",
        "page": 11,
        "verbatim_quote": "Axis 1 gives high scores to samples abundant in deciduous tree taxa (especially Quercus) and low scores to samples with abundant coniferous taxa (especially Pinus).",
        "supports_claims": ["C073"]
    },
    {
        "id": "E070",
        "content": "Axis 2 gives high scores to samples with abundant tree taxa and low scores to most important xerophytic taxa (Chenopodiaceae and Artemisia)",
        "evidence_type": "statistical_result",
        "page": 11,
        "verbatim_quote": "Axis 2 gives high scores to samples with abundant tree taxa and low scores to the most important xerophytic taxa, Chenopodiaceae and Artemisia.",
        "supports_claims": ["C074"]
    },
    {
        "id": "E071",
        "content": "Cold steppe phase (517.5–167.5 cm) dominated by Artemisia (24–37%) and Poaceae (8–25%), with Chenopodiaceae, Ranunculus-type and Polygonum aviculare-type well represented",
        "evidence_type": "pollen_assemblage",
        "page": 11,
        "verbatim_quote": "The lowermost zone is dominated by the pollen of herbs and grasses, with an abundance of Artemisia (24–37%) and Poaceae (8–25%). Chenopodiaceae, Ranunculus-type and Polygonum aviculare-type are well represented.",
        "supports_claims": ["C075"]
    },
    {
        "id": "E072",
        "content": "Pinus most abundant arboreal pollen type (3–26%) in cold steppe phase, but Quercus, Betula, Juniperus and Celtis also occur throughout",
        "evidence_type": "pollen_assemblage",
        "page": 11,
        "verbatim_quote": "Pinus is the most abundant arboreal pollen type (3–26%), but Quercus, Betula, Juniperus and Celtis also occur throughout.",
        "supports_claims": ["C075", "C076"]
    },
    {
        "id": "E073",
        "content": "Pediastrum abundant (up to 12 times terrestrial pollen sum) in cold steppe phase",
        "evidence_type": "pollen_assemblage",
        "page": 11,
        "verbatim_quote": "Pediastrum is abundant (up to 12 times the terrestrial pollen sum).",
        "supports_claims": ["C077"]
    },
    {
        "id": "E074",
        "content": "Semidesert phase (167.5–105 cm): Artemisia and arboreal pollen decline at beginning, Chenopodiaceae rises to completely dominate assemblage (58–69%)",
        "evidence_type": "pollen_assemblage",
        "page": 11,
        "verbatim_quote": "At the beginning of the second zone, Artemisia and arboreal pollen decline and Chenopodiaceae rises to a peak, completely dominating the pollen assemblage (58–69%).",
        "supports_claims": ["C078"]
    },
    {
        "id": "E075",
        "content": "Toward end of semidesert phase, arboreal pollen begins resurgence led by Quercus, Corylus and Ulmus",
        "evidence_type": "pollen_assemblage",
        "page": 11,
        "verbatim_quote": "Toward the end of the zone, arboreal pollen begins a resurgence led by Quercus, Corylus and Ulmus.",
        "supports_claims": ["C079"]
    },

    # Claims
    {
        "id": "C071",
        "content": "Pollen preservation affected by multiple factors including sediment chemistry, climate, and recent anthropogenic disturbance",
        "claim_type": "taphonomic_interpretation",
        "page": 11,
        "verbatim_quote": "Like the core of Tonkov et al. (2008a, 2009), collected nearby, pollen preservation in the sediments was variable. We attribute this to the alkalinity of the sediments, the continental climate and the fact that the wetland was artificially drained some decades ago.",
        "supported_by_evidence": ["E066"]
    },
    {
        "id": "C072",
        "content": "Statistical analysis identifies five distinct palaeovegetation phases in Straldzha record with ecologically meaningful indicator taxa",
        "claim_type": "analytical_interpretation",
        "page": 11,
        "verbatim_quote": "Cluster analysis (Fig. 5; supplementary information) was used to group the pollen record into five palaeovegetation phases (Fig. 4), the names of which are based on the assumed ecological preferences of the indicator taxa listed in Table 2. DCA axes 1 and 2 explain 46% and 20% of variance respectively and produced results in strong agreement with the cluster analysis",
        "supported_by_evidence": ["E067", "E068"]
    },
    {
        "id": "C073",
        "content": "DCA Axis 1 reflects winter temperature and/or rainfall seasonality gradient based on present-day ecology and distribution of represented tree species",
        "claim_type": "climatic_interpretation",
        "page": 11,
        "verbatim_quote": "Axis 1 gives high scores to samples abundant in deciduous tree taxa (especially Quercus) and low scores to samples with abundant coniferous taxa (especially Pinus). Given the present-day ecology and distribution of the tree species represented, this axis perhaps best reflects a winter temperature and/or rainfall seasonality gradient.",
        "supported_by_evidence": ["E068", "E069"]
    },
    {
        "id": "C074",
        "content": "DCA Axis 2 represents moisture gradient from tree-dominated to xerophytic vegetation",
        "claim_type": "climatic_interpretation",
        "page": 11,
        "verbatim_quote": "Axis 2 gives high scores to samples with abundant tree taxa and low scores to the most important xerophytic taxa, Chenopodiaceae and Artemisia. This axis is thus most easily attributed to a moisture gradient.",
        "supported_by_evidence": ["E070"]
    },
    {
        "id": "C075",
        "content": "Cold steppe phase characterized by herb and grass dominance with low but persistent arboreal presence",
        "claim_type": "vegetation_reconstruction",
        "page": 11,
        "verbatim_quote": "The lowermost zone is dominated by the pollen of herbs and grasses, with an abundance of Artemisia (24–37%) and Poaceae (8–25%). Chenopodiaceae, Ranunculus-type and Polygonum aviculare-type are well represented. Pinus is the most abundant arboreal pollen type (3–26%), but Quercus, Betula, Juniperus and Celtis also occur throughout.",
        "supported_by_evidence": ["E071", "E072"]
    },
    {
        "id": "C076",
        "content": "Presence of deciduous tree pollen in cold steppe phase indicates refugial populations persisted in region during glacial conditions",
        "claim_type": "ecological_interpretation",
        "page": 11,
        "verbatim_quote": "Pinus is the most abundant arboreal pollen type (3–26%), but Quercus, Betula, Juniperus and Celtis also occur throughout.",
        "supported_by_evidence": ["E072"]
    },
    {
        "id": "C077",
        "content": "High Pediastrum abundance indicates substantial aquatic habitat presence during cold steppe phase",
        "claim_type": "environmental_interpretation",
        "page": 11,
        "verbatim_quote": "Pediastrum is abundant (up to 12 times the terrestrial pollen sum).",
        "supported_by_evidence": ["E073"]
    },
    {
        "id": "C078",
        "content": "Semidesert phase represents major environmental shift to extreme aridity with Chenopodiaceae-dominated vegetation",
        "claim_type": "environmental_interpretation",
        "page": 11,
        "verbatim_quote": "At the beginning of the second zone, Artemisia and arboreal pollen decline and Chenopodiaceae rises to a peak, completely dominating the pollen assemblage (58–69%).",
        "supported_by_evidence": ["E074"]
    },
    {
        "id": "C079",
        "content": "Late semidesert phase marks beginning of Holocene afforestation process with resurgence of deciduous trees",
        "claim_type": "vegetation_interpretation",
        "page": 11,
        "verbatim_quote": "Toward the end of the zone, arboreal pollen begins a resurgence led by Quercus, Corylus and Ulmus.",
        "supported_by_evidence": ["E075"]
    }
]

# Combine all items from sections 8-10
all_items = section8_items + section9_items + section10_items

# Separate evidence and claims
evidence = [item for item in all_items if item['id'].startswith('E')]
claims = [item for item in all_items if item['id'].startswith('C')]

# Add to extraction
data['evidence'].extend(evidence)
data['claims'].extend(claims)

# Update extraction notes
if 'pass1_sections8-10' not in data.get('extraction_notes', {}):
    if 'extraction_notes' not in data:
        data['extraction_notes'] = {}
    data['extraction_notes']['pass1_sections8-10'] = {
        "completion_date": "2025-10-30",
        "sections_covered": "Chronology (2.4), Sediment description and mineral magnetics (3.1), Numerical analyses and pollen stratigraphy start (3.2)",
        "pages": "9-11",
        "items_extracted": len(all_items),
        "notes": "Chronology, sedimentology, mineral magnetics, and beginning of pollen stratigraphy results. Liberal extraction following 40-50% over-extraction approach."
    }

# Save
with open('/home/shawn/Code/llm-reproducibility/outputs/connor-et-al-2013/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Pass 1 Sections 8-10 Extraction Complete!")
print(f"\nItems Extracted:")
print(f"  Evidence: {len(evidence)}")
print(f"  Claims: {len(claims)}")
print(f"  Total: {len(all_items)}")
print(f"\nRunning Totals:")
print(f"  Evidence: {len(data['evidence'])}")
print(f"  Claims: {len(data['claims'])}")
print(f"  Total: {len(data['evidence']) + len(data['claims'])}")
print(f"\nSections completed: 1-10 of 13")
print(f"Ready for Sections 11-13 extraction (Results sections)")
