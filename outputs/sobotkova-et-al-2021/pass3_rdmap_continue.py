#!/usr/bin/env python3
"""
Pass 3 RDMAP Extraction (continued): System Requirements + FAIMS sections
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Load existing extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

# ============================================================================
# Pass 3 RDMAP Extraction: System Requirements + FAIMS Sections
# Sections: Pages 4-6, ~1200 words
# ============================================================================

# PROTOCOLS - Operational procedures about HOW SPECIFICALLY it was done
# =====================================================================

# P001: Legacy feature recording protocol
p001 = {
    "protocol_id": "P001",
    "protocol_text": "Feature verification protocol: navigate to known features using historical maps, record GPS coordinates, dimensions, photographs, descriptions, and condition assessments",
    "protocol_type": "data_collection",
    "protocol_status": "explicit",
    "location": {
        "section": "System Requirements - Legacy Feature Recording Requirements",
        "page": 4,
        "start_paragraph": 12,
        "end_paragraph": 12
    },
    "verbatim_quote": "During feature recording, teams navigated to known features and made a record that included coordinates, dimensions, photographs (on device and using digital cameras), drawings, and a description of the feature's condition, noting changes compared to the legacy record. Any unknown features located serendipitously were also recorded.",
    "protocol_steps": [
        "Navigate to feature using historical map",
        "Record GPS coordinates",
        "Measure dimensions",
        "Take photographs (device and digital camera)",
        "Record condition description",
        "Note changes from legacy record",
        "Record serendipitous discoveries"
    ],
    "implements_methods": ["M002"],
    "tool_configurations": [],
    "expected_information_missing": [
        "Specific GPS receiver settings",
        "Measurement tool specifications",
        "Photo capture standards",
        "Team size and roles"
    ],
    "extraction_confidence": "high"
}

# P002: Gridded survey protocol
p002 = {
    "protocol_id": "P002",
    "protocol_text": "Intensive gridded survey protocol: teams of 5 walk 25m×25m units in 5m spaced transects, recording artifact counts every 5m in 5m×5m cells",
    "protocol_type": "data_collection",
    "protocol_status": "explicit",
    "location": {
        "section": "System Requirements - Surface Survey Requirements",
        "page": 5,
        "start_paragraph": 2,
        "end_paragraph": 2
    },
    "verbatim_quote": "Since fieldwork focused on high-use areas near the sanctuary, we employed an intensive \"urban\" variant of systematic survey. Teams of five were trained to walk spaced 5 m apart in a 25 × 25 m grid, called a \"survey unit.\" Walkers examined a 2 m wide swath of ground 1–2 m in front of them, assessing the number and type of artifacts. They called their observations out every 5 m for the team leader to digitally register them, creating a record for each 5 × 5 m2 \"walker cell.\"",
    "protocol_steps": [
        "Team of 5 walkers space 5m apart",
        "Walk 25m × 25m survey unit",
        "Each walker observes 2m wide swath",
        "Stop every 5m",
        "Call out artifact observations",
        "Team leader records in 5m × 5m cells",
        "Record environmental conditions at unit start",
        "Collect and bag diagnostic artifacts"
    ],
    "parameters": {
        "team_size": 5,
        "walker_spacing": "5m",
        "unit_size": "25m × 25m",
        "observation_interval": "5m",
        "cell_size": "5m × 5m",
        "observation_swath": "2m wide"
    },
    "implements_methods": ["M002"],
    "expected_information_missing": [
        "Walking speed specifications",
        "Artifact classification training",
        "Team leader data entry procedures",
        "Quality control checks"
    ],
    "extraction_confidence": "high"
}

# P003: Bi-directional synchronization protocol
p003 = {
    "protocol_id": "P003",
    "protocol_text": "Automatic bi-directional incremental synchronization protocol: devices detect server, send changes, receive consolidated data, achieve complete database replication",
    "protocol_type": "data_management",
    "protocol_status": "explicit",
    "location": {
        "section": "FAIMS Mobile",
        "page": 5,
        "start_paragraph": 9,
        "end_paragraph": 9
    },
    "verbatim_quote": "Opportunistic, incremental, bi-directional synchronization is automatic. When a device detects its server (either local or online), it sends all changes made since last synchronization to the server. The server then integrates those data and returns an up-to-date copy to other devices when they connect. At the end of the process, each device has a complete copy of the database and media (multimedia synchronization can be made unidirectional to save storage space on devices).",
    "protocol_steps": [
        "Device detects server on network",
        "Device sends all changes since last sync",
        "Server integrates changes",
        "Server returns updated data to requesting device",
        "Other devices sync when they connect",
        "All devices achieve complete database copy"
    ],
    "implements_methods": ["M003"],
    "tool_configurations": [
        {
            "tool": "FAIMS Mobile",
            "setting": "synchronization_mode",
            "value": "bi-directional"
        },
        {
            "tool": "FAIMS Mobile",
            "setting": "synchronization_trigger",
            "value": "automatic_on_server_detection"
        }
    ],
    "expected_information_missing": [
        "Conflict resolution procedures",
        "Synchronization frequency",
        "Network requirements",
        "Error handling procedures"
    ],
    "extraction_confidence": "high"
}

# P004: Daily data export protocol
p004 = {
    "protocol_id": "P004",
    "protocol_text": "Daily data export protocol: export synchronized data to CSV and shapefile formats for review, planning, and sharing",
    "protocol_type": "data_management",
    "protocol_status": "explicit",
    "location": {
        "section": "System Requirements - Common Requirements",
        "page": 3,
        "start_paragraph": 7,
        "end_paragraph": 7
    },
    "verbatim_quote": "Such synchronization was also a prerequisite for daily data export as tabular (CSV) and geospatial (Shapefile; KML) files, which allowed project leaders to plan subsequent work, target locations for additional investigation, inform other decisions, and share data with external collaborators.",
    "protocol_steps": [
        "Complete device synchronization",
        "Export data from server",
        "Generate CSV files",
        "Generate shapefile/KML files",
        "Review data for planning",
        "Share with collaborators"
    ],
    "implements_methods": ["M003"],
    "expected_information_missing": [
        "Export timing (specific time of day)",
        "Quality checks before export",
        "Data transformation procedures",
        "File naming conventions"
    ],
    "extraction_confidence": "high"
}

# ADDITIONAL METHODS
# ==================

# M004: Module customization method
m004 = {
    "method_id": "M004",
    "method_text": "XML-based module customization using definition files to specify data structure, user interface, and validation rules",
    "method_type": "software_customization",
    "method_status": "explicit",
    "location": {
        "section": "FAIMS Mobile",
        "page": 6,
        "start_paragraph": 6,
        "end_paragraph": 6
    },
    "verbatim_quote": "Users do not extend a predefined data structure or UI. Since no \"defaults\" exist, FAIMS Mobile must be customized before use. To do so, users define their own data structure and digital forms from scratch or adapt an existing customization. Such a customization is called a \"module.\" ... Depending on the level of control needed, separate definition files can be used to instantiate data structure, UI, and validation rules, or all three can be generated from one, simplified XML file",
    "method_purpose": "To create field-ready applications tailored to specific research workflows",
    "implements_designs": ["RD002"],
    "realized_through_protocols": ["P005"],
    "expected_information_missing": [
        "XML schema documentation process",
        "Testing procedures for modules",
        "Version control for definition files"
    ],
    "extraction_confidence": "high"
}

# P005: Module adaptation protocol for Feature Recording
p005 = {
    "protocol_id": "P005",
    "protocol_text": "Feature Recording module adaptation protocol: expand controlled vocabularies, add GPS multi-point capability, test functionality, load maps, document workflow",
    "protocol_type": "software_customization",
    "protocol_status": "explicit",
    "location": {
        "section": "FAIMS at PPAP - Feature Recording",
        "page": 6,
        "start_paragraph": 2,
        "end_paragraph": 2
    },
    "verbatim_quote": "The controlled vocabulary for \"feature type\" was expanded to include features we expected to encounter based on previous experience and published research (\"wall,\" \"cistern,\" \"artifact scatter,\" etc.). The ability to collect multiple GPS points per feature was also added in order to accommodate more complex feature shapes. After implementing these changes, we tested module functionality, performance, interaction with sensors, synchronization, and export formats. Finally, we loaded local maps and satellite images and documented the recommended field workflow. Adaptation of the existing module took approximately 53 person-hours over five days",
    "protocol_steps": [
        "Expand controlled vocabulary for feature types",
        "Add multi-point GPS capability",
        "Test module functionality",
        "Test performance",
        "Test sensor interaction",
        "Test synchronization",
        "Test export formats",
        "Load local maps and satellite images",
        "Document field workflow"
    ],
    "parameters": {
        "adaptation_time": "53 person-hours",
        "adaptation_duration": "5 days"
    },
    "implements_methods": ["M004"],
    "tool_configurations": [],
    "expected_information_missing": [
        "Testing criteria",
        "Performance benchmarks",
        "Documentation format"
    ],
    "extraction_confidence": "high"
}

# P006: Module deployment for Gridded Survey
p006 = {
    "protocol_id": "P006",
    "protocol_text": "Gridded Survey module deployment protocol: test pre-existing prototype module without modification in parallel with Feature Recording module",
    "protocol_type": "software_customization",
    "protocol_status": "explicit",
    "location": {
        "section": "FAIMS at PPAP - Gridded Survey",
        "page": 6,
        "start_paragraph": 3,
        "end_paragraph": 3
    },
    "verbatim_quote": "Also in 2017, undergraduate programmers working for FAIMS built a demonstration module for systematic survey. This module reconceptualized the paper forms used by TRAP for field survey in Bulgaria during 2009–2011 and aimed to test FAIMS Mobile's performance and UI against a demanding field workflow. This \"Gridded Survey\" module had not previously been used in the field. It was deployed by PPAP without modification in the same five-day timeframe as Feature Recording",
    "protocol_steps": [
        "Evaluate pre-existing prototype module",
        "Test module without field deployment",
        "Deploy without modification",
        "Monitor performance during fieldwork"
    ],
    "parameters": {
        "deployment_time": "5 days"
    },
    "implements_methods": ["M004"],
    "expected_information_missing": [
        "Evaluation criteria for prototype",
        "Risk assessment for untested module",
        "Contingency plans"
    ],
    "extraction_confidence": "high"
}

# Add items to arrays
data["methods"].append(m004)
data["protocols"].extend([p001, p002, p003, p004, p005, p006])

# Update extraction metadata
data["extraction_timestamp"] = datetime.now(timezone.utc).isoformat()
data["extraction_notes"]["section_extracted"] = "Pass 3 RDMAP extraction continued: System Requirements + FAIMS sections (~1200 words). Extracted 1 additional method, 6 explicit protocols. Total: 2 designs, 4 methods, 6 protocols. Liberal extraction strategy maintained. Continuing with detailed implementation sections."

# Save progress
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print(f"✓ Pass 3 continued extraction complete")
print(f"  Research Designs: {len(data['research_designs'])}")
print(f"  Methods: {len(data['methods'])}")
print(f"  Protocols: {len(data['protocols'])}")
print(f"\nNext: Continue with FAIMS deployment sections and field workflows")
