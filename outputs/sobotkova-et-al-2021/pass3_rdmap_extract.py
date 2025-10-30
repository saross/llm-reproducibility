#!/usr/bin/env python3
"""
Pass 3: RDMAP Extraction for sobotkova-et-al-2021

This script extracts explicit Research Designs, Methods, and Protocols
from the paper's Methods/Approach sections.

Paper: "Deploying an Offline, Multi-User, Mobile System for Digital Recording
in the Perachora Peninsula, Greece" (Sobotkova et al. 2021)

This is a system implementation paper describing the deployment of FAIMS Mobile
for archaeological field recording.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Load existing extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

# Initialize RDMAP arrays if not present
if "research_designs" not in data:
    data["research_designs"] = []
if "methods" not in data:
    data["methods"] = []
if "protocols" not in data:
    data["protocols"] = []

# ============================================================================
# Pass 3 RDMAP Extraction: Abstract + Introduction + Deployment Context
# Section: Pages 2-4, ~1500 words
# ============================================================================

# RESEARCH DESIGNS - Strategic decisions about WHY research was framed this way
# ===========================================================================

# RD001: Comparative evaluation research design
rd001 = {
    "design_id": "RD001",
    "design_text": "Comparative case study design to evaluate FAIMS Mobile platform against common requirements for field data recording and open research principles",
    "design_type": "case_study",
    "reasoning_approach": "comparative_evaluation",
    "design_status": "explicit",
    "location": {
        "section": "Introduction",
        "page": 2,
        "start_paragraph": 8,
        "end_paragraph": 8
    },
    "verbatim_quote": "This paper presents the deployment of a research-specific, comprehensive, offline-first digital recording system designed to address these challenges during the initial 2020 season of the Perachora Peninsula Archaeological Project (PPAP).",
    "design_scope": "project_level",
    "design_rationale": "To demonstrate how research-specific software can address archaeological field data collection challenges while supporting FAIR principles",
    "expected_information_missing": [
        "Explicit statement of comparative evaluation as research design",
        "Alternative approaches considered",
        "Selection criteria for case study site"
    ],
    "extraction_confidence": "high"
}

# RD002: Requirements-driven development design
rd002 = {
    "design_id": "RD002",
    "design_text": "Requirements-driven system deployment design where field data collection requirements are articulated and matched against system capabilities",
    "design_type": "system_evaluation",
    "reasoning_approach": "requirements_analysis",
    "design_status": "explicit",
    "location": {
        "section": "System Requirements for Digital Field Data Collection",
        "page": 4,
        "start_paragraph": 1,
        "end_paragraph": 1
    },
    "verbatim_quote": "Field data collection requirements were articulated as early as the 1990s, underscoring the challenge of creating context-aware applications to support field walkers in data recording and validation (Pascoe, Ryan, and Morse 1998; Ryan, Pascoe, and Morse 1999).",
    "design_scope": "methodology",
    "design_rationale": "To ensure system selection and customization address actual field research needs",
    "expected_information_missing": [
        "Process for requirement elicitation",
        "Stakeholder involvement in requirements definition",
        "Prioritization criteria for requirements"
    ],
    "extraction_confidence": "high"
}

# METHODS - Tactical approaches about WHAT was done
# ==================================================

# M001: System adaptation method
m001 = {
    "method_id": "M001",
    "method_text": "Reuse and adaptation of existing software modules from open library to create customized field recording applications",
    "method_type": "software_customization",
    "method_status": "explicit",
    "location": {
        "section": "Abstract",
        "page": 2,
        "start_paragraph": 1,
        "end_paragraph": 1
    },
    "verbatim_quote": "We reused and adapted two existing customizations from the FAIMS library for comprehensive digital recording of two workflows, integrating a collection of structured data, geospatial data, photos, and text.",
    "method_purpose": "To quickly deploy field-ready recording systems tailored to project workflows",
    "implements_designs": ["RD001", "RD002"],
    "expected_information_missing": [
        "Selection criteria for base modules",
        "Adaptation process steps",
        "Testing procedures before deployment"
    ],
    "extraction_confidence": "high"
}

# M002: Dual workflow approach
m002 = {
    "method_id": "M002",
    "method_text": "Parallel deployment of two distinct field recording workflows: legacy feature verification and pedestrian survey",
    "method_type": "data_collection",
    "method_status": "explicit",
    "location": {
        "section": "Deployment Context",
        "page": 3,
        "start_paragraph": 4,
        "end_paragraph": 4
    },
    "verbatim_quote": "To achieve these aims, PPAP employed three methods: 1) legacy data verification, involving accurate documentation of features noted during previous fieldwork (and recording of unknown features found in the process); 2) pedestrian survey mapping the distribution of surface artifacts and features; and, 3) photogrammetry of significant features. The digital recording system presented here supported the first two of these methods.",
    "method_purpose": "To document both legacy features and surface artifact distributions in study area",
    "implements_designs": ["RD001"],
    "realized_through_protocols": ["P001", "P002"],
    "expected_information_missing": [
        "Rationale for workflow prioritization",
        "Integration strategy between workflows",
        "Resource allocation between workflows"
    ],
    "extraction_confidence": "high"
}

# M003: Offline-first data management approach
m003 = {
    "method_id": "M003",
    "method_text": "Offline-first data management using local server for module instantiation, synchronization, and export",
    "method_type": "data_management",
    "method_status": "explicit",
    "location": {
        "section": "Introduction",
        "page": 2,
        "start_paragraph": 3,
        "end_paragraph": 3
    },
    "verbatim_quote": "FAIMS Mobile required only modest hardware but supported offline setup, synchronization, and data export, allowing PPAP to deploy it despite unreliable internet access.",
    "method_purpose": "To enable data collection and management without reliable internet connectivity",
    "implements_designs": ["RD002"],
    "realized_through_protocols": ["P003", "P004"],
    "expected_information_missing": [
        "Backup strategy",
        "Conflict resolution approach",
        "Network architecture details"
    ],
    "extraction_confidence": "high"
}

# Add items to arrays
data["research_designs"].extend([rd001, rd002])
data["methods"].extend([m001, m002, m003])

# Update extraction metadata
data["extraction_timestamp"] = datetime.now(timezone.utc).isoformat()
data["extraction_notes"]["pass"] = 3
data["extraction_notes"]["section_extracted"] = "Pass 3 RDMAP extraction started: Abstract + Introduction + Deployment Context (~1500 words). Extracted 2 explicit research designs, 3 explicit methods. Liberal extraction strategy applied. Protocol extraction in progress."

# Save progress
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print(f"✓ Pass 3 initial extraction complete")
print(f"  Research Designs: {len(data['research_designs'])}")
print(f"  Methods: {len(data['methods'])}")
print(f"  Protocols: {len(data['protocols'])}")
print(f"\nNext: Continue extracting protocols and additional RDMAP from Methods sections")
