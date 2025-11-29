#!/usr/bin/env python3
"""
Pass 2: Consolidation Analysis
Identifies consolidation candidates among 154 extracted items

Strategy:
- Preserve ALL evidence items (15) - no consolidation
- Analyze 113 claims for consolidation opportunities
- Preserve ALL implicit arguments (26) - no consolidation
- Target: 15-20% reduction (24-31 items) → 130-140 items after Pass 2
- Focus: Similar methodological claims, repeated concepts, overlapping arguments

Analysis categories:
1. Definitional claims that overlap
2. Benefits of preregistration repeated multiple times
3. Similar critiques of current practice
4. Overlapping characterisations of archaeological methodology
5. Multiple claims about OSF templates/implementation

Consolidation principles:
- Merge when claims make essentially same point
- Preserve distinct conceptual contributions
- Keep claims with different evidence links separate
- Maintain argumentative structure and flow
"""

import json
from collections import defaultdict

# Load extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'r') as f:
    data = json.load(f)

print("=" * 80)
print("PASS 2: CONSOLIDATION ANALYSIS")
print("=" * 80)
print()
print(f"Starting totals:")
print(f"  Evidence: {len(data['evidence'])} items")
print(f"  Claims: {len(data['claims'])} items")
print(f"  Implicit Arguments: {len(data['implicit_arguments'])} items")
print(f"  TOTAL: {len(data['evidence']) + len(data['claims']) + len(data['implicit_arguments'])} items")
print()
print(f"Target after rationalization: 130-140 items")
print(f"Required reduction: 14-24 items (9-16%)")
print()

# ============================================================================
# CONSOLIDATION CANDIDATES
# ============================================================================

