#!/usr/bin/env python3
"""
Pass 1 Section 6: Extract claims from Discussion chunk 2 (section 4.3) + Conclusion (section 5)

Focus on limitations, methodological reflections, and concluding claims.
Liberal extraction philosophy: When uncertain, include it.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Load current extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

print("Extracting claims from Discussion chunk 2 and Conclusion...")

# New CLAIMS items (C088-C098)
new_claims = [
    {
        "claim_id": "C088",
        "claim_text": "Logit regressions require larger datasets than linear regressions due to more demanding maximum likelihood estimation algorithms",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "primary_function": "methodological_justification",
        "claim_nature": "descriptive",
        "supported_by": [],
        "supports_claims": [],
        "location": {
            "section": "4.3. Limitations: data requirements and timelessness",
            "page": 9,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Logit regressions require larger datasets than linear regressions (the maximum likelihood estimation algorithms employed in the estimation of the coefﬁcients are more demanding than least squares estimation).",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C089",
        "claim_text": "This approach requires dataset with comparatively large sample size and comparatively strong relationships between variables",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "primary_function": "methodological_justification",
        "claim_nature": "descriptive",
        "supported_by": [],
        "supports_claims": ["C088"],
        "location": {
            "section": "4.3. Limitations: data requirements and timelessness",
            "page": 9,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Our approach thus requires a dataset with a comparatively large sample size and comparatively strong relationships between the variables.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C090",
        "claim_text": "Logit regressions less demanding than probit (attempted ordered probit model failed when maximum likelihood algorithms unable to estimate coefficients)",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "primary_function": "comparative_assessment",
        "claim_nature": "comparative",
        "supported_by": [],
        "supports_claims": ["C050"],
        "location": {
            "section": "4.3. Limitations: data requirements and timelessness",
            "page": 9,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Note, however, that logit regressions are less demanding that probit; when we attempted to compare the results of an ordered probit model, the maximum likelihood algorithms were unable to successfully estimate coefﬁcients.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C091",
        "claim_text": "Successful computation of ordered logit coefficient estimates is harder than linear regression but easier than probit",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "primary_function": "comparative_assessment",
        "claim_nature": "comparative",
        "supported_by": [],
        "supports_claims": ["C088", "C090"],
        "location": {
            "section": "4.3. Limitations: data requirements and timelessness",
            "page": 9,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Successful computation of ordered logit coefﬁcient estimates is harder than linear regression, but easier than probit.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C092",
        "claim_text": "Logit simulation represents snapshot of current situation and predicts future snapshot but does not reveal time interval between snapshots",
        "claim_type": "methodological_argument",
        "claim_role": "core",
        "primary_function": "methodological_justification",
        "claim_nature": "descriptive",
        "supported_by": [],
        "supports_claims": [],
        "location": {
            "section": "4.3. Limitations: data requirements and timelessness",
            "page": 9,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "Burial mounds and other exposed archaeological heritage deteriorate over time. The logit simulation employed here represents a snapshot of the current situation, and predicts what a similar snapshot at an unspeciﬁed future date would look like should conditions change. The simulation, however, does not reveal the time interval between those snapshots.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C093",
        "claim_text": "Simulation yields probability that change in circumstances will alter mound's condition but does not estimate how long change will take or whether it will be sudden or gradual",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "primary_function": "methodological_justification",
        "claim_nature": "descriptive",
        "supported_by": [],
        "supports_claims": ["C092"],
        "location": {
            "section": "4.3. Limitations: data requirements and timelessness",
            "page": 9,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "It yields the probability that a change in circumstances will alter mound's condition, but does not estimate how long such a change will take, or indicate whether the change will be sudden or gradual.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C094",
        "claim_text": "Model provides only probability of change 'over time' without specifying timeframe",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "primary_function": "methodological_justification",
        "claim_nature": "descriptive",
        "supported_by": [],
        "supports_claims": ["C092", "C093"],
        "location": {
            "section": "4.3. Limitations: data requirements and timelessness",
            "page": 9,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        "verbatim_quote": "The model provides only the probability of change 'over time'.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C095",
        "claim_text": "Ordered logistic regression used here to assess burial mound vulnerability utilises large dataset to simulate results of changes to land use and urban boundaries",
        "claim_type": "methodological_argument",
        "claim_role": "core",
        "primary_function": "methodological_justification",
        "claim_nature": "descriptive",
        "supported_by": [],
        "supports_claims": ["C001", "C031"],
        "location": {
            "section": "5. Conclusions",
            "page": 9,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "The ordered logistic regression used here to assess the vulnerability of ancient burial mounds in the Kazanlak Valley utilises a large dataset to simulate the results of changes to land use and urban boundaries.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C096",
        "claim_text": "Conversion of pasture to arable land threatens mounds, as does urban retreat (confirmed by simulation)",
        "claim_type": "empirical",
        "claim_role": "core",
        "primary_function": "empirical_pattern",
        "claim_nature": "causal",
        "supported_by": [],
        "supports_claims": ["C002", "C003"],
        "location": {
            "section": "5. Conclusions",
            "page": 9,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "This simulation indicates that the conversion of pasture to arable land threatens mounds, as does urban retreat.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C097",
        "claim_text": "Increasing remoteness or isolation as cities shrink and villages are abandoned threatens mounds, probably because looters and farmers are freer to damage them when nobody is watching",
        "claim_type": "interpretation",
        "claim_role": "core",
        "primary_function": "causal_explanation",
        "claim_nature": "causal",
        "supported_by": [],
        "supports_claims": ["C003", "C069"],
        "location": {
            "section": "5. Conclusions",
            "page": 9,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "our results indicate that increasing remoteness or isolation as cities shrink and villages are abandoned also threaten mounds, probably because looters and farmers are freer to damage them when nobody is watching.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C098",
        "claim_text": "Approach quantifies probabilities of mound condition deteriorating, providing guidance for allocation of heritage resources and personnel, and can be generalised to assess likely impact of threats to sites and monuments quickly and continuously",
        "claim_type": "methodological_argument",
        "claim_role": "core",
        "primary_function": "methodological_justification",
        "claim_nature": "evaluative",
        "supported_by": [],
        "supports_claims": ["C006", "C007", "C008"],
        "location": {
            "section": "5. Conclusions",
            "page": 9,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Our approach quantiﬁes the probabilities of mound condition deteriorating on account of these threats, providing guidance for the allocation of heritage resources and personnel. It can also be generalised to assess the likely impact of threats to sites and monuments quickly and continuously.",
        "extraction_confidence": "high"
    },
    {
        "claim_id": "C099",
        "claim_text": "Since model extrapolates from current situation, it requires large dataset but does not rely upon predicting undiscovered site locations, prior knowledge of specific hazards, or forecasts of future development",
        "claim_type": "methodological_argument",
        "claim_role": "core",
        "primary_function": "methodological_justification",
        "claim_nature": "comparative",
        "supported_by": [],
        "supports_claims": ["C007", "C085"],
        "location": {
            "section": "5. Conclusions",
            "page": 9,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        "verbatim_quote": "Since the model extrapolates from the current situation, it requires a large dataset, but does not rely upon predicting undiscovered site locations, prior knowledge of speciﬁc hazards, or forecasts of future development.",
        "extraction_confidence": "high"
    }
]

print(f"  Adding {len(new_claims)} new claims (C088-C099)")

# Append new items to existing arrays
data["claims"].extend(new_claims)

# Update extraction notes
data["extraction_notes"]["sections_extracted"].append(
    "Pass 1 section 6: Discussion chunk 2 + Conclusion (sections 4.3, 5, page 9)"
)

# Mark claims/evidence extraction as complete
data["extraction_notes"]["claims_evidence_extraction_complete"] = True

# Update timestamp
data["extraction_timestamp"] = datetime.now(timezone.utc).isoformat()

# Save updated extraction
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print(f"\n✓ Section 6 extraction complete")
print(f"  - 0 new evidence items")
print(f"  - {len(new_claims)} new claims (C088-C099)")
print(f"  - 0 new implicit arguments")
print(f"\n✓✓✓ PASS 1 COMPLETE ✓✓✓")
print(f"Total extraction: 32 evidence, 99 claims, 8 implicit arguments")
print(f"✓ Updated extraction.json")
