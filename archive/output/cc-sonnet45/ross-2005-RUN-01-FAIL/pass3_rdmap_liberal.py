#!/usr/bin/env python3
"""
Pass 3: Liberal RDMAP (Research Design, Methods, Protocols) Extraction

Extracts research designs, methods, and protocols from Ross 2005.
Note: This is a literary/philological paper, so RDMAP items are thin compared
to empirical papers. The "methods" are primarily analytical approaches rather
than formal protocols.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

extraction_file = Path("extraction.json")

print("=" * 80)
print("PASS 3: LIBERAL RDMAP EXTRACTION")
print("=" * 80)
print()

# Read current extraction data
with open(extraction_file) as f:
    data = json.load(f)

# Initialize RDMAP arrays if they don't exist
if 'research_designs' not in data:
    data['research_designs'] = []
if 'methods' not in data:
    data['methods'] = []
if 'protocols' not in data:
    data['protocols'] = []

# ============================================================================
# RESEARCH DESIGNS
# ============================================================================

research_designs = [
    {
        "id": "RD001",
        "content": "Comparative textual analysis design: examining linguistic patterns across multiple epic texts (Iliad, Odyssey, Hesiod's Theogony, Homeric Hymns) to identify consistent patterns",
        "design_type": "comparative_literary_analysis",
        "page": 303,
        "verbatim_quote": "Three passages in the Iliad directly address the speaking of different languages (Il. 2.802–6, 2.867, 4.433–38; Od. 19.172–77, each discussed below)",
        "related_claims": ["C007", "C008", "C009"],
        "justification": "Comparative approach allows identification of patterns across epic tradition"
    },
    {
        "id": "RD002",
        "content": "Historical-linguistic contextualisation design: situating textual evidence within eighth-century BCE social and cultural context",
        "design_type": "historical_contextualisation",
        "page": 300,
        "verbatim_quote": "linguistic arrangements in the Iliad likely reflect the present of poet and audience around the time of stabilization, shaped by contemporary conditions, needs, and ideas",
        "related_claims": ["C001", "C002", "C014"],
        "justification": "Oral tradition preserves contemporary abstractions like identity more reliably than material culture"
    },
    {
        "id": "RD003",
        "content": "Oral tradition theory framework: using Nagy's stabilization theory and Vansina's oral tradition dynamics to date and interpret textual evidence",
        "design_type": "theoretical_framework",
        "page": 300,
        "verbatim_quote": "I have settled on these dates not only because the epics appear, linguistically, to be earlier than other Greek poetry, but especially for the reason Gregory Nagy proposed: that by about 700 b.c.e. the poems were so widely diffused that opportunities for recomposition would have been limited",
        "related_claims": ["C002", "C013", "C014"],
        "justification": "Oral tradition theory provides dating rationale and interpretive framework"
    }
]

# ============================================================================
# METHODS
# ============================================================================

methods = [
    {
        "id": "M001",
        "content": "Close reading of Greek epic passages mentioning language or speech diversity",
        "method_type": "textual_interpretation",
        "page": 303,
        "verbatim_quote": "Three passages in the Iliad directly address the speaking of different languages",
        "related_claims": ["C007", "C086", "C103"],
        "implementation_details": "Systematic identification and analysis of passages where linguistic diversity is explicitly mentioned"
    },
    {
        "id": "M002",
        "content": "Philological analysis of Greek terms (barbarophonos, glossa, phone, etc.)",
        "method_type": "philological_analysis",
        "page": 304,
        "verbatim_quote": "It is likely that the adjective βαρβαρόφωνος here does not denote merely non-Greek (or, more properly, non-Akhaian) speech, but instead carries the force of strange speech more generally",
        "related_claims": ["C092", "C093", "C094"],
        "implementation_details": "Analysis of semantic range and connotations of Greek vocabulary for language and speech"
    },
    {
        "id": "M003",
        "content": "Pattern identification across epic corpus: tracking when and where linguistic diversity is mentioned versus suppressed",
        "method_type": "pattern_analysis",
        "page": 313,
        "verbatim_quote": "While linguistic diversity is emphasized among the ἐπίκουροι defending Troy, it is entirely absent from the Akhaian force besieging the city",
        "related_claims": ["C233", "C235"],
        "implementation_details": "Systematic comparison of linguistic treatment of Akhaian vs. Trojan forces"
    },
    {
        "id": "M004",
        "content": "Scholarly debate engagement: positioning analysis within existing historiographical discussions",
        "method_type": "literature_review",
        "page": 301,
        "verbatim_quote": "Scholars who see Panhellenism as emerging primarily through opposition to a barbarian \"Other\" tend to downplay the extent of Panhellenism before the Persian Wars",
        "related_claims": ["C037", "C038", "C048"],
        "implementation_details": "Systematic review of scholarly positions on Panhellenism's emergence and dating"
    },
    {
        "id": "M005",
        "content": "Genre comparison: analyzing how linguistic diversity functions differently in epic versus hymnic traditions",
        "method_type": "genre_analysis",
        "page": 310,
        "verbatim_quote": "The passage from Hesiod deals not with diversity of human language, but instead focuses on differences between divine, human, and animal utterances",
        "related_claims": ["C156", "C162"],
        "implementation_details": "Comparison of divine-human dichotomy versus human linguistic diversity across genres"
    },
    {
        "id": "M006",
        "content": "Historical-linguistic contextualisation: interpreting textual evidence in light of eighth-century social conditions",
        "method_type": "historical_interpretation",
        "page": 307,
        "verbatim_quote": "Whether the Iliad drew upon a preexisting sense of nascent Panhellenism, or actively contributed to its construction (or some combination of both), Akhaian unity in the Iliad... reflected Panhellenic sentiments growing among eighth-century Greeks",
        "related_claims": ["C186", "C187", "C219"],
        "implementation_details": "Connecting textual patterns to historical processes of identity formation"
    },
    {
        "id": "M007",
        "content": "Comparative intra-textual analysis: examining consistency of linguistic treatment within and across texts",
        "method_type": "consistency_analysis",
        "page": 305,
        "verbatim_quote": "Notably, language is only mentioned once in the Catalogues of Iliad 2, in which Homer delineates and describes the opposing forces",
        "related_claims": ["C100"],
        "implementation_details": "Analyzing frequency and context of linguistic diversity references to assess importance"
    }
]

# ============================================================================
# PROTOCOLS
# ============================================================================

protocols = [
    {
        "id": "P001",
        "content": "Text selection criterion: focus on passages explicitly mentioning language, speech, or communication barriers",
        "protocol_type": "selection_criterion",
        "page": 303,
        "verbatim_quote": "Three passages in the Iliad directly address the speaking of different languages",
        "related_methods": ["M001"],
        "rationale": "Explicit mentions of linguistic diversity provide clearest evidence for linguistic attitudes"
    },
    {
        "id": "P002",
        "content": "Dating framework: accepting late 8th century (c. 700 BCE) as stabilization date for Iliad",
        "protocol_type": "dating_assumption",
        "page": 300,
        "verbatim_quote": "I believe, however, that the poems as we have them substantially preserve versions current during the late eighth century, with the Iliad perhaps somewhat earlier than the Odyssey",
        "related_methods": ["M006"],
        "rationale": "Based on Nagy's proliferation theory and linguistic evidence"
    },
    {
        "id": "P003",
        "content": "Translation approach: working from English translations for main analysis, using Greek terms selectively",
        "protocol_type": "linguistic_protocol",
        "page": 303,
        "verbatim_quote": "all translations by the author",
        "related_methods": ["M001", "M002"],
        "rationale": "Allows focus on semantic content while preserving access to Greek terminology for philological points"
    },
    {
        "id": "P004",
        "content": "Citation format: using standard scholarly format for ancient texts (author abbreviation, book.line numbers)",
        "protocol_type": "citation_convention",
        "page": 303,
        "verbatim_quote": "Il. 2.802–6, 2.867, 4.433–38; Od. 19.172–77",
        "related_methods": ["M001"],
        "rationale": "Follows disciplinary conventions for classical scholarship"
    },
    {
        "id": "P005",
        "content": "Comparative framework justification: examining Iliad alongside Odyssey, Hesiod, and Homeric Hymns",
        "protocol_type": "corpus_definition",
        "page": 307,
        "verbatim_quote": "The speaking of divergent languages is acknowledged once in the Odyssey, once in Hesiod's Theogony, and twice in the Homeric Hymns",
        "related_methods": ["M003", "M005"],
        "rationale": "Contextualises Iliad within broader early epic tradition to identify patterns and anomalies"
    },
    {
        "id": "P006",
        "content": "Scholarly positioning strategy: engaging with both 'oppositional' and 'aggregative' models of Panhellenism",
        "protocol_type": "methodological_positioning",
        "page": 301,
        "verbatim_quote": "Scholars who see Panhellenism as emerging primarily through opposition to a barbarian \"Other\" tend to downplay the extent of Panhellenism before the Persian Wars. Those who view Panhellenism as aggregated from disparate local and regional identities allow for its earlier appearance",
        "related_methods": ["M004"],
        "rationale": "Positions analysis between two major scholarly camps rather than fully adopting either"
    },
    {
        "id": "P007",
        "content": "Passage boundary determination: using natural narrative or thematic breaks rather than arbitrary line counts",
        "protocol_type": "text_segmentation",
        "page": 303,
        "verbatim_quote": "Il. 2.802–6... Il. 2.867... Il. 4.433–38",
        "related_methods": ["M001"],
        "rationale": "Preserves semantic and narrative coherence of analyzed passages"
    },
    {
        "id": "P008",
        "content": "Greek term transliteration: using standard scholarly transliteration conventions",
        "protocol_type": "transliteration_standard",
        "page": 303,
        "verbatim_quote": "ἐπίκουροι (allies or companions)",
        "related_methods": ["M002"],
        "rationale": "Allows precise reference to Greek terms while remaining accessible"
    },
    {
        "id": "P009",
        "content": "Evidence hierarchy: privileging direct textual evidence over scholarly interpretation",
        "protocol_type": "evidentiary_standard",
        "page": 313,
        "verbatim_quote": "Focusing on the Iliad itself, linguistic variation arises from two motivations",
        "related_methods": ["M001", "M003"],
        "rationale": "Primary texts provide direct evidence for eighth-century attitudes"
    },
    {
        "id": "P010",
        "content": "Oral tradition interpretation principle: abstractions like identity reflect contemporary period more than material culture",
        "protocol_type": "interpretive_principle",
        "page": 300,
        "verbatim_quote": "Oral tradition assimilates, forgets, and modifies different types of information at different rates. Physical things, be they objects or places, are much more durable in oral tradition... By contrast, so long as it is evolving through recomposition, oral tradition only tends to retain information about institutions and relationships so long as they are immediately relevant",
        "related_methods": ["M006"],
        "rationale": "Based on Vansina's oral tradition theory—abstractions update rapidly while material culture preserves longer"
    }
]

# Add items to extraction data
print(f"Adding {len(research_designs)} research designs...")
data['research_designs'].extend(research_designs)

print(f"Adding {len(methods)} methods...")
data['methods'].extend(methods)

print(f"Adding {len(protocols)} protocols...")
data['protocols'].extend(protocols)

# Update timestamp
data['extraction_timestamp'] = datetime.now(timezone.utc).isoformat()

# Write updated data
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print()
print("=" * 80)
print("PASS 3 COMPLETE")
print("=" * 80)
print()
print(f"RDMAP Totals:")
print(f"  Research Designs: {len(data['research_designs'])}")
print(f"  Methods: {len(data['methods'])}")
print(f"  Protocols: {len(data['protocols'])}")
print(f"  Total RDMAP items: {len(data['research_designs']) + len(data['methods']) + len(data['protocols'])}")
print()
print(f"Overall Totals:")
print(f"  Claims: {len(data['claims'])}")
print(f"  Evidence: {len(data['evidence'])}")
print(f"  Implicit Arguments: {len(data['implicit_arguments'])}")
print(f"  Research Designs: {len(data['research_designs'])}")
print(f"  Methods: {len(data['methods'])}")
print(f"  Protocols: {len(data['protocols'])}")
print(f"  Grand Total: {len(data['claims']) + len(data['evidence']) + len(data['implicit_arguments']) + len(data['research_designs']) + len(data['methods']) + len(data['protocols'])}")
print("=" * 80)
