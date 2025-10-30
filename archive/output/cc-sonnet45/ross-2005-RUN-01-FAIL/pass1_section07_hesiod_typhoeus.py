#!/usr/bin/env python3
"""
Pass 1: Liberal Claims & Evidence Extraction
Section 7: Hesiod Evidence - Typhoeus & Divine/Human Speech
Pages 309-310, ~700 words

Extracts claims, evidence, and implicit arguments from analysis of Hesiod's
Theogony passage on Typhoeus and the distinction between divine, human,
and monstrous speech.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

extraction_file = Path("extraction.json")

print("=" * 80)
print("PASS 1 - SECTION 7: Hesiod Evidence")
print("Pages 309-310: Typhoeus & Divine/Human Speech")
print("=" * 80)
print()

# Read current extraction data
with open(extraction_file) as f:
    data = json.load(f)

# Section 7 extraction: Hesiod Theogony on Typhoeus
section_claims = [
    {
        "id": "C155",
        "content": "Unlike Homer, Hesiod never recognizes differences between human languages",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 308,
        "verbatim_quote": "Unlike Homer, Hesiod never recognizes differences between human languages",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C156",
        "content": "Hesiod's only mention of language involves divine speech, contrasted with the inarticulate sounds made by animals",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 308,
        "verbatim_quote": "his only mention of language involves divine speech, contrasted with the inarticulate sounds made by animals",
        "supporting_evidence": ["E007"],
        "related_implicit_arguments": []
    },
    {
        "id": "C157",
        "content": "Typhoeus' many heads are described as making 'every sort of ungodly noise' (pantoien op' ieisai athesphaton)",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 310,
        "verbatim_quote": "the heads are described as πάντοην οὖπ᾽ ἱεῖσαι ἀθέσφατον (\"making every sort of ungodly noise\")",
        "supporting_evidence": ["E007"],
        "related_implicit_arguments": []
    },
    {
        "id": "C158",
        "content": "Typhoeus produces no kind of human speech",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 310,
        "verbatim_quote": "Typhoeus produces no kind of human speech",
        "supporting_evidence": ["E007"],
        "related_implicit_arguments": []
    },
    {
        "id": "C159",
        "content": "Hesiod's list of sounds from Typhoeus begins with 'hos te theois suniemen' (a sound as if for the gods' understanding)",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 310,
        "verbatim_quote": "The list of pantoien op'... athesphaton begins, somewhat incongruously... with ὥς τε θεοῖσι συνίεμεν (\"[a sound] as if for the gods' understanding\")",
        "supporting_evidence": ["E007"],
        "related_implicit_arguments": []
    },
    {
        "id": "C160",
        "content": "The inclusion of divine language sounds among Typhoeus' utterances is incongruous, since 'athesphatos' means literally 'not to be spoken even by a god'",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 310,
        "verbatim_quote": "somewhat incongruously—since ἀθέσφατος means literally \"not to be spoken even by a god\"",
        "supporting_evidence": ["E007"],
        "related_implicit_arguments": []
    },
    {
        "id": "C161",
        "content": "Hesiod contrasts divine language with other monstrous sounds: the sound of a bull, a lion, a pack of dogs, and hissing",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 310,
        "verbatim_quote": "Hesiod then contrasts this divine \"language\" with other pantoien op'... athesphaton: the sound of a bull, a lion, a pack of dogs, and ῥοίζεσχ᾽ (\"hissing\")",
        "supporting_evidence": ["E007"],
        "related_implicit_arguments": []
    },
    {
        "id": "C162",
        "content": "The gods are clearly thought of as having their own speech, as different from human speech as the roaring of a lion or the hissing of a snake",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 310,
        "verbatim_quote": "The gods are clearly thought of as having their own speech, as different from human speech as the roaring of a lion or the hissing of a snake",
        "supporting_evidence": ["E007"],
        "related_implicit_arguments": []
    },
    {
        "id": "C163",
        "content": "The contrast between divine and human speech in the Typhoeus passage is left implicit by Hesiod",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 310,
        "verbatim_quote": "but here the contrast is left implicit",
        "supporting_evidence": ["E007"],
        "related_implicit_arguments": ["IA019"]
    },
    {
        "id": "C164",
        "content": "Hesiod attributes only nonhuman types of 'speech' to Typhoeus",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 310,
        "verbatim_quote": "Hesiod attributes only nonhuman types of \"speech\" to Typhoeus",
        "supporting_evidence": ["E007"],
        "related_implicit_arguments": ["IA019"]
    },
    {
        "id": "C165",
        "content": "Hesiod may attribute only nonhuman speech to Typhoeus to reemphasize the horror and monstrosity of the creature",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 310,
        "verbatim_quote": "perhaps to reemphasize the horror and monstrosity of the creature",
        "supporting_evidence": ["E007"],
        "related_implicit_arguments": ["IA019"]
    },
    {
        "id": "C166",
        "content": "Homer uses the speaking of diverse languages on Krete to emphasize the exotic nature of that island",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 310,
        "verbatim_quote": "as Homer uses the speaking of diverse languages on Krete to emphasize the exotic nature of that island",
        "supporting_evidence": ["E006"],
        "related_implicit_arguments": []
    },
    {
        "id": "C167",
        "content": "Homer uses the alien speech of the Karians to indicate their outlandishness",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 310,
        "verbatim_quote": "or the alien speech of the Karians to indicate their outlandishness",
        "supporting_evidence": ["E004"],
        "related_implicit_arguments": []
    },
    {
        "id": "C168",
        "content": "The difference between human and divine speech is echoed elsewhere in the epic tradition when two names are given for a creature, one current among the gods and one among men",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 310,
        "verbatim_quote": "The difference between human and divine speech is echoed elsewhere in the epic tradition when two names are given for a creature, one current among the gods, the other among men",
        "supporting_evidence": ["E008"],
        "related_implicit_arguments": []
    },
    {
        "id": "C169",
        "content": "The practice of providing two names (one divine, one human) exemplifies the concern of Greek epic with the division between the human and the divine",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 310,
        "verbatim_quote": "Providing two names—one divine, the other human—both exemplifies the concern of Greek epic with the division between the human and the divine",
        "supporting_evidence": ["E008"],
        "related_implicit_arguments": []
    },
    {
        "id": "C170",
        "content": "Providing two names for creatures (divine and human) offers the poet an opportunity to display his privileged knowledge of the names used by the gods",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 310,
        "verbatim_quote": "and offers the poet an opportunity to display his privileged knowledge of the names used by the gods",
        "supporting_evidence": ["E008"],
        "related_implicit_arguments": []
    }
]

section_evidence = [
    {
        "id": "E007",
        "content": "Hesiod Theogony 824-35: Description of Typhoeus with hundred snake-heads making various sounds including divine speech, bull roaring, lion roaring, dog yelping, and snake hissing",
        "evidence_type": "primary_source",
        "page": 309,
        "verbatim_quote": "Theog. 824–35",
        "source": "Hesiod, Theogony 824-35",
        "related_claims": ["C156", "C157", "C158", "C159", "C160", "C161", "C162", "C163", "C164", "C165"]
    },
    {
        "id": "E008",
        "content": "Iliad 1.403-4: The creature called Briareos by the gods but Aigaion by all men",
        "evidence_type": "primary_source",
        "page": 310,
        "verbatim_quote": "Il. 1.403–4",
        "source": "Homer, Iliad 1.403-4",
        "related_claims": ["C168", "C169", "C170"]
    }
]

section_implicit_arguments = [
    {
        "id": "IA019",
        "content": "Linguistic monstrosity (speaking inappropriately or producing inarticulate sounds) functions as a marker of alterity comparable to human linguistic diversity",
        "claim_type": "interpretive_framework",
        "page": 310,
        "trigger_text": "Hesiod attributes only nonhuman types of 'speech' to Typhoeus, perhaps to reemphasize the horror and monstrosity of the creature, as Homer uses the speaking of diverse languages on Krete to emphasize the exotic nature",
        "inference_reasoning": "Ross draws a parallel between three uses of linguistic variation: (1) Typhoeus' monstrous multi-species vocalizations, (2) Kretan ethno-linguistic diversity, and (3) Karian barbarophonos designation. The implicit argument is that linguistic abnormality—whether monstrosity (Typhoeus), diversity (Krete), or strangeness (Karians)—serves the same literary function: marking alterity, distance, and foreignness. This is an analytical framework Ross imposes rather than something explicitly stated in the texts.",
        "related_claims": ["C163", "C164", "C165", "C166", "C167"]
    }
]

# Add new items to extraction data
print(f"Adding {len(section_claims)} claims from Section 7...")
data['claims'].extend(section_claims)

print(f"Adding {len(section_evidence)} evidence items from Section 7...")
data['evidence'].extend(section_evidence)

print(f"Adding {len(section_implicit_arguments)} implicit arguments from Section 7...")
data['implicit_arguments'].extend(section_implicit_arguments)

# Update timestamp
data['extraction_timestamp'] = datetime.now(timezone.utc).isoformat()

# Write updated data
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print()
print("=" * 80)
print("PASS 1 - SECTION 7 COMPLETE")
print("=" * 80)
print()
print(f"Section 7: Hesiod Evidence (pp. 309-310)")
print(f"  Claims: {len(section_claims)}")
print(f"  Evidence: {len(section_evidence)}")
print(f"  Implicit Arguments: {len(section_implicit_arguments)}")
print(f"  Total items: {len(section_claims) + len(section_evidence) + len(section_implicit_arguments)}")
print()
print(f"Running total: {len(data['claims'])} claims, {len(data['evidence'])} evidence, {len(data['implicit_arguments'])} implicit_arguments")
print("=" * 80)
