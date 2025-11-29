#!/usr/bin/env python3
"""
Pass 3 RDMAP Extraction - Groups 2-8 (Case Studies, Themes, Conclusions)
Extracts deployment methods, testing protocols, and support procedures from case study sections
"""

import json

# Load current extraction
with open('outputs/sobotkova-et-al-2016/extraction.json', 'r') as f:
    data = json.load(f)

# Additional Methods from case studies
additional_methods = [
    {
        'method_id': 'M004',
        'method_name': 'Iterative requirements gathering through feedback loops',
        'verbatim_quote': 'Requirements gathering, planning, and development is a lengthy, iterative process that requires frequent communication, consultation, and feedback. ... Prior to the field season, the FAIMS leadership team met with several of its partners at UQ, including those involved in MEMSAP. ... Ultimately only three iterations of the excavation module and two iterations of the survey module were needed before a functional system could be deployed in the field.',
        'page': 36,
        'source_location': 'Theme 1: Scoping and Development',
        'method_tier': 'primary',
        'implements_design': 'RD002',
        'realized_through_protocols': ['P009', 'P010'],
        'method_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'method_id': 'M005',
        'method_name': 'Paper-to-digital workflow conversion method',
        'verbatim_quote': 'Converting from paper to digital workflows is an involved and time-consuming process. It requires making the implicit knowledge embedded in paper forms explicit. Digital forms are also more formalised and restrictive than paper forms; relationships between entities, controlled vocabularies, and other aspects of the data model must be defined and encoded',
        'page': 36,
        'source_location': 'Theme 1: Scoping and Development',
        'method_tier': 'primary',
        'implements_design': 'RD002',
        'realized_through_protocols': ['P011'],
        'method_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'method_id': 'M006',
        'method_name': 'Module reuse and rapid adaptation method',
        'verbatim_quote': 'The PAZC module also benefited from reusing the Boncuklu module with some modifications (emphasising the advantages of an open source, document-based customisation strategy: modules can be rapidly modified and redeployed, while each new module or modification improves the whole system). The FAIMS team translated the Boncuklu module into Spanish and customised it where required by editing the Boncuklu definition documents, a process that required less than one week after the requirements were fully specified.',
        'page': 36,
        'source_location': 'Theme 1: Scoping and Development',
        'method_tier': 'primary',
        'implements_design': 'RD004',
        'realized_through_protocols': ['P012'],
        'method_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'method_id': 'M007',
        'method_name': 'Pre-fieldwork testing and training method',
        'verbatim_quote': 'Software development requires that scoping, programming, and testing be finite, limited, and in balance with one another. ... Testing the module prior to fieldwork ensured it was technically functional, and allowed for communication of changes that would be hard done remotely',
        'page': 41,
        'source_location': 'Theme 1: Testing and Training',
        'method_tier': 'primary',
        'implements_design': 'RD002',
        'realized_through_protocols': ['P013', 'P014', 'P015'],
        'method_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'method_id': 'M008',
        'method_name': 'High-quality in-field support method',
        'verbatim_quote': 'Exceptional support is necessary when deploying new technology in the field, especially software that is purpose-built for the research community (Fisher et al. 2010). Only the availability of high-quality and timely support can provide the peace of mind necessary for archaeologists to risk moving from commercial software to new systems designed specifically for our domain.',
        'page': 45,
        'source_location': 'The Importance of High-Quality Support',
        'method_tier': 'primary',
        'implements_design': 'RD002',
        'realized_through_protocols': ['P016'],
        'method_status': 'explicit',
        'extraction_confidence': 'high'
    }
]

