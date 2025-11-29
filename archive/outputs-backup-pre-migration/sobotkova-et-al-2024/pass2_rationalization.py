#!/usr/bin/env python3
"""
Pass 2 Conservative Rationalization
Paper: Sobotkova et al. 2024 - Validating predictions of burial mounds

Target: 15-20% reduction through conservative consolidation
Starting: 79 items (38 evidence, 32 claims, 9 implicit arguments)
Target: ~67 items after consolidation

Philosophy: Conservative - only consolidate clear redundancies or overlaps
Preserve: All well-differentiated technical measurements and distinct claims
"""

import json
from pathlib import Path

extraction_file = Path("/home/shawn/Code/llm-reproducibility/outputs/sobotkova-et-al-2024/extraction.json")
with open(extraction_file, 'r') as f:
    extraction = json.load(f)

print("Pass 2 Rationalization Analysis")
print("=" * 60)
print(f"Starting items: {len(extraction['evidence'])} evidence, {len(extraction['claims'])} claims, {len(extraction['implicit_arguments'])} implicit arguments")
print(f"Total: {len(extraction['evidence']) + len(extraction['claims']) + len(extraction['implicit_arguments'])} items")
print()

# Analysis of consolidation opportunities
print("CONSOLIDATION OPPORTUNITIES:")
print("-" * 60)

# Evidence analysis
print("\nEVIDENCE (38 items):")
print("E001-E003: Performance metrics from abstract - DISTINCT (false neg, false pos, true pos)")
print("E006-E007: Siberian study context - DISTINCT (success rates vs environmental conditions)")
print("E014-E015: Publication analysis - DISTINCT (annual count vs percentage)")
print("E016-E018: Publication bias analysis - DISTINCT (different aspects)")
print("E019-E022: Data specifications - DISTINCT (different data sources/specs)")
print("E023-E027: Training specifications - DISTINCT (technical parameters)")
print("E028-E032: 2021 model results - DISTINCT measurements (F1, tagged tiles, detection rates)")
print("E033-E038: 2022 model results - DISTINCT measurements")
print()
print("RECOMMENDATION: Evidence items are well-differentiated technical measurements.")
print("No consolidations appropriate - all support claims independently.")
print("This is characteristic of quantitative validation papers.")
print()

# Claims analysis
print("CLAIMS (32 items):")
print()
print("CONSOLIDATION 1: C018 + C019 → Claims about 2021 model performance")
print("  C018: High false pos/neg despite good F1")
print("  C019: F1 improvement didn't translate to real-world performance")
print("  Analysis: C019 is supporting detail of C018's broader point")
print("  Decision: CONSOLIDATE into single claim about 2021 model failure")
print()
print("CONSOLIDATION 2: C028 + C029 → Time comparison claims")
print("  C028: Manual processing would take 42h")
print("  C029: Manual (42h) < Model development (135h)")
print("  Analysis: C029 is the comparison; C028 is component")
print("  Decision: CONSOLIDATE into single comparative claim")
print()
print("RECOMMENDATION: Conservative consolidation - 2 merges")
print("Reduction: 32 → 30 claims (6.25% reduction)")
print()

# Implicit arguments analysis
print("IMPLICIT ARGUMENTS (9 items):")
print("All are distinct, well-reasoned arguments with unique trigger patterns.")
print("RECOMMENDATION: No consolidations - preserve all 9 items")
print()

# Summary
print("=" * 60)
print("CONSOLIDATION SUMMARY:")
print("  Evidence: 38 → 38 (0% reduction) - appropriate for quantitative paper")
print("  Claims: 32 → 30 (6.25% reduction) - conservative")
print("  Implicit Arguments: 9 → 9 (0% reduction)")
print("  TOTAL: 79 → 77 items (2.5% reduction)")
print()
print("RATIONALE FOR LOW REDUCTION:")
print("  This is a quantitative validation paper with:")
print("  - Well-differentiated performance metrics (not redundant)")
print("  - Distinct model runs requiring separate reporting")
print("  - Technical specifications that are independently important")
print("  - Claims that are already appropriately scoped")
print()
print("  Low consolidation rate (2.5%) is APPROPRIATE for this paper type.")
print("  Compare to: eftimoski-et-al-2017 (2% claims reduction),")
print("             sobotkova-et-al-2021 (6.25% RDMAP reduction)")
print()
print("Proceeding with conservative consolidation...")
print()

# Perform consolidations

# CONSOLIDATION 1: Merge C018 + C019
claims = extraction['claims']
c018 = next(c for c in claims if c['claim_id'] == 'C018')
c019 = next(c for c in claims if c['claim_id'] == 'C019')

# Create consolidated claim
c018_new = {
    "claim_id": "C018",
    "claim_text": "First model run (2021) had high false positive (87.1%) and false negative (95.3%) rates despite good F1 score (0.87), demonstrating that F1 improvement over previous model did not translate to real-world performance",
    "claim_type": "finding",
    "claim_role": "core",
    "claim_status": "explicit",
    "verbatim_quote": "After image augmentation, the model reported good learning and model fit (F1 5 0.87). This F1 score indicated that the use of a pre-trained model improved performance by 0.05 compared to a previous, manually trained model. Nevertheless, only 19 out of 148 tiles (12.8%) tagged by the model with at least a 60% chance of having a mound actually contained one",
    "location": {"section": "Results", "subsection": "First run (2021)", "paragraph": 1},
    "supported_by_evidence": ["E028", "E029", "E030", "E031", "E032"],
    "supported_by_claims": [],
    "supports_claims": ["C002", "C003"],
    "alternatives_mentioned": False,
    "qualifications": [],
    "contradicts": [],
    "consolidation_metadata": {
        "consolidated_from": ["P1_C018", "P1_C019"],
        "consolidation_type": "compound_interpretation",
        "information_preserved": "complete",
        "rationale": "C019 (F1 improvement didn't translate) is supporting detail of C018's broader finding about model failure. Consolidated to eliminate redundancy while preserving both the performance metrics and the interpretation that internal metrics were misleading."
    }
}

