#!/usr/bin/env python3
"""
Pass 2 Analysis Script for Sobotkova et al. 2023
Analyses evidence support patterns and identifies consolidation opportunities
"""

import json
from collections import defaultdict
from typing import Dict, List, Set, Tuple

def load_extraction(filepath: str) -> Dict:
    """Load extraction.json file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_support_patterns(extraction: Dict) -> Dict[str, List[str]]:
    """
    Analyze evidence support patterns to identify items with identical claim support.
    Returns dict mapping support pattern (frozenset of claims) to list of evidence IDs.
    """
    pattern_map = defaultdict(list)

    for evidence in extraction['evidence']:
        # Get the support pattern as a frozenset for hashability
        support_pattern = frozenset(evidence.get('supporting_claims', []))
        pattern_map[support_pattern].append(evidence['evidence_id'])

    return dict(pattern_map)

def find_consolidation_candidates(extraction: Dict) -> Dict[str, List]:
    """
    Find evidence items that are candidates for consolidation.
    Returns dict with consolidation types and candidate groups.
    """
    candidates = {
        'identical_support': [],
        'temporal_breakdown': [],
        'measurement_breakdown': [],
        'error_rate_specs': []
    }

    # Find identical support patterns
    patterns = analyze_support_patterns(extraction)
    for pattern, ev_ids in patterns.items():
        if len(ev_ids) > 1 and len(pattern) > 0:  # Multiple items, not orphaned
            candidates['identical_support'].append({
                'pattern': sorted(list(pattern)),
                'evidence_ids': ev_ids,
                'count': len(ev_ids)
            })

    # Find temporal breakdowns (2017 vs 2018, etc)
    temporal_evidence = []
    for evidence in extraction['evidence']:
        content = evidence.get('content', '').lower()
        if any(year in content for year in ['2017', '2018', '2010']):
            temporal_evidence.append(evidence['evidence_id'])

    if len(temporal_evidence) > 1:
        candidates['temporal_breakdown'] = temporal_evidence

    # Find measurement breakdowns
    for evidence in extraction['evidence']:
        content = evidence.get('content', '')
        eid = evidence['evidence_id']
        if 'person-hours' in content or 'hours' in content:
            candidates['measurement_breakdown'].append(eid)

    return candidates

def print_consolidation_report(candidates: Dict):
    """Print analysis report of consolidation candidates"""
    print("="*80)
    print("PASS 2 CONSOLIDATION ANALYSIS")
    print("="*80)

    print("\n1. IDENTICAL SUPPORT PATTERN CANDIDATES:")
    print("-" * 80)
    if candidates['identical_support']:
        for group in sorted(candidates['identical_support'], key=lambda x: x['count'], reverse=True):
            print(f"\nPattern: {group['pattern']}")
            print(f"Evidence IDs ({group['count']} items): {', '.join(group['evidence_ids'])}")
    else:
        print("None found")

    print("\n\n2. TEMPORAL BREAKDOWN CANDIDATES:")
    print("-" * 80)
    if candidates['temporal_breakdown']:
        print(f"Evidence IDs: {', '.join(candidates['temporal_breakdown'])}")
    else:
        print("None found")

    print("\n\n3. MEASUREMENT BREAKDOWN CANDIDATES:")
    print("-" * 80)
    if candidates['measurement_breakdown']:
        print(f"Evidence IDs ({len(candidates['measurement_breakdown'])} items)")
        print(f"First 20: {', '.join(candidates['measurement_breakdown'][:20])}")
    else:
        print("None found")

def main():
    extraction = load_extraction('extraction.json')

    print(f"Current counts:")
    print(f"  Evidence: {len(extraction['evidence'])}")
    print(f"  Claims: {len(extraction['claims'])}")
    print(f"  Implicit Arguments: {len(extraction['implicit_arguments'])}")
    print()

    candidates = find_consolidation_candidates(extraction)
    print_consolidation_report(candidates)

    # Save detailed analysis to JSON
    with open('pass2_candidates.json', 'w') as f:
        json.dump(candidates, f, indent=2)
    print("\n\nDetailed analysis saved to pass2_candidates.json")

if __name__ == '__main__':
    main()
