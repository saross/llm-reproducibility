#!/usr/bin/env python3
"""
Pass 1: Liberal Claims & Evidence Extraction
Section 2: Literature Review Part 1 - Oppositional vs Aggregative Panhellenism
Pages 301-302, ~600 words

Extracts claims, evidence, and implicit arguments from the literature review
discussing scholarly debates about Panhellenism.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

extraction_file = Path("extraction.json")

print("=" * 80)
print("PASS 1 - SECTION 2: Literature Review Part 1")
print("Pages 301-302: Oppositional vs Aggregative Panhellenism")
print("=" * 80)
print()

# Read current extraction data
with open(extraction_file) as f:
    data = json.load(f)

# Section 2 extraction: Literature review on scholarly positions
section_claims = [
    {
        "id": "C035",
        "content": "Pre-Classical Greek literature does not offer unambiguous evidence for Panhellenic identity",
        "claim_type": "scholarly_observation",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "Pre-Classical Greek literature does not offer unambiguous evidence for Panhellenic identity",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C036",
        "content": "The earlier one looks in Greek history, the more problematic the concept of Panhellenism becomes",
        "claim_type": "scholarly_observation",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "the earlier one looks, the more problematic the concept becomes",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C037",
        "content": "Scholars who see Panhellenism as emerging primarily through opposition to a barbarian 'Other' tend to downplay the extent of Panhellenism before the Persian Wars",
        "claim_type": "historiographical_observation",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "Scholars who see Panhellenism as emerging primarily through opposition to a barbarian \"Other\" tend to downplay the extent of Panhellenism before the Persian Wars",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA005"]
    },
    {
        "id": "C038",
        "content": "The consensus holds that the dichotomy between Greek and barbarian arose during and after the Persian Wars",
        "claim_type": "historiographical_consensus",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "The consensus holds that the dichotomy between Greek and barbarian arose during and after the Persian Wars",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C039",
        "content": "Any Panhellenic identity based on Greek-barbarian opposition does not precede the advent of the Classical Era",
        "claim_type": "scholarly_consensus",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "any Panhellenic identity based upon it, therefore, does not precede the advent of the Classical Era",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C040",
        "content": "In the Classical Era, Greeks construct their identities negatively through polarised oppositions of themselves to what they were not",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "Greeks . . . construct their identities negatively, by means of a series of polarized oppositions of themselves to what they were not",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C041",
        "content": "There is an absence of the barbarian concept in early Greek thought",
        "claim_type": "scholarly_observation",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "the absence of the barbarian in early Greek thought",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C042",
        "content": "A 'discourse of barbarism' arose in poetry after the Persian Wars",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "the \"discourse of barbarism\" that arose in poetry after the Persian Wars",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C043",
        "content": "The barbarian became solidified as the antithesis of the Hellene during the Classical period",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "the solidification of the barbarian as the antithesis of the Hellene",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C044",
        "content": "Panhellenism in Pindar's poetry is a novel development of the early Classical period",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "Morgan (1993, 18, 36) argues that Panhellenism in Pindar's poetry is a novel development",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C045",
        "content": "The Greek-barbarian dichotomy reaches maturity in Herodotus",
        "claim_type": "scholarly_observation",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "The Greek-barbarian dichotomy reaches maturity in Herodotus",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C046",
        "content": "Herodotus depicts Skythian 'otherness' especially through their nomadism",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "Hartog finds evidence for an oppositional identity in Herodotus' depiction of the Skythians' \"otherness,\" especially their nomadism",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C047",
        "content": "Herodotus implicitly contrasts Skythian lack of settled agricultural city life with the rooted, agricultural, and polis-oriented existence of the Athenians",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "Herodotus implicitly and negatively contrasts this lack of a settled, agricultural, city life with the rooted (indeed, autochthonous), agricultural, and πολις-oriented existence of the Athenians",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C048",
        "content": "Those who view Panhellenism as aggregated from disparate local and regional identities allow for its earlier appearance, at least in a limited or nascent form",
        "claim_type": "historiographical_observation",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "Those who view Panhellenism as aggregated from disparate local and regional identities allow for its earlier appearance, at least in a limited or nascent form",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA006"]
    },
    {
        "id": "C049",
        "content": "Snodgrass and Nagy find a nascent Panhellenism in the eighth century BCE built from, but beginning to transcend, local identities",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "Snodgrass and Nagy find a nascent Panhellenism in the eighth century b.c.e. built from, but beginning to transcend, local identities",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C050",
        "content": "The Olympic Games, the Delphic Oracle, and the Homeric epics are indicators of eighth-century Panhellenism",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "Both recognize, for example, the Olympic Games, the Delphic Oracle, and the Homeric epics themselves as indicators of eighth-century Panhellenism",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C051",
        "content": "J. Hall views Archaic Greek identity as 'aggregative' in character",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "J. Hall, who explicitly views Archaic Greek identity as \"aggregative\" in character",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C052",
        "content": "The sixth century BCE constitutes a critical juncture in the slow evolution of aggregative proto-Panhellenism",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "the sixth century b.c.e. constitutes a critical juncture in the slow evolution of aggregative proto-Panhellenism",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C053",
        "content": "The founding of the Hellenion at Naukratis and the first well-attested use of collective names (Hellenes or Panhellenes) mark a critical juncture in proto-Panhellenism",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "marked especially by the founding of the Hellenion at Naukratis and the first well-attested use of collective names (Hellenes or Panhellenes) for the Greeks as a whole",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C054",
        "content": "A third view has emerged that oppositional identity may have begun to develop in the Archaic period (or even the late Dark Age) through intercultural contact brought about by colonisation or trade",
        "claim_type": "historiographical_observation",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "A third view has recently emerged, that oppositional identity may have begun to develop in the Archaic period (or even the late Dark Age) through intercultural contact brought about by colonization or trade",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA007"]
    },
    {
        "id": "C055",
        "content": "Greeks constructed a 'negotiated periphery' with the Near East during the late Dark Age",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "Morris (1996, 1–8) has argued that Greeks constructed a \"negotiated periphery\" with the Near East during the late Dark Age",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C056",
        "content": "The negotiated periphery with the Near East engendered rejection of outside influences among some Greeks, while others actively sought out eastern goods",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "which engendered rejection of outside influences among some Greeks, while others actively sought out eastern goods",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C057",
        "content": "The Iliad potentially offers the earliest available literary evidence for Panhellenism",
        "claim_type": "research_positioning",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "The Iliad potentially offers the earliest available literary evidence for Panhellenism",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    }
]

section_evidence = []

section_implicit_arguments = [
    {
        "id": "IA005",
        "content": "There is a dichotomy in scholarly approaches between 'oppositional' and 'aggregative' models of Panhellenism formation",
        "claim_type": "methodological_framework",
        "page": 301,
        "trigger_text": "Scholars who see Panhellenism as emerging primarily through opposition... Those who view Panhellenism as aggregated from disparate local and regional identities...",
        "inference_reasoning": "Ross structures the literature review around two contrasting scholarly approaches to understanding Panhellenism. This binary framework is an analytical construct imposed on the scholarship rather than explicitly stated as a framework by the scholars themselves. The oppositional vs aggregative distinction serves as Ross's organising principle for understanding different scholarly positions.",
        "related_claims": ["C037", "C048", "C054"]
    },
    {
        "id": "IA006",
        "content": "Aggregative models of Panhellenism are more amenable to finding early proto-Panhellenic identity than oppositional models",
        "claim_type": "methodological_assumption",
        "page": 301,
        "trigger_text": "Those who view Panhellenism as aggregated from disparate local and regional identities allow for its earlier appearance",
        "inference_reasoning": "Ross implies that the theoretical framework one adopts (oppositional vs aggregative) determines the conclusions one reaches about the timing of Panhellenism's emergence. This is an unstated assumption about how methodological commitments shape historical interpretations. The word 'allow' suggests that the framework enables or permits certain conclusions.",
        "related_claims": ["C048", "C049", "C050", "C051", "C052"]
    },
    {
        "id": "IA007",
        "content": "Recent scholarship attempts to reconcile oppositional and aggregative models through theories of intercultural contact",
        "claim_type": "historiographical_interpretation",
        "page": 301,
        "trigger_text": "A third view has recently emerged, that oppositional identity may have begun to develop in the Archaic period... through intercultural contact",
        "inference_reasoning": "Ross presents Morris's 'negotiated periphery' concept as a 'third view' that potentially bridges the oppositional-aggregative divide. This synthesis is Ross's interpretive framework rather than Morris's explicit positioning. Ross implies that contact-based theories represent a newer, potentially more sophisticated approach that combines elements of both earlier models.",
        "related_claims": ["C054", "C055", "C056"]
    }
]

# Add new items to extraction data
print(f"Adding {len(section_claims)} claims from Section 2...")
data['claims'].extend(section_claims)

print(f"Adding {len(section_evidence)} evidence items from Section 2...")
data['evidence'].extend(section_evidence)

print(f"Adding {len(section_implicit_arguments)} implicit arguments from Section 2...")
data['implicit_arguments'].extend(section_implicit_arguments)

# Update timestamp
data['extraction_timestamp'] = datetime.now(timezone.utc).isoformat()

# Write updated data
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print()
print("=" * 80)
print("PASS 1 - SECTION 2 COMPLETE")
print("=" * 80)
print()
print(f"Section 2: Literature Review Part 1 (pp. 301-302)")
print(f"  Claims: {len(section_claims)}")
print(f"  Evidence: {len(section_evidence)}")
print(f"  Implicit Arguments: {len(section_implicit_arguments)}")
print(f"  Total items: {len(section_claims) + len(section_evidence) + len(section_implicit_arguments)}")
print()
print(f"Running total: {len(data['claims'])} claims, {len(data['evidence'])} evidence, {len(data['implicit_arguments'])} implicit_arguments")
print("=" * 80)
