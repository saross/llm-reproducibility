#!/usr/bin/env python3
"""
Pass 5: RDMAP Rationalization
Consolidates RDMAP items from 43 to ~36 (7 items reduction, 16.3%)

CONSERVATIVE CONSOLIDATION STRATEGY:
- Group M1: M007+M008 → M007 (abduction taxonomy + definition) = -1
- Group M3: M013+M020_implicit → M013 (template evaluation explicit+implicit) = -1
- Group P2: P006+P010 → P006 (methodological diversity + template adaptation) = -1
- Group P3: THREE consolidations:
  - P007+P016_implicit → P007 (OSF search explicit+implicit) = -1
  - P008+P009 → P008 (create registration + complete template sequence) = -1
  - P011+P017_implicit → P011 (TOP compliance + adaptation) = -1
- Group P4: P012+P013 → P012 (slow archaeology + built-in practices) = -1

Total reduction: 7 items (16.3%) → 36 RDMAP items after Pass 5
"""

import json
from datetime import datetime

# Load extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'r') as f:
    data = json.load(f)

print("=" * 80)
print("PASS 5: RDMAP RATIONALIZATION")
print("=" * 80)
print()
print(f"Starting totals:")
print(f"  Research Designs: {len(data['research_designs'])} items")
print(f"  Methods: {len(data['methods'])} items")
print(f"  Protocols: {len(data['protocols'])} items")
print(f"  TOTAL RDMAP: {len(data['research_designs']) + len(data['methods']) + len(data['protocols'])} items")
print()

# Create lookup dictionaries
methods_by_id = {method['id']: method for method in data['methods']}
protocols_by_id = {protocol['id']: protocol for protocol in data['protocols']}

# ============================================================================
# CONSOLIDATION FUNCTIONS
# ============================================================================

def consolidate_methods(kept_id, removed_ids, new_content, consolidation_note):
    """Consolidate multiple methods into one expanded method."""
    kept_method = methods_by_id[kept_id]

    kept_method['content'] = new_content
    kept_method['id'] = kept_id + '_consolidated' if '_consolidated' not in kept_id else kept_id

    kept_method['consolidation_metadata'] = {
        'consolidated_from': [kept_id] + removed_ids,
        'consolidation_rationale': consolidation_note,
        'original_count': 1 + len(removed_ids)
    }

    # Collect all pages if available
    all_pages = []
    if 'page_number' in kept_method and kept_method['page_number']:
        all_pages.append(kept_method['page_number'])
    for rid in removed_ids:
        if 'page_number' in methods_by_id[rid] and methods_by_id[rid]['page_number']:
            all_pages.append(methods_by_id[rid]['page_number'])
    if all_pages:
        kept_method['page_number'] = sorted(set([p for p in all_pages if p]))

    # Remove consolidated methods
    for rid in removed_ids:
        if rid in methods_by_id:
            data['methods'].remove(methods_by_id[rid])
            del methods_by_id[rid]

    return kept_method

def consolidate_protocols(kept_id, removed_ids, new_content, consolidation_note):
    """Consolidate multiple protocols into one expanded protocol."""
    kept_protocol = protocols_by_id[kept_id]

    kept_protocol['content'] = new_content
    kept_protocol['id'] = kept_id + '_consolidated' if '_consolidated' not in kept_id else kept_id

    kept_protocol['consolidation_metadata'] = {
        'consolidated_from': [kept_id] + removed_ids,
        'consolidation_rationale': consolidation_note,
        'original_count': 1 + len(removed_ids)
    }

    # Collect all pages
    all_pages = []
    if 'page_number' in kept_protocol and kept_protocol['page_number']:
        all_pages.append(kept_protocol['page_number'])
    for rid in removed_ids:
        if 'page_number' in protocols_by_id[rid] and protocols_by_id[rid]['page_number']:
            all_pages.append(protocols_by_id[rid]['page_number'])
    if all_pages:
        kept_protocol['page_number'] = sorted(set([p for p in all_pages if p]))

    # Consolidate procedure_steps if present
    if 'procedure_steps' in kept_protocol:
        all_steps = kept_protocol.get('procedure_steps', []).copy()
        for rid in removed_ids:
            if 'procedure_steps' in protocols_by_id[rid]:
                all_steps.extend(protocols_by_id[rid]['procedure_steps'])
        # Remove duplicates while preserving order
        seen = set()
        kept_protocol['procedure_steps'] = [s for s in all_steps if not (s in seen or seen.add(s))]

    # Remove consolidated protocols
    for rid in removed_ids:
        if rid in protocols_by_id:
            data['protocols'].remove(protocols_by_id[rid])
            del protocols_by_id[rid]

    return kept_protocol

