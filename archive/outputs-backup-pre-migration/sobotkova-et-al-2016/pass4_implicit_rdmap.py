#!/usr/bin/env python3
"""
Pass 4 Implicit RDMAP Extraction for sobotkova-et-al-2016
Extracts mentioned-but-undocumented and inferred RDMAP items
"""

import json

# Load current extraction
with open('outputs/sobotkova-et-al-2016/extraction.json', 'r') as f:
    data = json.load(f)

# Implicit Research Designs
implicit_designs = [
    {
        'design_id': 'RD-IMP-001',
        'design_name': 'Comparative digital vs paper performance evaluation design',
        'trigger_text': [
            'these improvements (digital data) have come at a cost—namely, less efficient data collection in the field',
            'While we have yet to keep time-on-task records for either paper-based recording or FAIMS, project members universally reported that data entry using FAIMS took longer than using our previous analogue system',
            'Learning the capabilities of FAIMS software and engaging in the scoping and testing required by co-development all took more time before fieldwork than producing paper forms would have'
        ],
        'trigger_locations': [
            {'section': 'Theme 2: Trade-Offs', 'subsection': 'Legacy Features vs Performance', 'page': 48, 'context': 'VanValkenburgh quote on performance costs'},
            {'section': 'Theme 2: Trade-Offs', 'subsection': 'Legacy Features vs Performance', 'page': 48, 'context': 'Time-on-task measurement discussion'},
            {'section': 'Theme 1', 'subsection': 'The Payoff', 'page': 43, 'context': 'Discussion of time investment trade-offs'}
        ],
        'inference_reasoning': 'Paper systematically compares digital vs paper workflows throughout (Theme 1 costs/payouts, Theme 2 trade-offs, conclusions), with specific attention to performance, time-on-task, and efficiency. However, Introduction and Methods do not state comparative evaluation as design objective. This strategic positioning pervades the paper but is never explicitly articulated as a research design goal.',
        'page': 48,
        'source_location': 'Theme 2: Trade-Offs and Shared Lessons',
        'design_tier': 'overarching',
        'research_stage': 'conceptual',
        'justification': None,
        'enables_methods': ['M-IMP-001', 'M-IMP-002', 'M-IMP-005'],
        'design_status': 'implicit',
        'extraction_confidence': 'high',
        'implicit_metadata': {
            'basis': 'inferred_from_results',
            'transparency_gap': 'Comparative evaluation design objective not stated in Introduction or Methods. Unknown if systematic comparison was pre-planned research design or post-hoc narrative framing.',
            'assessability_impact': 'Cannot assess whether comparative data collection was systematic (planned) or opportunistic (narrative convenience). Affects interpretation of reported performance differences.',
            'reconstruction_confidence': 'high'
        }
    },
    {
        'design_id': 'RD-IMP-002',
        'design_name': 'Reproducibility and transparency enhancement design objective',
        'trigger_text': [
            'More continuous recordkeeping, including of "messy" work-in-progress, not only helps researchers at a later time better understand what they have excavated, but may contribute toward both making workflows more transparent and "openly exposing the process of research" (Kansa, Ch. 4.2), thus improving the reproducibility and professionalism of field research',
            'The ability to make this sort of data-driven, quantitative argument improves the explanatory power and reproducibility of archaeological research',
            'Only after digital datasets are published and researchers start reusing and combining them will the full potential and impact of digital methods be realised'
        ],
        'trigger_locations': [
            {'section': 'Theme 3: Digital Recording and Archaeological Interpretation', 'page': 52, 'context': 'Discussion of continuous recordkeeping benefits'},
            {'section': 'Theme 3: Digital Recording and Archaeological Interpretation', 'page': 53, 'context': 'Discussion of quantitative arguments'},
            {'section': 'Theme 3: Digital Recording and Archaeological Interpretation', 'page': 54, 'context': 'Discussion of data reuse and synthesis'}
        ],
        'inference_reasoning': 'Discussion and Conclusions position FAIMS as contribution to reproducibility, transparency, and data reuse ("reproducibility and professionalism of field research", "improves the explanatory power and reproducibility"). However, Introduction does not state reproducibility enhancement as design objective, and Methods do not describe systematic approaches to achieve this goal.',
        'page': 52,
        'source_location': 'Theme 3: Digital Recording and Archaeological Interpretation',
        'design_tier': 'overarching',
        'research_stage': 'conceptual',
        'justification': None,
        'enables_methods': ['M-IMP-003', 'M-IMP-004'],
        'design_status': 'implicit',
        'extraction_confidence': 'medium',
        'implicit_metadata': {
            'basis': 'inferred_from_results',
            'transparency_gap': 'Reproducibility enhancement design objective appears in Discussion but not stated in Introduction or Methods. Unknown if this was a priori design goal or emergent theme from case study analysis.',
            'assessability_impact': 'Cannot distinguish between planned reproducibility assessment and post-hoc thematic interpretation. Affects credibility of reproducibility claims.',
            'reconstruction_confidence': 'medium'
        }
    }
]