# Remove C019, update C018
claims = [c for c in claims if c['claim_id'] != 'C019']
claims = [c018_new if c['claim_id'] == 'C018' else c for c in claims]

# Update cross-references: anything that referenced C019 should reference C018
for claim in claims:
    if 'C019' in claim.get('supported_by_claims', []):
        claim['supported_by_claims'] = [c if c != 'C019' else 'C018' for c in claim['supported_by_claims']]
    if 'C019' in claim.get('supports_claims', []):
        claim['supports_claims'] = [c if c != 'C019' else 'C018' for c in claim['supports_claims']]

# CONSOLIDATION 2: Merge C028 + C029
c028 = next(c for c in claims if c['claim_id'] == 'C028')
c029 = next(c for c in claims if c['claim_id'] == 'C029')

c028_new = {
    "claim_id": "C028",
    "claim_text": "Manual processing of 5,000 tiles at 30 seconds each would take approximately 42 hours, less than model development time of 135 hours",
    "claim_type": "comparative_analysis",
    "claim_role": "supporting",
    "claim_status": "explicit",
    "verbatim_quote": "With approximately 5,000 150 3 150 m tiles in our 600 sq km study area, and with an experienced operator able to make an assessment in ~30 s, manual processing would have taken approximately 42 h. Meanwhile, as reported above, simply developing the model required about 135 h",
    "location": {"section": "Discussion", "subsection": "Is it worth it?", "paragraph": 2},
    "supported_by_evidence": ["E004"],
    "supported_by_claims": [],
    "supports_claims": ["C027", "C004"],
    "alternatives_mentioned": False,
    "qualifications": ["approximately"],
    "contradicts": [],
    "consolidation_metadata": {
        "consolidated_from": ["P1_C028", "P1_C029"],
        "consolidation_type": "compound_interpretation",
        "information_preserved": "complete",
        "rationale": "C029 (comparison) depends entirely on C028 (manual time estimate). These form a single argumentative unit for cost-benefit analysis. Consolidated to eliminate redundancy while preserving both the time estimate and the comparison."
    }
}

# Remove C029, update C028
claims = [c for c in claims if c['claim_id'] != 'C029']
claims = [c028_new if c['claim_id'] == 'C028' else c for c in claims]

# Update cross-references for C029
for claim in claims:
    if 'C029' in claim.get('supported_by_claims', []):
        claim['supported_by_claims'] = [c if c != 'C029' else 'C028' for c in claim['supported_by_claims']]
    if 'C029' in claim.get('supports_claims', []):
        claim['supports_claims'] = [c if c != 'C029' else 'C028' for c in claim['supports_claims']]

extraction['claims'] = claims

# Update extraction notes
extraction['extraction_metadata']['extraction_notes'].append({
    "pass2_rationalization": {
        "pass_date": "2025-10-30",
        "starting_counts": {"evidence": 38, "claims": 32, "implicit_arguments": 9, "total": 79},
        "ending_counts": {"evidence": 38, "claims": 30, "implicit_arguments": 9, "total": 77},
        "reduction": {"items": 2, "percentage": 2.5},
        "consolidations_performed": [
            {
                "type": "claims",
                "consolidated_from": ["C018", "C019"],
                "consolidated_to": "C018",
                "rationale": "C019 (F1 improvement interpretation) is supporting detail of C018 (model failure). Compound interpretation consolidation."
            },
            {
                "type": "claims",
                "consolidated_from": ["C028", "C029"],
                "consolidated_to": "C028",
                "rationale": "C029 (time comparison) depends on C028 (manual time). Single argumentative unit. Compound interpretation consolidation."
            }
        ],
        "rationale_for_low_reduction": "Quantitative validation paper with well-differentiated performance metrics and technical specifications. Evidence items represent distinct measurements required for assessment. Low consolidation rate (2.5%) is appropriate for this paper type, consistent with other technical papers (eftimoski 2%, sobotkova-2021 6.25%).",
        "notes": "Conservative rationalization applied. Evidence items preserved as all represent distinct, independently assessable measurements. Claims consolidation focused on removing redundant supporting detail. Cross-references updated for consolidated items."
    }
})

# Save
with open(extraction_file, 'w') as f:
    json.dump(extraction, f, indent=2, ensure_ascii=False)

print("✓ Pass 2 rationalization complete")
print(f"  Evidence: 38 → 38 (no change)")
print(f"  Claims: 32 → 30 (-2 items, 6.25% reduction)")
print(f"  Implicit Arguments: 9 → 9 (no change)")
print(f"  TOTAL: 79 → 77 items (2.5% overall reduction)")
print()
print("Consolidations documented with complete metadata")
print("Cross-references updated for merged items")
