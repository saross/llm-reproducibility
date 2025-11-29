#!/usr/bin/env python3
"""
Pass 3: Liberal RDMAP Extraction (Research Designs, Methods, Protocols)
Ross et al. 2009 - Remote Sensing and Archaeological Prospection in Apulia, Italy

CRITICAL INSTRUCTIONS FROM USER:
1. Use SAME 6 section groups as Pass 1
2. Liberal extraction - cast wide net, aim for over-extraction (40-50% more)
3. Pay EQUAL attention to ALL sections (not over-focus on Methods)
4. Be ESPECIALLY liberal with research designs (commonly under-extracted)

Section groups (mirroring Pass 1):
1. Abstract + Introduction
2. L'Amastuola Project + Satellite Data
3. Methods (Georeferencing + Image Analysis)
4. Methods (Ground Control)
5. Results + Comparison
6. Environment/Geology + Conclusions

Target: 30-45 RDMAP items (liberal, will rationalize in Pass 5)
"""

import json
from datetime import datetime, timezone
from pathlib import Path

extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

print("=" * 70)
print("PASS 3: LIBERAL RDMAP EXTRACTION")
print("=" * 70)
print("Approach: Liberal extraction across ALL 6 sections")
print("Special focus: Research designs (commonly under-extracted)")
print()

#================================================================
# RESEARCH DESIGNS - Extract from ALL sections, especially liberal
#================================================================

research_designs = [
    {
        "research_design_id": "RD001",
        "content": "Integrated multi-method archaeological prospection combining remote sensing, ground control, surface survey, and environmental research",
        "verbatim_quote": "When deployed in combination with ground control, archaeological surface survey, and environmental research, remote sensing based upon high-resolution multispectral satellite imagery allows large areas to be evaluated efficiently",
        "page": 423,
        "design_type": "integrated_approach",
        "child_methods": ["M001", "M002", "M003", "M004"],
        "rationale": "Core overarching research design integrating multiple complementary methods"
    },
    {
        "research_design_id": "RD002",
        "content": "Comparative evaluation design contrasting remote sensing with systematic surface survey (MTS) using independent baseline data",
        "verbatim_quote": "Earlier fieldwork by the Murge Tableland Survey (MTS) provided independent definitions for various types of sites and a large sample of sites and off-site scatters in the study area. Comparison of our remote-sensing–guided efforts with the results of that survey suggests that our success rate is too high to be explained by random association",
        "page": 423,
        "design_type": "comparative_study",
        "child_methods": ["M005", "M006"],
        "rationale": "Comparative framework enabling methodological assessment"
    },
    {
        "research_design_id": "RD003",
        "content": "Iterative image analysis and ground control design with immediate feedback loop for pattern refinement",
        "verbatim_quote": "The process, built around iterative image analysis and ground control, led to the discovery of previously unknown sites... Information from ground control was used to refine ongoing feature identification in the image",
        "page": 424,
        "design_type": "iterative_methodology",
        "child_methods": ["M007", "M008"],
        "rationale": "Iterative learning design central to methodology"
    },
    {
        "research_design_id": "RD004",
        "content": "Blind interpretation design to avoid bias toward known site locations when evaluating remote sensing effectiveness",
        "verbatim_quote": "Image interpretation was performed blind, without knowledge of the location of sites previously identified by the MTS. Only after image analysis and ground control were complete did we compare the sites and off-site scatters newly discovered through remote sensing with previously known sites. This approach was employed in order to compare the results of remote sensing with surface survey and to avoid introducing a bias in favor of areas with known sites.",
        "page": 426,
        "design_type": "experimental_control",
        "child_methods": ["M009"],
        "rationale": "Experimental design element ensuring valid comparison"
    }
]

#================================================================
# METHODS - Extract liberally from ALL sections
#================================================================

