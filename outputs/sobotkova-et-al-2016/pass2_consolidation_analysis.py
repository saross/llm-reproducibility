#!/usr/bin/env python3
"""
Pass 2 Consolidation Analysis for sobotkova-et-al-2016
Analyses evidence/claims/implicit arguments for consolidation opportunities
"""

import json
from collections import defaultdict
from typing import Dict, List, Set, Tuple

def load_extraction():
    """Load the extraction JSON"""
    with open('outputs/sobotkova-et-al-2016/extraction.json', 'r') as f:
        return json.load(f)

def analyse_evidence_support_patterns(data: Dict) -> Dict:
    """
    Analyse evidence items by their claim support patterns (PRIMARY consolidation method)
    Returns groups of evidence with identical support patterns
    """
    # Build support pattern for each evidence item
    support_patterns = {}
    for evidence in data.get('evidence', []):
        eid = evidence['evidence_id']
        # Get all claims this evidence supports
        supports = frozenset(evidence.get('supports_claims', []))
        support_patterns[eid] = supports

    # Group evidence by support pattern
    pattern_groups = defaultdict(list)
    for eid, pattern in support_patterns.items():
        if pattern:  # Only group items that support at least one claim
            pattern_groups[pattern].append(eid)

    # Filter to groups with 2+ items (potential consolidations)
    consolidation_candidates = {
        pattern: eids
        for pattern, eids in pattern_groups.items()
        if len(eids) >= 2
    }

    return consolidation_candidates, support_patterns

def analyse_claims_structure(data: Dict) -> Dict:
    """Analyse claims for redundancy and synthesis opportunities"""
    claims_by_section = defaultdict(list)

    for claim in data.get('claims', []):
        page = claim.get('page', 0)
        claims_by_section[page].append(claim['claim_id'])

    return claims_by_section

def analyse_implicit_arguments(data: Dict) -> Dict:
    """Check implicit arguments completeness"""
    ia_count = len(data.get('implicit_arguments', []))
    core_claims = len([c for c in data.get('claims', []) if c.get('claim_tier') == 'core'])

    return {
        'total_implicit_arguments': ia_count,
        'core_claims': core_claims,
        'ratio': ia_count / core_claims if core_claims > 0 else 0
    }

def generate_consolidation_report(data: Dict) -> str:
    """Generate consolidation analysis report"""

    # Evidence analysis
    candidates, patterns = analyse_evidence_support_patterns(data)

    # Claims analysis
    claims_structure = analyse_claims_structure(data)

    # Implicit arguments analysis
    ia_stats = analyse_implicit_arguments(data)

    # Generate report
    report = []
    report.append("=" * 80)
    report.append("PASS 2 CONSOLIDATION ANALYSIS")
    report.append("=" * 80)
    report.append("")

    # Current counts
    report.append("CURRENT ITEM COUNTS:")
    report.append(f"  Evidence: {len(data.get('evidence', []))}")
    report.append(f"  Claims: {len(data.get('claims', []))}")
    report.append(f"  Implicit Arguments: {len(data.get('implicit_arguments', []))}")
    report.append(f"  TOTAL: {len(data.get('evidence', [])) + len(data.get('claims', [])) + len(data.get('implicit_arguments', []))}")
    report.append("")

    # Target reduction
    current_total = len(data.get('evidence', [])) + len(data.get('claims', [])) + len(data.get('implicit_arguments', []))
    target_reduction = int(current_total * 0.175)  # 17.5% (middle of 15-20%)
    target_total = current_total - target_reduction
    report.append("TARGET REDUCTION (15-20%, aiming for 17.5%):")
    report.append(f"  Current: {current_total}")
    report.append(f"  Target: ~{target_total}")
    report.append(f"  Reduction needed: ~{target_reduction} items")
    report.append("")

    # Evidence consolidation opportunities
    report.append("EVIDENCE CONSOLIDATION OPPORTUNITIES (Identical Support Patterns):")
    report.append("")
    if candidates:
        total_evidence_candidates = sum(len(eids) for eids in candidates.values())
        potential_savings = sum(len(eids) - 1 for eids in candidates.values())
        report.append(f"  Found {len(candidates)} groups with identical support patterns")
        report.append(f"  Total evidence items in groups: {total_evidence_candidates}")
        report.append(f"  Potential consolidation: {potential_savings} items")
        report.append("")

        for i, (pattern, eids) in enumerate(candidates.items(), 1):
            claims_list = ', '.join(sorted(pattern))
            report.append(f"  Group {i}: {len(eids)} evidence items")
            report.append(f"    Items: {', '.join(sorted(eids))}")
            report.append(f"    Support pattern: [{claims_list}]")
            report.append("")
    else:
        report.append("  No evidence items with identical support patterns found")
        report.append("  Evidence items have distinct analytical roles")
        report.append("")

    # Claims analysis
    report.append("CLAIMS ANALYSIS:")
    report.append(f"  Claims distributed across {len(claims_structure)} page ranges")
    report.append("  Manual review needed for:")
    report.append("    - Redundant calculation claims")
    report.append("    - Narrative consolidation opportunities")
    report.append("    - Cross-subsection synthesis")
    report.append("")

    # Implicit arguments completeness
    report.append("IMPLICIT ARGUMENTS COMPLETENESS:")
    report.append(f"  Total: {ia_stats['total_implicit_arguments']}")
    report.append(f"  Core claims: {ia_stats['core_claims']}")
    report.append(f"  Ratio: {ia_stats['ratio']:.2f} implicit args per core claim")
    if ia_stats['total_implicit_arguments'] < 3:
        report.append("  ⚠️  LOW COUNT - Verify if reasoning is genuinely explicit")
    report.append("")

    # Recommendations
    report.append("CONSOLIDATION STRATEGY:")
    report.append(f"1. Evidence: Apply identical support pattern consolidation ({len(candidates)} groups)")
    report.append("2. Claims: Manual review for narrative/synthesis consolidation")
    report.append("3. Implicit Arguments: Systematic Type 1-4 review (STEP 3)")
    report.append("4. Cross-reference repair: Update all references after consolidation")
    report.append("")

    return '\n'.join(report)

if __name__ == '__main__':
    data = load_extraction()
    report = generate_consolidation_report(data)
    print(report)

    # Save report
    with open('outputs/sobotkova-et-al-2016/pass2_analysis_report.txt', 'w') as f:
        f.write(report)

    print("Report saved to: outputs/sobotkova-et-al-2016/pass2_analysis_report.txt")
