#!/usr/bin/env python3
"""
Pass 1: Liberal Extraction - Section 1
Ross 2005 - Barbarophonos

Section 1: Introduction & Methodological Framework (pages 299-301)
~950 words
Content: Research problem, linguistic approach, dating debate, oral tradition theory
"""

import json
from datetime import datetime, timezone

# Load extraction.json
with open('/home/shawn/Code/llm-reproducibility/outputs/ross-2005/extraction.json', 'r') as f:
    data = json.load(f)

# Section 1 items
section_claims = [
    {
        "id": "C001",
        "content": "The extent of Panhellenism in early Archaic Greece provokes considerable disagreement among scholars",
        "claim_type": "scholarly_context",
        "claim_status": "explicit",
        "page": 299,
        "verbatim_quote": "THE EXTENT OF PANHELLENISM in early Archaic Greece provokes considerable disagreement.",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C002",
        "content": "Full-fledged Panhellenism had emerged by the beginning of the Classical period",
        "claim_type": "scholarly_consensus",
        "claim_status": "explicit",
        "page": 299,
        "verbatim_quote": "Although it is widely agreed that full-fledged Panhellenism had emerged by the beginning of the Classical period",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C003",
        "content": "The nature—and even the very existence—of earlier proto-Panhellenism remains the subject of debate",
        "claim_type": "scholarly_context",
        "claim_status": "explicit",
        "page": 299,
        "verbatim_quote": "the nature—and even the very existence—of earlier proto-Panhellenism remains the subject of debate",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C004",
        "content": "Language is one important component of mature Panhellenism",
        "claim_type": "conceptual_framework",
        "claim_status": "explicit",
        "page": 299,
        "verbatim_quote": "Examination of one important component of mature Panhellenism—language",
        "supporting_evidence": ["E001"],
        "related_implicit_arguments": []
    },
    {
        "id": "C005",
        "content": "The Iliad is arguably the earliest available literary source for examining Panhellenism",
        "claim_type": "methodological_rationale",
        "claim_status": "explicit",
        "page": 299,
        "verbatim_quote": "in what is arguably the earliest available literary source, the Iliad",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA001"]
    },
    {
        "id": "C006",
        "content": "Examination of language in the Iliad should serve to illuminate the extent and saliency of Panhellenic identity in the eighth century BCE",
        "claim_type": "research_purpose",
        "claim_status": "explicit",
        "page": 299,
        "verbatim_quote": "should serve to illuminate the extent and saliency of Panhellenic identity in the eighth century b.c.e.",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA001"]
    },
    {
        "id": "C007",
        "content": "The speaking of different languages is only rarely acknowledged in early epic poetry, including the Iliad",
        "claim_type": "textual_observation",
        "claim_status": "explicit",
        "page": 299,
        "verbatim_quote": "Although the speaking of different languages is only rarely acknowledged in early epic poetry, the Iliad included",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C008",
        "content": "The instances of linguistic diversity that do occur in the Iliad follow a consistent pattern",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 299,
        "verbatim_quote": "the instances of linguistic diversity that do occur in the Iliad follow a consistent pattern",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C009",
        "content": "Akhaians and Trojans communicate freely with one another in the Iliad",
        "claim_type": "textual_interpretation",
        "claim_status": "explicit",
        "page": 299,
        "verbatim_quote": "Akhaians and Trojans communicate freely with one another",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C010",
        "content": "No hard linguistic dividing line between Akhaians and others emerges over the course of the Iliad",
        "claim_type": "textual_interpretation",
        "claim_status": "explicit",
        "page": 299,
        "verbatim_quote": "no hard linguistic dividing line between Akhaians and others emerges over the course of the epic",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C011",
        "content": "The later, categorical Greek-Barbarian dichotomy has not yet emerged in the Iliad",
        "claim_type": "textual_interpretation",
        "claim_status": "explicit",
        "page": 299,
        "verbatim_quote": "nor does it appear that the later, categorical Greek-Barbarian dichotomy has yet emerged",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C012",
        "content": "Through poetic emphasis or suppression, linguistic diversity is limited to the Trojan epikouroi defending the city",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 299,
        "verbatim_quote": "through poetic emphasis or suppression, linguistic diversity is limited to the Trojan ἐπίκουροι (allies or companions) defending the city",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C013",
        "content": "Linguistic diversity is absent from the Akhaian forces besieging Troy",
        "claim_type": "textual_interpretation",
        "claim_status": "explicit",
        "page": 299,
        "verbatim_quote": "while it is absent from the Akhaian forces besieging Troy",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C014",
        "content": "The differential treatment of Akhaian and Trojan forces reveals a notion of 'pan-Akhaian' linguistic uniformity, distinct from the cacophony of the Trojan host",
        "claim_type": "interpretive_claim",
        "claim_status": "explicit",
        "page": 299,
        "verbatim_quote": "This differential treatment of Akhaian and Trojan forces reveals a notion of \"pan-Akhaian\" linguistic uniformity, distinct from the cacophony of the Trojan host",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C015",
        "content": "The selective recognition of linguistic diversity indicates the coalescing of a non-oppositional but shared Greek identity",
        "claim_type": "historical_interpretation",
        "claim_status": "explicit",
        "page": 299,
        "verbatim_quote": "perhaps indicating the coalescing of a non-oppositional but shared Greek identity",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C016",
        "content": "The selective recognition of linguistic diversity among Trojan epikouroi, versus the homogeneity of the Akhaians, offers a glimpse of an undeveloped and unstable proto-Panhellenism",
        "claim_type": "historical_interpretation",
        "claim_status": "explicit",
        "page": 299,
        "verbatim_quote": "the selective recognition of linguistic diversity among Trojan ἐπίκουροι, versus the homogeneity of the Akhaians, offers a glimpse of an undeveloped and unstable proto-Panhellenism",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C017",
        "content": "Opinion varies widely on both the date when Homer's poems reached more or less their final form and the date of the society from which the world of the epics is principally drawn",
        "claim_type": "scholarly_context",
        "claim_status": "explicit",
        "page": 299,
        "verbatim_quote": "Opinion varies widely on both issues.",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C018",
        "content": "The dating controversy concerning Homer is complex and involved—and perhaps ultimately irresolvable or even irrelevant",
        "claim_type": "methodological_positioning",
        "claim_status": "explicit",
        "page": 300,
        "verbatim_quote": "The controversy is complex and involved—and perhaps ultimately irresolvable or even irrelevant.",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C019",
        "content": "The poems as we have them substantially preserve versions current during the late eighth century, with the Iliad perhaps somewhat earlier than the Odyssey",
        "claim_type": "dating_position",
        "claim_status": "explicit",
        "page": 300,
        "verbatim_quote": "I believe, however, that the poems as we have them substantially preserve versions current during the late eighth century, with the Iliad perhaps somewhat earlier than the Odyssey.",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C020",
        "content": "Ross adopts late eighth century dating because the epics appear linguistically earlier than other Greek poetry",
        "claim_type": "dating_rationale",
        "claim_status": "explicit",
        "page": 300,
        "verbatim_quote": "I have settled on these dates not only because the epics appear, linguistically, to be earlier than other Greek poetry",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C021",
        "content": "By about 700 BCE the poems were so widely diffused that opportunities for recomposition would have been limited by the expectations of a large, diverse, and informed audience",
        "claim_type": "oral_tradition_theory",
        "claim_status": "explicit",
        "page": 300,
        "verbatim_quote": "that by about 700 b.c.e. the poems were so widely diffused that opportunities for recomposition would have been limited by the expectations of a large, diverse, and informed audience",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA002"]
    },
    {
        "id": "C022",
        "content": "The world depicted in the Iliad and Odyssey reflects, with some exceptions, common aspects of Greek-speaking civilization during the three generations leading up to when the poems' content stabilized",
        "claim_type": "dating_position",
        "claim_status": "explicit",
        "page": 300,
        "verbatim_quote": "I consider the world depicted in the Iliad and Odyssey to reflect, with some exceptions, common aspects of Greek-speaking civilization during the three generations leading up to the time when the poems' content stabilized.",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA002"]
    },
    {
        "id": "C023",
        "content": "The rise of Panhellenic sentiments as reflected in linguistic patterns in the Iliad reflects the historical moment when the poems reached their present form, around the turn of the eighth century",
        "claim_type": "interpretive_framework",
        "claim_status": "explicit",
        "page": 300,
        "verbatim_quote": "More specifically, the features of interest in this paper—the rise of Panhellenic sentiments as reflected in the speaking of different languages in the Iliad—reflect the historical moment when the poems reached their present form, around the turn of the eighth century.",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA002", "IA003"]
    },
    {
        "id": "C024",
        "content": "Oral tradition assimilates, forgets, and modifies different types of information at different rates",
        "claim_type": "oral_tradition_theory",
        "claim_status": "explicit",
        "page": 300,
        "verbatim_quote": "Oral tradition assimilates, forgets, and modifies different types of information at different rates.",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C025",
        "content": "Physical things (objects or places) are much more durable in oral tradition than institutions and relationships",
        "claim_type": "oral_tradition_theory",
        "claim_status": "explicit",
        "page": 300,
        "verbatim_quote": "Physical things, be they objects or places, are much more durable in oral tradition",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C026",
        "content": "The appearance of boars' tusk helmets and the preeminence of Mycenae in the Iliad illustrate the durability of physical things in oral tradition",
        "claim_type": "oral_tradition_theory",
        "claim_status": "explicit",
        "page": 300,
        "verbatim_quote": "hence the appearance of boars' tusk helmets and the preeminence of Mycenae in the Iliad",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C027",
        "content": "Oral tradition only tends to retain information about institutions and relationships so long as they are immediately relevant to the poet's audience or relate directly to contemporary social structures",
        "claim_type": "oral_tradition_theory",
        "claim_status": "explicit",
        "page": 300,
        "verbatim_quote": "so long as it is evolving through recomposition, oral tradition only tends to retain information about institutions and relationships so long as they are immediately relevant to the poet's audience or relate directly to contemporary social structures",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA003"]
    },
    {
        "id": "C028",
        "content": "Abstractions like institutions and relationships are often manipulated by the poet to explain or justify contemporary conditions, express group identity, or legitimize rights and privileges",
        "claim_type": "oral_tradition_theory",
        "claim_status": "explicit",
        "page": 300,
        "verbatim_quote": "Furthermore, such abstractions are often manipulated by the poet to explain or justify contemporary conditions, express group identity, or legitimize rights and privileges.",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA003"]
    },
    {
        "id": "C029",
        "content": "Precise linguistic arrangements evolve rapidly through recomposition until the epics became relatively fixed due to wide dispersion and audience expectations",
        "claim_type": "oral_tradition_theory",
        "claim_status": "explicit",
        "page": 300-301,
        "verbatim_quote": "Precise linguistic arrangements (and the epics are very consistent in this regard) represent just such an abstraction, evolving rapidly through recomposition until the epics became relatively fixed due to wide dispersion and concomitant audience expectations.",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA003"]
    },
    {
        "id": "C030",
        "content": "Linguistic arrangements in the Iliad likely reflect the present of poet and audience around the time of stabilization, shaped by contemporary conditions, needs, and ideas",
        "claim_type": "interpretive_framework",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "Thus, linguistic arrangements in the Iliad likely reflect the present of poet and audience around the time of stabilization, shaped by contemporary conditions, needs, and ideas.",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA002", "IA003"]
    },
    {
        "id": "C031",
        "content": "The Iliad is the product of an oral tradition that stabilized in approximately its current form circa 700 BCE",
        "claim_type": "dating_position",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "the Iliad is the product of an oral tradition that stabilized in approximately its current form circa 700 b.c.e.",
        "supporting_evidence": [],
        "related_implicit_arguments": []
    },
    {
        "id": "C032",
        "content": "Due to the nature of oral tradition, the Iliad for the most part reflects beliefs about language and identity roughly contemporary with the moment of stabilization",
        "claim_type": "interpretive_framework",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "Due to the nature of oral tradition, the poem for the most part reflects beliefs about language and identity roughly contemporary with the moment of stabilization.",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA002", "IA003"]
    },
    {
        "id": "C033",
        "content": "Ross will attempt to interpret the linguistic situation in the Iliad as it would have been understood by poet and audience at about the time of stabilization, around the turn of the eighth century",
        "claim_type": "methodological_approach",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "I will attempt to interpret the linguistic situation in the Iliad as it would have been understood by poet and audience at about the time of stabilization, around the turn of the eighth century.",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA004"]
    },
    {
        "id": "C034",
        "content": "Assigning an understanding that equates Akhaians with Greeks and Trojans with barbarians to an eighth-century BCE performance is anachronistic and unsupported by the linguistic situation depicted in the epics",
        "claim_type": "methodological_critique",
        "claim_status": "explicit",
        "page": 301,
        "verbatim_quote": "Even though later Greeks—after the Persian Wars, perhaps—may have directly equated Akhaians with Greeks and Trojans with barbarians as they heard or read the Iliad, assigning such an understanding of identity to an eighth-century b.c.e. performance is anachronistic, unsupported by the linguistic situation depicted in the epics.",
        "supporting_evidence": [],
        "related_implicit_arguments": ["IA004"]
    }
]

