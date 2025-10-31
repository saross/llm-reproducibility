#!/usr/bin/env python3
"""
Pass 5 RDMAP Rationalization for sobotkova-et-al-2016
Consolidates RDMAP items following assessment compatibility test
"""

import json
from datetime import datetime

# Load current extraction
with open('outputs/sobotkova-et-al-2016/extraction.json', 'r') as f:
    data = json.load(f)

print("=" * 80)
print("PASS 5 RDMAP RATIONALIZATION")
print("=" * 80)
print()

items_before = len(data['research_designs']) + len(data['methods']) + len(data['protocols'])
print(f"Before rationalization: {items_before} RDMAP items")
print(f"  Research Designs: {len(data['research_designs'])}")
print(f"  Methods: {len(data['methods'])}")
print(f"  Protocols: {len(data['protocols'])}")
print()

# Consolidation: M-IMP-003 + M-IMP-004 → M-IMP-003
# Find the two methods
m_imp_003 = next(m for m in data['methods'] if m['method_id'] == 'M-IMP-003')
m_imp_004 = next(m for m in data['methods'] if m['method_id'] == 'M-IMP-004')

# Create consolidated method
consolidated_method = {
    'method_id': 'M-IMP-003',
    'method_name': 'Post-fieldwork assessment methodology combining questionnaires and impact evaluation',
    'trigger_text': m_imp_003['trigger_text'] + m_imp_004['trigger_text'],
    'trigger_locations': m_imp_003['trigger_locations'] + m_imp_004['trigger_locations'],
    'inference_reasoning': 'Post-project questionnaires explicitly mentioned as data source. Directors "asked to assess the direct impact" implies structured assessment methodology. These are unified: questionnaire IS the vehicle for collecting impact assessments. Both are post-fieldwork evaluation approaches that would be assessed together as comprehensive project evaluation methodology. Consolidated because assessment methodology and questionnaire methodology are aspects of the same evaluation approach.',
    'page': 34,
    'source_location': 'Three Case Studies and Three Themes / Theme 3',
    'method_tier': 'primary',
    'implements_design': 'RD-IMP-002',
    'realized_through_protocols': [],
    'method_status': 'implicit',
    'extraction_confidence': 'high',
    'implicit_metadata': {
        'basis': 'mentioned_undocumented',
        'transparency_gap': 'Post-fieldwork assessment methodology undocumented. Unknown: questionnaire content/format (open/closed), impact assessment framework, evaluation criteria, question design, response validation, thematic analysis approach.',
        'assessability_impact': 'Cannot assess whether director responses represent systematic data collection or selective reporting. Unknown whether impact assessment was guided or open-ended, systematic or impressionistic. Affects credibility of theme construction and impact claims.',
        'reconstruction_confidence': 'low'
    },
    'consolidation_metadata': {
        'consolidated_from': ['P4_M-IMP-003', 'P4_M-IMP-004'],
        'consolidation_type': 'validation_chain',
        'information_preserved': 'complete',
        'rationale': 'Assessment compatibility test: Would assess TOGETHER. Questionnaire methodology and impact assessment methodology are aspects of the same post-fieldwork evaluation approach. Questionnaire is the instrument for collecting impact assessments. Both mentioned but undocumented as part of unified case study evaluation methodology.'
    }
}

# Remove M-IMP-004 and replace M-IMP-003
data['methods'] = [m for m in data['methods'] if m['method_id'] != 'M-IMP-004']
for i, m in enumerate(data['methods']):
    if m['method_id'] == 'M-IMP-003':
        data['methods'][i] = consolidated_method
        break

print("Consolidation performed:")
print("  M-IMP-003 + M-IMP-004 → M-IMP-003")
print("  Type: validation_chain")
print("  Rationale: Questionnaire is vehicle for impact assessment - unified evaluation method")
print()

# Update extraction notes
items_after = len(data['research_designs']) + len(data['methods']) + len(data['protocols'])

data['extraction_notes']['pass5_rdmap_rationalization'] = {
    'completion_date': datetime.now().isoformat(),
    'items_before': items_before,
    'items_after': items_after,
    'reduction_count': items_before - items_after,
    'reduction_percentage': round((items_before - items_after) / items_before * 100, 1),
    'consolidations_performed': 1,
    'consolidation_detail': {
        'methods': 1,
        'protocols': 0,
        'research_designs': 0
    },
    'tier_corrections': 0,
    'boundary_corrections': 0,
    'rationale': 'Conservative RDMAP rationalization using assessment compatibility test. Only 1 consolidation identified (M-IMP-003 + M-IMP-004 assessment methods). Low reduction (2.4%) appropriate because: (1) Pass 3 explicit extraction was well-bounded, not over-extracted; (2) Pass 4 implicit extraction was conservative (28.6%); (3) RDMAP items represent genuine procedural diversity in co-development study; (4) Assessment compatibility test shows most items need independent assessment. Research Designs (6): All address distinct strategic concerns. Methods (13→12): Only post-fieldwork assessment methods unified. Protocols (23): No consolidation - operational specifications require granularity for replication assessment.'
}

# Save
with open('outputs/sobotkova-et-al-2016/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"After rationalization: {items_after} RDMAP items")
print(f"  Research Designs: {len(data['research_designs'])}")
print(f"  Methods: {len(data['methods'])}")
print(f"  Protocols: {len(data['protocols'])}")
print(f"  Reduction: {items_before - items_after} items ({round((items_before - items_after) / items_before * 100, 1)}%)")
print()
print("✓ Pass 5 complete - ready for Pass 6 (Validation)")
