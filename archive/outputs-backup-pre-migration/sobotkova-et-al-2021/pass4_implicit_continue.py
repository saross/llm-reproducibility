#!/usr/bin/env python3
"""
Pass 4 Implicit RDMAP Extraction (continued): Patterns 2-4
Scanning for additional implicit items using remaining patterns
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Load existing extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

# ============================================================================
# Pass 4 Implicit RDMAP Extraction (continued)
# Patterns 2-4: Effects implying causes, tools without specs, strategic positioning
# ============================================================================

# ADDITIONAL IMPLICIT PROTOCOLS
# ==============================

# IP006: Digital camera photo tracking protocol (Pattern 3: Tools mentioned without specs)
ip006 = {
    "protocol_id": "IP006",
    "protocol_text": "Digital camera photo tracking and linking protocol: record photo numbers from external digital camera, link to device records via notes fields, consolidate during post-processing",
    "protocol_type": "photo_management",
    "protocol_status": "implicit",
    "trigger_text": [
        "During feature recording, teams navigated to known features and made a record that included coordinates, dimensions, photographs (on device and using digital cameras), drawings, and a description of the feature's condition",
        "Notes also accommodated digital camera photo numbers, allowing these photographs to be matched to the record later.",
        "Once server-side validation was completed, data and multimedia were exported from the FAIMS server and stored on a separate file server ... At the end of each day, fieldworkers would return to base, initiate synchronization, download images from digital cameras, and scan any paper records such as plan drawings."
    ],
    "trigger_locations": [
        {
            "section": "System Requirements - Legacy Feature Recording Requirements",
            "page": 4,
            "start_paragraph": 12,
            "end_paragraph": 12
        },
        {
            "section": "Feature Recording - Typical workflow",
            "page": 14,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        {
            "section": "Post-processing - FAIMS data export",
            "page": 17,
            "start_paragraph": 2,
            "end_paragraph": 2
        }
    ],
    "inference_reasoning": "The paper mentions using external digital cameras alongside device cameras and recording photo numbers to link them, but never documents the tracking protocol. Triggers show: (1) both device and digital cameras used, (2) digital camera photo numbers recorded in notes, (3) photos matched to records later, (4) images downloaded from digital cameras daily. This implies a protocol for tracking external camera photos, recording their numbers, linking them to digital records, downloading and organizing them, but these procedures are not documented.",
    "implicit_metadata": {
        "basis": "mentioned_undocumented",
        "transparency_gap": "Digital camera photo tracking protocol not documented: photo number recording standards, linking procedure, download and organization workflow, verification of photo-record linkage, file naming and storage conventions",
        "assessability_impact": "Cannot assess reliability of photo-record linkage or systematic nature of photo management procedures",
        "reconstruction_confidence": "medium"
    },
    "implements_methods": ["M002", "M006"],
    "procedure_steps": [
        "(inferred) Take photo with digital camera",
        "(inferred) Note camera photo number",
        "(inferred) Record photo number in device notes field",
        "(inferred) Download photos from camera at day end",
        "(inferred) Match photo numbers to records",
        "(inferred) Organize and store linked photos"
    ],
    "expected_information_missing": [
        "Photo number recording format",
        "Linking verification procedures",
        "File organization standards",
        "Photo metadata management",
        "Quality control for photo-record linkage"
    ],
    "extraction_confidence": "high"
}

# IP007: Efficiency comparison method (Pattern 2: Effects implying methodology)
# Note: Re-examining this - it's mentioned in Discussion but methodology not in Methods
im002 = {
    "method_id": "IM002",
    "method_text": "Retrospective efficiency comparison method: compare time spent on field data management between current FAIMS-based workflow and previous hybrid paper-digital workflow",
    "method_type": "comparative_evaluation",
    "method_status": "implicit",
    "trigger_text": [
        "Three of the authors conducted TRAP fieldwork in Bulgaria from 2008–2011 using hybrid paper and digital (ArcPad-based) field data recording (Ross et al. 2010; Sobotkova and Ross 2018). Compared to that approach, we estimate that the fully digital workflow using FAIMS Mobile offered the following time savings: 1) a more comprehensive system saved all team members 2–3 hours of paper form digitization and manual image labelling and renaming each day; 2) automated synchronization saved team leaders about 1 hour of tending the manual aspects of ArcPad data synchronization each day; 3) data validation saved team leaders 1/2 day per week previously spent checking and correcting errors...",
        "PPAP did not, however, aim to achieve efficiency at the expense of all else."
    ],
    "trigger_locations": [
        {
            "section": "Discussion - Efficiency dividends",
            "page": 19,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        {
            "section": "Discussion - Efficiency dividends",
            "page": 19,
            "start_paragraph": 2,
            "end_paragraph": 2
        }
    ],
    "inference_reasoning": "The Discussion presents detailed time-saving estimates comparing FAIMS workflow to previous TRAP workflow, but the comparison methodology is not documented. Triggers show: (1) authors draw on previous project experience (TRAP 2008-2011), (2) specific time estimates provided (2-3 hours/day, 1 hour/day, 0.5 day/week), (3) comparison across multiple workflow components, (4) estimates qualified as not pursuing efficiency at all costs. This implies a method for retrospective efficiency comparison, but the basis for estimates (timing studies, logs, memory, etc.) and comparison methodology are not documented in Methods.",
    "implicit_metadata": {
        "basis": "inferred_from_results",
        "transparency_gap": "Efficiency comparison method not documented: data collection approach for time estimates, comparison methodology, baseline workflow documentation, estimation procedures, uncertainty quantification",
        "assessability_impact": "Cannot assess reliability of efficiency claims or verify comparison methodology rigor",
        "reconstruction_confidence": "low"
    },
    "method_purpose": "To evaluate workflow efficiency improvements from fully digital system compared to hybrid approach",
    "implements_designs": ["RD001"],
    "expected_information_missing": [
        "Time measurement methodology",
        "Data sources for estimates (logs, surveys, memory)",
        "Comparison criteria and metrics",
        "Baseline workflow documentation",
        "Uncertainty estimation procedures"
    ],
    "extraction_confidence": "high"
}

# IP008: Hardware configuration protocol (Pattern 3: Equipment mentioned without specs)
ip008 = {
    "protocol_id": "IP008",
    "protocol_text": "Local server hardware configuration protocol: configure low-power industrial computer as FAIMS server, set up network, install server software from virtual machine image",
    "protocol_type": "system_setup",
    "protocol_status": "implicit",
    "trigger_text": [
        "In terms of resource constraints, we had little scope for hardware purchases or software development. In addition to project leaders' university-provided laptops, we had access to a low-power industrial computer, basic networking gear, and Android tablets, all purchased for fieldwork in 2015 (Supplemental Material 1).",
        "PPAP used a low-power industrial computer as a local server (see Supplemental Material 1), preconfigured before fieldwork. The server has a web interface available to any device on the network",
        "The server is a Ruby application running under Ubuntu, installed either from a shell script or a virtual machine image supplied by FAIMS."
    ],
    "trigger_locations": [
        {
            "section": "Additional PPAP Requirements",
            "page": 5,
            "start_paragraph": 2,
            "end_paragraph": 2
        },
        {
            "section": "FAIMS Mobile deployment - Module instantiation on a server",
            "page": 7,
            "start_paragraph": 1,
            "end_paragraph": 1
        },
        {
            "section": "FAIMS Mobile deployment - Module instantiation on a server",
            "page": 7,
            "start_paragraph": 1,
            "end_paragraph": 1
        }
    ],
    "inference_reasoning": "The paper mentions server hardware and that it was preconfigured before fieldwork, but does not document the configuration protocol. Triggers show: (1) low-power industrial computer used as server, (2) basic networking gear deployed, (3) server preconfigured before fieldwork, (4) Ruby application installed from script or VM image, (5) web interface set up. This implies a protocol for server hardware selection, installation, network configuration, and testing, but these procedures are not documented.",
    "implicit_metadata": {
        "basis": "mentioned_undocumented",
        "transparency_gap": "Server configuration protocol not documented: hardware specifications, installation procedures, network setup steps, security configuration, performance testing, backup system setup",
        "assessability_impact": "Cannot assess whether server infrastructure was adequate for project scale or properly configured for field conditions",
        "reconstruction_confidence": "low"
    },
    "implements_methods": ["M003", "M004"],
    "procedure_steps": [
        "(inferred) Select server hardware",
        "(inferred) Install Ruby/Ubuntu from image",
        "(inferred) Configure network settings",
        "(inferred) Set up web interface",
        "(inferred) Test server functionality",
        "(inferred) Configure backup system",
        "(inferred) Document server access credentials"
    ],
    "expected_information_missing": [
        "Hardware selection criteria",
        "Installation procedure details",
        "Network configuration specifications",
        "Security configuration steps",
        "Performance testing procedures",
        "Pre-deployment checklist"
    ],
    "extraction_confidence": "medium"
}

# Add items to arrays
data["protocols"].extend([ip006, ip008])
data["methods"].append(im002)

# Update extraction metadata - PASS 4 COMPLETE
data["extraction_timestamp"] = datetime.now(timezone.utc).isoformat()
data["extraction_notes"]["pass"] = 4
data["extraction_notes"]["section_extracted"] = "Pass 4 implicit RDMAP extraction COMPLETE. Systematic 4-pattern scan across all sections completed. Total implicit RDMAP: 2 methods, 7 protocols = 9 items. Explicit RDMAP: 2 designs, 6 methods, 15 protocols = 23 items. Combined total: 2 designs, 8 methods, 22 protocols = 32 items. Implicit RDMAP: 28.1% (9/32). Within expected 20-40% range. Patterns 1 (mentioned undocumented) and 3 (tools without specs) yielded most items. Pattern 2 (effects implying causes) yielded 1 retrospective comparison method. No implicit research designs found - strategic decisions were explicitly documented. Next: Pass 5 rationalization."
data["extraction_notes"]["extraction_strategy"] = "Pass 4 used systematic 4-pattern scanning for implicit RDMAP: (1) procedures mentioned without description, (2) effects implying methodological causes, (3) tools/equipment mentioned without specifications, (4) strategic positioning without explicit statement. Most implicit items found via Pattern 1 and 3. Scanned Abstract, Introduction, Methods, Results, Discussion systematically. Implicit items concentrated in Results/Discussion sections and operational details mentioned but not elaborated in Methods."
data["extraction_notes"]["known_uncertainties"] = [
    "Efficiency comparison method reconstruction confidence is low (estimates based on author memory)",
    "Server configuration and backup protocols have low reconstruction confidence (minimal documentation)",
    "Training method details completely absent (only existence mentioned)",
    "Some additional implicit protocols may exist but signals too weak to extract with confidence"
]

# Save final Pass 4 state
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

# Generate summary statistics
total_explicit_rdmap = 2 + 6 + 15  # designs, methods, protocols
total_implicit_rdmap = 0 + 2 + 7   # designs, methods, protocols
total_rdmap = total_explicit_rdmap + total_implicit_rdmap
implicit_percentage = (total_implicit_rdmap / total_rdmap * 100)

total_claims_evidence = len(data['evidence']) + len(data['claims']) + len(data['implicit_arguments'])
grand_total = total_claims_evidence + total_rdmap

print("=" * 70)
print("PASS 4 IMPLICIT RDMAP EXTRACTION COMPLETE")
print("=" * 70)
print(f"\nRDMAP Breakdown:")
print(f"  Research Designs: {len(data['research_designs'])} (2 explicit, 0 implicit)")
print(f"  Methods: {len(data['methods'])} (6 explicit, 2 implicit)")
print(f"  Protocols: {len(data['protocols'])} (15 explicit, 7 implicit)")
print(f"  RDMAP Subtotal: {total_rdmap} ({total_explicit_rdmap} explicit, {total_implicit_rdmap} implicit)")
print(f"  Implicit RDMAP: {implicit_percentage:.1f}%")
print(f"\nClaims/Evidence (from Pass 1-2):")
print(f"  Evidence: {len(data['evidence'])}")
print(f"  Claims: {len(data['claims'])}")
print(f"  Implicit Arguments: {len(data['implicit_arguments'])}")
print(f"  Subtotal: {total_claims_evidence}")
print(f"\nGRAND TOTAL (after Pass 4): {grand_total} items")
print(f"\n" + "=" * 70)
print("NEXT STEP: Pass 5 - RDMAP Rationalization and Consolidation")
print("=" * 70)
print("\nPass 5 tasks:")
print("  - Review RDMAP tier assignments (design vs method vs protocol)")
print("  - Consolidate any redundant RDMAP items")
print("  - Verify cross-references between RDMAP items")
print("  - Target 15-20% reduction if appropriate")
