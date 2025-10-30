#!/usr/bin/env python3
"""
Pass 1: Liberal Claims & Evidence Extraction
Section 9: Homeric Hymns Part 2 - Aphrodite & Pattern Synthesis
Pages 311-313, ~1100 words

Extracts claims, evidence, and implicit arguments from analysis of the Hymn
to Aphrodite passage about Phrygian-Trojan linguistic communication, and
comparative synthesis across the epic corpus.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

extraction_file = Path("extraction.json")

print("=" * 80)
print("PASS 1 - SECTION 9: Homeric Hymns Part 2")
print("Pages 311-313: Aphrodite & Pattern Synthesis")
print("=" * 80)
print()

# Read current extraction data
with open(extraction_file) as f:
    data = json.load(f)

# Section 9 extraction: Hymn to Aphrodite and comparative patterns
section_claims = [
    {
        "id": "C188",
        "content": "The Homeric Hymn to Aphrodite passage more closely parallels the passages from the Iliad, dealing as it does with linguistic variation between Trojans and Phrygians",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 311,
        "verbatim_quote": "Another passage from the Homeric Hymns more closely parallels the passages from the Iliad, dealing as it does with linguistic variation between Trojans and Phrygians",
        "supporting_evidence": ["E010"],
        "related_implicit_arguments": []
    },
    {
        "id": "C189",
        "content": "The Hymn to Aphrodite is set a generation before the Trojan War",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 311,
        "verbatim_quote": "Set a generation before the Trojan War",
        "supporting_evidence": ["E010"],
        "related_implicit_arguments": []
    },
    {
        "id": "C190",
        "content": "Aphrodite, disguised as the daughter of king Otreus of Phrygia, explains to Ankhises that she can speak his language because she was brought up by a Trojan nurse",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 312,
        "verbatim_quote": "Aphrodite... constructs a mortal identity, claiming to be the daughter of king Otreus of Phrygia... Aphrodite next defends her mortal origins by explaining how it is that she can speak Ankhises' language",
        "supporting_evidence": ["E010"],
        "related_implicit_arguments": []
    },
    {
        "id": "C191",
        "content": "Aphrodite's explanation for her linguistic ability is vigorous and emphatic, bracketed by numerous emphatic adverbs, particles, and conjunctions",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 312,
        "verbatim_quote": "Not only is a four-line explanatory tale provided, but it is quite vigorous, bracketed by numerous emphatic adverbs, particles, and conjunctions in lines 113 and 116 (σάφα... δή τοι... γε καί)",
        "supporting_evidence": ["E010"],
        "related_implicit_arguments": ["IA021"]
    },
    {
        "id": "C192",
        "content": "Redundancy between lines 113 and 116 of the Hymn to Aphrodite further strengthens the emphasis of the language explanation",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 312,
        "verbatim_quote": "redundancy between lines 113 and 116 further strengthens the emphasis",
        "supporting_evidence": ["E010"],
        "related_implicit_arguments": ["IA021"]
    },
    {
        "id": "C193",
        "content": "Meeting a stranger who can speak his language perfectly strikes Ankhises as odd, something that might be explained were his interlocutor divine",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 312,
        "verbatim_quote": "Perhaps meeting a stranger who can speak his language perfectly strikes Ankhises as odd, something that might be explained were his interlocutor divine, which he already suspects from her beauty and bearing",
        "supporting_evidence": ["E010"],
        "related_implicit_arguments": ["IA021"]
    },
    {
        "id": "C194",
        "content": "Aphrodite takes care to concoct a plausible and forceful explanation for her linguistic ability to combat Ankhises' suspicion",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 312,
        "verbatim_quote": "Combating his suspicion, Aphrodite takes some care to concoct a plausible and forceful explanation",
        "supporting_evidence": ["E010"],
        "related_implicit_arguments": ["IA021"]
    },
    {
        "id": "C195",
        "content": "When Demeter disguises herself as an old woman from Krete and seeks refuge in Eleusis, she has no difficulty talking with the daughters of King Keleos",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 312,
        "verbatim_quote": "When Demeter disguises herself as an old woman from Krete and seeks refuge in Eleusis, she has no difficulty talking with the daughters of King Keleos (Hymn. Hom. Cer. 118–44)",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C196",
        "content": "When Dionysus is seized by pirates, he communicates with the ship's helmsman without difficulty",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 312,
        "verbatim_quote": "Dionysus, when seized by pirates, likewise communicates with the ship's helmsman without difficulty (Hymn. Hom. Bacch. 53–57)",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C197",
        "content": "The case of Aphrodite involves communication between a Phrygian and Ankhises (a Trojan nobleman), echoing the theme from the Iliad that the epikouroi speak a variety of languages distinct from each other and differing from Trojan speech",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 312,
        "verbatim_quote": "the case of Aphrodite involves communication between a Phrygian—Phrygians being future ἐπίκουροι of the Trojans—and Ankhises, a Trojan nobleman, echoing the theme from the Iliad that the ἐπίκουροι speak a variety of languages distinct from each other and differing from Trojan speech",
        "supporting_evidence": ["E010"],
        "related_implicit_arguments": []
    },
    {
        "id": "C198",
        "content": "As is typical in the Iliad, in the Hymn to Aphrodite glossa (language) is associated with place of origin, in this case Phrygia",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 313,
        "verbatim_quote": "As is typical in the Iliad, in the Hymn to Aphrodite γλῶσσα is associated with place of origin, in this case Phrygia",
        "supporting_evidence": ["E010"],
        "related_implicit_arguments": []
    },
    {
        "id": "C199",
        "content": "No mention of Phrygian linguistic difference appears in the Iliad itself",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 313,
        "verbatim_quote": "although no mention of Phrygian linguistic difference appears in the Iliad itself",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C200",
        "content": "The remoteness of the Phrygian homeland is noted in the Iliad by the phrase 'tel' ex' ('from afar') in the Trojan Catalogue",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 313,
        "verbatim_quote": "the remoteness of the Phrygian homeland is noted by the phrase τῆλ᾽ ἐξ, \"from afar,\" in the Trojan Catalogue (2.862–63)",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C201",
        "content": "In the Iliad (3.181-90), the Otreus mentioned in the Hymn to Aphrodite is named by Priam as a contemporary of his youth",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 313,
        "verbatim_quote": "Elsewhere in the Iliad (3.181–90), the Otreus mentioned in the Hymn to Aphrodite is named by Priam as a contemporary of his youth",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C202",
        "content": "Priam favorably compares the Akhaian host under Agamemnon to the largest army he has previously seen: the Phrygians under Otreus and Mygdon who arrayed themselves against the Amazons",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 313,
        "verbatim_quote": "Priam favorably compares the Akhaian host to the largest army he has previously seen, the Phrygians under Otreus and Mygdon who arrayed themselves against the Amazons",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C203",
        "content": "The remoteness of the Phrygians, combined with the fact that they were a powerful people in the youth of Priam (and therefore of Ankhises), makes the poet's choice of the Phrygians as the people of origin for Aphrodite plausible",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 313,
        "verbatim_quote": "The remoteness of the Phrygians, combined with the fact that they were a powerful people in the youth of Priam (and, therefore, of Ankhises, as the two are of the same generation), makes the poet's choice of the Phrygians as the people of origin for Aphrodite plausible",
        "supporting_evidence": ["E010"],
        "related_implicit_arguments": []
    },
    {
        "id": "C204",
        "content": "The poet's choice of Phrygians for Aphrodite's disguise ties the Hymn to the Trojan cycle",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 313,
        "verbatim_quote": "and ties it to the Trojan cycle",
        "supporting_evidence": ["E010"],
        "related_implicit_arguments": []
    },
    {
        "id": "C205",
        "content": "The poet's need to provide a Phrygian princess with a Trojan education to explain how she can converse with Ankhises illustrates the degree to which the image of linguistic diversity among the epikouroi of the Trojans found in the Iliad had solidified within the epic tradition",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 313,
        "verbatim_quote": "the poet's need to provide a Phrygian princess with a Trojan education in order to explain how she can converse with Ankhises illustrates the degree to which the image of linguistic diversity among the ἐπίκουροι of the Trojans found in the Iliad had solidified within the epic tradition",
        "supporting_evidence": ["E010"],
        "related_implicit_arguments": ["IA022"]
    },
    {
        "id": "C206",
        "content": "Although the speaking of different languages occurs only occasionally in the early epic tradition, when it does it tends to serve one of several specific ends",
        "claim_type": "scholarly_observation",
        "claim_status": "explicit",
        "page": 313,
        "verbatim_quote": "although the speaking of different languages occurs only occasionally in the early epic tradition, when it does it tends to serve one of several specific ends",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C207",
        "content": "In the Odyssey, in the Theogony, and sometimes in the Iliad, the speaking of a strange language indicates strangeness, difference, and distance",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 313,
        "verbatim_quote": "In the Odyssey and in the Theogony, and sometimes in the Iliad, the speaking of a strange language indicates just that, strangeness, difference, and distance",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C208",
        "content": "Language as a marker of alterity joins Odysseus' tale of an exotic Krete with Hesiod's image of the horrific beast Typhoeus and with the description of the remote Karians in the Trojan Catalogue",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 313,
        "verbatim_quote": "Language as a marker of alterity joins Odysseus' tale of an exotic Krete with Hesiod's image of the horrific beast Typhoeus—and both with the description of the remote Karians in the Trojan Catalogue",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C209",
        "content": "The contrast between the human and the divine, a recurrent theme in the epic tradition, manifests itself through the allocation of different names to the same creature or place by men on the one hand and gods on the other",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 313,
        "verbatim_quote": "The contrast between the human and the divine, a recurrent theme in the epic tradition, manifests itself through the allocation of different names to the same creature or place by men on the one hand and gods on the other",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C210",
        "content": "Typhoeus combines divine language with the sounds of beasts, but utters nothing understandable by humans",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 313,
        "verbatim_quote": "Typhoeus combines divine language with the sounds of beasts, but utters nothing understandable by humans",
        "supporting_evidence": ["E007"],
        "related_implicit_arguments": []
    },
    {
        "id": "C211",
        "content": "The special status of divine language underlies the universally understood speech found in the Homeric Hymn to Delian Apollo",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 313,
        "verbatim_quote": "The special status of divine language also underlies the universally understood speech found in the Homeric Hymn to Delian Apollo",
        "supporting_evidence": ["E009"],
        "related_implicit_arguments": []
    },
    {
        "id": "C212",
        "content": "The special status of divine language fuels Ankhises' suspicions about Aphrodite's identity",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 313,
        "verbatim_quote": "and perhaps fuels Ankhises' suspicions about Aphrodite's identity",
        "supporting_evidence": ["E010"],
        "related_implicit_arguments": []
    },
    {
        "id": "C213",
        "content": "The transcendence of human linguistic barriers in the Hymn to Delian Apollo is what makes the scene worthy of mention",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 313,
        "verbatim_quote": "The transcendence of human linguistic barriers is what makes the scene from the Hymn to Delian Apollo worthy of mention",
        "supporting_evidence": ["E009"],
        "related_implicit_arguments": []
    },
    {
        "id": "C214",
        "content": "The Homeric Hymn to Aphrodite mirrors the patterns of linguistic division between Trojan and epikourosin the Iliad: Aphrodite, disguised as a Phrygian, can only communicate with Ankhises (a Trojan) because she once had a Trojan nurse",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 313,
        "verbatim_quote": "while the Homeric Hymn to Aphrodite mirrors the patterns of linguistic division between Trojan and ἐπίκουρος in the Iliad: Aphrodite, disguised as a Phrygian, can only communicate with Ankhises, a Trojan, because she once had a Trojan nurse who taught her his language",
        "supporting_evidence": ["E010"],
        "related_implicit_arguments": []
    },
    {
        "id": "C215",
        "content": "Human linguistic variation accounts for more of the instances of linguistic diversity noted in the early epic tradition than does the human-divine dichotomy, even among examples taken from outside the Iliad",
        "claim_type": "scholarly_observation",
        "claim_status": "explicit",
        "page": 313,
        "verbatim_quote": "Overall, human linguistic variation accounts for more of the instances of linguistic diversity noted in the early epic tradition than does the human-divine dichotomy, even among examples taken from outside the Iliad",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    }
]

section_evidence = [
    {
        "id": "E010",
        "content": "Homeric Hymn to Aphrodite 111-16: Aphrodite (disguised as Phrygian princess) explains she can speak Ankhises' (Trojan) language because a Trojan nurse raised her",
        "evidence_type": "primary_source",
        "page": 312,
        "verbatim_quote": "Hymn. Hom. Ven. 111–16",
        "source": "Homeric Hymn to Aphrodite 111-16",
        "related_claims": ["C188", "C189", "C190", "C191", "C192", "C193", "C194", "C197", "C198", "C203", "C204", "C205", "C212", "C214"]
    }
]

section_implicit_arguments = [
    {
        "id": "IA021",
        "content": "The emphatic and vigorous nature of Aphrodite's language explanation signals that linguistic barriers between Phrygians and Trojans were expected by the audience",
        "claim_type": "audience_expectation",
        "page": 312,
        "trigger_text": "Not only is a four-line explanatory tale provided, but it is quite vigorous, bracketed by numerous emphatic adverbs, particles, and conjunctions... Perhaps meeting a stranger who can speak his language perfectly strikes Ankhises as odd",
        "inference_reasoning": "Ross infers from the stylistic features of the text (emphasis, redundancy, vigor) that the poet felt the need to justify linguistic comprehensibility. This implies an audience expectation that Phrygians and Trojans would NOT normally understand each other. The inference chain is: emphatic explanation → justification needed → audience expects linguistic barrier. This is an implicit claim about eighth-century audience beliefs inferred from poetic technique.",
        "related_claims": ["C191", "C192", "C193", "C194"]
    },
    {
        "id": "IA022",
        "content": "The epic tradition developed consistent conventions about linguistic patterns (Akhaian unity vs. epikouroi diversity) that became normative expectations constraining later compositions",
        "claim_type": "oral_tradition_theory",
        "page": 313,
        "trigger_text": "the poet's need to provide a Phrygian princess with a Trojan education in order to explain how she can converse with Ankhises illustrates the degree to which the image of linguistic diversity among the ἐπίκουροι of the Trojans found in the Iliad had solidified within the epic tradition",
        "inference_reasoning": "Ross argues that the Hymn to Aphrodite shows the Iliad's linguistic patterns had 'solidified' as tradition. This implies a theory about how oral traditions develop: successful patterns become conventional, then normative, then constraining. Later poets must either follow the pattern or explicitly explain deviations. This is an unstated theory about oral tradition dynamics: innovation → convention → constraint. Ross uses this to argue for relative chronology (Hymn post-dates Iliad) and for the cultural salience of the Iliad's linguistic patterns.",
        "related_claims": ["C205"]
    }
]

# Add new items to extraction data
print(f"Adding {len(section_claims)} claims from Section 9...")
data['claims'].extend(section_claims)

print(f"Adding {len(section_evidence)} evidence items from Section 9...")
data['evidence'].extend(section_evidence)

print(f"Adding {len(section_implicit_arguments)} implicit arguments from Section 9...")
data['implicit_arguments'].extend(section_implicit_arguments)

# Update timestamp
data['extraction_timestamp'] = datetime.now(timezone.utc).isoformat()

# Write updated data
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print()
print("=" * 80)
print("PASS 1 - SECTION 9 COMPLETE")
print("=" * 80)
print()
print(f"Section 9: Homeric Hymns Part 2 (pp. 311-313)")
print(f"  Claims: {len(section_claims)}")
print(f"  Evidence: {len(section_evidence)}")
print(f"  Implicit Arguments: {len(section_implicit_arguments)}")
print(f"  Total items: {len(section_claims) + len(section_evidence) + len(section_implicit_arguments)}")
print()
print(f"Running total: {len(data['claims'])} claims, {len(data['evidence'])} evidence, {len(data['implicit_arguments'])} implicit_arguments")
print("=" * 80)
