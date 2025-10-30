#!/usr/bin/env python3
"""
Pass 1 Section 5: Extract claims from Discussion chunk 1 (sections 4, 4.1, 4.2, pages 7-9)

Focus on interpretations, explanations, and wider significance claims.
Liberal extraction philosophy: When uncertain, include it.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Load current extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

print("Extracting evidence from Discussion chunk 1...")

# New EVIDENCE items (E030-E032)
new_evidence = [
    {
        "evidence_id": "E030",
        "evidence_text": "All cities, towns, and villages within 5 km of burial mounds experienced total population decline of 14,931 people (15.9%) between 1994 and 2011, with only one town not experiencing depopulation",
        "evidence_type": "demographic_data",
        "evidence_basis": "statistical_output",
        "supports_claims": ["C065", "C066"],
        "location": {
            "section": "4.1. Burial mound vulnerability in the Kazanlak Valley",
            "page": 8,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "All towns but one experience depopulation, with a total decline of 14,931 people, or 15.9%",
        "extraction_confidence": "high",
        "extraction_notes": "Cited from Figure 9 caption"
    },
    {
        "evidence_id": "E031",
        "evidence_text": "Stara Zagora province projected to experience ca. 33% depopulation between 2011 and 2070",
        "evidence_type": "demographic_projection",
        "evidence_basis": "statistical_output",
        "supports_claims": ["C066"],
        "declared_uncertainty": {
            "type": "approximation",
            "indicator": "ca.",
            "quantification": "ca. 33%"
        },
        "location": {
            "section": "4.1. Burial mound vulnerability in the Kazanlak Valley",
            "page": 8,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "A meaningful increase in distance to the nearest urban boundary is plausible under the projected ca. 33% depopulation of Stara Zagora province between 2011 and 2070 (Fig. 10).",
        "extraction_confidence": "high"
    },
    {
        "evidence_id": "E032",
        "evidence_text": "Preliminary logit regression indicates remoteness increases probability of mound being robbed",
        "evidence_type": "analytical_result",
        "evidence_basis": "statistical_output",
        "supports_claims": ["C069"],
        "location": {
            "section": "4.1. Burial mound vulnerability in the Kazanlak Valley",
            "page": 8,
            "start_paragraph": 3,
            "end_paragraph": 3
        },
        "verbatim_quote": "A preliminary logit regression indicates that remoteness increases the probability of a mound being robbed",
        "extraction_confidence": "medium",
        "extraction_notes": "Data about robbing are coarse (binary robbed/unrobbed without severity indication)"
    }
]

print(f"  Adding {len(new_evidence)} new evidence items (E030-E032)")

print("Extracting claims from Discussion chunk 1...")

# New CLAIMS items (C065-C087)
new_claims = [
    {
        "claim_id": "C065",
        "claim_text": "Converting all pasture of Kazanlak Valley to annual agriculture would produce 30% shift in mean probability from well-preserved to more damaged mounds",
        "claim_type": "interpretation",
        "claim_role": "core",
        "primary_function": "empirical_pattern",
        "claim_nature": "predictive",
        "supported_by": ["E024"],
        "supports_claims": ["C002", "C058", "C059"],
        "location": {
            "section": "4.1. Burial mound vulnerability in the Kazanlak Valley",
            "page": 8,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Converting all the pasture of the Kazanlak Valley to annual agriculture would produce a 30% shift in mean probability from well-preserved (Condition 1–2) to more damaged (Condition 3–5) mounds.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C066",
        "claim_text": "Meaningful increase in distance to nearest urban boundary is plausible under projected ca. 33% depopulation of Stara Zagora province between 2011-2070",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "primary_function": "empirical_pattern",
        "claim_nature": "predictive",
        "supported_by": ["E030", "E031"],
        "supports_claims": [],
        "location": {
            "section": "4.1. Burial mound vulnerability in the Kazanlak Valley",
            "page": 8,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "A meaningful increase in distance to the nearest urban boundary is plausible under the projected ca. 33% depopulation of Stara Zagora province between 2011 and 2070 (Fig. 10).",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C067",
        "claim_text": "Relatively small-scale reallocation of land from pasture to annual agriculture endangers many mounds, especially since mounds are concentrated in pasture",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "primary_function": "causal_explanation",
        "claim_nature": "causal",
        "supported_by": ["E014", "E024"],
        "supports_claims": [],
        "location": {
            "section": "4.1. Burial mound vulnerability in the Kazanlak Valley",
            "page": 8,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "With an effect this large, even relatively small-scale reallocation of land from pasture to annual agriculture endangers many mounds – especially since mounds are concentrated in pasture.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C068",
        "claim_text": "Agricultural damage to mounds likely arises from aggressive ploughing, harrowing, and clearing of stones",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "primary_function": "mechanism_proposal",
        "claim_nature": "causal",
        "supported_by": [],
        "supports_claims": ["C004", "C034"],
        "location": {
            "section": "4.1. Burial mound vulnerability in the Kazanlak Valley",
            "page": 8,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "This damage likely arises from aggressive ploughing, harrowing, and clearing of stones (mound mantles often contain ﬁeld stones, which make stony piles once the sod is removed and erosion carries away exposed soil; these piles are sometimes then removed to the edges of ﬁelds).",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C069",
        "claim_text": "Remote mounds may be more vulnerable to deterioration because fewer witnesses live nearby to report destructive looting or agricultural damage",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "primary_function": "mechanism_proposal",
        "claim_nature": "causal",
        "supported_by": ["E032"],
        "supports_claims": ["C005", "C060", "C061"],
        "expected_information_missing": ["Independent data about agricultural damage for similar analysis"],
        "location": {
            "section": "4.1. Burial mound vulnerability in the Kazanlak Valley",
            "page": 8,
            "start_paragraph": 3,
            "end_paragraph": 3
        },
        "verbatim_quote": "Remote mounds may be more vulnerable to deterioration because fewer witnesses live nearby to report destructive looting or agricultural damage, although further investigation is necessary to establish causality.",
        "extraction_confidence": "medium"
    },
    {
        "claim_id": "C070",
        "claim_text": "Dangers to remote mounds from looting and agriculture appear to outweigh threats from peri-urban development",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "primary_function": "comparative_assessment",
        "claim_nature": "comparative",
        "supported_by": [],
        "supports_claims": ["C014"],
        "location": {
            "section": "4.1. Burial mound vulnerability in the Kazanlak Valley",
            "page": 8,
            "start_paragraph": 3,
            "end_paragraph": 3
        },
        "verbatim_quote": "Provisionally, the dangers posed to remote mounds by looting and agriculture appear to outweigh threats from peri-urban development",
        "extraction_confidence": "medium"
    },
    {
        "claim_id": "C071",
        "claim_text": "Burial mounds may be recognised by community as valuable part of local cultural heritage that promotes social cohesion, cultural awareness, and economic growth through tourist income",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "primary_function": "mechanism_proposal",
        "claim_nature": "causal",
        "supported_by": [],
        "supports_claims": ["C070"],
        "location": {
            "section": "4.1. Burial mound vulnerability in the Kazanlak Valley",
            "page": 8,
            "start_paragraph": 3,
            "end_paragraph": 3
        },
        "verbatim_quote": "perhaps because the burial mounds are recognised by the community as a valuable part of local cultural heritage that promotes social cohesion, cultural awareness, and economic growth through tourist income",
        "extraction_confidence": "medium"
    },
    {
        "claim_id": "C072",
        "claim_text": "Urban and peri-urban development is often recognised as threat to archaeological heritage",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "primary_function": "empirical_pattern",
        "claim_nature": "descriptive",
        "supported_by": [],
        "supports_claims": [],
        "location": {
            "section": "4.1. Burial mound vulnerability in the Kazanlak Valley",
            "page": 8,
            "start_paragraph": 4,
            "end_paragraph": 4
        },
        "verbatim_quote": "Urban and peri-urban development is often recognised as a threat to archaeological heritage",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C073",
        "claim_text": "Depopulation, village abandonment, and urban retreat can also threaten heritage (contrasting with typical focus on sprawl)",
        "claim_type": "interpretation",
        "claim_role": "core",
        "primary_function": "theoretical_interpretation",
        "claim_nature": "evaluative",
        "supported_by": ["E025", "E030", "E031"],
        "supports_claims": ["C010", "C014"],
        "location": {
            "section": "4.1. Burial mound vulnerability in the Kazanlak Valley",
            "page": 8,
            "start_paragraph": 4,
            "end_paragraph": 4
        },
        "verbatim_quote": "Our results indicate, however, that depopulation, village abandonment, and urban retreat can also threaten heritage.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C074",
        "claim_text": "Larger mounds are in better condition (contrary to initial intuition)",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "primary_function": "empirical_pattern",
        "claim_nature": "descriptive",
        "supported_by": ["E027"],
        "supports_claims": ["C063"],
        "location": {
            "section": "4.1. Burial mound vulnerability in the Kazanlak Valley",
            "page": 8,
            "start_paragraph": 5,
            "end_paragraph": 5
        },
        "verbatim_quote": "Also contrary to our intuition, larger mounds are in better condition.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C075",
        "claim_text": "Taller mounds are more likely to have been robbed (confirmed by preliminary logit regression)",
        "claim_type": "empirical",
        "claim_role": "supporting",
        "primary_function": "empirical_pattern",
        "claim_nature": "correlational",
        "supported_by": [],
        "supports_claims": ["C037"],
        "location": {
            "section": "4.1. Burial mound vulnerability in the Kazanlak Valley",
            "page": 8,
            "start_paragraph": 5,
            "end_paragraph": 5
        },
        "verbatim_quote": "Although a preliminary logit regression conﬁrms that taller mounds are more likely to have been robbed",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C076",
        "claim_text": "Small mounds are easier to plough over or otherwise disassemble (intentionally or unintentionally) during agricultural work",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "primary_function": "mechanism_proposal",
        "claim_nature": "causal",
        "supported_by": [],
        "supports_claims": ["C074"],
        "location": {
            "section": "4.1. Burial mound vulnerability in the Kazanlak Valley",
            "page": 8,
            "start_paragraph": 5,
            "end_paragraph": 5
        },
        "verbatim_quote": "small mounds are, intuitively, easier to plough over or otherwise disassemble (intentionally or unintentionally) in the course of agricultural work.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C077",
        "claim_text": "Relationship between greater height and better condition indicates damage to small mounds from agriculture outweighs damage to large mounds from looting",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "primary_function": "comparative_assessment",
        "claim_nature": "comparative",
        "supported_by": ["E027"],
        "supports_claims": ["C074"],
        "location": {
            "section": "4.1. Burial mound vulnerability in the Kazanlak Valley",
            "page": 8,
            "start_paragraph": 5,
            "end_paragraph": 5
        },
        "verbatim_quote": "On balance, the relationship between greater height and better condition indicates that the damage to small mounds from agricultural activities outweighs the damage to large mounds from looting.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C078",
        "claim_text": "Correlation between elevation and mound deterioration is likely due either to increased erosion at higher elevations or to indirect relationship between elevation and other explanatory variables",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "primary_function": "mechanism_proposal",
        "claim_nature": "causal",
        "supported_by": ["E026"],
        "supports_claims": ["C062"],
        "expected_information_missing": ["Further investigation required to understand elevation-deterioration relationship"],
        "location": {
            "section": "4.1. Burial mound vulnerability in the Kazanlak Valley",
            "page": 8,
            "start_paragraph": 6,
            "end_paragraph": 6
        },
        "verbatim_quote": "The correlation between elevation and mound deterioration is likely due either to increased erosion at higher elevations, or to some indirect relationship between elevation and our other explanatory variables. Further investigation will be required to understand this relationship.",
        "extraction_confidence": "medium"
    },
    {
        "claim_id": "C079",
        "claim_text": "Heritage resources and personnel should be allocated preferentially to monitoring plough damage to mounds surrounded by annual agriculture, especially small mounds or fields converted from pasture",
        "claim_type": "interpretation",
        "claim_role": "core",
        "primary_function": "future_direction",
        "claim_nature": "evaluative",
        "supported_by": [],
        "supports_claims": ["C006"],
        "location": {
            "section": "4.1. Burial mound vulnerability in the Kazanlak Valley",
            "page": 8,
            "start_paragraph": 7,
            "end_paragraph": 7
        },
        "verbatim_quote": "heritage resources and personnel should be allocated preferentially, when possible, to monitoring plough damage to mounds surrounded by annual agriculture, especially if the mounds are small in size or are located in ﬁelds that have been converted from pasture.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C080",
        "claim_text": "Remote mounds should be monitored for looting and other damage, especially if they grow more remote as villages are abandoned or urban boundaries retreat",
        "claim_type": "interpretation",
        "claim_role": "core",
        "primary_function": "future_direction",
        "claim_nature": "evaluative",
        "supported_by": [],
        "supports_claims": ["C006"],
        "location": {
            "section": "4.1. Burial mound vulnerability in the Kazanlak Valley",
            "page": 8,
            "start_paragraph": 7,
            "end_paragraph": 7
        },
        "verbatim_quote": "Likewise, remote mounds should be monitored for looting and other damage, especially if they grow more remote as villages are abandoned or urban boundaries retreat.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C081",
        "claim_text": "Recommend collecting granular information about different types of damage on Likert scales to identify relationships between explanatory variables and specific causes of deterioration",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "primary_function": "future_direction",
        "claim_nature": "evaluative",
        "supported_by": [],
        "supports_claims": [],
        "location": {
            "section": "4.1. Burial mound vulnerability in the Kazanlak Valley",
            "page": 8,
            "start_paragraph": 7,
            "end_paragraph": 7
        },
        "verbatim_quote": "In future, we recommend collecting granular information about different types of damage to mounds (e.g., damage from looting, agriculture, etc., on Likert scales) in order to identify relationships between explanatory variables like remoteness or height and speciﬁc causes of mound deterioration like robbing or ploughing.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C082",
        "claim_text": "Burial mounds studied are representative of those found across the Balkans, making approach transferable to other parts of Bulgaria, northern Greece, European Turkey, and beyond",
        "claim_type": "methodological_argument",
        "claim_role": "core",
        "primary_function": "methodological_justification",
        "claim_nature": "evaluative",
        "supported_by": [],
        "supports_claims": ["C008"],
        "location": {
            "section": "4.2. Wider application and significance",
            "page": 9,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "The burial mounds studied are representative of those found across the Balkans, making our approach transferable to other parts of Bulgaria, northern Greece, European Turkey, and beyond.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C083",
        "claim_text": "Ordered logit is well suited for analysis of categorical response variables like condition, which are often estimated using Likert scales",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "primary_function": "methodological_justification",
        "claim_nature": "evaluative",
        "supported_by": [],
        "supports_claims": ["C042", "C043"],
        "location": {
            "section": "4.2. Wider application and significance",
            "page": 9,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "The statistical model used, an ordered logit, is well suited for analysis of categorical response variables like condition, which are often estimated using Likert scales.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C084",
        "claim_text": "Suitable data may already exist in cultural heritage registers or be obtainable using remote sensing and extensive survey techniques",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "primary_function": "methodological_justification",
        "claim_nature": "descriptive",
        "supported_by": [],
        "supports_claims": ["C082"],
        "location": {
            "section": "4.2. Wider application and significance",
            "page": 9,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "We acquired our data through systematic pedestrian survey, but suitable data may already exist in cultural heritage registers, or obtained using a variety of remote sensing and extensive survey techniques",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C085",
        "claim_text": "Model avoids need for site location modeling, simplifying application by predicting evolving vulnerability of existing monuments",
        "claim_type": "methodological_argument",
        "claim_role": "core",
        "primary_function": "methodological_justification",
        "claim_nature": "comparative",
        "supported_by": [],
        "supports_claims": ["C007"],
        "location": {
            "section": "4.2. Wider application and significance",
            "page": 9,
            "start_paragraph": 3,
            "end_paragraph": 3
        },
        "verbatim_quote": "In our model, risk to monuments is deduced from a large dataset of observations, which avoids the need for site location modeling. The simulation stands on its own to predict the evolving vulnerability of existing monuments, simplifying application.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C086",
        "claim_text": "Results problematize the perception that agricultural activities are benign",
        "claim_type": "interpretation",
        "claim_role": "core",
        "primary_function": "theoretical_interpretation",
        "claim_nature": "evaluative",
        "supported_by": [],
        "supports_claims": ["C009"],
        "location": {
            "section": "4.2. Wider application and significance",
            "page": 9,
            "start_paragraph": 4,
            "end_paragraph": 4
        },
        "verbatim_quote": "Beyond the methodological approach, our results raise two important issues. First, they problematize the perception that agricultural activities are benign",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C087",
        "claim_text": "Results highlight the threat to cultural heritage posed by depopulation, de-urbanisation, and abandonment of rural villages",
        "claim_type": "interpretation",
        "claim_role": "core",
        "primary_function": "theoretical_interpretation",
        "claim_nature": "evaluative",
        "supported_by": [],
        "supports_claims": ["C010", "C073"],
        "location": {
            "section": "4.2. Wider application and significance",
            "page": 9,
            "start_paragraph": 4,
            "end_paragraph": 4
        },
        "verbatim_quote": "Second, they highlight the threat to cultural heritage posed by depopulation, de-urbanisation, and abandonment of rural villages.",
        "extraction_confidence": "high"
    }
]

print(f"  Adding {len(new_claims)} new claims (C065-C087)")

# Append new items to existing arrays
data["evidence"].extend(new_evidence)
data["claims"].extend(new_claims)

# Update extraction notes
data["extraction_notes"]["sections_extracted"].append(
    "Pass 1 section 5: Discussion chunk 1 (sections 4, 4.1, 4.2, pages 7-9)"
)

# Update timestamp
data["extraction_timestamp"] = datetime.now(timezone.utc).isoformat()

# Save updated extraction
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print(f"\n✓ Section 5 extraction complete")
print(f"  - {len(new_evidence)} new evidence items (E030-E032)")
print(f"  - {len(new_claims)} new claims (C065-C087)")
print(f"  - 0 new implicit arguments")
print(f"✓ Updated extraction.json")
