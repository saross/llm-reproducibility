#!/usr/bin/env python3
"""
Pass 1: Liberal Claims & Evidence Extraction
Section 10: Synthesis & Conclusions
Pages 313-316, ~1400 words

Extracts claims, evidence, and implicit arguments from the synthesis and
conclusions section, including the two motivations for linguistic variation
in the Iliad and the proto-Panhellenism argument.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

extraction_file = Path("extraction.json")

print("=" * 80)
print("PASS 1 - SECTION 10: Synthesis & Conclusions")
print("Pages 313-316")
print("=" * 80)
print()

# Read current extraction data
with open(extraction_file) as f:
    data = json.load(f)

# Section 10 extraction: Synthesis and conclusions
section_claims = [
    {
        "id": "C216",
        "content": "Linguistic variation in the Iliad arises from two motivations on the part of the poet",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 313,
        "verbatim_quote": "Focusing on the Iliad itself, linguistic variation arises from two motivations on the part of the poet",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C217",
        "content": "The first motivation for linguistic variation in the Iliad is linguistic difference as a marker of distance and alterity, which occurs widely in the epic tradition",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 313,
        "verbatim_quote": "The first occurs widely in the epic tradition and has been noted above: linguistic difference as a marker of distance and alterity",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C218",
        "content": "The second motivation for linguistic variation in the Iliad is more specific to the internal dynamics of the poem: the desire to cast the Trojan host as divided and chaotic, the Akhaian as unified and organized",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "The second is more specific to the internal dynamics of the Iliad: the desire to cast the Trojan host as divided and chaotic, the Akhaian as unified and organized",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C219",
        "content": "The artistic devices of linguistic variation work because during the late eighth century, around the time the Iliad stabilized, both resonated with and perhaps even contributed to an emerging sense of Panhellenism",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "These artistic devices work because during the late eighth century, around the time the Iliad stabilized in its final form, both resonated with—and perhaps even contributed to—an emerging sense of Panhellenism",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA023"]
    },
    {
        "id": "C220",
        "content": "The audience found the linguistically homogenous Akhaians familiar",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "the audience found the linguistically homogenous Akhaians familiar",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA023"]
    },
    {
        "id": "C221",
        "content": "The eighth-century audience perhaps saw an extension or idealization of their own emergent shared culture in the Akhaians' unified cultural, social, and political community",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "and perhaps saw an extension or idealization of their own emergent shared culture in the Akhaians' unified cultural, social, and political community",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA023"]
    },
    {
        "id": "C222",
        "content": "The Panhellenism revealed by the use of language in the Iliad is at an early stage of development",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "The Panhellenism revealed by the use of language in the Iliad is, however, at an early stage of development",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C223",
        "content": "Language is not the most important criterion of identity in the Iliad",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "language is not the most important criterion of identity",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C224",
        "content": "In all three passages about language in the Iliad, language is coupled with, or even subordinate to, place of origin or membership in a particular military retinue",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "in all three passages it is coupled with, or even subordinate to, place of origin or membership in a particular military retinue",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C225",
        "content": "Never in the Iliad is there a language barrier between Akhaian and Trojan",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "never in the Iliad is there a language barrier between Akhaian and Trojan",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C226",
        "content": "Heroes from Akhaian and Trojan camps freely communicate in face-to-face encounters",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "heroes from both camps freely communicate in face-to-face encounters",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C227",
        "content": "The Trojans are not represented merely as some undifferentiated barbarian horde",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "Nor are the Trojans represented merely as some undifferentiated barbarian horde",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C228",
        "content": "Linguistic diversity among the Trojan epikouroi is neither ignored nor suppressed",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "linguistic diversity among the Trojan ἐπίκουροι is neither ignored nor suppressed",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C229",
        "content": "Every reference to variation in language in the Iliad occurs within the Trojan sphere",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "and every reference to variation in language occurs within the Trojan sphere",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C230",
        "content": "The monolithic 'barbarian', a genus diametrically opposed to 'Greek', remains absent from the Iliad",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "The monolithic \"barbarian,\" a genus diametrically opposed to \"Greek,\" remains absent",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C231",
        "content": "The monolithic barbarian concept awaited the psychological and cultural upheaval triggered by the Persian Wars",
        "claim_type": "historical_claim",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "awaiting the psychological and cultural upheaval triggered by the Persian Wars",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C232",
        "content": "The Iliad draws a contrast between Trojans and the Akhaians",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "The epics do, however, draw a contrast between Trojans and the Akhaians",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C233",
        "content": "While linguistic diversity is emphasized among the epikouroi defending Troy, it is entirely absent from the Akhaian force besieging the city",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "While linguistic diversity is emphasized among the ἐπίκουροι defending Troy, it is entirely absent from the Akhaian force besieging the city",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C234",
        "content": "Although the Iliad lacks a clearly oppositional Panhellenic identity with consistent differentiation between 'Akhaian-speakers' and others, it contains a nascent Panhellenic identity based on linguistic unity",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "although the Iliad lacks a clearly oppositional Panhellenic identity with consistent differentiation between \"Akhaian-speakers\" and others, it contains a nascent Panhellenic identity based on linguistic unity",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C235",
        "content": "The Iliad contains a recognition of Akhaian homogeneity of language against the linguistic diversity of the Trojan epikouroi",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "a recognition of Akhaian homogeneity of language against the linguistic diversity of the Trojan ἐπίκουροι",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C236",
        "content": "The linguistic situation in the Iliad exemplifies the early, underdeveloped Panhellenism found in the eighth century BCE",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "This linguistic situation exemplifies the early, underdeveloped Panhellenism found in the eighth century b.c.e.",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C237",
        "content": "Eighth-century Panhellenism was a cultural synthesis still tempered by intra-Hellenic diversity and lacking systematic opposition with a non-Hellenic Other",
        "claim_type": "historical_claim",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "a cultural synthesis still tempered by intra-Hellenic diversity and lacking systematic opposition with a non-Hellenic Other",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C238",
        "content": "Peoples who spoke strange and diverse languages might very well be thought disunited, chaotic, strange, and exotic",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "although peoples who spoke strange and diverse languages might very well be thought disunited, chaotic, strange, and exotic",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C239",
        "content": "No Akhaian/non-Akhaian division in the Iliad had yet evolved to a unified 'us' versus a unified 'them'",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "no Akhaian/non-Akhaian division in the Iliad had yet evolved to a unified \"us\" versus a unified \"them\"",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C240",
        "content": "The development of Panhellenism has been captured in the Iliad at the stage of an operationally but incompletely unified 'us' versus a diverse, plural 'those others'",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "Instead, the development of Panhellenism has been captured at the stage of an operationally but incompletely unified \"us\" versus a diverse, plural \"those others\"",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C241",
        "content": "The Greeks of the late eighth century BCE shared enough to accept a common epic tradition in which they recognized the Akhaians as an idealized vision of themselves",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "The Greeks of the late eighth century b.c.e. shared enough to accept a common epic tradition, in which they recognized the Akhaians as an idealized vision of themselves",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA024"]
    },
    {
        "id": "C242",
        "content": "The Akhaians in the Iliad are represented as ordered and unified; close, native, and familiar",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 314,
        "verbatim_quote": "ordered and unified; close, native, and familiar",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    }
]

section_evidence = []

section_implicit_arguments = [
    {
        "id": "IA023",
        "content": "Effective oral poetry requires resonance between poetic devices and audience beliefs—literary patterns work because they reflect or shape cultural attitudes",
        "claim_type": "oral_tradition_theory",
        "page": 314,
        "trigger_text": "These artistic devices work because during the late eighth century, around the time the Iliad stabilized in its final form, both resonated with—and perhaps even contributed to—an emerging sense of Panhellenism",
        "inference_reasoning": "Ross's argument depends on an unstated theory about how oral tradition operates: poetic devices are effective only if they resonate with audience experience and beliefs. This is a fundamental assumption about the relationship between art and culture in oral traditions. The claim goes beyond saying the Iliad reflects Panhellenism—it posits a causal mechanism (resonance/contribution) linking poetic technique to social reality. This theory underwrites Ross's entire historical reconstruction from textual evidence.",
        "related_claims": ["C219", "C220", "C221"]
    },
    {
        "id": "IA024",
        "content": "The Iliad functioned as a vehicle for eighth-century Greek self-recognition and identity formation",
        "claim_type": "cultural_function",
        "page": 314,
        "trigger_text": "The Greeks of the late eighth century b.c.e. shared enough to accept a common epic tradition, in which they recognized the Akhaians as an idealized vision of themselves: ordered and unified; close, native, and familiar",
        "inference_reasoning": "This is Ross's culminating implicit claim about the Iliad's social function. He argues that the epic didn't just reflect proto-Panhellenic identity but actively enabled Greeks to see themselves as a collective. The phrase 'recognized the Akhaians as an idealized vision of themselves' implies the poem mediated between disparate Greek communities, providing a shared imaginative space for collective identity. This goes beyond textual analysis to make a claim about the poem's role in identity formation—an unstated theory about literature's social function.",
        "related_claims": ["C241", "C242"]
    }
]

# Add new items to extraction data
print(f"Adding {len(section_claims)} claims from Section 10...")
data['claims'].extend(section_claims)

print(f"Adding {len(section_evidence)} evidence items from Section 10...")
data['evidence'].extend(section_evidence)

print(f"Adding {len(section_implicit_arguments)} implicit arguments from Section 10...")
data['implicit_arguments'].extend(section_implicit_arguments)

# Update timestamp
data['extraction_timestamp'] = datetime.now(timezone.utc).isoformat()

# Write updated data
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print()
print("=" * 80)
print("PASS 1 - SECTION 10 COMPLETE")
print("=" * 80)
print()
print(f"Section 10: Synthesis & Conclusions (pp. 313-316)")
print(f"  Claims: {len(section_claims)}")
print(f"  Evidence: {len(section_evidence)}")
print(f"  Implicit Arguments: {len(section_implicit_arguments)}")
print(f"  Total items: {len(section_claims) + len(section_evidence) + len(section_implicit_arguments)}")
print()
print(f"Running total: {len(data['claims'])} claims, {len(data['evidence'])} evidence, {len(data['implicit_arguments'])} implicit_arguments")
print("=" * 80)
print()
print("=" * 80)
print("PASS 1 COMPLETE - ALL 10 SECTIONS EXTRACTED")
print("=" * 80)
