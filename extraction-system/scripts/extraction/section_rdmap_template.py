#!/usr/bin/env python3
"""
Section-by-Section RDMAP Extraction Template

Demonstrates extracting BOTH explicit and implicit RDMAP from a single section.
Adapt for each section: Abstract+Intro, Methods, Results, Discussion.

Key principle:
Each section extraction must capture BOTH:
1. EXPLICIT RDMAP - documented/clearly stated procedures
2. IMPLICIT RDMAP - mentioned procedures without procedural detail

Common failure mode: Only extracting explicit items, missing implicit ones.
This causes zero implicit RDMAP in final extraction.

Recognition patterns for implicit RDMAP:
- VERBS without procedures: cleaned, validated, checked, assigned, corrected
- EFFECTS implying causes: "performance degraded" → monitoring protocol
- MENTIONS without descriptions: "assigned maps" → assignment protocol
"""

import json

# Load existing extraction
with open('extraction.json', 'r') as f:
    data = json.load(f)

# ============================================
# EXPLICIT RDMAP (documented or clearly stated)
# ============================================

# Example: Explicit method documented in Methods section
explicit_methods = [
    {
        "method_id": "M001",
        "method_text": "Data collection using mobile GIS application",
        "method_tier": "data_collection",
        "method_status": "explicit",
        "verbatim_quote": "We collected data using a customised mobile GIS application deployed on Android smartphones.",
        "location": {
            "section": "Methods",
            "subsection": "2.3 Data Collection",
            "page": 5
        },
        "enabled_by_designs": ["RD001"],
        "realized_through_protocols": ["P001"]
    }
]

# Example: Explicit protocol with specific configuration details
explicit_protocols = [
    {
        "protocol_id": "P001",
        "protocol_text": "GPS coordinate recording using Trimble GeoXH 6000 with WAAS correction",
        "protocol_tier": "data_acquisition",
        "protocol_status": "explicit",
        "verbatim_quote": "GPS coordinates were recorded using Trimble GeoXH 6000 receivers with WAAS differential correction.",
        "location": {
            "section": "Methods",
            "subsection": "2.3 Data Collection",
            "page": 5
        },
        "implements_method": "M001"
    }
]

# ============================================
# IMPLICIT RDMAP (mentioned but not described)
# ============================================

# Example: Implicit protocol inferred from Results section
# Pattern: "Mentioned Procedure" - paper states action occurred but no details
implicit_protocols = [
    {
        "protocol_id": "P002",
        "protocol_text": "Map tile assignment protocol for volunteer allocation",
        "protocol_tier": "task_allocation",
        "protocol_status": "implicit",
        # CRITICAL: trigger_text must be verbatim passages from paper
        "trigger_text": [
            "Students were assigned specific map tiles to prevent overlap.",
            "Student C failing to digitise assigned sections led to data gaps."
        ],
        # CRITICAL: trigger_locations must specify where each trigger found
        "trigger_locations": [
            {"section": "Results", "subsection": "3.2", "page": 7, "paragraph": 1},
            {"section": "Results", "subsection": "3.3", "page": 8, "paragraph": 2}
        ],
        # CRITICAL: inference_reasoning must explain how triggers imply the RDMAP item
        "inference_reasoning": "Multiple references to 'assigned' map tiles indicate an assignment protocol existed. The paper mentions students received specific tile allocations to prevent overlap, and discusses consequences of failing to complete 'assigned' sections. However, the allocation method (random, spatial, volunteer preference, etc.) is never described. This represents undocumented but operationally critical task allocation.",
        # CRITICAL: implicit_metadata required for implicit RDMAP
        "implicit_metadata": {
            "basis": "mentioned_undocumented",
            "confidence": "high",
            "assessment_implication": "Cannot assess whether assignment strategy (e.g., spatial proximity, skill-based) affected error patterns or data completeness. Allocation method may have influenced which areas received more experienced volunteers."
        },
        "location": {
            "section": "Results",
            "subsection": "3.2",
            "page": 7
        },
        "implements_method": "M001"
    }
]

