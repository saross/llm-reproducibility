#!/usr/bin/env python3
"""
Pass 2: Rationalization
Execute consolidations identified in pass2_rationalization_analysis.md
Target: 16.4% reduction (35 items: 213 → 178)
"""

import json
from typing import List, Dict, Any

# Load current extraction
with open('/home/shawn/Code/llm-reproducibility/outputs/connor-et-al-2013/extraction.json', 'r') as f:
    data = json.load(f)

# Helper function to update cross-references throughout the dataset
def update_cross_references(data: Dict, old_ids: List[str], keep_id: str, item_type: str):
    """
    Update all cross-references from old_ids to keep_id

    Args:
        data: Full extraction dataset
        old_ids: List of IDs being removed (will redirect to keep_id)
        keep_id: ID being kept (target for redirected references)
        item_type: 'evidence' or 'claims' - what type is being consolidated
    """
    all_old_ids = set(old_ids)

    # Update evidence items
    for e in data['evidence']:
        if 'supports_claims' in e:
            e['supports_claims'] = [
                keep_id if ref in all_old_ids else ref
                for ref in e['supports_claims']
            ]
            # Remove duplicates while preserving order
            seen = set()
            e['supports_claims'] = [x for x in e['supports_claims'] if not (x in seen or seen.add(x))]

    # Update claims items
    for c in data['claims']:
        if 'supported_by_evidence' in c:
            c['supported_by_evidence'] = [
                keep_id if ref in all_old_ids else ref
                for ref in c['supported_by_evidence']
            ]
            # Remove duplicates
            seen = set()
            c['supported_by_evidence'] = [x for x in c['supported_by_evidence'] if not (x in seen or seen.add(x))]

        if 'supported_by_claims' in c:
            c['supported_by_claims'] = [
                keep_id if ref in all_old_ids else ref
                for ref in c['supported_by_claims']
            ]
            # Remove duplicates
            seen = set()
            c['supported_by_claims'] = [x for x in c['supported_by_claims'] if not (x in seen or seen.add(x))]

    # Update methods items (for future RDMAP)
    for m in data.get('methods', []):
        if 'supported_by_evidence' in m:
            m['supported_by_evidence'] = [
                keep_id if ref in all_old_ids else ref
                for ref in m['supported_by_evidence']
            ]

# Helper function to find and update item by ID
def update_item_content(items: List[Dict], item_id: str, new_content: str, merge_sources: List[str] = None):
    """Update content of item with given ID"""
    for item in items:
        if item['id'] == item_id:
            item['content'] = new_content
            if merge_sources:
                item['rationalization_note'] = f"Consolidated from {', '.join(merge_sources)} in Pass 2"
            return True
    return False

# Helper function to remove items by ID
def remove_items(items: List[Dict], ids_to_remove: List[str]) -> List[Dict]:
    """Remove items with specified IDs"""
    return [item for item in items if item['id'] not in ids_to_remove]

# Track consolidations
consolidations_log = []

print("=" * 80)
print("PASS 2: RATIONALIZATION")
print("=" * 80)
print()
print(f"Starting items: {len(data['evidence']) + len(data['claims'])} (Evidence: {len(data['evidence'])}, Claims: {len(data['claims'])})")
print()

# ============================================================================
# CATEGORY 1: CHRONOLOGY REDUNDANCY (5 consolidations, -6 items)
# ============================================================================

# CONS-01: Duplicate radiocarbon dating descriptions (C061 + C090)
print("CONS-01: Merging C061 + C090 (radiocarbon dating strategy)")
update_item_content(
    data['claims'],
    'C061',
    "Comprehensive radiocarbon dating strategy employed using 13 AMS dates across Straldzha profiles, analysed using Bayesian age-depth modelling to establish chronological framework",
    ['C061', 'C090']
)
update_cross_references(data, ['C090'], 'C061', 'claims')
data['claims'] = remove_items(data['claims'], ['C090'])
consolidations_log.append({'id': 'CONS-01', 'kept': 'C061', 'removed': ['C090'], 'reduction': 1})

# CONS-02: Age-depth model construction workflow (E056 + E057 + C063)
print("CONS-02: Merging E056 + E057 + C063 (age-depth model construction)")
update_item_content(
    data['evidence'],
    'E056',
    "Age-depth model constructed using Markov chain Monte-Carlo analysis with Bayesian statistical approach in OxCal 4.1.7 based on IntCal09 calibration curve, extended by linear extrapolation to cover entire quarry section, providing robust chronological framework",
    ['E056', 'E057', 'C063']
)
update_cross_references(data, ['E057', 'C063'], 'E056', 'evidence')
data['evidence'] = remove_items(data['evidence'], ['E057'])
data['claims'] = remove_items(data['claims'], ['C063'])
consolidations_log.append({'id': 'CONS-02', 'kept': 'E056', 'removed': ['E057', 'C063'], 'reduction': 2})