# ============================================================================
# PERFORM CONSOLIDATIONS
# ============================================================================

consolidations_performed = []

# M1: Abduction taxonomy + definition (M007, M008 → M007)
print("Consolidating M007+M008: Abduction taxonomy and definition...")
consolidate_methods(
    'M007',
    ['M008'],
    "Methodological taxonomy characterising archaeology as incorporating deductive, inductive, and abductive modes of inference. Abductive inference—'inference to the best explanation'—involves generation, selection, and evaluation of candidate hypotheses based on explanatory power, and plays a central role in archaeological reasoning though seldom explicitly acknowledged",
    "M008 provides definitional detail for abduction, which is one component of M007's three-part taxonomy. Consolidating to avoid fragmenting the inferential taxonomy"
)
consolidations_performed.append("M007+M008 → M007 (abduction taxonomy+definition)")

# M3: Template evaluation explicit + implicit (M013, M020_implicit → M013)
print("Consolidating M013+M020_implicit: Template evaluation...")
consolidate_methods(
    'M013',
    ['M020_implicit'],
    "Template evaluation method comparing OSF's qualitative preregistration template structure and fields to assess suitability for archaeological adaptation. Evaluation criteria (how 'closer to' determined, what makes qualitative template better fit) not fully documented, limiting replicability of assessment",
    "M020_implicit describes the same template evaluation method but highlights that assessment criteria were not documented. Consolidating to present complete picture of method's transparency level"
)
consolidations_performed.append("M013+M020_implicit → M013 (template evaluation, noted implicit criteria)")

# P2: Methodological diversity + template adaptation (P006, P010 → P006)
print("Consolidating P006+P010: Preregistration across diversity + template adaptation...")
consolidate_protocols(
    'P006',
    ['P010'],
    "Protocol for preregistering research across methodological diversity continuum: articulate chosen position on quantitative-qualitative and idiographic-nomothetic axes, specify inferential mode (deductive/inductive/abductive), and adapt OSF qualitative template to archaeological contexts by documenting theoretical tradition, approach, hypotheses/expectations, data collection plans (what to record, how to record), workflows, and data models",
    "P010 provides specific implementation of P006's general principles via OSF template adaptation. Consolidating as P010 operationalises P006"
)
consolidations_performed.append("P006+P010 → P006 (diversity articulation + OSF template adaptation)")

# P3a: OSF search explicit + implicit (P007, P016_implicit → P007)
print("Consolidating P007+P016_implicit: OSF search procedure...")
consolidate_protocols(
    'P007',
    ['P016_implicit'],
    "Protocol for searching OSF for archaeological preregistrations: search for projects classified as 'archaeology', filter for registrations, manually review to classify type. Full search protocol partially documented (search term, filters stated; search date, false positive review procedures not stated), limiting exact replicability",
    "P016_implicit highlights that P007's search protocol was only partially documented. Consolidating to present complete transparency picture"
)
consolidations_performed.append("P007+P016_implicit → P007 (OSF search, noted implicit details)")

# P3b: Create registration + complete template (P008, P009 → P008)
print("Consolidating P008+P009: Creating and completing OSF preregistration...")
consolidate_protocols(
    'P008',
    ['P009'],
    "Protocol for creating archaeological preregistration on OSF: create project, select appropriate template (recommend qualitative template), complete required template fields (study information, research questions, hypotheses, data collection methods, analysis plan), submit registration before data collection, and link to eventual data deposit",
    "P008 and P009 form a sequential process: P008 describes creating registration, P009 describes completing the template. Consolidating as single end-to-end registration creation protocol"
)
consolidations_performed.append("P008+P009 → P008 (OSF registration creation + template completion sequence)")

