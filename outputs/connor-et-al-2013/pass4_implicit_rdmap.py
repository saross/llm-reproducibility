#!/usr/bin/env python3
"""
Pass 4: Implicit RDMAP Extraction
Connor et al. 2013

Scan whole paper for mentioned-but-undocumented procedures and inferred methodology.
Target: 15-25% of total RDMAP should be implicit (~11-20 items from current 61 explicit).

Focus on:
- Procedures mentioned but not documented (e.g., parameter selection, threshold choices)
- Quality control procedures implied but not specified
- Data processing steps operationally necessary but undocumented
- Analytical decisions apparent from results without methodological documentation
"""

import json

# Load current extraction
with open('/home/shawn/Code/llm-reproducibility/outputs/connor-et-al-2013/extraction.json', 'r') as f:
    data = json.load(f)

# IMPLICIT RDMAP ITEMS
# Mentioned but not documented, or inferred from Methods/Results

implicit_rdmap = [
    # Implicit Research Designs
    {
        "id": "RD008",
        "content": "Multi-proxy integration strategy for combining pollen, charcoal, magnetic susceptibility, and NPP data to reconstruct palaeoenvironmental history",
        "design_type": "analytical_integration_strategy",
        "design_status": "implicit",
        "trigger_text": "pollen, non-pollen palynomorph, magnetic susceptibility and charcoal record",
        "page": 4,
        "inference_reasoning": "Paper presents integrated interpretation of four proxy types, but provides no documented framework for how these proxies are synthesised, weighted, or reconciled when they provide contradictory signals. The integration strategy is operationally necessary but undocumented.",
        "supported_by_methods": ["M001", "M002", "M003", "M004"]
    },
    {
        "id": "RD009",
        "content": "Reference site selection strategy for regional comparative analysis using European Pollen Database",
        "design_type": "comparative_framework_design",
        "design_status": "implicit",
        "trigger_text": "selected a number of representative records from the Bulgarian mountains and the Black Sea area",
        "page": 8,
        "inference_reasoning": "Sites selected for comparison (Fig. 1, Fig. 5) but criteria for 'representative' not documented. Geographic proximity? Temporal coverage? Methodological comparability? Site selection fundamentally shapes regional synthesis but rationale unstated.",
        "supported_by_methods": ["M013"]
    },

    # Implicit Methods
    {
        "id": "M021",
        "content": "Pollen preservation assessment method",
        "method_type": "quality_control",
        "method_status": "implicit",
        "trigger_text": "pollen preservation in the sediments was variable",
        "page": 11,
        "inference_reasoning": "Variable preservation documented and attributed to alkalinity, climate, and drainage, but method for assessing preservation quality not specified. Preservation assessment likely affected counting procedures and interpretation but methodology not documented.",
        "implemented_by_protocols": []
    },
    {
        "id": "M022",
        "content": "Age-depth model quality evaluation criteria and decision rules for excluding dates",
        "method_type": "chronological_validation",
        "method_status": "implicit",
        "trigger_text": "performance statistics indicated poor agreement; Exclusion of Wk-32001 increased the model's agreement index to a more acceptable level",
        "page": 13,
        "inference_reasoning": "Agreement index thresholds (12% = poor, 58% = acceptable) used to evaluate and modify age-depth model, but criteria for acceptable agreement not documented. Decision rules for iterative date exclusion process not specified.",
        "implemented_by_protocols": []
    },
    {
        "id": "M023",
        "content": "Regional pollen source area estimation method",
        "method_type": "spatial_representation",
        "method_status": "implicit",
        "trigger_text": "representative of a large spatial area, estimated at ~10^4-10^5 km^2",
        "page": 13,
        "inference_reasoning": "Source area estimate cited from Sugita (2007) but application method not documented. How basin size (14,000 ha) translated to source area estimate? Site-specific calculations or general assumption? Critical for interpreting spatial scale of vegetation changes.",
        "implemented_by_protocols": []
    },
    {
        "id": "M024",
        "content": "Palaeovegetation phase boundary determination from cluster analysis",
        "method_type": "zonation",
        "method_status": "implicit",
        "trigger_text": "Cluster analysis was used to group the pollen record into five palaeovegetation phases",
        "page": 11,
        "inference_reasoning": "Cluster analysis produced five phases but criteria for selecting five (vs 4 or 6) not documented. Phase boundary placement involves subjective decisions about optimal cluster number that are assessment-critical but undocumented.",
        "implemented_by_protocols": ["P042"]
    },
    {
        "id": "M025",
        "content": "Visualization and graphic design methodology for pollen diagrams",
        "method_type": "visualization",
        "method_status": "implicit",
        "trigger_text": "Results were plotted using Psimpoll",
        "page": 8,
        "inference_reasoning": "Psimpoll software mentioned but diagram design choices not documented: exaggeration factors (5x for magnetic susceptibility visible in Fig 4), color schemes, grouping decisions, axis scaling. These choices affect interpretation but are undocumented.",
        "implemented_by_protocols": []
    },

    # Implicit Protocols
    {
        "id": "P035",
        "content": "Pollen counting threshold determination and stopping rules",
        "protocol_type": "counting_protocol",
        "protocol_status": "implicit",
        "trigger_text": "At least 200 (average 600) terrestrial pollen were counted",
        "page": 7,
        "inference_reasoning": "Minimum threshold (200) and average count (600) stated but decision rules not documented. When to stop at 200 vs continue to 600? How determined if assemblage sufficiently diverse? Stopping rules critical for reproducibility but undocumented.",
        "implements_methods": ["M002"],
        "parameters": {
            "minimum_count": "200 terrestrial pollen",
            "average_count": "600 terrestrial pollen"
        }
    },
    {
        "id": "P036",
        "content": "Lycopodium marker spike tablet concentration and addition volume",
        "protocol_type": "concentration_calculation",
        "protocol_status": "implicit",
        "trigger_text": "combined with Lycopodium spore tablets (University of Lund)",
        "page": 7,
        "inference_reasoning": "Lycopodium tablets used for concentration calculations but tablet specifications not documented: spore concentration per tablet, batch number, addition protocol. Standard procedure but specifics needed for replication.",
        "implements_methods": ["M002"],
        "parameters": {
            "marker_type": "Lycopodium spore tablets",
            "supplier": "University of Lund"
        }
    },
    {
        "id": "P037",
        "content": "Charcoal particle size boundary discrimination procedures",
        "protocol_type": "particle_classification",
        "protocol_status": "implicit",
        "trigger_text": "Microscopic charcoal (<200 µm); macroscopic charcoal (>250 µm)",
        "page": 7,
        "inference_reasoning": "Size classes defined but discrimination procedures not documented. For microscopic: how measured on slides at 400x magnification? For macroscopic: sieve mesh size exact or approximate? Gap between 200-250 µm not addressed. Critical for local vs regional fire signal separation.",
        "implements_methods": ["M003"],
        "parameters": {
            "microscopic_threshold": "<200 µm",
            "macroscopic_threshold": ">250 µm",
            "undocumented_gap": "200-250 µm fraction"
        }
    },
    {
        "id": "P038",
        "content": "Image analysis parameter selection and calibration for charcoal quantification",
        "protocol_type": "image_analysis",
        "protocol_status": "implicit",
        "trigger_text": "Charcoal concentrations were quantified using image analysis software (Scion Image 4.0.3.2)",
        "page": 8,
        "inference_reasoning": "Scion Image software specified but analysis parameters not documented: threshold settings for charcoal vs non-charcoal, particle detection parameters, calibration procedures. These parameters fundamentally determine charcoal concentration results.",
        "implements_methods": ["M003"],
        "parameters": {
            "software": "Scion Image 4.0.3.2",
            "measurement_type": "area (mm² per cm³)"
        }
    },
    {
        "id": "P039",
        "content": "Magnetic susceptibility measurement frequency and sample preparation protocol",
        "protocol_type": "measurement_protocol",
        "protocol_status": "implicit",
        "trigger_text": "Dual-frequency magnetic susceptibility measurements were run on a Bartington MS2",
        "page": 8,
        "inference_reasoning": "Dual-frequency measurement mentioned (implies low and high frequency) but specific frequencies not stated. Sample preparation (mass, drying, homogenization) not documented. Measurement frequencies critical for frequency-dependent susceptibility calculations.",
        "implements_methods": ["M004"],
        "parameters": {
            "instrument": "Bartington MS2 meter",
            "measurement_type": "dual-frequency"
        }
    },
    {
        "id": "P040",
        "content": "VFTB measurement parameters and field strength protocols for mineral magnetic analysis",
        "protocol_type": "measurement_protocol",
        "protocol_status": "implicit",
        "trigger_text": "Magnetic Measurements Variable Field Translation Balance (VFTB), including IRM acquisition curves and backfields, hysteresis loops and thermomagnetic curves",
        "page": 8,
        "inference_reasoning": "VFTB analyses listed but measurement parameters not documented: field strengths for IRM acquisition, backfield steps, hysteresis loop field range, heating/cooling rates for thermomagnetic curves. These parameters determine data quality and comparability.",
        "implements_methods": ["M004"]
    },
    {
        "id": "P041",
        "content": "Monte Carlo permutation test iteration number selection for indicator species analysis",
        "protocol_type": "statistical_testing",
        "protocol_status": "implicit",
        "trigger_text": "p=0.001; Monte Carlo test, 1000 permutations",
        "page": 9,
        "inference_reasoning": "1000 permutations specified but rationale not documented. Sufficient for stability? Computational constraint? Standard practice? Iteration number affects p-value precision and test power.",
        "implements_methods": ["M013"],
        "parameters": {
            "significance_level": "p=0.001",
            "permutation_iterations": "1000"
        }
    },
    {
        "id": "P042",
        "content": "DCA detrending segment length and cluster analysis linkage method parameters",
        "protocol_type": "multivariate_analysis",
        "protocol_status": "implicit",
        "trigger_text": "Detrended Correspondence Analysis (DCA: Hill and Gauch, 1980) and minimum variance cluster analysis (Ward, 1963)",
        "page": 8,
        "inference_reasoning": "DCA and cluster analysis methods cited but analytical parameters not documented. DCA: detrending by segments or polynomials? Segment length? Cluster analysis: Ward's method specified but distance metric not stated (Euclidean? Chord?). Parameters affect ordination and clustering results.",
        "implements_methods": ["M013"]
    },
    {
        "id": "P043",
        "content": "Pollen taxonomic standardization decisions and morphotype grouping rules",
        "protocol_type": "taxonomic_harmonization",
        "protocol_status": "implicit",
        "trigger_text": "Pollen taxonomy was standardised to a base of 99 taxa, resulting in some loss of information",
        "page": 9,
        "inference_reasoning": "Standardization to 99 taxa for multi-site comparison but grouping decisions not documented. Which Quercus morphotypes merged? How other genera lumped? 'Loss of information' acknowledged but specific decisions not stated. Critical for comparative analysis validity.",
        "implements_methods": ["M013"],
        "parameters": {
            "standardized_taxa_count": "99 taxa"
        }
    },
    {
        "id": "P044",
        "content": "Indicator species analysis significance threshold selection rationale",
        "protocol_type": "significance_testing",
        "protocol_status": "implicit",
        "trigger_text": "at least one statistically significant indicator (p=0.001)",
        "page": 9,
        "inference_reasoning": "p=0.001 threshold used for indicator species but rationale not documented. More stringent than conventional p=0.05. Bonferroni correction for multiple testing? Study-specific choice? Threshold determines optimum cluster number and phase definition.",
        "implements_methods": ["M013"],
        "parameters": {
            "significance_threshold": "p=0.001"
        }
    },
    {
        "id": "P045",
        "content": "Radiocarbon sample material selection strategy and pre-treatment evaluation",
        "protocol_type": "sample_selection",
        "protocol_status": "implicit",
        "trigger_text": "In the absence of macrobotanical material for dating, five of the radiocarbon determinations were made on pollen concentrates; The remaining samples were cleaned to remove rootlets and pre-treated by acid washing",
        "page": 9,
        "inference_reasoning": "Sample material selection strategy implied (preference hierarchy: macrobotanicals > pollen concentrates > bulk organics) but evaluation criteria not documented. How assessed if rootlets were modern contamination? Why pollen concentrates preferred over bulk organics for 5 samples? Material selection decisions affect chronology reliability.",
        "implements_methods": ["M015"],
        "parameters": {
            "pollen_concentrate_count": "5 dates",
            "organic_residue_count": "8 dates"
        }
    },
    {
        "id": "P046",
        "content": "Sample interval selection rationale for variable resolution sampling",
        "protocol_type": "sampling_strategy",
        "protocol_status": "implicit",
        "trigger_text": "Samples ~20cm³ in size were taken at 5-cm intervals until a depth of 140 cm from the surface and thereafter at 20-cm intervals",
        "page": 7,
        "inference_reasoning": "Variable sampling intervals (5 cm vs 20 cm) with transition at 140 cm but rationale not documented. Lithological change? Temporal resolution target? Practical constraint? Interval selection determines temporal resolution and affects ability to detect rapid environmental changes.",
        "implements_methods": ["M001"],
        "parameters": {
            "upper_interval": "5 cm (0-140 cm depth)",
            "lower_interval": "20 cm (140-520 cm depth)"
        }
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
explicit_count = total_rdmap - implicit_count
implicit_percentage = (implicit_count / total_rdmap) * 100

# Update extraction notes
data['extraction_notes']['pass4_implicit_rdmap'] = {
    "completion_date": "2025-10-30",
    "approach": "Systematic whole-paper scan for mentioned-but-undocumented procedures and inferred methodology",
    "scan_focus": [
        "Parameter selection decisions mentioned without documentation",
        "Quality control procedures implied but not specified",
        "Data processing standards operationally necessary but undocumented",
        "Analytical decisions apparent from results without methodological explanation",
        "Threshold and stopping rule justifications"
    ],
    "items_extracted": {
        "implicit_designs": len(implicit_designs),
        "implicit_methods": len(implicit_methods),
        "implicit_protocols": len(implicit_protocols),
        "total_implicit": implicit_count
    },
    "total_rdmap": {
        "explicit": explicit_count,
        "implicit": implicit_count,
        "total": total_rdmap,
        "implicit_percentage": round(implicit_percentage, 1)
    },
    "target_met": f"Target 15-25% implicit: {round(implicit_percentage, 1)}% ({'✓' if 15 <= implicit_percentage <= 25 else '✗'})",
    "notes": "Palaeoecological reconstruction paper with detailed Methods section, but many standard procedures (parameter selection, threshold justification, quality assessment) mentioned but not documented. Implicit items critical for assessing reproducibility, particularly for multivariate analyses and multi-proxy integration."
}

# Save
with open('/home/shawn/Code/llm-reproducibility/outputs/connor-et-al-2013/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print("=" * 80)
print("PASS 4: IMPLICIT RDMAP EXTRACTION COMPLETE!")
print("=" * 80)
print(f"\nImplicit Items Extracted:")
print(f"  Implicit Designs: {len(implicit_designs)}")
print(f"  Implicit Methods: {len(implicit_methods)}")
print(f"  Implicit Protocols: {len(implicit_protocols)}")
print(f"  Total Implicit: {implicit_count}")
print(f"\nTotal RDMAP (Explicit + Implicit):")
print(f"  Research Designs: {len(data['research_designs'])} (Explicit: {len(data['research_designs'])-len(implicit_designs)}, Implicit: {len(implicit_designs)})")
print(f"  Methods: {len(data['methods'])} (Explicit: {len(data['methods'])-len(implicit_methods)}, Implicit: {len(implicit_methods)})")
print(f"  Protocols: {len(data['protocols'])} (Explicit: {len(data['protocols'])-len(implicit_protocols)}, Implicit: {len(implicit_protocols)})")
print(f"  Total: {total_rdmap}")
print(f"\nImplicit Percentage: {round(implicit_percentage, 1)}%")
print(f"Target met (15-25%): {'✓ YES' if 15 <= implicit_percentage <= 25 else '✗ NO - ' + ('TOO LOW' if implicit_percentage < 15 else 'TOO HIGH')}")
print(f"\nReady for Pass 5: RDMAP rationalization")
