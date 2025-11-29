#!/usr/bin/env python3
"""
Pass 2 Rationalization for sobotkova-et-al-2016
Consolidates evidence/claims/implicit arguments and repairs cross-references
"""

import json
import copy
from datetime import datetime
from typing import Dict, List, Set

def load_extraction():
    """Load the extraction JSON"""
    with open('outputs/sobotkova-et-al-2016/extraction.json', 'r') as f:
        return json.load(f)

def consolidate_evidence(data: Dict) -> tuple:
    """Consolidate evidence items with identical support patterns"""

    consolidations = []
    items_before = len(data['evidence'])

    # Group 2: E007-E008 (server pricing alternatives)
    e007 = next(e for e in data['evidence'] if e['evidence_id'] == 'E007')
    e008 = next(e for e in data['evidence'] if e['evidence_id'] == 'E008')

    consolidated_e007 = {
        'evidence_id': 'E007',
        'verbatim_quote': f"{e007['verbatim_quote']} {e008['verbatim_quote']}",
        'page': e007['page'],
        'source_location': 'The FAIMS Mobile Platform / Customising and Deploying section',
        'evidence_tier': e007.get('evidence_tier', 'supporting'),
        'supports_claims': sorted(list(set(e007.get('supports_claims', []) + e008.get('supports_claims', [])))),
        'extraction_confidence': 'high',
        'consolidation_metadata': {
            'consolidated_from': ['P1_E007', 'P1_E008'],
            'consolidation_type': 'identical_support_pattern',
            'information_preserved': 'complete',
            'rationale': 'Both items support C018 only, providing alternative server deployment pricing options (purchase vs lease). Always cited together to demonstrate affordability flexibility.'
        },
        'status': 'explicit'
    }

    # Remove E008 from data
    data['evidence'] = [e for e in data['evidence'] if e['evidence_id'] != 'E008']
    # Replace E007 with consolidated version
    for i, e in enumerate(data['evidence']):
        if e['evidence_id'] == 'E007':
            data['evidence'][i] = consolidated_e007
            break

    consolidations.append({'type': 'evidence', 'ids': ['E007', 'E008'], 'result': 'E007'})

    # Group 4: E017-E018 (deployment speed examples)
    e017 = next(e for e in data['evidence'] if e['evidence_id'] == 'E017')
    e018 = next(e for e in data['evidence'] if e['evidence_id'] == 'E018')

    consolidated_e017 = {
        'evidence_id': 'E017',
        'verbatim_quote': f"{e017['verbatim_quote']} {e018['verbatim_quote']}",
        'page': e017['page'],
        'source_location': 'Theme 1: Scoping and Development section',
        'evidence_tier': e017.get('evidence_tier', 'supporting'),
        'supports_claims': sorted(list(set(e017.get('supports_claims', []) + e018.get('supports_claims', [])))),
        'extraction_confidence': 'high',
        'consolidation_metadata': {
            'consolidated_from': ['P1_E017', 'P1_E018'],
            'consolidation_type': 'identical_support_pattern',
            'information_preserved': 'complete',
            'rationale': 'Both items support C038 only, providing examples of rapid FAIMS deployment (PAZC 3.5 weeks, Boncuklu Spanish translation <1 week). Always cited together to demonstrate deployment speed.'
        },
        'status': 'explicit'
    }

    # Remove E018
    data['evidence'] = [e for e in data['evidence'] if e['evidence_id'] != 'E018']
    # Replace E017
    for i, e in enumerate(data['evidence']):
        if e['evidence_id'] == 'E017':
            data['evidence'][i] = consolidated_e017
            break

    consolidations.append({'type': 'evidence', 'ids': ['E017', 'E018'], 'result': 'E017'})

    # Group 6: E042-E043 (director quotes on interpretive impact)
    e042 = next(e for e in data['evidence'] if e['evidence_id'] == 'E042')
    e043 = next(e for e in data['evidence'] if e['evidence_id'] == 'E043')

    consolidated_e042 = {
        'evidence_id': 'E042',
        'verbatim_quote': f"{e042['verbatim_quote']} {e043['verbatim_quote']}",
        'page': e042['page'],
        'source_location': 'Theme 3: Digital Recording and Archaeological Interpretation section',
        'evidence_tier': e042.get('evidence_tier', 'supporting'),
        'supports_claims': sorted(list(set(e042.get('supports_claims', []) + e043.get('supports_claims', [])))),
        'extraction_confidence': 'high',
        'consolidation_metadata': {
            'consolidated_from': ['P1_E042', 'P1_E043'],
            'consolidation_type': 'identical_support_pattern',
            'information_preserved': 'complete',
            'rationale': 'Both items support C085 only, providing director quotes expressing uncertainty about immediate interpretive impact of digital methods. Redundant expressions of same observation.'
        },
        'status': 'explicit'
    }

    # Remove E043
    data['evidence'] = [e for e in data['evidence'] if e['evidence_id'] != 'E043']
    # Replace E042
    for i, e in enumerate(data['evidence']):
        if e['evidence_id'] == 'E042':
            data['evidence'][i] = consolidated_e042
            break

    consolidations.append({'type': 'evidence', 'ids': ['E042', 'E043'], 'result': 'E042'})

    items_after = len(data['evidence'])

    return data, consolidations, items_before, items_after

