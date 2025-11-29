#!/usr/bin/env python3
"""
Pass 3 Liberal RDMAP Extraction
Paper: Sobotkova et al. 2024 - Validating predictions of burial mounds

CRITICAL: Equal attention to ALL sections
- Research Designs often in Introduction, Discussion, Conclusion
- Methods in Methods section
- Protocols in Methods and Results sections

Liberal extraction: When uncertain, INCLUDE IT
"""

import json
from pathlib import Path

extraction_file = Path("/home/shawn/Code/llm-reproducibility/outputs/sobotkova-et-al-2024/extraction.json")
with open(extraction_file, 'r') as f:
    extraction = json.load(f)

# Research Designs (WHY) - Strategic decisions about framing
research_designs = [
    {
        "design_id": "RD001",
        "design_text": "External validation design comparing ML model predictions against comprehensive field survey data",
        "design_status": "explicit",
        "verbatim_quote": "In this study we used a dataset of 773 mounds, collected by TRAP during 2009 – 2011 field survey in the Kazanlak Valley, Bulgaria, to validate the performance of a pre-trained CNN",
        "location": {"section": "Data", "subsection": "Pedestrian survey", "paragraph": 1},
        "design_rationale": "Field data serves as ground truth for assessing ML detection accuracy",
        "alternative_designs_considered": [],
        "linked_methods": ["M001", "M002", "M003", "M006"],
        "expected_information_missing": ["Why Kazanlak Valley chosen", "Sample size justification"]
    },
    {
        "design_id": "RD002",
        "design_text": "Comparative two-run design testing impact of training data curation on model performance",
        "design_status": "explicit",
        "verbatim_quote": "In the 2021 run of the model, we used all 773 cutouts for training regardless of what was visible in the satellite image. In the 2022 run, we selected 249 cutouts where a mound was discernible with the naked eye.",
        "location": {"section": "Methods", "subsection": "Additional CNN training", "paragraph": 1},
        "design_rationale": "Test hypothesis that curated training data (visible mounds only) improves model performance",
        "alternative_designs_considered": [],
        "linked_methods": ["M002"],
        "expected_information_missing": ["Hypothesis stated explicitly", "Statistical test design"]
    },
    {
        "design_id": "RD003",
        "design_text": "Negative results documentation design to counterbalance publication bias in ML-for-archaeology literature",
        "design_status": "explicit",
        "verbatim_quote": "This paper presents the failure of a good-faith attempt to utilise these approaches as a counterbalance and cautionary tale to potential adopters of the technology.",
        "location": {"section": "Abstract", "subsection": "Social implications", "paragraph": 1},
        "design_rationale": "Address identified gap in literature where negative results underreported (63% of papers mention no challenges)",
        "alternative_designs_considered": [],
        "linked_methods": [],
        "expected_information_missing": ["Peer review process for negative results", "Target audience specification"]
    },
    {
        "design_id": "RD004",
        "design_text": "Cost-benefit analysis design comparing ML development time against manual processing alternative",
        "design_status": "explicit",
        "verbatim_quote": "With approximately 5,000 150 3 150 m tiles in our 600 sq km study area, and with an experienced operator able to make an assessment in ~30 s, manual processing would have taken approximately 42 h. Meanwhile, as reported above, simply developing the model required about 135 h",
        "location": {"section": "Discussion", "subsection": "Is it worth it?", "paragraph": 2},
        "design_rationale": "Assess whether ML approach justified given resource investment compared to manual alternative",
        "alternative_designs_considered": ["Crowdsourcing approach mentioned"],
        "linked_methods": ["M001", "M002"],
        "expected_information_missing": ["Manual processing accuracy rates", "Cost of false negatives not quantified"]
    }
]