methods = [
    {
        "method_id": "M001",
        "content": "High-resolution multispectral satellite imagery analysis (QuickBird) for archaeological feature detection",
        "verbatim_quote": "Our project evaluated 100 sq km of high-resolution multispectral imagery using established methods of image analysis to discover features associated with past human activity.",
        "page": 424,
        "implements_design": "RD001",
        "child_protocols": ["P001", "P002", "P003", "P004", "P005", "P006", "P007"]
    },
    {
        "method_id": "M002",
        "content": "Ground control field verification through systematic feature visitation and surface material assessment",
        "verbatim_quote": "Ground control was carried out concurrently with feature identification because of time constraints and to improve the accuracy of feature identification through immediate feedback from the field.",
        "page": 426,
        "implements_design": "RD001",
        "child_protocols": ["P008", "P009", "P010", "P011", "P012"]
    },
    {
        "method_id": "M003",
        "content": "Geological and environmental investigation to determine feature origin and settlement-environment relationships",
        "verbatim_quote": "Image analysis was supplemented and extended by ground control and geological investigation to improve the accuracy and efficiency of site detection, as well as to determine the nature of the relationship between the features visible in the image and archaeological evidence found in the field.",
        "page": 424,
        "implements_design": "RD001",
        "child_protocols": []
    },
    {
        "method_id": "M004",
        "content": "Systematic archaeological surface survey (MTS methodology) providing comparative baseline",
        "verbatim_quote": "The MTS, a sister project conducted between 2003 and 2007, involved systematic survey of a transect extending from the coastal plain of Taranto into the karstic Murge uplands.",
        "page": 424,
        "implements_design": "RD001",
        "child_protocols": []
    },
    {
        "method_id": "M005",
        "content": "Quantitative comparison of discovery rates against expected random distribution",
        "verbatim_quote": "The MTS, which explored a representative transect of our study area, yielded an average of 6.3 sites and off-site scatters per sq km (63 sites in total). At this rate, an area the size of that analyzed during remote sensing ground control (1.45 sq km) should have produced a total of about nine ancient sites and off-site scatters. The discovery of 29 sites and off-site scatters exceeds the number expected from a randomly chosen area of equal size by more than three times.",
        "page": 432,
        "implements_design": "RD002",
        "child_protocols": ["P013"]
    },
    {
        "method_id": "M006",
        "content": "False negative analysis comparing remote sensing discoveries with comprehensive survey results",
        "verbatim_quote": "\"False negatives,\" sites or off-site scatters previously discovered by the MTS but not detected during our image analysis (FIG. 6), also reveal the value and limitations of remote sensing.",
        "page": 432,
        "implements_design": "RD002",
        "child_protocols": ["P014"]
    },
    {
        "method_id": "M007",
        "content": "Concurrent image analysis and ground control with immediate feedback for pattern refinement",
        "verbatim_quote": "Information from ground control was used to refine ongoing feature identification in the image, as spectral responses or patterns consistently denoting modern or natural features were eliminated from consideration and characteristics of features frequently associated with ancient surface material became clearer.",
        "page": 426,
        "implements_design": "RD003",
        "child_protocols": ["P015"]
    },
    {
        "method_id": "M008",
        "content": "Adaptive feature search based on early ground control results",
        "verbatim_quote": "As ground control proceeded, image patterns associated with these features became readily identifiable, and were eliminated during the subsequent image analysis. Conversely, features identified in the image that proved to be associated with ancient surface material were scrutinized, and a careful search was conducted for similar features thereafter.",
        "page": 429,
        "implements_design": "RD003",
        "child_protocols": ["P016", "P017"]
    },
    {
        "method_id": "M009",
        "content": "Blind image interpretation without knowledge of known site locations",
        "verbatim_quote": "Image interpretation was performed blind, without knowledge of the location of sites previously identified by the MTS.",
        "page": 426,
        "implements_design": "RD004",
        "child_protocols": []
    },
    {
        "method_id": "M010",
        "content": "Manual band recombination emphasizing red and NIR spectral bands for vegetation analysis",
        "verbatim_quote": "Our analysis began with band combinations prioritizing red and NIR, as they best reveal differences in vegetation growth sometimes associated with subsurface archaeological remains. Contrasts between high NIR values (healthy vegetation) and high red values (stressed vegetation) were sought primarily through manual band recombination",
        "page": 426,
        "implements_design": "RD001",
        "child_protocols": ["P018", "P019"]
    },
    {
        "method_id": "M011",
        "content": "NDVI transformation for quick bare/vegetated area distinction and discovery confirmation",
        "verbatim_quote": "The results of manual band recombination were then supplemented with transformations such as NDVI... Since there is such wide variation in NIR versus red reflectance produced by variable ground cover across our large study area, we used NDVI primarily to quickly distinguish between bare and vegetated areas and to confirm discoveries made through manual band recombination",
        "page": 427,
        "implements_design": "RD001",
        "child_protocols": ["P020"]
    },
    {
        "method_id": "M012",
        "content": "Georeferencing and projection to improve image geolocation accuracy",
        "verbatim_quote": "Before georeferencing using ground control points, the image had a root mean square error (RMSE) of 14 m... After georeferencing by Samsung Lim, its accuracy was improved to an RMSE of approximately 3 m",
        "page": 426,
        "implements_design": "RD001",
        "child_protocols": ["P021"]
    }
]

