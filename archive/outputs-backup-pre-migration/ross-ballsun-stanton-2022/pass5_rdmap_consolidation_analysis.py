#!/usr/bin/env python3
"""
Pass 5: RDMAP Consolidation Analysis
Identifies consolidation candidates among 43 RDMAP items

Current totals: 5 RD, 20 M, 18 P = 43 items
Target reduction: 15-20% (6-9 items) → 34-37 items after Pass 5

Strategy:
- Minimal RD consolidation (only 5 items, all distinct)
- Focus on Methods: Look for overlapping conceptual frameworks
- Focus on Protocols: Look for related OSF procedures, similar classification protocols
"""

import json

# Load extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'r') as f:
    data = json.load(f)

print("=" * 80)
print("PASS 5: RDMAP CONSOLIDATION ANALYSIS")
print("=" * 80)
print()
print(f"Starting totals:")
print(f"  Research Designs: {len(data['research_designs'])} items")
print(f"  Methods: {len(data['methods'])} items")
print(f"  Protocols: {len(data['protocols'])} items")
print(f"  TOTAL RDMAP: {len(data['research_designs']) + len(data['methods']) + len(data['protocols'])} items")
print()
print(f"Target after rationalization: 34-37 items")
print(f"Required reduction: 6-9 items (14-21%)")
print()

# ============================================================================
# CONSOLIDATION CANDIDATES
# ============================================================================

consolidation_groups = {
    "Group RD1: Research designs": {
        "items": ["RD001", "RD002", "RD003", "RD004", "RD005_implicit"],
        "reasoning": "RD001: overall paper design; RD002: comparative analysis; RD003: historical analysis; RD004: OSF survey; RD005_implicit: case study selection. All distinct analytical approaches. NO CONSOLIDATION - each serves different purpose.",
        "action": "NO CONSOLIDATION"
    },

    "Group M1: Conceptual framework methods": {
        "items": ["M001", "M007", "M008", "M009", "M015"],
        "reasoning": "M001: prediction/postdiction distinction; M007: deductive/inductive/abductive taxonomy; M008: abduction definition; M009: multi-axis diversity framework; M015: slow archaeology framework. M007+M008 both about abduction (taxonomy includes it, M008 defines it). Could consolidate M007+M008 as M008 is definitional component of M007's taxonomy. CONSOLIDATE.",
        "action": "CONSOLIDATE → M007_expanded (incorporate abduction definition)"
    },

    "Group M2: Literature/synthesis methods": {
        "items": ["M002", "M016_implicit", "M019_implicit"],
        "reasoning": "M002: literature review on reproducibility; M016_implicit: scoping preregistration literature; M019_implicit: historical synthesis of planning evolution. All literature-based but serve different purposes (reproducibility context vs preregistration knowledge vs historical narrative). KEEP SEPARATE.",
        "action": "NO CONSOLIDATION"
    },

    "Group M3: Analytical methods": {
        "items": ["M003", "M010", "M011", "M012", "M013", "M020_implicit"],
        "reasoning": "M003: survey data analysis (HARKing rates); M010: database search (OSF); M011: content analysis (registration type); M012: metadata completeness assessment; M013: template evaluation; M020_implicit: template evaluation (implicit). M013+M020_implicit both assess OSF templates - M013 is explicit, M020_implicit adds undocumented assessment criteria. These describe same method at different transparency levels. CONSOLIDATE.",
        "action": "CONSOLIDATE → M013_expanded (note implicit assessment criteria)"
    },

    "Group M4: Classification/framework construction": {
        "items": ["M004", "M005", "M006", "M014", "M017_implicit", "M018_implicit"],
        "reasoning": "M004: just-in-time archaeology characterisation; M005: FAIMS evidence synthesis; M006: under-investment framework; M014: analogical reasoning (Ocean Health Index); M017_implicit: argument construction structure; M018_implicit: typology construction (three types under-investment). M006+M018_implicit both about under-investment classification - M006 applies economic framework, M018_implicit derives three-type typology. Related but M018 is HOW the typology was created, M006 is WHAT framework was applied. KEEP SEPARATE (different analytical levels).",
        "action": "NO CONSOLIDATION"
    },

    "Group P1: Classification procedures": {
        "items": ["P001", "P002", "P004", "P014_implicit"],
        "reasoning": "P001: distinguishing prediction/postdiction; P002: identifying HARKing; P004: classifying under-investment types; P014_implicit: classifying registration types. All classification protocols but for different things (inquiry types, practices, under-investment, registrations). KEEP SEPARATE.",
        "action": "NO CONSOLIDATION"
    },

    "Group P2: Preregistration application protocols": {
        "items": ["P005", "P006", "P010", "P018_implicit"],
        "reasoning": "P005: applying preregistration to abductive research; P006: preregistering across methodological diversity; P010: adapting OSF qualitative template to archaeology; P018_implicit: determining registration content priorities. P006+P010 overlap - P006 is general (articulate position on methodological axes), P010 is specific (adapt OSF template to archaeology). P010 could be seen as implementation of P006 principles. CONSOLIDATE.",
        "action": "CONSOLIDATE → P006_expanded (incorporate template adaptation as implementation)"
    },

    "Group P3: OSF infrastructure protocols": {
        "items": ["P007", "P008", "P009", "P011", "P016_implicit", "P017_implicit"],
        "reasoning": "P007: searching OSF for archaeology; P008: creating preregistration on OSF; P009: completing qualitative template; P011: meeting TOP guidelines; P016_implicit: OSF search procedure; P017_implicit: adapting TOP criteria. P007+P016_implicit both OSF search (P007 explicit, P016 notes implicit search details). P008+P009 are sequential (create registration → complete template). P011+P017_implicit both TOP guidelines (P011 general, P017 adaptation). Multiple consolidation opportunities: P007+P016_implicit (search), P008+P009 (creation sequence), P011+P017_implicit (TOP compliance).",
        "action": "CONSOLIDATE → P007_expanded (search), P008_expanded (creation+completion sequence), P011_expanded (TOP compliance+adaptation)"
    },

    "Group P4: Assessment protocols": {
        "items": ["P003", "P012", "P013", "P015_implicit"],
        "reasoning": "P003: identifying just-in-time archaeology; P012: implementing slow archaeology; P013: built-in vs bolt-on practices; P015_implicit: assessing metadata completeness. P012+P013 both about implementing good practice principles (slow archaeology vs built-in practices) - these are parallel formulations. CONSOLIDATE.",
        "action": "CONSOLIDATE → P012_expanded (incorporate built-in principle)"
    }
}

