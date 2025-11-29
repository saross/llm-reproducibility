#!/usr/bin/env python3
"""
Pass 3 RDMAP Extraction (finalize): Results/Discussion sections
Final scan for explicit RDMAP before moving to Pass 4 (implicit)
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Load existing extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

# ============================================================================
# Pass 3 RDMAP Extraction: Results/Discussion Final Scan
# Sections: Pages 18-20, checking for additional explicit RDMAP
# ============================================================================

# ADDITIONAL PROTOCOL from Results
# =================================

# P015: Performance testing protocol
p015 = {
    "protocol_id": "P015",
    "protocol_text": "Automated load testing protocol to predict field performance and identify degradation thresholds for mobile application",
    "protocol_type": "system_testing",
    "protocol_status": "explicit",
    "location": {
        "section": "Results - Performance",
        "page": 18,
        "start_paragraph": 2,
        "end_paragraph": 2
    },
    "verbatim_quote": "Automated testing of the Gridded Survey module suggested that performance would degrade between 50 and 200 units or ca. 30,000–120,000 values (see Supplemental Material 4). The assumptions built into the tests were too pessimistic, however, and we were able to collect around 230 survey unit records (> 135,000 values) before one device became unstable.",
    "protocol_steps": [
        "Run automated load tests on module",
        "Predict performance degradation thresholds",
        "Compare predictions with actual field performance",
        "Document discrepancies"
    ],
    "parameters": {
        "predicted_degradation": "50-200 units (30,000-120,000 values)",
        "actual_performance": "230 units (>135,000 values)"
    },
    "implements_methods": ["M004"],
    "expected_information_missing": [
        "Testing methodology details",
        "Assumptions in test design",
        "Performance metrics measured"
    ],
    "extraction_confidence": "high"
}

# Note: Scanned Results/Discussion for additional explicit RDMAP
# Most content describes outcomes rather than methods/protocols
# Several implicit protocols identified for Pass 4:
# - Device malfunction recovery protocol (mentioned but not described)
# - Bluetooth GPS connectivity troubleshooting (mentioned but procedure unclear)
# - Daily artifact inventory procedure (mentioned but not detailed)

# Add final protocol
data["protocols"].append(p015)

# Update extraction metadata - PASS 3 COMPLETE
data["extraction_timestamp"] = datetime.now(timezone.utc).isoformat()
data["extraction_notes"]["pass"] = 3
data["extraction_notes"]["section_extracted"] = "Pass 3 EXPLICIT RDMAP extraction COMPLETE. Extracted from all sections: Abstract through Discussion. Total explicit RDMAP: 2 research_designs, 6 methods, 15 protocols = 23 items. Liberal extraction strategy applied throughout. Several implicit RDMAP items noted for Pass 4 extraction: device troubleshooting protocols, artifact inventory procedures, error correction workflows. Next: Pass 4 implicit RDMAP extraction across full paper."
data["extraction_notes"]["extraction_strategy"] = "Pass 3 used liberal extraction philosophy: when uncertain about tier assignment or inclusion, erred on side of extraction. Focused on explicitly documented RDMAP items with clear verbatim quotes from Methods/Approach sections. Systematic scan of Abstract, Introduction, Deployment Context, System Requirements, FAIMS sections, detailed workflows (pages 7-17), and Results/Discussion."
data["extraction_notes"]["known_uncertainties"] = [
    "Some protocols may be borderline between Method and Protocol tiers",
    "Data cleaning procedures mentioned briefly - may warrant additional extraction",
    "Training procedures referenced but not fully documented",
    "Several implicit protocols noted but deferred to Pass 4"
]

# Save final Pass 3 state
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

# Generate summary statistics
total_items = len(data['evidence']) + len(data['claims']) + len(data['implicit_arguments'])
total_rdmap = len(data['research_designs']) + len(data['methods']) + len(data['protocols'])
grand_total = total_items + total_rdmap

print("=" * 70)
print("PASS 3 EXPLICIT RDMAP EXTRACTION COMPLETE")
print("=" * 70)
print(f"\nExplicit RDMAP Extracted:")
print(f"  Research Designs: {len(data['research_designs'])}")
print(f"  Methods: {len(data['methods'])}")
print(f"  Protocols: {len(data['protocols'])}")
print(f"  RDMAP Subtotal: {total_rdmap}")
print(f"\nPrevious Extractions:")
print(f"  Evidence: {len(data['evidence'])}")
print(f"  Claims: {len(data['claims'])}")
print(f"  Implicit Arguments: {len(data['implicit_arguments'])}")
print(f"  Claims/Evidence Subtotal: {total_items}")
print(f"\nGRAND TOTAL (after Pass 3): {grand_total} items")
print(f"\n" + "=" * 70)
print("NEXT STEP: Pass 4 - Implicit RDMAP extraction")
print("=" * 70)
print("\nImplicit RDMAP items to extract in Pass 4:")
print("  - Device malfunction recovery procedures")
print("  - Bluetooth GPS troubleshooting protocols")
print("  - Artifact inventory procedures")
print("  - Error correction workflows")
print("  - Other procedures mentioned but not detailed")
