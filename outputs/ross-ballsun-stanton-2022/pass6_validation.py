#!/usr/bin/env python3
"""
Pass 6: Validation and Cross-Reference Repair

Validates extraction completeness and repairs cross-references broken by consolidations.

Validation checks:
1. All explicit items have verbatim_quote
2. All implicit items have trigger_text and inference_reasoning
3. All cross-references point to existing items
4. No duplicate IDs

Repair operations:
- Fix cross-references broken by Pass 2 and Pass 5 consolidations
"""

import json
from collections import defaultdict

# Load extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'r') as f:
    data = json.load(f)

print("=" * 80)
print("PASS 6: VALIDATION AND CROSS-REFERENCE REPAIR")
print("=" * 80)
print()

# ============================================================================
# BUILD ID REGISTRIES
# ============================================================================

evidence_ids = {e['id'] for e in data['evidence']}
claim_ids = {c['id'] for c in data['claims']}
implicit_arg_ids = {ia['id'] for ia in data['implicit_arguments']}
rd_ids = {rd['id'] for rd in data['research_designs']}
method_ids = {m['id'] for m in data['methods']}
protocol_ids = {p['id'] for p in data['protocols']}

all_ids = evidence_ids | claim_ids | implicit_arg_ids | rd_ids | method_ids | protocol_ids

print(f"ID Registry built:")
print(f"  Evidence: {len(evidence_ids)} IDs")
print(f"  Claims: {len(claim_ids)} IDs")
print(f"  Implicit Arguments: {len(implicit_arg_ids)} IDs")
print(f"  Research Designs: {len(rd_ids)} IDs")
print(f"  Methods: {len(method_ids)} IDs")
print(f"  Protocols: {len(protocol_ids)} IDs")
print(f"  Total unique IDs: {len(all_ids)}")
print()

# ============================================================================
# VALIDATION CHECKS
# ============================================================================

validation_issues = []
validation_warnings = []

print("Running validation checks...")
print()

# Check 1: Explicit items have verbatim_quote
print("Check 1: Explicit items have verbatim_quote...")
explicit_missing_quote = []

for e in data['evidence']:
    if e.get('evidence_status') == 'explicit' and not e.get('verbatim_quote'):
        explicit_missing_quote.append(('evidence', e['id']))

for c in data['claims']:
    # Claims don't have claim_status field, they're all explicit unless in implicit_arguments
    if not c.get('verbatim_quote'):
        explicit_missing_quote.append(('claim', c['id']))

for rd in data['research_designs']:
    if rd.get('design_status') == 'explicit' and not rd.get('verbatim_quote'):
        explicit_missing_quote.append(('research_design', rd['id']))

for m in data['methods']:
    if m.get('method_status') == 'explicit' and not m.get('verbatim_quote'):
        explicit_missing_quote.append(('method', m['id']))

for p in data['protocols']:
    if p.get('protocol_status') == 'explicit' and not p.get('verbatim_quote'):
        explicit_missing_quote.append(('protocol', p['id']))

if explicit_missing_quote:
    validation_issues.append(f"CRITICAL: {len(explicit_missing_quote)} explicit items missing verbatim_quote: {explicit_missing_quote[:10]}")
else:
    print("  ✓ All explicit items have verbatim_quote")

# Check 2: Implicit items have trigger_text and inference_reasoning (or reasoning)
print("Check 2: Implicit items have trigger_text and inference_reasoning...")
implicit_missing_triggers = []

for ia in data['implicit_arguments']:
    # Accept either 'inference_reasoning' or 'reasoning' for implicit arguments
    has_reasoning = ia.get('inference_reasoning') or ia.get('reasoning')
    if not ia.get('trigger_text') or not has_reasoning:
        implicit_missing_triggers.append(('implicit_argument', ia['id']))