# CONS-03: Canal core chronology methods (E058 + C064)
print("CONS-03: Merging E058 + C064 (canal core chronology)")
update_item_content(
    data['claims'],
    'C064',
    "Canal core chronology established through combination of sediment accumulation rates from upper part of record applied to upper metre and statistical correlation with quarry section",
    ['E058', 'C064']
)
update_cross_references(data, ['E058'], 'C064', 'claims')
data['evidence'] = remove_items(data['evidence'], ['E058'])
consolidations_log.append({'id': 'CONS-03', 'kept': 'C064', 'removed': ['E058'], 'reduction': 1})

# CONS-04: Age-depth model problems sequence (C091 + C093 + C094)
print("CONS-04: Merging C091 + C093 + C094 (age-depth model problems)")
update_item_content(
    data['claims'],
    'C091',
    "Low organic content and large error margins led to exclusion of three radiocarbon dates (particularly problematic sample Wk-32001) from age-depth model, improving agreement index from 12% to acceptable level (Amodel 60%)",
    ['C091', 'C093', 'C094']
)
update_cross_references(data, ['C093', 'C094'], 'C091', 'claims')
data['claims'] = remove_items(data['claims'], ['C093', 'C094'])
consolidations_log.append({'id': 'CONS-04', 'kept': 'C091', 'removed': ['C093', 'C094'], 'reduction': 2})

# CONS-05: Multiple dating materials (C062 + E063)
print("CONS-05: Merging C062 + E063 (dating materials)")
update_item_content(
    data['evidence'],
    'E063',
    "Thirteen AMS radiocarbon dates obtained from Rafter Radiocarbon Laboratory using diverse sample materials including pollen concentrates and organic residues to establish chronology across sequence",
    ['C062', 'E063']
)
update_cross_references(data, ['C062'], 'E063', 'evidence')
data['claims'] = remove_items(data['claims'], ['C062'])
consolidations_log.append({'id': 'CONS-05', 'kept': 'E063', 'removed': ['C062'], 'reduction': 1})

# ============================================================================
# CATEGORY 2: ANALYTICAL WORKFLOWS (4 consolidations, -14 items)
# ============================================================================

# CONS-06: Charcoal analysis workflow evidence (E034 + E035 + E036 + E038)
print("CONS-06: Merging E034 + E035 + E036 + E038 (charcoal analysis workflow)")
update_item_content(
    data['evidence'],
    'E034',
    "Microscopic charcoal (<200 µm) quantified on pollen slides using point-count method, and macroscopic charcoal (>250 µm) quantified using modification of Oregon sieving method (~2 cm³ sediment in 4.2% sodium hypochlorite for 24 hours, washed through 250 µm sieve, hand-sorted, photographed), with concentrations quantified using image analysis software (Scion Image 4.0.3.2) and converted to influx (CHAR) by normalising for deposition time",
    ['E034', 'E035', 'E036', 'E038']
)
update_cross_references(data, ['E035', 'E036', 'E038'], 'E034', 'evidence')
data['evidence'] = remove_items(data['evidence'], ['E035', 'E036', 'E038'])
consolidations_log.append({'id': 'CONS-06', 'kept': 'E034', 'removed': ['E035', 'E036', 'E038'], 'reduction': 3})

# CONS-07: Charcoal analysis workflow claims (C042 + C043 + C044 + C045 + C046)
print("CONS-07: Merging C042 + C043 + C044 + C045 + C046 (charcoal analysis rationale)")
update_item_content(
    data['claims'],
    'C042',
    "Size-based separation and quantification of microscopic (<200 µm) and macroscopic (>250 µm) charcoal using point-count and Oregon sieving methods with image analysis allows discrimination between local and regional fire signals, with conversion to influx rates accounting for variable sedimentation to provide temporal fire frequency estimates",
    ['C042', 'C043', 'C044', 'C045', 'C046']
)
update_cross_references(data, ['C043', 'C044', 'C045', 'C046'], 'C042', 'claims')
data['claims'] = remove_items(data['claims'], ['C043', 'C044', 'C045', 'C046'])
consolidations_log.append({'id': 'CONS-07', 'kept': 'C042', 'removed': ['C043', 'C044', 'C045', 'C046'], 'reduction': 4})