#================================================================
# PROTOCOLS - Extract specific procedures liberally
#================================================================

protocols = [
    {
        "protocol_id": "P001",
        "content": "QuickBird archival imagery acquisition (0.61m panchromatic, 2.44m multispectral, 18 March 2004, early spring timing)",
        "verbatim_quote": "Our image was archival rather than newly tasked, collected on 18 March 2004... At the time the project was initiated, QuickBird was the highest-resolution satellite imagery commercially available, with optimal panchromatic resolution of 0.61 m and multispectral resolution of 2.44 m. The early spring date of the image captured vigorous plant growth, increasing the contrast between healthy and stressed vegetation",
        "page": 425,
        "implements_method": "M001"
    },
    {
        "protocol_id": "P002",
        "content": "Image georeferencing using ground control points to improve RMSE from 14m to 3m",
        "verbatim_quote": "After georeferencing by Samsung Lim, its accuracy was improved to an RMSE of approximately 3 m, an excellent result facilitated by the low off-nadir angle of the image.",
        "page": 426,
        "implements_method": "M012"
    },
    {
        "protocol_id": "P003",
        "content": "Projection onto WGS 84, UTM 33N coordinate system",
        "verbatim_quote": "After georeferencing, the image was projected onto a local coordinate system (WGS 84, UTM 33N)",
        "page": 426,
        "implements_method": "M012"
    },
    {
        "protocol_id": "P004",
        "content": "Pan-sharpening: combining panchromatic and multispectral layers to enrich spatial resolution with spectral information",
        "verbatim_quote": "the two components of the image were combined so that the higher spatial resolution of the panchromatic layer was enriched by information from the multispectral layer.",
        "page": 426,
        "implements_method": "M001"
    },
    {
        "protocol_id": "P005",
        "content": "Manual band recombination procedure using limited range (4-2-1; 4-1-2; 4-1-4) emphasizing NIR/red contrast",
        "verbatim_quote": "the most effective way to quickly evaluate a large image with wide variations in vegetation cover, topography, and other parameters involved the use of a limited range of manual band combinations (4-2-1; 4-1-2; 4-1-4)",
        "page": 428,
        "implements_method": "M010"
    },
    {
        "protocol_id": "P006",
        "content": "Visual feature identification focusing on spatial patterns in reflectance intensity with misalignment from modern structures",
        "verbatim_quote": "Features were identified visually; in most cases they appeared as spatial patterns in the intensity of reflectance, usually in band combinations emphasizing the contrast between red and NIR... paying special attention to idiosyncratic features that did not align with the orientation of modern structures and field divisions.",
        "page": 428,
        "implements_method": "M001"
    },
    {
        "protocol_id": "P007",
        "content": "Pattern-based selection for ground control: scrutinizing rectilinear patterns (Greek/Roman) and circular patterns (prehistoric) without modern alignment",
        "verbatim_quote": "Both rectilinear and circular patterns were scrutinized under the working assumption that Greek and Roman sites would have a rectilinear form, while prehistoric sites might be circular. Particular attention was paid to features that did not align with the modern field system, roads, or structures such as field division walls.",
        "page": 428,
        "implements_method": "M001"
    },
    {
        "protocol_id": "P008",
        "content": "Ground control team procedure: 2-3 person teams walking feature perimeters plus multiple transects",
        "verbatim_quote": "A team consisting of two or three people visited each feature, walked its perimeter and then walked several paths across it.",
        "page": 428,
        "implements_method": "M002"
    },
    {
        "protocol_id": "P009",
        "content": "Systematic surface material density recording at all features",
        "verbatim_quote": "The density of ancient surface material (if present) was systematically recorded.",
        "page": 428,
        "implements_method": "M002"
    },
    {
        "protocol_id": "P010",
        "content": "Five-category feature classification: sites, off-site scatters, ambiguous, false positives, unassessed",
        "verbatim_quote": "Ultimately, they were placed into one of five categories: sites, off-site scatters, ambiguous (significant image anomaly but little or no surface material), false positives, and unassessed.",
        "page": 428,
        "implements_method": "M002"
    },
    {
        "protocol_id": "P011",
        "content": "Site definition criteria: 5 sherds/m² for historical sites, 2 sherds/m² for prehistoric sites (matching MTS)",
        "verbatim_quote": "We employed the same site definition criteria as the MTS (a threshold of five sherds per sq m for historical sites and two sherds per sq m for prehistoric sites)",
        "page": 429,
        "implements_method": "M002"
    },
    {
        "protocol_id": "P012",
        "content": "Surface visibility correction procedure (following MTS methodology)",
        "verbatim_quote": "and, like the MTS, we corrected for surface visibility... Correction for surface visibility was particularly important because, unlike a typical surface survey, we could not choose fields based primarily on agricultural condition and visibility.",
        "page": 429,
        "implements_method": "M002"
    },
    {
        "protocol_id": "P013",
        "content": "Expected discovery calculation: MTS rate (6.3 sites/km²) × ground control area (1.45 km²) = baseline expectation",
        "verbatim_quote": "The MTS, which explored a representative transect of our study area, yielded an average of 6.3 sites and off-site scatters per sq km (63 sites in total). At this rate, an area the size of that analyzed during remote sensing ground control (1.45 sq km) should have produced a total of about nine ancient sites and off-site scatters.",
        "page": 432,
        "implements_method": "M005"
    },
    {
        "protocol_id": "P014",
        "content": "False negative identification: comparing image feature locations with comprehensive MTS site inventory",
        "verbatim_quote": "\"False negatives,\" sites or off-site scatters previously discovered by the MTS but not detected during our image analysis (FIG. 6), also reveal the value and limitations of remote sensing. Our project encountered 51 such false negatives.",
        "page": 432,
        "implements_method": "M006"
    },
    {
        "protocol_id": "P015",
        "content": "Iterative pattern refinement: eliminating spectral patterns denoting modern/natural features while clarifying ancient material characteristics",
        "verbatim_quote": "Information from ground control was used to refine ongoing feature identification in the image, as spectral responses or patterns consistently denoting modern or natural features were eliminated from consideration and characteristics of features frequently associated with ancient surface material became clearer.",
        "page": 426,
        "implements_method": "M007"
    },
    {
        "protocol_id": "P016",
        "content": "False positive pattern elimination: identifying and excluding spectral responses associated with early-identified false positives",
        "verbatim_quote": "As ground control proceeded, image patterns associated with these features became readily identifiable, and were eliminated during the subsequent image analysis.",
        "page": 429,
        "implements_method": "M008"
    },
    {
        "protocol_id": "P017",
        "content": "Positive pattern targeting: scrutinizing features associated with ancient material and systematically searching for similar features",
        "verbatim_quote": "Conversely, features identified in the image that proved to be associated with ancient surface material were scrutinized, and a careful search was conducted for similar features thereafter.",
        "page": 429,
        "implements_method": "M008"
    },
    {
        "protocol_id": "P018",
        "content": "4-1-4 band combination procedure: displaying NIR as purple and red as green while excluding other color information",
        "verbatim_quote": "Contrasts between high NIR values (healthy vegetation) and high red values (stressed vegetation) were sought primarily through manual band recombination displaying, for example, NIR as purple and red as green while excluding all other color information (a 4-1-4 band combination).",
        "page": 426,
        "implements_method": "M010"
    },
    {
        "protocol_id": "P019",
        "content": "Limited band combination set application (4-2-1; 4-1-2; 4-1-4) for efficient large-area evaluation",
        "verbatim_quote": "the most effective way to quickly evaluate a large image with wide variations in vegetation cover, topography, and other parameters involved the use of a limited range of manual band combinations (4-2-1; 4-1-2; 4-1-4)",
        "page": 428,
        "implements_method": "M010"
    },
    {
        "protocol_id": "P020",
        "content": "NDVI application for quick bare/vegetated distinction and manual discovery confirmation",
        "verbatim_quote": "we used NDVI primarily to quickly distinguish between bare and vegetated areas and to confirm discoveries made through manual band recombination rather than as the principal means for detecting crop marks.",
        "page": 428,
        "implements_method": "M011"
    },
    {
        "protocol_id": "P021",
        "content": "Ground control point georeferencing procedure improving RMSE from 14m to 3m",
        "verbatim_quote": "Before georeferencing using ground control points, the image had a root mean square error (RMSE) of 14 m... After georeferencing by Samsung Lim, its accuracy was improved to an RMSE of approximately 3 m, an excellent result facilitated by the low off-nadir angle of the image.",
        "page": 426,
        "implements_method": "M012"
    }
]

