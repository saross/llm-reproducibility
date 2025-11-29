#!/usr/bin/env python3
"""
Pass 4: Implicit RDMAP Extraction

Current RDMAP: 27 items (4 designs, 10 methods, 13 protocols)
Current implicit: 4 items (2 methods, 2 protocols)
Implicit percentage: 14.8%

Target: 10-20% implicit RDMAP (already at 14.8%)
Review for additional implicit items from whole-paper perspective
"""

import json
from pathlib import Path

extraction_path = Path("outputs/ross-2005/extraction.json")
with open(extraction_path, 'r', encoding='utf-8') as f:
    extraction = json.load(f)

# Count current implicit RDMAP
current_implicit = sum(1 for m in extraction["methods"] if m.get("status") == "implicit")
current_implicit += sum(1 for p in extraction["protocols"] if p.get("status") == "implicit")
current_total_rdmap = len(extraction["research_designs"]) + len(extraction["methods"]) + len(extraction["protocols"])
current_implicit_pct = (current_implicit / current_total_rdmap * 100) if current_total_rdmap > 0 else 0

print(f"Pass 4 Implicit RDMAP review...")
print(f"  Current implicit RDMAP: {current_implicit}/{current_total_rdmap} ({current_implicit_pct:.1f}%)")
print(f"  Target: 10-20%")

# Additional implicit RDMAP items identified through whole-paper review
# These are procedures mentioned but not documented

additional_implicit_protocols = [
    {
        "id": "IP001",
        "content": "Source text edition specification: using specific editions of ancient texts without citing which editions",
        "protocol_type": "textual_source",
        "page": 303,
        "trigger_text": ["all translations by the author"],
        "trigger_locations": [{"section": "Analysis", "subsection": None, "paragraph": 1}],
        "inference_reasoning": "Ross states 'all translations by the author' but never specifies which Greek editions/texts he translated from. Standard practice would document source editions (e.g., OCT, Loeb, West), but these are unstated.",
        "implements_method": ["M001", "M002"],
        "expected_information_missing": ["Source text editions used", "Editorial choices for variant readings"],
        "reconstruction_confidence": "medium",
        "status": "implicit",
        "implicit_metadata": {
            "basis": "mentioned_but_undocumented",
            "assessment_implication": "Different editions/readings could affect philological interpretations"
        }
    },
    {
        "id": "IP002",
        "content": "Scholarly literature search scope: selecting which scholarly debates to engage without stating search/selection criteria",
        "protocol_type": "literature_selection",
        "page": 301,
        "trigger_text": ["Scholars who see Panhellenism as emerging primarily through opposition"],
        "trigger_locations": [{"section": "Introduction", "subsection": None, "paragraph": 2}],
        "inference_reasoning": "Ross engages with specific scholars (Finley, Nagy, Hall, Mackie, etc.) representing different positions, but never states how these were selected or whether systematic literature review was performed.",
        "implements_method": ["M004"],
        "expected_information_missing": ["Literature search strategy", "Inclusion/exclusion criteria", "Search dates/databases"],
        "reconstruction_confidence": "low",
        "status": "implicit",
        "implicit_metadata": {
            "basis": "mentioned_but_undocumented",
            "assessment_implication": "Selective engagement with literature may miss relevant positions"
        }
    }
]

# Add to extraction
extraction["protocols"].extend(additional_implicit_protocols)

# Recalculate implicit percentages
new_implicit = current_implicit + len(additional_implicit_protocols)
new_total_rdmap = current_total_rdmap + len(additional_implicit_protocols)
new_implicit_pct = (new_implicit / new_total_rdmap * 100) if new_total_rdmap > 0 else 0

# Update extraction notes
extraction["extraction_notes"].append(
    f"Pass 4 Implicit RDMAP complete: Added {len(additional_implicit_protocols)} implicit protocols. "
    f"Total implicit RDMAP: {new_implicit}/{new_total_rdmap} ({new_implicit_pct:.1f}%). "
    f"Implicit RDMAP breakdown: 0 implicit designs, 2 implicit methods (M008, M009), "
    f"{len([p for p in extraction['protocols'] if p.get('status') == 'implicit'])} implicit protocols. "
    f"Target 10-20% implicit RDMAP: {'ACHIEVED' if 10 <= new_implicit_pct <= 20 else 'OUTSIDE TARGET'}."
)

with open(extraction_path, 'w', encoding='utf-8') as f:
    json.dump(extraction, f, indent=2, ensure_ascii=False)

print(f"\n✓ Pass 4 Implicit RDMAP complete")
print(f"  - Implicit protocols added: {len(additional_implicit_protocols)}")
print(f"  - Total implicit RDMAP: {new_implicit}/{new_total_rdmap} ({new_implicit_pct:.1f}%)")
print(f"  - Breakdown: 0 implicit designs, 2 implicit methods, {len([p for p in extraction['protocols'] if p.get('status') == 'implicit'])} implicit protocols")
print(f"  - Target: 10-20%")
print(f"  - Status: {'WITHIN TARGET' if 10 <= new_implicit_pct <= 20 else 'OUTSIDE TARGET'}")
print(f"\nRUNNING TOTAL after Pass 4:")
print(f"  - Total RDMAP: {new_total_rdmap} ({len(extraction['research_designs'])} designs, {len(extraction['methods'])} methods, {len(extraction['protocols'])} protocols)")
print(f"  - Overall total: {len(extraction['evidence']) + len(extraction['claims']) + len(extraction['implicit_arguments']) + new_total_rdmap} items")
