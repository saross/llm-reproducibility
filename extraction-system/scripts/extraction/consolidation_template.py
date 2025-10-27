#!/usr/bin/env python3
"""
Consolidation Template with Cross-Reference Repair

This is a TEMPLATE showing the standard consolidation workflow.
Adapt this for specific Pass 2 (Claims/Evidence) or Pass 4 (RDMAP) consolidations.

Key principles:
1. Consolidate items using consolidation_metadata to track source IDs
2. After ALL consolidations complete, repair cross-references
3. Validate that no broken references remain
4. Only then write the updated JSON

This prevents the common failure mode where consolidation creates broken
cross-references (e.g., claims pointing to deleted evidence IDs).
"""

import json


def repair_cross_references(data):
    """
    Repair all cross-references after consolidation.

    This function:
    1. Builds a map of old_id → new_id from consolidation_metadata
    2. Updates all cross-reference arrays to use new IDs
    3. Removes duplicate references created by consolidation

    Args:
        data: The extraction data dictionary with consolidation_metadata populated

    Returns:
        Number of ID mappings repaired
    """
    consolidation_map = {}  # old_id → new_id

    # Build consolidation map from all object types that might be consolidated
    for evidence in data.get('evidence', []):
        if evidence.get('consolidation_metadata'):
            new_id = evidence['evidence_id']
            for old_id in evidence['consolidation_metadata'].get('consolidated_from', []):
                consolidation_map[old_id] = new_id

    for method in data.get('methods', []):
        if method.get('consolidation_metadata'):
            new_id = method['method_id']
            for old_id in method['consolidation_metadata'].get('consolidated_from', []):
                consolidation_map[old_id] = new_id

    for protocol in data.get('protocols', []):
        if protocol.get('consolidation_metadata'):
            new_id = protocol['protocol_id']
            for old_id in protocol['consolidation_metadata'].get('consolidated_from', []):
                consolidation_map[old_id] = new_id

    for rd in data.get('research_designs', []):
        if rd.get('consolidation_metadata'):
            new_id = rd['design_id']
            for old_id in rd['consolidation_metadata'].get('consolidated_from', []):
                consolidation_map[old_id] = new_id

    # Repair all cross-references using the consolidation map

    # Claims → Evidence
    for claim in data.get('claims', []):
        if 'supported_by_evidence' in claim:
            # Map old IDs to new IDs
            updated = [consolidation_map.get(eid, eid) for eid in claim['supported_by_evidence']]
            # Remove duplicates (preserving order)
            claim['supported_by_evidence'] = list(dict.fromkeys(updated))

    # Methods → Protocols
    for method in data.get('methods', []):
        if 'realized_through_protocols' in method:
            updated = [consolidation_map.get(pid, pid) for pid in method['realized_through_protocols']]
            method['realized_through_protocols'] = list(dict.fromkeys(updated))
        if 'enabled_by_designs' in method:
            updated = [consolidation_map.get(rdid, rdid) for rdid in method['enabled_by_designs']]
            method['enabled_by_designs'] = list(dict.fromkeys(updated))

    # Research Designs → Methods
    for rd in data.get('research_designs', []):
        if 'enables_methods' in rd:
            updated = [consolidation_map.get(mid, mid) for mid in rd['enables_methods']]
            rd['enables_methods'] = list(dict.fromkeys(updated))

    # Protocols → Methods (single value, not array)
    for protocol in data.get('protocols', []):
        if protocol.get('implements_method'):
            old = protocol['implements_method']
            protocol['implements_method'] = consolidation_map.get(old, old)

    return len(consolidation_map)


def validate_cross_references(data):
    """
    Validate that all cross-references point to existing items.

    This catches any broken references that might remain after consolidation
    and repair. Should be run before writing the JSON file.

    Args:
        data: The extraction data dictionary

    Returns:
        Number of valid cross-references checked

    Raises:
        AssertionError: If any broken reference is found
    """
    # Build sets of all valid IDs
    evidence_ids = {e['evidence_id'] for e in data.get('evidence', [])}
    method_ids = {m['method_id'] for m in data.get('methods', [])}
    protocol_ids = {p['protocol_id'] for p in data.get('protocols', [])}
    rd_ids = {rd['design_id'] for rd in data.get('research_designs', [])}

    valid_count = 0

    # Check claims → evidence
    for claim in data.get('claims', []):
        for eid in claim.get('supported_by_evidence', []):
            assert eid in evidence_ids, f"Broken: {claim['claim_id']} → {eid}"
            valid_count += 1

    # Check methods → protocols
    for method in data.get('methods', []):
        for pid in method.get('realized_through_protocols', []):
            assert pid in protocol_ids, f"Broken: {method['method_id']} → {pid}"
            valid_count += 1

    # Check research_designs → methods
    for rd in data.get('research_designs', []):
        for mid in rd.get('enables_methods', []):
            assert mid in method_ids, f"Broken: {rd['design_id']} → {mid}"
            valid_count += 1

    # Check protocols → methods
    for protocol in data.get('protocols', []):
        if protocol.get('implements_method'):
            mid = protocol['implements_method']
            assert mid in method_ids, f"Broken: {protocol['protocol_id']} → {mid}"
            valid_count += 1

    return valid_count


# EXAMPLE USAGE
if __name__ == "__main__":
    # Load existing extraction
    with open('extraction.json', 'r') as f:
        data = json.load(f)

    # ============================================
    # YOUR CONSOLIDATION LOGIC HERE
    # ============================================
    # Example:
    # 1. Identify items to consolidate (e.g., identical support patterns)
    # 2. Create new consolidated item with consolidation_metadata
    # 3. Remove old items from array
    # 4. Continue for all consolidations
    # ============================================

    # CRITICAL: After ALL consolidations, repair cross-references
    num_repairs = repair_cross_references(data)
    print(f"✅ Repaired {num_repairs} ID mappings")

    # Validate that no broken references remain
    valid = validate_cross_references(data)
    print(f"✅ Validated {valid} cross-references - all valid")

    # Write updated extraction
    with open('extraction.json', 'w') as f:
        json.dump(data, f, indent=2)

    print("✅ Consolidation complete with cross-references repaired and validated")
