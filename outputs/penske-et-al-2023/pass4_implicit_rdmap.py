#!/usr/bin/env python3
"""
Pass 4: Implicit RDMAP Extraction
Scan whole paper for mentioned-but-undocumented procedures and inferred methodology
Target: 15-25% of total RDMAP should be implicit (~8-13 items)
"""

import json

# Load current extraction
with open('/home/shawn/Code/llm-reproducibility/outputs/penske-et-al-2023/extraction.json', 'r') as f:
    data = json.load(f)

# IMPLICIT RDMAP ITEMS
# Mentioned but not documented, or inferred from Results/Discussion

implicit_rdmap = [
    # Implicit Research Design
    {
        "id": "RD008",
        "content": "Strategic focus on four Holocene cornerstone populations as ancestry reference framework",
        "design_type": "reference_framework_selection",
        "design_status": "implicit",
        "trigger_text": "four Holocene 'cornerstone' populations (Turkey_N, WHG, EHG/WSHG and CHG)",
        "page": 3,
        "inference_reasoning": "The choice of these specific four populations as cornerstone references is a strategic design decision, but no rationale is provided for why these four (vs other possible ancient references) or what criteria guided selection. This reference framework shapes all downstream ancestry interpretations.",
        "supported_by_methods": ["M015"]
    },

    # Implicit Methods
    {
        "id": "M017",
        "content": "Model selection procedure for qpAdm admixture modelling",
        "method_type": "model_selection",
        "method_status": "implicit",
        "trigger_text": "well-fit model; model fit; best proxies",
        "page": 2-3,
        "inference_reasoning": "Paper reports 'well-fit models' and 'best proxies' implying systematic model comparison, but the method for evaluating model fit and selecting between competing models is not documented. P-values reported suggest likelihood testing but procedure not specified.",
        "implemented_by_protocols": []
    },
    {
        "id": "M018",
        "content": "Data quality filtering criteria beyond endogenous DNA threshold",
        "method_type": "quality_control",
        "method_status": "implicit",
        "trigger_text": "initial quality criteria; assessment of human DNA content and DNA damage profiles",
        "page": 5,
        "inference_reasoning": "References 'initial quality criteria' and assessing 'damage profiles' implying quality filtering beyond 0.1% endogenous threshold, but specific criteria for damage patterns, contamination estimates, or other quality metrics not documented.",
        "implemented_by_protocols": []
    },
    {
        "id": "M019",
        "content": "Population grouping and naming conventions for genetic clusters",
        "method_type": "population_definition",
        "method_status": "implicit",
        "trigger_text": "SEE 1; local group SEE 1; Ukraine Eneolithic; Steppe Eneolithic",
        "page": 2-3,
        "inference_reasoning": "Paper creates and uses population labels (SEE 1, Ukraine Eneolithic, etc.) implying systematic grouping methodology, but criteria for when individuals are grouped vs analyzed separately not documented. How boundaries between 'populations' determined is implicit.",
        "implemented_by_protocols": []
    },
    {
        "id": "M020",
        "content": "Figure generation and data visualization methodology",
        "method_type": "visualization",
        "method_status": "implicit",
        "trigger_text": "Fig. 1b; Fig. 2; Fig. 3; Extended Data Fig.",
        "page": "throughout",
        "inference_reasoning": "Extensive figures presented (PCA plots, geographic maps, admixture bar plots) with no documentation of visualization software, parameter choices, or graphic design decisions. These visualization choices affect interpretation.",
        "implemented_by_protocols": []
    },

    # Implicit Protocols
    {
        "id": "P031",
        "content": "Reference panel selection and preparation for PCA projection",
        "protocol_type": "reference_preparation",
        "protocol_status": "implicit",
        "trigger_text": "present-day West Eurasian populations",
        "page": 2,
        "inference_reasoning": "PCA requires projecting ancient samples onto modern reference panel, but which specific present-day populations used, how many individuals, SNP overlap requirements, and projection algorithm not documented.",
        "implements_methods": ["M005"]
    },
    {
        "id": "P032",
        "content": "Source population selection for qpAdm models",
        "protocol_type": "source_selection",
        "protocol_status": "implicit",
        "trigger_text": "SEE N; VAR_CA; Ukraine Trypillia; Iron Gates HG; KO1",
        "page": 2-3,
        "inference_reasoning": "qpAdm requires selecting specific source populations for modeling, but criteria for source selection (geographic proximity, temporal overlap, genetic distinctiveness?) not documented. Different sources used for different targets without documented rationale.",
        "implements_methods": ["M008"]
    },
    {
        "id": "P033",
        "content": "Outgroup selection and preparation for f-statistics",
        "protocol_type": "outgroup_selection",
        "protocol_status": "implicit",
        "trigger_text": "Mbuti; outgroup",
        "page": 2-3,
        "inference_reasoning": "All f-statistics use Mbuti as outgroup, but rationale for Mbuti selection (vs other African populations), sample composition, and quality requirements not documented.",
        "implements_methods": ["M006", "M007"]
    },
    {
        "id": "P034",
        "content": "SNP filtering and imputation for genetic analyses",
        "protocol_type": "data_filtering",
        "protocol_status": "implicit",
        "trigger_text": "1,240,000 SNP capture",
        "page": 5,
        "inference_reasoning": "Capture targets 1.24M SNPs but actual coverage varies per sample. Missing data handling (e.g., missingness thresholds, imputation, pseudo-haploid calling) not documented despite being standard for ancient DNA.",
        "implements_methods": ["M004", "M005", "M006", "M007", "M008"]
    },
    {
        "id": "P035",
        "content": "Contamination estimation and filtering procedure",
        "protocol_type": "contamination_control",
        "protocol_status": "implicit",
        "trigger_text": "DNA damage profiles (initial quality criteria)",
        "page": 5,
        "inference_reasoning": "Damage profiles mentioned as quality criterion suggesting contamination estimation (modern DNA has low damage), but method for contamination estimation (X-chromosome, autosomal methods) and acceptable threshold not documented.",
        "implements_methods": ["M002", "M018"]
    },
    {
        "id": "P036",
        "content": "Sample duplication and read merging procedures",
        "protocol_type": "data_processing",
        "protocol_status": "implicit",
        "trigger_text": "enriched libraries; sequencing",
        "page": 5,
        "inference_reasoning": "Libraries screened then enriched and re-sequenced, implying data merging from multiple sequencing runs, but deduplication strategy and read merging procedures not documented.",
        "implements_methods": ["M002", "M004"]
    },
    {
        "id": "P037",
        "content": "Significance threshold application for statistical tests",
        "protocol_type": "significance_testing",
        "protocol_status": "implicit",
        "trigger_text": "|Z| ≥ 3; P = 0.05; significantly negative",
        "page": 2-3,
        "inference_reasoning": "Uses |Z| ≥ 3 for f-statistics and various P-value thresholds, but rationale for threshold choices and multiple testing correction (if any) not documented. Standard practice vs study-specific choice unclear.",
        "implements_methods": ["M007", "M013"]
    },
    {
        "id": "P038",
        "content": "Temporal binning and periodization for chronological grouping",
        "protocol_type": "temporal_grouping",
        "protocol_status": "implicit",
        "trigger_text": "Neolithic; Copper Age; Eneolithic; Early Bronze Age",
        "page": "throughout",
        "inference_reasoning": "Individuals assigned to periods (Neolithic, CA, Eneolithic, EBA) implying temporal grouping rules, but date boundaries and criteria for period assignment (radiocarbon date, archaeological context, both?) not documented.",
        "implements_methods": ["M001", "M003"]
    },
    {
        "id": "P039",
        "content": "Geographic coordinate mapping and spatial analysis parameters",
        "protocol_type": "spatial_analysis",
        "protocol_status": "implicit",
        "trigger_text": "mapped geographically (Fig. 2)",
        "page": 3,
        "inference_reasoning": "Geographic mapping of genetic affinities presented but coordinate system, interpolation method, and spatial parameters not documented.",
        "implements_methods": ["M014"]
    }
]

