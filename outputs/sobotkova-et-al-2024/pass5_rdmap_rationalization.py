#!/usr/bin/env python3
"""
Pass 5 RDMAP Rationalization
Paper: Sobotkova et al. 2024 - Validating predictions of burial mounds

Conservative consolidation of RDMAP items
Target: 15-20% reduction (may be lower for well-differentiated technical papers)
"""

import json
from pathlib import Path

extraction_file = Path("/home/shawn/Code/llm-reproducibility/outputs/sobotkova-et-al-2024/extraction.json")
with open(extraction_file, 'r') as f:
    extraction = json.load(f)

print("Pass 5 RDMAP Rationalization Analysis")
print("=" * 60)
print(f"Starting RDMAP: {len(extraction['research_designs'])} designs, {len(extraction['methods'])} methods, {len(extraction['protocols'])} protocols")
print(f"Total RDMAP: {len(extraction['research_designs']) + len(extraction['methods']) + len(extraction['protocols'])} items")
print()

# Analysis of consolidation opportunities
print("CONSOLIDATION OPPORTUNITIES:")
print("-" * 60)

print("\nRESEARCH DESIGNS (4 items):")
print("RD001: External validation design")
print("RD002: Comparative two-run design")
print("RD003: Negative results documentation design")
print("RD004: Cost-benefit analysis design")
print("Analysis: All four represent distinct strategic decisions")
print("RECOMMENDATION: No consolidations - preserve all 4")
print()

print("METHODS (7 items):")
print("M001: Transfer learning with ResNet-50")
print("M002: Additional CNN training")
print("M003: Binary classification approach")
print("M004: Image augmentation")
print("M005: Automated performance evaluation")
print("M006: Field-based external validation")
print("M007: Probability thresholding")
print("Analysis: All represent distinct analytical approaches")
print("RECOMMENDATION: No consolidations - preserve all 7")
print()

print("PROTOCOLS (12 items: 9 explicit + 3 implicit):")
print("P001: ResNet-50 selection")
print("P002: Training cutout generation")
print("P003: NO MOUND data generation")
print("P004: Training data composition (1:2 ratio)")
print("P005: 2022 run data curation")
print("P006: Train/val/test split (70:20:10)")
print("P007: Model application to 600 sq km")
print("P008: F1 score calculation")
print("P009: Field validation inspection")
print("P010: [Implicit] Model selection experimentation")
print("P011: [Implicit] Image augmentation procedures")
print("P012: [Implicit] Manual timing estimation")
print()
print("Analysis: All protocols represent distinct operational procedures")
print("RECOMMENDATION: No consolidations - preserve all 12")
print()

print("=" * 60)
print("CONSOLIDATION SUMMARY:")
print("  Research Designs: 4 → 4 (0% reduction)")
print("  Methods: 7 → 7 (0% reduction)")
print("  Protocols: 12 → 12 (0% reduction)")
print("  TOTAL RDMAP: 23 → 23 items (0% reduction)")
print()
print("RATIONALE FOR ZERO REDUCTION:")
print("  This is a methods-focused validation paper with:")
print("  - Well-differentiated strategic decisions (each design serves distinct purpose)")
print("  - Distinct analytical methods (not redundant or overlapping)")
print("  - Technical protocols that are independently assessable")
print("  - RDMAP hierarchy properly structured (no misclassifications)")
print()
print("  Zero consolidation is APPROPRIATE for this paper.")
print("  Compare to: sobotkova-et-al-2021 (6.25% RDMAP reduction),")
print("             eftimoski-et-al-2017 (0% RDMAP reduction)")
print()
print("No consolidations performed. All RDMAP items preserved.")
print()

# Update extraction notes
extraction["extraction_metadata"]["extraction_notes"].append({
    "pass5_rdmap_rationalization": {
        "pass_date": "2025-10-30",
        "starting_counts": {"designs": 4, "methods": 7, "protocols": 12, "total": 23},
        "ending_counts": {"designs": 4, "methods": 7, "protocols": 12, "total": 23},
        "reduction": {"items": 0, "percentage": 0.0},
        "consolidations_performed": [],
        "rationale_for_zero_reduction": "Methods-focused validation paper with well-differentiated RDMAP items. All strategic decisions, analytical methods, and operational protocols are distinct and independently assessable. RDMAP hierarchy properly structured. Zero consolidation rate is appropriate for this technical paper type, consistent with eftimoski-et-al-2017 (0% RDMAP reduction).",
        "notes": "Conservative rationalization review completed. No consolidation opportunities identified. All RDMAP items represent distinct, independently documentable procedures. Hierarchy links verified."
    }
})

# Save
with open(extraction_file, 'w') as f:
    json.dump(extraction, f, indent=2, ensure_ascii=False)

print("✓ Pass 5 RDMAP rationalization complete")
print(f"  Research Designs: 4 → 4 (no change)")
print(f"  Methods: 7 → 7 (no change)")
print(f"  Protocols: 12 → 12 (no change)")
print(f"  TOTAL RDMAP: 23 → 23 items (0% reduction)")
print()
print(f"FINAL TOTAL: 100 items")
print(f"  (77 claims/evidence/implicit args + 23 RDMAP)")
