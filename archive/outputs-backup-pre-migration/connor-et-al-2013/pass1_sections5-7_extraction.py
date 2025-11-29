#!/usr/bin/env python3
"""
Pass 1: Liberal Extraction - Sections 5-7 (Material and methods)
Connor et al. 2013 - Environmental conditions in SE Balkans since LGM

Liberal over-extraction approach: 40-50% over expected targets
Sections: Site description, Sampling and analytical techniques, Numerical analyses
"""

import json

# Load current extraction
with open('/home/shawn/Code/llm-reproducibility/outputs/connor-et-al-2013/extraction.json', 'r') as f:
    data = json.load(f)

# SECTION 5: SITE DESCRIPTION (pages 6-7)
section5_items = [
    # Evidence items
    {
        "id": "E018",
        "content": "Straldzha Mire located in Karnobat Lowlands at foot of Stara Planina Mountains",
        "evidence_type": "site_description",
        "page": 6,
        "verbatim_quote": "The Straldzha Mire is located in the Karnobat Lowlands at the foot of the Stara Planina Mountains (Fig. 2).",
        "supports_claims": ["C028"]
    },
    {
        "id": "E019",
        "content": "Mire occupies large shallow depression underlain by Pleistocene silts and gravels, surrounded by low hills of Upper Cretaceous limestones, marls and volcanic deposits",
        "evidence_type": "geological_context",
        "page": 6,
        "verbatim_quote": "The mire occupies a large, shallow depression underlain by Pleistocene silts and gravels and is surrounded by low hills of Upper Cretaceous limestones, marls and volcanic deposits",
        "supports_claims": ["C028"]
    },
    {
        "id": "E020",
        "content": "Mire formerly covered area of around 14,000 ha, making it largest freshwater wetland basin in Bulgaria",
        "evidence_type": "site_dimensions",
        "page": 6,
        "verbatim_quote": "The mire formerly covered an area of around 14,000 ha (Bonchev, 1929), making it the largest freshwater wetland basin in Bulgaria.",
        "supports_claims": ["C029"]
    },
    {
        "id": "E021",
        "content": "Early 20th century botanists recorded Straldzha Mire was diverse reed-swamp dominated by Phragmites australis, with floating islands, thick peat layer and halophilous vegetation",
        "evidence_type": "historical_observation",
        "page": 6,
        "verbatim_quote": "Early 20th century botanists recorded that the Straldzha Mire was a diverse reed-swamp dominated by Phragmites australis, with floating islands in areas of open water, a thick peat layer and halophilous vegetation distributed around the margins",
        "supports_claims": ["C030"]
    },
    {
        "id": "E022",
        "content": "Artificial drainage of Straldzha Mire proceeded 1932-1939, initially by deepening bed of Marash creek; by 1960s mire was completely drained",
        "evidence_type": "historical_event",
        "page": 6,
        "verbatim_quote": "Artificial drainage of the Straldzha Mire proceeded from 1932 to 1939, initially by deepening the bed of the Marash, a creek that runs along the western edge of the mire. Expansion of the canal system continued and, by the 1960s, the mire was completely drained",
        "supports_claims": ["C031"]
    },
    {
        "id": "E023",
        "content": "Area around mire thought to have been vegetated by oak forests (Q. cerris, Q. pubescens, Q. frainetto, Q. robur) with Ulmus minor and Fraxinus angustifolia over floodplains",
        "evidence_type": "vegetation_reconstruction",
        "page": 6,
        "verbatim_quote": "The area around the mire, like most of Bulgarian Thrace, is thought to have once been vegetated by oak forests (Q. cerris, Q. pubescens ssp. pubescens, Q. frainetto and Q. robur), with Ulmus minor and Fraxinus angustifolia ssp. oxycarpa communities distributed over floodplains",
        "supports_claims": ["C032"]
    },
    {
        "id": "E024",
        "content": "Today few remnants of forest communities remain and entire lowland is agricultural landscape",
        "evidence_type": "present_day_observation",
        "page": 7,
        "verbatim_quote": "Today, few remnants of these forest communities remain and the entire lowland is an agricultural landscape.",
        "supports_claims": ["C033"]
    },
    {
        "id": "E025",
        "content": "Climate of Bulgaria's Thracian Plain transitional between Mediterranean and continental zones, with two precipitation maxima in winter and May-June",
        "evidence_type": "climatic_data",
        "page": 7,
        "verbatim_quote": "The climate of Bulgaria's Thracian Plain is transitional between Mediterranean and continental zones, with two precipitation maxima: in winter and May-June (Fig.2).",
        "supports_claims": ["C034"]
    },
    {
        "id": "E026",
        "content": "Average annual precipitation 540 mm, average temperature 12°C, absolute maximum 38°C",
        "evidence_type": "climatic_data",
        "page": 7,
        "verbatim_quote": "Average annual precipitation amounts to 540 mm and the average temperature is 12 ºC, reaching an absolute maximum of 38 ºC",
        "supports_claims": ["C034"]
    },

    # Claims from section 5
    {
        "id": "C028",
        "content": "Straldzha Mire provides appropriate site for examining regional palaeoenvironmental history of Thracian Plain",
        "claim_type": "methodological",
        "page": 6,
        "verbatim_quote": "The Straldzha Mire is located in the Karnobat Lowlands at the foot of the Stara Planina Mountains (Fig. 2). These lowlands are part of the pre-Balkan sunkland",
        "supported_by_evidence": ["E018", "E019"]
    },
    {
        "id": "C029",
        "content": "Large size of Straldzha Mire (14,000 ha) makes it significant site for regional-scale palaeovegetation reconstruction",
        "claim_type": "interpretive",
        "page": 6,
        "verbatim_quote": "making it the largest freshwater wetland basin in Bulgaria",
        "supported_by_evidence": ["E020"]
    },
    {
        "id": "C030",
        "content": "Historical botanical records provide baseline understanding of pre-drainage wetland character",
        "claim_type": "interpretive",
        "page": 6,
        "verbatim_quote": "Early 20th century botanists recorded that the Straldzha Mire was a diverse reed-swamp dominated by Phragmites australis",
        "supported_by_evidence": ["E021"]
    },
    {
        "id": "C031",
        "content": "20th century drainage activities have fundamentally altered wetland ecosystem",
        "claim_type": "interpretive",
        "page": 6,
        "verbatim_quote": "by the 1960s, the mire was completely drained",
        "supported_by_evidence": ["E022"]
    },
    {
        "id": "C032",
        "content": "Pre-agricultural vegetation of Thracian Plain lowlands consisted primarily of oak-dominated forests",
        "claim_type": "interpretive",
        "page": 6,
        "verbatim_quote": "The area around the mire, like most of Bulgarian Thrace, is thought to have once been vegetated by oak forests",
        "supported_by_evidence": ["E023"]
    },
    {
        "id": "C033",
        "content": "Contemporary landscape represents complete transformation from historical forested conditions",
        "claim_type": "interpretive",
        "page": 7,
        "verbatim_quote": "Today, few remnants of these forest communities remain and the entire lowland is an agricultural landscape.",
        "supported_by_evidence": ["E024"]
    },
    {
        "id": "C034",
        "content": "Transitional Mediterranean-continental climate with bimodal precipitation influences regional vegetation patterns",
        "claim_type": "interpretive",
        "page": 7,
        "verbatim_quote": "The climate of Bulgaria's Thracian Plain is transitional between Mediterranean and continental zones, with two precipitation maxima",
        "supported_by_evidence": ["E025", "E026"]
    },
]

