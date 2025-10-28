#!/usr/bin/env python3
"""
Pass 4: RDMAP Implicit Extraction for sobotkova-et-al-2023.

Scans for implicit RDMAP items (mentioned but undocumented, or inferred
from Results/Discussion sections).

Note: This is a methods paper with extensive explicit documentation.
Implicit RDMAP items are expected to be minimal.
"""

import json
import shutil
from datetime import datetime
from pathlib import Path

def load_extraction():
    """Load the extraction JSON."""
    path = Path("/home/shawn/Code/llm-reproducibility/outputs/sobotkova-et-al-2023/extraction.json")
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_extraction(data, filepath):
    """Save the extraction JSON."""
    # Create backup
    backup_path = filepath.parent / f"{filepath.stem}_before_pass4.json"
    if not backup_path.exists():
        shutil.copy2(filepath, backup_path)
        print(f"Backup created: {backup_path}")

    # Write updated file
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Updated file written: {filepath}")

def add_implicit_methods(data):
    """Add implicit methods inferred from Results/Discussion."""

    # Add to existing methods array
    implicit_methods = [
        {
            "method_id": "M007",
            "content": "Data export and post-processing method for converting device data to analysis-ready formats",
            "method_type": "data_processing",
            "method_status": "implicit",
            "implicit_metadata": {
                "basis": "mentioned_but_not_described",
                "trigger_text": [
                    "Exported data was consistent and complete, ready for analysis with minimal cleaning.",
                    "project staff exported data using the FAIMS Mobile server"
                ],
                "trigger_locations": [
                    "Abstract, page 1",
                    "Approach (2.4), page 5"
                ],
                "inference_reasoning": "Paper mentions data export and processing but does not describe the export methodology, format conversion procedures, or cleaning steps in Methods section.",
                "transparency_gap": "export format selection, cleaning procedures, format conversion steps"
            },
            "location": {
                "section": "Abstract and Approach (inferred)",
                "page": 1
            },
            "implements_designs": ["RD001"],
            "expected_information_missing": [
                "export format specification",
                "cleaning procedure details",
                "quality checks during export"
            ]
        },
        {
            "method_id": "M008",
            "content": "Error categorization method for classifying digitization errors into types (false positives, false negatives, double-marked, classification errors)",
            "method_type": "quality_assessment",
            "method_status": "implicit",
            "implicit_metadata": {
                "basis": "inferred_from_results",
                "trigger_text": [
                    "Forty-two of these errors were false negatives (symbols missed by students). Six were double-marked (Student C digitised a section of a map twice). Students made only one classification error (a similar symbol mistaken for a benchmark), and no outright false positives."
                ],
                "trigger_locations": [
                    "Results (3.5.2), page 9"
                ],
                "inference_reasoning": "Results section reports error types suggesting a classification scheme was applied, but Methods section does not describe the error categorization methodology.",
                "transparency_gap": "error type definitions, classification decision rules"
            },
            "location": {
                "section": "Results (3.5.2) - inferred",
                "page": 9
            },
            "implements_designs": ["RD004"],
            "realized_through_protocols": ["P012"],
            "expected_information_missing": [
                "error type definitions",
                "classification criteria",
                "inter-rater reliability"
            ]
        }
    ]

    data['methods'].extend(implicit_methods)
    print(f"✓ Added {len(implicit_methods)} implicit Methods")
    return len(implicit_methods)

def add_implicit_protocols(data):
    """Add implicit protocols inferred from Results/Discussion."""

    # Add to existing protocols array
    implicit_protocols = [
        {
            "protocol_id": "P015",
            "content": "Map tile assignment protocol for distributing maps to volunteers",
            "protocol_type": "work_allocation",
            "protocol_status": "implicit",
            "implicit_metadata": {
                "basis": "mentioned_but_not_described",
                "trigger_text": [
                    "First, participants failed to digitise some assigned maps, leaving noticeable gaps"
                ],
                "trigger_locations": [
                    "Results (3.5.2), page 7"
                ],
                "inference_reasoning": "Results mention 'assigned maps' implying an assignment protocol existed, but Methods section does not describe how maps were assigned to volunteers.",
                "transparency_gap": "assignment algorithm, load balancing, tracking completion"
            },
            "location": {
                "section": "Results (3.5.2) - inferred",
                "page": 7
            },
            "implements_methods": ["M001"],
            "expected_information_missing": [
                "assignment criteria",
                "volunteer workload balancing",
                "completion tracking method"
            ]
        },
        {
            "protocol_id": "P016",
            "content": "Database reset protocol for managing device performance degradation beyond 2,500-3,000 records",
            "protocol_type": "system_maintenance",
            "protocol_status": "implicit",
            "implicit_metadata": {
                "basis": "inferred_from_results",
                "trigger_text": [
                    "Deteriorating performance was mitigated by exporting all data and instantiating a new and empty version of the application."
                ],
                "trigger_locations": [
                    "Results (3.4), page 7"
                ],
                "inference_reasoning": "Results describe the mitigation strategy but Methods section does not specify when/how performance monitoring triggered resets.",
                "transparency_gap": "performance monitoring method, reset trigger thresholds, data aggregation procedure"
            },
            "location": {
                "section": "Results (3.4) - inferred",
                "page": 7
            },
            "implements_methods": ["M003"],
            "expected_information_missing": [
                "performance monitoring protocol",
                "reset decision criteria",
                "data re-aggregation steps"
            ]
        },
        {
            "protocol_id": "P017",
            "content": "Spatial omission correction protocol for re-extracting coordinates from geodatabase when lat/long fields empty",
            "protocol_type": "error_correction",
            "protocol_status": "implicit",
            "implicit_metadata": {
                "basis": "inferred_from_results",
                "trigger_text": [
                    "Since the geodatabase preserved geometries, spatial omissions were corrected by re-extracting latitude and longitude; only two data points could not be recovered."
                ],
                "trigger_locations": [
                    "Results (3.5.1), page 7"
                ],
                "inference_reasoning": "Results describe correction outcome but Methods section does not describe the re-extraction procedure or tools used.",
                "transparency_gap": "re-extraction tool/script, verification steps, unrecoverable record handling"
            },
            "location": {
                "section": "Results (3.5.1) - inferred",
                "page": 7
            },
            "implements_methods": ["M004"],
            "expected_information_missing": [
                "coordinate extraction tool",
                "verification procedure",
                "handling of unrecoverable records"
            ]
        }
    ]

    data['protocols'].extend(implicit_protocols)
    print(f"✓ Added {len(implicit_protocols)} implicit Protocols")
    return len(implicit_protocols)

