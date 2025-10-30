#!/usr/bin/env python3
"""
Pass 1: Liberal Claims & Evidence Extraction
Section 6: Odyssey Evidence - Krete Passage
Pages 307-309, ~900 words

Extracts claims, evidence, and implicit arguments from the analysis of
Odyssey 19.172-77 and Nagy's related discussion.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

extraction_file = Path("extraction.json")

print("=" * 80)
print("PASS 1 - SECTION 6: Odyssey Evidence")
print("Pages 307-309: Krete Passage")
print("=" * 80)
print()

# Read current extraction data
with open(extraction_file) as f:
    data = json.load(f)

# Section 6 extraction: Odyssey and Nagy's analysis
section_claims = [
    {
        "id": "C129",
        "content": "Nagy presents evidence that the unity of the Akhaians in the Iliad resonated with the sentiments of eighth-century Greeks",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 307,
        "verbatim_quote": "Further evidence that the unity of the Akhaians in the Iliad resonated with the sentiments of eighth-century Greeks is presented by Nagy",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C130",
        "content": "Nagy explores the relationship between the artistry of the poem and the culture that produced it",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 307,
        "verbatim_quote": "Nagy, who also explores the relationship between the artistry of the poem and the culture that produced it",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C131",
        "content": "The fusion of the Delian and Pythian traditions in the Homeric Hymn to Apollo reflects the unification of not just artistic, but also socio-religious traditions",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 307,
        "verbatim_quote": "In his analysis of the Homeric Hymn to Apollo, Nagy believes that the fusion of the Delian and Pythian traditions in this hymn reflects the unification of not just artistic, but also socio-religious traditions",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C132",
        "content": "The fusion of traditions in the Hymn to Apollo brings together not only divergent stories, but also diverse audiences",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 307,
        "verbatim_quote": "bringing together not only divergent stories, but also diverse audiences",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C133",
        "content": "Proliferation of the Homeric epics by the late eighth century BCE indicates an approximate date for the stabilisation of the oral tradition",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 307,
        "verbatim_quote": "just as Nagy argues that proliferation of the Homeric epics by the late eighth century b.c.e. indicates an approximate date for the stabilization of the oral tradition",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C134",
        "content": "The broad acceptance of the epics among the Greeks is evidence for an emerging 'intercultural synthesis' that contributed to a nascent sense of Panhellenism",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 307,
        "verbatim_quote": "he also cites the broad acceptance of the epics among the Greeks as evidence—along with the rise of institutions such as the Olympic Games and Delphic Oracle—for an emerging \"intercultural synthesis\" that contributed to a nascent sense of Panhellenism",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C135",
        "content": "The image of the Akhaians presented in the Iliad was apparently an acceptable part of the eighth-century intercultural synthesis",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 307,
        "verbatim_quote": "The image of the Akhaians—who were certainly viewed as Greek, even if the Trojans had not yet become stand-ins for the generic, undifferentiated barbarian—presented in the Iliad was apparently an acceptable part of this intercultural synthesis",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C136",
        "content": "Whether the Iliad drew upon a preexisting sense of nascent Panhellenism, or actively contributed to its construction (or some combination of both), Akhaian unity in the Iliad reflected Panhellenic sentiments growing among eighth-century Greeks",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 307,
        "verbatim_quote": "Whether the Iliad drew upon a preexisting sense of nascent Panhellenism, or actively contributed to its construction (or some combination of both), Akhaian unity in the Iliad, manifested in such features as a shared common language, reflected Panhellenic sentiments growing among eighth-century Greeks",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA016"]
    },
    {
        "id": "C137",
        "content": "Only three passages from the Iliad deal with Akhaian linguistic unity or the linguistic diversity of the Trojan epikouroi",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 307,
        "verbatim_quote": "Admittedly, only three passages from the Iliad deal with Akhaian linguistic unity or the linguistic diversity of the Trojan ἐπίκουροι",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C138",
        "content": "The nature and importance of the three Iliad language passages can be better assessed by interpreting them in the context of the surviving body of early Greek epic poetry",
        "claim_type": "methodological_positioning",
        "claim_status": "explicit",
        "page": 307,
        "verbatim_quote": "The nature and importance of these passages can be better assessed by interpreting them in the context of the surviving body of early Greek epic poetry",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA017"]
    },
    {
        "id": "C139",
        "content": "The speaking of divergent languages is acknowledged once in the Odyssey, once in Hesiod's Theogony, and twice in the Homeric Hymns",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 307,
        "verbatim_quote": "The speaking of divergent languages is acknowledged once in the Odyssey, once in Hesiod's Theogony, and twice in the Homeric Hymns",
        "supporting_evidence": ["E006"],
        "related_implicit_arguments": []
    },
    {
        "id": "C140",
        "content": "The only recognition of linguistic diversity within Akhaian lands found in early literature occurs in the Odyssey",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 308,
        "verbatim_quote": "The only recognition of linguistic diversity within Akhaian lands found in early literature occurs in the Odyssey",
        "supporting_evidence": ["E006"],
        "related_implicit_arguments": []
    },
    {
        "id": "C141",
        "content": "Taking on the persona of Aithon, Odysseus observes that different tongues are mingled on Krete: Akhaioi, Eteokretes, Kudones, Doriees, and Pelasgoi",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 308,
        "verbatim_quote": "Taking on the persona of Aithon, a fallen aristocrat from Krete, Odysseus observes of the people of the island... And different tongues are mingled there",
        "supporting_evidence": ["E006"],
        "related_implicit_arguments": []
    },
    {
        "id": "C142",
        "content": "The languages spoken on Krete are described as memigmenē ('mingled' or 'mixed') using the same verb employed in Iliad 4.438",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 308,
        "verbatim_quote": "The languages spoken on the island are simply described as μεμιγμένη (\"mingled\" or \"mixed\") using the same verb (μίγνυμι) employed in Iliad 4.438",
        "supporting_evidence": ["E006"],
        "related_implicit_arguments": []
    },
    {
        "id": "C143",
        "content": "The phrase 'but there are different tongues' (ἄλλη δ᾽ ἄλλων γλῶσσα) is repeated from Iliad 2.804, where it is used to communicate the diversity of the Trojan epikouroi",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 308,
        "verbatim_quote": "Likewise, the phrase ἄλλη δ᾽ ἄλλων γλῶσσα is repeated from Iliad 2.804, where it is used to communicate the diversity of the Trojan ἐπίκουροι",
        "supporting_evidence": ["E006"],
        "related_implicit_arguments": []
    },
    {
        "id": "C144",
        "content": "Unlike in other passages concerning linguistic diversity in Homer, in the Krete passage it remains unclear how language corresponds to place of origin",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 308,
        "verbatim_quote": "Unlike in the other passages concerning linguistic diversity in Homer, however, here it remains unclear how language corresponds to place of origin",
        "supporting_evidence": ["E006"],
        "related_implicit_arguments": []
    },
    {
        "id": "C145",
        "content": "Particular linguistic groups on Krete are not located within a single region in the way that the barbarophonoi Karians are linked to a single homeland",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 308,
        "verbatim_quote": "Nor are particular linguistic groups located within a single region of Krete in the way that the βαρβαρόφωνοι Karians are linked to a single homeland, Karia",
        "supporting_evidence": ["E006"],
        "related_implicit_arguments": []
    },
    {
        "id": "C146",
        "content": "After noting the mixing of languages on Krete, the poet provides a list of 'ethnic' names—a marker of identity less commonly employed in the Iliad than place of origin or membership in a military contingent",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 309,
        "verbatim_quote": "Instead, after noting the mixing of languages on Krete, the poet provides a list of \"ethnic\" names—a marker of identity less commonly employed in the Iliad than place of origin or membership in a military contingent",
        "supporting_evidence": ["E006"],
        "related_implicit_arguments": []
    },
    {
        "id": "C147",
        "content": "Groups traditionally considered Greek (Akhaians and Dorians) are not distinguished from those who were not (Eteocretans, Kudones, Pelasgians) in the Krete passage",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 309,
        "verbatim_quote": "Groups traditionally considered Greek (Akhaians and Dorians) are not, however, distinguished from those who were not (Eteocretans, Kudones, Pelasgians)",
        "supporting_evidence": ["E006"],
        "related_implicit_arguments": []
    },
    {
        "id": "C148",
        "content": "No rigid dichotomy emerges between Akhaians and non-Akhaians in the Krete passage",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 309,
        "verbatim_quote": "again, no rigid dichotomy emerges between Akhaians and non-Akhaians",
        "supporting_evidence": ["E006"],
        "related_implicit_arguments": []
    },
    {
        "id": "C149",
        "content": "The reliance on language and 'ethnicity' in the Krete passage marks it out as unusual",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 309,
        "verbatim_quote": "The reliance on language and \"ethnicity\" in this passage mark it out as unusual",
        "supporting_evidence": ["E006"],
        "related_implicit_arguments": []
    },
    {
        "id": "C150",
        "content": "Considering the context—a tale told to Penelope to hide Odysseus' real identity—perhaps Odysseus is focusing on the exotic as he does in his other travel stories",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 309,
        "verbatim_quote": "Considering the context of the passage—a tale told to Penelope to hide Odysseus' real identity from her—perhaps Odysseus is focusing on the exotic as he does in his other travel stories",
        "supporting_evidence": ["E006"],
        "related_implicit_arguments": ["IA018"]
    },
    {
        "id": "C151",
        "content": "Ethno-linguistic diversity would make Krete strange and distant, perhaps even 'foreign', despite the fact that the island is ruled by an Akhaian king and sent a contingent to the Trojan War",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 309,
        "verbatim_quote": "In this case, ethno-linguistic diversity would make Krete strange and distant, perhaps even \"foreign,\" despite the fact that the island is ruled by an Akhaian king and sent a contingent to the Trojan War",
        "supporting_evidence": ["E006"],
        "related_implicit_arguments": ["IA018"]
    },
    {
        "id": "C152",
        "content": "Such a use of linguistic diversity to generate the impression of alterity recalls the description of the remote and barbarophonos Karians in the Trojan Catalogue",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 309,
        "verbatim_quote": "Such a use of linguistic diversity to generate the impression of alterity recalls the description of the remote and βαρβαρόφωνος Karians in the Trojan Catalogue",
        "supporting_evidence": ["E004", "E006"],
        "related_implicit_arguments": []
    },
    {
        "id": "C153",
        "content": "Although the linkage between ethnicity and language in Odyssey 19.175-77 distinguishes it from the three analogous passages in the Iliad, the vocabulary and wording are very similar to Iliad 2.804 and 4.438",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 309,
        "verbatim_quote": "Although the linkage between ethnicity and language in Odyssey 19.175–77 distinguishes it from the three analogous passages in the Iliad, the vocabulary and wording are very similar to Iliad 2.804 and 4.438",
        "supporting_evidence": ["E006"],
        "related_implicit_arguments": []
    },
    {
        "id": "C154",
        "content": "The intention of the Krete passage—evoking strangeness and distance—mirrors that of the Karian entry in the Trojan Catalogue",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 309,
        "verbatim_quote": "while the intention of the passage, evoking as it does strangeness and distance, mirrors that of the Karian entry in the Trojan Catalogue",
        "supporting_evidence": ["E004", "E006"],
        "related_implicit_arguments": []
    }
]

section_evidence = [
    {
        "id": "E006",
        "content": "Odyssey 19.172-77: Krete has ninety poleis with different tongues mingled - Akhaioi, Eteokretes, Kudones, Doriees, and Pelasgoi",
        "evidence_type": "primary_source",
        "page": 308,
        "verbatim_quote": "ἄλλη δ᾽ ἄλλων γλῶσσα μεμιγμένη: ἐν μὲν Ἀχαιοί, / ἐν δ᾽ Ἐτεόκρητες μεγαλήτορες, ἐν δὲ Κύδωνες, / Δωριέες τε τριχάϊκες δῖοί τε Πελασγοί.",
        "source": "Homer, Odyssey 19.172-77",
        "related_claims": ["C139", "C140", "C141", "C142", "C143", "C144", "C145", "C146", "C147", "C148", "C149", "C150", "C151", "C152", "C153", "C154"]
    }
]

section_implicit_arguments = [
    {
        "id": "IA016",
        "content": "Literary representations and historical realities can mutually reinforce each other in oral tradition without clear causal priority",
        "claim_type": "oral_tradition_theory",
        "page": 307,
        "trigger_text": "Whether the Iliad drew upon a preexisting sense... or actively contributed to its construction (or some combination of both)",
        "inference_reasoning": "Ross explicitly acknowledges the difficulty of determining causal direction between literary representation and social reality. This reflects a sophisticated understanding of oral tradition as both reflecting and shaping social attitudes. The 'or some combination of both' acknowledges complex feedback loops between art and society. This is a theoretical position about how oral tradition relates to social change.",
        "related_claims": ["C136"]
    },
    {
        "id": "IA017",
        "content": "The significance of textual patterns becomes clearer through comparative analysis across the broader epic tradition",
        "claim_type": "methodological_principle",
        "page": 307,
        "trigger_text": "The nature and importance of these passages can be better assessed by interpreting them in the context of the surviving body of early Greek epic poetry",
        "inference_reasoning": "Ross's methodological move from close reading of the Iliad to comparative analysis across epic tradition implies a principle about how to assess the significance of rare phenomena. When something appears only three times in one text, its meaning becomes clearer by comparison with similar phenomena in contemporary texts. This is a hermeneutic principle about moving from particular to general.",
        "related_claims": ["C137", "C138", "C139"]
    },
    {
        "id": "IA018",
        "content": "Linguistic diversity functions as a marker of exoticism/alterity even within Akhaian/Greek space when deployed in specific narrative contexts",
        "claim_type": "interpretive_framework",
        "page": 309,
        "trigger_text": "perhaps Odysseus is focusing on the exotic as he does in his other travel stories... ethno-linguistic diversity would make Krete strange and distant, perhaps even \"foreign,\" despite the fact that the island is ruled by an Akhaian king",
        "inference_reasoning": "Ross argues that linguistic diversity can create alterity effects even for places that are politically/ethnically 'inside' (Krete is ruled by Akhaians). This suggests that markers of identity are contextually deployed for narrative effect rather than reflecting fixed categories. The parallel with Odysseus' other travel tales (which Ross doesn't detail here) implies a pattern of exotic-ification through linguistic reference.",
        "related_claims": ["C150", "C151", "C152"]
    }
]

# Add new items to extraction data
print(f"Adding {len(section_claims)} claims from Section 6...")
data['claims'].extend(section_claims)

print(f"Adding {len(section_evidence)} evidence items from Section 6...")
data['evidence'].extend(section_evidence)

print(f"Adding {len(section_implicit_arguments)} implicit arguments from Section 6...")
data['implicit_arguments'].extend(section_implicit_arguments)

# Update timestamp
data['extraction_timestamp'] = datetime.now(timezone.utc).isoformat()

# Write updated data
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print()
print("=" * 80)
print("PASS 1 - SECTION 6 COMPLETE")
print("=" * 80)
print()
print(f"Section 6: Odyssey Evidence (pp. 307-309)")
print(f"  Claims: {len(section_claims)}")
print(f"  Evidence: {len(section_evidence)}")
print(f"  Implicit Arguments: {len(section_implicit_arguments)}")
print(f"  Total items: {len(section_claims) + len(section_evidence) + len(section_implicit_arguments)}")
print()
print(f"Running total: {len(data['claims'])} claims, {len(data['evidence'])} evidence, {len(data['implicit_arguments'])} implicit_arguments")
print("=" * 80)
