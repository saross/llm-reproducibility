#!/usr/bin/env python3
"""
Pass 4 Implicit RDMAP Extraction
Paper: Sobotkova et al. 2024 - Validating predictions of burial mounds

Extract RDMAP items that are mentioned but not documented.
Pattern recognition: procedures referenced but not described.
"""

import json
from pathlib import Path

extraction_file = Path("/home/shawn/Code/llm-reproducibility/outputs/sobotkova-et-al-2024/extraction.json")
with open(extraction_file, 'r') as f:
    extraction = json.load(f)

# Implicit RDMAP items - mentioned but undocumented procedures
implicit_protocols = [
    {
        "protocol_id": "P010",
        "protocol_text": "Preliminary experimentation procedure for comparing pre-trained model performance",
        "protocol_status": "implicit",
        "trigger_text": [
            "After some preliminary experimentation with a range of different pre-trained models, we concluded that ResNet-50 seemed to perform best for our data."
        ],
        "trigger_locations": [
            {"section": "Methods", "subsection": "Transfer learning", "paragraph": 4}
        ],
        "inference_reasoning": "Paper mentions 'preliminary experimentation' and 'range of different pre-trained models' but provides no procedural details about how models were compared, what performance metrics were used, how many models were tested, or what constituted 'best' performance. This experimentation clearly occurred but the selection methodology is undocumented.",
        "location": {"section": "Methods", "subsection": "Transfer learning", "paragraph": 4},
        "linked_methods": ["M001"],
        "linked_evidence": [],
        "execution_context": {"models_tested": "Multiple (unspecified)", "comparison_basis": "Performance (unspecified metrics)"},
        "implicit_metadata": {
            "basis_for_inference": "Procedure mentioned but not described",
            "expected_information_missing": ["Models tested", "Performance metrics used", "Test dataset", "Comparison criteria"],
            "assessment_implication": "Cannot assess appropriateness of model selection or reproduce selection process. Critical for reproducibility."
        }
    },
    {
        "protocol_id": "P011",
        "protocol_text": "Image augmentation procedures applied to training data",
        "protocol_status": "implicit",
        "trigger_text": [
            "After image augmentation, the model reported good learning and model fit (F1 5 0.87)."
        ],
        "trigger_locations": [
            {"section": "Results", "subsection": "First run (2021)", "paragraph": 1}
        ],
        "inference_reasoning": "Results section confirms 'image augmentation' was performed before model training, but no description of augmentation techniques, parameters, or rationale appears in Methods. Common techniques include rotation, flipping, scaling, but paper doesn't specify which were used or why.",
        "location": {"section": "Results", "subsection": "First run (2021)", "paragraph": 1},
        "linked_methods": ["M004"],
        "linked_evidence": [],
        "execution_context": {"augmentation_applied": "Yes (techniques unspecified)"},
        "implicit_metadata": {
            "basis_for_inference": "Procedure mentioned in Results but not described in Methods",
            "expected_information_missing": ["Augmentation techniques", "Augmentation factor", "Parameter ranges", "Rationale"],
            "assessment_implication": "Cannot assess whether augmentation appropriate for satellite imagery or evaluate potential artifacts. Critical for reproducibility and bias assessment."
        }
    },
    {
        "protocol_id": "P012",
        "protocol_text": "Manual time estimation procedure for cost-benefit analysis",
        "protocol_status": "implicit",
        "trigger_text": [
            "with an experienced operator able to make an assessment in ~30 s"
        ],
        "trigger_locations": [
            {"section": "Discussion", "subsection": "Is it worth it?", "paragraph": 2}
        ],
        "inference_reasoning": "Paper provides specific time estimate (30 seconds per tile) for manual processing but doesn't describe how this estimate was derived. Was it measured empirically? Estimated from experience? Averaged across operators? The precision of cost-benefit comparison depends on validity of this estimate, but estimation methodology is undocumented.",
        "location": {"section": "Discussion", "subsection": "Is it worth it?", "paragraph": 2},
        "linked_methods": [],
        "linked_evidence": [],
        "execution_context": {"operator_experience": "Experienced (unspecified criteria)", "timing_basis": "Estimate (methodology undocumented)"},
        "implicit_metadata": {
            "basis_for_inference": "Specific timing value provided without methodology",
            "expected_information_missing": ["Timing measurement protocol", "Sample size", "Operator variability", "Empirical vs estimated"],
            "assessment_implication": "Cost-benefit conclusion depends on accuracy of this estimate. Without methodology, cannot assess reliability or variability. Affects validity of efficiency claims."
        }
    }
]

# Add implicit RDMAP items
extraction["protocols"].extend(implicit_protocols)

# Update extraction notes
extraction["extraction_metadata"]["extraction_notes"].append({
    "pass4_implicit_rdmap": {
        "pass_date": "2025-10-30",
        "items_extracted": {
            "implicit_protocols": len(implicit_protocols),
            "implicit_methods": 0,
            "implicit_designs": 0,
            "total": len(implicit_protocols)
        },
        "implicit_percentage": f"{len(implicit_protocols) / (20 + len(implicit_protocols)) * 100:.1f}%",
        "notes": "Systematic scan for mentioned-but-undocumented procedures. Found 3 implicit protocols: model selection experimentation (P010), image augmentation (P011), and manual timing estimation (P012). No implicit methods or designs identified - all strategic and tactical approaches were explicitly documented. Implicit rate of 13.0% (3/23 total RDMAP) is within expected range."
    }
})

# Save
with open(extraction_file, 'w') as f:
    json.dump(extraction, f, indent=2, ensure_ascii=False)

print(f"✓ Pass 4 implicit RDMAP extraction complete")
print(f"  Implicit Protocols: {len(implicit_protocols)} items")
print(f"  Total RDMAP: {20 + len(implicit_protocols)} items")
print(f"  Implicit percentage: {len(implicit_protocols) / (20 + len(implicit_protocols)) * 100:.1f}%")
print()
print(f"Running total: {77 + 20 + len(implicit_protocols)} items")
print(f"  (77 claims/evidence + {20 + len(implicit_protocols)} RDMAP)")
