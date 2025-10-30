#!/usr/bin/env python3
"""
Pass 6: Validation

Validates extraction completeness, integrity, and cross-reference consistency.
"""

import json
from pathlib import Path
from collections import Counter, defaultdict

extraction_file = Path("extraction.json")

print("=" * 80)
print("PASS 6: VALIDATION")
print("=" * 80)
print()

# Read extraction data
with open(extraction_file) as f:
    data = json.load(f)

errors = []
warnings = []

# Validate structure
print("1. Validating data structure...")
required_fields = ['claims', 'evidence', 'implicit_arguments', 'research_designs', 'methods', 'protocols']
for field in required_fields:
    if field not in data:
        errors.append(f"Missing required field: {field}")
    else:
        print(f"   ✓ {field}: {len(data[field])} items")

# Validate IDs are unique
print("\n2. Validating ID uniqueness...")
all_ids = defaultdict(list)
for claim in data['claims']:
    all_ids[claim['id']].append('claim')
for evidence in data['evidence']:
    all_ids[evidence['id']].append('evidence')
for ia in data['implicit_arguments']:
    all_ids[ia['id']].append('implicit_argument')
for rd in data['research_designs']:
    all_ids[rd['id']].append('research_design')
for method in data['methods']:
    all_ids[method['id']].append('method')
for protocol in data['protocols']:
    all_ids[protocol['id']].append('protocol')

duplicates = {id: types for id, types in all_ids.items() if len(types) > 1}
if duplicates:
    for id, types in duplicates.items():
        errors.append(f"Duplicate ID {id} used in: {', '.join(types)}")
else:
    print("   ✓ All IDs unique")

# Validate cross-references
print("\n3. Validating cross-references...")
claim_ids = set(c['id'] for c in data['claims'])
evidence_ids = set(e['id'] for e in data['evidence'])
ia_ids = set(ia['id'] for ia in data['implicit_arguments'])
method_ids = set(m['id'] for m in data['methods'])

broken_refs = 0
for claim in data['claims']:
    for ev_id in claim.get('supporting_evidence', []):
        if ev_id not in evidence_ids:
            warnings.append(f"Claim {claim['id']} references non-existent evidence {ev_id}")
            broken_refs += 1
    for ia_id in claim.get('related_implicit_arguments', []):
        if ia_id not in ia_ids:
            warnings.append(f"Claim {claim['id']} references non-existent implicit argument {ia_id}")
            broken_refs += 1

for evidence in data['evidence']:
    for claim_id in evidence.get('related_claims', []):
        if claim_id not in claim_ids:
            warnings.append(f"Evidence {evidence['id']} references non-existent claim {claim_id}")
            broken_refs += 1

for method in data['methods']:
    for claim_id in method.get('related_claims', []):
        if claim_id not in claim_ids:
            warnings.append(f"Method {method['id']} references non-existent claim {claim_id}")
            broken_refs += 1

if broken_refs == 0:
    print("   ✓ All cross-references valid")
else:
    print(f"   ⚠ {broken_refs} broken cross-references found")

# Validate required fields in items
print("\n4. Validating item fields...")
missing_fields = 0
for claim in data['claims']:
    required = ['id', 'content', 'claim_type', 'page']
    for field in required:
        if field not in claim:
            errors.append(f"Claim {claim.get('id', '?')} missing required field: {field}")
            missing_fields += 1

if missing_fields == 0:
    print("   ✓ All items have required fields")
else:
    print(f"   ✗ {missing_fields} items missing required fields")

# Summary statistics
print("\n5. Summary statistics...")
print(f"   Total items: {len(data['claims']) + len(data['evidence']) + len(data['implicit_arguments']) + len(data['research_designs']) + len(data['methods']) + len(data['protocols'])}")
print(f"   Claims: {len(data['claims'])}")
print(f"   Evidence: {len(data['evidence'])}")
print(f"   Implicit Arguments: {len(data['implicit_arguments'])}")
print(f"   Research Designs: {len(data['research_designs'])}")
print(f"   Methods: {len(data['methods'])}")
print(f"   Protocols: {len(data['protocols'])}")

# Coverage analysis
print("\n6. Coverage analysis...")
pages_with_items = set()
for claim in data['claims']:
    pages_with_items.add(claim.get('page'))
for evidence in data['evidence']:
    pages_with_items.add(evidence.get('page'))

print(f"   Pages with extracted items: {sorted(pages_with_items)}")
print(f"   Page range: {min(pages_with_items)} - {max(pages_with_items)}")

# Final report
print("\n" + "=" * 80)
print("VALIDATION COMPLETE")
print("=" * 80)
print()
if errors:
    print(f"ERRORS: {len(errors)}")
    for error in errors[:10]:  # Show first 10
        print(f"  - {error}")
    if len(errors) > 10:
        print(f"  ... and {len(errors) - 10} more")
else:
    print("✓ No errors found")

if warnings:
    print(f"\nWARNINGS: {len(warnings)}")
    for warning in warnings[:10]:  # Show first 10
        print(f"  - {warning}")
    if len(warnings) > 10:
        print(f"  ... and {len(warnings) - 10} more")
else:
    print("✓ No warnings")

if not errors:
    print("\n✓ Extraction validated successfully")
print("=" * 80)