for rd in data['research_designs']:
    if rd.get('design_status') == 'implicit':
        if not rd.get('trigger_text') or not rd.get('inference_reasoning'):
            implicit_missing_triggers.append(('research_design', rd['id']))

for m in data['methods']:
    if m.get('method_status') == 'implicit':
        if not m.get('trigger_text') or not m.get('inference_reasoning'):
            implicit_missing_triggers.append(('method', m['id']))

for p in data['protocols']:
    if p.get('protocol_status') == 'implicit':
        if not p.get('trigger_text') or not p.get('inference_reasoning'):
            implicit_missing_triggers.append(('protocol', p['id']))

if implicit_missing_triggers:
    validation_issues.append(f"CRITICAL: {len(implicit_missing_triggers)} implicit items missing trigger_text/inference_reasoning: {implicit_missing_triggers}")
else:
    print("  ✓ All implicit items have trigger_text and inference_reasoning")

# Check 3: Cross-reference integrity
print("Check 3: Cross-reference integrity...")
broken_references = []

def check_references(item, item_type, item_id):
    """Check all cross-reference fields in an item."""
    for field in ['evidence_refs', 'claim_refs', 'method_refs', 'protocol_refs', 'research_design_refs']:
        if field in item and item[field]:
            for ref_id in item[field]:
                if ref_id not in all_ids:
                    broken_references.append({
                        'item_type': item_type,
                        'item_id': item_id,
                        'field': field,
                        'broken_ref': ref_id
                    })

for e in data['evidence']:
    check_references(e, 'evidence', e['id'])
for c in data['claims']:
    check_references(c, 'claim', c['id'])
for ia in data['implicit_arguments']:
    check_references(ia, 'implicit_argument', ia['id'])
for rd in data['research_designs']:
    check_references(rd, 'research_design', rd['id'])
for m in data['methods']:
    check_references(m, 'method', m['id'])
for p in data['protocols']:
    check_references(p, 'protocol', p['id'])

if broken_references:
    print(f"  ⚠ Found {len(broken_references)} broken cross-references (will repair)")
    for br in broken_references[:10]:  # Show first 10
        print(f"    {br['item_type']} {br['item_id']}: {br['field']} references missing {br['broken_ref']}")
else:
    print("  ✓ All cross-references valid")

# Check 4: Duplicate IDs
print("Check 4: Duplicate IDs...")
all_ids_list = []
for e in data['evidence']:
    all_ids_list.append(('evidence', e['id']))
for c in data['claims']:
    all_ids_list.append(('claim', c['id']))
for ia in data['implicit_arguments']:
    all_ids_list.append(('implicit_argument', ia['id']))
for rd in data['research_designs']:
    all_ids_list.append(('research_design', rd['id']))
for m in data['methods']:
    all_ids_list.append(('method', m['id']))
for p in data['protocols']:
    all_ids_list.append(('protocol', p['id']))

id_counts = defaultdict(list)
for item_type, item_id in all_ids_list:
    id_counts[item_id].append(item_type)

duplicates = {k: v for k, v in id_counts.items() if len(v) > 1}
if duplicates:
    validation_issues.append(f"CRITICAL: Duplicate IDs found: {duplicates}")
else:
    print("  ✓ No duplicate IDs")

print()

# ============================================================================
# CROSS-REFERENCE REPAIR
# ============================================================================