#================================================================
# ADD TO EXTRACTION FILE
#================================================================

data['research_designs'] = research_designs
data['methods'] = methods
data['protocols'] = protocols

data['extraction_timestamp'] = datetime.now(timezone.utc).isoformat()

data['extraction_notes']['pass3_rdmap'] = {
    'completion_date': datetime.now(timezone.utc).isoformat(),
    'approach': 'Liberal extraction across all 6 section groups with equal attention. Especially liberal with research designs (4 extracted vs typical 2-3).',
    'section_coverage': 'ALL sections scanned for RDMAP content, not over-focused on Methods sections',
    'counts': {
        'research_designs': len(research_designs),
        'methods': len(methods),
        'protocols': len(protocols),
        'total_rdmap': len(research_designs) + len(methods) + len(protocols)
    },
    'notes': 'Comprehensive methods paper yielded high RDMAP density (37 items). Extracted 4 research designs (integrated approach, comparative evaluation, iterative feedback, blind design). Methods include image analysis techniques, ground control procedures, and comparative analysis. Protocols capture specific procedural details across entire workflow.'
}

with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print("PASS 3 COMPLETE - Liberal RDMAP Extraction")
print("=" * 70)
print(f"Research Designs: {len(research_designs)}")
print(f"Methods: {len(methods)}")
print(f"Protocols: {len(protocols)}")
print(f"Total RDMAP: {len(research_designs) + len(methods) + len(protocols)}")
print()
print(f"Total extraction now: {len(data['evidence']) + len(data['claims']) + len(data['implicit_arguments']) + len(research_designs) + len(methods) + len(protocols)} items")
print("=" * 70)
