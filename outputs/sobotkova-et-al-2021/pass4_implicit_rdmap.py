#!/usr/bin/env python3
"""
Pass 4: Implicit RDMAP Extraction for sobotkova-et-al-2021

Systematic scan for RDMAP items that are mentioned but undocumented,
or inferred from Results/Discussion sections.

Using 4-pattern systematic scanning as per prompt 04.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Load existing extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

# ============================================================================
# Pass 4 Implicit RDMAP Extraction
# Systematic 4-pattern scan across all sections
# ============================================================================

# IMPLICIT PROTOCOLS
# ==================

# IP001: Device malfunction recovery protocol (Pattern 1: Mentioned without description)
ip001 = {
    "protocol_id": "IP001",
    "protocol_text": "Device malfunction recovery protocol: restart unstable device, resume data collection on same or different device, rely on synchronization for data integrity",
    "protocol_type": "system_recovery",
    "protocol_status": "implicit",
    "trigger_text": [
        "we were able to collect around 230 survey unit records (> 135,000 values) before one device became unstable. This malfunction required a restart, but no data were lost.",
        "The device was used for the remainder of the day but continued to perform poorly. Data successfully synchronized in the evening. The remaining 55 survey units were recorded using other tablets, as bi-directional synchronization allowed seamless replacement of any device at any time."
    ],
    "trigger_locations": [
        {
            "section": "Results - Performance",
            "page": 18,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        {
            "section": "Results - Performance",
            "page": 18,
            "start_paragraph": 2,
            "end_paragraph": 2
        }
    ],
    "inference_reasoning": "The paper describes device malfunction and recovery but does not document the recovery protocol. Triggers show: (1) device became unstable requiring restart, (2) device continued to be used despite poor performance, (3) data synchronized successfully, (4) remaining work completed on other devices. This implies a protocol for handling device failures, but no procedure is documented in Methods section for device troubleshooting, deciding when to switch devices, or ensuring data integrity during recovery.",
    "implicit_metadata": {
        "basis": "mentioned_undocumented",
        "transparency_gap": "Device failure recovery procedures not documented: troubleshooting steps, decision criteria for device replacement, data integrity verification after malfunction",
        "assessability_impact": "Cannot assess whether data loss risks were properly managed during device failures, or whether recovery procedures were systematic vs ad-hoc",
        "reconstruction_confidence": "medium"
    },
    "implements_methods": ["M003"],
    "procedure_steps": [
        "(inferred) Recognize device instability",
        "(inferred) Restart device",
        "(inferred) Attempt continued use",
        "(inferred) Decide to switch to alternate device",
        "(inferred) Verify synchronization integrity",
        "(inferred) Continue on alternate device"
    ],
    "expected_information_missing": [
        "Instability symptoms and recognition criteria",
        "Troubleshooting checklist",
        "Decision criteria for device replacement",
        "Data integrity verification procedures",
        "Device swap protocols"
    ],
    "extraction_confidence": "high"
}

# IP002: Bluetooth GPS troubleshooting protocol (Pattern 1: Mentioned without description)
ip002 = {
    "protocol_id": "IP002",
    "protocol_text": "Bluetooth GPS connectivity troubleshooting protocol: detect connection loss, switch from external to internal GPS, accept reduced accuracy to maintain data collection",
    "protocol_type": "sensor_troubleshooting",
    "protocol_status": "implicit",
    "trigger_text": [
        "On Nvidia Shield tablets, the Gridded Survey module also tended to lose connectivity with external Bluetooth GPS, a device-specific bug that we were unable to fix in the field. Internal GPS was used instead, introducing a slightly larger spatial error and reducing device battery life."
    ],
    "trigger_locations": [
        {
            "section": "Results - Performance",
            "page": 18,
            "start_paragraph": 2,
            "end_paragraph": 2
        }
    ],
    "inference_reasoning": "The paper describes Bluetooth GPS connectivity problems and the solution (switching to internal GPS) but does not document the troubleshooting protocol. The trigger shows: (1) connectivity loss occurred, (2) problem identified as device-specific bug, (3) field fix attempted but unsuccessful, (4) fallback to internal GPS implemented, (5) trade-offs accepted (reduced accuracy, battery life). This implies a protocol for diagnosing GPS problems, attempting fixes, and implementing fallback solutions, but no such procedure is documented in Methods.",
    "implicit_metadata": {
        "basis": "mentioned_undocumented",
        "transparency_gap": "GPS troubleshooting procedures not documented: diagnostic steps, fallback decision criteria, accuracy trade-off thresholds, battery management strategies",
        "assessability_impact": "Cannot assess whether GPS problems were systematically diagnosed and resolved, or how spatial accuracy requirements were balanced against operational constraints",
        "reconstruction_confidence": "medium"
    },
    "implements_methods": ["M002", "M003"],
    "procedure_steps": [
        "(inferred) Detect Bluetooth GPS connectivity loss",
        "(inferred) Attempt to reconnect",
        "(inferred) Diagnose as device-specific bug",
        "(inferred) Attempt field fix",
        "(inferred) Decide to use internal GPS instead",
        "(inferred) Accept accuracy and battery trade-offs"
    ],
    "expected_information_missing": [
        "GPS connectivity diagnostic procedures",
        "Reconnection attempts and timing",
        "Field troubleshooting checklist",
        "Decision criteria for fallback to internal GPS",
        "Accuracy threshold specifications"
    ],
    "extraction_confidence": "high"
}

# IP003: Daily artifact collection and labeling protocol (Pattern 1: Mentioned without description)
ip003 = {
    "protocol_id": "IP003",
    "protocol_text": "Diagnostic artifact collection and labeling protocol: collect diagnostic artifacts during survey, bag and label samples, link to digital records via identifiers",
    "protocol_type": "sample_management",
    "protocol_status": "implicit",
    "trigger_text": [
        "Separate counts or densities of major artifact types (e.g., pottery, tile, worked stone, etc.) were announced where possible. At the start of each unit, walkers would report environmental conditions (e.g., land use, slope, surface visibility). At the end of the unit, they would bag and label any diagnostic artifacts they had collected.",
        "Such samples were bagged and tagged. The leader noted the presence of a sample in the Survey Unit tab ... updated any data that proved inaccurate, and characterized the chronology and condition of artifacts."
    ],
    "trigger_locations": [
        {
            "section": "System Requirements - Surface Survey Requirements",
            "page": 5,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        {
            "section": "Gridded Survey - Typical workflow",
            "page": 17,
            "start_paragraph": 3,
            "end_paragraph": 3
        }
    ],
    "inference_reasoning": "The paper mentions collecting, bagging, and labeling diagnostic artifacts multiple times but never documents the protocol. Triggers show: (1) diagnostic artifacts collected during survey, (2) bagging and labeling occurred at unit end, (3) sample presence recorded in digital system, (4) artifact characteristics documented. This implies a systematic sample collection and labeling protocol, including label content, linking to digital records, and tracking procedures, but these operational details are not documented in Methods.",
    "implicit_metadata": {
        "basis": "mentioned_undocumented",
        "transparency_gap": "Artifact collection protocol not documented: selection criteria for diagnostic artifacts, labeling standards, linking procedure between physical samples and digital records, tracking and storage procedures",
        "assessability_impact": "Cannot assess artifact sampling strategy rigor, or verify physical-digital linkage integrity for sample provenance",
        "reconstruction_confidence": "medium"
    },
    "implements_methods": ["M002"],
    "procedure_steps": [
        "(inferred) Identify diagnostic artifacts during survey",
        "(inferred) Collect diagnostic specimens",
        "(inferred) Bag artifacts at unit end",
        "(inferred) Label bags with unit identifier",
        "(inferred) Record sample presence in digital system",
        "(inferred) Characterize artifact chronology and condition",
        "(inferred) Transport and store samples"
    ],
    "expected_information_missing": [
        "Diagnostic artifact selection criteria",
        "Labeling content and format specifications",
        "Physical-digital linkage procedure",
        "Storage and transport protocols",
        "Inventory verification procedures"
    ],
    "extraction_confidence": "high"
}

# IP004: Server-side validation protocol (Pattern 1: Mentioned without description)
ip004 = {
    "protocol_id": "IP004",
    "protocol_text": "Server-side validation protocol: apply validation rules after synchronization, flag records for review, correct errors while memories fresh",
    "protocol_type": "quality_control",
    "protocol_status": "implicit",
    "trigger_text": [
        "Data can be validated with specified rules on the device at the time of creation or on the server after synchronization.",
        "The Gridded Survey module also used simple server validation rules that marked records for review on both the server and on devices if key fields were null. Such validation at the time of synchronization allowed errors to be corrected while memories were fresh.",
        "Synchronization was fully automated and required no further configuration or intervention on the part of the user except in rare cases of conflict when more than one user edited the same record while offline; conflicting edits like these were flagged on the server for manual reconciliation."
    ],
    "trigger_locations": [
        {
            "section": "FAIMS Mobile",
            "page": 5,
            "start_paragraph": 9,
            "end_paragraph": 9
        },
        {
            "section": "Post-processing - Server-side validation",
            "page": 17,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        {
            "section": "Post-processing - Synchronization",
            "page": 17,
            "start_paragraph": 1,
            "end_paragraph": 1
        }
    ],
    "inference_reasoning": "The paper mentions server-side validation multiple times but never documents the validation protocol in detail. Triggers show: (1) validation occurs after synchronization, (2) rules flag records with null key fields, (3) flagged records marked for review, (4) conflicts identified and flagged for manual reconciliation, (5) errors corrected while memories fresh. This implies a systematic server-side validation protocol including validation rule specifications, flagging mechanisms, error correction workflows, and conflict resolution procedures, but operational details are not documented.",
    "implicit_metadata": {
        "basis": "mentioned_undocumented",
        "transparency_gap": "Server-side validation protocol not documented: specific validation rules, flagging criteria, error notification procedures, correction workflow, conflict resolution procedures, validation timing",
        "assessability_impact": "Cannot assess comprehensiveness of validation rules or systematic nature of error correction procedures",
        "reconstruction_confidence": "medium"
    },
    "implements_methods": ["M005", "M006"],
    "procedure_steps": [
        "(inferred) Devices synchronize with server",
        "(inferred) Server applies validation rules",
        "(inferred) System flags records with null key fields",
        "(inferred) System flags conflicting edits",
        "(inferred) Flagged records marked for review",
        "(inferred) Project staff review flagged records",
        "(inferred) Errors corrected on devices or server",
        "(inferred) Conflicts manually reconciled"
    ],
    "expected_information_missing": [
        "Complete validation rule specifications",
        "Flagging notification procedures",
        "Error correction workflow documentation",
        "Conflict resolution decision criteria",
        "Validation log documentation"
    ],
    "extraction_confidence": "high"
}

# IP005: Data backup protocol (Pattern 1: Mentioned without description)
ip005 = {
    "protocol_id": "IP005",
    "protocol_text": "Automated backup protocol: continuously backup server data to ruggedized external hard drive, maintain redundancy across devices and server",
    "protocol_type": "data_management",
    "protocol_status": "implicit",
    "trigger_text": [
        "Data on the server was continually and automatically backed up to a ruggedized external hard drive. This redundancy, combined with the append-only nature of the database, protected against data loss, made devices interchangeable, and allowed teams to verify and edit one another's data."
    ],
    "trigger_locations": [
        {
            "section": "Post-processing - Synchronization",
            "page": 17,
            "start_paragraph": 1,
            "end_paragraph": 1
        }
    ],
    "inference_reasoning": "The paper mentions continuous automated backup but does not document the backup protocol. The trigger shows: (1) backups were continuous and automatic, (2) backups stored on ruggedized external hard drive, (3) redundancy strategy across devices and server, (4) backup purpose was data loss protection. This implies a systematic backup protocol including backup frequency, verification procedures, restoration procedures, and storage management, but these operational details are not documented in Methods.",
    "implicit_metadata": {
        "basis": "mentioned_undocumented",
        "transparency_gap": "Backup protocol not documented: backup frequency/schedule, verification procedures, restoration testing, storage management, backup retention policy",
        "assessability_impact": "Cannot assess backup strategy comprehensiveness or data recovery capability in case of server failure",
        "reconstruction_confidence": "low"
    },
    "implements_methods": ["M003"],
    "procedure_steps": [
        "(inferred) Server continuously monitors for changes",
        "(inferred) Changed data automatically copied to external drive",
        "(inferred) Backup integrity verified (procedure unknown)",
        "(inferred) Backup storage maintained (procedure unknown)"
    ],
    "expected_information_missing": [
        "Backup frequency and trigger conditions",
        "Backup verification procedures",
        "Restoration testing procedures",
        "Storage management and rotation",
        "Backup retention and cleanup policies"
    ],
    "extraction_confidence": "medium"
}

# IMPLICIT METHODS
# ================

# IM001: Student training method (Pattern 1: Mentioned without description)
im001 = {
    "method_id": "IM001",
    "method_text": "Student volunteer training method: train inexperienced students in field methods, local materials, and digital recording systems",
    "method_type": "training",
    "method_status": "implicit",
    "trigger_text": [
        "Like many projects, moreover, PPAP relied on student volunteers, most of whom had little fieldwork experience, had not previously worked in Greece, and had only basic digital literacy limited to the use of common consumer software.",
        "Teams of five were trained to walk spaced 5 m apart in a 25 × 25 m grid, called a \"survey unit.\"",
        "One of the main aims of PPAP was to train students."
    ],
    "trigger_locations": [
        {
            "section": "Additional PPAP Requirements",
            "page": 5,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        {
            "section": "System Requirements - Surface Survey Requirements",
            "page": 5,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        {
            "section": "Additional PPAP Requirements",
            "page": 5,
            "start_paragraph": 1,
            "end_paragraph": 1
        }
    ],
    "inference_reasoning": "The paper repeatedly mentions student training as a project component and emphasizes reliance on inexperienced student volunteers, but never documents the training method. Triggers show: (1) students had little fieldwork experience, (2) students lacked local knowledge, (3) students had basic digital literacy only, (4) training in survey methods occurred (\"teams trained to walk\"), (5) training students was a main project aim. This implies a systematic training method including curriculum, duration, assessment, and skill development, but training procedures are not documented in Methods.",
    "implicit_metadata": {
        "basis": "mentioned_undocumented",
        "transparency_gap": "Training method not documented: training curriculum, duration, instructional approach, assessment of student competency, practice exercises, error detection and correction during training",
        "assessability_impact": "Cannot assess whether student training was adequate to ensure data quality and consistency, or evaluate training effectiveness",
        "reconstruction_confidence": "low"
    },
    "method_purpose": "To enable inexperienced students to collect reliable archaeological field data using digital systems",
    "implements_designs": ["RD001", "RD002"],
    "expected_information_missing": [
        "Training curriculum content and sequence",
        "Training duration and schedule",
        "Instructional methods and materials",
        "Competency assessment procedures",
        "Practice and feedback mechanisms"
    ],
    "extraction_confidence": "high"
}

# Add items to arrays
data["protocols"].extend([ip001, ip002, ip003, ip004, ip005])
data["methods"].append(im001)

# Update extraction metadata - PASS 4 IN PROGRESS
data["extraction_timestamp"] = datetime.now(timezone.utc).isoformat()
data["extraction_notes"]["pass"] = 4
data["extraction_notes"]["section_extracted"] = "Pass 4 implicit RDMAP extraction IN PROGRESS. Systematic 4-pattern scan across paper. Extracted 5 implicit protocols (device recovery, GPS troubleshooting, sample management, server validation, backup) and 1 implicit method (training). Pattern 1 (mentioned without description) yielded most items. Total RDMAP: 2 designs, 7 methods (6 explicit + 1 implicit), 20 protocols (15 explicit + 5 implicit) = 29 items. Implicit RDMAP: 20.7%. Continuing scan for remaining patterns."

# Save progress
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print(f"✓ Pass 4 implicit RDMAP extraction in progress")
print(f"  Research Designs: {len(data['research_designs'])} (2 explicit)")
print(f"  Methods: {len(data['methods'])} (6 explicit, 1 implicit)")
print(f"  Protocols: {len(data['protocols'])} (15 explicit, 5 implicit)")
print(f"  Total RDMAP: {len(data['research_designs']) + len(data['methods']) + len(data['protocols'])}")
print(f"  Implicit RDMAP: {6 / 29 * 100:.1f}%")
print(f"\nNext: Continue scanning for Pattern 2-4 implicit items")