# CONS-08: Magnetic susceptibility analysis (E039 + E040 + C047 + C048)
print("CONS-08: Merging E039 + E040 + C047 + C048 (magnetic susceptibility)")
update_item_content(
    data['evidence'],
    'E039',
    "Dual-frequency magnetic susceptibility measurements run on Bartington MS2 meter following Dearing (1999) and Herries and Fisher (2010) protocols, with additional mineral magnetic analysis on Magnetic Measurements Variable Field Translation Balance (VFTB) including IRM acquisition curves, backfields, hysteresis loops, thermomagnetic curves to provide proxy for sediment source and environmental change through detailed characterisation of magnetic mineral assemblages",
    ['E039', 'E040', 'C047', 'C048']
)
update_cross_references(data, ['E040', 'C047', 'C048'], 'E039', 'evidence')
data['evidence'] = remove_items(data['evidence'], ['E040'])
data['claims'] = remove_items(data['claims'], ['C047', 'C048'])
consolidations_log.append({'id': 'CONS-08', 'kept': 'E039', 'removed': ['E040', 'C047', 'C048'], 'reduction': 3})

# CONS-09: Statistical analysis workflow (C053 + C055 + C056 + C057 + C058 + C059 + C060)
print("CONS-09: Merging C053 + C055 + C056 + C057 + C058 + C059 + C060 (statistical workflow)")
update_item_content(
    data['claims'],
    'C053',
    "Detrended Correspondence Analysis and cluster analysis in PC-Ord with taxonomic standardisation to remove methodological artefacts, combined with indicator species analysis (p=0.001 with Monte Carlo testing) and temporal plotting, provides objective statistical basis for comparing palaeovegetational patterns and identifying characteristic taxa across multiple sites while assessing synchronous vs. asynchronous vegetation changes across region",
    ['C053', 'C055', 'C056', 'C057', 'C058', 'C059', 'C060']
)
update_cross_references(data, ['C055', 'C056', 'C057', 'C058', 'C059', 'C060'], 'C053', 'claims')
data['claims'] = remove_items(data['claims'], ['C055', 'C056', 'C057', 'C058', 'C059', 'C060'])
consolidations_log.append({'id': 'CONS-09', 'kept': 'C053', 'removed': ['C055', 'C056', 'C057', 'C058', 'C059', 'C060'], 'reduction': 6})

# ============================================================================
# CATEGORY 3: POLLEN ANALYSIS PROCEDURES (2 consolidations, -3 items)
# ============================================================================

# CONS-10: Pollen preparation and counting (C039 + C040 + C041)
print("CONS-10: Merging C039 + C040 + C041 (pollen preparation)")
update_item_content(
    data['claims'],
    'C039',
    "Standard pollen preparation techniques with counting thresholds (minimum 200, average 600 pollen grains) and inclusion of non-pollen palynomorphs ensure comparability with other palynological studies and provide statistically robust basis for percentage calculations with complementary environmental indicators beyond pollen evidence",
    ['C039', 'C040', 'C041']
)
update_cross_references(data, ['C040', 'C041'], 'C039', 'claims')
data['claims'] = remove_items(data['claims'], ['C040', 'C041'])
consolidations_log.append({'id': 'CONS-10', 'kept': 'C039', 'removed': ['C040', 'C041'], 'reduction': 2})

# CONS-11: Pollen data presentation (C052 + E067)
print("CONS-11: Merging C052 + E067 (pollen data presentation)")
update_item_content(
    data['evidence'],
    'E067',
    "Cluster analysis used to group pollen record into five palaeovegetation phases with names based on assumed ecological preferences of indicator taxa, visualised using Psimpoll software for standardised presentation of pollen stratigraphic data",
    ['C052', 'E067']
)
update_cross_references(data, ['C052'], 'E067', 'evidence')
data['claims'] = remove_items(data['claims'], ['C052'])
consolidations_log.append({'id': 'CONS-11', 'kept': 'E067', 'removed': ['C052'], 'reduction': 1})

# ============================================================================
# CATEGORY 4: CITATION CONSOLIDATIONS (3 consolidations, -5 items)
# ============================================================================