# SECTION 6: SAMPLING AND ANALYTICAL TECHNIQUES (pages 7-8)
section6_items = [
    # Evidence items
    {
        "id": "E027",
        "content": "Trench 520 cm deep and 30 cm wide dug into side of Straldja tile factory quarry in March 2008",
        "evidence_type": "sampling_procedure",
        "page": 7,
        "verbatim_quote": "In March 2008, we dug a trench 520 cm deep and 30 cm wide into the side of the \"Straldja\" tile factory's quarry in the lowest part of the Straldzha Mire",
        "supports_claims": ["C035"]
    },
    {
        "id": "E028",
        "content": "Quarry location: 42°37'49\"N, 26°46'12\"E, 138 m a.s.l., near Gyola area where Tonkov et al. obtained late Holocene pollen record",
        "evidence_type": "site_coordinates",
        "page": 7,
        "verbatim_quote": "42º37'49\"N, 26º46'12\"E, 138 m a.s.l.).The quarry is located near the 'Gyola' area where Tonkov et al. (2008a, 2009) obtained their late Holocene pollen record.",
        "supports_claims": ["C036"]
    },
    {
        "id": "E029",
        "content": "Samples ~20 cm³ taken at 5-cm intervals until 140 cm depth, thereafter at 20-cm intervals",
        "evidence_type": "sampling_procedure",
        "page": 7,
        "verbatim_quote": "Samples ~20cm3 in size were taken at 5-cm intervals until a depth of 140 cm from the surface and thereafter at 20-cm intervals.",
        "supports_claims": ["C037"]
    },
    {
        "id": "E030",
        "content": "Samples sealed in plastic bags and stored in refrigerator",
        "evidence_type": "sample_preservation",
        "page": 7,
        "verbatim_quote": "The samples were immediately sealed in plastic bags and stored in a refrigerator.",
        "supports_claims": ["C038"]
    },
    {
        "id": "E031",
        "content": "Subsamples of 1 cm³ extracted for pollen analysis, combined with Lycopodium spore tablets, treated with 10% HCl, density separation in sodium polytungstate (s.g. 2.0), acetolysis for 1 minute, mounted in glycerol",
        "evidence_type": "laboratory_procedure",
        "page": 7,
        "verbatim_quote": "Subsamples of 1cm3 were extracted for pollen analysis, combined with Lycopodium spore tablets (University of Lund), treated with 10% HCl, density separation in sodium polytungstate (s.g. 2.0) and acetolysis for 1 minute, prior to being mounted in glycerol",
        "supports_claims": ["C039"]
    },
    {
        "id": "E032",
        "content": "At least 200 (average 600) terrestrial pollen counted in each sample at 400× magnification",
        "evidence_type": "counting_procedure",
        "page": 7,
        "verbatim_quote": "At least 200 (average 600) terrestrial pollen were counted in each sample. Pollen identifications were made with reference to Moore et al. (1991) and Reille (1999).",
        "supports_claims": ["C040"]
    },
    {
        "id": "E033",
        "content": "Non-pollen palynomorphs classified according to Jankovská and Komárek (2000), van Geel (2001) and van Geel and Aptroot (2006)",
        "evidence_type": "classification_procedure",
        "page": 7,
        "verbatim_quote": "Non-pollen palynomorphs were classified according to Jankovská and Komárek (2000), van Geel (2001) and van Geel and Aptroot (2006).",
        "supports_claims": ["C041"]
    },
    {
        "id": "E034",
        "content": "Microscopic charcoal (<200 µm) quantified on pollen slides using point-count method",
        "evidence_type": "analytical_procedure",
        "page": 7,
        "verbatim_quote": "Microscopic charcoal (<200 µm) was quantified on pollen slides using the point-count method (Clark, 1982)",
        "supports_claims": ["C042"]
    },
    {
        "id": "E035",
        "content": "Macroscopic charcoal (>250 µm) quantified using modification of Oregon sieving method: ~2 cm³ sediment in 4.2% sodium hypochlorite for 24 hours, washed through 250 µm sieve, hand-sorted, photographed",
        "evidence_type": "analytical_procedure",
        "page": 7,
        "verbatim_quote": "macroscopic charcoal (>250 µm) was quantified using a modification of the 'Oregon sieving method' (Long et al., 1998; Mooney and Tinner, 2011). A known volume (~2 cm3) of sediment was placed in dilute (4.2%) sodium hypochlorite (bleach) for 24 hours (Rhodes 1998) and then washed through a 250 µm sieve. The captured material was hand-sorted to remove extraneous material and the charcoal photographed",
        "supports_claims": ["C043"]
    },
    {
        "id": "E036",
        "content": "Charcoal concentrations quantified using image analysis software (Scion Image 4.0.3.2), expressed as area (mm² per cm³)",
        "evidence_type": "analytical_procedure",
        "page": 8,
        "verbatim_quote": "Charcoal concentrations were quantified using image analysis software (Scion Image 4.0.3.2). This resulted in the concentration of macroscopic charcoal >250 µm, expressed as an area (mm2 per cm3).",
        "supports_claims": ["C044"]
    },
    {
        "id": "E037",
        "content": "Charcoal particles >250 µm should predominantly reflect local fire events",
        "evidence_type": "methodological_rationale",
        "page": 8,
        "verbatim_quote": "Charcoal particles of this size should predominantly reflect local fire events (Long et al., 1998; Whitlock and Larsen, 2001; Conedera et al., 2009).",
        "supports_claims": ["C045"]
    },
    {
        "id": "E038",
        "content": "Charcoal concentrations converted to influx (CHAR) by normalising for deposition time",
        "evidence_type": "analytical_procedure",
        "page": 8,
        "verbatim_quote": "Charcoal concentrations were then converted to an influx (also known as charcoal accumulation rates or CHAR), by normalising for the deposition time of the sample.",
        "supports_claims": ["C046"]
    },
    {
        "id": "E039",
        "content": "Dual-frequency magnetic susceptibility measurements run on Bartington MS2 meter following Dearing (1999) and Herries and Fisher (2010) protocols",
        "evidence_type": "analytical_procedure",
        "page": 8,
        "verbatim_quote": "Dual-frequency magnetic susceptibility measurements were run on a Bartington MS2 magnetic susceptibility meter following the protocols outlined by Dearing (1999) and Herries and Fisher (2010).",
        "supports_claims": ["C047"]
    },
    {
        "id": "E040",
        "content": "Additional mineral magnetic analysis undertaken on Magnetic Measurements Variable Field Translation Balance (VFTB) including IRM acquisition curves, backfields, hysteresis loops, thermomagnetic curves",
        "evidence_type": "analytical_procedure",
        "page": 8,
        "verbatim_quote": "Additional mineral magnetic analysis was undertaken on a Magnetic Measurements Variable Field Translation Balance (VFTB), including isothermal remanent magnetisation (IRM) acquisition curves and backfields, hysteresis loops and thermomagnetic curves.",
        "supports_claims": ["C048"]
    },
    {
        "id": "E041",
        "content": "Mineral magnetic measurements provide information on magnetic minerals (magnetite, maghaemite, haematite), their grain size and concentrations",
        "evidence_type": "methodological_rationale",
        "page": 8,
        "verbatim_quote": "These mineral magnetic measurements provide information on changes in the magnetic minerals present (i.e. magnetite, maghaemite and haematite), their magnetic grain size and concentrations",
        "supports_claims": ["C049"]
    },
    {
        "id": "E042",
        "content": "Additional cores obtained from three locations where canal excavation preserved original sediment surface, collected with Eijkelkamp auger",
        "evidence_type": "sampling_procedure",
        "page": 8,
        "verbatim_quote": "we obtained additional cores from three locations on the mire (Fig. 2) where material excavated during construction of drainage canals preserved the original sediment surface. The cores were collected with an Eijkelkamp auger.",
        "supports_claims": ["C050"]
    },
    {
        "id": "E043",
        "content": "Canal core samples taken at 10-cm intervals (5-cm intervals around sedimentological changes), pollen extracted as described but Lycopodium markers unavailable",
        "evidence_type": "sampling_procedure",
        "page": 8,
        "verbatim_quote": "Samples from the westernmost site (canal core, Fig. 2) were taken at 10-cm intervals (5-cm intervals around sedimentological changes) and pollen extracted as described above, although Lycopodium markers were unavailable at the time.",
        "supports_claims": ["C051"]
    },
    {
        "id": "E044",
        "content": "Results plotted using Psimpoll (Bennett, 2004)",
        "evidence_type": "data_presentation",
        "page": 8,
        "verbatim_quote": "Results were plotted using Psimpoll (Bennett, 2004).",
        "supports_claims": ["C052"]
    },

    # Claims from section 6
    {
        "id": "C035",
        "content": "Quarry section provides access to deep sedimentary sequence suitable for long-term palaeoenvironmental reconstruction",
        "claim_type": "methodological",
        "page": 7,
        "verbatim_quote": "we dug a trench 520 cm deep and 30 cm wide into the side of the \"Straldja\" tile factory's quarry",
        "supported_by_evidence": ["E027"]
    },
    {
        "id": "C036",
        "content": "Proximity to previous pollen study site allows cross-validation of late Holocene results",
        "claim_type": "methodological",
        "page": 7,
        "verbatim_quote": "The quarry is located near the 'Gyola' area where Tonkov et al. (2008a, 2009) obtained their late Holocene pollen record.",
        "supported_by_evidence": ["E028"]
    },
    {
        "id": "C037",
        "content": "Variable sampling intervals provide higher resolution for recent sediments while maintaining coverage of entire sequence",
        "claim_type": "methodological",
        "page": 7,
        "verbatim_quote": "Samples ~20cm3 in size were taken at 5-cm intervals until a depth of 140 cm from the surface and thereafter at 20-cm intervals.",
        "supported_by_evidence": ["E029"]
    },
    {
        "id": "C038",
        "content": "Immediate sealing and refrigeration preserve sample integrity for palynological analysis",
        "claim_type": "methodological",
        "page": 7,
        "verbatim_quote": "The samples were immediately sealed in plastic bags and stored in a refrigerator.",
        "supported_by_evidence": ["E030"]
    },
    {
        "id": "C039",
        "content": "Standard pollen preparation techniques ensure comparability with other palynological studies",
        "claim_type": "methodological",
        "page": 7,
        "verbatim_quote": "Subsamples of 1cm3 were extracted for pollen analysis, combined with Lycopodium spore tablets (University of Lund), treated with 10% HCl, density separation in sodium polytungstate (s.g. 2.0) and acetolysis for 1 minute",
        "supported_by_evidence": ["E031"]
    },
    {
        "id": "C040",
        "content": "Pollen counting thresholds (minimum 200, average 600) provide statistically robust basis for percentage calculations",
        "claim_type": "methodological",
        "page": 7,
        "verbatim_quote": "At least 200 (average 600) terrestrial pollen were counted in each sample.",
        "supported_by_evidence": ["E032"]
    },
    {
        "id": "C041",
        "content": "Non-pollen palynomorphs provide complementary environmental indicators beyond pollen evidence",
        "claim_type": "methodological",
        "page": 7,
        "verbatim_quote": "Non-pollen palynomorphs were classified according to Jankovská and Komárek (2000), van Geel (2001) and van Geel and Aptroot (2006).",
        "supported_by_evidence": ["E033"]
    },
    {
        "id": "C042",
        "content": "Point-count method for microscopic charcoal allows quantification of regional fire signals",
        "claim_type": "methodological",
        "page": 7,
        "verbatim_quote": "Microscopic charcoal (<200 µm) was quantified on pollen slides using the point-count method",
        "supported_by_evidence": ["E034"]
    },
    {
        "id": "C043",
        "content": "Oregon sieving method modification provides standardised quantification of macroscopic charcoal",
        "claim_type": "methodological",
        "page": 7,
        "verbatim_quote": "macroscopic charcoal (>250 µm) was quantified using a modification of the 'Oregon sieving method'",
        "supported_by_evidence": ["E035"]
    },
    {
        "id": "C044",
        "content": "Image analysis provides objective measurement of charcoal area concentrations",
        "claim_type": "methodological",
        "page": 8,
        "verbatim_quote": "Charcoal concentrations were quantified using image analysis software (Scion Image 4.0.3.2).",
        "supported_by_evidence": ["E036"]
    },
    {
        "id": "C045",
        "content": "Size-based separation of charcoal allows discrimination between local and regional fire signals",
        "claim_type": "methodological",
        "page": 8,
        "verbatim_quote": "Charcoal particles of this size should predominantly reflect local fire events",
        "supported_by_evidence": ["E037"]
    },
    {
        "id": "C046",
        "content": "Conversion to influx rates accounts for variable sedimentation and provides temporal fire frequency estimates",
        "claim_type": "methodological",
        "page": 8,
        "verbatim_quote": "Charcoal concentrations were then converted to an influx (also known as charcoal accumulation rates or CHAR), by normalising for the deposition time of the sample.",
        "supported_by_evidence": ["E038"]
    },
    {
        "id": "C047",
        "content": "Magnetic susceptibility measurements provide proxy for sediment source and environmental change",
        "claim_type": "methodological",
        "page": 8,
        "verbatim_quote": "Dual-frequency magnetic susceptibility measurements were run on a Bartington MS2 magnetic susceptibility meter following the protocols outlined by Dearing (1999) and Herries and Fisher (2010).",
        "supported_by_evidence": ["E039"]
    },
    {
        "id": "C048",
        "content": "Multiple mineral magnetic analyses allow detailed characterisation of magnetic mineral assemblages",
        "claim_type": "methodological",
        "page": 8,
        "verbatim_quote": "Additional mineral magnetic analysis was undertaken on a Magnetic Measurements Variable Field Translation Balance (VFTB), including isothermal remanent magnetisation (IRM) acquisition curves and backfields, hysteresis loops and thermomagnetic curves.",
        "supported_by_evidence": ["E040"]
    },
    {
        "id": "C049",
        "content": "Mineral magnetic properties reveal changes in sediment source, alteration processes and environmental forcing",
        "claim_type": "interpretive",
        "page": 8,
        "verbatim_quote": "thus allowing changes in sediment source and alteration to be identified and the driving forces behind magnetic susceptibility changes to be established.",
        "supported_by_evidence": ["E041"]
    },
    {
        "id": "C050",
        "content": "Additional cores address potential truncation or disturbance in upper part of quarry section",
        "claim_type": "methodological",
        "page": 8,
        "verbatim_quote": "Since the upper part of the Straldzha quarry record may have been disturbed or truncated by quarrying activities, we obtained additional cores from three locations on the mire (Fig. 2) where material excavated during construction of drainage canals preserved the original sediment surface.",
        "supported_by_evidence": ["E042"]
    },
    {
        "id": "C051",
        "content": "Canal core provides more complete representation of upper sedimentary sequence",
        "claim_type": "interpretive",
        "page": 8,
        "verbatim_quote": "Samples from the westernmost site (canal core, Fig. 2) were taken at 10-cm intervals",
        "supported_by_evidence": ["E043"]
    },
    {
        "id": "C052",
        "content": "Psimpoll software allows standardised visualisation of pollen stratigraphic data",
        "claim_type": "methodological",
        "page": 8,
        "verbatim_quote": "Results were plotted using Psimpoll (Bennett, 2004).",
        "supported_by_evidence": ["E044"]
    },
]

