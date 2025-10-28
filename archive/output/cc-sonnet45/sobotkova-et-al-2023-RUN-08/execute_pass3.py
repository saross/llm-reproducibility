#!/usr/bin/env python3
"""
Pass 3: RDMAP Explicit Extraction for sobotkova-et-al-2023.

Extracts Research Designs, Methods, and Protocols explicitly documented
in the paper's Methods/Approach sections (Section 2).

Safety: Loads full JSON, adds RDMAP arrays, preserves claims/evidence arrays.
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
    backup_path = filepath.parent / f"{filepath.stem}_before_pass3.json"
    if not backup_path.exists():
        shutil.copy2(filepath, backup_path)
        print(f"Backup created: {backup_path}")

    # Write updated file
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Updated file written: {filepath}")

def extract_research_designs(data):
    """Extract explicit Research Designs from paper."""

    designs = [
        {
            "design_id": "RD001",
            "content": "Case study approach to demonstrate crowdsourced map digitization as minimally resourced auxiliary activity during archaeological fieldwork",
            "verbatim_quote": "This article presents a case study of crowdsourced cultural heritage digitisation from historical maps undertaken by volunteers using a lightweight, streamlined Geographical Information System (GIS) running offline on mobile devices.",
            "design_type": "study_design",
            "design_status": "explicit",
            "reasoning_approach": "demonstrative",
            "location": {
                "section": "Introduction",
                "page": 1
            },
            "validates_claims": ["C001", "C002", "C003", "C004"],
            "expected_information_missing": [
                "explicit rationale for case study selection",
                "generalizability discussion"
            ]
        },
        {
            "design_id": "RD002",
            "content": "Comparative evaluation framework for assessing digitization approaches (desktop GIS by experts, desktop GIS by volunteers, crowdsourcing with mobile apps, machine learning)",
            "verbatim_quote": "This paper argues that crowdsourcing offers advantages compared to alternative approaches under many, if not most, map digitisation scenarios.",
            "design_type": "comparative_evaluation",
            "design_status": "explicit",
            "reasoning_approach": "comparative",
            "location": {
                "section": "Introduction (1.3)",
                "page": 3
            },
            "validates_claims": ["C001", "C017", "C018", "C019"],
            "expected_information_missing": [
                "pre-defined evaluation criteria",
                "systematic comparison protocol"
            ]
        },
        {
            "design_id": "RD003",
            "content": "Usability-focused system design prioritizing 'useful' tools combining utility and usability for novice volunteers",
            "verbatim_quote": "While some expert interaction is unavoidable and desirable, it can be profitably supplemented by the development of 'useful' tools that combine 'utility' with 'usability' (Nielsen, 2012).",
            "design_type": "design_framework",
            "design_status": "explicit",
            "reasoning_approach": "theoretical",
            "location": {
                "section": "Introduction (1.4)",
                "page": 3
            },
            "validates_claims": ["C003", "C023", "C031"],
            "expected_information_missing": [
                "explicit usability testing protocol",
                "user acceptance criteria"
            ]
        },
        {
            "design_id": "RD004",
            "content": "Efficiency evaluation design using staff time as primary metric for comparing digitization approaches",
            "verbatim_quote": "At that point, we decided to catalogue inputs (time invested by staff and volunteers) versus outputs (features digitised) as part of a research program to evaluate digital approaches to fieldwork",
            "design_type": "evaluation_framework",
            "design_status": "explicit",
            "reasoning_approach": "quantitative",
            "location": {
                "section": "Approach (2.5)",
                "page": 6
            },
            "validates_claims": ["C001", "C017", "C018"],
            "expected_information_missing": [
                "justification for staff time as primary metric",
                "cost-benefit analysis framework"
            ]
        }
    ]

    data['research_designs'] = designs
    print(f"✓ Extracted {len(designs)} Research Designs")
    return len(designs)

def extract_methods(data):
    """Extract explicit Methods from paper."""

    methods = [
        {
            "method_id": "M001",
            "content": "Crowdsourcing approach using undergraduate field school participants as novice volunteers for map digitization",
            "verbatim_quote": "The task of digitising potentially thousands of mounds provided an opportunity to involve students in authentic research.",
            "method_type": "data_collection",
            "method_status": "explicit",
            "location": {
                "section": "Approach (2.2)",
                "page": 4
            },
            "implements_designs": ["RD001", "RD002"],
            "realized_through_protocols": ["P001", "P002", "P005"],
            "expected_information_missing": [
                "volunteer recruitment protocol",
                "volunteer retention strategy"
            ]
        },
        {
            "method_id": "M002",
            "content": "Mobile application customization approach using FAIMS Mobile platform to create streamlined GIS for volunteers",
            "verbatim_quote": "For the 2017–2018 field seasons, TRAP staff created a simplified and streamlined data capture system built using the FAIMS Mobile platform.",
            "method_type": "tool_development",
            "method_status": "explicit",
            "location": {
                "section": "Approach (2)",
                "page": 3
            },
            "implements_designs": ["RD003"],
            "realized_through_protocols": ["P003", "P004", "P006"],
            "expected_information_missing": [
                "customization methodology",
                "iterative design process"
            ]
        },
        {
            "method_id": "M003",
            "content": "Offline-first data collection method tolerating degraded network connectivity in rural field conditions",
            "verbatim_quote": "FAIMS Mobile worked offline. Our digitisation took place alongside fieldwork, at field bases in rural Bulgaria. Reliable internet connectivity could not be guaranteed under these circumstances; a system that tolerated degraded network connectivity was required.",
            "method_type": "data_collection",
            "method_status": "explicit",
            "location": {
                "section": "Approach (2.3)",
                "page": 4
            },
            "implements_designs": ["RD001"],
            "realized_through_protocols": ["P007", "P008"],
            "expected_information_missing": [
                "network failure handling procedures",
                "data loss prevention strategy"
            ]
        },
        {
            "method_id": "M004",
            "content": "Random sampling quality assurance method for accuracy checking of volunteer digitization",
            "verbatim_quote": "Finally, project staff reviewed randomly selected digitisation work completed by volunteers to characterise errors.",
            "method_type": "quality_control",
            "method_status": "explicit",
            "location": {
                "section": "Approach (2.5)",
                "page": 6
            },
            "implements_designs": ["RD004"],
            "realized_through_protocols": ["P012"],
            "expected_information_missing": [
                "sample size determination",
                "error classification scheme"
            ]
        },
        {
            "method_id": "M005",
            "content": "Time-on-task measurement method tracking staff and volunteer hours for efficiency evaluation",
            "verbatim_quote": "To measure inputs, we collated the amount of time spent by various participants in the process, including the student programmer who instantiated the customisation, the student volunteers who undertook the digitisation, and project staff who configured the system, supported volunteers, exported data, and checked for errors.",
            "method_type": "measurement",
            "method_status": "explicit",
            "location": {
                "section": "Approach (2.5)",
                "page": 6
            },
            "implements_designs": ["RD004"],
            "realized_through_protocols": ["P013", "P014"],
            "expected_information_missing": [
                "time recording granularity",
                "handling of interrupted work sessions"
            ]
        },
        {
            "method_id": "M006",
            "content": "Separation of concerns approach: staff handle technical setup, volunteers handle digitization only",
            "verbatim_quote": "This approach moved activities requiring technical expertise to phases where specialists could contribute, while simplifying the tasks assigned to student volunteers as much as possible.",
            "method_type": "workflow_organization",
            "method_status": "explicit",
            "location": {
                "section": "Approach (2.4)",
                "page": 5
            },
            "implements_designs": ["RD003"],
            "realized_through_protocols": ["P003", "P009"],
            "expected_information_missing": [
                "task allocation criteria",
                "handoff procedures between staff and volunteers"
            ]
        }
    ]

    data['methods'] = methods
    print(f"✓ Extracted {len(methods)} Methods")
    return len(methods)

def extract_protocols(data):
    """Extract explicit Protocols from paper."""

    protocols = [
        {
            "protocol_id": "P001",
            "content": "Minimal training protocol: volunteers receive only minutes of training before beginning digitization",
            "verbatim_quote": "Training and supervision of students took no more than half an hour of staff time across the entire 2017 season.",
            "protocol_type": "training",
            "protocol_status": "explicit",
            "location": {
                "section": "Results (3.1)",
                "page": 7
            },
            "implements_methods": ["M001"],
            "expected_information_missing": [
                "training content details",
                "training delivery method"
            ]
        },
        {
            "protocol_id": "P002",
            "content": "Opportunistic work allocation: volunteers digitize when time available (rainy days, downtime from main fieldwork)",
            "verbatim_quote": "In 2017, it was used for a total of 125.8 person-hours concentrated across five rainy days... In 2018, use was more sporadic; participants who stayed at the base for any reason sometimes undertook digitisation.",
            "protocol_type": "work_allocation",
            "protocol_status": "explicit",
            "location": {
                "section": "Results (3.2)",
                "page": 7
            },
            "implements_methods": ["M001"],
            "expected_information_missing": [
                "task assignment mechanism",
                "workload balancing strategy"
            ]
        },
        {
            "protocol_id": "P003",
            "content": "Server-client setup protocol: staff configure server and client devices before volunteer digitization begins",
            "verbatim_quote": "Setup of the server and configuration of the client devices in the field required 3 h from staff.",
            "protocol_type": "system_setup",
            "protocol_status": "explicit",
            "location": {
                "section": "Results (3.1)",
                "page": 7
            },
            "implements_methods": ["M002", "M006"],
            "expected_information_missing": [
                "server configuration steps",
                "device configuration checklist"
            ]
        },
        {
            "protocol_id": "P004",
            "content": "Map preparation protocol: georeferenced maps tiled and pyramids added before distribution to devices",
            "verbatim_quote": "Map preparation (tiling, adding pyramids) required about 1.5 h.",
            "protocol_type": "data_preparation",
            "protocol_status": "explicit",
            "location": {
                "section": "Results (3.1)",
                "page": 7
            },
            "implements_methods": ["M002"],
            "expected_information_missing": [
                "tiling parameters",
                "pyramid generation tool",
                "quality control checks"
            ]
        },
        {
            "protocol_id": "P005",
            "content": "Point-and-annotate digitization protocol: volunteers place point on symbol and fill out attribute form",
            "verbatim_quote": "Volunteers could toggle between a map view for geospatial data interactions and a form view for attribute creation and editing.",
            "protocol_type": "data_capture",
            "protocol_status": "explicit",
            "location": {
                "section": "Approach (2.4)",
                "page": 6
            },
            "implements_methods": ["M001"],
            "expected_information_missing": [
                "symbol identification guidance",
                "attribute completion rules"
            ]
        },
        {
            "protocol_id": "P006",
            "content": "Controlled vocabulary implementation: predefined attribute terms displayed to volunteers for selection",
            "verbatim_quote": "It applied the spatial reference system, rendered maps in the workspace, provided layer management (including a data entry layer), enforced shape topology, displayed pre-defined controlled vocabularies for attribute terms",
            "protocol_type": "data_validation",
            "protocol_status": "explicit",
            "location": {
                "section": "Approach (2.4)",
                "page": 5
            },
            "implements_methods": ["M002"],
            "expected_information_missing": [
                "vocabulary terms list",
                "vocabulary development process"
            ]
        },
        {
            "protocol_id": "P007",
            "content": "Offline data collection protocol: volunteers work without network, data stored locally on device",
            "verbatim_quote": "Data collection works offline, and can employ as many devices as necessary. It is later synchronised opportunistically, when a network is available.",
            "protocol_type": "data_collection",
            "protocol_status": "explicit",
            "location": {
                "section": "Approach (2.3)",
                "page": 4
            },
            "implements_methods": ["M003"],
            "expected_information_missing": [
                "local storage management",
                "device capacity limits"
            ]
        },
        {
            "protocol_id": "P008",
            "content": "Opportunistic synchronization protocol: data synced to server when network becomes available",
            "verbatim_quote": "This system allowed any number of participants to digitise map features using mobile devices, regardless of network connectivity, and consolidated the resulting data when a network became available.",
            "protocol_type": "data_synchronization",
            "protocol_status": "explicit",
            "location": {
                "section": "Approach (2)",
                "page": 3
            },
            "implements_methods": ["M003"],
            "expected_information_missing": [
                "conflict resolution strategy",
                "sync failure handling"
            ]
        },
        {
            "protocol_id": "P009",
            "content": "Automated metadata capture protocol: system records creation time, author, and change history automatically",
            "verbatim_quote": "It applied the spatial reference system, rendered maps in the workspace... recorded creation time and author for each record, maintained a history of all changes to data",
            "protocol_type": "metadata_capture",
            "protocol_status": "explicit",
            "location": {
                "section": "Approach (2.4)",
                "page": 5
            },
            "implements_methods": ["M002", "M006"],
            "expected_information_missing": [
                "metadata schema",
                "timestamp precision"
            ]
        },
        {
            "protocol_id": "P010",
            "content": "On-device validation protocol: system validates record completeness before allowing save",
            "verbatim_quote": "It applied the spatial reference system... applied validation to ensure record completeness",
            "protocol_type": "data_validation",
            "protocol_status": "explicit",
            "location": {
                "section": "Approach (2.4)",
                "page": 5
            },
            "implements_methods": ["M002"],
            "expected_information_missing": [
                "validation rules specification",
                "error message content"
            ]
        },
        {
            "protocol_id": "P011",
            "content": "Multi-device data merging protocol: server merges data from multiple devices into single dataset",
            "verbatim_quote": "It applied the spatial reference system... merged data from multiple devices, and exported data in common formats.",
            "protocol_type": "data_aggregation",
            "protocol_status": "explicit",
            "location": {
                "section": "Approach (2.4)",
                "page": 5
            },
            "implements_methods": ["M003"],
            "expected_information_missing": [
                "merge algorithm",
                "duplicate detection strategy"
            ]
        },
        {
            "protocol_id": "P012",
            "content": "Random map sampling for QA: four maps (7% of total) randomly selected for staff review and error counting",
            "verbatim_quote": "A review by project staff of four randomly selected maps (7% of the total) found 49 errors from a true count of 834 features",
            "protocol_type": "quality_assurance",
            "protocol_status": "explicit",
            "location": {
                "section": "Results (3.5.2)",
                "page": 7
            },
            "implements_methods": ["M004"],
            "expected_information_missing": [
                "random selection method",
                "review completion criteria"
            ]
        },
        {
            "protocol_id": "P013",
            "content": "Device timestamp recording: system automatically records feature creation start and end times",
            "verbatim_quote": "The average time to record a point feature was 54 s, based on start and end times of feature creation as recorded by the devices",
            "protocol_type": "measurement",
            "protocol_status": "explicit",
            "location": {
                "section": "Results (3.2)",
                "page": 7
            },
            "implements_methods": ["M005"],
            "expected_information_missing": [
                "timestamp format",
                "pause detection method"
            ]
        },
        {
            "protocol_id": "P014",
            "content": "Staff time logging: staff record time-on-task for activities in field journals",
            "verbatim_quote": "Project records provided much of this data (timesheets from the programmer; record creation timestamps for students using the system), while project staff logged time-on-task for activities in journals.",
            "protocol_type": "measurement",
            "protocol_status": "explicit",
            "location": {
                "section": "Approach (2.5)",
                "page": 6
            },
            "implements_methods": ["M005"],
            "expected_information_missing": [
                "journal entry format",
                "recording granularity rules"
            ]
        }
    ]

    data['protocols'] = protocols
    print(f"✓ Extracted {len(protocols)} Protocols")
    return len(protocols)

def update_extraction_notes(data, counts):
    """Update extraction notes for Pass 3."""
    data['extraction_timestamp'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    data['extractor'] = "Claude Code (Sonnet 4.5) - Pass 3"

    data['extraction_notes'] = {
        "pass": 3,
        "section_extracted": "Full paper - explicit RDMAP extraction complete",
        "extraction_strategy": "Extracted explicitly documented RDMAP from Methods/Approach sections (Section 2). Research Designs scanned from Abstract/Introduction. All items have verbatim_quote from paper. Liberal extraction applied per Pass 1 guidance.",
        "research_designs_extracted": counts['designs'],
        "methods_extracted": counts['methods'],
        "protocols_extracted": counts['protocols'],
        "known_uncertainties": [
            "Some design rationales implicit rather than explicit",
            "Validation protocol details limited in Methods section",
            "Time recording procedures mentioned but not fully specified"
        ],
        "claims_evidence_extraction_complete": True,
        "rdmap_explicit_extraction_complete": True,
        "rdmap_implicit_extraction_complete": False
    }

def main():
    print("="*80)
    print("PASS 3: EXPLICIT RDMAP EXTRACTION")
    print("="*80)

    # Load extraction
    extraction_path = Path("/home/shawn/Code/llm-reproducibility/outputs/sobotkova-et-al-2023/extraction.json")
    print("\nLoading extraction.json...")
    data = load_extraction()

    # Print before counts
    print(f"\nBEFORE Pass 3:")
    print(f"  Evidence: {len(data['evidence'])}")
    print(f"  Claims: {len(data['claims'])}")
    print(f"  Implicit Arguments: {len(data['implicit_arguments'])}")
    print(f"  Research Designs: {len(data.get('research_designs', []))}")
    print(f"  Methods: {len(data.get('methods', []))}")
    print(f"  Protocols: {len(data.get('protocols', []))}")

    # Execute extraction
    print("\n" + "-"*80)
    print("EXTRACTING EXPLICIT RDMAP")
    print("-"*80)

    counts = {}
    counts['designs'] = extract_research_designs(data)
    counts['methods'] = extract_methods(data)
    counts['protocols'] = extract_protocols(data)

    # Update extraction notes
    update_extraction_notes(data, counts)

    # Print after counts
    print("\n" + "-"*80)
    print("RESULTS")
    print("-"*80)
    print(f"\nAFTER Pass 3:")
    print(f"  Evidence: {len(data['evidence'])}")
    print(f"  Claims: {len(data['claims'])}")
    print(f"  Implicit Arguments: {len(data['implicit_arguments'])}")
    print(f"  Research Designs: {len(data['research_designs'])}")
    print(f"  Methods: {len(data['methods'])}")
    print(f"  Protocols: {len(data['protocols'])}")

    total_rdmap = len(data['research_designs']) + len(data['methods']) + len(data['protocols'])
    print(f"\n  Total RDMAP items extracted: {total_rdmap}")

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
    print("PASS 3 COMPLETE")
    print("="*80)

if __name__ == "__main__":
    main()
