#!/usr/bin/env python3
"""
Pass 3 RDMAP Extraction - Group 1 (Abstract, Introduction, FAIMS Project sections)
Pages 5-23, ~972 words
Focuses on research designs and high-level methods described in introductory sections
"""

import json

# Load current extraction
with open('outputs/sobotkova-et-al-2016/extraction.json', 'r') as f:
    data = json.load(f)

# Initialize RDMAP arrays if not present
if 'research_designs' not in data:
    data['research_designs'] = []
if 'methods' not in data:
    data['methods'] = []
if 'protocols' not in data:
    data['protocols'] = []

# Research Designs - Strategic decisions about WHY
research_designs = [
    {
        'design_id': 'RD001',
        'design_name': 'Generalised platform positioning strategy',
        'verbatim_quote': 'FAIMS lies near the middle of this spectrum. Compared to a general-purpose DBMS, FAIMS is "generalised" in the sense it has no predetermined data schemas or user interface, instead offering a degree of control over data structures and forms similar to DBMSes like Microsoft Access or FileMaker Pro. It is not general-purpose, however, in that it has been purpose built to perform well under difficult field conditions and includes functionality specifically requested by archaeologists',
        'page': 29,
        'source_location': 'Between Off-the-Shelf and Bespoke Software section',
        'design_tier': 'overarching',
        'research_stage': 'conceptual',
        'justification': 'Position FAIMS between commercial DBMS and bespoke applications, offering customisation with field-optimised capabilities. Balances accessibility with archaeological requirements.',
        'enables_methods': [],  # Will link after methods created
        'design_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'design_id': 'RD002',
        'design_name': 'Co-development partnership design',
        'verbatim_quote': 'Such co-development involves a partnership between field archaeologists and a software development team. This partnership can ease the transitions from paper to digital fieldwork, illuminate the advantages digital approaches offer, and ensure that software is fit-to-purpose.',
        'page': 14,
        'source_location': 'Introduction section',
        'design_tier': 'overarching',
        'research_stage': 'conceptual',
        'justification': 'Collaborative development between archaeologists and developers to ensure software meets actual field requirements. Analogous to Open Context data sharing model.',
        'enables_methods': [],
        'design_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'design_id': 'RD003',
        'design_name': 'Iterative infrastructure funding sustainability model',
        'verbatim_quote': 'The sustainability plan of the FAIMS project involves iterative applications for research infrastructure funding, primarily through the ARC LIEF program. LIEFs are matching grants that require partner organisations (primarily universities) to contribute approximately one-third to one-half of the total budget.',
        'page': 14,
        'source_location': 'The FAIMS Project section',
        'design_tier': 'overarching',
        'research_stage': 'conceptual',
        'justification': 'Financial sustainability through recurring infrastructure grants plus service fees (5% currently, targeting 25% in 5 years). Enables professional development team while making software accessible.',
        'enables_methods': [],
        'design_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'design_id': 'RD004',
        'design_name': 'Shared core library cost distribution design',
        'verbatim_quote': 'Because the core FAIMS software is common to all deployments, however, the fixed costs of development and maintenance can be shared across many users, projects, and institutions. Improvements that benefit all users can be made incrementally as resources come available.',
        'page': 29,
        'source_location': 'Between Off-the-Shelf and Bespoke Software section',
        'design_tier': 'overarching',
        'research_stage': 'conceptual',
        'justification': 'Share development/maintenance costs across multiple deployments by maintaining common core software. Enables incremental improvements and attracts sustainable user base.',
        'enables_methods': ['M001'],
        'design_status': 'explicit',
        'extraction_confidence': 'high'
    }
]

# Methods - Tactical approaches about WHAT
methods = [
    {
        'method_id': 'M001',
        'method_name': 'Module customisation via definition documents',
        'verbatim_quote': 'Such a "deployment" involves tailoring the core software by creating or modifying "definition documents," primarily Extensible Markup Language (XML) files, which produce customised data collection "modules"',
        'page': 25,
        'source_location': 'The FAIMS Mobile Platform section',
        'method_tier': 'primary',
        'implements_design': 'RD004',
        'realized_through_protocols': ['P001', 'P002', 'P003', 'P004'],
        'method_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'method_id': 'M002',
        'method_name': 'GitHub-based module reuse and improvement',
        'verbatim_quote': 'Software or other text documents stored on GitHub can be downloaded, edited, copied, and adapted at will. ... This module was duplicated ("forked") and modified to meet the needs of each project. ... It also allowed for the most useful changes to each of the derivative modules to be incorporated ("pulled") back into the original "deluxe excavation" module.',
        'page': 25,
        'source_location': 'The FAIMS Mobile Platform section',
        'method_tier': 'primary',
        'implements_design': 'RD004',
        'realized_through_protocols': ['P005'],
        'method_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'method_id': 'M003',
        'method_name': 'Scoping-coding-QA software deployment workflow',
        'verbatim_quote': 'The FAIMS approach ... has us treat each deployment as an authentic, miniature software development project that requires proper "scoping" (requirements gathering, software design, and development planning), coding, and "quality assurance" (testing at each step of development to ensure that software works and is fit-to-purpose).',
        'page': 29,
        'source_location': 'The Nature of Co-Development section',
        'method_tier': 'primary',
        'implements_design': 'RD002',
        'realized_through_protocols': [],
        'method_status': 'explicit',
        'extraction_confidence': 'high'
    }
]