section_evidence = [
    {
        "id": "E001",
        "content": "In the Classical Era, Herodotus considers speaking a single tongue to be one of the three central elements of Hellenic identity, along with shared customs and a common religion",
        "evidence_type": "scholarly_citation",
        "evidence_status": "explicit",
        "page": 302,
        "verbatim_quote": "In the Classical Era, language was central to Panhellenism. Herodotus considers speaking a single tongue to be one of the three central elements of Hellenic identity, along with shared customs and a common religion.",
        "evidence_source": "Herodotus 8.144",
        "supports_claims": ["C004"]
    }
]

section_implicit_arguments = [
    {
        "id": "IA001",
        "content": "If the Iliad is the earliest available literary source, then linguistic patterns in it provide the best evidence for eighth-century Panhellenic identity formation",
        "page": 299,
        "trigger_text": "Examination of one important component of mature Panhellenism—language—in what is arguably the earliest available literary source, the Iliad, should serve to illuminate the extent and saliency of Panhellenic identity in the eighth century b.c.e.",
        "inference_reasoning": "Ross assumes that because the Iliad is earliest, it is most reliable for understanding proto-Panhellenism. This assumes that earlier sources are better sources for understanding early periods, without explicitly defending this methodological choice against alternatives (e.g., later sources might preserve earlier traditions, or comparative evidence from other genres).",
        "related_claims": ["C005", "C006"]
    },
    {
        "id": "IA002",
        "content": "Wide diffusion of oral poems creates audience expectations that prevent significant changes to content, effectively 'freezing' the tradition",
        "claim_type": "oral_tradition_assumption",
        "page": 300,
        "trigger_text": "by about 700 b.c.e. the poems were so widely diffused that opportunities for recomposition would have been limited by the expectations of a large, diverse, and informed audience",
        "inference_reasoning": "Ross adopts Nagy's theory that wide diffusion limits recomposition, but this is a theoretical assumption about how oral tradition works. The mechanism by which audience expectations constrain oral poets is not empirically demonstrated, only theorized. This assumption is critical to dating the Iliad's content to ca. 700 BCE.",
        "related_claims": ["C021", "C022", "C023", "C030", "C032"]
    },
    {
        "id": "IA003",
        "content": "Linguistic arrangements in oral poetry are abstractions that reflect contemporary social structures and identity concepts rather than historical memory",
        "claim_type": "oral_tradition_assumption",
        "page": 300-301,
        "trigger_text": "Precise linguistic arrangements (and the epics are very consistent in this regard) represent just such an abstraction, evolving rapidly through recomposition until the epics became relatively fixed",
        "inference_reasoning": "Ross argues that linguistic patterns are abstractions that evolve rapidly to reflect contemporary conditions, unlike durable physical objects. This assumes a sharp distinction between 'physical things' and 'abstractions' in oral tradition, and assumes that the Iliad's linguistic patterns were actively shaped by eighth-century concerns rather than inherited from earlier tradition. This unstated assumption is crucial to interpreting linguistic patterns as evidence for eighth-century proto-Panhellenism.",
        "related_claims": ["C023", "C027", "C028", "C029", "C030", "C032"]
    },
    {
        "id": "IA004",
        "content": "Later Greek interpretations of the Iliad (post-Persian Wars) should not be projected back onto eighth-century understanding of the poem",
        "claim_type": "methodological_assumption",
        "page": 301,
        "trigger_text": "Even though later Greeks—after the Persian Wars, perhaps—may have directly equated Akhaians with Greeks and Trojans with barbarians as they heard or read the Iliad, assigning such an understanding of identity to an eighth-century b.c.e. performance is anachronistic",
        "inference_reasoning": "Ross assumes that eighth-century audiences understood the Iliad differently from Classical-era audiences, and that we can reconstruct this earlier understanding. This requires assuming that we can distinguish layers of interpretation and identify what is 'original' versus what is 'later reading'. The method for making this distinction is not made explicit.",
        "related_claims": ["C033", "C034"]
    }
]

# Add items to data
data['claims'].extend(section_claims)
data['evidence'].extend(section_evidence)
data['implicit_arguments'].extend(section_implicit_arguments)

# Update timestamp
data['extraction_timestamp'] = datetime.now(timezone.utc).isoformat()

# Save
with open('/home/shawn/Code/llm-reproducibility/outputs/ross-2005/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print("=" * 80)
print("PASS 1 - SECTION 1 COMPLETE")
print("=" * 80)
print(f"Section 1: Introduction & Methodological Framework (pp. 299-301)")
print(f"  Claims: {len(section_claims)}")
print(f"  Evidence: {len(section_evidence)}")
print(f"  Implicit Arguments: {len(section_implicit_arguments)}")
print(f"  Total items: {len(section_claims) + len(section_evidence) + len(section_implicit_arguments)}")
print()
print(f"Running total: {len(data['claims'])} claims, {len(data['evidence'])} evidence, {len(data['implicit_arguments'])} implicit_arguments")
print("=" * 80)
