#!/usr/bin/env python3
"""
Pass 1: Liberal Claims & Evidence Extraction
Section 8: Homeric Hymns Part 1 - Delian Apollo & Divine Speech
Pages 310-311, ~900 words

Extracts claims, evidence, and implicit arguments from analysis of the Hymn
to Delian Apollo passage about the Delian maidens who can mimic all human
languages.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

extraction_file = Path("extraction.json")

print("=" * 80)
print("PASS 1 - SECTION 8: Homeric Hymns Part 1")
print("Pages 310-311: Delian Apollo & Divine Speech")
print("=" * 80)
print()

# Read current extraction data
with open(extraction_file) as f:
    data = json.load(f)

# Section 8 extraction: Hymn to Delian Apollo on linguistic transcendence
section_claims = [
    {
        "id": "C171",
        "content": "The Homeric Hymn to Delian Apollo implies the transcendence of divine speech over human",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 310,
        "verbatim_quote": "Another passage, from the Homeric Hymn to Delian Apollo, implies the transcendence of divine speech over human",
        "supporting_evidence": ["E009"],
        "related_implicit_arguments": []
    },
    {
        "id": "C172",
        "content": "The Hymn to Delian Apollo provides the only instance in early epic poetry where human linguistic diversity is recognized in a generic way, outside the context of the Trojan epikouroi and the Trojan War",
        "claim_type": "scholarly_observation",
        "claim_status": "explicit",
        "page": 310,
        "verbatim_quote": "it also provides the only instance in early epic poetry where human linguistic diversity is recognized in a generic way, outside the context of the Trojan ἐπίκουροι and the Trojan War",
        "supporting_evidence": ["E009"],
        "related_implicit_arguments": []
    },
    {
        "id": "C173",
        "content": "In the Hymn to Delian Apollo, each listener hears the Delian maidens singing in his own language, no matter which of the 'phyla anthropon' (tribes of people) he comes from",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 311,
        "verbatim_quote": "each listener, no matter which of the φῦλ᾽ ἀνθρώπων (\"tribes of people\") he comes from, hears the Delian maidens singing in his own language",
        "supporting_evidence": ["E009"],
        "related_implicit_arguments": []
    },
    {
        "id": "C174",
        "content": "The Delian maidens know how to mimic 'the speech and stammer of all people' (panton d' anthropon phonas kai bambalistyn mimeisth' isasin)",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 311,
        "verbatim_quote": "the maidens πάντων δ᾽ ἀνθρώπων φωνάς καὶ βαμβαλιαστύν / μιμεῖσθ᾽ ἴσασιν",
        "supporting_evidence": ["E009"],
        "related_implicit_arguments": []
    },
    {
        "id": "C175",
        "content": "Each listener to the Delian maidens' song would swear that he uttered the sounds himself",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 311,
        "verbatim_quote": "φαίη δέ κεν αὐτός ἕκαστος / φθέγγεσθ᾽",
        "supporting_evidence": ["E009"],
        "related_implicit_arguments": []
    },
    {
        "id": "C176",
        "content": "The simultaneous understanding of all listeners in their varied languages is either the product of the singers' skill (implied by 'mimeisth' isasin' and 'houto sphin kale synaregren aoide') or the result of some divine miracle (evoked by words like 'thauma' and 'thelgousi')",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 311,
        "verbatim_quote": "Whether the utterance of words comprehensible to all listeners is the product of the singers' skill—implied by the phrases μιμεῖσθ᾽ ἴσασιν and οὕτω σφιν καλή συνάρηρεν ἀοιδή—or the result of some divine miracle—evoked by such words as θαῦμα and θέλγουσι",
        "supporting_evidence": ["E009"],
        "related_implicit_arguments": ["IA020"]
    },
    {
        "id": "C177",
        "content": "For the Delian maidens scene to be considered remarkable requires the imagined audience to come to the performance speaking a multitude of languages",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 311,
        "verbatim_quote": "for the scene to be considered remarkable requires the imagined audience to come to the performance of the maidens speaking a multitude of languages",
        "supporting_evidence": ["E009"],
        "related_implicit_arguments": ["IA020"]
    },
    {
        "id": "C178",
        "content": "The fact that the Delian maidens' songs can be understood not only by Delian Greeks alone, but by all listeners simultaneously in all their varied languages, ensures that the kleos of the scene oupot' oleitai (never fades)",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 311,
        "verbatim_quote": "That the songs can be understood not only by Delian Greeks alone, but by all listeners, simultaneously, in all of their varied languages, ensures that the κλέος of the scene οὔποτ᾽ ὀλεῖται",
        "supporting_evidence": ["E009"],
        "related_implicit_arguments": []
    },
    {
        "id": "C179",
        "content": "If the simultaneous understanding of all listeners in the Delian Apollo passage is the result of a miracle, it implies that divine or divinely inspired speech transcends individual human languages",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 311,
        "verbatim_quote": "If the simultaneous understanding of the φῦλ᾽ ἀνθρώπων is the result of a miracle, it implies that divine or divinely inspired speech transcends individual human languages",
        "supporting_evidence": ["E009"],
        "related_implicit_arguments": []
    },
    {
        "id": "C180",
        "content": "In the Delian Apollo passage, the distinction between divine and human language and the differences between human languages are intertwined",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 311,
        "verbatim_quote": "Perhaps, then, in this passage the distinction between divine and human language and the differences between human languages are intertwined",
        "supporting_evidence": ["E009"],
        "related_implicit_arguments": ["IA020"]
    },
    {
        "id": "C181",
        "content": "The thauma (wonder) of the Delian maidens scene presupposes and requires human linguistic diversity",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 311,
        "verbatim_quote": "the θαῦμα of the scene presupposes and requires human linguistic diversity",
        "supporting_evidence": ["E009"],
        "related_implicit_arguments": ["IA020"]
    },
    {
        "id": "C182",
        "content": "Nagy believes that the fusion of the Delian and Pythian traditions in the Hymn to Apollo reflects the unification of not just artistic, but also socio-religious traditions",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 307,
        "verbatim_quote": "Nagy... believes that the fusion of the Delian and Pythian traditions in this hymn reflects the unification of not just artistic, but also socio-religious traditions",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C183",
        "content": "The fusion of Delian and Pythian traditions in the Hymn to Apollo brought together not only divergent stories, but also diverse audiences",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 307,
        "verbatim_quote": "bringing together not only divergent stories, but also diverse audiences",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C184",
        "content": "Nagy cites the broad acceptance of the Homeric epics among the Greeks as evidence (along with institutions like the Olympic Games and Delphic Oracle) for an emerging 'intercultural synthesis' that contributed to a nascent sense of Panhellenism",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 307,
        "verbatim_quote": "Nagy... cites the broad acceptance of the epics among the Greeks as evidence—along with the rise of institutions such as the Olympic Games and Delphic Oracle—for an emerging \"intercultural synthesis\" that contributed to a nascent sense of Panhellenism",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C185",
        "content": "The image of the Akhaians presented in the Iliad was apparently an acceptable part of the eighth-century intercultural synthesis",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 307,
        "verbatim_quote": "The image of the Akhaians... presented in the Iliad was apparently an acceptable part of this intercultural synthesis",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C186",
        "content": "Akhaian unity in the Iliad, manifested in such features as a shared common language, reflected Panhellenic sentiments growing among eighth-century Greeks",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 307,
        "verbatim_quote": "Akhaian unity in the Iliad, manifested in such features as a shared common language, reflected Panhellenic sentiments growing among eighth-century Greeks",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C187",
        "content": "Whether the Iliad drew upon a preexisting sense of nascent Panhellenism, or actively contributed to its construction (or some combination of both), the poem reflected Panhellenic sentiments",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 307,
        "verbatim_quote": "Whether the Iliad drew upon a preexisting sense of nascent Panhellenism, or actively contributed to its construction (or some combination of both), Akhaian unity in the Iliad... reflected Panhellenic sentiments growing among eighth-century Greeks",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    }
]

section_evidence = [
    {
        "id": "E009",
        "content": "Homeric Hymn to Delian Apollo 156-64: The Delian maidens can mimic the speech and stammer of all people, so each listener would swear he uttered the sounds himself",
        "evidence_type": "primary_source",
        "page": 310,
        "verbatim_quote": "Hymn. Hom. Ap. 156–64",
        "source": "Homeric Hymn to Delian Apollo 156-64",
        "related_claims": ["C171", "C172", "C173", "C174", "C175", "C176", "C177", "C178", "C179", "C180", "C181"]
    }
]

section_implicit_arguments = [
    {
        "id": "IA020",
        "content": "The Delian Apollo passage demonstrates that human linguistic diversity was a recognized social reality in the early Archaic period, not merely a literary device",
        "claim_type": "historical_claim",
        "page": 311,
        "trigger_text": "for the scene to be considered remarkable requires the imagined audience to come to the performance of the maidens speaking a multitude of languages... the θαῦμα of the scene presupposes and requires human linguistic diversity",
        "inference_reasoning": "Ross argues that the 'wonder' of the scene depends on linguistic diversity being real and recognized by the audience. If audiences didn't experience linguistic diversity in their actual lives, the miraculous transcendence of language barriers wouldn't be remarkable. This moves beyond textual analysis to make a claim about eighth-century social reality. The implicit argument is that literary devices must resonate with audience experience to be effective—a claim about how oral tradition works that underlies much of Ross's analysis but is here most explicitly tied to historical reconstruction.",
        "related_claims": ["C176", "C177", "C180", "C181"]
    }
]

# Add new items to extraction data
print(f"Adding {len(section_claims)} claims from Section 8...")
data['claims'].extend(section_claims)

print(f"Adding {len(section_evidence)} evidence items from Section 8...")
data['evidence'].extend(section_evidence)

print(f"Adding {len(section_implicit_arguments)} implicit arguments from Section 8...")
data['implicit_arguments'].extend(section_implicit_arguments)

# Update timestamp
data['extraction_timestamp'] = datetime.now(timezone.utc).isoformat()

# Write updated data
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print()
print("=" * 80)
print("PASS 1 - SECTION 8 COMPLETE")
print("=" * 80)
print()
print(f"Section 8: Homeric Hymns Part 1 (pp. 310-311)")
print(f"  Claims: {len(section_claims)}")
print(f"  Evidence: {len(section_evidence)}")
print(f"  Implicit Arguments: {len(section_implicit_arguments)}")
print(f"  Total items: {len(section_claims) + len(section_evidence) + len(section_implicit_arguments)}")
print()
print(f"Running total: {len(data['claims'])} claims, {len(data['evidence'])} evidence, {len(data['implicit_arguments'])} implicit_arguments")
print("=" * 80)
