#!/usr/bin/env python3
"""
Pass 6 Repair: Fix cross-reference issues
"""

import json
from pathlib import Path

extraction_file = Path("/home/shawn/Code/llm-reproducibility/outputs/sobotkova-et-al-2024/extraction.json")
with open(extraction_file, 'r') as f:
    extraction = json.load(f)

print("Pass 6 Repair: Fixing cross-references")
print("=" * 60)

# Fix E028 and E029 - remove reference to consolidated C019
for evidence in extraction['evidence']:
    if evidence['evidence_id'] in ['E028', 'E029']:
        if 'C019' in evidence['supports_claims']:
            print(f"Removing C019 reference from {evidence['evidence_id']}")
            evidence['supports_claims'] = [c for c in evidence['supports_claims'] if c != 'C019']
            if 'C018' not in evidence['supports_claims']:
                evidence['supports_claims'].append('C018')
                print(f"  Added C018 reference to {evidence['evidence_id']}")

# Update extraction notes
extraction['extraction_metadata']['extraction_notes'].append({
    "pass6_repair": {
        "repair_date": "2025-10-30",
        "repairs_performed": [
            {
                "issue": "E028 and E029 referenced consolidated claim C019",
                "action": "Removed C019, verified C018 reference present",
                "rationale": "C019 was consolidated into C018 in Pass 2, references not updated in evidence"
            }
        ],
        "notes": "Cross-reference repair completed. Evidence items now correctly reference C018."
    }
})

with open(extraction_file, 'w') as f:
    json.dump(extraction, f, indent=2, ensure_ascii=False)

print()
print("✓ Repairs complete")
print("Re-running validation...")
