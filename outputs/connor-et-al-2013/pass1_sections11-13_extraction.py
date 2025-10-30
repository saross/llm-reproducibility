#!/usr/bin/env python3
"""
Pass 1: Liberal Extraction - Sections 11-13 (Final Results & Early Discussion)
Connor et al. 2013 - Environmental conditions in the SE Balkans

Section 11: Pollen stratigraphy continuation (3.2.3-3.2.5) - pages 11-12
Section 12: Age-depth model (3.3) - page 13
Section 13: Discussion - Late Quaternary vegetation (4.1-4.1.1) - pages 13-14

Liberal over-extraction approach: Extract 40-50% more items than expected
Target for sections 11-13: ~40-50 items
"""

import json

# Load current extraction
with open('/home/shawn/Code/llm-reproducibility/outputs/connor-et-al-2013/extraction.json', 'r') as f:
    data = json.load(f)

# Evidence items (E076-E115 estimated)
new_evidence = [
    # Section 11: Pollen stratigraphy continuation (3.2.3-3.2.5)
    {
        "id": "E076",
        "content": "Suite of grassland taxa (Allium, Centaurea, Dipsacus, Filipendula-type, Galium-type, Heracleum-type, Sanguisorba minor) increases in forest-steppe phase against background of slowly rising Quercus values",
        "evidence_type": "pollen_assemblage",
        "page": 12,
        "verbatim_quote": "A suite of grassland taxa (e.g. Allium, Centaurea, Dipsacus, Filipendula-type, Galium-type, Heracleum-type, Sanguisorba minor) increases in the third zone against a background of slowly rising Quercus values and the constant presence (<1%) of Pistacia.",
        "supports_claims": ["C080"]
    },
    {
        "id": "E077",
        "content": "Constant presence of Pistacia (<1%) throughout forest-steppe phase",
        "evidence_type": "pollen_observation",
        "page": 12,
        "verbatim_quote": "A suite of grassland taxa (e.g. Allium, Centaurea, Dipsacus, Filipendula-type, Galium-type, Heracleum-type, Sanguisorba minor) increases in the third zone against a background of slowly rising Quercus values and the constant presence (<1%) of Pistacia.",
        "supports_claims": ["C081"]
    },
    {
        "id": "E078",
        "content": "Spores of dung-inhabiting fungi (Sporormiella and Sordaria) and charred particles decline through forest-steppe phase",
        "evidence_type": "non_pollen_palynomorphs",
        "page": 12,
        "verbatim_quote": "Spores of dung-inhabiting fungi (Sporormiella and Sordaria) and charred particles decline through this zone.",
        "supports_claims": ["C082"]
    },
    {
        "id": "E079",
        "content": "Quercus increases rapidly in oak woods phase, reaching highest proportions for entire record (up to 52%)",
        "evidence_type": "pollen_percentage",
        "page": 12,
        "verbatim_quote": "Quercus increases rapidly in the fourth zone, this time reaching its highest proportions for the entire record (up to 52%).",
        "supports_claims": ["C083"]
    },
    {
        "id": "E080",
        "content": "Average pollen concentrations of Quercus are three times higher in oak woods phase than in previous zone",
        "evidence_type": "pollen_concentration",
        "page": 12,
        "verbatim_quote": "Average pollen concentrations of Quercus are three times higher than in the previous zone, while Ulmus and Corylus concentrations double (supplementary information).",
        "supports_claims": ["C083"]
    },
    {
        "id": "E081",
        "content": "Ulmus and Corylus concentrations double in oak woods phase compared to forest-steppe phase",
        "evidence_type": "pollen_concentration",
        "page": 12,
        "verbatim_quote": "Average pollen concentrations of Quercus are three times higher than in the previous zone, while Ulmus and Corylus concentrations double (supplementary information).",
        "supports_claims": ["C083"]
    },
    {
        "id": "E082",
        "content": "Charcoal, Chenopodiaceae, grassland taxa and dung fungal spores reduced during oak woods phase",
        "evidence_type": "pollen_and_charcoal",
        "page": 12,
        "verbatim_quote": "Charcoal, Chenopodiaceae, grassland taxa and dung fungal spores are reduced.",
        "supports_claims": ["C084"]
    },
    {
        "id": "E083",
        "content": "Potomogeton and Pediastrum occur throughout oak woods phase",
        "evidence_type": "aquatic_indicators",
        "page": 12,
        "verbatim_quote": "Potomogeton and Pediastrum occur throughout.",
        "supports_claims": ["C085"]
    },
    {
        "id": "E084",
        "content": "Deforestation phase shows sharp decline in Quercus, Corylus and Ulmus, and increase in charred particles, dung fungal spores, Poaceae and Plantago lanceolata-type",
        "evidence_type": "pollen_assemblage_change",
        "page": 12,
        "verbatim_quote": "The final zone shows a sharp decline in Quercus, Corylus and Ulmus, and an increase in charred particles, dung fungal spores, Poaceae and Plantago lanceolata-type.",
        "supports_claims": ["C086"]
    },
    {
        "id": "E085",
        "content": "Canal core indicates deforestation was preceded by late succession of Fagus and Carpinus",
        "evidence_type": "pollen_succession",
        "page": 12,
        "verbatim_quote": "The canal core, which is regarded as a more complete representation of this phase, indicates that deforestation was preceded by the late succession of Fagus and Carpinus and followed by considerable peaks in Salix, Alnus and fern spores, and a temporary recovery of Quercus.",
        "supports_claims": ["C087"]
    },
    {
        "id": "E086",
        "content": "Deforestation followed by considerable peaks in Salix, Alnus and fern spores, and temporary recovery of Quercus",
        "evidence_type": "pollen_succession",
        "page": 12,
        "verbatim_quote": "The canal core, which is regarded as a more complete representation of this phase, indicates that deforestation was preceded by the late succession of Fagus and Carpinus and followed by considerable peaks in Salix, Alnus and fern spores, and a temporary recovery of Quercus.",
        "supports_claims": ["C088"]
    },
    {
        "id": "E087",
        "content": "At end of deforestation phase, Salix, Alnus, fern spores and Quercus decrease when Chenopodiaceae, Triticum-type and macroscopic charcoal increase",
        "evidence_type": "pollen_and_charcoal",
        "page": 12,
        "verbatim_quote": "All of these taxa decrease toward the end of the zone, when Chenopodiaceae, Triticum-type and macroscopic charcoal increase.",
        "supports_claims": ["C089"]
    },

    # Section 12: Age-depth model (3.3)
    {
        "id": "E088",
        "content": "Thirteen Accelerator Mass Spectrometer radiocarbon dates obtained for Straldzha profiles",
        "evidence_type": "chronology",
        "page": 13,
        "verbatim_quote": "Radiocarbon dating results are provided in Table 3. Three dated points were initially excluded from the age-depth model, having both low organic content and large error margins.",
        "supports_claims": ["C090"]
    },
    {
        "id": "E089",
        "content": "Three dated points initially excluded from age-depth model due to low organic content and large error margins",
        "evidence_type": "chronology",
        "page": 13,
        "verbatim_quote": "Radiocarbon dating results are provided in Table 3. Three dated points were initially excluded from the age-depth model, having both low organic content and large error margins.",
        "supports_claims": ["C091"]
    },
    {
        "id": "E090",
        "content": "Residual carbonates adhering to pollen grain walls may explain discrepancy between 14C ages for pollen concentrates and bulk sediment samples",
        "evidence_type": "methodological_observation",
        "page": 13,
        "verbatim_quote": "Residual carbonates adhering to the pollen grain walls may explain the discrepancy between 14C ages for pollen concentrates and bulk sediment samples (Kilian et al., 2002).",
        "supports_claims": ["C092"]
    },
    {
        "id": "E091",
        "content": "Using remaining radiocarbon points, performance statistics indicated poor agreement between data and model (agreement index Amodel 12%)",
        "evidence_type": "chronology",
        "page": 13,
        "verbatim_quote": "Using the remaining points, performance statistics indicated poor agreement between the data and the model (agreement index Amodel 12%), especially in relation to samples Wk-32001 and Wk-32002.",
        "supports_claims": ["C093"]
    },
    {
        "id": "E092",
        "content": "Exclusion of sample Wk-32001 increased model's agreement index to 58%",
        "evidence_type": "chronology",
        "page": 13,
        "verbatim_quote": "Exclusion of Wk-32001 increased the model's agreement index to a more acceptable level (Amodel 58%).",
        "supports_claims": ["C094"]
    },
    {
        "id": "E093",
        "content": "Age-depth model places Pleistocene-Holocene boundary around 128-130 cm, close to lithological change and initial oak pollen increase at 125 cm",
        "evidence_type": "chronology",
        "page": 13,
        "verbatim_quote": "This model (Fig. 3) places the Pleistocene–Holocene boundary around 128–130 cm, close to the lithological change and initial oak pollen increase at 125 cm.",
        "supports_claims": ["C095"]
    },

    # Section 13: Discussion - Late Quaternary vegetation (4.1-4.1.1)
    {
        "id": "E094",
        "content": "Pollen source-area of large sites (>100 ha) is dominated by regional pollen component",
        "evidence_type": "methodological_principle",
        "page": 13,
        "verbatim_quote": "The second consideration is that the pollen source-area of large sites (>100 ha) is dominated by a regional pollen component (Jacobson and Bradshaw, 1981; Sugita, 2007).",
        "supports_claims": ["C096"]
    },
    {
        "id": "E095",
        "content": "Palaeovegetation records from large sites representative of spatial area estimated at ~10^4-10^5 km^2",
        "evidence_type": "methodological_principle",
        "page": 13,
        "verbatim_quote": "Palaeovegetation records from such sites are representative of a large spatial area, estimated at ~10^4–10^5 km^2 (Sugita, 2007), and recent modelling suggests even greater areas may be involved (Theuerkauf et al., 2012).",
        "supports_claims": ["C096"]
    },
    {
        "id": "E096",
        "content": "Artemisia-dominated cold steppe phase occurred from beginning of Straldzha quarry record until ~17,900 cal. a BP",
        "evidence_type": "pollen_zone",
        "page": 14,
        "verbatim_quote": "An Artemisia-dominated cold steppe phase occurred from the beginning of the Straldzha quarry record until ~17,900 cal. a BP.",
        "supports_claims": ["C097"]
    },
    {
        "id": "E097",
        "content": "Cold steppe phase corresponds to pollen spectra dated to Marine Isotope Stages (MIS) 2 and 3 in Tenaghi Philippon record",
        "evidence_type": "correlation",
        "page": 14,
        "verbatim_quote": "This phase corresponds to pollen spectra dated to Marine Isotope Stages (MIS) 2 and 3 in the Tenaghi Philippon record (Müller et al., 2011) and also occurs in pollen records from the Black Sea (Atanassova, 2005; Shumilovskikh et al., 2012) and the mountains of SW Bulgaria (Fig. 5).",
        "supports_claims": ["C098"]
    },
    {
        "id": "E098",
        "content": "Similar pollen assemblages to cold steppe appear in earliest part of Ezero record dated around 15,000 cal. a BP",
        "evidence_type": "correlation",
        "page": 14,
        "verbatim_quote": "Similar pollen assemblages appear in the earliest part of the Ezero record (Magyari et al., 2008), dated around 15,000 cal. a BP, and were interpreted as a landscape of dry steppe and wooded steppe.",
        "supports_claims": ["C099"]
    },
    {
        "id": "E099",
        "content": "Plant macrofossil data from Ezero indicate arboreal taxa (Juniperus, Celtis, Quercus, Betula, certain Rosaceae) present on Thracian Plain during cold steppe phase",
        "evidence_type": "macrofossil_data",
        "page": 14,
        "verbatim_quote": "Plant macrofossil data from Ezero indicate that arboreal taxa such as Juniperus, Celtis, Quercus, Betula and certain Rosaceae were present on the Thracian Plain, but their presence is hardly evident from pollen data perhaps because of reduced pollen production under glacial conditions (Magyari et al., 2008; Feurdean et al., 2012; see also Willis, 1994).",
        "supports_claims": ["C100"]
    },
    {
        "id": "E100",
        "content": "Eastern Balkans regarded as probable refugial area for deciduous thermophilous trees during glacial period",
        "evidence_type": "biogeographic_inference",
        "page": 14,
        "verbatim_quote": "Similar patches of xeric woodland were probably present around the Straldzha Mire, since the same pollen taxa occur during the cold steppe phase and the eastern Balkans is regarded as one of the probable refugial areas for deciduous thermophilous trees (Krebs et al., 2004; Leroy and Arpe, 2007; Bozilova et al., 2011).",
        "supports_claims": ["C101"]
    },
    {
        "id": "E101",
        "content": "Presence of Betula indicates climate considerably colder than present during cold steppe phase",
        "evidence_type": "climatic_indicator",
        "page": 14,
        "verbatim_quote": "The presence of Betula, however, seems to indicate a climate considerably colder than at present (Tarasov et al., 1998; Magyari et al., 2008).",
        "supports_claims": ["C102"]
    },
    {
        "id": "E102",
        "content": "Magnetic susceptibility and mineralogy suggest alternation between detrital input and derived pedogenically enhanced sediments during cold steppe phase",
        "evidence_type": "magnetic_analysis",
        "page": 14,
        "verbatim_quote": "The magnetic susceptibility and mineralogy of this period suggests that detrital input into the lake alternated with derived, pedogenically enhanced sediments, and this potentially reflects colder but variable climatic conditions consistent with deposition during MIS 3 and into MIS 2.",
        "supports_claims": ["C103"]
    },
    {
        "id": "E103",
        "content": "Ordination results suggest climatic variability through cold steppe phase",
        "evidence_type": "numerical_analysis",
        "page": 14,
        "verbatim_quote": "Ordination results also suggest climatic variability through this phase (Fig. 6).",
        "supports_claims": ["C104"]
    },
    {
        "id": "E104",
        "content": "Pinus pollen concentrations did not vary substantially from Pleistocene to Holocene",
        "evidence_type": "pollen_concentration",
        "page": 14,
        "verbatim_quote": "Pinus pollen concentrations did not vary substantially from the Pleistocene to the Holocene (supplementary information), suggesting that much of the Pinus pollen in Straldzha Mire was blown in from distant sources.",
        "supports_claims": ["C105"]
    },
    {
        "id": "E105",
        "content": "Lowest arboreal pollen contribution (7.5%) recorded at earliest part of cold steppe phase corresponding to grey silt band around 35,000 cal. a BP",
        "evidence_type": "pollen_percentage",
        "page": 14,
        "verbatim_quote": "The lowest arboreal pollen contribution (7.5%) is recorded at the earliest part of the cold steppe phase, corresponding to the grey silt band around 35,000 cal. a BP.",
        "supports_claims": ["C106"]
    },
    {
        "id": "E106",
        "content": "Similar arboreal pollen minima dated to ~39,000 cal. a BP (mid MIS 3) recorded at Lake Prespa and Tenaghi Philippon",
        "evidence_type": "correlation",
        "page": 14,
        "verbatim_quote": "Similar minima, dated to ~39,000 cal. a BP (mid MIS 3), are recorded at Lake Prespa (Leng et al., in press) and Tenaghi Philippon (Müller et al., 2011), possibly reflecting a regional climatic fluctuation.",
        "supports_claims": ["C107"]
    },
]

