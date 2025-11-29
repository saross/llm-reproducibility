#!/usr/bin/env python3
"""
Pass 4: Extract implicit RDMAP items

Look for methods/protocols that are:
- Mentioned but not documented (pattern 1)
- Implied by results/tools (patterns 2-3)
- Assumed as disciplinary practice (pattern 4)
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Load current extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

print("Pass 4: Implicit RDMAP Extraction Starting...")
print(f"Current RDMAP: {len(data['research_designs'])} designs, {len(data['methods'])} methods, {len(data['protocols'])} protocols")

# Pattern 1 (mentioned undocumented) implicit RDMAP items identified:

implicit_protocols = [
    {
        "protocol_id": "IP001",
        "protocol_name": "Personnel training procedure",
        "protocol_description": "Training procedure for personnel to ensure consistent, standardised recording of mound GPS locations, dimensions, land-use, and condition during survey",
        "protocol_type": "training",
        "method_context": ["M002"],
        "implements_methods": ["M002"],
        "sourcing_status": "implicit",
        "implicit_basis": "mentioned_undocumented",
        "trigger_text": [
            "GPS location, dimensions, surrounding land-use, and condition of 773 burial mounds were collected by trained personnel using standardised record sheets"
        ],
        "trigger_locations": [
            {
                "section": "2.1. Dataset",
                "page": 3,
                "start_paragraph": 1,
                "end_paragraph": 1
            }
        ],
        "inference_reasoning": "Paper states personnel were 'trained' and used 'standardised record sheets', implying existence of training procedures to ensure consistency in mound recording, but no details provided about training content, duration, or quality control methods.",
        "expected_information_missing": [
            "Training duration and content",
            "Training materials or manual",
            "Quality control or inter-rater reliability checks",
            "Criteria for personnel selection"
        ],
        "reconstruction_confidence": "medium",
        "location": {
            "section": "2.1. Dataset",
            "page": 3,
            "start_paragraph": 1,
            "end_paragraph": 1
        }
    },
    {
        "protocol_id": "IP002",
        "protocol_name": "Land-use classification criteria",
        "protocol_description": "Criteria and decision rules for classifying land-use around mounds into categories (pasture, forest, annual agriculture, perennial agriculture, beach, scrub, urban)",
        "protocol_type": "classification",
        "method_context": ["M002"],
        "implements_methods": ["M002"],
        "sourcing_status": "implicit",
        "implicit_basis": "mentioned_undocumented",
        "trigger_text": [
            "'Land-use' represents how land was used around the mound at the time of survey with categorical values of pasture, forest, annual agriculture (arable land), perennial agriculture, beach, scrub, and urban"
        ],
        "trigger_locations": [
            {
                "section": "2.2. Variables",
                "page": 3,
                "start_paragraph": 3,
                "end_paragraph": 3
            }
        ],
        "inference_reasoning": "Paper defines land-use categories but does not specify classification criteria (e.g., how to distinguish pasture from scrub, what qualifies as 'annual agriculture', spatial extent considered 'around the mound'). Such criteria necessary for consistent classification across 773 mounds and multiple surveyors.",
        "expected_information_missing": [
            "Spatial extent definition (how far 'around the mound')",
            "Decision rules for boundary cases",
            "Criteria distinguishing similar categories (pasture vs scrub)",
            "Temporal considerations (land-use at which time of year)"
        ],
        "reconstruction_confidence": "low",
        "location": {
            "section": "2.2. Variables",
            "page": 3,
            "start_paragraph": 3,
            "end_paragraph": 3
        }
    },
    {
        "protocol_id": "IP003",
        "protocol_name": "Condition assessment procedure",
        "protocol_description": "Visual inspection procedure and criteria for assessing mound condition on Likert scale 1-5, informed by Wildesen's (1982) 'effect' concept, collapsing impacts from multiple damage types into single categorical assessment",
        "protocol_type": "assessment",
        "method_context": ["M002"],
        "implements_methods": ["M002"],
        "sourcing_status": "implicit",
        "implicit_basis": "mentioned_undocumented",
        "trigger_text": [
            "Mound condition, our response variable, is based on subjective observation of burial mound condition at the time of survey. This variable was informed by Wildesen's (1982, 54) concept of 'effect', which denotes professional judgement about a measurable characteristic relating to the archaeological value of the site.",
            "We recorded condition on Likert scale from 1 (intact) to 5 (extinct), producing a categorical variable. Category 1 mounds might have slight damage, but their archaeological value had not been compromised. Categories 2–4 represented increasingly signiﬁcant damage."
        ],
        "trigger_locations": [
            {
                "section": "2.2. Variables",
                "page": 4,
                "start_paragraph": 5,
                "end_paragraph": 5
            }
        ],
        "inference_reasoning": "Paper describes condition as 'subjective observation' informed by professional judgment but provides only brief category descriptions. Specific assessment criteria, diagnostic features, or decision rules for assigning 1-5 ratings not documented, though such criteria necessary for consistent assessment across 773 mounds.",
        "expected_information_missing": [
            "Specific diagnostic features for each category (2, 3, 4)",
            "Assessment procedure (what aspects examined, in what order)",
            "Decision rules for boundary cases between categories",
            "Inter-rater reliability measures or calibration procedures"
        ],
        "reconstruction_confidence": "low",
        "location": {
            "section": "2.2. Variables",
            "page": 4,
            "start_paragraph": 5,
            "end_paragraph": 5
        }
    }
]

print(f"\nIdentified {len(implicit_protocols)} implicit protocols (pattern 1: mentioned undocumented)")
for ip in implicit_protocols:
    print(f"  - {ip['protocol_id']}: {ip['protocol_name']}")

# Add to extraction
data["protocols"].extend(implicit_protocols)

# Update extraction notes
data["extraction_notes"]["rdmap_sections_extracted"].append(
    "Pass 4: Implicit RDMAP (3 protocols identified)"
)

# Update timestamp
data["extraction_timestamp"] = datetime.now(timezone.utc).isoformat()

# Save updated extraction
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print("\n✓ Pass 4 implicit RDMAP extraction complete")
print(f"  - Total protocols: {len(data['protocols'])} (7 explicit + 3 implicit)")
print(f"  - Total RDMAP: {len(data['research_designs']) + len(data['methods']) + len(data['protocols'])} items")
print("✓ Saved to extraction.json")