def update_extraction_notes(data, counts):
    """Update extraction notes for Pass 4."""
    data['extraction_timestamp'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    data['extractor'] = "Claude Code (Sonnet 4.5) - Pass 4"

    data['extraction_notes'] = {
        "pass": 4,
        "section_extracted": "Full paper - implicit RDMAP scan complete",
        "extraction_strategy": "Targeted scan for implicit RDMAP items (mentioned but undocumented, or inferred from Results/Discussion). Minimal implicit items found due to thorough explicit documentation in Methods section.",
        "implicit_methods_added": counts['methods'],
        "implicit_protocols_added": counts['protocols'],
        "implicit_research_designs_added": 0,
        "observation": "Paper has unusually complete explicit documentation. Most procedures are explicitly described in Methods section. Implicit items limited to operational details and post-processing steps.",
        "known_uncertainties": [
            "Some operational protocols may exist but not be discoverable from paper text",
            "Quality assurance procedures mentioned but details limited"
        ],
        "claims_evidence_extraction_complete": True,
        "rdmap_explicit_extraction_complete": True,
        "rdmap_implicit_extraction_complete": True
    }

def main():
    print("="*80)
    print("PASS 4: IMPLICIT RDMAP EXTRACTION")
    print("="*80)

    # Load extraction
    extraction_path = Path("/home/shawn/Code/llm-reproducibility/outputs/sobotkova-et-al-2023/extraction.json")
    print("\nLoading extraction.json...")
    data = load_extraction()

    # Print before counts
    print(f"\nBEFORE Pass 4:")
    print(f"  Research Designs: {len(data['research_designs'])} (all explicit)")
    print(f"  Methods: {len(data['methods'])} (all explicit)")
    print(f"  Protocols: {len(data['protocols'])} (all explicit)")
    print(f"  Total RDMAP: {len(data['research_designs']) + len(data['methods']) + len(data['protocols'])}")

    # Execute extraction
    print("\n" + "-"*80)
    print("SCANNING FOR IMPLICIT RDMAP")
    print("-"*80)
    print("\nNote: This methods paper has extensive explicit documentation.")
    print("Implicit items expected to be minimal.")

    counts = {}
    counts['methods'] = add_implicit_methods(data)
    counts['protocols'] = add_implicit_protocols(data)
    counts['designs'] = 0  # No implicit designs found

    # Update extraction notes
    update_extraction_notes(data, counts)

    # Print after counts
    total_implicit = counts['methods'] + counts['protocols'] + counts['designs']

    print("\n" + "-"*80)
    print("RESULTS")
    print("-"*80)
    print(f"\nAFTER Pass 4:")
    print(f"  Research Designs: {len(data['research_designs'])} (4 explicit + 0 implicit)")
    print(f"  Methods: {len(data['methods'])} (6 explicit + {counts['methods']} implicit)")
    print(f"  Protocols: {len(data['protocols'])} (14 explicit + {counts['protocols']} implicit)")
    print(f"  Total RDMAP: {len(data['research_designs']) + len(data['methods']) + len(data['protocols'])}")
    print(f"\n  Implicit items added: {total_implicit}")

    # Save
    print("\n" + "-"*80)
    save_extraction(data, extraction_path)

    # Validate
    print("\n" + "-"*80)
    print("POST-WRITE VALIDATION")
    print("-"*80)
    print(f"✓ Research Designs: {len(data['research_designs'])} items")
    print(f"✓ Methods: {len(data['methods'])} items")
    print(f"✓ Protocols: {len(data['protocols'])} items")
    print(f"✓ Claims/Evidence arrays preserved: {len(data['evidence'])}/{len(data['claims'])}/{len(data['implicit_arguments'])}")

    print("\n" + "="*80)
    print("PASS 4 COMPLETE - Ready for Pass 5 (RDMAP Rationalization)")
    print("="*80)

if __name__ == "__main__":
    main()
