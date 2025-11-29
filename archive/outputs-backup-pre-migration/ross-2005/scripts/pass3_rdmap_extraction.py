#!/usr/bin/env python3
"""
Pass 3: Liberal RDMAP Extraction

Target for literary/philological paper (40-50% over-extraction):
- Research Designs: 3-6 items (rationalize to 2-4)
- Methods: 9-14 items (rationalize to 6-10)
- Protocols: 14-24 items (rationalize to 10-18)
- Total: 26-44 items (rationalize to 16-28)

RDMAP hierarchy: Research Designs (WHY) → Methods (WHAT) → Protocols (HOW)
"""

import json
from pathlib import Path

extraction_path = Path("outputs/ross-2005/extraction.json")
with open(extraction_path, 'r', encoding='utf-8') as f:
    extraction = json.load(f)

# Research Designs (WHY) - Strategic approaches
research_designs = [
    {
        "id": "RD001",
        "content": "Comparative textual analysis design: examining linguistic patterns across multiple epic texts (Iliad, Odyssey, Hesiod's Theogony, Homeric Hymns) to identify consistent patterns",
        "design_type": "comparative_literary_analysis",
        "page": 303,
        "verbatim_quote": "Three passages in the Iliad directly address the speaking of different languages (Il. 2.802–6, 2.867, 4.433–38)",
        "related_claims": ["C006", "C007", "C008"],
        "justification": "Comparative approach allows identification of patterns across epic tradition"
    },
    {
        "id": "RD002",
        "content": "Historical-linguistic contextualisation design: situating textual evidence within eighth-century BCE social and cultural context",
        "design_type": "historical_contextualisation",
        "page": 300,
        "verbatim_quote": "linguistic arrangements in the Iliad likely reflect the present of poet and audience around the time of stabilization, shaped by contemporary conditions, needs, and ideas",
        "related_claims": ["C018", "C021", "C022"],
        "justification": "Oral tradition preserves contemporary abstractions like identity more reliably than material culture"
    },
    {
        "id": "RD003",
        "content": "Oral tradition theory framework: using Nagy's stabilization theory and Vansina's oral tradition dynamics to date and interpret textual evidence",
        "design_type": "theoretical_framework",
        "page": 300,
        "verbatim_quote": "I have settled on these dates not only because the epics appear, linguistically, to be earlier than other Greek poetry, but especially for the reason Gregory Nagy proposed: that by about 700 b.c.e. the poems were so widely diffused that opportunities for recomposition would have been limited",
        "related_claims": ["C018", "C020", "C023"],
        "justification": "Oral tradition theory provides dating rationale and interpretive framework"
    },
    {
        "id": "RD004",
        "content": "Pattern-based evidence design: treating textual absences (Akhaian linguistic uniformity) as equally significant evidence as presences (Trojan diversity)",
        "design_type": "absence_as_evidence",
        "page": 313,
        "verbatim_quote": "While linguistic diversity is emphasized among the ἐπίκουροι defending Troy, it is entirely absent from the Akhaian force besieging the city",
        "related_claims": ["C033", "C011"],
        "justification": "Poetic emphasis and suppression both carry meaning in careful analysis"
    }
]