# Separate by type for adding to arrays
implicit_designs = [item for item in implicit_rdmap if item['id'].startswith('RD')]
implicit_methods = [item for item in implicit_rdmap if item['id'].startswith('M')]
implicit_protocols = [item for item in implicit_rdmap if item['id'].startswith('P')]

# Add to existing arrays
data['research_designs'].extend(implicit_designs)
data['methods'].extend(implicit_methods)
data['protocols'].extend(implicit_protocols)

# Calculate statistics
total_rdmap = len(data['research_designs']) + len(data['methods']) + len(data['protocols'])
implicit_count = len(implicit_rdmap)
implicit_percentage = (implicit_count / total_rdmap) * 100

# Update extraction notes
data['extraction_notes']['pass4_implicit_rdmap'] = {
    "completion_date": "2025-10-30",
    "approach": "Systematic whole-paper scan for mentioned-but-undocumented and inferred methodology",
    "scan_focus": [
        "Mentioned procedures without documentation (e.g., reference selection, model selection)",
        "Quality control procedures implied but not specified",
        "Data processing steps operationally necessary but undocumented",
        "Analytical decisions apparent from results without methodological documentation"
    ],
    "items_extracted": {
        "implicit_designs": len(implicit_designs),
        "implicit_methods": len(implicit_methods),
        "implicit_protocols": len(implicit_protocols),
        "total_implicit": implicit_count
    },
    "total_rdmap": {
        "explicit": total_rdmap - implicit_count,
        "implicit": implicit_count,
        "total": total_rdmap,
        "implicit_percentage": round(implicit_percentage, 1)
    },
    "target_met": f"Target 15-25% implicit: {round(implicit_percentage, 1)}% ({'✓' if 15 <= implicit_percentage <= 25 else '✗'})",
    "notes": "Technical genetics paper with detailed Methods section, but many standard procedures (contamination estimation, data filtering, model selection) mentioned but not documented. Implicit items critical for assessing reproducibility."
}

# Save
with open('/home/shawn/Code/llm-reproducibility/outputs/penske-et-al-2023/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Pass 4 Implicit RDMAP Extraction Complete!")
print(f"\nImplicit Items Extracted:")
print(f"  Implicit Designs: {len(implicit_designs)}")
print(f"  Implicit Methods: {len(implicit_methods)}")
print(f"  Implicit Protocols: {len(implicit_protocols)}")
print(f"  Total Implicit: {implicit_count}")
print(f"\nTotal RDMAP (Explicit + Implicit):")
print(f"  Research Designs: {len(data['research_designs'])}")
print(f"  Methods: {len(data['methods'])}")
print(f"  Protocols: {len(data['protocols'])}")
print(f"  Total: {total_rdmap}")
print(f"\nImplicit Percentage: {round(implicit_percentage, 1)}%")
print(f"Target met (15-25%): {'✓ YES' if 15 <= implicit_percentage <= 25 else '✗ NO'}")
print(f"\nReady for Pass 5: RDMAP rationalization")
PYTHON_SCRIPT
