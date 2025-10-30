#!/usr/bin/env python3
"""
Pass 3 RDMAP Extraction (continued): FAIMS Workflows and Data Management
Extracting from pages 7-18: Detailed workflows and post-processing
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Load existing extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

# ============================================================================
# Pass 3 RDMAP Extraction: FAIMS Workflows + Post-Processing
# Sections: Pages 7-18, ~4000 words of detailed methodology
# ============================================================================

# ADDITIONAL METHODS
# ==================

# M005: Controlled vocabulary and automation method
m005 = {
    "method_id": "M005",
    "method_text": "Data quality assurance through aggressive use of controlled vocabularies, automation of value inheritance and derivation, and on-device validation",
    "method_type": "data_quality",
    "method_status": "explicit",
    "location": {
        "section": "Discussion",
        "page": 19,
        "start_paragraph": 2,
        "end_paragraph": 2
    },
    "verbatim_quote": "Aggressive use of controlled vocabularies, automation, validation, and in-application help augmented training and improved the quality of data generated largely by student volunteers.",
    "method_purpose": "To ensure data consistency and quality despite use of inexperienced student volunteers",
    "implements_designs": ["RD002"],
    "realized_through_protocols": ["P007", "P008", "P009"],
    "expected_information_missing": [
        "Vocabulary development process",
        "Validation rule specifications",
        "Training curriculum details"
    ],
    "extraction_confidence": "high"
}

# M006: Daily data review method
m006 = {
    "method_id": "M006",
    "method_text": "Daily review of exported data in GIS and spreadsheet software to inform next-day planning and detect errors while memories fresh",
    "method_type": "quality_control",
    "method_status": "explicit",
    "location": {
        "section": "Post-processing - FAIMS data export",
        "page": 17,
        "start_paragraph": 2,
        "end_paragraph": 2
    },
    "verbatim_quote": "Once server-side validation was completed, data and multimedia were exported from the FAIMS server and stored on a separate file server, where they were accessible to project participants.",
    "method_purpose": "To enable rapid error detection and responsive fieldwork planning",
    "implements_designs": ["RD002"],
    "realized_through_protocols": ["P004", "P010"],
    "expected_information_missing": [
        "Review checklist criteria",
        "Error correction procedures",
        "Team communication protocols"
    ],
    "extraction_confidence": "high"
}

# ADDITIONAL PROTOCOLS
# ====================

# P007: Module instantiation protocol
p007 = {
    "protocol_id": "P007",
    "protocol_text": "Server-based module instantiation protocol: upload definition files via web interface, specify metadata, validate files, populate user lists and vocabularies",
    "protocol_type": "software_deployment",
    "protocol_status": "explicit",
    "location": {
        "section": "FAIMS Mobile deployment - Module instantiation on a server",
        "page": 7,
        "start_paragraph": 2,
        "end_paragraph": 2
    },
    "verbatim_quote": "Module instantiation involves uploading the definition files to the server via this interface, then specifying module- and project-level metadata ... The \"Upload Module\" button allows a user to upload a compressed folder containing all definition files in tar.gz format. Alternatively, pressing the \"Create Module\" button opens a page where each definition file can be uploaded individually. Once definition files are validated and the module instantiated, its name will appear in the module list.",
    "protocol_steps": [
        "Access server web interface",
        "Upload definition files (tar.gz or individually)",
        "Specify module and project metadata",
        "System validates definition files",
        "Module appears in module list",
        "Populate user lists",
        "Modify controlled vocabularies",
        "Upload maps or multimedia",
        "Configure backup settings"
    ],
    "implements_methods": ["M004"],
    "tool_configurations": [
        {
            "tool": "FAIMS Server",
            "setting": "web_interface_access",
            "value": "URL_or_IP_address_with_login"
        }
    ],
    "expected_information_missing": [
        "Validation criteria details",
        "Error handling procedures",
        "Module versioning approach"
    ],
    "extraction_confidence": "high"
}

# P008: Device module installation protocol
p008 = {
    "protocol_id": "P008",
    "protocol_text": "Device module installation protocol: install FAIMS Mobile from Google Play, connect to server, download module, work offline after installation",
    "protocol_type": "software_deployment",
    "protocol_status": "explicit",
    "location": {
        "section": "FAIMS Mobile deployment - Module instantiation on mobile devices",
        "page": 7,
        "start_paragraph": 3,
        "end_paragraph": 3
    },
    "verbatim_quote": "Once per device, a user installs FAIMS Mobile from Google Play. Upon first launch, the application is connected to an online demonstration server with example modules and must be reconnected to the project-specific local server or online server ... Since PPAP employed a local server, users connected a device by joining the server's network, opening the application, then selecting \"Auto-Discover Server\" or entering the server's IP address from \"Settings\" in Android's \"overflow menu\" (three stacked dots). Once connected to a server, users see a list of available modules. Modules on the server can be installed or updated on the device by tapping them. Once a module is loaded on the device, data can be collected without a connection to the server.",
    "protocol_steps": [
        "Install FAIMS Mobile from Google Play",
        "Join server network (for local server)",
        "Open FAIMS Mobile application",
        "Auto-discover server or enter IP address",
        "Select module from list",
        "Tap to install/update module",
        "Work offline after installation"
    ],
    "implements_methods": ["M004"],
    "expected_information_missing": [
        "Device requirements",
        "Network configuration details",
        "Troubleshooting procedures"
    ],
    "extraction_confidence": "high"
}

# P009: On-device validation protocol
p009 = {
    "protocol_id": "P009",
    "protocol_text": "On-device validation protocol: press Validate button to check required fields, receive immediate feedback on missing data, supply missing information before proceeding",
    "protocol_type": "quality_control",
    "protocol_status": "explicit",
    "location": {
        "section": "FAIMS Mobile deployment - On-device validation",
        "page": 10,
        "start_paragraph": 7,
        "end_paragraph": 7
    },
    "verbatim_quote": "Each module was equipped with a prominent \"Validate\" button, also available in the application drawer ... When pressed, this button either listed all required fields in the current record that remained empty or displayed an \"All fields contain valid data!\" message ... Required fields included GPS coordinates, device photo, and basic measurements. Validation to ensure required fields are not empty can be invoked quickly in a module's XML definition file. On-device validation was popular with fieldworkers, as it immediately confirmed that all necessary data had been collected.",
    "protocol_steps": [
        "Press Validate button in module",
        "System checks required fields",
        "Display missing fields OR success message",
        "Fieldworker supplies missing data if needed",
        "Re-validate before record completion"
    ],
    "implements_methods": ["M005"],
    "expected_information_missing": [
        "Validation rule specifications",
        "Error message formatting",
        "Validation timing recommendations"
    ],
    "extraction_confidence": "high"
}

# P010: Spatial data management protocol
p010 = {
    "protocol_id": "P010",
    "protocol_text": "Daily spatial data digitization protocol: export feature data to GIS, digitize survey unit polygons using GPS points and unit parameters, review spatial accuracy",
    "protocol_type": "data_processing",
    "protocol_status": "explicit",
    "location": {
        "section": "Post-processing - Spatial data management",
        "page": 17,
        "start_paragraph": 3,
        "end_paragraph": 3
    },
    "verbatim_quote": "Each day, we plotted spatial data exported from the Feature Recording module in a desktop GIS (QGIS), where features were reviewed. Gridded Survey data were also exported to the GIS, where project participants drew polygons using the starting GPS point as an anchor, and walker number, row count, and walker/count interval as parameters defining the size of each survey unit polygon. This shape creation was supplemented by points from handheld GPS receivers if necessary. Survey unit polygons were digitized immediately upon return from the field in order to ensure accurate representation of teams' progress and took about 30 minutes per team each day.",
    "protocol_steps": [
        "Export feature data to GIS (QGIS)",
        "Plot and review feature locations",
        "Export survey unit data",
        "Draw survey unit polygons using GPS anchor points",
        "Apply walker number and interval parameters",
        "Supplement with handheld GPS points if needed",
        "Complete within ~30 minutes per team"
    ],
    "parameters": {
        "processing_time": "30 minutes per team per day",
        "software": "QGIS"
    },
    "implements_methods": ["M006"],
    "expected_information_missing": [
        "Polygon drawing standards",
        "Accuracy thresholds",
        "Error correction procedures"
    ],
    "extraction_confidence": "high"
}

# P011: Feature Recording typical workflow protocol
p011 = {
    "protocol_id": "P011",
    "protocol_text": "Feature Recording field workflow: login, initialize GPS, navigate using map, create record, work through tabs cooperatively, validate, proceed to next feature",
    "protocol_type": "data_collection",
    "protocol_status": "explicit",
    "location": {
        "section": "Feature Recording - Typical workflow",
        "page": 14,
        "start_paragraph": 1,
        "end_paragraph": 2
    },
    "verbatim_quote": "At the start of each day, the user operating the tablet would log in, confirm the \"Next Feature ID\" value on the device, and either initialize the internal GPS or connect to an external GPS. The team then navigated to the first feature of the day using the historical map, topographic map, and satellite image available via the Map tab. Each team worked within a separate target area to avoid duplicate recordings. Previously recorded features were visible in the Map tab, and associated data were available. Once at a feature, the \"Create New Record\" button would be pressed and the team would work through the tabs of the Feature tabgroup ... The recording was done cooperatively, with everyone on the team contributing observations and reviewing content.",
    "protocol_steps": [
        "Login to module",
        "Confirm Next Feature ID",
        "Initialize or connect to GPS",
        "Navigate using maps in Map tab",
        "Create new record at feature",
        "Work through General tab (photos, description, setting)",
        "Record Additional GPS points if needed",
        "Measure dimensions",
        "Photograph and describe associated material",
        "Record condition in CRM tab",
        "Validate record",
        "Proceed to next feature"
    ],
    "parameters": {
        "team_composition": "cooperative team",
        "work_pattern": "target areas to avoid duplicate recording"
    },
    "implements_methods": ["M002"],
    "related_protocols": ["P001"],
    "expected_information_missing": [
        "Team roles and responsibilities",
        "Communication protocols",
        "Time per feature estimates"
    ],
    "extraction_confidence": "high"
}

# P012: Gridded Survey typical workflow protocol
p012 = {
    "protocol_id": "P012",
    "protocol_text": "Gridded Survey field workflow: login, set defaults in Control tab, add survey unit, walk transects calling observations, leader records in Walker Grid, validate, generate next unit",
    "protocol_type": "data_collection",
    "protocol_status": "explicit",
    "location": {
        "section": "Gridded Survey - Typical workflow",
        "page": 16,
        "start_paragraph": 1,
        "end_paragraph": 3
    },
    "verbatim_quote": "After logging in and activating the GPS receiver, the team leader opened the Walkers tab, added each team member, and ordered them according to their position. She then defined environmental and administrative defaults for the unit in the Main tab. As the leader completed these preliminary tasks, other members took their positions and prepared for their assigned roles ... When the team was ready to begin, the leader pressed the \"Add New Survey Unit\" button, which opened the Survey Unit tab and prepopulated it with information inherited from the Main tab, then recorded the starting GPS point. She then switched to the Walker Cells tab and pressed the Walker Grid button ... The team walked in unison at approximately 1 m/s. At the designated 5 m counting interval, the team briefly stopped. The first walker then called out a count or density for each artifact type, which the leader entered into the form associated with that grid cell. After counts were entered for the first walker, the leader pressed the \"Next Cell\" button",
    "protocol_steps": [
        "Login to module",
        "Activate GPS receiver",
        "Open Walkers tab and add team members",
        "Set environmental defaults in Main tab",
        "Team members take positions",
        "Press Add New Survey Unit",
        "Record starting GPS point",
        "Open Walker Grid",
        "Walk in unison at ~1 m/s",
        "Stop every 5m",
        "Walkers call out observations",
        "Leader enters in grid cells",
        "Press Next Cell after each walker",
        "Press Next Row to advance rows",
        "Compute artifact counts at unit end",
        "Validate record",
        "Generate next survey unit"
    ],
    "parameters": {
        "walking_speed": "approximately 1 m/s",
        "observation_interval": "5m",
        "team_size": 5
    },
    "implements_methods": ["M002"],
    "related_protocols": ["P002"],
    "expected_information_missing": [
        "Team training procedures",
        "Quality control checks during survey",
        "Break and rotation schedules"
    ],
    "extraction_confidence": "high"
}

# P013: End-of-day synchronization protocol
p013 = {
    "protocol_id": "P013",
    "protocol_text": "End-of-day synchronization protocol: return to base, connect devices to chargers and wifi, login, enable sync, wait for completion, verify data on server",
    "protocol_type": "data_management",
    "protocol_status": "explicit",
    "location": {
        "section": "Post-processing - Synchronization",
        "page": 17,
        "start_paragraph": 1,
        "end_paragraph": 1
    },
    "verbatim_quote": "At the end of the day, teams would return to base, connect all devices to chargers, join them to the server's wifi network, open the application, log in, and initiate synchronization by pressing the \"Enable Sync\" button in the overflow menu in the app bar. Bi-directional, incremental synchronization across all devices generally took a few minutes for the Gridded Survey module, which contained only text and structured data, and somewhat longer for the Feature Recording module, which often contained many photographs. After synchronization, all records were available on all devices and on the server. Data on the server was continually and automatically backed up to a ruggedized external hard drive. This redundancy, combined with the append-only nature of the database, protected against data loss, made devices interchangeable, and allowed teams to verify and edit one another's data.",
    "protocol_steps": [
        "Return to base",
        "Connect devices to chargers",
        "Join server wifi network",
        "Open FAIMS Mobile application",
        "Login to module",
        "Press Enable Sync button",
        "Wait for synchronization completion",
        "Verify data availability on server",
        "Automatic backup to external hard drive"
    ],
    "parameters": {
        "sync_duration_survey": "few minutes",
        "sync_duration_features": "longer (due to photos)"
    },
    "implements_methods": ["M003"],
    "related_protocols": ["P003"],
    "expected_information_missing": [
        "Conflict resolution procedures",
        "Sync failure handling",
        "Backup verification procedures"
    ],
    "extraction_confidence": "high"
}

# P014: Final data preparation protocol
p014 = {
    "protocol_id": "P014",
    "protocol_text": "Post-fieldwork data cleaning protocol: streamline free-text fields, extract annotations to separate columns, using OpenRefine for ~2 hours of processing",
    "protocol_type": "data_processing",
    "protocol_status": "explicit",
    "location": {
        "section": "Post-processing - Final data preparation",
        "page": 17,
        "start_paragraph": 4,
        "end_paragraph": 4
    },
    "verbatim_quote": "While data exports were sufficient for mapping of results and day-to-day decision-making, some further data cleaning proved necessary before analysis. Fields that relied on free-text entry rather than controlled vocabularies needed streamlining. Annotations attached to particular values needed to be extracted into their own columns (in a CSV file). Since relatively few fields allowed free-text entry for anything aside from notes or descriptions and the consistent structure of annotations simplified their manipulation, data cleaning for the entire Perachora 2020 dataset took approximately two hours using OpenRefine.",
    "protocol_steps": [
        "Export data from FAIMS",
        "Open in OpenRefine",
        "Streamline free-text fields",
        "Extract annotations to separate columns",
        "Standardize terminology",
        "Export cleaned data"
    ],
    "parameters": {
        "cleaning_time": "approximately 2 hours",
        "software": "OpenRefine"
    },
    "implements_methods": ["M006"],
    "expected_information_missing": [
        "Specific OpenRefine operations used",
        "Annotation extraction rules",
        "Quality control checks"
    ],
    "extraction_confidence": "high"
}

# Add items to arrays
data["methods"].extend([m005, m006])
data["protocols"].extend([p007, p008, p009, p010, p011, p012, p013, p014])

# Update extraction metadata
data["extraction_timestamp"] = datetime.now(timezone.utc).isoformat()
data["extraction_notes"]["section_extracted"] = "Pass 3 RDMAP extraction continued: FAIMS workflows and post-processing (~4000 words, pages 7-18). Extracted 2 additional methods, 8 additional protocols. Total: 2 designs, 6 methods, 14 protocols. Liberal extraction maintained. Implementation details thoroughly documented. Next: Review for additional RDMAP in Results/Discussion."

# Save progress
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print(f"✓ Pass 3 workflows extraction complete")
print(f"  Research Designs: {len(data['research_designs'])}")
print(f"  Methods: {len(data['methods'])}")
print(f"  Protocols: {len(data['protocols'])}")
print(f"  Total RDMAP: {len(data['research_designs']) + len(data['methods']) + len(data['protocols'])}")
print(f"\nNext: Scan Results/Discussion for implicit RDMAP, then finalize Pass 3")