# Methods (WHAT) - Analytical approaches
methods = [
    {
        "id": "M001",
        "content": "Close reading of Greek epic passages mentioning language or speech diversity",
        "method_type": "textual_interpretation",
        "page": 303,
        "verbatim_quote": "Three passages in the Iliad directly address the speaking of different languages",
        "implements_design": ["RD001"],
        "related_claims": ["C077"],
        "implementation_details": "Systematic identification and analysis of passages where linguistic diversity is explicitly mentioned"
    },
    {
        "id": "M002",
        "content": "Philological analysis of Greek terms (barbarophonos, glossa, phone, etc.)",
        "method_type": "philological_analysis",
        "page": 304,
        "verbatim_quote": "It is likely that the adjective βαρβαρόφωνος here does not denote merely non-Greek (or, more properly, non-Akhaian) speech, but instead carries the force of strange speech more generally",
        "implements_design": ["RD001"],
        "related_claims": ["C031", "C057"],
        "implementation_details": "Analysis of semantic range and connotations of Greek vocabulary for language and speech"
    },
    {
        "id": "M003",
        "content": "Pattern identification across epic corpus: tracking when and where linguistic diversity is mentioned versus suppressed",
        "method_type": "pattern_analysis",
        "page": 313,
        "verbatim_quote": "While linguistic diversity is emphasized among the ἐπίκουροι defending Troy, it is entirely absent from the Akhaian force besieging the city",
        "implements_design": ["RD001", "RD004"],
        "related_claims": ["C033"],
        "implementation_details": "Systematic comparison of linguistic treatment of Akhaian vs. Trojan forces"
    },
    {
        "id": "M004",
        "content": "Scholarly debate engagement: positioning analysis within existing historiographical discussions",
        "method_type": "literature_review",
        "page": 301,
        "verbatim_quote": "Scholars who see Panhellenism as emerging primarily through opposition to a barbarian \\\"Other\\\" tend to downplay the extent of Panhellenism before the Persian Wars",
        "implements_design": ["RD002"],
        "related_claims": ["C029"],
        "implementation_details": "Systematic review of scholarly positions on Panhellenism's emergence and dating"
    },
    {
        "id": "M005",
        "content": "Genre comparison: analyzing how linguistic diversity functions differently in epic versus hymnic traditions",
        "method_type": "genre_analysis",
        "page": 310,
        "verbatim_quote": "The passage from Hesiod deals not with diversity of human language, but instead focuses on differences between divine, human, and animal utterances",
        "implements_design": ["RD001"],
        "related_claims": ["C046"],
        "implementation_details": "Comparison of divine-human dichotomy versus human linguistic diversity across genres"
    },
    {
        "id": "M006",
        "content": "Historical-linguistic contextualisation: interpreting textual evidence in light of eighth-century social conditions",
        "method_type": "historical_interpretation",
        "page": 307,
        "verbatim_quote": "Whether the Iliad drew upon a preexisting sense of nascent Panhellenism, or actively contributed to its construction (or some combination of both), Akhaian unity in the Iliad... reflected Panhellenic sentiments growing among eighth-century Greeks",
        "implements_design": ["RD002"],
        "related_claims": ["C034", "C065"],
        "implementation_details": "Connecting textual patterns to historical processes of identity formation"
    },
    {
        "id": "M007",
        "content": "Comparative intra-textual analysis: examining consistency of linguistic treatment within and across texts",
        "method_type": "consistency_analysis",
        "page": 305,
        "verbatim_quote": "Notably, language is only mentioned once in the Catalogues of Iliad 2, in which Homer delineates and describes the opposing forces",
        "implements_design": ["RD001"],
        "related_claims": ["C032"],
        "implementation_details": "Analyzing frequency and context of linguistic diversity references to assess importance"
    },
    {
        "id": "M008",
        "content": "Interpretive priority method: privileging authorial intent and audience reception over modern theoretical frameworks",
        "method_type": "interpretive_stance",
        "page": 301,
        "inference_reasoning": "Ross consistently interprets passages in terms of what poet and eighth-century audience would have understood, rather than applying modern theoretical lenses. This methodological choice is enacted throughout but never explicitly defended.",
        "implements_design": ["RD002"],
        "related_claims": ["C022"],
        "implementation_details": "Implicit throughout analysis - focuses on contemporary meaning rather than later receptions or modern theoretical readings",
        "status": "implicit"
    },
    {
        "id": "M009",
        "content": "Selective evidence method: focusing on explicit linguistic diversity mentions rather than systematic analysis of all speech acts",
        "method_type": "evidence_selection",
        "page": 303,
        "inference_reasoning": "Ross examines only passages that explicitly mention linguistic diversity, not all instances of communication or speech. This selective approach is methodologically significant but not explicitly justified.",
        "implements_design": ["RD001"],
        "related_claims": ["C077"],
        "implementation_details": "Limits analysis to three Iliad passages plus comparative epic examples where language is explicitly thematized",
        "status": "implicit"
    },
    {
        "id": "M010",
        "content": "Contextual-narrative analysis: examining linguistic passages within their narrative contexts",
        "method_type": "narrative_analysis",
        "page": 309,
        "verbatim_quote": "Considering the context of the passage—a tale told to Penelope to hide Odysseus' real identity from her—perhaps Odysseus is focusing on the exotic",
        "implements_design": ["RD001"],
        "related_claims": ["C067", "C068"],
        "implementation_details": "Analyzes why linguistic diversity appears in specific narrative moments"
    }
]