# Methods (WHAT) - Analytical approaches
methods = [
    {
        "method_id": "M001",
        "method_text": "Transfer learning using pre-trained ResNet-50 convolutional neural network",
        "method_status": "explicit",
        "verbatim_quote": "Rather than training our own model from scratch, we used a pre-trained CNN, a technique known as transfer learning. After some preliminary experimentation with a range of different pre-trained models, we concluded that ResNet-50 seemed to perform best for our data.",
        "location": {"section": "Methods", "subsection": "Transfer learning", "paragraph": 1},
        "method_category": "computational_analysis",
        "linked_protocols": ["P001", "P002", "P003"],
        "linked_designs": ["RD001", "RD004"],
        "expected_information_missing": ["Criteria for 'best performance'", "Other models tested", "Pre-training dataset characteristics"]
    },
    {
        "method_id": "M002",
        "method_text": "Additional CNN training using domain-specific burial mound imagery",
        "method_status": "explicit",
        "verbatim_quote": "Although pre-trained models have already been exposed to millions of images and have developed weights that respond to low-level features, they still need to be trained with domain-specific data.",
        "location": {"section": "Methods", "subsection": "Transfer learning", "paragraph": 3},
        "method_category": "computational_analysis",
        "linked_protocols": ["P002", "P003", "P004"],
        "linked_designs": ["RD001", "RD002", "RD004"],
        "expected_information_missing": ["Training hyperparameters", "Stopping criteria", "Overfitting prevention strategy"]
    },
    {
        "method_id": "M003",
        "method_text": "Binary classification approach distinguishing tiles containing mounds from tiles without mounds",
        "method_status": "explicit",
        "verbatim_quote": "The CNN was trained to identify 150 3 150 m tiles that contained mounds (MOUND) and those that did not (NO MOUND).",
        "location": {"section": "Methods", "subsection": "Additional CNN training", "paragraph": 1},
        "method_category": "computational_analysis",
        "linked_protocols": ["P004", "P005"],
        "linked_designs": ["RD001"],
        "expected_information_missing": ["Decision threshold selection", "Multi-mound tile handling strategy"]
    },
    {
        "method_id": "M004",
        "method_text": "Image augmentation to expand training dataset",
        "method_status": "explicit",
        "verbatim_quote": "After image augmentation, the model reported good learning and model fit",
        "location": {"section": "Results", "subsection": "First run (2021)", "paragraph": 1},
        "method_category": "data_preparation",
        "linked_protocols": [],
        "linked_designs": ["RD001"],
        "expected_information_missing": ["Augmentation techniques used", "Augmentation factor", "Rationale for augmentation strategy"]
    },
    {
        "method_id": "M005",
        "method_text": "Automated model performance evaluation using held-out test set",
        "method_status": "explicit",
        "verbatim_quote": "After processing, cutouts were divided into training, validation, and test sets following a 70:20:10 ratio for automated performance validation.",
        "location": {"section": "Methods", "subsection": "Additional CNN training", "paragraph": 1},
        "method_category": "validation",
        "linked_protocols": ["P008"],
        "linked_designs": ["RD001"],
        "expected_information_missing": ["Metrics used beyond F1", "Stratification strategy", "Cross-validation"]
    },
    {
        "method_id": "M006",
        "method_text": "Field-based external validation comparing model predictions against surveyed ground truth",
        "method_status": "explicit",
        "verbatim_quote": "Validation of results against field data showed that self-reported success rates were misleadingly high",
        "location": {"section": "Abstract", "subsection": "Findings", "paragraph": 1},
        "method_category": "validation",
        "linked_protocols": ["P009"],
        "linked_designs": ["RD001"],
        "expected_information_missing": ["Validation protocol details", "False positive/negative classification criteria", "Inter-rater reliability"]
    },
    {
        "method_id": "M007",
        "method_text": "Probability thresholding at >60% for positive mound detection",
        "method_status": "explicit",
        "verbatim_quote": "Nevertheless, only 19 out of 148 tiles (12.8%) tagged by the model with at least a 60% chance of having a mound actually contained one",
        "location": {"section": "Results", "subsection": "First run (2021)", "paragraph": 1},
        "method_category": "computational_analysis",
        "linked_protocols": [],
        "linked_designs": ["RD001"],
        "expected_information_missing": ["Threshold selection rationale", "Threshold sensitivity analysis", "Alternative thresholds tested"]
    }
]

