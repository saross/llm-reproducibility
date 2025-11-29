#!/usr/bin/env python3
"""
Pass 3: Liberal RDMAP extraction from Methodology sections

Extract Research Designs, Methods, and Protocols describing:
- WHY: Strategic research approach decisions
- WHAT: Tactical data collection/analysis approaches
- HOW: Specific operational procedures
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Load current extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

print("Pass 3: RDMAP Extraction Starting...")

# ========================================
# RESEARCH DESIGNS (Strategic WHY decisions)
# ========================================

research_designs = [
    {
        "design_id": "RD001",
        "design_name": "Ordered logit vulnerability assessment model",
        "design_description": "Use ordered logistic regression model to assess vulnerability of burial mounds to anthropogenic threats by modeling relationships between current condition and circumstances, then simulating probable condition under changed circumstances",
        "design_type": "quantitative",
        "design_rationale": "Assess mound vulnerability to inform heritage resource allocation without relying on site location models, prior hazard knowledge, or development forecasts",
        "implemented_by_methods": ["M001", "M002", "M003", "M004"],
        "location": {
            "section": "2. Methodology",
            "page": 2,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "We applied an ordered logit model to determine the vulnerability of burial mounds to anthropogenic threats in the Kazanlak Valley.",
        "extraction_confidence": "high"
    },
    {
        "design_id": "RD002",
        "design_name": "Perceptive risk assessment approach",
        "design_type": "qualitative",
        "design_description": "Select risk factors based on field researchers' intuitions and observations about principal threats, then test hypotheses about these factors using quantitative model",
        "design_rationale": "Ground factor selection in field experience of ubiquitous mound degradation rather than purely theoretical considerations",
        "implemented_by_methods": ["M001"],
        "location": {
            "section": "2. Methodology",
            "page": 3,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Researchers in the ﬁeld (including the authors) believed that looting, agricultural activity, and peri-urban development were the principal factors contributing to the ubiquitous degradation of the mounds we saw during archaeological survey. Choosing these factors over others constituted a 'perceptive' initial risk assessment",
        "extraction_confidence": "high"
    }
]

print(f"Extracted {len(research_designs)} research designs")

# ========================================
# METHODS (Tactical WHAT approaches)
# ========================================

methods = [
    {
        "method_id": "M001",
        "method_name": "Hypothesis-driven factor selection",
        "method_description": "Propose three hypotheses about factors affecting mound vulnerability based on field observations: (1) annual agriculture damages mounds through ploughing, (2) proximity to urban areas contributes to damage from peri-urban activities, (3) looters target larger mounds",
        "method_type": "conceptual",
        "design_context": ["RD002", "RD001"],
        "implements_designs": ["RD002"],
        "used_in_protocols": ["P001"],
        "location": {
            "section": "2. Methodology",
            "page": 3,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Based on this intuition, we proposed three hypotheses: the ploughing, harrowing, and removal of obstacles from ﬁelds associated with annual agriculture damage mounds [...]; proximity to a city, town, or village would contribute to damage [...]; looters would preferentially target larger mounds",
        "extraction_confidence": "high"
    },
    {
        "method_id": "M002",
        "method_name": "Large-scale systematic pedestrian survey",
        "method_description": "Compile burial mound dataset through regional, total-coverage, pedestrian survey campaigns using trained personnel with standardised record sheets to collect GPS location, dimensions, land-use, and condition data",
        "method_type": "observational",
        "design_context": ["RD001"],
        "implements_designs": ["RD001"],
        "used_in_protocols": ["P002"],
        "location": {
            "section": "2.1. Dataset",
            "page": 3,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "TRAP compiled the burial mound dataset during three archaeological surface survey campaigns in the Kazanlak Valley during 2009–2011 (Ross et al. forthcoming). GPS location, dimensions, surrounding land-use, and condition of 773 burial mounds were collected by trained personnel using standardised record sheets over the course of regional, total-coverage, pedestrian survey",
        "extraction_confidence": "high"
    },
    {
        "method_id": "M003",
        "method_name": "GIS-based spatial variable derivation",
        "method_description": "Extract elevation data from digital elevation model and calculate distance metrics using GIS tools (Distance Matrix plugin in qGIS) applied to boundary polygons",
        "method_type": "computational",
        "design_context": ["RD001"],
        "implements_designs": ["RD001"],
        "used_in_protocols": ["P003", "P004"],
        "location": {
            "section": "2.1. Dataset",
            "page": 3,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Elevations were extracted from an ASTER digital elevation model. The distance to the nearest urban boundary was calculated using the Distance Matrix plugin in qGIS on the boundary polygons generated by the Japanese International Cooperation Agency (JICA) in 1994.",
        "extraction_confidence": "high"
    },
    {
        "method_id": "M004",
        "method_name": "Ordered logit model estimation and simulation",
        "method_description": "Estimate ordered logit model coef ficients using maximum likelihood algorithms to model relationships between mound condition and explanatory variables, then run simulations extrapolating to probable condition under changed circumstances",
        "method_type": "quantitative",
        "design_context": ["RD001"],
        "implements_designs": ["RD001"],
        "used_in_protocols": ["P005", "P006", "P007"],
        "location": {
            "section": "2.3. Statistical method",
            "page": 6,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "An ordered logit model was estimated using the variables discussed in Section 2.2; coefﬁcients are reported in Table 1. This model established the relationship between the current condition and circumstances of the mounds. Then we ran the simulations described in Section 2, extrapolating from the existing relationships between condition and circumstances to probable mound condition under new circumstances.",
        "extraction_confidence": "high"
    }
]

print(f"Extracted {len(methods)} methods")

# ========================================
# PROTOCOLS (Operational HOW procedures)
# ========================================

protocols = [
    {
        "protocol_id": "P001",
        "protocol_name": "Variable selection for model",
        "protocol_description": "Select explanatory variables based on three hypothesized factors (land use, proximity to urban boundary, mound size) plus elevation for coefficient estimation improvement, and define four specific change simulations to test",
        "protocol_type": "data_specification",
        "method_context": ["M001"],
        "implements_methods": ["M001"],
        "location": {
            "section": "2. Methodology",
            "page": 3,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "We use a large number of observations to model relationships between mound condition and elevation, mound size, surrounding land use (including annual agriculture, perennial agriculture, pasture, or forest), and distance to the nearest urban boundary. Four speciﬁc changes were then simulated: conversion of all forest to annual agriculture; conversion of all forest to pasture; conversion of all pasture to annual agriculture; an increase in distance of one standard deviation (673 m) from the nearest edge of a city, town, or village.",
        "extraction_confidence": "high"
    },
    {
        "protocol_id": "P002",
        "protocol_name": "Standardised mound recording procedure",
        "protocol_description": "Use standardised record sheets to systematically record GPS location, dimensions (height using scale/range-pole), surrounding land-use (categorical), and condition (Likert scale 1-5 based on visual assessment) for each mound during pedestrian survey",
        "protocol_type": "data_collection",
        "method_context": ["M002"],
        "implements_methods": ["M002"],
        "location": {
            "section": "2.1. Dataset + 2.2. Variables",
            "page": 3,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "GPS location, dimensions, surrounding land-use, and condition of 773 burial mounds were collected by trained personnel using standardised record sheets",
        "extraction_confidence": "high"
    },
    {
        "protocol_id": "P003",
        "protocol_name": "Elevation extraction from ASTER DEM",
        "protocol_description": "Extract elevation values for each mound location from ASTER digital elevation model",
        "protocol_type": "data_processing",
        "method_context": ["M003"],
        "implements_methods": ["M003"],
        "location": {
            "section": "2.1. Dataset",
            "page": 3,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Elevations were extracted from an ASTER digital elevation model.",
        "extraction_confidence": "high"
    },
    {
        "protocol_id": "P004",
        "protocol_name": "Distance calculation using qGIS Distance Matrix",
        "protocol_description": "Calculate distance to nearest urban boundary using Distance Matrix plugin in qGIS applied to JICA 1994 boundary polygons; calculate distance to Kazanlak center using centroid rather than boundary",
        "protocol_type": "data_processing",
        "method_context": ["M003"],
        "implements_methods": ["M003"],
        "location": {
            "section": "2.1. Dataset",
            "page": 3,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "The distance to the nearest urban boundary was calculated using the Distance Matrix plugin in qGIS on the boundary polygons generated by the Japanese International Cooperation Agency (JICA) in 1994. The distance to the local capital, Kazanlak, was calculated similarly, but using the centroid of its polygon rather than the boundary",
        "extraction_confidence": "high"
    },
    {
        "protocol_id": "P005",
        "protocol_name": "Ordered logit coefficient estimation",
        "protocol_description": "Estimate ordered logit model coefficients using maximum likelihood estimation algorithms applied to full dataset of 773 mounds with explanatory variables (elevation, distance, land-use types, height) and categorical response variable (condition 1-5)",
        "protocol_type": "statistical_analysis",
        "method_context": ["M004"],
        "implements_methods": ["M004"],
        "location": {
            "section": "2.3. Statistical method",
            "page": 6,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "An ordered logit model was estimated using the variables discussed in Section 2.2",
        "extraction_confidence": "high",
        "expected_information_missing": ["Specific software used", "Convergence criteria", "Model diagnostics performed"]
    },
    {
        "protocol_id": "P006",
        "protocol_name": "Simulation procedure for changed circumstances",
        "protocol_description": "Run simulations by extrapolating from estimated relationships between condition and circumstances to calculate probable mound conditions under hypothetical changes (land-use conversions, urban boundary retreat)",
        "protocol_type": "statistical_analysis",
        "method_context": ["M004"],
        "implements_methods": ["M004"],
        "location": {
            "section": "2.3. Statistical method",
            "page": 6,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "Then we ran the simulations described in Section 2, extrapolating from the existing relationships between condition and circumstances to probable mound condition under new circumstances. For example, the (negative) relationship between mound condition and distance to the nearest urban boundary was ﬁrst quantiﬁed, and then new mound conditions were estimated as if the nearest boundary had retreated by 673 m (one standard deviation).",
        "extraction_confidence": "high"
    },
    {
        "protocol_id": "P007",
        "protocol_name": "Graphical representation of simulation results",
        "protocol_description": "Represent simulation results using probability density function charts showing shifts in distribution for each condition category, rather than reporting coefficients and odds ratios",
        "protocol_type": "data_visualization",
        "method_context": ["M004"],
        "implements_methods": ["M004"],
        "location": {
            "section": "2.3. Statistical method",
            "page": 6,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "Since the typical outputs of logit models (coefﬁcients and odds ratios) are difﬁcult to explain and interpret, we chose to represent the changes graphically; for each simulation, visible shifts in the probability density functions indicate how changing circumstances affect mound vulnerability.",
        "extraction_confidence": "high"
    }
]

print(f"Extracted {len(protocols)} protocols")

# Add to extraction
data["research_designs"] = research_designs
data["methods"] = methods
data["protocols"] = protocols

# Update extraction notes
data["extraction_notes"]["rdmap_extraction_complete"] = False  # Will be true after Pass 5
data["extraction_notes"]["rdmap_sections_extracted"] = [
    "Pass 3: Methodology (sections 2, 2.1, 2.2, 2.3)"
]

# Update timestamp
data["extraction_timestamp"] = datetime.now(timezone.utc).isoformat()

# Save updated extraction
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print("\n✓ Pass 3 RDMAP extraction complete")
print(f"  - {len(research_designs)} research designs")
print(f"  - {len(methods)} methods")
print(f"  - {len(protocols)} protocols")
print(f"  - Total RDMAP: {len(research_designs) + len(methods) + len(protocols)} items")
print("✓ Saved to extraction.json")