# Protocols (HOW) - Specific procedures
protocols = [
    {
        "id": "P001",
        "content": "Text selection criterion: focus on passages explicitly mentioning language, speech, or communication barriers",
        "protocol_type": "selection_criterion",
        "page": 303,
        "verbatim_quote": "Three passages in the Iliad directly address the speaking of different languages",
        "implements_method": ["M001", "M009"],
        "rationale": "Explicit mentions of linguistic diversity provide clearest evidence for linguistic attitudes"
    },
    {
        "id": "P002",
        "content": "Dating framework: accepting late 8th century (c. 700 BCE) as stabilization date for Iliad",
        "protocol_type": "dating_assumption",
        "page": 300,
        "verbatim_quote": "I believe, however, that the poems as we have them substantially preserve versions current during the late eighth century, with the Iliad perhaps somewhat earlier than the Odyssey",
        "implements_method": ["M006"],
        "rationale": "Based on Nagy's proliferation theory and linguistic evidence"
    },
    {
        "id": "P003",
        "content": "Translation approach: working from English translations for main analysis, using Greek terms selectively",
        "protocol_type": "linguistic_protocol",
        "page": 303,
        "verbatim_quote": "all translations by the author",
        "implements_method": ["M001", "M002"],
        "rationale": "Allows focus on semantic content while preserving access to Greek terminology for philological points"
    },
    {
        "id": "P004",
        "content": "Citation format: using standard scholarly format for ancient texts (author abbreviation, book.line numbers)",
        "protocol_type": "citation_convention",
        "page": 303,
        "verbatim_quote": "Il. 2.802–6, 2.867, 4.433–38; Od. 19.172–77",
        "implements_method": ["M001"],
        "rationale": "Follows disciplinary conventions for classical scholarship"
    },
    {
        "id": "P005",
        "content": "Comparative framework justification: examining Iliad alongside Odyssey, Hesiod, and Homeric Hymns",
        "protocol_type": "corpus_definition",
        "page": 307,
        "verbatim_quote": "The speaking of divergent languages is acknowledged once in the Odyssey, once in Hesiod's Theogony, and twice in the Homeric Hymns",
        "implements_method": ["M003", "M005"],
        "rationale": "Contextualises Iliad within broader early epic tradition to identify patterns and anomalies"
    },
    {
        "id": "P006",
        "content": "Scholarly positioning strategy: engaging with both 'oppositional' and 'aggregative' models of Panhellenism",
        "protocol_type": "methodological_positioning",
        "page": 301,
        "verbatim_quote": "Scholars who see Panhellenism as emerging primarily through opposition to a barbarian \\\"Other\\\" tend to downplay the extent of Panhellenism before the Persian Wars. Those who view Panhellenism as aggregated from disparate local and regional identities allow for its earlier appearance",
        "implements_method": ["M004"],
        "rationale": "Positions analysis between two major scholarly camps rather than fully adopting either"
    },
    {
        "id": "P007",
        "content": "Passage boundary determination: using natural narrative or thematic breaks rather than arbitrary line counts",
        "protocol_type": "text_segmentation",
        "page": 303,
        "verbatim_quote": "Il. 2.802–6... Il. 2.867... Il. 4.433–38",
        "implements_method": ["M001"],
        "rationale": "Preserves semantic and narrative coherence of analyzed passages"
    },
    {
        "id": "P008",
        "content": "Greek term transliteration: using standard scholarly transliteration conventions",
        "protocol_type": "transliteration_standard",
        "page": 303,
        "verbatim_quote": "ἐπίκουροι (allies or companions)",
        "implements_method": ["M002"],
        "rationale": "Allows precise reference to Greek terms while remaining accessible"
    },
    {
        "id": "P009",
        "content": "Evidence hierarchy: privileging direct textual evidence over scholarly interpretation",
        "protocol_type": "evidentiary_standard",
        "page": 313,
        "verbatim_quote": "Focusing on the Iliad itself, linguistic variation arises from two motivations",
        "implements_method": ["M001", "M003"],
        "rationale": "Primary texts provide direct evidence for eighth-century attitudes"
    },
    {
        "id": "P010",
        "content": "Oral tradition interpretation principle: abstractions like identity reflect contemporary period more than material culture",
        "protocol_type": "interpretive_principle",
        "page": 300,
        "verbatim_quote": "Oral tradition assimilates, forgets, and modifies different types of information at different rates. Physical things, be they objects or places, are much more durable in oral tradition... By contrast, so long as it is evolving through recomposition, oral tradition only tends to retain information about institutions and relationships so long as they are immediately relevant",
        "implements_method": ["M006"],
        "rationale": "Based on Vansina's oral tradition theory—abstractions update rapidly while material culture preserves longer"
    },
    {
        "id": "P011",
        "content": "Assumption of textual stability: treating received texts as reliably representing c. 700 BCE versions",
        "protocol_type": "textual_assumption",
        "page": 300,
        "inference_reasoning": "Ross uses texts as evidence for eighth-century attitudes without discussing manuscript tradition, textual variants, or transmission issues. This assumes textual stability from composition to our received texts.",
        "implements_method": ["M001"],
        "rationale": "Necessary simplifying assumption for historical-linguistic analysis",
        "status": "implicit"
    },
    {
        "id": "P012",
        "content": "Monocausal interpretation avoidance: attributing patterns to multiple possible motivations rather than single causes",
        "protocol_type": "interpretive_caution",
        "page": 314,
        "inference_reasoning": "Ross explicitly identifies 'two motivations' for linguistic variation, signaling awareness that single-cause explanations are insufficient. This methodological caution is demonstrated but not explicitly theorized.",
        "implements_method": ["M003"],
        "rationale": "Reflects awareness of complexity in literary evidence",
        "status": "implicit"
    },
    {
        "id": "P013",
        "content": "Pattern frequency analysis: counting explicit linguistic diversity references across texts",
        "protocol_type": "quantitative_observation",
        "page": 307,
        "verbatim_quote": "The speaking of divergent languages is acknowledged once in the Odyssey, once in Hesiod's Theogony, and twice in the Homeric Hymns",
        "implements_method": ["M007"],
        "rationale": "Frequency of mentions indicates saliency and distribution of theme"
    }
]