# SECTION 7: NUMERICAL ANALYSES (pages 8-9)
section7_items = [
    # Evidence items
    {
        "id": "E045",
        "content": "Detrended Correspondence Analysis (DCA: Hill and Gauch, 1980) and minimum variance cluster analysis (Ward, 1963) used to compare pre-existing pollen data to new record",
        "evidence_type": "analytical_procedure",
        "page": 8,
        "verbatim_quote": "We used Detrended Correspondence Analysis (DCA: Hill and Gauch, 1980) and minimum variance cluster analysis (Ward, 1963) to compare pre-existing pollen data to the new record.",
        "supports_claims": ["C053"]
    },
    {
        "id": "E046",
        "content": "Data from European Pollen Database used, representative records selected from Bulgarian mountains and Black Sea area",
        "evidence_type": "data_source",
        "page": 8,
        "verbatim_quote": "We made use of data publicly available through the European Pollen Database (Fyfe et al., 2009) and selected a number of representative records from the Bulgarian mountains and the Black Sea area (Fig. 1)",
        "supports_claims": ["C054"]
    },
    {
        "id": "E047",
        "content": "Pollen taxonomy standardised to base of 99 taxa, resulting in some loss of information",
        "evidence_type": "data_processing",
        "page": 9,
        "verbatim_quote": "Pollen taxonomy was standardised to a base of 99 taxa (see supplementary information), resulting in some loss of information.",
        "supports_claims": ["C055"]
    },
    {
        "id": "E048",
        "content": "Standardisation necessary to remove influence of different pollen-taxonomic systems (e.g. differentiation of Quercus morphotypes)",
        "evidence_type": "methodological_rationale",
        "page": 9,
        "verbatim_quote": "This standardisation was necessary to remove the influence of different pollen-taxonomic systems (e.g. differentiation of Quercus morphotypes).",
        "supports_claims": ["C056"]
    },
    {
        "id": "E049",
        "content": "Analyses implemented in program PC-Ord (McCune and Mefford, 1999)",
        "evidence_type": "analytical_software",
        "page": 9,
        "verbatim_quote": "Analyses were implemented in the program PC-Ord (McCune and Mefford, 1999).",
        "supports_claims": ["C057"]
    },
    {
        "id": "E050",
        "content": "Combination of minimum variance clustering and indicator species analysis (Dufrêne and Legendre, 1997) used to determine optimum number of groups",
        "evidence_type": "analytical_procedure",
        "page": 9,
        "verbatim_quote": "A combination of minimum variance clustering and indicator species analysis (Dufrêne and Legendre, 1997) was used to determine an optimum number of groups.",
        "supports_claims": ["C058"]
    },
    {
        "id": "E051",
        "content": "Selected maximum number of groups in which each group had at least one statistically significant indicator (p=0.001; Monte Carlo test, 1000 permutations)",
        "evidence_type": "statistical_procedure",
        "page": 9,
        "verbatim_quote": "We selected the maximum number of groups in which each group had at least one statistically significant indicator (p=0.001; Monte Carlo test, 1000 permutations).",
        "supports_claims": ["C059"]
    },
    {
        "id": "E052",
        "content": "Results plotted on timescales from European Pollen Database or from original publication (Lake Varna: Bozilova and Beug, 1994)",
        "evidence_type": "data_presentation",
        "page": 9,
        "verbatim_quote": "Results were plotted on timescales provided in the European Pollen Database or, in the case of Lake Varna, from the original publication (Bozilova and Beug, 1994).",
        "supports_claims": ["C060"]
    },

    # Claims from section 7
    {
        "id": "C053",
        "content": "DCA and cluster analysis provide objective basis for comparing palaeovegetational patterns across multiple sites",
        "claim_type": "methodological",
        "page": 8,
        "verbatim_quote": "Pollen data were analysed numerically to elucidate the palaeoclimatic significance and palaeovegetational context of the results. We used Detrended Correspondence Analysis (DCA: Hill and Gauch, 1980) and minimum variance cluster analysis (Ward, 1963)",
        "supported_by_evidence": ["E045"]
    },
    {
        "id": "C054",
        "content": "Regional comparison reveals geographical and altitudinal patterns in vegetation development",
        "claim_type": "interpretive",
        "page": 8,
        "verbatim_quote": "selected a number of representative records from the Bulgarian mountains and the Black Sea area (Fig. 1) in order to compare geographical and altitudinal patterns in vegetation development.",
        "supported_by_evidence": ["E046"]
    },
    {
        "id": "C055",
        "content": "Taxonomic standardisation enables cross-site comparison despite some information loss",
        "claim_type": "methodological",
        "page": 9,
        "verbatim_quote": "Pollen taxonomy was standardised to a base of 99 taxa (see supplementary information), resulting in some loss of information.",
        "supported_by_evidence": ["E047"]
    },
    {
        "id": "C056",
        "content": "Standardisation removes methodological artefacts arising from different taxonomic conventions",
        "claim_type": "methodological",
        "page": 9,
        "verbatim_quote": "This standardisation was necessary to remove the influence of different pollen-taxonomic systems",
        "supported_by_evidence": ["E048"]
    },
    {
        "id": "C057",
        "content": "PC-Ord provides robust platform for multivariate ecological data analysis",
        "claim_type": "methodological",
        "page": 9,
        "verbatim_quote": "Analyses were implemented in the program PC-Ord (McCune and Mefford, 1999).",
        "supported_by_evidence": ["E049"]
    },
    {
        "id": "C058",
        "content": "Indicator species analysis provides statistical basis for identifying characteristic taxa of each vegetation group",
        "claim_type": "methodological",
        "page": 9,
        "verbatim_quote": "A combination of minimum variance clustering and indicator species analysis (Dufrêne and Legendre, 1997) was used to determine an optimum number of groups.",
        "supported_by_evidence": ["E050"]
    },
    {
        "id": "C059",
        "content": "Statistical significance threshold (p=0.001) with Monte Carlo testing ensures robust group definitions",
        "claim_type": "methodological",
        "page": 9,
        "verbatim_quote": "We selected the maximum number of groups in which each group had at least one statistically significant indicator (p=0.001; Monte Carlo test, 1000 permutations).",
        "supported_by_evidence": ["E051"]
    },
    {
        "id": "C060",
        "content": "Temporal plotting allows assessment of synchronous vs. asynchronous vegetation changes across region",
        "claim_type": "methodological",
        "page": 9,
        "verbatim_quote": "Results were plotted on timescales provided in the European Pollen Database",
        "supported_by_evidence": ["E052"]
    },
]

# Combine all items from sections 5-7
all_items = section5_items + section6_items + section7_items

# Separate evidence and claims
evidence = [item for item in all_items if item['id'].startswith('E')]
claims = [item for item in all_items if item['id'].startswith('C')]

# Add to existing arrays
data['evidence'].extend(evidence)
data['claims'].extend(claims)

# Save updated extraction
with open('/home/shawn/Code/llm-reproducibility/outputs/connor-et-al-2013/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

# Print summary
print("Pass 1 Sections 5-7 Extraction Complete!")
print(f"\nItems Extracted:")
print(f"  Evidence: {len(evidence)}")
print(f"  Claims: {len(claims)}")
print(f"  Total: {len(all_items)}")

print(f"\nRunning Totals:")
print(f"  Evidence: {len(data['evidence'])}")
print(f"  Claims: {len(data['claims'])}")
print(f"  Total: {len(data['evidence']) + len(data['claims'])}")

print(f"\nReady for Sections 8-10 extraction")