print("CONSOLIDATION ANALYSIS:")
print()

total_consolidations = 0
for group_name, group_data in consolidation_groups.items():
    print(f"{group_name}:")
    print(f"  Items: {', '.join(group_data['items'])}")
    print(f"  Reasoning: {group_data['reasoning']}")
    print(f"  Action: {group_data['action']}")
    if "CONSOLIDATE" in group_data['action'] and "NO CONSOLIDATION" not in group_data['action']:
        # Count reductions
        num_items = len(group_data['items'])
        num_consolidated = group_data['action'].count("_expanded") + group_data['action'].count("→") - group_data['action'].count("_expanded")
        reduction = num_items - num_consolidated
        total_consolidations += reduction
        print(f"  Reduction: {reduction} items")
    print()

print("=" * 80)
print(f"ESTIMATED TOTAL REDUCTION: {total_consolidations} RDMAP items")
print(f"After Pass 5: ~{43 - total_consolidations} RDMAP items")
print(f"Reduction percentage: {total_consolidations / 43 * 100:.1f}%")
print()

if 6 <= total_consolidations <= 9:
    print("✓ Consolidation target achieved (6-9 items, 14-21%)")
elif total_consolidations < 6:
    print(f"⚠ Below target - need {6 - total_consolidations} more consolidations")
else:
    print(f"⚠ Above target - {total_consolidations - 9} too many consolidations")
print()
print("✓ Analysis complete - ready for Pass 5 rationalization script")