def repair_cross_references(data: Dict, consolidations: List[Dict]) -> Dict:
    """Repair cross-references after consolidation"""

    # Build consolidation map (old_id → new_id)
    consolidation_map = {}
    for cons in consolidations:
        result_id = cons['result']
        for old_id in cons['ids']:
            if old_id != result_id:
                consolidation_map[old_id] = result_id

    print(f"Consolidation map: {consolidation_map}")

    # Update claims → evidence references
    for claim in data.get('claims', []):
        if 'supported_by_evidence' in claim and claim['supported_by_evidence']:
            updated_refs = []
            for eid in claim['supported_by_evidence']:
                new_eid = consolidation_map.get(eid, eid)
                updated_refs.append(new_eid)
            # Remove duplicates while preserving order
            claim['supported_by_evidence'] = list(dict.fromkeys(updated_refs))

    # Update evidence → claims references (ensure bidirectional)
    # First, rebuild supported_by_evidence from evidence.supports_claims
    evidence_to_claims = {}
    for evidence in data.get('evidence', []):
        eid = evidence['evidence_id']
        for cid in evidence.get('supports_claims', []):
            if cid not in evidence_to_claims:
                evidence_to_claims[cid] = []
            evidence_to_claims[cid].append(eid)

    # Update claims with corrected supported_by_evidence
    for claim in data.get('claims', []):
        cid = claim['claim_id']
        if cid in evidence_to_claims:
            claim['supported_by_evidence'] = sorted(list(set(evidence_to_claims[cid])))
        else:
            claim['supported_by_evidence'] = []

    # Update implicit_arguments → claims references
    for ia in data.get('implicit_arguments', []):
        if 'related_claims' in ia and ia['related_claims']:
            # No consolidation of claims yet, so just ensure they're valid
            pass

    return data

def update_extraction_notes(data: Dict, items_before: int, items_after: int, consolidations: List[Dict]) -> Dict:
    """Update extraction_notes with Pass 2 info"""

    if 'extraction_notes' not in data:
        data['extraction_notes'] = {}

    # Add Pass 2 information
    data['extraction_notes']['pass2_rationalization'] = {
        'completion_date': datetime.now().isoformat(),
        'items_before': items_before,
        'items_after': items_after,
        'reduction_count': items_before - items_after,
        'reduction_percentage': round((items_before - items_after) / items_before * 100, 1),
        'evidence_consolidations': len([c for c in consolidations if c['type'] == 'evidence']),
        'claims_consolidations': len([c for c in consolidations if c['type'] == 'claim']),
        'consolidations_detail': consolidations,
        'rationale': 'Conservative evidence consolidation using empirical graph analysis (identical support patterns). 3 evidence groups consolidated (E007+E008, E017+E018, E042+E043). Claims and implicit arguments reviewed but no consolidation opportunities identified - items are well-differentiated with distinct analytical roles.'
    }

    return data

def rationalize_extraction():
    """Main rationalization function"""

    print("=" * 80)
    print("PASS 2 RATIONALIZATION - sobotkova-et-al-2016")
    print("=" * 80)
    print()

    # Load data
    data = load_extraction()

    items_before = (len(data.get('evidence', [])) +
                   len(data.get('claims', [])) +
                   len(data.get('implicit_arguments', [])))

    print(f"Before rationalization: {items_before} items")
    print(f"  Evidence: {len(data['evidence'])}")
    print(f"  Claims: {len(data['claims'])}")
    print(f"  Implicit Arguments: {len(data['implicit_arguments'])}")
    print()

    # Consolidate evidence
    print("Consolidating evidence...")
    data, consolidations, ev_before, ev_after = consolidate_evidence(data)
    print(f"  Evidence: {ev_before} → {ev_after} ({ev_before - ev_after} consolidated)")
    print()

    # Repair cross-references
    print("Repairing cross-references...")
    data = repair_cross_references(data, consolidations)
    print("  Cross-references updated")
    print()

    # Update extraction notes
    items_after = (len(data.get('evidence', [])) +
                  len(data.get('claims', [])) +
                  len(data.get('implicit_arguments', [])))

    data = update_extraction_notes(data, items_before, items_after, consolidations)

    print(f"After rationalization: {items_after} items")
    print(f"  Evidence: {len(data['evidence'])}")
    print(f"  Claims: {len(data['claims'])}")
    print(f"  Implicit Arguments: {len(data['implicit_arguments'])}")
    print(f"  Reduction: {items_before - items_after} items ({round((items_before - items_after) / items_before * 100, 1)}%)")
    print()

    # Save rationalized extraction
    with open('outputs/sobotkova-et-al-2016/extraction.json', 'w') as f:
        json.dump(data, f, indent=2)

    print("✓ Rationalization complete!")
    print("✓ Saved to: outputs/sobotkova-et-al-2016/extraction.json")
    print()

    # Validation check
    print("Validation check:")
    evidence_ids = {e['evidence_id'] for e in data['evidence']}
    broken_refs = []
    for claim in data['claims']:
        for eid in claim.get('supported_by_evidence', []):
            if eid not in evidence_ids:
                broken_refs.append(f"Claim {claim['claim_id']} → Evidence {eid}")

    if broken_refs:
        print(f"  ⚠️  Found {len(broken_refs)} broken references:")
        for ref in broken_refs[:10]:
            print(f"    {ref}")
    else:
        print("  ✓ No broken cross-references")
    print()

if __name__ == '__main__':
    rationalize_extraction()
