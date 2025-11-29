#!/usr/bin/env python3
"""
Pass 2: Rationalization of claims and evidence

Target: 15-20% reduction through:
- Consolidating redundant or over-granular items
- Removing calculation claims that just restate evidence
- Adding missing synthesis claims
- Verifying all relationships

Consolidation requires complete consolidation_metadata.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Load current extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

# Track consolidations
consolidations_log = []
additions_log = []
removals_log = []

print("Pass 2 Rationalization Starting...")
print(f"Current counts: {len(data['evidence'])} evidence, {len(data['claims'])} claims, {len(data['implicit_arguments'])} implicit arguments")

# ========================================
# EVIDENCE CONSOLIDATIONS
# ========================================

# No obvious evidence consolidations identified in current extraction
# All evidence items support different claim sets or provide distinct measurements

print("\nEvidence review: No consolidations identified")
print("  - All 32 evidence items provide distinct measurements or observations")
print("  - Each supports different claim combinations")

# ========================================
# CLAIMS CONSOLIDATIONS
# ========================================

print("\nClaims consolidation analysis...")

# Pattern 1: Redundant restatements of same finding
# C011, C012, C013 → These all restate the same two findings from Results
# C011: "Two factors predict mound vulnerability: land use and proximity to urban boundary"
# C012: "Conversion from pasture to annual agriculture increases likelihood of damage"
# C013: "Mounds further from urban boundaries are more likely to be damaged"
# These are progressive refinements stating the same core findings
# However, C011 is summary, C012/C013 are specific - keep all for hierarchical clarity

# Pattern 2: Methodological redundancy
# C042 and C043 both state logit superiority over linear regression for categorical variables
# Consolidate these as they make the same point

# Create consolidated C042-C043
consolidated_c042 = {
    "claim_id": "C042",
    "claim_text": "Ordered logit model chosen over simple linear regression for superior ability to accommodate categorical response variables like mound condition",
    "claim_type": "methodological_argument",
    "claim_role": "core",
    "primary_function": "methodological_justification",
    "claim_nature": "comparative",
    "supported_by": [],
    "supports_claims": ["C031"],
    "implicit_assumptions": [],
    "location": {
        "section": "2.3. Statistical method",
        "page": 4,
        "start_paragraph": 1,
        "end_paragraph": 2
    },
    "verbatim_quote": "An ordered logit model provided the best theoretical and empirical ﬁt for our observational data and desired outcome. We chose a logit response model over a simple linear regression for its superior ability to accommodate categorical response variables like mound condition.",
    "extraction_confidence": "high",
    "consolidation_metadata": {
        "consolidated_from": ["P1_C042", "P1_C043"],
        "consolidation_type": "compound_interpretation",
        "information_preserved": "complete",
        "rationale": "C042 and C043 both state that logit is superior to linear regression for categorical variables. Combined into single claim that captures both the overall superiority statement and the specific advantage."
    }
}

# Remove C043 (index 42 in 0-indexed list)
# Update cross-references from C043 to C042

# Pattern 3: Calculation claims
# No obvious calculation claims found - all claims provide interpretation beyond arithmetic

# Pattern 4: Near-duplicate interpretation claims
# C058 and C059 both describe pasture→agriculture simulation results
# C058: "Transformation of all pasture to annual agriculture predicts significant deterioration"
# C059: "Pasture to annual agriculture conversion causes approximately 30.16% decrease"
# C059 provides quantification of C058 - keep both as hierarchical pair

# Pattern 5: Similar but distinct interpretations in Discussion
# C073 and C087 both state depopulation threatens heritage
# C073: "Depopulation, village abandonment, and urban retreat can also threaten heritage"
# C087: "Results highlight the threat to cultural heritage posed by depopulation, de-urbanisation, and abandonment"
# These are making same point in different sections - consolidate

consolidated_c073 = {
    "claim_id": "C073",
    "claim_text": "Results indicate and highlight that depopulation, village abandonment, de-urbanisation, and urban retreat can threaten cultural heritage (contrasting with typical focus on sprawl)",
    "claim_type": "interpretation",
    "claim_role": "core",
    "primary_function": "theoretical_interpretation",
    "claim_nature": "evaluative",
    "supported_by": ["E025", "E030", "E031"],
    "supports_claims": ["C010", "C014"],
    "location": {
        "section": "4.1. Burial mound vulnerability + 4.2. Wider application",
        "page": 8,
        "start_paragraph": 4,
        "end_paragraph": 4
    },
    "verbatim_quote": "Our results indicate, however, that depopulation, village abandonment, and urban retreat can also threaten heritage. [...] Second, they highlight the threat to cultural heritage posed by depopulation, de-urbanisation, and abandonment of rural villages.",
    "extraction_confidence": "high",
    "consolidation_metadata": {
        "consolidated_from": ["P1_C073", "P1_C087"],
        "consolidation_type": "redundancy_elimination",
        "information_preserved": "complete",
        "rationale": "C073 and C087 make identical substantive point about depopulation threatening heritage, appearing in Discussion sections 4.1 and 4.2. Consolidated to eliminate redundancy while preserving both quote sources."
    }
}

# Pattern 6: Methodological consolidation opportunities
# C048, C049, C050, C051 all discuss logit vs probit vs multinomial choice
# These form a decision tree that could be consolidated

# However, upon review, these document distinct decision points:
# - C048: logit output respects discrete nature
# - C049: choice needed between logit/probit and multinomial/ordered
# - C050: logit chosen over probit (computational simplicity)
# - C051: ordered chosen over multinomial (retains ordering)
# Keep separate as they document different aspects of model selection

print("\nConsolidations identified:")
print("  1. C042 + C043 → C042 (logit superiority)")
print("  2. C073 + C087 → C073 (depopulation threatens heritage)")
print("  Total: 2 consolidations (2.0% reduction from 99 to 97 claims)")

# Apply consolidations
claims_before = len(data['claims'])

# Replace C042 (index 41)
data['claims'][41] = consolidated_c042

# Remove C043 (now index 42)
removed_c043 = data['claims'].pop(42)

# Replace C073 (need to find index)
c073_index = next(i for i, c in enumerate(data['claims']) if c['claim_id'] == 'C073')
data['claims'][c073_index] = consolidated_c073

# Remove C087 (need to find index)
c087_index = next(i for i, c in enumerate(data['claims']) if c['claim_id'] == 'C087')
removed_c087 = data['claims'].pop(c087_index)

consolidations_log.append({
    "type": "claims_consolidation",
    "consolidated": ["C042+C043", "C073+C087"],
    "result_ids": ["C042", "C073"],
    "reduction": 2
})

claims_after = len(data['claims'])

print(f"  Claims: {claims_before} → {claims_after} ({((claims_before - claims_after) / claims_before * 100):.1f}% reduction)")

# ========================================
# CROSS-REFERENCE UPDATES
# ========================================

print("\nUpdating cross-references after consolidation...")

# C043 → C042 references
# C087 → C073 references

# Update any claims that had C043 in supports_claims to use C042
# Update any claims that had C087 in supports_claims to use C073

for claim in data['claims']:
    if 'supports_claims' in claim and claim['supports_claims']:
        if 'C043' in claim['supports_claims']:
            claim['supports_claims'].remove('C043')
            if 'C042' not in claim['supports_claims']:
                claim['supports_claims'].append('C042')
        if 'C087' in claim['supports_claims']:
            claim['supports_claims'].remove('C087')
            if 'C073' not in claim['supports_claims']:
                claim['supports_claims'].append('C073')

# Update any claims that reference C043/C087 in supported_by
for claim in data['claims']:
    if 'supported_by' in claim and claim['supported_by']:
        # Claims don't reference other claims in supported_by, only evidence
        pass

# ========================================
# ADDITIONS: Missing synthesis claims
# ========================================

print("\nChecking for missing synthesis claims...")

# Pattern: Overlooked explicit recommendations
# The paper ends with strong statements about approach generalizability
# and requirements for application - these are well captured in C082-C099

# Pattern: Cross-subsection synthesis
# Major findings are well synthesized in Discussion and Conclusion

# No obvious missing claims identified

print("  No missing synthesis claims identified")

# ========================================
# IMPLICIT ARGUMENTS REVIEW
# ========================================

print("\nReviewing implicit arguments for completeness...")

# Current: 8 implicit arguments for 99 claims (now 97)
# Core claims count: C001, C002, C003, C006, C007, C009, C010, C014, C031, C034, C035, C036, C037, C039, C042, C058, C059, C060, C061, C073, C079, C080, C082, C085, C086, C092, C095, C096, C097, C098, C099

# Reviewing core claims for missing implicit arguments:
# - Most methodological claims (C001, C006, C007, etc.) have appropriate assumptions documented
# - Empirical claims (C002, C003, C058-C061) have key assumptions documented (IA003, IA004, IA005)
# - Limitations claims (C092-C094) appropriately note temporal limitations

# No obvious gaps in implicit argument coverage

print("  8 implicit arguments adequate for paper's argument structure")
print("  No additional implicit arguments identified")

# ========================================
# UPDATE METADATA
# ========================================

items_before = claims_before
items_after = claims_after
reduction_pct = ((items_before - items_after) / items_before) * 100

data["extraction_notes"]["pass2_rationalization"] = {
    "items_before_rationalization": items_before,
    "items_after_rationalization": items_after,
    "reduction_percentage": round(reduction_pct, 1),
    "consolidations_performed": len(consolidations_log),
    "additions_performed": len(additions_log),
    "boundary_corrections": 0,
    "notes": "Conservative rationalization targeting clear redundancy. Limited consolidation opportunities due to well-differentiated claims in source paper."
}

# Update timestamp
data["extraction_timestamp"] = datetime.now(timezone.utc).isoformat()

# Save updated extraction
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print("\n✓ Pass 2 rationalization complete")
print(f"✓ Evidence: {len(data['evidence'])} (no changes)")
print(f"✓ Claims: {items_before} → {items_after} (-{items_before - items_after}, {reduction_pct:.1f}% reduction)")
print(f"✓ Implicit arguments: {len(data['implicit_arguments'])} (no changes)")
print(f"✓ Consolidations: {len(consolidations_log)}")
print("\n⚠️  Note: Low reduction rate (2%) due to well-differentiated claims in technical paper")
print("   Each claim provides distinct information or interpretation")
print("✓ Saved to extraction.json")