# Claims items (C080-C125 estimated)
new_claims = [
    # Section 11: Pollen stratigraphy continuation
    {
        "id": "C080",
        "content": "Vegetation of forest-steppe phase must have been relatively open, based on diversity of xeric and mesic herbs represented in pollen record",
        "claim_type": "palaeoenvironmental_interpretation",
        "page": 12,
        "verbatim_quote": "The vegetation of the third phase must have been relatively open, based on the diversity of xeric and mesic herbs represented in the pollen record.",
        "supported_by_evidence": ["E076"]
    },
    {
        "id": "C081",
        "content": "Pistacia terebinthus shrubs took part in early Holocene vegetation of Thracian Plain based on constant low pollen percentages",
        "claim_type": "vegetation_interpretation",
        "page": 19,
        "verbatim_quote": "Pistacia's poor pollen productivity (Roberts, 2002) implies that P. terebinthus shrubs took part in the early Holocene vegetation of the Thracian Plain, which also included a mixture of deciduous oaks, rosaceous shrubs and grassy meadow communities.",
        "supported_by_evidence": ["E077"]
    },
    {
        "id": "C082",
        "content": "Grazing and fire were perhaps not main factors stalling expansion of oak during forest-steppe phase based on reduced charcoal and dung fungi",
        "claim_type": "environmental_process",
        "page": 19,
        "verbatim_quote": "Importantly, charcoal concentrations and the occurrence of dung-inhabiting fungi are reduced during the forest-steppe phase, so grazing and fire were perhaps not the main factors stalling the expansion of oak.",
        "supported_by_evidence": ["E078"]
    },
    {
        "id": "C083",
        "content": "Forest landscape dominated by Quercus persisted from ~8700 to ~4000 cal. a BP during oak woods phase",
        "claim_type": "palaeovegetation",
        "page": 12,
        "verbatim_quote": "Around 8700 cal. a BP, Quercus commenced a rapid expansion and meadow vegetation contracted, creating a forest landscape that persisted until ~4000 cal. a BP.",
        "supported_by_evidence": ["E079", "E080", "E081"]
    },
    {
        "id": "C084",
        "content": "Oak woods phase characterized by reduced disturbance indicators (charcoal, grassland taxa, dung fungal spores)",
        "claim_type": "palaeoenvironmental_interpretation",
        "page": 12,
        "verbatim_quote": "Charcoal, Chenopodiaceae, grassland taxa and dung fungal spores are reduced.",
        "supported_by_evidence": ["E082"]
    },
    {
        "id": "C085",
        "content": "Straldzha Mire existed as carbonate-rich lake during oak woods phase based on aquatic indicators",
        "claim_type": "lake_status",
        "page": 19,
        "verbatim_quote": "Around Straldzha Mire, which at the time was a carbonate-rich lake with predominantly authigenic sedimentation, oak forest expansion stalled for 2500–3000 years after its initial Holocene advance (Fig. 5).",
        "supported_by_evidence": ["E083"]
    },
    {
        "id": "C086",
        "content": "Deforestation phase beginning ~4000 cal. a BP marked by sharp forest decline and increased human impact indicators",
        "claim_type": "anthropogenic_impact",
        "page": 12,
        "verbatim_quote": "A phase of deforestation represents the final stage in the vegetation history of Bulgaria's Thracian Plain and is more faithfully registered in the canal core than in the quarry section.",
        "supported_by_evidence": ["E084"]
    },
    {
        "id": "C087",
        "content": "Late succession of Fagus and Carpinus preceded deforestation based on canal core evidence",
        "claim_type": "vegetation_succession",
        "page": 12,
        "verbatim_quote": "The canal core, which is regarded as a more complete representation of this phase, indicates that deforestation was preceded by the late succession of Fagus and Carpinus and followed by considerable peaks in Salix, Alnus and fern spores, and a temporary recovery of Quercus.",
        "supported_by_evidence": ["E085"]
    },
    {
        "id": "C088",
        "content": "Pioneer species (Salix, Alnus, ferns) temporarily colonized cleared areas following deforestation with brief Quercus recovery",
        "claim_type": "vegetation_succession",
        "page": 12,
        "verbatim_quote": "The canal core, which is regarded as a more complete representation of this phase, indicates that deforestation was preceded by the late succession of Fagus and Carpinus and followed by considerable peaks in Salix, Alnus and fern spores, and a temporary recovery of Quercus.",
        "supported_by_evidence": ["E086"]
    },
    {
        "id": "C089",
        "content": "Final stage of deforestation phase characterized by cereal cultivation and increased fire activity",
        "claim_type": "anthropogenic_impact",
        "page": 12,
        "verbatim_quote": "All of these taxa decrease toward the end of the zone, when Chenopodiaceae, Triticum-type and macroscopic charcoal increase.",
        "supported_by_evidence": ["E087"]
    },

    # Section 12: Age-depth model
    {
        "id": "C090",
        "content": "Chronology for Straldzha record based on 13 AMS radiocarbon dates using Bayesian age-depth modelling",
        "claim_type": "methodological",
        "page": 13,
        "verbatim_quote": "Thirteen Accelerator Mass Spectrometer radiocarbon dates were obtained for the Straldzha profiles.",
        "supported_by_evidence": ["E088"]
    },
    {
        "id": "C091",
        "content": "Low organic content and large error margins led to exclusion of three radiocarbon dates from age-depth model",
        "claim_type": "methodological",
        "page": 13,
        "verbatim_quote": "Three dated points were initially excluded from the age-depth model, having both low organic content and large error margins.",
        "supported_by_evidence": ["E089"]
    },
    {
        "id": "C092",
        "content": "Pollen concentrate radiocarbon ages may be affected by residual carbonates adhering to pollen grain walls",
        "claim_type": "methodological_limitation",
        "page": 13,
        "verbatim_quote": "Residual carbonates adhering to the pollen grain walls may explain the discrepancy between 14C ages for pollen concentrates and bulk sediment samples (Kilian et al., 2002).",
        "supported_by_evidence": ["E090"]
    },
    {
        "id": "C093",
        "content": "Initial age-depth model showed poor agreement with data, especially for samples Wk-32001 and Wk-32002",
        "claim_type": "methodological",
        "page": 13,
        "verbatim_quote": "Using the remaining points, performance statistics indicated poor agreement between the data and the model (agreement index Amodel 12%), especially in relation to samples Wk-32001 and Wk-32002.",
        "supported_by_evidence": ["E091"]
    },
    {
        "id": "C094",
        "content": "Exclusion of problematic sample Wk-32001 improved age-depth model agreement to acceptable level",
        "claim_type": "methodological",
        "page": 13,
        "verbatim_quote": "Exclusion of Wk-32001 increased the model's agreement index to a more acceptable level (Amodel 58%).",
        "supported_by_evidence": ["E092"]
    },
    {
        "id": "C095",
        "content": "Pleistocene-Holocene transition at Straldzha occurred around 128-130 cm depth, corresponding to lithological and vegetation changes",
        "claim_type": "chronological_interpretation",
        "page": 13,
        "verbatim_quote": "This model (Fig. 3) places the Pleistocene–Holocene boundary around 128–130 cm, close to the lithological change and initial oak pollen increase at 125 cm.",
        "supported_by_evidence": ["E093"]
    },

    # Section 13: Discussion - Late Quaternary vegetation
    {
        "id": "C096",
        "content": "Straldzha pollen record represents regional vegetation changes over large spatial area (~10^4-10^5 km^2) rather than local changes",
        "claim_type": "methodological_interpretation",
        "page": 13,
        "verbatim_quote": "Only large-scale vegetation changes are thus expected to register in the Straldzha pollen record.",
        "supported_by_evidence": ["E094", "E095"]
    },
    {
        "id": "C097",
        "content": "Considerable uncertainty attached to pre-Holocene chronology due to low organic content, possible old carbon effects and overlapping ages",
        "claim_type": "methodological_limitation",
        "page": 13,
        "verbatim_quote": "Considerable uncertainty is attached to the pre-Holocene section, which is affected by low organic content, possible old carbon effects and overlapping ages for different sediment depths.",
        "supported_by_evidence": ["E096"]
    },
    {
        "id": "C098",
        "content": "Cold steppe vegetation at Straldzha corresponds to MIS 2 and 3 conditions documented across wider Balkan and Black Sea region",
        "claim_type": "regional_correlation",
        "page": 14,
        "verbatim_quote": "This phase corresponds to pollen spectra dated to Marine Isotope Stages (MIS) 2 and 3 in the Tenaghi Philippon record (Müller et al., 2011) and also occurs in pollen records from the Black Sea (Atanassova, 2005; Shumilovskikh et al., 2012) and the mountains of SW Bulgaria (Fig. 5).",
        "supported_by_evidence": ["E097"]
    },
    {
        "id": "C099",
        "content": "Cold steppe vegetation at Straldzha interpreted as dry steppe and wooded steppe landscape similar to Ezero",
        "claim_type": "palaeoenvironmental_interpretation",
        "page": 14,
        "verbatim_quote": "Similar pollen assemblages appear in the earliest part of the Ezero record (Magyari et al., 2008), dated around 15,000 cal. a BP, and were interpreted as a landscape of dry steppe and wooded steppe.",
        "supported_by_evidence": ["E098"]
    },
    {
        "id": "C100",
        "content": "Arboreal taxa present on Thracian Plain during glacial period but hardly evident in pollen data due to reduced pollen production under cold conditions",
        "claim_type": "palaeobotanical_interpretation",
        "page": 14,
        "verbatim_quote": "Plant macrofossil data from Ezero indicate that arboreal taxa such as Juniperus, Celtis, Quercus, Betula and certain Rosaceae were present on the Thracian Plain, but their presence is hardly evident from pollen data perhaps because of reduced pollen production under glacial conditions (Magyari et al., 2008; Feurdean et al., 2012; see also Willis, 1994).",
        "supported_by_evidence": ["E099"]
    },
    {
        "id": "C101",
        "content": "Patches of xeric woodland probably present around Straldzha Mire during cold steppe phase as part of refugial populations",
        "claim_type": "biogeographic_interpretation",
        "page": 14,
        "verbatim_quote": "Similar patches of xeric woodland were probably present around the Straldzha Mire, since the same pollen taxa occur during the cold steppe phase and the eastern Balkans is regarded as one of the probable refugial areas for deciduous thermophilous trees (Krebs et al., 2004; Leroy and Arpe, 2007; Bozilova et al., 2011).",
        "supported_by_evidence": ["E100"]
    },
    {
        "id": "C102",
        "content": "Climate during cold steppe phase was considerably colder than present based on presence of Betula",
        "claim_type": "climatic_interpretation",
        "page": 14,
        "verbatim_quote": "The presence of Betula, however, seems to indicate a climate considerably colder than at present (Tarasov et al., 1998; Magyari et al., 2008).",
        "supported_by_evidence": ["E101"]
    },
    {
        "id": "C103",
        "content": "Cold steppe phase characterized by colder but variable climatic conditions during MIS 3 and into MIS 2",
        "claim_type": "climatic_interpretation",
        "page": 14,
        "verbatim_quote": "The magnetic susceptibility and mineralogy of this period suggests that detrital input into the lake alternated with derived, pedogenically enhanced sediments, and this potentially reflects colder but variable climatic conditions consistent with deposition during MIS 3 and into MIS 2.",
        "supported_by_evidence": ["E102", "E103"]
    },
    {
        "id": "C104",
        "content": "Pine trees present in region throughout last glacial period but Pinus pollen largely derived from distant sources",
        "claim_type": "palaeobotanical_interpretation",
        "page": 14,
        "verbatim_quote": "Pine trees were also present in the region throughout the last glacial period. Pinus pollen concentrations did not vary substantially from the Pleistocene to the Holocene (supplementary information), suggesting that much of the Pinus pollen in Straldzha Mire was blown in from distant sources.",
        "supported_by_evidence": ["E104"]
    },
    {
        "id": "C105",
        "content": "Arboreal pollen minimum around 35,000 cal. a BP represents coldest/driest conditions during cold steppe phase",
        "claim_type": "climatic_interpretation",
        "page": 14,
        "verbatim_quote": "The lowest arboreal pollen contribution (7.5%) is recorded at the earliest part of the cold steppe phase, corresponding to the grey silt band around 35,000 cal. a BP.",
        "supported_by_evidence": ["E105"]
    },
    {
        "id": "C106",
        "content": "Mid-MIS 3 arboreal pollen minimum at Straldzha correlates with similar minima across Balkans, possibly reflecting regional climatic fluctuation",
        "claim_type": "regional_correlation",
        "page": 14,
        "verbatim_quote": "Similar minima, dated to ~39,000 cal. a BP (mid MIS 3), are recorded at Lake Prespa (Leng et al., in press) and Tenaghi Philippon (Müller et al., 2011), possibly reflecting a regional climatic fluctuation.",
        "supported_by_evidence": ["E106"]
    },
    {
        "id": "C107",
        "content": "Higher arboreal percentages (up to 35%) in later part of cold steppe phase likely reflect expansion of frost-tolerant woodland during MIS 2",
        "claim_type": "palaeovegetation",
        "page": 15,
        "verbatim_quote": "Higher arboreal percentages (up to 35%), especially of Pinus, in the later part of the phase are most likely to reflect the expansion of frost-tolerant woodland during MIS 2 (Müller et al., 2011).",
        "supported_by_evidence": []
    },
]