# CONS-12: Regional deforestation timing synthesis (C024 + C025 + C026)
print("CONS-12: Merging C024 + C025 + C026 (deforestation timing)")
update_item_content(
    data['claims'],
    'C024',
    "Previous terrestrial pollen studies conclude that Thracian Plain's oak forests were destroyed prior to ~4000 cal. a BP, supported by marine sediments from Black Sea showing early-mid Holocene Quercus expansion, though timing of deforestation is unclear from marine records with some showing abrupt Quercus decline around 6000 cal. a BP and others showing no decline at all",
    ['C024', 'C025', 'C026']
)
update_cross_references(data, ['C025', 'C026'], 'C024', 'claims')
data['claims'] = remove_items(data['claims'], ['C025', 'C026'])
consolidations_log.append({'id': 'CONS-12', 'kept': 'C024', 'removed': ['C025', 'C026'], 'reduction': 2})

# CONS-13: Agricultural transition debate (C003 + C008 + C010)
print("CONS-13: Merging C003 + C008 + C010 (agricultural transition debate)")
update_item_content(
    data['claims'],
    'C008',
    "Degree to which environmental change influenced Neolithic transition remains topic of vast scientific debate, with previous studies invoking rapid sea-level and climatic changes to explain timing of agricultural expansion, though precise timing of arrival of Neolithic agriculture in SE Europe remains contentious",
    ['C003', 'C008', 'C010']
)
update_cross_references(data, ['C003', 'C010'], 'C008', 'claims')
data['claims'] = remove_items(data['claims'], ['C003', 'C010'])
consolidations_log.append({'id': 'CONS-13', 'kept': 'C008', 'removed': ['C003', 'C010'], 'reduction': 2})

# CONS-14: Major environmental changes (C006 + C009)
print("CONS-14: Merging C006 + C009 (environmental changes and impacts)")
update_item_content(
    data['claims'],
    'C009',
    "Climate changes during late Pleistocene and early Holocene triggered major migrations of species and biomes in temperate latitudes, with rapid environmental changes like 8200 cal. a BP climatic event and Black Sea flood having major impacts on Neolithic transition",
    ['C006', 'C009']
)
update_cross_references(data, ['C006'], 'C009', 'claims')
data['claims'] = remove_items(data['claims'], ['C006'])
consolidations_log.append({'id': 'CONS-14', 'kept': 'C009', 'removed': ['C006'], 'reduction': 1})

# ============================================================================
# CATEGORY 5: SITE CONTEXT (2 consolidations, -3 items)
# ============================================================================

# CONS-15: Site significance (C028 + C035 + C036)
print("CONS-15: Merging C028 + C035 + C036 (site significance)")
update_item_content(
    data['claims'],
    'C028',
    "Straldzha Mire provides appropriate site for examining regional palaeoenvironmental history of Thracian Plain through deep sedimentary sequence suitable for long-term reconstruction, with proximity to previous pollen study site allowing cross-validation of late Holocene results",
    ['C028', 'C035', 'C036']
)
update_cross_references(data, ['C035', 'C036'], 'C028', 'claims')
data['claims'] = remove_items(data['claims'], ['C035', 'C036'])
consolidations_log.append({'id': 'CONS-15', 'kept': 'C028', 'removed': ['C035', 'C036'], 'reduction': 2})

# CONS-16: Sampling strategy (C037 + C038)
print("CONS-16: Merging C037 + C038 (sampling strategy)")
update_item_content(
    data['claims'],
    'C037',
    "Variable sampling intervals provide higher resolution for recent sediments while maintaining coverage of entire sequence, with immediate sealing and refrigeration to preserve sample integrity for palynological analysis",
    ['C037', 'C038']
)
update_cross_references(data, ['C038'], 'C037', 'claims')
data['claims'] = remove_items(data['claims'], ['C038'])
consolidations_log.append({'id': 'CONS-16', 'kept': 'C037', 'removed': ['C038'], 'reduction': 1})

# ============================================================================
# CATEGORY 6: ADDITIONAL (4 consolidations, -4 items)
# ============================================================================

# CONS-17: Thracian Plain agricultural corridor (C012 + C018)
print("CONS-17: Merging C012 + C018 (Thracian Plain corridor)")
update_item_content(
    data['claims'],
    'C012',
    "Geographical factors mean Thracian Plain is one of probable corridors through which agriculture made its way into rest of Europe from Western Asia and was home to Europe's earliest metalworking cultures",
    ['C012', 'C018']
)
update_cross_references(data, ['C018'], 'C012', 'claims')
data['claims'] = remove_items(data['claims'], ['C018'])
consolidations_log.append({'id': 'CONS-17', 'kept': 'C012', 'removed': ['C018'], 'reduction': 1})