# Implicit Methods
implicit_methods = [
    {
        'method_id': 'M-IMP-001',
        'method_name': 'Performance monitoring and degradation detection methodology',
        'trigger_text': [
            'Performance degradation was barely perceptible during testing, which involved only a few records, but it worsened exponentially as the database grew',
            'More serious was the slowdown of the system halfway through its period of use. A record which initially took 20 minutes to input took over an hour due to slow syncing and updating',
            'Performance would degrade once approximately 3,000-6,000 records had been created'
        ],
        'trigger_locations': [
            {'section': 'Theme 2: Trade-Offs', 'subsection': 'Legacy Features vs Performance', 'page': 48, 'context': 'Discussion of context numbering performance'},
            {'section': 'Theme 2: Trade-Offs', 'subsection': 'Legacy Features vs Performance', 'page': 48, 'context': 'Fairbairn quote on slowdown'},
            {'section': 'Theme 2: Trade-Offs', 'subsection': 'Legacy Features vs Performance', 'page': 48, 'context': 'Discussion of record thresholds'}
        ],
        'inference_reasoning': 'Specific performance thresholds reported (3,000-6,000 records, 20 min → 60+ min input time, exponential degradation) imply systematic monitoring. However, monitoring methodology not documented: unknown how performance was measured, monitoring frequency, metrics used, or degradation detection criteria.',
        'page': 48,
        'source_location': 'Theme 2: Legacy Features vs Performance',
        'method_tier': 'primary',
        'implements_design': 'RD-IMP-001',
        'realized_through_protocols': [],
        'method_status': 'implicit',
        'extraction_confidence': 'high',
        'implicit_metadata': {
            'basis': 'inferred_from_results',
            'transparency_gap': 'Performance monitoring methodology undocumented. Unknown: measurement tools, monitoring schedule, performance metrics, threshold detection criteria, data collection procedures.',
            'assessability_impact': 'Cannot assess reliability of performance claims. Unknown whether monitoring was systematic or anecdotal. Critical for evaluating trade-off arguments.',
            'reconstruction_confidence': 'medium'
        }
    },
    {
        'method_id': 'M-IMP-002',
        'method_name': 'Time-on-task measurement methodology',
        'trigger_text': [
            'While we have yet to keep time-on-task records for either paper-based recording or FAIMS, project members universally reported that data entry using FAIMS took longer than using our previous analogue system'
        ],
        'trigger_locations': [
            {'section': 'Theme 2: Trade-Offs', 'subsection': 'Legacy Features vs Performance', 'page': 48, 'context': 'VanValkenburgh discussion of data entry time'}
        ],
        'inference_reasoning': 'Explicitly mentions planned time-on-task measurement ("we have yet to keep time-on-task records") but method not documented. Paper presents time comparisons elsewhere (Fairbairn: "2-3 hours vs several hundred hours") suggesting measurement occurred, but methodology never specified.',
        'page': 48,
        'source_location': 'Theme 2: Legacy Features vs Performance',
        'method_tier': 'primary',
        'implements_design': 'RD-IMP-001',
        'realized_through_protocols': [],
        'method_status': 'implicit',
        'extraction_confidence': 'high',
        'implicit_metadata': {
            'basis': 'mentioned_undocumented',
            'transparency_gap': 'Time-on-task measurement method not specified. Unknown: measurement protocol, data recording procedures, comparison baseline, participant selection.',
            'assessability_impact': 'Cannot assess validity of efficiency claims. Unknown whether time measurements were systematic, controlled, or anecdotal.',
            'reconstruction_confidence': 'low'
        }
    },
    {
        'method_id': 'M-IMP-003',
        'method_name': 'Post-fieldwork questionnaire methodology',
        'trigger_text': [
            'They took the time to complete post-project questionnaires',
            'The FAIMS team asked each of the project directors to reflect on the design, development, and deployment of their module'
        ],
        'trigger_locations': [
            {'section': 'Three Case Studies and Three Themes', 'page': 34, 'context': 'Description of data sources'},
            {'section': 'Theme 1', 'subsection': 'The Payoff', 'page': 41, 'context': 'Introduction to project director reflections'}
        ],
        'inference_reasoning': 'Post-project questionnaires mentioned as data source for case study quotations. However, questionnaire content, design, administration procedure, and analysis methodology not documented. Primary evidence source but method invisible.',
        'page': 34,
        'source_location': 'Three Case Studies and Three Themes of Observation',
        'method_tier': 'primary',
        'implements_design': 'RD-IMP-002',
        'realized_through_protocols': [],
        'method_status': 'implicit',
        'extraction_confidence': 'high',
        'implicit_metadata': {
            'basis': 'mentioned_undocumented',
            'transparency_gap': 'Questionnaire methodology undocumented. Unknown: question content, format (open/closed), administration timing, response validation, thematic analysis approach.',
            'assessability_impact': 'Cannot assess whether director quotations represent systematic data collection or selective reporting. Affects credibility of theme construction.',
            'reconstruction_confidence': 'low'
        }
    },
    {
        'method_id': 'M-IMP-004',
        'method_name': 'Interpretive impact assessment methodology',
        'trigger_text': [
            'When asked to assess the direct impact of the digital recording on their research, project directors first emphasised improvements in the quantity, quality, and availability of data'
        ],
        'trigger_locations': [
            {'section': 'Theme 3: Digital Recording and Archaeological Interpretation', 'page': 52, 'context': 'Introduction to impact assessment discussion'}
        ],
        'inference_reasoning': 'Project directors were "asked to assess" interpretive impact, implying structured assessment methodology. However, assessment framework, criteria, question design, and analysis approach not documented.',
        'page': 52,
        'source_location': 'Theme 3: Digital Recording and Archaeological Interpretation',
        'method_tier': 'primary',
        'implements_design': 'RD-IMP-002',
        'realized_through_protocols': [],
        'method_status': 'implicit',
        'extraction_confidence': 'medium',
        'implicit_metadata': {
            'basis': 'mentioned_undocumented',
            'transparency_gap': 'Impact assessment methodology not specified. Unknown: assessment framework, evaluation criteria, question design, response validation.',
            'assessability_impact': 'Cannot evaluate reliability of impact claims. Unknown whether assessment was guided or open-ended, systematic or impressionistic.',
            'reconstruction_confidence': 'low'
        }
    },
    {
        'method_id': 'M-IMP-005',
        'method_name': 'Cost-benefit quantification methodology',
        'trigger_text': [
            'The greatest gains in the FAIMS system were found after the excavation season was finished with post-processing of the data and checking taking 2–3 hours in comparison to several hundred hours for entry of the >300 context records generated in a typical season. This saving in paid RA time equates to c. AU$5,000–10,000 per annum',
            'The benefits to the excavation project in financial/labour terms are hugely significant, equating to a total of 1–1.5 days of handling time using FAIMS against 25–30 days when not in use per annum, in other words a 95% labour saving',
            'the tablets saved at least eight person-days of work'
        ],
        'trigger_locations': [
            {'section': 'Theme 1', 'subsection': 'The Payoff', 'page': 44, 'context': 'Fairbairn cost-benefit calculation'},
            {'section': 'Theme 1', 'subsection': 'The Payoff', 'page': 44, 'context': 'Fairbairn labour saving calculation'},
            {'section': 'Theme 1', 'subsection': 'The Payoff', 'page': 43, 'context': 'Thompson person-days saved'}
        ],
        'inference_reasoning': 'Precise cost-benefit calculations presented (95% labour saving, $5k-10k savings, 8 person-days) imply systematic quantification methodology. However, calculation methods, baseline measurements, cost accounting approaches, and verification procedures not documented.',
        'page': 44,
        'source_location': 'Theme 1: The Payoff',
        'method_tier': 'primary',
        'implements_design': 'RD-IMP-001',
        'realized_through_protocols': [],
        'method_status': 'implicit',
        'extraction_confidence': 'high',
        'implicit_metadata': {
            'basis': 'mentioned_undocumented',
            'transparency_gap': 'Cost-benefit quantification method not documented. Unknown: time measurement procedures, cost accounting methods, baseline calculation, person-hour valuation, comparison controls.',
            'assessability_impact': 'Cannot verify cost-benefit calculations. Unknown assumptions, measurement precision, or comparison validity. Critical for evaluating efficiency claims.',
            'reconstruction_confidence': 'medium'
        }
    }
]

