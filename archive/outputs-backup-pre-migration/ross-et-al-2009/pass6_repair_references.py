#!/usr/bin/env python3
"""
Pass 6: Repair Cross-References
Ross et al. 2009 - Remote Sensing and Archaeological Prospection in Apulia, Italy

Fix broken references from Pass 2 rationalization:
- Update evidence.supports_claims to point to consolidated claim IDs
- Update implicit_argument.related_claims to point to consolidated claim IDs
"""

import json
from datetime import datetime, timezone
from pathlib import Path

extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

print("=" * 70)
print("PASS 6: REPAIR CROSS-REFERENCES")
print("=" * 70)
print()

# Mapping from deleted/consolidated claims to their replacement IDs
# Based on Pass 2 rationalization operations
claim_id_mapping = {
    'C002': None,      # Deleted (vague claim)
    'C017': 'C016',    # Consolidated into C016
    'C026': None,      # Deleted (vague claim)
    'C046': 'C045',    # Consolidated into C045
    'C058': 'C056',    # Consolidated into C056
    'C067': 'C066',    # Consolidated into C066
    'C071': 'C069',    # Consolidated into C069
    'C083': 'C049',    # Consolidated into C049
    'C098': 'C097',    # Consolidated into C097
    'C103': None,      # Deleted (vague claim)
    'C111': 'C108',    # Consolidated into C108
    'C113': 'C110',    # Consolidated into C110
    'C116': 'C115',    # Consolidated into C115
    'C138': 'C134',    # Consolidated into C134
    'C140': 'C119',    # Consolidated into C119
    'C141': 'C134',    # Consolidated into C134
    'C142': 'C136',    # Consolidated into C136
    'C148': 'C145',    # Consolidated into C145
    'C151': 'C145'     # Consolidated into C145
}

# Track repairs
repairs = {
    'evidence_updates': [],
    'implicit_argument_updates': []
}

# =================================================================
# 1. REPAIR EVIDENCE → CLAIM REFERENCES
# =================================================================
print("1. Repairing Evidence → Claim References")
print("-" * 70)

for evidence in data['evidence']:
    if 'supports_claims' in evidence:
        original_refs = evidence['supports_claims'].copy()
        updated_refs = []

        for claim_id in original_refs:
            if claim_id in claim_id_mapping:
                # This claim was consolidated/deleted
                replacement = claim_id_mapping[claim_id]
                if replacement:
                    # Replace with consolidated claim
                    if replacement not in updated_refs:
                        updated_refs.append(replacement)
                    repairs['evidence_updates'].append(
                        f"{evidence['evidence_id']}: {claim_id} → {replacement}"
                    )
                else:
                    # Claim was deleted, remove reference
                    repairs['evidence_updates'].append(
                        f"{evidence['evidence_id']}: {claim_id} → REMOVED (deleted claim)"
                    )
            else:
                # Claim still exists, keep reference
                if claim_id not in updated_refs:
                    updated_refs.append(claim_id)

        evidence['supports_claims'] = updated_refs

print(f"  Updated {len(repairs['evidence_updates'])} evidence references")
for update in repairs['evidence_updates']:
    print(f"    {update}")

print()

# =================================================================
# 2. REPAIR IMPLICIT_ARGUMENT → CLAIM REFERENCES
# =================================================================
print("2. Repairing Implicit_Argument → Claim References")
print("-" * 70)

for implicit_arg in data['implicit_arguments']:
    if 'related_claims' in implicit_arg:
        original_refs = implicit_arg['related_claims'].copy()
        updated_refs = []

        for claim_id in original_refs:
            if claim_id in claim_id_mapping:
                # This claim was consolidated/deleted
                replacement = claim_id_mapping[claim_id]
                if replacement:
                    # Replace with consolidated claim
                    if replacement not in updated_refs:
                        updated_refs.append(replacement)
                    repairs['implicit_argument_updates'].append(
                        f"{implicit_arg['implicit_argument_id']}: {claim_id} → {replacement}"
                    )
                else:
                    # Claim was deleted, remove reference
                    repairs['implicit_argument_updates'].append(
                        f"{implicit_arg['implicit_argument_id']}: {claim_id} → REMOVED (deleted claim)"
                    )
            else:
                # Claim still exists, keep reference
                if claim_id not in updated_refs:
                    updated_refs.append(claim_id)

        implicit_arg['related_claims'] = updated_refs

print(f"  Updated {len(repairs['implicit_argument_updates'])} implicit_argument references")
for update in repairs['implicit_argument_updates']:
    print(f"    {update}")

print()

# =================================================================
# UPDATE EXTRACTION FILE
# =================================================================

data['extraction_notes']['pass6_reference_repair'] = {
    'completion_date': datetime.now(timezone.utc).isoformat(),
    'repairs_applied': {
        'evidence_updates': len(repairs['evidence_updates']),
        'implicit_argument_updates': len(repairs['implicit_argument_updates']),
        'total_repairs': len(repairs['evidence_updates']) + len(repairs['implicit_argument_updates'])
    },
    'claim_id_mapping': claim_id_mapping,
    'notes': 'Repaired broken cross-references resulting from Pass 2 claim consolidations/deletions. All evidence→claim and implicit_argument→claim references now point to valid claim IDs.'
}

data['extraction_timestamp'] = datetime.now(timezone.utc).isoformat()

with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print("=" * 70)
print("REFERENCE REPAIR COMPLETE")
print("=" * 70)
print(f"Total repairs: {len(repairs['evidence_updates']) + len(repairs['implicit_argument_updates'])}")
print(f"  - Evidence references updated: {len(repairs['evidence_updates'])}")
print(f"  - Implicit_argument references updated: {len(repairs['implicit_argument_updates'])}")
print()
print("Updated extraction.json saved")
print("=" * 70)
