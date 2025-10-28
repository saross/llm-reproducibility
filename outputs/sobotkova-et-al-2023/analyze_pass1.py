#!/usr/bin/env python3
"""
Analyze Pass 1 extraction to identify consolidation opportunities for Pass 2.

This script analyzes evidence/claim/implicit_argument arrays to find:
- Items with identical support patterns (primary consolidation signal)
- Potential boundary errors
- Missing relationships
- Consolidation opportunities
"""

import json
from collections import defaultdict
from pathlib import Path

def load_extraction():
    """Load the extraction JSON."""
    path = Path("/home/shawn/Code/llm-reproducibility/outputs/sobotkova-et-al-2023/extraction.json")
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_evidence_support_patterns(data):
    """Find evidence items with identical claim support patterns."""
    print("\n" + "="*80)
    print("EVIDENCE SUPPORT PATTERN ANALYSIS")
    print("="*80)

    # Group evidence by their support patterns
    pattern_groups = defaultdict(list)

    for ev in data['evidence']:
        # Create a tuple of sorted claim IDs
        pattern = tuple(sorted(ev.get('supporting_claims', [])))
        pattern_groups[pattern].append(ev['evidence_id'])

    # Find groups with multiple evidence items (consolidation candidates)
    print("\nEvidence groups with IDENTICAL support patterns (consolidation candidates):")
    print("-" * 80)

    consolidation_candidates = []
    for pattern, evidence_ids in sorted(pattern_groups.items()):
        if len(evidence_ids) > 1:
            consolidation_candidates.append((pattern, evidence_ids))
            print(f"\nSupports claims: {list(pattern) if pattern else '(none)'}")
            print(f"Evidence items: {', '.join(evidence_ids)} ({len(evidence_ids)} items)")

            # Show the content of these items
            for eid in evidence_ids:
                ev = next(e for e in data['evidence'] if e['evidence_id'] == eid)
                print(f"  {eid}: {ev['content'][:100]}...")

    if not consolidation_candidates:
        print("\nNo evidence items with identical support patterns found.")

    return consolidation_candidates

def analyze_evidence_by_section(data):
    """Analyze evidence distribution by section."""
    print("\n" + "="*80)
    print("EVIDENCE DISTRIBUTION BY SECTION")
    print("="*80)

    section_counts = defaultdict(int)
    for ev in data['evidence']:
        section = ev.get('location', {}).get('section', 'Unknown')
        section_counts[section] += 1

    for section, count in sorted(section_counts.items()):
        print(f"  {section}: {count} items")

def analyze_claims_by_type(data):
    """Analyze claims by type and support structure."""
    print("\n" + "="*80)
    print("CLAIMS ANALYSIS")
    print("="*80)

    type_counts = defaultdict(int)
    unsupported_claims = []

    for claim in data['claims']:
        claim_type = claim.get('claim_type', 'unknown')
        type_counts[claim_type] += 1

        # Check if claim has evidence support
        evidence_support = claim.get('supported_by_evidence', [])
        claim_support = claim.get('supported_by_claims', [])

        if not evidence_support and not claim_support:
            unsupported_claims.append(claim['claim_id'])

    print("\nClaims by type:")
    for claim_type, count in sorted(type_counts.items()):
        print(f"  {claim_type}: {count} items")

    if unsupported_claims:
        print(f"\n⚠️  Claims with no support: {', '.join(unsupported_claims)}")
    else:
        print("\n✓ All claims have evidence or claim support")

def analyze_implicit_arguments(data):
    """Analyze implicit arguments."""
    print("\n" + "="*80)
    print("IMPLICIT ARGUMENTS ANALYSIS")
    print("="*80)

    type_counts = defaultdict(int)
    for ia in data['implicit_arguments']:
        arg_type = ia.get('argument_type', 'unknown')
        type_counts[arg_type] += 1

    print(f"\nTotal implicit arguments: {len(data['implicit_arguments'])}")
    print("\nBy type:")
    for arg_type, count in sorted(type_counts.items()):
        print(f"  {arg_type}: {count} items")

def find_orphaned_references(data):
    """Find broken cross-references."""
    print("\n" + "="*80)
    print("CROSS-REFERENCE INTEGRITY CHECK")
    print("="*80)

    # Collect all valid IDs
    evidence_ids = {e['evidence_id'] for e in data['evidence']}
    claim_ids = {c['claim_id'] for c in data['claims']}

    errors = []

    # Check evidence → claims references
    for ev in data['evidence']:
        for claim_id in ev.get('supporting_claims', []):
            if claim_id not in claim_ids:
                errors.append(f"Evidence {ev['evidence_id']} references non-existent claim {claim_id}")

    # Check claims → evidence references
    for claim in data['claims']:
        for ev_id in claim.get('supported_by_evidence', []):
            if ev_id not in evidence_ids:
                errors.append(f"Claim {claim['claim_id']} references non-existent evidence {ev_id}")

        # Check claims → claims references
        for claim_id in claim.get('supported_by_claims', []):
            if claim_id not in claim_ids:
                errors.append(f"Claim {claim['claim_id']} references non-existent claim {claim_id}")

    # Check implicit arguments → claims references
    for ia in data['implicit_arguments']:
        for claim_id in ia.get('supports_claims', []):
            if claim_id not in claim_ids:
                errors.append(f"Implicit argument {ia['implicit_argument_id']} references non-existent claim {claim_id}")

    if errors:
        print("\n⚠️  CROSS-REFERENCE ERRORS FOUND:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("\n✓ All cross-references valid")

def main():
    print("Loading extraction.json...")
    data = load_extraction()

    print(f"\nPass 1 extraction loaded:")
    print(f"  Evidence: {len(data['evidence'])} items")
    print(f"  Claims: {len(data['claims'])} items")
    print(f"  Implicit Arguments: {len(data['implicit_arguments'])} items")

    # Run analyses
    consolidation_candidates = analyze_evidence_support_patterns(data)
    analyze_evidence_by_section(data)
    analyze_claims_by_type(data)
    analyze_implicit_arguments(data)
    find_orphaned_references(data)

    # Summary
    print("\n" + "="*80)
    print("CONSOLIDATION OPPORTUNITY SUMMARY")
    print("="*80)
    print(f"\nEvidence groups with identical support patterns: {len(consolidation_candidates)}")
    print(f"  These are PRIMARY consolidation candidates")
    print(f"\nTarget reduction: 15-20% = ~21-28 items")
    print(f"  Current: {len(data['evidence']) + len(data['claims']) + len(data['implicit_arguments'])} items")
    print(f"  Target: ~111-118 items")

if __name__ == "__main__":
    main()