if broken_references:
    print("=" * 80)
    print("REPAIRING BROKEN CROSS-REFERENCES")
    print("=" * 80)
    print()

    # Build consolidation mapping from Pass 2 and Pass 5
    consolidation_map = {}

    # Pass 2 claim consolidations (from pass2_rationalization.py)
    consolidation_map.update({
        'C004': 'C003_consolidated',
        'C048': 'C003_consolidated',
        'C015': 'C014_consolidated',
        'C020': 'C016_consolidated',
        'C009': 'C008_consolidated',
        'C046': 'C030_consolidated',
        'C051': 'C050_consolidated',
        'C054': 'C053_consolidated',
        'C059': 'C058_consolidated',
        'C088': 'C087_consolidated',
        'C092': 'C091_consolidated',
        'C094': 'C093_consolidated',
        'C111': 'C110_consolidated',
        'C098': 'C096_consolidated'
    })

    # Pass 5 RDMAP consolidations (from pass5_rdmap_rationalization.py)
    consolidation_map.update({
        'M008': 'M007_consolidated',
        'M020_implicit': 'M013_consolidated',
        'P010': 'P006_consolidated',
        'P016_implicit': 'P007_consolidated',
        'P009': 'P008_consolidated',
        'P017_implicit': 'P011_consolidated',
        'P013': 'P012_consolidated'
    })

    # Track repairs
    repairs_made = []

    def repair_references(item):
        """Repair broken references in an item using consolidation map."""
        for field in ['evidence_refs', 'claim_refs', 'method_refs', 'protocol_refs', 'research_design_refs']:
            if field in item and item[field]:
                repaired_refs = []
                for ref_id in item[field]:
                    if ref_id not in all_ids:
                        # Try to find replacement in consolidation map
                        if ref_id in consolidation_map:
                            repaired_refs.append(consolidation_map[ref_id])
                            repairs_made.append((item.get('id', 'unknown'), field, ref_id, consolidation_map[ref_id]))
                            print(f"  Repaired {field} in {item.get('id', 'unknown')}: {ref_id} → {consolidation_map[ref_id]}")
                        else:
                            # Keep broken reference but flag it
                            repaired_refs.append(ref_id)
                            print(f"  ⚠ WARNING: Cannot repair {field} in {item.get('id', 'unknown')}: {ref_id} not in consolidation map")
                    else:
                        repaired_refs.append(ref_id)
                item[field] = repaired_refs

    # Apply repairs
    for e in data['evidence']:
        repair_references(e)
    for c in data['claims']:
        repair_references(c)
    for ia in data['implicit_arguments']:
        repair_references(ia)
    for rd in data['research_designs']:
        repair_references(rd)
    for m in data['methods']:
        repair_references(m)
    for p in data['protocols']:
        repair_references(p)

    print()
    print(f"✓ Made {len(repairs_made)} cross-reference repairs")
    print()

# ============================================================================
# VALIDATION SUMMARY
# ============================================================================

print("=" * 80)
print("VALIDATION SUMMARY")
print("=" * 80)
print()

if validation_issues:
    print(f"❌ CRITICAL ISSUES: {len(validation_issues)}")
    for issue in validation_issues:
        print(f"  - {issue}")
    print()
    validation_status = "FAIL"
else:
    print("✓ No critical issues found")
    validation_status = "PASS"

if validation_warnings:
    print(f"⚠ WARNINGS: {len(validation_warnings)}")
    for warning in validation_warnings:
        print(f"  - {warning}")
    print()
else:
    print("✓ No warnings")

if broken_references and len(repairs_made) > 0:
    print(f"✓ Cross-reference repairs: {len(repairs_made)} references repaired")
    if len(repairs_made) < len(broken_references):
        validation_status = "PASS_WITH_WARNINGS"
        print(f"  ⚠ {len(broken_references) - len(repairs_made)} references could not be repaired")

# Update metadata
data['extraction_notes']['pass6_validation'] = {
    'validation_status': validation_status,
    'critical_issues': len(validation_issues),
    'warnings': len(validation_warnings),
    'broken_references_found': len(broken_references),
    'references_repaired': len(repairs_made) if broken_references else 0,
    'checks_performed': [
        'explicit_items_have_verbatim_quote',
        'implicit_items_have_trigger_text_and_reasoning',
        'cross_reference_integrity',
        'no_duplicate_ids'
    ]
}

# Save updated extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print()
print(f"Final validation status: {validation_status}")
print()
print("✓ Pass 6 validation complete - extraction.json updated")
print()