consolidation_groups = {
    "Group 1: Preregistration definitions/descriptions": {
        "items": ["C001", "C002"],
        "reasoning": "C001 defines preregistration's purposes, C002 defines what it is. These partially overlap but C001 focuses on benefits while C002 is definitional. KEEP SEPARATE - distinct purposes.",
        "action": "NO CONSOLIDATION"
    },

    "Group 2: Preregistration accommodates diverse approaches": {
        "items": ["C003", "C004", "C048"],
        "reasoning": "C003: accommodates inductive/deductive; C004: accommodates idiographic/nomothetic; C048: can accommodate diversity/transdisciplinarity. All make same basic point about flexibility. CONSOLIDATE C048 into expanded C003-C004 cluster.",
        "action": "CONSOLIDATE → C003_expanded"
    },

    "Group 3: Distinction between prediction/postdiction is important": {
        "items": ["C014", "C015"],
        "reasoning": "C014: both essential but must not be conflated; C015: formalisms enforce distinctions improve quality. C015 is logical extension of C014. CONSOLIDATE.",
        "action": "CONSOLIDATE → C014_expanded"
    },

    "Group 4: Problems from conflating prediction/postdiction": {
        "items": ["C016", "C017", "C018", "C019", "C020"],
        "reasoning": "All describe consequences of conflating prediction/postdiction: overconfidence (C016, C020), memory/bias issues (C017, C018), statistical errors (C019). Multiple distinct problems. C016 and C020 both about overconfidence. CONSOLIDATE C016+C020.",
        "action": "CONSOLIDATE → C016_expanded (overconfidence); KEEP C017, C018, C019 separate"
    },

    "Group 5: Just-in-time archaeology problems": {
        "items": ["C007", "C008", "C009"],
        "reasoning": "C007: lack of planning leads to modifications raising costs; C008: ad hoc changes limit quality; C009: hinders interoperability. All consequences of poor planning. C008+C009 both about data quality consequences. CONSOLIDATE C008+C009.",
        "action": "CONSOLIDATE → C008_expanded; KEEP C007 separate"
    },

    "Group 6: Three types of archaeologist under-investment": {
        "items": ["C036", "C037", "C038", "C039", "C040", "C041", "C042"],
        "reasoning": "C036-C037: imprecise documentation; C038-C039: implicit knowledge; C040-C042: late development. These are three distinct problems with distinct consequences. NO CONSOLIDATION - maintains three-part structure from paper.",
        "action": "NO CONSOLIDATION"
    },

    "Group 7: Preregistration helps/can overcome problems": {
        "items": ["C006", "C030", "C031", "C033", "C034", "C044", "C045", "C046"],
        "reasoning": "Multiple claims about how preregistration helps: C006 (counteract reluctance), C030 (encourages planning), C031 (help articulate approach), C033 (makes assumptions explicit), C034 (mitigates sociotechnical barrier), C044 (resist just-in-time), C045 (make explicit, scrutinize), C046 (overcome underinvestment). Several overlap significantly. C030+C046 both about overcoming underinvestment in planning. C033+C045 both about making things explicit. CONSOLIDATE these pairs.",
        "action": "CONSOLIDATE → C030_expanded (planning encouragement), C045_expanded (making explicit)"
    },

    "Group 8: Archaeological methodological diversity": {
        "items": ["C049", "C050", "C051", "C052"],
        "reasoning": "C049: archaeology is deductive/inductive/abductive; C050: defines abduction; C051: abduction seldom acknowledged; C052: quantitative/qualitative, idiographic/nomothetic. C049 introduces abduction, C050 defines it, C051 notes it's unacknowledged. C050+C051 could consolidate (definition + observation about lack of acknowledgment). CONSOLIDATE.",
        "action": "CONSOLIDATE → C050_expanded"
    },

    "Group 9: Preregistration and diversity": {
        "items": ["C053", "C054", "C055"],
        "reasoning": "C053: doesn't privilege approaches, demands articulation; C054: diversity makes articulation important; C055: explicit design avoids conflation. C054 is logical extension of C053 (diversity makes articulation MORE important). CONSOLIDATE.",
        "action": "CONSOLIDATE → C053_expanded"
    },

    "Group 10: Serendipity not a barrier": {
        "items": ["C057", "C058", "C059"],
        "reasoning": "C057: results not under control in any discipline; C058: research design IS under control; C059: prior knowledge allows stating how/why. Logical progression of single argument. C058+C059 form single point (design controllable because of prior knowledge). CONSOLIDATE.",
        "action": "CONSOLIDATE → C058_expanded"
    },

    "Group 11: What could/should be registered": {
        "items": ["C081", "C082", "C085", "C087", "C088"],
        "reasoning": "C081: data models and workflows; C082: will help meet TOP guidelines; C085: could include tradition, approach, hypotheses, plans, workflows, models; C087: approach+hypotheses combats biases; C088: models+workflows overcomes just-in-time. C085 is comprehensive list, others are specific recommendations. C087+C088 could consolidate as 'priorities'. CONSOLIDATE.",
        "action": "CONSOLIDATE → C087_expanded (priority recommendations)"
    },

    "Group 12: OSF/template recommendations": {
        "items": ["C091", "C092", "C093", "C094", "C095"],
        "reasoning": "C091: could use OSF; C092: OSF has templates including qualitative; C093: would benefit from domain-specific; C094: interim recommend OSF qualitative; C095: key fields from template. C091+C092 both about OSF availability. C093+C094 about development needs vs interim. CONSOLIDATE pairs.",
        "action": "CONSOLIDATE → C091_expanded (OSF infrastructure), C093_expanded (development path)"
    },

    "Group 13: Preregistration promotes good practice": {
        "items": ["C109", "C110", "C111"],
        "reasoning": "All from conclusions: C109 (pathway to solving challenges), C110 (promotes built-in not bolt-on), C111 (fosters slow not just-in-time). C110+C111 are parallel formulations of same point. CONSOLIDATE.",
        "action": "CONSOLIDATE → C110_expanded"
    },

    "Group 14: Ocean Health Index parallels": {
        "items": ["C096", "C097", "C098"],
        "reasoning": "C096: oceanography has small data problems; C097: includes questionable practices; C098: inhibited synthesis. C096+C098 make basic parallel (similar problems, similar consequences). C097 adds questionable practices dimension. CONSOLIDATE C096+C098.",
        "action": "CONSOLIDATE → C096_expanded"
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
        if "→" in group_data['action']:
            # Count how many consolidated groups result
            num_consolidated = group_data['action'].count("_expanded")
            reduction = num_items - num_consolidated
            total_consolidations += reduction
            print(f"  Reduction: {reduction} items ({num_items} → {num_consolidated})")
    print()

print("=" * 80)
print(f"ESTIMATED TOTAL REDUCTION: {total_consolidations} claims")
print(f"After Pass 2: ~{len(data['claims']) - total_consolidations} claims")
print(f"Total items after Pass 2: ~{154 - total_consolidations} items")
print(f"Reduction percentage: {total_consolidations / len(data['claims']) * 100:.1f}%")
print()

if total_consolidations >= 14 and total_consolidations <= 24:
    print("✓ Consolidation target achieved (14-24 items, 9-16%)")
elif total_consolidations < 14:
    print(f"⚠ Below target - need {14 - total_consolidations} more consolidations")
else:
    print(f"⚠ Above target - {total_consolidations - 24} too many consolidations")
print()

# Count by reasoning type
print("Claims by reasoning type:")
reasoning_counts = defaultdict(int)
for claim in data['claims']:
    reasoning_counts[claim['reasoning_type']] += 1

for reasoning_type, count in sorted(reasoning_counts.items(), key=lambda x: -x[1]):
    print(f"  {reasoning_type}: {count} claims")
print()

# Count by claim type
print("Claims by claim type:")
type_counts = defaultdict(int)
for claim in data['claims']:
    type_counts[claim['claim_type']] += 1

for claim_type, count in sorted(type_counts.items(), key=lambda x: -x[1]):
    print(f"  {claim_type}: {count} claims")
print()

print("✓ Analysis complete - ready for Pass 2 rationalization script")
print()