# Protocols (HOW) - Specific procedures
protocols = [
    {
        "protocol_id": "P001",
        "protocol_text": "ResNet-50 CNN model selection with ~25.6m trainable parameters",
        "protocol_status": "explicit",
        "verbatim_quote": "After some preliminary experimentation with a range of different pre-trained models, we concluded that ResNet-50 seemed to perform best for our data. This model is one of the smaller pre-trained CNNs available, with only around 25.6m trainable parameters",
        "location": {"section": "Methods", "subsection": "Transfer learning", "paragraph": 4},
        "linked_methods": ["M001"],
        "linked_evidence": ["E023"],
        "execution_context": {"computational_requirements": "Lower than larger models", "implementation": "Pre-trained model available"},
        "expected_information_missing": ["Hardware specifications", "Training time", "Framework/library used (TensorFlow, PyTorch?)"]
    },
    {
        "protocol_id": "P002",
        "protocol_text": "Training cutout generation: 150x150m square polygons centred on mound points, clipped from IKONOS imagery",
        "protocol_status": "explicit",
        "verbatim_quote": "Mound points taken during fieldwork were used as centroids for the generation of 150 3 150 m square polygons (150 3 150 pixels at 1 m resolution), which were clipped from the IKONOS imagery.",
        "location": {"section": "Methods", "subsection": "Additional CNN training", "paragraph": 1},
        "linked_methods": ["M001", "M002"],
        "linked_evidence": ["E024"],
        "execution_context": {"tools": "GIS software (unspecified)", "resolution": "1m IKONOS panchromatic"},
        "expected_information_missing": ["Edge case handling", "Tile overlap strategy", "GIS software/tools used"]
    },
    {
        "protocol_id": "P003",
        "protocol_text": "NO MOUND training data generation by randomly sampling tiles without known mounds",
        "protocol_status": "explicit",
        "verbatim_quote": "NO MOUND cutouts were created by randomly sampling the landscape within the TRAP survey area, at places where there were no known mounds.",
        "location": {"section": "Methods", "subsection": "Additional CNN training", "paragraph": 1},
        "linked_methods": ["M001", "M002"],
        "linked_evidence": [],
        "execution_context": {"sampling": "Random within survey area"},
        "expected_information_missing": ["Minimum distance from mounds", "Sampling density", "Seed for reproducibility"]
    },
    {
        "protocol_id": "P004",
        "protocol_text": "Training data composition: 1:2 positive to negative ratio (32%-68%)",
        "protocol_status": "explicit",
        "verbatim_quote": "The ratio of positive to negative training data was approximately 1:2 (32%–68%).",
        "location": {"section": "Methods", "subsection": "Additional CNN training", "paragraph": 1},
        "linked_methods": ["M002", "M003"],
        "linked_evidence": ["E025"],
        "execution_context": {"class_balance": "Imbalanced toward negatives"},
        "expected_information_missing": ["Rationale for 1:2 ratio", "Class weighting or resampling", "Impact on decision threshold"]
    },
    {
        "protocol_id": "P005",
        "protocol_text": "2022 run training data curation: Visual selection of 249 cutouts where mound discernible",
        "protocol_status": "explicit",
        "verbatim_quote": "In the 2022 run, we selected 249 cutouts where a mound was discernible with the naked eye.",
        "location": {"section": "Methods", "subsection": "Additional CNN training", "paragraph": 1},
        "linked_methods": ["M002"],
        "linked_evidence": ["E026"],
        "execution_context": {"selection": "Manual visual inspection", "operator": "Trained researcher (implied)"},
        "expected_information_missing": ["Inter-rater reliability", "Selection criteria documentation", "Rejected cutout characteristics"]
    },
    {
        "protocol_id": "P006",
        "protocol_text": "Training/validation/test split: 70:20:10 ratio",
        "protocol_status": "explicit",
        "verbatim_quote": "After processing, cutouts were divided into training, validation, and test sets following a 70:20:10 ratio",
        "location": {"section": "Methods", "subsection": "Additional CNN training", "paragraph": 1},
        "linked_methods": ["M005"],
        "linked_evidence": ["E027"],
        "execution_context": {"split_method": "Unspecified"},
        "expected_information_missing": ["Stratification", "Random seed", "Spatial autocorrelation handling"]
    },
    {
        "protocol_id": "P007",
        "protocol_text": "Model application to 600 sq km study area covering ~5,000 tiles",
        "protocol_status": "explicit",
        "verbatim_quote": "With approximately 5,000 150 3 150 m tiles in our 600 sq km study area",
        "location": {"section": "Discussion", "subsection": "Is it worth it?", "paragraph": 2},
        "linked_methods": ["M001"],
        "linked_evidence": [],
        "execution_context": {"scale": "Full valley coverage"},
        "expected_information_missing": ["Processing time", "Tile overlap handling", "Edge tile treatment"]
    },
    {
        "protocol_id": "P008",
        "protocol_text": "F1 score calculation for model performance assessment",
        "protocol_status": "explicit",
        "verbatim_quote": "After image augmentation, the model reported good learning and model fit (F1 5 0.87).",
        "location": {"section": "Results", "subsection": "First run (2021)", "paragraph": 1},
        "linked_methods": ["M005"],
        "linked_evidence": ["E028", "E033"],
        "execution_context": {"metric": "F1 score (harmonic mean of precision and recall)"},
        "expected_information_missing": ["Precision/recall individually", "Confusion matrix", "ROC curve"]
    },
    {
        "protocol_id": "P009",
        "protocol_text": "Field validation by manual inspection of model-tagged tiles against ground truth mound locations",
        "protocol_status": "explicit",
        "verbatim_quote": "Validation of results against field data showed that self-reported success rates were misleadingly high, and that the model was misidentifying most features.",
        "location": {"section": "Abstract", "subsection": "Findings", "paragraph": 1},
        "linked_methods": ["M006"],
        "linked_evidence": ["E029", "E030", "E031", "E032", "E034", "E035", "E036", "E037", "E038"],
        "execution_context": {"ground_truth": "773 surveyed mounds", "comparison": "Tile-by-tile"},
        "expected_information_missing": ["Validation team size", "Blind validation", "Quality control procedures", "Ambiguous case resolution"]
    }
]