# Protocols - Operational procedures about HOW
protocols = [
    {
        'protocol_id': 'P001',
        'protocol_name': 'Module reuse as-is',
        'verbatim_quote': 'Reuse an existing module as-is, which requires only downloading the application from Google Play and selecting the desired module from a list',
        'page': 25,
        'source_location': 'Customising and Deploying section',
        'protocol_tier': 'standard',
        'implements_method': 'M001',
        'protocol_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'protocol_id': 'P002',
        'protocol_name': 'Heurist GUI-based module generation',
        'verbatim_quote': 'Use Heurist (an online data service), which provides a graphic user interface for the generation of definition documents (suitable for relatively simple modules)',
        'page': 25,
        'source_location': 'Customising and Deploying section',
        'protocol_tier': 'standard',
        'implements_method': 'M001',
        'protocol_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'protocol_id': 'P003',
        'protocol_name': 'Simplified XML generator for module definition',
        'verbatim_quote': 'Use a simplified module generator, which requires writing a single XML file that generates definition documents (suitable for modules of moderate complexity)',
        'page': 25,
        'source_location': 'Customising and Deploying section',
        'protocol_tier': 'standard',
        'implements_method': 'M001',
        'protocol_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'protocol_id': 'P004',
        'protocol_name': 'Direct definition document editing',
        'verbatim_quote': 'Modify an existing module, or create a new one, by editing the definition documents directly, which requires proficiency with XML and BeanShell (a scripting language).',
        'page': 25,
        'source_location': 'Customising and Deploying section',
        'protocol_tier': 'standard',
        'implements_method': 'M001',
        'protocol_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'protocol_id': 'P005',
        'protocol_name': 'Module forking and pull request workflow',
        'verbatim_quote': 'This module was duplicated ("forked") and modified to meet the needs of each project. ... it also allowed for the most useful changes to each of the derivative modules to be incorporated ("pulled") back into the original "deluxe excavation" module.',
        'page': 25,
        'source_location': 'The FAIMS Mobile Platform section',
        'protocol_tier': 'standard',
        'implements_method': 'M002',
        'protocol_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'protocol_id': 'P006',
        'protocol_name': 'Server installation via Ubuntu commands',
        'verbatim_quote': 'Users can establish a local or online server themselves by installing Linux (specifically, the most recent Long Term Service release of Ubuntu) and executing a few commands to download and install the FAIMS server software.',
        'page': 25,
        'source_location': 'Customising and Deploying section',
        'protocol_tier': 'standard',
        'implements_method': None,
        'protocol_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'protocol_id': 'P007',
        'protocol_name': 'Pre-configured server procurement',
        'verbatim_quote': 'For users who want to purchase a pre-configured server, the FAIMS project has established relationships with vendors in Australia and the United States who can provide and support local or online servers. Purchasing a pre-configured local server with all necessary hardware costs AUD $1,700–$3,500 from one of these vendors (excluding tablets). Alternatively, an online or local server can be leased for approximately AUD $150–$200 per month.',
        'page': 25,
        'source_location': 'Customising and Deploying section',
        'protocol_tier': 'standard',
        'implements_method': None,
        'protocol_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'protocol_id': 'P008',
        'protocol_name': 'Customisation service cost estimation',
        'verbatim_quote': 'When a project hires the FAIMS team to adapt an existing module or develop a new one, this service generally costs approximately AUD $1,500–$15,000 per season for the mobile platform, depending on the complexity and novelty of the recording system required.',
        'page': 25,
        'source_location': 'Customising and Deploying section',
        'protocol_tier': 'standard',
        'implements_method': None,
        'protocol_status': 'explicit',
        'extraction_confidence': 'high'
    }
]

# Add to data arrays
data['research_designs'].extend(research_designs)
data['methods'].extend(methods)
data['protocols'].extend(protocols)

# Update extraction notes
if 'extraction_notes' not in data:
    data['extraction_notes'] = {}

data['extraction_notes']['pass3_rdmap_group1'] = {
    'sections': 'Abstract, Introduction, FAIMS Project, FAIMS Mobile Platform, Customising and Deploying, Between Off-the-Shelf, Nature of Co-Development',
    'word_count': 'approximately 4800 words',
    'items_extracted': {
        'research_designs': 4,
        'methods': 3,
        'protocols': 8
    },
    'notes': 'Foundational sections describing FAIMS positioning, co-development design, sustainability model, and customisation methods. Strong research design presence in introductory/positioning sections.'
}

# Save
with open('outputs/sobotkova-et-al-2016/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Group 1 RDMAP extraction complete:")
print(f"  Research Designs: {len(research_designs)}")
print(f"  Methods: {len(methods)}")
print(f"  Protocols: {len(protocols)}")
print(f"  Total: {len(research_designs) + len(methods) + len(protocols)}")
