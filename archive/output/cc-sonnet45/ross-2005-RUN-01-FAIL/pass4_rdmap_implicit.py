#!/usr/bin/env python3
"""
Pass 4: Implicit RDMAP Extraction

Identifies unstated methodological assumptions, implicit theoretical frameworks,
and background research design choices not explicitly articulated in Pass 3.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

extraction_file = Path("extraction.json")

print("=" * 80)
print("PASS 4: IMPLICIT RDMAP EXTRACTION")
print("=" * 80)
print()

# Read current extraction data
with open(extraction_file) as f:
    data = json.load(f)

# ============================================================================
# IMPLICIT RESEARCH DESIGNS
# ============================================================================

implicit_research_designs = []

# No major implicit research designs to add - the designs are fairly explicit

# ============================================================================
# IMPLICIT METHODS
# ============================================================================

implicit_methods = [
    {
        "id": "M008",
        "content": "Interpretive priority method: privileging authorial intent and audience reception over modern theoretical frameworks",
        "method_type": "interpretive_stance",
        "page": 301,
        "inference_reasoning": "Ross consistently interprets passages in terms of what poet and eighth-century audience would have understood, rather than applying modern theoretical lenses. This methodological choice is enacted throughout but never explicitly defended.",
        "related_claims": ["C015", "C016"],
        "implementation_details": "Implicit throughout analysis - focuses on contemporary meaning rather than later receptions or modern theoretical readings"
    },
    {
        "id": "M009",
        "content": "Selective evidence method: focusing on explicit linguistic diversity mentions rather than systematic analysis of all speech acts",
        "method_type": "evidence_selection",
        "page": 303,
        "inference_reasoning": "Ross examines only passages that explicitly mention linguistic diversity, not all instances of communication or speech. This selective approach is methodologically significant but not explicitly justified.",
        "related_claims": ["C007"],
        "implementation_details": "Limits analysis to three Iliad passages plus comparative epic examples where language is explicitly thematized"
    }
]

# ============================================================================
# IMPLICIT PROTOCOLS
# ============================================================================

implicit_protocols = [
    {
        "id": "P011",
        "content": "Assumption of textual stability: treating received texts as reliably representing c. 700 BCE versions",
        "protocol_type": "textual_assumption",
        "page": 300,
        "inference_reasoning": "Ross uses texts as evidence for eighth-century attitudes without discussing manuscript tradition, textual variants, or transmission issues. This assumes textual stability from composition to our received texts.",
        "related_methods": ["M001"],
        "rationale": "Necessary simplifying assumption for historical-linguistic analysis"
    },
    {
        "id": "P012",
        "content": "Monocausal interpretation avoidance: attributing patterns to multiple possible motivations rather than single causes",
        "protocol_type": "interpretive_caution",
        "page": 314,
        "inference_reasoning": "Ross explicitly identifies 'two motivations' for linguistic variation, signaling awareness that single-cause explanations are insufficient. This methodological caution is demonstrated but not explicitly theorized.",
        "related_methods": ["M003"],
        "rationale": "Reflects awareness of complexity in literary evidence"
    }
]

# Add items to extraction data
print(f"Adding {len(implicit_research_designs)} implicit research designs...")
data['research_designs'].extend(implicit_research_designs)

print(f"Adding {len(implicit_methods)} implicit methods...")
data['methods'].extend(implicit_methods)

print(f"Adding {len(implicit_protocols)} implicit protocols...")
data['protocols'].extend(implicit_protocols)

# Update timestamp
data['extraction_timestamp'] = datetime.now(timezone.utc).isoformat()

# Write updated data
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print()
print("=" * 80)
print("PASS 4 COMPLETE")
print("=" * 80)
print()
print(f"Implicit RDMAP added:")
print(f"  Implicit Research Designs: {len(implicit_research_designs)}")
print(f"  Implicit Methods: {len(implicit_methods)}")
print(f"  Implicit Protocols: {len(implicit_protocols)}")
print()
print(f"Total RDMAP:")
print(f"  Research Designs: {len(data['research_designs'])}")
print(f"  Methods: {len(data['methods'])}")
print(f"  Protocols: {len(data['protocols'])}")
print(f"  Total: {len(data['research_designs']) + len(data['methods']) + len(data['protocols'])}")
print("=" * 80)