# Add to extraction
extraction["research_designs"] = research_designs
extraction["methods"] = methods
extraction["protocols"] = protocols

# Update extraction notes
rdmap_total = len(research_designs) + len(methods) + len(protocols)
extraction["extraction_notes"].append(
    f"Pass 3 RDMAP extraction complete: Liberal extraction yielded {rdmap_total} items "
    f"({len(research_designs)} research_designs, {len(methods)} methods, {len(protocols)} protocols). "
    f"Target for literary paper: 26-44 items (achieved). "
    f"Includes 2 implicit methods (M008, M009) and 2 implicit protocols (P011, P012). "
    f"RDMAP hierarchy links established: protocols → methods → designs."
)

with open(extraction_path, 'w', encoding='utf-8') as f:
    json.dump(extraction, f, indent=2, ensure_ascii=False)

print(f"✓ Pass 3 RDMAP extraction complete")
print(f"  - Research Designs: {len(research_designs)} (target: 3-6)")
print(f"  - Methods: {len(methods)} (target: 9-14)")
print(f"  - Protocols: {len(protocols)} (target: 14-24)")
print(f"  - TOTAL RDMAP: {rdmap_total} (target: 26-44)")
print(f"  - Status: {'WITHIN TARGET' if 26 <= rdmap_total <= 44 else 'OUTSIDE TARGET'}")
print(f"\nRUNNING TOTAL after Pass 3:")
print(f"  - Evidence: {len(extraction['evidence'])}")
print(f"  - Claims: {len(extraction['claims'])}")
print(f"  - Implicit Arguments: {len(extraction['implicit_arguments'])}")
print(f"  - Research Designs: {len(extraction['research_designs'])}")
print(f"  - Methods: {len(extraction['methods'])}")
print(f"  - Protocols: {len(extraction['protocols'])}")
print(f"  - TOTAL: {len(extraction['evidence']) + len(extraction['claims']) + len(extraction['implicit_arguments']) + len(extraction['research_designs']) + len(extraction['methods']) + len(extraction['protocols'])} items")
