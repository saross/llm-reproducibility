#!/usr/bin/env python3
"""
Pass 6 Fixes for sobotkova-et-al-2016
Repairs cross-references and validates corrections
"""

import json

# Load extraction
with open('outputs/sobotkova-et-al-2016/extraction.json', 'r') as f:
    data = json.load(f)

print("=" * 80)
print("PASS 6 FIXES")
print("=" * 80)
print()

fixes_applied = []

# Fix 1: Broken cross-reference (RD-IMP-002 → M-IMP-004)
# M-IMP-004 was consolidated into M-IMP-003 in Pass 5
# Need to update RD-IMP-002.enables_methods
print("Fix 1: Repairing broken cross-reference (RD-IMP-002 → M-IMP-004)")

for rd in data['research_designs']:
    if rd['design_id'] == 'RD-IMP-002':
        if rd.get('enables_methods') and 'M-IMP-004' in rd['enables_methods']:
            # Replace M-IMP-004 with M-IMP-003
            rd['enables_methods'] = [mid if mid != 'M-IMP-004' else 'M-IMP-003' for mid in rd['enables_methods']]
            # Remove duplicates
            rd['enables_methods'] = list(dict.fromkeys(rd['enables_methods']))
            fixes_applied.append({
                'fix': 'Update RD-IMP-002.enables_methods: M-IMP-004 → M-IMP-003',
                'reason': 'M-IMP-004 consolidated into M-IMP-003 in Pass 5'
            })
            print(f"  ✓ Updated: {rd['enables_methods']}")

# Fix 2: Low protocol-method linking (56.5%)
# Review protocols without methods and add links where appropriate
print()
print("Fix 2: Improving protocol-method linking...")

# Protocols that should link to methods:
protocol_method_links = {
    'P001': 'M001',  # Module reuse as-is → Module customisation
    'P002': 'M001',  # Heurist GUI → Module customisation
    'P003': 'M001',  # XML generator → Module customisation
    'P004': 'M001',  # Direct editing → Module customisation
    'P005': 'M002',  # Forking workflow → GitHub-based reuse
    # P006-P008 are deployment infrastructure, not method-specific
    # P009-P012 already linked
    # P013-P015 already linked
    # P016 already linked
    'P017': None,  # Data export - operational, not method-specific
    'P018': None,  # Data checking - operational, not method-specific
    # Implicit protocols - operational specifications without specific method links
}

for p in data['protocols']:
    pid = p['protocol_id']

    # Handle explicit protocols needing links
    if pid in protocol_method_links and protocol_method_links[pid]:
        target_method = protocol_method_links[pid]

        # Get current implements_method (handle both string and array)
        current = p.get('implements_method')
        if isinstance(current, str):
            current = [current] if current else []
        elif current is None:
            current = []

        if target_method not in current:
            current.append(target_method)
            p['implements_method'] = current
            fixes_applied.append({
                'fix': f'Link {pid} → {target_method}',
                'reason': 'Protocol implements this method'
            })
            print(f"  ✓ Linked {pid} → {target_method}")

# Normalize all implements_method to arrays
for p in data['protocols']:
    if 'implements_method' in p and isinstance(p['implements_method'], str):
        p['implements_method'] = [p['implements_method']] if p['implements_method'] else []

# Update extraction notes
if 'extraction_notes' not in data:
    data['extraction_notes'] = {}

data['extraction_notes']['pass6_validation_fixes'] = {
    'fixes_applied': len(fixes_applied),
    'details': fixes_applied,
    'note': 'Repaired broken cross-references after Pass 5 consolidation and improved protocol-method linking where appropriate. Many protocols (deployment options, infrastructure specifications) are intentionally not linked to specific methods as they operate at system level.'
}

# Save corrected extraction
with open('outputs/sobotkova-et-al-2016/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print()
print(f"✓ Applied {len(fixes_applied)} fixes")
print()
print("Fixes applied:")
for fix in fixes_applied:
    print(f"  - {fix['fix']}")
    print(f"    Reason: {fix['reason']}")
print()
print("✓ Corrected extraction saved")