# Add new items to existing arrays
data['evidence'].extend(new_evidence)
data['claims'].extend(new_claims)

# Calculate totals
total_evidence = len(data['evidence'])
total_claims = len(data['claims'])
total_items = total_evidence + total_claims

# Update extraction notes
if 'pass1_sections11-13' not in data['extraction_notes']:
    data['extraction_notes']['pass1_sections11-13'] = {}

data['extraction_notes']['pass1_sections11-13'] = {
    "completion_date": "2025-10-30",
    "sections_covered": [
        "Section 11: Pollen stratigraphy continuation (3.2.3-3.2.5) - pages 11-12",
        "Section 12: Age-depth model (3.3) - page 13",
        "Section 13: Discussion - Late Quaternary vegetation (4.1-4.1.1) - pages 13-14"
    ],
    "items_extracted": {
        "evidence": len(new_evidence),
        "claims": len(new_claims),
        "total": len(new_evidence) + len(new_claims)
    },
    "running_totals": {
        "evidence": total_evidence,
        "claims": total_claims,
        "total": total_items
    },
    "notes": "Completed final sections of Pass 1 covering remaining pollen stratigraphy results, age-depth model discussion, and beginning of Discussion section. Liberal extraction approach maintained."
}

# Save updated extraction
with open('/home/shawn/Code/llm-reproducibility/outputs/connor-et-al-2013/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Pass 1 Sections 11-13 Extraction Complete!")
print(f"\nItems Extracted:")
print(f"  Evidence: {len(new_evidence)}")
print(f"  Claims: {len(new_claims)}")
print(f"  Total: {len(new_evidence) + len(new_claims)}")
print(f"\nRunning Totals:")
print(f"  Evidence: {total_evidence}")
print(f"  Claims: {total_claims}")
print(f"  Total: {total_items}")
print(f"\nSections completed: 1-13 of 13")
print(f"\nPass 1 COMPLETE! Ready for Pass 2: Rationalization")
