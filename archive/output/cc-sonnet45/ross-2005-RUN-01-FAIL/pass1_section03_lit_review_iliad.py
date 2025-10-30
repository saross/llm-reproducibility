#!/usr/bin/env python3
"""
Pass 1: Liberal Claims & Evidence Extraction
Section 3: Literature Review Part 2 - Scholarly Positions on the Iliad
Pages 302-303, ~600 words

Extracts claims, evidence, and implicit arguments from the literature review
discussing scholarly positions specifically about Panhellenism in the Iliad.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

extraction_file = Path("extraction.json")

print("=" * 80)
print("PASS 1 - SECTION 3: Literature Review Part 2")
print("Pages 302-303: Scholarly Positions on the Iliad")
print("=" * 80)
print()

# Read current extraction data
with open(extraction_file) as f:
    data = json.load(f)

# Section 3 extraction: Scholarly positions on Panhellenism in the Iliad
section_claims = [
    {
        "id": "C058",
        "content": "The Iliad seems poised to reveal what early Greeks thought of their collective identity and the differences between themselves and non-Greeks, given its subject matter of a united Akhaian army besieging a non-Akhaian city",
        "claim_type": "research_positioning",
        "claim_status": "explicit",
        "page": 302,
        "verbatim_quote": "judging from its subject—a war between a united Akhaian army besieging a non-Akhaian city—the poem seems poised to reveal what early Greeks thought of their collective identity and the differences between themselves and non-Greeks",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C059",
        "content": "The picture of Panhellenism that emerges from the Iliad is ambiguous enough to spark considerable disagreement among scholars",
        "claim_type": "scholarly_observation",
        "claim_status": "explicit",
        "page": 302,
        "verbatim_quote": "The picture that emerges from the epic is ambiguous enough, however, to spark considerable disagreement",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C060",
        "content": "No one argues for a mature Panhellenism in the Iliad or in the late Dark Age or early Archaic period more broadly",
        "claim_type": "scholarly_consensus",
        "claim_status": "explicit",
        "page": 302,
        "verbatim_quote": "Although no one argues for a mature Panhellenism in the Iliad (or in the late Dark Age or early Archaic period more broadly)",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C061",
        "content": "A wide gulf separates scholars who demand evidence for a well-developed sense of Greek versus Other before admitting the saliency of Panhellenism, and those who already see a shared Hellenic identity superseding intra-Hellenic diversity in the epics",
        "claim_type": "historiographical_observation",
        "claim_status": "explicit",
        "page": 302,
        "verbatim_quote": "a wide gulf still separates scholars who demand evidence for a well-developed sense of Greek versus Other before admitting the saliency of Panhellenism, and those who already see a shared Hellenic identity superseding intra-Hellenic social and cultural diversity in the epics",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA008"]
    },
    {
        "id": "C062",
        "content": "In the Classical Era, language was central to Panhellenism",
        "claim_type": "historical_observation",
        "claim_status": "explicit",
        "page": 302,
        "verbatim_quote": "In the Classical Era, language was central to Panhellenism",
        "supporting_evidence": ["E002"],
        "related_implicit_arguments": []
    },
    {
        "id": "C063",
        "content": "Herodotus considers speaking a single tongue to be one of the three central elements of Hellenic identity, along with shared customs and a common religion",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 302,
        "verbatim_quote": "Herodotus considers speaking a single tongue to be one of the three central elements of Hellenic identity, along with shared customs and a common religion",
        "supporting_evidence": ["E002"],
        "related_implicit_arguments": []
    },
    {
        "id": "C064",
        "content": "Implicit in Herodotus' observation is the belief that those who do not speak Greek differ fundamentally from those who do",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 302,
        "verbatim_quote": "Implicit in Herodotus' observation is the belief that those who do not speak Greek differ fundamentally from those who do",
        "supporting_evidence": ["E002"],
        "related_implicit_arguments": []
    },
    {
        "id": "C065",
        "content": "If 'we' are united by language, then 'we' must be divided from 'them', the others who do not speak our language",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 302,
        "verbatim_quote": "if \"we\" are united by language, then \"we\" must be divided from \"them,\" the others who do not speak our language",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C066",
        "content": "Just as the entire concept of Panhellenism is problematic in earlier Greek history, the role of language in the formation of a shared Hellenic identity in the late Dark Age and Archaic period is controversial",
        "claim_type": "scholarly_observation",
        "claim_status": "explicit",
        "page": 302,
        "verbatim_quote": "Just as the entire concept of Panhellenism is problematic in earlier Greek history, however, the role of language in the formation of a shared Hellenic identity in the late Dark Age and Archaic period is controversial",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C067",
        "content": "Scholarly opinion on language and Hellenic identity ranges from the contention that dialect variation caused strong intra-Hellenic divisions, to the belief that communication among Greek-speakers was unimpeded by dialect and that the Greek language fostered cultural unity from an early date",
        "claim_type": "historiographical_observation",
        "claim_status": "explicit",
        "page": 303,
        "verbatim_quote": "Opinion ranges from the contention that dialect variation caused strong intra-Hellenic divisions, to the belief that communication among Greek-speakers was unimpeded by dialect and that the Greek language fostered cultural unity from an early date",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA009"]
    },
    {
        "id": "C068",
        "content": "In the Iliad, the depiction of language—when interpreters are necessary; who speak directly with one another unimpeded; what overall importance attaches language to identity—reveals a situation that consistently differentiates between Akhaians and others without establishing a strict opposition",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 303,
        "verbatim_quote": "In the Iliad, the depiction of language—when interpreters are necessary; who speak directly with one another unimpeded; what overall importance attaches language to identity—reveals a situation that consistently differentiates between Akhaians and others without establishing a strict opposition",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C069",
        "content": "Just as the existence of a multiplicity of common names for Homer's 'Greeks'—Akhaians, Danaans, Argives—sheds light on the tension between unity and diversity among the Akhaians, the linguistic landscape of the Iliad provides a window into the complex nature of identity in the epics",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 303,
        "verbatim_quote": "Just as the existence of a multiplicity of common names for Homer's \"Greeks\"—Akhaians, Danaans, Argives—sheds light on the tension between unity and diversity among the Akhaians, the linguistic landscape of the Iliad provides a window into the complex nature of identity in the epics",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C070",
        "content": "The linguistic landscape of the Iliad provides insight into identity among the Greeks of the late eighth century BCE",
        "claim_type": "research_positioning",
        "claim_status": "explicit",
        "page": 303,
        "verbatim_quote": "the linguistic landscape of the Iliad provides a window into the complex nature of identity in the epics, and among the Greeks of the late eighth century b.c.e.",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C071",
        "content": "Cartledge argues against any sense of Panhellenism in Homer based largely on the lack of the term 'barbarian' or an equivalent",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 302,
        "verbatim_quote": "Based largely on the lack of the term \"barbarian\" or an equivalent, Cartledge (1993, 12) argues against any sense of Panhellenism in Homer",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C072",
        "content": "Konstan contends that the contrast between civilised and uncivilised worlds underlying Books 9-12 of the Odyssey is never conceived of in terms of Greek versus non-Greek",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 302,
        "verbatim_quote": "Konstan (2001) extends this line of thought, contending that the contrast between civilized and uncivilized worlds underlying Books 9–12 of the Odyssey is never conceived of in terms of Greek versus non-Greek",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C073",
        "content": "It seems impossible, on the basis of the epics themselves, to discriminate Greeks from non-Greeks on the basis of language, religion, customs, geography, or even genealogy",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 302,
        "verbatim_quote": "It seems impossible, on the basis of the epics themselves, to discriminate Greeks from non-Greeks\" on the basis of language, religion, customs, geography, or even genealogy",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C074",
        "content": "Achaeans and only Achaeans mobilise to carry on the siege of Troy, whereas Priam draws his allies from among only non-Achaean populations",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 302,
        "verbatim_quote": "Achaeans and only Achaeans who mobilize to carry on the siege of Troy, whereas Priam draws his allies from among [only] non-Achaean populations",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C075",
        "content": "Finley both respects the heterogeneity of Homer's Akhaians and sees in the epics the beginnings of Greekness",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 302,
        "verbatim_quote": "Finley (1979, 18) both respects the heterogeneity of Homer's Akhaians and sees in the epics the beginnings of Greekness",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C076",
        "content": "Homer's use of multiple common names for the Akhaians is a metaphor for early Panhellenism",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 302,
        "verbatim_quote": "He sees Homer's use of (multiple) common names for the Akhaians as a metaphor for early Panhellenism",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C077",
        "content": "The presence of a common name (or names) for the Akhaians is a symbol that Greek history proper had been launched",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 302,
        "verbatim_quote": "The presence of a common name (or names) is a symbol that Greek history proper had been launched",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C078",
        "content": "There is more than one common name for the Akhaians, which serves as a symbol of the social and cultural diversity which characterised Hellas both in its infancy and throughout its history",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 302,
        "verbatim_quote": "But there was more than one name, and that serves as a symbol, too, of the social and cultural diversity which characterized Hellas both in its infancy and throughout its history",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C079",
        "content": "There are no local, regional, or national dividing lines of genuine consequence in Homer",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 302,
        "verbatim_quote": "there are no local, regional, or national dividing lines of genuine consequence in Homer",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C080",
        "content": "While individuals and classes vary in capacity in Homer, peoples do not",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 302,
        "verbatim_quote": "while individuals and classes vary in capacity, peoples do not",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C081",
        "content": "Mackie argues for 'complex unity' of the Greek army before Troy",
        "claim_type": "scholarly_interpretation",
        "claim_status": "explicit",
        "page": 302,
        "verbatim_quote": "compare Mackie (1996, chap. 1, esp. p. 20), where she argues for \"complex unity\" of the Greek army before Troy",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    }
]

section_evidence = [
    {
        "id": "E002",
        "content": "Herodotus 8.144: Speaking a single tongue is one of three central elements of Hellenic identity",
        "evidence_type": "primary_source",
        "page": 302,
        "verbatim_quote": "Hdt. 8.144",
        "source": "Herodotus",
        "related_claims": ["C062", "C063", "C064"]
    }
]

section_implicit_arguments = [
    {
        "id": "IA008",
        "content": "The scholarly debate about Panhellenism in Homer hinges on definitional thresholds for what counts as 'Panhellenic'",
        "claim_type": "methodological_observation",
        "page": 302,
        "trigger_text": "a wide gulf still separates scholars who demand evidence for a well-developed sense of Greek versus Other... and those who already see a shared Hellenic identity",
        "inference_reasoning": "Ross identifies a fundamental divide not just in conclusions but in evidentiary standards. The phrases 'demand evidence for a well-developed sense' versus 'already see' suggest that scholars are operating with different definitional thresholds for what qualifies as Panhellenism. This meta-analytical observation about scholarly disagreement is Ross's interpretive framework rather than something explicitly stated by the scholars under discussion.",
        "related_claims": ["C061", "C071", "C072", "C073", "C075"]
    },
    {
        "id": "IA009",
        "content": "Debates about dialect and linguistic unity in Archaic Greece parallel broader debates about the nature and timing of Panhellenism",
        "claim_type": "methodological_observation",
        "page": 302,
        "trigger_text": "Opinion ranges from the contention that dialect variation caused strong intra-Hellenic divisions, to the belief that communication among Greek-speakers was unimpeded by dialect",
        "inference_reasoning": "Ross draws a parallel between two scholarly debates: one about language/dialect and one about Panhellenism. The parallel structure ('just as... however') implies that these are related manifestations of the same underlying historiographical problem. This connection between linguistic and political/cultural unity debates is Ross's analytical insight rather than an explicit claim by the scholars cited.",
        "related_claims": ["C066", "C067", "C068"]
    }
]

# Add new items to extraction data
print(f"Adding {len(section_claims)} claims from Section 3...")
data['claims'].extend(section_claims)

print(f"Adding {len(section_evidence)} evidence items from Section 3...")
data['evidence'].extend(section_evidence)

print(f"Adding {len(section_implicit_arguments)} implicit arguments from Section 3...")
data['implicit_arguments'].extend(section_implicit_arguments)

# Update timestamp
data['extraction_timestamp'] = datetime.now(timezone.utc).isoformat()

# Write updated data
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print()
print("=" * 80)
print("PASS 1 - SECTION 3 COMPLETE")
print("=" * 80)
print()
print(f"Section 3: Literature Review Part 2 (pp. 302-303)")
print(f"  Claims: {len(section_claims)}")
print(f"  Evidence: {len(section_evidence)}")
print(f"  Implicit Arguments: {len(section_implicit_arguments)}")
print(f"  Total items: {len(section_claims) + len(section_evidence) + len(section_implicit_arguments)}")
print()
print(f"Running total: {len(data['claims'])} claims, {len(data['evidence'])} evidence, {len(data['implicit_arguments'])} implicit_arguments")
print("=" * 80)