# Implicit Protocols
implicit_protocols = [
    {
        'protocol_id': 'P-IMP-001',
        'protocol_name': 'Identifier seed assignment to devices protocol',
        'trigger_text': [
            'Assignment of seeds to individual devices, combined with server-side validation after all devices synchronise, ensures uniqueness of the critical portion of the overall identifier without performance degradation'
        ],
        'trigger_locations': [
            {'section': 'Theme 2: Trade-Offs', 'subsection': 'Legacy Features vs Performance', 'page': 49, 'context': 'Discussion of alternative context numbering approach'}
        ],
        'inference_reasoning': 'Seed assignment protocol mentioned as solution to performance problem. Procedure involves assigning seeds to devices before fieldwork, but assignment method, seed range calculation, device-seed mapping, and validation rules not specified.',
        'page': 49,
        'source_location': 'Theme 2: Legacy Features vs Performance',
        'protocol_tier': 'standard',
        'implements_method': None,
        'protocol_status': 'implicit',
        'extraction_confidence': 'medium',
        'implicit_metadata': {
            'basis': 'mentioned_undocumented',
            'transparency_gap': 'Seed assignment procedure not documented. Unknown: seed range calculation, device-seed mapping strategy, assignment timing, validation rules, conflict resolution.',
            'assessability_impact': 'Cannot assess reliability of seed-based identifier uniqueness claims. Critical for understanding scalability solution.',
            'reconstruction_confidence': 'medium'
        }
    },
    {
        'protocol_id': 'P-IMP-002',
        'protocol_name': 'Live module update deployment protocol',
        'trigger_text': [
            'Fairbairn\'s module had to be updated while live in the field. Live updates, designed for situations like this one (where a problem is identified after deployment) can be useful (cf. Fee, Ch. 2.1), but they pose risks of failure due to the lack of testing and should be avoided'
        ],
        'trigger_locations': [
            {'section': 'Theme 1', 'subsection': 'Testing and Training', 'page': 40, 'context': 'Discussion of live update necessity'}
        ],
        'inference_reasoning': 'Live update capability exists and was used ("Fairbairn\'s module had to be updated while live"). Feature is documented as risky but necessary. However, live update deployment protocol not specified: update distribution, device synchronisation, data migration, rollback procedures.',
        'page': 40,
        'source_location': 'Theme 1: Testing and Training',
        'protocol_tier': 'standard',
        'implements_method': None,
        'protocol_status': 'implicit',
        'extraction_confidence': 'high',
        'implicit_metadata': {
            'basis': 'mentioned_undocumented',
            'transparency_gap': 'Live update protocol not documented. Unknown: update distribution method, device coordination, data migration, rollback procedures, testing requirements.',
            'assessability_impact': 'Cannot assess update safety claims. Unknown whether live updates follow systematic protocol or ad-hoc procedures.',
            'reconstruction_confidence': 'low'
        }
    },
    {
        'protocol_id': 'P-IMP-003',
        'protocol_name': 'Communication archival and supplementary data protocol',
        'trigger_text': [
            'They took the time to complete post-project questionnaires, and also exchanged many emails and chat messages with the FAIMS team before, during, and after their fieldwork. These sources provide the quotations below; their complete, unedited communications with the FAIMS project are available via the digital supplement to this volume'
        ],
        'trigger_locations': [
            {'section': 'Three Case Studies and Three Themes', 'page': 34, 'context': 'Description of data sources and supplementary materials'}
        ],
        'inference_reasoning': 'Communications systematically archived as supplementary data ("complete, unedited communications...available via the digital supplement"). Implies archival protocol for collecting, organising, and publishing communications. However, archival procedures, selection criteria (if "complete, unedited" is accurate), and publication protocol not specified.',
        'page': 34,
        'source_location': 'Three Case Studies and Three Themes of Observation',
        'protocol_tier': 'standard',
        'implements_method': None,
        'protocol_status': 'implicit',
        'extraction_confidence': 'medium',
        'implicit_metadata': {
            'basis': 'mentioned_undocumented',
            'transparency_gap': 'Communication archival protocol not specified. Unknown: collection procedures, format standardisation, organisation scheme, de-identification procedures (if any), publication platform.',
            'assessability_impact': 'Cannot verify "complete, unedited" claim without archival protocol. Affects transparency and data reuse potential.',
            'reconstruction_confidence': 'medium'
        }
    },
    {
        'protocol_id': 'P-IMP-004',
        'protocol_name': 'Concatenated identifier export transformation protocol',
        'trigger_text': [
            'The five separate fields can be concatenated on export into a combined identifier to maintain the expected output'
        ],
        'trigger_locations': [
            {'section': 'Theme 2: Trade-Offs', 'subsection': 'Legacy Features vs Performance', 'page': 49, 'context': 'Discussion of alternative identifier approach'}
        ],
        'inference_reasoning': 'Export transformation mentioned as solution to performance problem ("concatenated on export"). Implies protocol for transforming five separate fields into single identifier during data export. However, concatenation rules, delimiter selection, field ordering, and export trigger not specified.',
        'page': 49,
        'source_location': 'Theme 2: Legacy Features vs Performance',
        'protocol_tier': 'standard',
        'implements_method': None,
        'protocol_status': 'implicit',
        'extraction_confidence': 'medium',
        'implicit_metadata': {
            'basis': 'mentioned_undocumented',
            'transparency_gap': 'Concatenation protocol not documented. Unknown: field ordering rules, delimiter selection, validation procedures, export trigger timing.',
            'assessability_impact': 'Cannot assess whether export maintains data integrity. Unknown if transformation is reversible or lossy.',
            'reconstruction_confidence': 'medium'
        }
    },
    {
        'protocol_id': 'P-IMP-005',
        'protocol_name': 'Server virtual machine installation protocol',
        'trigger_text': [
            'VanValkenburgh attempted to install a virtual server on his laptop. Unfortunately, the installation failed, and an online server was deployed instead'
        ],
        'trigger_locations': [
            {'section': 'Theme 2: Trade-Offs', 'subsection': 'Local vs Online Servers', 'page': 50, 'context': 'Description of VanValkenburgh server setup'}
        ],
        'inference_reasoning': 'VM installation attempted but failed. Implies installation protocol exists (since P006 documents Ubuntu installation for dedicated servers). However, VM-specific installation protocol, troubleshooting procedures, and failure diagnostics not documented.',
        'page': 50,
        'source_location': 'Theme 2: Local vs Online Servers',
        'protocol_tier': 'standard',
        'implements_method': None,
        'protocol_status': 'implicit',
        'extraction_confidence': 'low',
        'implicit_metadata': {
            'basis': 'mentioned_undocumented',
            'transparency_gap': 'VM installation protocol not documented. Unknown: VM software requirements, installation steps, configuration parameters, troubleshooting procedures, failure diagnostics.',
            'assessability_impact': 'Cannot assess whether VM installation is viable deployment option. Installation failure undocumented affects reproducibility.',
            'reconstruction_confidence': 'low'
        }
    }
]

