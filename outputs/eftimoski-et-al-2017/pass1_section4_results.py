#!/usr/bin/env python3
"""
Pass 1 Section 4: Extract evidence and claims from Results (section 3, pages 6-7)

Focus on quantitative results from simulations and statistical analyses.
Liberal extraction philosophy: When uncertain, include it.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Load current extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

print("Extracting evidence from Results section...")

# New EVIDENCE items (E022-E030)
new_evidence = [
    {
        "evidence_id": "E022",
        "evidence_text": "Simulating change in proximity to Kazanlak indicated no realistic increase or decrease would have significant impact on mound condition",
        "evidence_type": "analytical_result",
        "evidence_basis": "statistical_output",
        "supports_claims": ["C056"],
        "location": {
            "section": "3.1. Null results",
            "page": 6,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "As noted above (Section 2.2), simulating a change in proximity to Kazanlak indicated that no realistic increase or decrease in its size would have a signiﬁcant impact on mound condition, despite the fact that Kazanlak is the regional center and approximately 10 times the size of the next largest town.",
        "extraction_confidence": "high"
    },
    {
        "evidence_id": "E023",
        "evidence_text": "Simulations produced almost no impact when land converted from forest to annual agriculture or forest to pasture",
        "evidence_type": "analytical_result",
        "evidence_basis": "statistical_output",
        "supports_claims": ["C057"],
        "location": {
            "section": "3.1. Null results",
            "page": 6,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Simulations also produced almost no impact when land was converted from forest to annual agriculture or forest to pasture.",
        "extraction_confidence": "high"
    },
    {
        "evidence_id": "E024",
        "evidence_text": "Pasture to annual agriculture simulation: Mean probability of well-preserved mounds (Condition 1-2) decreases from 55.63% to 25.47% (30.16% decrease), damaged mounds (Condition 3-5) increase from 44.36% to 74.53%",
        "evidence_type": "quantitative_result",
        "evidence_basis": "statistical_output",
        "supports_claims": ["C058", "C059"],
        "declared_uncertainty": {
            "type": "approximation",
            "indicator": "ca.",
            "quantification": "ca. 30%"
        },
        "location": {
            "section": "3.2. Ordered logit simulation 1",
            "page": 6,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "Expressed in this manner, the simulation predicts approximately a 30.16% decrease in the probability of mounds being well-preserved, and a corresponding increase in the probability of mounds being more damaged, should all pasture be converted to annual agriculture.",
        "extraction_confidence": "high",
        "extraction_notes": "Values calculated from Table 2: Current (3.38+52.25=55.63%), Simulated (0.95+24.52=25.47%)"
    },
    {
        "evidence_id": "E025",
        "evidence_text": "Urban boundary retreat simulation: Mean probability of well-preserved mounds (Condition 1-2) decreases from 55.63% to 47.05% (8.59% decline), damaged mounds (Condition 3-5) increase from 44.36% to 52.96%",
        "evidence_type": "quantitative_result",
        "evidence_basis": "statistical_output",
        "supports_claims": ["C060", "C061"],
        "declared_uncertainty": {
            "type": "approximation",
            "indicator": "ca.",
            "quantification": "ca. 9%"
        },
        "location": {
            "section": "3.3. Ordered logit simulation 2",
            "page": 6,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Again using changes in mean probability as an indication of the scale of the shifts, the simulation predicts an 8.59% decline in mean probability of well-preserved mounds, accompanied by a corresponding net increase in more damaged mounds (Table 3), as remoteness increases.",
        "extraction_confidence": "high",
        "extraction_notes": "Values calculated from Table 3: Current (3.38+52.25=55.63%), Simulated (2.34+44.71=47.05%)"
    },
    {
        "evidence_id": "E026",
        "evidence_text": "Elevation coefficient: 0.003 (P<0.1), indicating for every 1 m elevation increase, odds of Category 5 condition are 1.003 times greater",
        "evidence_type": "statistical_output",
        "evidence_basis": "statistical_output",
        "supports_claims": ["C062"],
        "declared_uncertainty": {
            "type": "statistical",
            "indicator": "P<0.1",
            "quantification": "P<0.1"
        },
        "location": {
            "section": "3.4. Height and elevation",
            "page": 6,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Calculating the 'effect' coefﬁcient for 'elevation' and 'height' produces values of 0.003 and −0.070 respectively. These values indicate, for example, that for every 1 m increase in elevation, the odds of a mound being in Category 5 versus any other category are 1.003 times greater.",
        "extraction_confidence": "high"
    },
    {
        "evidence_id": "E027",
        "evidence_text": "Height coefficient: -0.070 (P<0.1), indicating for every 1 m height increase, odds of Category 5 condition are 0.930 times as much (odds decline)",
        "evidence_type": "statistical_output",
        "evidence_basis": "statistical_output",
        "supports_claims": ["C063"],
        "declared_uncertainty": {
            "type": "statistical",
            "indicator": "P<0.1",
            "quantification": "P<0.1"
        },
        "location": {
            "section": "3.4. Height and elevation",
            "page": 6,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Conversely, for every m increase in mound height, the odds of it being in Category 5 versus any other category are 0.930 times as much (i.e., the odds decline).",
        "extraction_confidence": "high"
    },
    {
        "evidence_id": "E028",
        "evidence_text": "Pasture coefficient: -2.246 (P<0.01, highly significant)",
        "evidence_type": "statistical_output",
        "evidence_basis": "statistical_output",
        "supports_claims": ["C058"],
        "declared_uncertainty": {
            "type": "statistical",
            "indicator": "***",
            "quantification": "P<0.01"
        },
        "location": {
            "section": "3. Results",
            "page": 6,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Pasture                          −2.246***                        0.666",
        "extraction_confidence": "high",
        "extraction_notes": "From Table 1. Negative coefficient indicates pasture associated with better condition"
    },
    {
        "evidence_id": "E029",
        "evidence_text": "Forest coefficient: -1.943 (P<0.01, highly significant)",
        "evidence_type": "statistical_output",
        "evidence_basis": "statistical_output",
        "supports_claims": ["C057"],
        "declared_uncertainty": {
            "type": "statistical",
            "indicator": "***",
            "quantification": "P<0.01"
        },
        "location": {
            "section": "3. Results",
            "page": 6,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Forest                           −1.943***                        0.690",
        "extraction_confidence": "high",
        "extraction_notes": "From Table 1. Negative coefficient indicates forest associated with better condition"
    }
]

print(f"  Adding {len(new_evidence)} new evidence items (E022-E029)")

print("Extracting claims from Results section...")

# New CLAIMS items (C056-C063)
new_claims = [
    {
        "claim_id": "C056",
        "claim_text": "No realistic change in proximity to Kazanlak would have significant impact on mound condition despite it being regional center approximately 10 times size of next largest town",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "primary_function": "empirical_pattern",
        "claim_nature": "descriptive",
        "supported_by": ["E022"],
        "supports_claims": [],
        "quantitative_details": {
            "involves_quantification": False
        },
        "location": {
            "section": "3.1. Null results",
            "page": 6,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "As noted above (Section 2.2), simulating a change in proximity to Kazanlak indicated that no realistic increase or decrease in its size would have a signiﬁcant impact on mound condition, despite the fact that Kazanlak is the regional center and approximately 10 times the size of the next largest town.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C057",
        "claim_text": "Land conversion from forest to annual agriculture or forest to pasture produced almost no impact on mound condition",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "primary_function": "empirical_pattern",
        "claim_nature": "descriptive",
        "supported_by": ["E023", "E029"],
        "supports_claims": [],
        "quantitative_details": {
            "involves_quantification": False
        },
        "location": {
            "section": "3.1. Null results",
            "page": 6,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Simulations also produced almost no impact when land was converted from forest to annual agriculture or forest to pasture.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C058",
        "claim_text": "Transformation of all pasture to annual agriculture predicts significant deterioration of mound condition",
        "claim_type": "empirical",
        "claim_role": "core",
        "primary_function": "empirical_pattern",
        "claim_nature": "predictive",
        "supported_by": ["E024", "E028"],
        "supports_claims": ["C002", "C012", "C035"],
        "quantitative_details": {
            "involves_quantification": True,
            "metric": "probability of well-preserved mounds",
            "comparison_type": "percentage_change",
            "effect_size": "30.16% decrease"
        },
        "location": {
            "section": "3.2. Ordered logit simulation 1",
            "page": 6,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Simulating the transformation of all pasture to annual agriculture predicts a signiﬁcant deterioration of mound condition",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C059",
        "claim_text": "Pasture to annual agriculture conversion causes approximately 30.16% decrease in probability of well-preserved mounds and corresponding increase in damaged mounds",
        "claim_type": "empirical",
        "claim_role": "core",
        "primary_function": "empirical_pattern",
        "claim_nature": "predictive",
        "supported_by": ["E024"],
        "supports_claims": ["C058"],
        "quantitative_details": {
            "involves_quantification": True,
            "metric": "mean probability",
            "comparison_type": "percentage_change",
            "effect_size": "30.16%"
        },
        "declared_uncertainty": {
            "type": "approximation",
            "indicator": "approximately",
            "quantification": "ca. 30%"
        },
        "location": {
            "section": "3.2. Ordered logit simulation 1",
            "page": 6,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "the simulation predicts approximately a 30.16% decrease in the probability of mounds being well-preserved, and a corresponding increase in the probability of mounds being more damaged, should all pasture be converted to annual agriculture.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C060",
        "claim_text": "Simulated retreat of nearest town boundary by 673 m (one standard deviation) led to deterioration of burial mound condition",
        "claim_type": "empirical",
        "claim_role": "core",
        "primary_function": "empirical_pattern",
        "claim_nature": "predictive",
        "supported_by": ["E025"],
        "supports_claims": ["C003", "C013"],
        "quantitative_details": {
            "involves_quantification": True,
            "metric": "probability of well-preserved mounds",
            "comparison_type": "percentage_change",
            "effect_size": "8.59% decline"
        },
        "location": {
            "section": "3.3. Ordered logit simulation 2",
            "page": 6,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Simulated retreat of the nearest town boundary by 673 m (one standard deviation) also led to the deterioration of burial mound condition.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C061",
        "claim_text": "Urban boundary retreat by 673 m causes 8.59% decline in mean probability of well-preserved mounds with corresponding increase in damaged mounds as remoteness increases",
        "claim_type": "empirical",
        "claim_role": "core",
        "primary_function": "empirical_pattern",
        "claim_nature": "predictive",
        "supported_by": ["E025"],
        "supports_claims": ["C060"],
        "quantitative_details": {
            "involves_quantification": True,
            "metric": "mean probability",
            "comparison_type": "percentage_change",
            "effect_size": "8.59%"
        },
        "declared_uncertainty": {
            "type": "approximation",
            "indicator": "ca.",
            "quantification": "ca. 9%"
        },
        "location": {
            "section": "3.3. Ordered logit simulation 2",
            "page": 6,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "the simulation predicts an 8.59% decline in mean probability of well-preserved mounds, accompanied by a corresponding net increase in more damaged mounds (Table 3), as remoteness increases.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C062",
        "claim_text": "Mounds at higher elevations are more likely to be very damaged (for every 1 m elevation increase, odds of Category 5 condition are 1.003 times greater)",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "primary_function": "empirical_pattern",
        "claim_nature": "correlational",
        "supported_by": ["E026"],
        "supports_claims": [],
        "quantitative_details": {
            "involves_quantification": True,
            "metric": "odds ratio",
            "statistical_test": "ordered logit",
            "effect_size": "1.003"
        },
        "declared_uncertainty": {
            "type": "statistical",
            "quantification": "P<0.1"
        },
        "location": {
            "section": "3.4. Height and elevation",
            "page": 6,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "In other words, mounds at higher elevations are more likely to be very damaged",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C063",
        "claim_text": "Larger mounds are less likely to be very damaged (for every 1 m height increase, odds of Category 5 condition are 0.930 times as much)",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "primary_function": "empirical_pattern",
        "claim_nature": "correlational",
        "supported_by": ["E027"],
        "supports_claims": [],
        "quantitative_details": {
            "involves_quantification": True,
            "metric": "odds ratio",
            "statistical_test": "ordered logit",
            "effect_size": "0.930"
        },
        "declared_uncertainty": {
            "type": "statistical",
            "quantification": "P<0.1"
        },
        "location": {
            "section": "3.4. Height and elevation",
            "page": 6,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "while larger mounds are less likely to be so",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C064",
        "claim_text": "Magnitude of elevation and height effects is relatively small but accumulates over observed mound height and elevation ranges",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "primary_function": "comparative_assessment",
        "claim_nature": "evaluative",
        "supported_by": [],
        "supports_claims": ["C062", "C063"],
        "location": {
            "section": "3.4. Height and elevation",
            "page": 7,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "The magnitude of these effects is relatively small, but they accumulate over observed mound height and elevation ranges",
        "extraction_confidence": "high"
    }
]

print(f"  Adding {len(new_claims)} new claims (C056-C064)")

# Append new items to existing arrays
data["evidence"].extend(new_evidence)
data["claims"].extend(new_claims)

# Update extraction notes
data["extraction_notes"]["sections_extracted"].append(
    "Pass 1 section 4: Results (section 3, 3.1-3.4, pages 6-7)"
)

# Update timestamp
data["extraction_timestamp"] = datetime.now(timezone.utc).isoformat()

# Save updated extraction
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print(f"\n✓ Section 4 extraction complete")
print(f"  - {len(new_evidence)} new evidence items (E022-E029)")
print(f"  - {len(new_claims)} new claims (C056-C064)")
print(f"  - 0 new implicit arguments")
print(f"✓ Updated extraction.json")