# Additional Protocols from case studies and themes
additional_protocols = [
    {
        'protocol_id': 'P009',
        'protocol_name': 'Multi-stakeholder requirements workshop',
        'verbatim_quote': 'Prior to the field season, the FAIMS leadership team met with several of its partners at UQ, including those involved in MEMSAP. ... Several hours were spent in discussions with all senior project personnel to ensure that all data types they wanted recorded were represented in the modules',
        'page': 36,
        'source_location': 'Theme 1: Scoping and Development',
        'protocol_tier': 'standard',
        'implements_method': 'M004',
        'protocol_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'protocol_id': 'P010',
        'protocol_name': 'Iterative prototype testing and refinement',
        'verbatim_quote': 'Ultimately only three iterations of the excavation module and two iterations of the survey module were needed before a functional system could be deployed in the field.',
        'page': 36,
        'source_location': 'Theme 1: Scoping and Development',
        'protocol_tier': 'standard',
        'implements_method': 'M004',
        'protocol_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'protocol_id': 'P011',
        'protocol_name': 'Recording system review and revision during conversion',
        'verbatim_quote': 'In the process of defining the parameters of the future FAIMS module I also got the opportunity to thoroughly review and refine the Boncuklu recording system to the last field and attribute, which identified some redundancies and allowed better definition of the attributes expected in the system.',
        'page': 36,
        'source_location': 'Theme 1: Scoping and Development',
        'protocol_tier': 'standard',
        'implements_method': 'M005',
        'protocol_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'protocol_id': 'P012',
        'protocol_name': 'Module translation and customisation from existing template',
        'verbatim_quote': 'The FAIMS team translated the Boncuklu module into Spanish and customised it where required by editing the Boncuklu definition documents, a process that required less than one week after the requirements were fully specified.',
        'page': 36,
        'source_location': 'Theme 1: Scoping and Development',
        'protocol_tier': 'standard',
        'implements_method': 'M006',
        'protocol_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'protocol_id': 'P013',
        'protocol_name': 'Authentic situation testing with real data',
        'verbatim_quote': 'Test your module and, if you are using multiple tablets, the server and its system extensively before you depart for the field with real data including every field and recording type you may use; bugs may be hard to find and you need to be sure the system works for your needs.',
        'page': 41,
        'source_location': 'Theme 1: Testing and Training',
        'protocol_tier': 'standard',
        'implements_method': 'M007',
        'protocol_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'protocol_id': 'P014',
        'protocol_name': 'Device-specific compatibility testing',
        'verbatim_quote': 'It therefore proved necessary to test the FAIMS mobile platform on each device.',
        'page': 41,
        'source_location': 'Theme 1: Testing and Training',
        'protocol_tier': 'standard',
        'implements_method': 'M007',
        'protocol_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'protocol_id': 'P015',
        'protocol_name': 'Project novice training for workflow validation',
        'verbatim_quote': 'Simulation of fieldwork is highly advised here. Or better yet, training a project novice in the use of the module is where potential misunderstandings (of the workflow) become apparent.',
        'page': 41,
        'source_location': 'Theme 1: Testing and Training',
        'protocol_tier': 'standard',
        'implements_method': 'M007',
        'protocol_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'protocol_id': 'P016',
        'protocol_name': 'In-field technical support and bug fixing',
        'verbatim_quote': 'Once identified and reproduced by the FAIMS team, bugs were quickly fixed, unclear workflows were explained, and alternative paths around design shortcomings were developed',
        'page': 45,
        'source_location': 'The Importance of High-Quality Support',
        'protocol_tier': 'standard',
        'implements_method': 'M008',
        'protocol_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'protocol_id': 'P017',
        'protocol_name': 'Data export to CSV for analysis',
        'verbatim_quote': 'He received his comma separated value (CSV; a standard spreadsheet-type format) data files and created an Access database from them',
        'page': 41,
        'source_location': 'Theme 1: The Payoff',
        'protocol_tier': 'standard',
        'implements_method': None,
        'protocol_status': 'explicit',
        'extraction_confidence': 'high'
    },
    {
        'protocol_id': 'P018',
        'protocol_name': 'Immediate post-field data checking',
        'verbatim_quote': 'His data was digital and ready for review promptly at the end of the season, which revealed problems that would otherwise have gone undetected until the paper forms were digitised—perhaps months later—when the errors would have been far more difficult to correct.',
        'page': 41,
        'source_location': 'Theme 1: The Payoff',
        'protocol_tier': 'standard',
        'implements_method': None,
        'protocol_status': 'explicit',
        'extraction_confidence': 'high'
    }
]

# Add to data arrays
data['methods'].extend(additional_methods)
data['protocols'].extend(additional_protocols)

# Update extraction notes for groups 2-8
data['extraction_notes']['pass3_rdmap_groups2to8'] = {
    'sections': 'Case Studies (3 projects: Boncuklu, MEMSAP, PAZC), Theme 1 (Costs/Payouts), Theme 2 (Trade-Offs), Theme 3 (Interpretive Benefits), Conclusions',
    'word_count': 'approximately 5400 words',
    'items_extracted': {
        'research_designs': 0,
        'methods': 5,
        'protocols': 10
    },
    'notes': 'Case study sections rich in deployment methods and protocols. Extracted iterative requirements gathering, testing procedures, support methods, and specific protocols for module development, testing, and deployment. No additional research designs - strategic decisions established in Group 1.'
}

data['extraction_notes']['pass3_complete'] = {
    'total_rdmap_items': len(data['research_designs']) + len(data['methods']) + len(data['protocols']),
    'breakdown': {
        'research_designs': len(data['research_designs']),
        'methods': len(data['methods']),
        'protocols': len(data['protocols'])
    },
    'extraction_approach': 'Liberal extraction following 8 section groups from Pass 1. Focused on all sections (not just methods) to capture research designs in introductory/positioning sections and methods/protocols in case study sections.',
    'completion_date': '2025-10-31T16:00:00Z'
}

# Save
with open('outputs/sobotkova-et-al-2016/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Groups 2-8 RDMAP extraction complete:")
print(f"  Additional Methods: {len(additional_methods)}")
print(f"  Additional Protocols: {len(additional_protocols)}")
print(f"\nPass 3 Complete - Total RDMAP:")
print(f"  Research Designs: {len(data['research_designs'])}")
print(f"  Methods: {len(data['methods'])}")
print(f"  Protocols: {len(data['protocols'])}")
print(f"  Total: {len(data['research_designs']) + len(data['methods']) + len(data['protocols'])}")
