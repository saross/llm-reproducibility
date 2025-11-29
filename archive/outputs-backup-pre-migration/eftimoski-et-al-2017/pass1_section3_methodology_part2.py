#!/usr/bin/env python3
"""
Pass 1 Section 3: Extract claims from Methodology chunk 2 (section 2.3 continued)

Focus on remaining methodological choices and simulation approach (pages 5-6).
Liberal extraction philosophy: When uncertain, include it.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Load current extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

print("Extracting claims from Methodology chunk 2 (section 2.3 continued)...")

# New CLAIMS items (C048-C055)
new_claims = [
    {
        "claim_id": "C048",
        "claim_text": "Output of logit model respects discrete nature of response variable, avoiding need to interpret non-integer results",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "primary_function": "methodological_justification",
        "claim_nature": "evaluative",
        "supported_by": [],
        "supports_claims": ["C043"],
        "implicit_assumptions": [],
        "location": {
            "section": "2.3. Statistical method",
            "page": 5,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "The output of a logit model respects the discrete nature of the response variable, avoiding the need to interpret non-integer results.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C049",
        "claim_text": "Choice required between logit and probit, and between multinomial and ordered models",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "primary_function": "methodological_justification",
        "claim_nature": "descriptive",
        "supported_by": [],
        "supports_claims": ["C042"],
        "implicit_assumptions": [],
        "location": {
            "section": "2.3. Statistical method",
            "page": 6,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Once we had decided that we needed a model that would respect categorical variables, we had to choose between logit and probit, and between multinomial and ordered models.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C050",
        "claim_text": "Logit chosen over probit because results were similar and former is computationally simpler (does not require specifying standard normal distribution function)",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "primary_function": "methodological_justification",
        "claim_nature": "comparative",
        "supported_by": [],
        "supports_claims": ["C042"],
        "implicit_assumptions": [],
        "location": {
            "section": "2.3. Statistical method",
            "page": 6,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "We chose logit over probit because results were similar and the former is computationally simpler, since it does not require specifying a standard normal distribution function.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C051",
        "claim_text": "Ordered model chosen over multinomial logit to retain information about ordering in categorical variable",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "primary_function": "methodological_justification",
        "claim_nature": "evaluative",
        "supported_by": [],
        "supports_claims": ["C042"],
        "implicit_assumptions": [],
        "location": {
            "section": "2.3. Statistical method",
            "page": 6,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Next, we chose ordered over multinomial logit to retain the information about ordering in our categorical variable.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C052",
        "claim_text": "Model established relationship between current condition and circumstances of mounds, then simulations extrapolated to probable condition under new circumstances",
        "claim_type": "methodological_argument",
        "claim_role": "core",
        "primary_function": "methodological_justification",
        "claim_nature": "descriptive",
        "supported_by": [],
        "supports_claims": ["C039"],
        "implicit_assumptions": ["IA002"],
        "location": {
            "section": "2.3. Statistical method",
            "page": 6,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "This model established the relationship between the current condition and circumstances of the mounds. Then we ran the simulations described in Section 2, extrapolating from the existing relationships between condition and circumstances to probable mound condition under new circumstances.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C053",
        "claim_text": "Graphical representation chosen over typical logit outputs (coefficients and odds ratios) because latter are difficult to explain and interpret",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "primary_function": "methodological_justification",
        "claim_nature": "evaluative",
        "supported_by": [],
        "supports_claims": [],
        "implicit_assumptions": [],
        "location": {
            "section": "2.3. Statistical method",
            "page": 6,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "Since the typical outputs of logit models (coefﬁcients and odds ratios) are difﬁcult to explain and interpret, we chose to represent the changes graphically",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C054",
        "claim_text": "Visible shifts in probability density functions indicate how changing circumstances affect mound vulnerability",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "primary_function": "methodological_justification",
        "claim_nature": "descriptive",
        "supported_by": [],
        "supports_claims": ["C053"],
        "implicit_assumptions": [],
        "location": {
            "section": "2.3. Statistical method",
            "page": 6,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "for each simulation, visible shifts in the probability density functions indicate how changing circumstances affect mound vulnerability.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C055",
        "claim_text": "Squared distance included in model to capture any nonlinear effects of distance (none were indicated)",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "primary_function": "methodological_justification",
        "claim_nature": "descriptive",
        "supported_by": [],
        "supports_claims": [],
        "expected_information_missing": ["Justification for why nonlinear effects were anticipated"],
        "location": {
            "section": "2.2. Variables",
            "page": 5,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "The squared distance was included in the model to capture any nonlinear effects of distance (none were indicated).",
        "extraction_confidence": "high"
    }
]

print(f"  Adding {len(new_claims)} new claims (C048-C055)")

# Append new items to existing arrays
data["claims"].extend(new_claims)

# Update extraction notes
data["extraction_notes"]["sections_extracted"].append(
    "Pass 1 section 3: Methodology chunk 2 (section 2.3 continued, pages 5-6)"
)

# Update timestamp
data["extraction_timestamp"] = datetime.now(timezone.utc).isoformat()

# Save updated extraction
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print(f"\n✓ Section 3 extraction complete")
print(f"  - 0 new evidence items")
print(f"  - {len(new_claims)} new claims (C048-C055)")
print(f"  - 0 new implicit arguments")
print(f"✓ Updated extraction.json")