# CONS-18: Cold steppe pollen assemblage (E068 + E069)
print("CONS-18: Merging E068 + E069 (cold steppe assemblage)")
update_item_content(
    data['evidence'],
    'E068',
    "Cold steppe phase assemblage dominated by herbaceous taxa (>90%), including Poaceae, Artemisia, Chenopodiaceae, and Cyperaceae, with limited woody components (Salix, Juniperus, Betula) typically <5%",
    ['E068', 'E069']
)
update_cross_references(data, ['E069'], 'E068', 'evidence')
data['evidence'] = remove_items(data['evidence'], ['E069'])
consolidations_log.append({'id': 'CONS-18', 'kept': 'E068', 'removed': ['E069'], 'reduction': 1})

# CONS-19: Oak forest dominance timing (C080 + C083)
print("CONS-19: Merging C080 + C083 (oak dominance)")
update_item_content(
    data['claims'],
    'C083',
    "Oak woods phase beginning ~8900 cal. a BP marked by Quercus becoming dominant arboreal taxon (30-52% of total pollen sum), transitioning from forest-steppe as thermophilous deciduous trees expanded and grassland indicators declined",
    ['C080', 'C083']
)
update_cross_references(data, ['C080'], 'C083', 'claims')
data['claims'] = remove_items(data['claims'], ['C080'])
consolidations_log.append({'id': 'CONS-19', 'kept': 'C083', 'removed': ['C080'], 'reduction': 1})

# CONS-20: Multiple core strategy (C050 + E044)
print("CONS-20: Merging C050 + E044 (multiple core strategy)")
update_item_content(
    data['evidence'],
    'E044',
    "Six cores obtained using 5 cm diameter gouge auger along two perpendicular transects to address potential truncation or disturbance in upper part of quarry section",
    ['C050', 'E044']
)
update_cross_references(data, ['C050'], 'E044', 'evidence')
data['claims'] = remove_items(data['claims'], ['C050'])
consolidations_log.append({'id': 'CONS-20', 'kept': 'E044', 'removed': ['C050'], 'reduction': 1})

# ============================================================================
# FINALIZATION
# ============================================================================

# Calculate final statistics
final_evidence = len(data['evidence'])
final_claims = len(data['claims'])
final_total = final_evidence + final_claims

# Calculate reduction
initial_total = 213
reduction = initial_total - final_total
reduction_pct = (reduction / initial_total) * 100

# Update extraction notes
data['extraction_notes']['pass2_rationalization'] = {
    "completion_date": "2025-10-30",
    "approach": "Conservative rationalization focusing on sequential workflows, redundant methodological descriptions, and citation clusters",
    "consolidations_performed": len(consolidations_log),
    "items_before": {
        "evidence": 106,
        "claims": 107,
        "total": 213
    },
    "items_after": {
        "evidence": final_evidence,
        "claims": final_claims,
        "total": final_total
    },
    "reduction": {
        "items": reduction,
        "percentage": round(reduction_pct, 1)
    },
    "target_met": f"Target 10-20% reduction: {round(reduction_pct, 1)}% ({'✓' if 10 <= reduction_pct <= 20 else '✗'})",
    "consolidation_categories": {
        "chronology_redundancy": 5,
        "analytical_workflows": 4,
        "pollen_analysis": 2,
        "citations": 3,
        "site_context": 2,
        "additional": 4
    },
    "notes": "Preserved distinct temporal phases, proxy types, and spatial contexts while consolidating sequential procedural steps and redundant methodological descriptions. All cross-references updated programmatically."
}

# Save updated extraction
with open('/home/shawn/Code/llm-reproducibility/outputs/connor-et-al-2013/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print()
print("=" * 80)
print("PASS 2 RATIONALIZATION COMPLETE!")
print("=" * 80)
print()
print(f"Initial Items: {initial_total} (Evidence: 106, Claims: 107)")
print(f"Final Items: {final_total} (Evidence: {final_evidence}, Claims: {final_claims})")
print()
print(f"Reduction: {reduction} items ({round(reduction_pct, 1)}%)")
print(f"Target Achievement: {'✓ Within 10-20% target range' if 10 <= reduction_pct <= 20 else '✗ Outside target range'}")
print()
print(f"Consolidations Performed: {len(consolidations_log)}")
print()
print("Category Summary:")
print(f"  Chronology Redundancy: 5 consolidations")
print(f"  Analytical Workflows: 4 consolidations")
print(f"  Pollen Analysis: 2 consolidations")
print(f"  Citations: 3 consolidations")
print(f"  Site Context: 2 consolidations")
print(f"  Additional: 4 consolidations")
print()
print("Ready for Pass 3: Liberal RDMAP extraction")
