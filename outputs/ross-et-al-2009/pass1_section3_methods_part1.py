#!/usr/bin/env python3
"""
Pass 1, Section 3: Liberal Claims/Evidence Extraction
Ross et al. 2009 - Remote Sensing and Archaeological Prospection in Apulia, Italy

Section: Methods (Georeferencing + Image Analysis) (~1300 words, pages 426-428)

Approach: Liberal extraction, cast wide net, aim for over-extraction.
Focus on methodological procedures, technical specifications, and analytical techniques.
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
        "evidence_id": "E029",
        "content": "Analysis of imagery began with georeferencing and projection, followed by image overlay and enhancement.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Analysis of the imagery began with georeferencing and projection, followed by image overlay and enhancement.",
        "page": 426,
        "relevance": "Documents sequence of image processing steps",
        "supports_claims": ["C048"]
    },
    {
        "evidence_id": "E030",
        "content": "Ground control was carried out concurrently with feature identification due to time constraints and to improve accuracy through immediate feedback.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Ground control was carried out concurrently with feature identification because of time constraints and to improve the accuracy of feature identification through immediate feedback from the field.",
        "page": 426,
        "relevance": "Explains concurrent methodology and its rationale",
        "supports_claims": ["C049", "C050"]
    },
    {
        "evidence_id": "E031",
        "content": "Information from ground control was used to refine ongoing feature identification by eliminating spectral patterns consistently denoting modern or natural features.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Information from ground control was used to refine ongoing feature identification in the image, as spectral responses or patterns consistently denoting modern or natural features were eliminated from consideration",
        "page": 426,
        "relevance": "Describes iterative refinement process",
        "supports_claims": ["C051"]
    },
    {
        "evidence_id": "E032",
        "content": "Ground control provided the location and extent of sites and off-site scatters as defined by the MTS.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Ground control also provided the location and extent of sites and off-site scatters as defined by the MTS.",
        "page": 426,
        "relevance": "Documents additional role of ground control",
        "supports_claims": ["C052"]
    },
    {
        "evidence_id": "E033",
        "content": "Image interpretation was performed blind, without knowledge of MTS site locations, until after image analysis and ground control were complete.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Image interpretation was performed blind, without knowledge of the location of sites previously identified by the MTS. Only after image analysis and ground control were complete did we compare the sites and off-site scatters newly discovered through remote sensing with previously known sites.",
        "page": 426,
        "relevance": "Documents blinded experimental design",
        "supports_claims": ["C053", "C054"]
    },
    {
        "evidence_id": "E034",
        "content": "Before georeferencing using ground control points, the image had a root mean square error (RMSE) of 14 m.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Before georeferencing using ground control points, the image had a root mean square error (RMSE) of 14 m",
        "page": 426,
        "relevance": "Documents initial geolocation accuracy",
        "supports_claims": ["C055"]
    },
    {
        "evidence_id": "E035",
        "content": "After georeferencing by Samsung Lim, image accuracy was improved to an RMSE of approximately 3 m.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "After georeferencing by Samsung Lim, its accuracy was improved to an RMSE of approximately 3 m",
        "page": 426,
        "relevance": "Documents improved geolocation accuracy",
        "supports_claims": ["C056", "C057"]
    },
    {
        "evidence_id": "E036",
        "content": "The image was projected onto WGS 84, UTM 33N coordinate system.",
        "evidence_type": "technical_specification",
        "verbatim_quote": "After georeferencing, the image was projected onto a local coordinate system (WGS 84, UTM 33N)",
        "page": 426,
        "relevance": "Specifies coordinate system used",
        "supports_claims": ["C058"]
    },
    {
        "evidence_id": "E037",
        "content": "The two components of the image were combined so that the higher spatial resolution of the panchromatic layer was enriched by multispectral layer information.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "and the two components of the image were combined so that the higher spatial resolution of the panchromatic layer was enriched by information from the multispectral layer.",
        "page": 426,
        "relevance": "Describes pan-sharpening or image fusion",
        "supports_claims": ["C059"]
    },
    {
        "evidence_id": "E038",
        "content": "Archaeological analysis of satellite images relies on the assumption that certain spatial and spectral patterns of vegetation or topsoil can be correlated with buried archaeological remains.",
        "evidence_type": "theoretical_premise",
        "verbatim_quote": "Archaeological analysis of satellite images relies on the assumption that certain spatial and spectral patterns or characteristics of vegetation or topsoil can be correlated with buried archaeological remains",
        "page": 426,
        "relevance": "States fundamental methodological assumption",
        "supports_claims": ["C060"]
    },
    {
        "evidence_id": "E039",
        "content": "Conventional bird's eye photographs have been used for decades to identify soil marks, crop marks, and shadow marks indicating past human activity.",
        "evidence_type": "literature_observation",
        "verbatim_quote": "For many decades conventional photographs taken from a bird's eye perspective have been used to identify patterns such as soil marks, crop marks, and shadow marks that may indicate past human activity (Crawford 1929; Partington 1983; Riley 1987).",
        "page": 426,
        "relevance": "Provides historical context for technique",
        "supports_claims": ["C061"]
    },
    {
        "evidence_id": "E040",
        "content": "Some patterns become visible only through manipulation of color bands in multispectral satellite imagery.",
        "evidence_type": "technical_observation",
        "verbatim_quote": "Some of these patterns, however, only become visible through manipulation of the various color bands that constitute multispectral satellite imagery (typically blue, green, red, and NIR).",
        "page": 426,
        "relevance": "Explains advantage of multispectral over panchromatic",
        "supports_claims": ["C062"]
    },
    {
        "evidence_id": "E041",
        "content": "Indicators of buried archaeological remains amenable to spectral analysis include vegetation vigor and soil moisture.",
        "evidence_type": "technical_observation",
        "verbatim_quote": "Indicators of buried archaeological remains amenable to spectral analysis include vegetation vigor and soil moisture.",
        "page": 426,
        "relevance": "Identifies key spectral indicators",
        "supports_claims": ["C063"]
    },
    {
        "evidence_id": "E042",
        "content": "Analysis began with band combinations prioritizing red and NIR, as they best reveal differences in vegetation growth associated with subsurface remains.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Our analysis began with band combinations prioritizing red and NIR, as they best reveal differences in vegetation growth sometimes associated with subsurface archaeological remains.",
        "page": 426,
        "relevance": "Documents initial analytical strategy",
        "supports_claims": ["C064"]
    },
    {
        "evidence_id": "E043",
        "content": "The ratio of NIR to red light reflected from plants indicates vegetation health, revealing soil and substrate quality.",
        "evidence_type": "technical_principle",
        "verbatim_quote": "The ratio of NIR to red light reflected from plants indicates the health of vegetation, in turn revealing the quality of the soil and substrate.",
        "page": 426,
        "relevance": "Explains technical principle behind vegetation analysis",
        "supports_claims": ["C065"]
    },
    {
        "evidence_id": "E044",
        "content": "Chlorophyll in healthy vegetation reflects NIR and absorbs red light.",
        "evidence_type": "technical_principle",
        "verbatim_quote": "The chlorophyll in healthy vegetation reflects NIR and absorbs red.",
        "page": 426,
        "relevance": "Explains spectral behavior of healthy vegetation",
        "supports_claims": ["C066"]
    },
    {
        "evidence_id": "E045",
        "content": "Stressed plants are associated with low NIR and high red values.",
        "evidence_type": "technical_principle",
        "verbatim_quote": "Conversely, stressed plants are associated with low NIR and high red values.",
        "page": 426,
        "relevance": "Explains spectral behavior of stressed vegetation",
        "supports_claims": ["C067"]
    },
    {
        "evidence_id": "E046",
        "content": "Contrasts between high NIR and high red values were sought primarily through manual band recombination (e.g., 4-1-4 displaying NIR as purple and red as green).",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Contrasts between high NIR values (healthy vegetation) and high red values (stressed vegetation) were sought primarily through manual band recombination displaying, for example, NIR as purple and red as green while excluding all other color information (a 4-1-4 band combination).",
        "page": 426,
        "relevance": "Describes specific analytical technique used",
        "supports_claims": ["C068"]
    },
    {
        "evidence_id": "E047",
        "content": "Manual band recombination results were supplemented with transformations such as NDVI, though Principal Component Analysis did not prove useful.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "The results of manual band recombination were then supplemented with transformations such as NDVI and Principal Component Analysis, although the latter did not prove useful in our study",
        "page": 427,
        "relevance": "Documents additional analytical techniques and their utility",
        "supports_claims": ["C069", "C070"]
    },
    {
        "evidence_id": "E048",
        "content": "Wide variation in NIR versus red reflectance across the large study area led to using NDVI primarily for quick bare/vegetated distinction and confirmation rather than as principal detection means.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Since there is such wide variation in NIR versus red reflectance produced by variable ground cover across our large study area, we used NDVI primarily to quickly distinguish between bare and vegetated areas and to confirm discoveries made through manual band recombination rather than as the principal means for detecting crop marks.",
        "page": 428,
        "relevance": "Explains adapted use of NDVI for this study",
        "supports_claims": ["C071"]
    },
    {
        "evidence_id": "E049",
        "content": "Different soil characteristics (texture, chemistry, moisture) produce distinct spectral responses visible as soil marks.",
        "evidence_type": "technical_principle",
        "verbatim_quote": "Different soil characteristics (e.g., texture, chemistry, moisture, etc.) produce distinct spectral responses visible as \"soil marks\" in aerial photography or satellite imagery (Riley 1983: 9).",
        "page": 428,
        "relevance": "Explains origin of soil mark visibility",
        "supports_claims": ["C072"]
    },
    {
        "evidence_id": "E050",
        "content": "Soil marks appear as lighter spots against darker background, likely due to differences in soil moisture from better drainage or subsurface masonry presence.",
        "evidence_type": "interpretive_observation",
        "verbatim_quote": "Some soil marks, for example, may appear as lighter spots against the darker background for most of the year (e.g., F1025; see figs. 4A–B). The higher reflectance in this case can probably be attributed to differences in soil moisture resulting from the better drainage of disturbed soils and/or the presence of subsurface masonry",
        "page": 428,
        "relevance": "Interprets mechanism behind specific soil mark type",
        "supports_claims": ["C073"]
    },
    {
        "evidence_id": "E051",
        "content": "Thin, xeric, and calcareous soils in the Murge are sensitive to moisture fluctuations, facilitating soil mark detectability.",
        "evidence_type": "environmental_observation",
        "verbatim_quote": "The level of contrast will depend on particular soil types and season; thin, xeric, and calcareous soils such as those in the Murge are fairly sensitive to fluctuations in moisture and other disturbances, facilitating the detectability of soil marks.",
        "page": 428,
        "relevance": "Explains environmental factors enhancing detection",
        "supports_claims": ["C074"]
    },
    {
        "evidence_id": "E052",
        "content": "Soil marks caused by texture and chemical composition variations appear across all bands of a multispectral image.",
        "evidence_type": "technical_observation",
        "verbatim_quote": "Soil marks, which are caused by variations in texture and chemical composition, tend to appear across all bands of a multispectral image",
        "page": 428,
        "relevance": "Distinguishes soil marks from crop marks spectrally",
        "supports_claims": ["C075"]
    },
    {
        "evidence_id": "E053",
        "content": "Some soil marks from plowed bedrock were readily visible in panchromatic image, while others appeared more clearly in particular band combinations.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "In our image, some soil marks, particularly where bedrock had been plowed into surface soils, were readily visible in the panchromatic image (FIG. 3A). Elsewhere, soil marks appeared more clearly in a particular band combination, as was the case with Feature F1014",
        "page": 428,
        "relevance": "Documents variability in soil mark visibility across bands",
        "supports_claims": ["C076"]
    },
    {
        "evidence_id": "E054",
        "content": "Idiosyncrasies in the image were selected for ground control based on whether they displayed distinctive patterns without obvious natural or modern explanation.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Idiosyncrasies in our image were selected for ground control based on whether or not they displayed distinctive patterns that had no immediately obvious natural or modern explanation.",
        "page": 428,
        "relevance": "Describes feature selection criteria",
        "supports_claims": ["C077"]
    },
    {
        "evidence_id": "E055",
        "content": "Both rectilinear and circular patterns were scrutinized under the assumption that Greek and Roman sites would be rectilinear while prehistoric sites might be circular.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Both rectilinear and circular patterns were scrutinized under the working assumption that Greek and Roman sites would have a rectilinear form, while prehistoric sites might be circular.",
        "page": 428,
        "relevance": "Documents pattern recognition strategy",
        "supports_claims": ["C078"]
    },
    {
        "evidence_id": "E056",
        "content": "Particular attention was paid to features not aligned with modern field system, roads, or structures.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Particular attention was paid to features that did not align with the modern field system, roads, or structures such as field division walls.",
        "page": 428,
        "relevance": "Describes discrimination strategy for ancient features",
        "supports_claims": ["C079"]
    },
    {
        "evidence_id": "E057",
        "content": "The most effective approach involved using a limited range of manual band combinations (4-2-1; 4-1-2; 4-1-4) with attention to idiosyncratic features not aligned with modern structures.",
        "evidence_type": "methodological_conclusion",
        "verbatim_quote": "In short, over the course of analyzing this image we found that, given the constraints of time and resources, the most effective way to quickly evaluate a large image with wide variations in vegetation cover, topography, and other parameters involved the use of a limited range of manual band combinations (4-2-1; 4-1-2; 4-1-4), paying special attention to idiosyncratic features that did not align with the orientation of modern structures and field divisions.",
        "page": 428,
        "relevance": "Summarizes optimal analytical strategy developed",
        "supports_claims": ["C080"]
    },
    {
        "evidence_id": "E058",
        "content": "Features were identified visually as spatial patterns in reflectance intensity, usually in band combinations emphasizing red/NIR contrast.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Features were identified visually; in most cases they appeared as spatial patterns in the intensity of reflectance, usually in band combinations emphasizing the contrast between red and NIR.",
        "page": 428,
        "relevance": "Describes visual identification method",
        "supports_claims": ["C081"]
    },
    {
        "evidence_id": "E059",
        "content": "Determining whether patterns were crop or soil marks usually required ground control, though careful comparison of images and transformations sometimes allowed determination.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Sometimes we could determine whether these patterns were crop or soil marks through careful comparison of the panchromatic and multispectral images and automated transformations, but in most cases doing so required ground control.",
        "page": 428,
        "relevance": "Emphasizes importance of ground control for interpretation",
        "supports_claims": ["C082"]
    },
    {
        "evidence_id": "E060",
        "content": "Immediate feedback from simultaneous ground control improved image interpretation by allowing exclusion of false positive spectral responses and identification of productive patterns.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "The immediate feedback provided by simultaneous ground control improved image interpretation; spectral responses associated with false positives identified early in the process could be excluded as the analysis proceeded, while those associated with ancient surface material could be sought out.",
        "page": 428,
        "relevance": "Explains benefit of concurrent ground control",
        "supports_claims": ["C083"]
    }
]

# ============================================================================
# CLAIMS - Liberal extraction
# ============================================================================

claims_items = [
    {
        "claim_id": "C048",
        "content": "Image processing followed a standardized sequence beginning with georeferencing and projection, followed by overlay and enhancement.",
        "claim_type": "methodological_description",
        "verbatim_quote": "Analysis of the imagery began with georeferencing and projection, followed by image overlay and enhancement.",
        "page": 426,
        "supporting_evidence": ["E029"],
        "confidence": "high",
        "relevance": "Documents methodological workflow"
    },
    {
        "claim_id": "C049",
        "content": "Concurrent ground control improves feature identification accuracy through immediate feedback.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Ground control was carried out concurrently with feature identification because of time constraints and to improve the accuracy of feature identification through immediate feedback from the field.",
        "page": 426,
        "supporting_evidence": ["E030"],
        "confidence": "high",
        "relevance": "Asserts advantage of concurrent approach"
    },
    {
        "claim_id": "C050",
        "content": "Time constraints justified concurrent rather than sequential ground control.",
        "claim_type": "methodological_justification",
        "verbatim_quote": "Ground control was carried out concurrently with feature identification because of time constraints",
        "page": 426,
        "supporting_evidence": ["E030"],
        "confidence": "high",
        "relevance": "Explains practical rationale for approach"
    },
    {
        "claim_id": "C051",
        "content": "Iterative refinement using ground control feedback improves feature identification by eliminating false spectral patterns.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Information from ground control was used to refine ongoing feature identification in the image, as spectral responses or patterns consistently denoting modern or natural features were eliminated from consideration",
        "page": 426,
        "supporting_evidence": ["E031"],
        "confidence": "high",
        "relevance": "Describes learning process during analysis"
    },
    {
        "claim_id": "C052",
        "content": "Ground control serves multiple functions including both validation of new discoveries and mapping of known sites.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Ground control also provided the location and extent of sites and off-site scatters as defined by the MTS.",
        "page": 426,
        "supporting_evidence": ["E032"],
        "confidence": "high",
        "relevance": "Identifies dual purpose of ground control"
    },
    {
        "claim_id": "C053",
        "content": "Blind interpretation without knowledge of known site locations avoids introducing bias favoring areas with known sites.",
        "claim_type": "methodological_justification",
        "verbatim_quote": "This approach was employed in order to compare the results of remote sensing with surface survey and to avoid introducing a bias in favor of areas with known sites.",
        "page": 426,
        "supporting_evidence": ["E033"],
        "confidence": "high",
        "relevance": "Justifies experimental design choice"
    },
    {
        "claim_id": "C054",
        "content": "Blind methodology allows valid comparison between remote sensing and surface survey discovery rates.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "This approach was employed in order to compare the results of remote sensing with surface survey",
        "page": 426,
        "supporting_evidence": ["E033"],
        "confidence": "high",
        "relevance": "Establishes purpose of blind design"
    },
    {
        "claim_id": "C055",
        "content": "Initial image geolocation accuracy of 14 m RMSE was insufficient for archaeological purposes.",
        "claim_type": "technical_evaluation",
        "verbatim_quote": "Before georeferencing using ground control points, the image had a root mean square error (RMSE) of 14 m",
        "page": 426,
        "supporting_evidence": ["E034"],
        "confidence": "high",
        "relevance": "Establishes need for georeferencing"
    },
    {
        "claim_id": "C056",
        "content": "Georeferencing improved image accuracy to approximately 3 m RMSE, an excellent result.",
        "claim_type": "technical_evaluation",
        "verbatim_quote": "After georeferencing by Samsung Lim, its accuracy was improved to an RMSE of approximately 3 m, an excellent result",
        "page": 426,
        "supporting_evidence": ["E035"],
        "confidence": "high",
        "relevance": "Documents georeferencing success"
    },
    {
        "claim_id": "C057",
        "content": "The low off-nadir angle of the image facilitated achieving excellent georeferencing results.",
        "claim_type": "technical_assertion",
        "verbatim_quote": "an excellent result facilitated by the low off-nadir angle of the image.",
        "page": 426,
        "supporting_evidence": ["E035"],
        "confidence": "high",
        "relevance": "Explains factor enabling accurate georeferencing"
    },
    {
        "claim_id": "C058",
        "content": "Further correction beyond 3 m RMSE (such as orthorectification) was not worthwhile given artifact scatter size and variability.",
        "claim_type": "methodological_justification",
        "verbatim_quote": "The investigators determined that no further correction (such as orthorectification) would be worthwhile since the size and variability of an artifact scatter (the most common archaeological phenomenon encountered) does not require more precise mapping.",
        "page": 426,
        "supporting_evidence": ["E036"],
        "confidence": "high",
        "relevance": "Justifies sufficiency of achieved accuracy"
    },
    {
        "claim_id": "C059",
        "content": "Combining panchromatic and multispectral layers enriches spatial resolution with spectral information.",
        "claim_type": "technical_assertion",
        "verbatim_quote": "the two components of the image were combined so that the higher spatial resolution of the panchromatic layer was enriched by information from the multispectral layer.",
        "page": 426,
        "supporting_evidence": ["E037"],
        "confidence": "high",
        "relevance": "Describes purpose of image fusion"
    },
    {
        "claim_id": "C060",
        "content": "Archaeological remote sensing fundamentally relies on correlation between spectral/spatial patterns and buried remains.",
        "claim_type": "theoretical_claim",
        "verbatim_quote": "Archaeological analysis of satellite images relies on the assumption that certain spatial and spectral patterns or characteristics of vegetation or topsoil can be correlated with buried archaeological remains",
        "page": 426,
        "supporting_evidence": ["E038"],
        "confidence": "high",
        "relevance": "States foundational methodological assumption"
    },
    {
        "claim_id": "C061",
        "content": "Aerial photograph interpretation for archaeology has a long established history dating to the early 20th century.",
        "claim_type": "historical_claim",
        "verbatim_quote": "For many decades conventional photographs taken from a bird's eye perspective have been used to identify patterns such as soil marks, crop marks, and shadow marks that may indicate past human activity (Crawford 1929; Partington 1983; Riley 1987).",
        "page": 426,
        "supporting_evidence": ["E039"],
        "confidence": "high",
        "relevance": "Provides historical context for technique"
    },
    {
        "claim_id": "C062",
        "content": "Multispectral imagery reveals patterns invisible in conventional photography through band manipulation.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Some of these patterns, however, only become visible through manipulation of the various color bands that constitute multispectral satellite imagery",
        "page": 426,
        "supporting_evidence": ["E040"],
        "confidence": "high",
        "relevance": "Asserts unique capability of multispectral approach"
    },
    {
        "claim_id": "C063",
        "content": "Vegetation vigor and soil moisture are key indicators for detecting buried archaeological remains through spectral analysis.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Indicators of buried archaeological remains amenable to spectral analysis include vegetation vigor and soil moisture.",
        "page": 426,
        "supporting_evidence": ["E041"],
        "confidence": "high",
        "relevance": "Identifies primary detection indicators"
    },
    {
        "claim_id": "C064",
        "content": "Red and NIR bands are prioritized because they best reveal vegetation differences associated with subsurface remains.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Our analysis began with band combinations prioritizing red and NIR, as they best reveal differences in vegetation growth sometimes associated with subsurface archaeological remains.",
        "page": 426,
        "supporting_evidence": ["E042"],
        "confidence": "high",
        "relevance": "Justifies analytical band priority"
    },
    {
        "claim_id": "C065",
        "content": "NIR/red ratio in plant reflectance serves as an indicator of soil and substrate quality.",
        "claim_type": "technical_principle",
        "verbatim_quote": "The ratio of NIR to red light reflected from plants indicates the health of vegetation, in turn revealing the quality of the soil and substrate.",
        "page": 426,
        "supporting_evidence": ["E043"],
        "confidence": "high",
        "relevance": "Explains detection mechanism"
    },
    {
        "claim_id": "C066",
        "content": "Positive crop marks (healthy vegetation with high NIR, low red) may reveal features like filled ditches containing moist, nutrient-rich soil.",
        "claim_type": "interpretive_principle",
        "verbatim_quote": "Such \"positive\" crop or weed marks may identify aerated, moist, or fertile soils, sometimes revealing filled ditches, graves, or other \"cuts\" containing disturbed soil that retain water and nutrients.",
        "page": 426,
        "supporting_evidence": ["E044"],
        "confidence": "high",
        "relevance": "Explains positive anomaly interpretation"
    },
    {
        "claim_id": "C067",
        "content": "Negative crop marks (stressed vegetation with low NIR, high red) may reveal subsurface masonry depriving plants of water and nutrients.",
        "claim_type": "interpretive_principle",
        "verbatim_quote": "These \"negative\" crop or weed marks may reveal packed, dry, or infertile soils, sometimes indicating underground masonry that is depriving plants of water and nutrients",
        "page": 426,
        "supporting_evidence": ["E045"],
        "confidence": "high",
        "relevance": "Explains negative anomaly interpretation"
    },
    {
        "claim_id": "C068",
        "content": "Manual band recombination is an effective technique for revealing vegetation health contrasts.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Contrasts between high NIR values (healthy vegetation) and high red values (stressed vegetation) were sought primarily through manual band recombination",
        "page": 426,
        "supporting_evidence": ["E046"],
        "confidence": "high",
        "relevance": "Identifies primary analytical technique"
    },
    {
        "claim_id": "C069",
        "content": "NDVI transformation supplements manual band recombination for vegetation analysis.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "The results of manual band recombination were then supplemented with transformations such as NDVI",
        "page": 427,
        "supporting_evidence": ["E047"],
        "confidence": "high",
        "relevance": "Documents complementary technique"
    },
    {
        "claim_id": "C070",
        "content": "Principal Component Analysis did not prove useful in this study.",
        "claim_type": "methodological_evaluation",
        "verbatim_quote": "and Principal Component Analysis, although the latter did not prove useful in our study",
        "page": 427,
        "supporting_evidence": ["E047"],
        "confidence": "high",
        "relevance": "Documents unsuccessful technique"
    },
    {
        "claim_id": "C071",
        "content": "In large study areas with variable ground cover, NDVI is better used for quick classification and confirmation than as primary detection tool.",
        "claim_type": "methodological_recommendation",
        "verbatim_quote": "Since there is such wide variation in NIR versus red reflectance produced by variable ground cover across our large study area, we used NDVI primarily to quickly distinguish between bare and vegetated areas and to confirm discoveries made through manual band recombination rather than as the principal means for detecting crop marks.",
        "page": 428,
        "supporting_evidence": ["E048"],
        "confidence": "high",
        "relevance": "Offers context-specific methodological guidance"
    },
    {
        "claim_id": "C072",
        "content": "Soil marks arise from spectral differences caused by variations in soil texture, chemistry, and moisture.",
        "claim_type": "technical_principle",
        "verbatim_quote": "Different soil characteristics (e.g., texture, chemistry, moisture, etc.) produce distinct spectral responses visible as \"soil marks\"",
        "page": 428,
        "supporting_evidence": ["E049"],
        "confidence": "high",
        "relevance": "Explains soil mark origin"
    },
    {
        "claim_id": "C073",
        "content": "Lighter soil marks likely result from moisture differences due to better drainage or subsurface masonry.",
        "claim_type": "interpretive_claim",
        "verbatim_quote": "The higher reflectance in this case can probably be attributed to differences in soil moisture resulting from the better drainage of disturbed soils and/or the presence of subsurface masonry",
        "page": 428,
        "supporting_evidence": ["E050"],
        "confidence": "medium",
        "relevance": "Interprets specific soil mark type"
    },
    {
        "claim_id": "C074",
        "content": "Thin, xeric, calcareous soils like those in the Murge enhance soil mark detectability due to moisture sensitivity.",
        "claim_type": "environmental_assertion",
        "verbatim_quote": "thin, xeric, and calcareous soils such as those in the Murge are fairly sensitive to fluctuations in moisture and other disturbances, facilitating the detectability of soil marks.",
        "page": 428,
        "supporting_evidence": ["E051"],
        "confidence": "high",
        "relevance": "Connects soil type to detection capability"
    },
    {
        "claim_id": "C075",
        "content": "Soil marks should be more easily traceable than crop marks because they appear across all spectral bands.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "As a result, soil marks should be more easily traceable than crop marks, a phenomenon dependant upon subtle differences in the vegetation health visible only in particular band combinations.",
        "page": 428,
        "supporting_evidence": ["E052"],
        "confidence": "medium",
        "relevance": "Compares detectability of mark types"
    },
    {
        "claim_id": "C076",
        "content": "Soil mark visibility varies across spectral bands depending on their origin (plowed bedrock vs. compositional differences).",
        "claim_type": "technical_observation",
        "verbatim_quote": "In our image, some soil marks, particularly where bedrock had been plowed into surface soils, were readily visible in the panchromatic image (FIG. 3A). Elsewhere, soil marks appeared more clearly in a particular band combination",
        "page": 428,
        "supporting_evidence": ["E053"],
        "confidence": "high",
        "relevance": "Documents variability in soil mark detection"
    },
    {
        "claim_id": "C077",
        "content": "Ground control is necessary for distinguishing soil marks from crop marks and determining their nature.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Determining the nature of soil marks and distinguishing soil marks from crop or weed marks requires ground control, especially when considering a large image.",
        "page": 428,
        "supporting_evidence": ["E054"],
        "confidence": "high",
        "relevance": "Emphasizes importance of ground-truthing"
    },
    {
        "claim_id": "C078",
        "content": "Cultural period can be inferred from feature shape (rectilinear for Greek/Roman, circular for prehistoric).",
        "claim_type": "interpretive_assumption",
        "verbatim_quote": "Both rectilinear and circular patterns were scrutinized under the working assumption that Greek and Roman sites would have a rectilinear form, while prehistoric sites might be circular.",
        "page": 428,
        "supporting_evidence": ["E055"],
        "confidence": "medium",
        "relevance": "Documents chronological interpretation strategy"
    },
    {
        "claim_id": "C079",
        "content": "Features misaligned with modern field patterns are more likely to be ancient.",
        "claim_type": "interpretive_principle",
        "verbatim_quote": "Particular attention was paid to features that did not align with the modern field system, roads, or structures such as field division walls.",
        "page": 428,
        "supporting_evidence": ["E056"],
        "confidence": "high",
        "relevance": "Describes discrimination criterion"
    },
    {
        "claim_id": "C080",
        "content": "A limited range of manual band combinations (4-2-1; 4-1-2; 4-1-4) focusing on misaligned features provides the most efficient large-area analysis.",
        "claim_type": "methodological_recommendation",
        "verbatim_quote": "the most effective way to quickly evaluate a large image with wide variations in vegetation cover, topography, and other parameters involved the use of a limited range of manual band combinations (4-2-1; 4-1-2; 4-1-4), paying special attention to idiosyncratic features that did not align with the orientation of modern structures and field divisions.",
        "page": 428,
        "supporting_evidence": ["E057"],
        "confidence": "high",
        "relevance": "Synthesizes optimal analytical strategy"
    },
    {
        "claim_id": "C081",
        "content": "Visual identification of spatial patterns in reflectance is the primary feature detection method.",
        "claim_type": "methodological_description",
        "verbatim_quote": "Features were identified visually; in most cases they appeared as spatial patterns in the intensity of reflectance",
        "page": 428,
        "supporting_evidence": ["E058"],
        "confidence": "high",
        "relevance": "Describes detection approach"
    },
    {
        "claim_id": "C082",
        "content": "Ground control is usually necessary to determine whether patterns are crop marks or soil marks.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "but in most cases doing so required ground control.",
        "page": 428,
        "supporting_evidence": ["E059"],
        "confidence": "high",
        "relevance": "Emphasizes ground control necessity"
    },
    {
        "claim_id": "C083",
        "content": "Simultaneous ground control enables iterative learning that improves feature identification during analysis.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "The immediate feedback provided by simultaneous ground control improved image interpretation; spectral responses associated with false positives identified early in the process could be excluded as the analysis proceeded, while those associated with ancient surface material could be sought out.",
        "page": 428,
        "supporting_evidence": ["E060"],
        "confidence": "high",
        "relevance": "Explains advantage of concurrent methodology"
    }
]

# ============================================================================
# IMPLICIT ARGUMENTS
# ============================================================================

implicit_arguments = [
    {
        "implicit_argument_id": "IA011",
        "content": "3 m RMSE is sufficient accuracy for mapping archaeological scatters (implied by decision not to orthorectify further).",
        "argument_type": "unstated_premise",
        "trigger_text": "no further correction (such as orthorectification) would be worthwhile since the size and variability of an artifact scatter... does not require more precise mapping.",
        "page": 426,
        "reconstruction_confidence": "high",
        "related_claims": ["C056", "C058"],
        "critical_for_logic": True,
        "notes": "Threshold for adequate precision implied by stopping point"
    },
    {
        "implicit_argument_id": "IA012",
        "content": "Knowing the location of previously discovered sites would bias analysts toward confirming known sites rather than discovering new ones (implied by blind methodology).",
        "argument_type": "unstated_assumption",
        "trigger_text": "to avoid introducing a bias in favor of areas with known sites.",
        "page": 426,
        "reconstruction_confidence": "high",
        "related_claims": ["C053"],
        "critical_for_logic": True,
        "notes": "Assumption about analyst bias drives experimental design"
    },
    {
        "implicit_argument_id": "IA013",
        "content": "Iterative learning during analysis is methodologically acceptable and improves results (implied by use of feedback to refine criteria).",
        "argument_type": "methodological_assumption",
        "trigger_text": "spectral responses or patterns consistently denoting modern or natural features were eliminated from consideration and characteristics of features frequently associated with ancient surface material became clearer.",
        "page": 426,
        "reconstruction_confidence": "high",
        "related_claims": ["C051", "C083"],
        "critical_for_logic": False,
        "notes": "Adaptive methodology contrasts with purely a priori approach"
    },
    {
        "implicit_argument_id": "IA014",
        "content": "Manual band recombination is superior to automated transformations for this type of analysis (implied by emphasis on manual approach).",
        "argument_type": "unstated_premise",
        "trigger_text": "primarily through manual band recombination... supplemented with transformations such as NDVI",
        "page": 426,
        "reconstruction_confidence": "medium",
        "related_claims": ["C068", "C069", "C071"],
        "critical_for_logic": False,
        "notes": "Prioritization of manual over automated methods"
    },
    {
        "implicit_argument_id": "IA015",
        "content": "Ancient features have different orientations than modern agricultural features (implied by using alignment as discrimination criterion).",
        "argument_type": "unstated_premise",
        "trigger_text": "Particular attention was paid to features that did not align with the modern field system, roads, or structures",
        "page": 428,
        "reconstruction_confidence": "high",
        "related_claims": ["C079"],
        "critical_for_logic": True,
        "notes": "Temporal discrimination based on orientation difference"
    },
    {
        "implicit_argument_id": "IA016",
        "content": "Visual pattern recognition by trained analysts is reliable for feature identification (implied by reliance on visual identification).",
        "argument_type": "unstated_assumption",
        "trigger_text": "Features were identified visually; in most cases they appeared as spatial patterns in the intensity of reflectance",
        "page": 428,
        "reconstruction_confidence": "medium",
        "related_claims": ["C081"],
        "critical_for_logic": True,
        "notes": "Human interpretation assumed to be effective detection method"
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
    'section': 'Section 3: Methods (Georeferencing + Image Analysis)',
    'pages': '426-428',
    'word_count_estimate': 1300,
    'items_extracted': {
        'evidence': len(evidence_items),
        'claims': len(claims_items),
        'implicit_arguments': len(implicit_arguments)
    },
    'notes': 'Dense technical section with extensive methodological detail. High concentration of evidence about procedures and technical principles. Many claims about analytical techniques, detection mechanisms, and interpretation strategies. Rich source for future RDMAP extraction.'
})

with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print(f"✓ Pass 1, Section 3 complete: Methods (Georeferencing + Image Analysis)")
print(f"  - Evidence items: {len(evidence_items)}")
print(f"  - Claims: {len(claims_items)}")
print(f"  - Implicit arguments: {len(implicit_arguments)}")
print(f"  - Total items this section: {len(evidence_items) + len(claims_items) + len(implicit_arguments)}")
print(f"  - Running total: {len(data['evidence'])} evidence, {len(data['claims'])} claims, {len(data['implicit_arguments'])} implicit arguments")
