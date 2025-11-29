#!/usr/bin/env python3
"""
Pass 6 Repair: Fix Cross-Reference Issues

Issue: Protocol P001 references M009, which was consolidated into M001 in Pass 5
Fix: Update P001's implements_method to reference M001 instead
"""

import json
from pathlib import Path

extraction_path = Path("outputs/ross-2005/extraction.json")
with open(extraction_path, 'r', encoding='utf-8') as f:
    extraction = json.load(f)

print("Pass 6 Repair: Fixing cross-reference issues...")

# Fix P001: Replace M009 reference with M001
for protocol in extraction["protocols"]:
    if protocol["id"] == "P001":
        if "implements_method" in protocol and "M009" in protocol["implements_method"]:
            protocol["implements_method"].remove("M009")
            if "M001" not in protocol["implements_method"]:
                protocol["implements_method"].append("M001")
            print(f"  ✓ Fixed P001: Updated implements_method from M009 → M001")

# Update extraction notes
extraction["extraction_notes"].append(
    "Pass 6 Repair complete: Fixed 1 cross-reference issue (P001 implements_method updated M009 → M001 after Pass 5 consolidation). "
    "Re-validation required."
)

with open(extraction_path, 'w', encoding='utf-8') as f:
    json.dump(extraction, f, indent=2, ensure_ascii=False)

print("\n✓ Pass 6 Repair complete")
print("  Cross-references updated")
print("  Re-running validation...")
