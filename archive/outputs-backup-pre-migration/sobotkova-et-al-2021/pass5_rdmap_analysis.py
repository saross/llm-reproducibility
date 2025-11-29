#!/usr/bin/env python3
"""
Pass 5: RDMAP Rationalization Analysis
Systematic review of RDMAP items for consolidation opportunities
"""

import json
from pathlib import Path

# Load extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

print("=" * 70)
print("PASS 5: RDMAP RATIONALIZATION ANALYSIS")
print("=" * 70)

# Count items
designs = data['research_designs']
methods = data['methods']
protocols = data['protocols']

print(f"\nCurrent RDMAP Counts:")
print(f"  Research Designs: {len(designs)}")
print(f"  Methods: {len(methods)}")
print(f"  Protocols: {len(protocols)}")
print(f"  Total: {len(designs) + len(methods) + len(protocols)}")

print(f"\nTarget after 15-20% reduction: 26-27 items")

print("\n" + "=" * 70)
print("RESEARCH DESIGNS ANALYSIS (2 items)")
print("=" * 70)
for rd in designs:
    print(f"\n{rd['design_id']}: {rd['design_text'][:70]}...")
    print(f"  Type: {rd['design_type']}")
    print(f"  Status: {rd['design_status']}")

print("\nConsolidation Analysis:")
print("  - RD001 (comparative case study) and RD002 (requirements-driven)")
print("    are DISTINCT strategic decisions addressing different aspects:")
print("    * RD001: Overall research approach (case study evaluation)")
print("    * RD002: System selection methodology (requirements analysis)")
print("  - RECOMMENDATION: Keep separate - independent assessment required")

print("\n" + "=" * 70)
print("METHODS ANALYSIS (8 items)")
print("=" * 70)

method_groups = {
    "System customization": [],
    "Field workflows": [],
    "Quality control": [],
    "Training/comparison": []
}

for m in methods:
    print(f"\n{m['method_id']}: {m['method_text'][:70]}...")
    print(f"  Type: {m['method_type']}")
    print(f"  Status: {m['method_status']}")

    # Categorize
    if 'customization' in m['method_type'] or 'software' in m['method_type']:
        method_groups["System customization"].append(m['method_id'])
    elif 'data_collection' in m['method_type'] or 'management' in m['method_type']:
        method_groups["Field workflows"].append(m['method_id'])
    elif 'quality' in m['method_type']:
        method_groups["Quality control"].append(m['method_id'])
    else:
        method_groups["Training/comparison"].append(m['method_id'])

print("\n\nMethod Groupings:")
for group, items in method_groups.items():
    print(f"  {group}: {items}")

print("\nConsolidation Analysis:")
print("  - M001 (module reuse) and M004 (XML customization):")
print("    Both relate to customization but address different levels:")
print("    * M001: Strategic approach (reuse existing modules)")
print("    * M004: Technical mechanism (XML-based customization)")
print("    RECOMMENDATION: Keep separate - different assessment perspectives")
print("\n  - M005 (controlled vocabularies) and M006 (daily review):")
print("    Both relate to quality but at different stages:")
print("    * M005: Preventive controls (during data entry)")
print("    * M006: Detective controls (post-collection review)")
print("    RECOMMENDATION: Keep separate - different QA mechanisms")
print("\n  - All methods represent distinct tactical approaches")
print("    RECOMMENDATION: No consolidation warranted")

print("\n" + "=" * 70)
print("PROTOCOLS ANALYSIS (22 items)")
print("=" * 70)

# Group protocols by type
protocol_groups = {}
for p in protocols:
    ptype = p['protocol_type']
    if ptype not in protocol_groups:
        protocol_groups[ptype] = []
    protocol_groups[ptype].append({
        'id': p['protocol_id'],
        'text': p['protocol_text'][:60] + "...",
        'status': p['protocol_status']
    })

for ptype, items in sorted(protocol_groups.items()):
    print(f"\n{ptype.upper()} ({len(items)} protocols):")
    for item in items:
        print(f"  {item['id']} ({item['status']}): {item['text']}")

print("\n" + "=" * 70)
print("CONSOLIDATION OPPORTUNITIES")
print("=" * 70)

print("\nPotential consolidations identified:")
print("\n1. P011 (Feature Recording workflow) and P001 (Legacy feature protocol):")
print("   - P011 describes detailed daily workflow")
print("   - P001 describes core feature recording steps")
print("   - Assessment: P011 SUBSUMES P001 (workflow includes core steps)")
print("   - CONSOLIDATE: Merge P001 into P011")
print("   - Type: workflow_integration")
print("   - Reduction: 1 item")

print("\n2. P012 (Gridded Survey workflow) and P002 (Gridded survey protocol):")
print("   - P012 describes detailed daily workflow")
print("   - P002 describes core survey methodology")
print("   - Assessment: P012 SUBSUMES P002 (workflow includes methodology)")
print("   - CONSOLIDATE: Merge P002 into P012")
print("   - Type: workflow_integration")
print("   - Reduction: 1 item")

print("\n3. P003 (Bi-directional sync) and P013 (End-of-day sync):")
print("   - P003 describes general synchronization mechanism")
print("   - P013 describes specific daily sync workflow")
print("   - Assessment: DIFFERENT LEVELS - mechanism vs application")
print("   - KEEP SEPARATE: Independent assessment value")

print("\n4. Other protocols:")
print("   - All remaining protocols describe distinct procedures")
print("   - No clear redundancy or subsumption relationships")
print("   - Quality control protocols (P009, IP004) at different stages")
print("   - Data management protocols (P004, P010, P014) address different aspects")
print("   - Recovery/troubleshooting protocols (IP001, IP002) for distinct issues")

print("\n" + "=" * 70)
print("CONSOLIDATION RECOMMENDATION SUMMARY")
print("=" * 70)
print("\nProposed consolidations: 2")
print("  1. Merge P001 into P011 (feature recording workflow integration)")
print("  2. Merge P002 into P012 (survey workflow integration)")
print("\nExpected outcome:")
print("  - Current: 32 items (2 designs, 8 methods, 22 protocols)")
print("  - After consolidation: 30 items (2 designs, 8 methods, 20 protocols)")
print("  - Reduction: 2 items (6.25%)")
print("\nNote: 6.25% reduction is below 15-20% target, but appropriate because:")
print("  - System implementation paper with well-differentiated procedures")
print("  - Each protocol describes distinct operational step")
print("  - Over-consolidation would compromise assessment granularity")
print("  - Quality over quantity: maintain assessment utility")