# Add RDMAP items
extraction["research_designs"] = research_designs
extraction["methods"] = methods
extraction["protocols"] = protocols

# Update extraction notes
extraction["extraction_metadata"]["extraction_notes"].append({
    "pass3_rdmap_extraction": {
        "pass_date": "2025-10-30",
        "items_extracted": {
            "research_designs": len(research_designs),
            "methods": len(methods),
            "protocols": len(protocols),
            "total": len(research_designs) + len(methods) + len(protocols)
        },
        "equal_attention_applied": True,
        "sections_covered": {
            "research_designs": ["Abstract", "Data", "Methods", "Discussion"],
            "methods": ["Methods", "Results"],
            "protocols": ["Methods", "Results", "Discussion"]
        },
        "notes": "Liberal RDMAP extraction with equal attention to all sections. Research designs found in Abstract (RD003 - negative results documentation), Data (RD001 - external validation), Methods (RD002 - comparative design), and Discussion (RD004 - cost-benefit analysis). All items have verbatim_quote sourcing. Expected information documented for transparency assessment."
    }
})

# Save
with open(extraction_file, 'w') as f:
    json.dump(extraction, f, indent=2, ensure_ascii=False)

print(f"✓ Pass 3 RDMAP extraction complete")
print(f"  Research Designs: {len(research_designs)} items")
print(f"  Methods: {len(methods)} items")
print(f"  Protocols: {len(protocols)} items")
print(f"  TOTAL RDMAP: {len(research_designs) + len(methods) + len(protocols)} items")
print()
print(f"Running total: {77 + len(research_designs) + len(methods) + len(protocols)} items")
print(f"  (77 from Pass 2 + {len(research_designs) + len(methods) + len(protocols)} RDMAP)")