# P3c: TOP compliance + adaptation (P011, P017_implicit → P011)
print("Consolidating P011+P017_implicit: TOP Guidelines compliance...")
consolidate_protocols(
    'P011',
    ['P017_implicit'],
    "Protocol for meeting Transparency and Openness Promotion (TOP) Guidelines Level 2 via preregistration: register research plan before data collection, obtain timestamped registration, report existence and location in manuscript, report all deviations, request TOP Level 2 badge. Adaptation of TOP criteria from experimental sciences to archaeological contexts (observational, excavation, survey, mixed methods) not fully documented, requiring archaeologists to interpret general criteria for their specific research types",
    "P017_implicit highlights that TOP criteria adaptation to archaeology was not documented. Consolidating to present complete compliance pathway with transparency caveat"
)
consolidations_performed.append("P011+P017_implicit → P011 (TOP compliance + archaeology adaptation note)")

# P4: Slow archaeology + built-in practices (P012, P013 → P012)
print("Consolidating P012+P013: Slow archaeology and built-in practices...")
consolidate_protocols(
    'P012',
    ['P013'],
    "Protocol for implementing 'slow archaeology' approach with 'built-in' rather than 'bolt-on' best practices: allocate dedicated time for research design planning, develop comprehensive documentation before fieldwork, integrate best practices into initial research design (not retrofitted after data collection), engage collaborators in design process, prioritise quality of planning over speed of execution, and use preregistration to formalise slow, integrated approach",
    "P012 and P013 are parallel formulations of the same principle: P012 frames as 'slow vs just-in-time', P013 frames as 'built-in vs bolt-on'. Consolidating as unified good practice implementation protocol"
)
consolidations_performed.append("P012+P013 → P012 (slow archaeology + built-in practices principle)")

print()
print("=" * 80)
print("CONSOLIDATIONS COMPLETED")
print("=" * 80)
for consolidation in consolidations_performed:
    print(f"  ✓ {consolidation}")
print()

# Update metadata
data['extraction_notes']['pass5_rdmap_rationalization'] = {
    'research_designs_before': 5,
    'methods_before': 20,
    'protocols_before': 18,
    'rdmap_before': 43,
    'research_designs_after': len(data['research_designs']),
    'methods_after': len(data['methods']),
    'protocols_after': len(data['protocols']),
    'rdmap_after': len(data['research_designs']) + len(data['methods']) + len(data['protocols']),
    'rdmap_reduced': 43 - (len(data['research_designs']) + len(data['methods']) + len(data['protocols'])),
    'reduction_percentage': round((43 - (len(data['research_designs']) + len(data['methods']) + len(data['protocols']))) / 43 * 100, 1),
    'consolidation_groups': len(consolidations_performed),
    'target_achieved': '6-9 items' if 6 <= (43 - (len(data['research_designs']) + len(data['methods']) + len(data['protocols']))) <= 9 else 'OUT OF RANGE'
}

# Save updated extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Final totals after Pass 5:")
print(f"  Research Designs: {len(data['research_designs'])} items (unchanged)")
print(f"  Methods: {len(data['methods'])} items (reduced from 20)")
print(f"  Protocols: {len(data['protocols'])} items (reduced from 18)")
print(f"  TOTAL RDMAP: {len(data['research_designs']) + len(data['methods']) + len(data['protocols'])} items")
print()
print(f"Reduction: {43 - (len(data['research_designs']) + len(data['methods']) + len(data['protocols']))} RDMAP items ({(43 - (len(data['research_designs']) + len(data['methods']) + len(data['protocols']))) / 43 * 100:.1f}%)")

if 6 <= (43 - (len(data['research_designs']) + len(data['methods']) + len(data['protocols']))) <= 9:
    print("✓ Target achieved: 6-9 items (14-21%)")
elif 34 <= (len(data['research_designs']) + len(data['methods']) + len(data['protocols'])) <= 37:
    print("✓ Overall target achieved: 34-37 total RDMAP items")
else:
    print(f"⚠ Check targets")
print()
print("✓ Pass 5 RDMAP rationalization complete - extraction.json updated")
print()
