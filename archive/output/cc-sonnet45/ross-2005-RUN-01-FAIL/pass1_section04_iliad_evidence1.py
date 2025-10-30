#!/usr/bin/env python3
"""
Pass 1: Liberal Claims & Evidence Extraction
Section 4: Iliad Evidence Part 1 - Books 2.802-6 & 2.867
Pages 303-304, ~900 words

Extracts claims, evidence, and implicit arguments from the first analysis
of Iliad passages addressing linguistic diversity.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

extraction_file = Path("extraction.json")

print("=" * 80)
print("PASS 1 - SECTION 4: Iliad Evidence Part 1")
print("Pages 303-304: Books 2.802-6 & 2.867")
print("=" * 80)
print()

# Read current extraction data
with open(extraction_file) as f:
    data = json.load(f)

# Section 4 extraction: First Iliad passages on linguistic diversity
section_claims = [
    {
        "id": "C082",
        "content": "Three passages in the Iliad directly address the speaking of different languages (Il. 2.802-6, 2.867, 4.433-38; Od. 19.172-77)",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 303,
        "verbatim_quote": "Three passages in the Iliad directly address the speaking of different languages (Il. 2.802–6, 2.867, 4.433–38; Od. 19.172–77, each discussed below)",
        "supporting_evidence": ["E003", "E004", "E005"],
        "related_implicit_arguments": []
    },
    {
        "id": "C083",
        "content": "In all three Iliad passages, Homer recognises strangeness or diversity of speech among the epikouroi of the Trojans",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 303,
        "verbatim_quote": "In all three, Homer recognizes strangeness or diversity of speech among the ἐπίκουροι of the Trojans",
        "supporting_evidence": ["E003", "E004", "E005"],
        "related_implicit_arguments": []
    },
    {
        "id": "C084",
        "content": "The first passage recognising linguistic diversity occurs as the Trojans prepare to counter an Akhaian attack in Book 2",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 303,
        "verbatim_quote": "The first of these passages occurs as the Trojans prepare to counter an Akhaian attack in Book 2",
        "supporting_evidence": ["E003"],
        "related_implicit_arguments": []
    },
    {
        "id": "C085",
        "content": "The phrase 'but there are different tongues among the wide-strewn human race' makes it clear that the epikouroi speak various mutually unintelligible languages",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 304,
        "verbatim_quote": "The phrase ἄλλη δ᾽ ἄλλων γλῶσσα πολυσπερέων ἀνθρώπων (\"but there are different tongues among the wide-strewn human race\") makes it clear that the ἐπίκουροι speak various mutually unintelligible languages",
        "supporting_evidence": ["E003"],
        "related_implicit_arguments": []
    },
    {
        "id": "C086",
        "content": "There would be no need to dispatch each leader to command his own troops if the epikouroi spoke mutually intelligible languages",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 304,
        "verbatim_quote": "otherwise, there would be no need to dispatch each leader to command his own troops",
        "supporting_evidence": ["E003"],
        "related_implicit_arguments": []
    },
    {
        "id": "C087",
        "content": "In Iliad 2.802-6, Hektor must dispatch each commander to array the residents of his own polis (polites)",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 304,
        "verbatim_quote": "What is more, in this passage Hektor must dispatch each commander to array the residents of his own πόλις (πολῖται)",
        "supporting_evidence": ["E003"],
        "related_implicit_arguments": []
    },
    {
        "id": "C088",
        "content": "It is assumed that all members of a single polis community (and consequently the military contingent based upon it) speak the same language",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 304,
        "verbatim_quote": "It is assumed that all members of a single πόλις community (and consequently the military contingent based upon it) speak the same language",
        "supporting_evidence": ["E003"],
        "related_implicit_arguments": ["IA010"]
    },
    {
        "id": "C089",
        "content": "Language barriers may arise between poleis and their associated military bands",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 304,
        "verbatim_quote": "but that language barriers may arise between πόλεις and their associated military bands",
        "supporting_evidence": ["E003"],
        "related_implicit_arguments": ["IA010"]
    },
    {
        "id": "C090",
        "content": "In Iliad 2.802-6, language does not define particular ethnic or socio-linguistic groups",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 304,
        "verbatim_quote": "In this case, language does not define particular ethnic or socio-linguistic groups",
        "supporting_evidence": ["E003"],
        "related_implicit_arguments": []
    },
    {
        "id": "C091",
        "content": "Linguistic variation among the epikouroi follows the contours of other aspects of identity more frequently invoked by Homer: polis and military contingent",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 304,
        "verbatim_quote": "Instead, linguistic variation among the ἐπίκουροι follows the contours of other aspects of identity more frequently invoked by Homer (and found among both Trojan and Akhaian forces): πόλις and military contingent",
        "supporting_evidence": ["E003"],
        "related_implicit_arguments": ["IA011"]
    },
    {
        "id": "C092",
        "content": "The second example of linguistic variation among the Trojan epikouroi is found in the Trojan Catalogue of Book 2",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 304,
        "verbatim_quote": "The second example of linguistic variation among the ἐπίκουροι of the Trojans is found in the Trojan Catalogue of Book 2",
        "supporting_evidence": ["E004"],
        "related_implicit_arguments": []
    },
    {
        "id": "C093",
        "content": "Homer labels the Karians barbarophonos ('barbarous-voiced' or 'strange-speaking') without further comment in the Trojan Catalogue",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 304,
        "verbatim_quote": "In this passage, Homer labels the Karians βαρβαρόφωνος (\"barbarous-voiced\" or \"strange-speaking\") without further comment",
        "supporting_evidence": ["E004"],
        "related_implicit_arguments": []
    },
    {
        "id": "C094",
        "content": "Iliad 2.867-69 marks the only use of a barbaros cognate or compound in the Iliad",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 304,
        "verbatim_quote": "This passage marks the only use of a βάρβαρος cognate or compound in the Iliad",
        "supporting_evidence": ["E004"],
        "related_implicit_arguments": []
    },
    {
        "id": "C095",
        "content": "This is the only use of a barbaros-cognate in Greek literature prior to the latter half of the sixth century BCE",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 304,
        "verbatim_quote": "Indeed, this is the only use of a βάρβαρος-cognate in Greek literature prior to the latter half of the sixth century b.c.e. (Anac. frag. 423 Page; see J. Hall 2002, 111–12)",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C096",
        "content": "The adjective barbarophonos here does not denote merely non-Greek (or non-Akhaian) speech, but instead carries the force of strange speech more generally",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 304,
        "verbatim_quote": "It is likely that the adjective βαρβαρόφωνος here does not denote merely non-Greek (or, more properly, non-Akhaian) speech, but instead carries the force of strange speech more generally",
        "supporting_evidence": ["E004"],
        "related_implicit_arguments": ["IA012"]
    },
    {
        "id": "C097",
        "content": "Every other passage in the Iliad that concerns the use of mutually incomprehensible languages refers not to a divide between Akhaians and non-Akhaian divisions, but instead to differences between epikouroi and Trojans (or among epikouroi)",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 304,
        "verbatim_quote": "since every other passage in the Iliad that concerns the use of mutually incomprehensible languages refers not to a divide between Akhaians and non-Akhaian divisions, but instead to differences between ἐπίκουροι and Trojans (or among ἐπίκουροι)",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA012"]
    },
    {
        "id": "C098",
        "content": "The poet is not only, or even primarily, drawing a distinction between the Karians and the Akhaians, but instead is setting the Karians apart as strange and foreign in general",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 305,
        "verbatim_quote": "the poet is not only, or even primarily, drawing a distinction between the Karians and the Akhaians (or between the Karians and his Greek-speaking audience), but instead is setting the Karians apart as strange and foreign in general",
        "supporting_evidence": ["E004"],
        "related_implicit_arguments": []
    },
    {
        "id": "C099",
        "content": "The Karians are set apart as far removed not just from the Akhaians but also from the Trojans themselves and perhaps even from the other epikouroi",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 305,
        "verbatim_quote": "far removed not just from the Akhaians but also from the Trojans themselves and perhaps even from the other ἐπίκουροι",
        "supporting_evidence": ["E004"],
        "related_implicit_arguments": []
    },
    {
        "id": "C100",
        "content": "The idea of Karian remoteness is reinforced by the fact that the Karians occur next-to-last in the Trojan Catalogue, which appears to be arranged in geographical order",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 305,
        "verbatim_quote": "The idea of remoteness is reinforced by the fact that the Karians occur next-to-last in the Trojan Catalogue, which appears to be arranged in geographical order",
        "supporting_evidence": ["E004"],
        "related_implicit_arguments": []
    },
    {
        "id": "C101",
        "content": "Linguistic diversity among the Trojan epikouroi is at issue, rather than any hard dividing line of language between Akhaian and non-Akhaian",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 305,
        "verbatim_quote": "Here, as elsewhere, linguistic diversity among the Trojan ἐπίκουροι is at issue, rather than any hard dividing line of language between Akhaian and non-Akhaian",
        "supporting_evidence": ["E003", "E004"],
        "related_implicit_arguments": []
    }
]

section_evidence = [
    {
        "id": "E003",
        "content": "Iliad 2.802-6: Hektor dispatches commanders to lead their own polis contingents because of different tongues among the wide-strewn human race",
        "evidence_type": "primary_source",
        "page": 303,
        "verbatim_quote": "πολλοὶ γὰρ κατὰ ἄστυ μέγα Πριάμου ἐπίκουροι, / ἄλλη δ᾽ ἄλλων γλῶσσα πολυσπερέων ἀνθρώπων: / τοῖσιν ἕκαστος ἀνὴρ σημαινέτω οἷσί περ ἄρχει, / τῶν δ᾽ ἐξηγείσθω κοσμησάμενος πολιήτας.",
        "source": "Homer, Iliad 2.802-6",
        "related_claims": ["C082", "C083", "C084", "C085", "C086", "C087", "C088", "C089", "C090", "C091", "C101"]
    },
    {
        "id": "E004",
        "content": "Iliad 2.867-69: Nastes led the barbarophonoi Karians who held Miletos and surrounding regions",
        "evidence_type": "primary_source",
        "page": 304,
        "verbatim_quote": "Νάστης αὖ Καρῶν ἡγήσατο βαρβαροφώνων, / οἳ Μίλητον ἔχον Φθιρῶν τ᾽ ὄρος ἀκριτόφυλλον / Μαιάνδρου τε ῥοὰς Μυκάλης τ᾽ αἰπεινὰ κάρηνα.",
        "source": "Homer, Iliad 2.867-69",
        "related_claims": ["C082", "C083", "C092", "C093", "C094", "C096", "C098", "C099", "C100", "C101"]
    }
]

section_implicit_arguments = [
    {
        "id": "IA010",
        "content": "In Homeric society, political/residential community (polis) and linguistic community are assumed to be coterminous",
        "claim_type": "social_assumption",
        "page": 304,
        "trigger_text": "It is assumed that all members of a single πόλις community... speak the same language, but that language barriers may arise between πόλεις",
        "inference_reasoning": "Ross identifies an unstated assumption in the Iliad that linguistic boundaries align with political boundaries (polis membership). This is an inference from the text's structure (Hektor dispatching leaders to their respective poleis) rather than an explicit statement. The assumption reveals Homeric conceptions of the relationship between political and linguistic identity.",
        "related_claims": ["C088", "C089", "C091"]
    },
    {
        "id": "IA011",
        "content": "Language is subordinate to polis-identity and military organisation as markers of identity in the Iliad",
        "claim_type": "interpretive_framework",
        "page": 304,
        "trigger_text": "linguistic variation among the ἐπίκουροι follows the contours of other aspects of identity more frequently invoked by Homer... πόλις and military contingent",
        "inference_reasoning": "Ross argues that language doesn't define identity groups independently but rather maps onto more fundamental categories (polis and military contingent). This hierarchical relationship between identity markers is Ross's analytical framework rather than something explicitly stated in the text. It suggests that Homer conceives of language as an attribute of groups defined by other criteria.",
        "related_claims": ["C090", "C091"]
    },
    {
        "id": "IA012",
        "content": "The term barbarophonos in the Iliad denotes strangeness/alterity generally rather than specifically non-Greek identity",
        "claim_type": "semantic_interpretation",
        "page": 304,
        "trigger_text": "does not denote merely non-Greek... but instead carries the force of strange speech more generally, since every other passage... refers not to a divide between Akhaians and non-Akhaian divisions",
        "inference_reasoning": "Ross infers the semantic range of barbarophonos from the pattern of language use across the Iliad rather than from the word itself. The argument that it means 'strange' generally (rather than 'non-Greek' specifically) depends on comparative analysis of all language passages. This interpretation counters potential anachronistic readings that would import later Greek-barbarian dichotomies back into Homer.",
        "related_claims": ["C096", "C097", "C098"]
    }
]

# Add new items to extraction data
print(f"Adding {len(section_claims)} claims from Section 4...")
data['claims'].extend(section_claims)

print(f"Adding {len(section_evidence)} evidence items from Section 4...")
data['evidence'].extend(section_evidence)

print(f"Adding {len(section_implicit_arguments)} implicit arguments from Section 4...")
data['implicit_arguments'].extend(section_implicit_arguments)

# Update timestamp
data['extraction_timestamp'] = datetime.now(timezone.utc).isoformat()

# Write updated data
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print()
print("=" * 80)
print("PASS 1 - SECTION 4 COMPLETE")
print("=" * 80)
print()
print(f"Section 4: Iliad Evidence Part 1 (pp. 303-304)")
print(f"  Claims: {len(section_claims)}")
print(f"  Evidence: {len(section_evidence)}")
print(f"  Implicit Arguments: {len(section_implicit_arguments)}")
print(f"  Total items: {len(section_claims) + len(section_evidence) + len(section_implicit_arguments)}")
print()
print(f"Running total: {len(data['claims'])} claims, {len(data['evidence'])} evidence, {len(data['implicit_arguments'])} implicit_arguments")
print("=" * 80)