# Example: Implicit protocol inferred from threshold detection in Results
# Pattern: "Inferred from Results" - operational detail revealed but method undocumented
implicit_protocols_2 = [
    {
        "protocol_id": "P003",
        "protocol_text": "Device performance monitoring protocol for load threshold detection",
        "protocol_tier": "quality_assurance",
        "protocol_status": "implicit",
        "trigger_text": [
            "Performance degraded noticeably after approximately 2,500 records per device.",
            "We observed slowdowns when devices exceeded 2,500 cached features."
        ],
        "trigger_locations": [
            {"section": "Results", "subsection": "3.4", "page": 9, "paragraph": 2},
            {"section": "Discussion", "subsection": "4.2", "page": 11, "paragraph": 1}
        ],
        "inference_reasoning": "The precise threshold of ~2,500 records implies systematic monitoring of device performance relative to record counts. Detecting this specific threshold requires tracking both performance metrics (response time, lag) and record counts during fieldwork. However, the paper never describes how performance was monitored, what metrics were tracked, or how the threshold was determined. This represents an implicit quality assurance protocol.",
        "implicit_metadata": {
            "basis": "procedural_inference",
            "confidence": "high",
            "assessment_implication": "Cannot assess monitoring methodology (continuous vs periodic), metrics used (subjective vs objective), or threshold detection precision. The 2,500 record threshold credibility depends on undocumented monitoring rigour."
        },
        "location": {
            "section": "Results",
            "subsection": "3.4",
            "page": 9
        },
        "implements_method": "M001"
    }
]

# Example: Implicit method from Results section
# Pattern: "VERBS without procedures" - action mentioned but procedure not described
implicit_methods = [
    {
        "method_id": "M002",
        "method_text": "Data cleaning method for coordinate validation",
        "method_tier": "data_processing",
        "method_status": "implicit",
        "trigger_text": [
            "We cleaned the coordinate data to remove outliers.",
            "After cleaning, 8,343 features remained for analysis."
        ],
        "trigger_locations": [
            {"section": "Results", "subsection": "3.1", "page": 6, "paragraph": 3},
            {"section": "Results", "subsection": "3.1", "page": 6, "paragraph": 4}
        ],
        "inference_reasoning": "Paper states data cleaning occurred ('we cleaned') and provides before/after counts, but never describes the cleaning procedure. What constituted an 'outlier'? What thresholds were used? What validation checks were applied? The cleaning method is operationally significant (affects final dataset) but procedurally undocumented.",
        "implicit_metadata": {
            "basis": "mentioned_undocumented",
            "confidence": "high",
            "assessment_implication": "Cannot assess cleaning rigour, appropriateness of outlier criteria, or risk of inappropriate data exclusion. Cleaning methodology affects dataset credibility but is not reproducible from paper."
        },
        "location": {
            "section": "Results",
            "subsection": "3.1",
            "page": 6
        },
        "enabled_by_designs": [],
        "realized_through_protocols": []
    }
]

# ============================================
# Add items to extraction
# ============================================

# Extend arrays (do not replace - accumulate across sections)
data['methods'].extend(explicit_methods)
data['methods'].extend(implicit_methods)
data['protocols'].extend(explicit_protocols)
data['protocols'].extend(implicit_protocols)
data['protocols'].extend(implicit_protocols_2)

# Write updated extraction
with open('extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Section extraction complete:")
print(f"   - {len(explicit_methods)} explicit methods")
print(f"   - {len(implicit_methods)} implicit methods")
print(f"   - {len(explicit_protocols)} explicit protocols")
print(f"   - {len(implicit_protocols) + len(implicit_protocols_2)} implicit protocols")
print(f"\n💡 Remember: BOTH explicit AND implicit extraction required for each section")