# Add to data arrays
data['research_designs'].extend(implicit_designs)
data['methods'].extend(implicit_methods)
data['protocols'].extend(implicit_protocols)

# Update extraction notes
data['extraction_notes']['pass4_implicit_rdmap'] = {
    'completion_date': '2025-10-31T17:30:00Z',
    'sections_scanned': 'All 8 section groups from Pass 1',
    'scan_methodology': '4-pattern systematic scan (mentioned undocumented, inferred from results, tools without specs, strategic positioning) across Abstract, Introduction, FAIMS sections, Case Studies, Themes 1-3, Conclusions',
    'items_extracted': {
        'implicit_research_designs': 2,
        'implicit_methods': 5,
        'implicit_protocols': 5,
        'total_implicit': 12
    },
    'implicit_ratio': {
        'total_rdmap_after_pass3': 30,
        'total_rdmap_after_pass4': 42,
        'implicit_percentage': '28.6%',
        'note': 'Within target range of 20-40%'
    },
    'key_findings': [
        'Comparative digital vs paper evaluation pervades paper but never stated as design objective',
        'Multiple measurement methodologies (performance, time-on-task, cost-benefit) mentioned but not documented',
        'Post-project questionnaire is primary data source but methodology invisible',
        'Several operational protocols (seed assignment, live updates, concatenation) mentioned without specification'
    ]
}

# Save
with open('outputs/sobotkova-et-al-2016/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print("=" * 80)
print("PASS 4 IMPLICIT RDMAP EXTRACTION COMPLETE")
print("=" * 80)
print()
print(f"Implicit Items Extracted:")
print(f"  Research Designs: {len(implicit_designs)} (2)")
print(f"  Methods: {len(implicit_methods)} (5)")
print(f"  Protocols: {len(implicit_protocols)} (5)")
print(f"  Total Implicit: {len(implicit_designs) + len(implicit_methods) + len(implicit_protocols)} (12)")
print()
print(f"Total RDMAP After Pass 4:")
print(f"  Research Designs: {len(data['research_designs'])} (4 explicit + 2 implicit)")
print(f"  Methods: {len(data['methods'])} (8 explicit + 5 implicit)")
print(f"  Protocols: {len(data['protocols'])} (18 explicit + 5 implicit)")
print(f"  Total: {len(data['research_designs']) + len(data['methods']) + len(data['protocols'])} (42)")
print()
print(f"Implicit Ratio: 12/42 = 28.6% (within 20-40% target)")
print()
print("✓ Pass 4 complete - ready for Pass 5 (RDMAP rationalization)")
