#!/usr/bin/env python3
"""
Pass 1 - Section 1: Abstract + Introduction (pp. 299-301, ~1300 words)

Extracts evidence, claims, and implicit arguments from:
- Abstract (main argument summary)
- Introduction (dating framework, oral tradition theory)

Section characteristics:
- No primary source citations yet (those start in Section 3)
- Scholarly debate positioning (Nagy, Finley, Morris, Vansina)
- Ross's methodological framework and dating assumptions
- High implicit argument density (dating, oral tradition dynamics)

Target extraction: 12-15 claims, 1-2 evidence, 3-5 implicit arguments
"""

import json
from pathlib import Path

# Read current extraction
extraction_path = Path("outputs/ross-2005/extraction.json")
with open(extraction_path, 'r', encoding='utf-8') as f:
    extraction = json.load(f)

# Section 1: Evidence
# Limited evidence in this section - mostly theoretical framing
evidence_section1 = []

# No primary ancient text citations in Abstract/Intro
# Evidence will start in Section 3 with Iliad passages

# Section 1: Claims
claims_section1 = [
    {
        "id": "C001",
        "content": "The extent of Panhellenism in early Archaic Greece provokes considerable disagreement among scholars",
        "claim_type": "contextualization",
        "claim_role": "intermediate",
        "page": 299,
        "verbatim_quote": "he extent of panhellenism in early Archaic Greece provokes considerable disagreement.",
        "supporting_evidence": [],
        "related_claims": ["C002", "C003"]
    },
    {
        "id": "C002",
        "content": "Full-fledged Panhellenism had emerged by the beginning of the Classical period (widely agreed)",
        "claim_type": "scholarly_consensus",
        "claim_role": "supporting",
        "page": 299,
        "verbatim_quote": "Although it is widely agreed that full-ﬂedged Panhellenism had emerged by the beginning of the Classical period, the nature—and even the very existence—of earlier proto-Panhellenism remains the subject of debate.",
        "supporting_evidence": [],
        "related_claims": ["C001", "C003"]
    },
    {
        "id": "C003",
        "content": "The nature and even the very existence of earlier proto-Panhellenism remains subject of debate",
        "claim_type": "problem_statement",
        "claim_role": "core",
        "page": 299,
        "verbatim_quote": "the nature—and even the very existence—of earlier proto-Panhellenism remains the subject of debate.",
        "supporting_evidence": [],
        "related_claims": ["C001", "C002", "C004"]
    },
    {
        "id": "C004",
        "content": "Examination of language in the Iliad should illuminate the extent and saliency of Panhellenic identity in the eighth century BCE",
        "claim_type": "methodological",
        "claim_role": "core",
        "page": 299,
        "verbatim_quote": "Examination of one important component of mature Panhellenism—language—in what is arguably the earliest available literary source, the Iliad, should serve to illuminate the extent and saliency of Panhellenic identity in the eighth century b.c.e.",
        "supporting_evidence": [],
        "related_claims": ["C003", "C005", "C006"]
    },
    {
        "id": "C005",
        "content": "The speaking of different languages is only rarely acknowledged in early epic poetry including the Iliad",
        "claim_type": "observation",
        "claim_role": "supporting",
        "page": 299,
        "verbatim_quote": "Although the speaking of different languages is only rarely acknowledged in early epic poetry, the Iliad included, the instances of linguistic diversity that do occur in the Iliad follow a consistent pattern.",
        "supporting_evidence": [],
        "related_claims": ["C004", "C006"]
    },
    {
        "id": "C006",
        "content": "The instances of linguistic diversity that do occur in the Iliad follow a consistent pattern",
        "claim_type": "pattern_identification",
        "claim_role": "core",
        "page": 299,
        "verbatim_quote": "the instances of linguistic diversity that do occur in the Iliad follow a consistent pattern.",
        "supporting_evidence": [],
        "related_claims": ["C005", "C007", "C010"]
    },
    {
        "id": "C007",
        "content": "Akhaians and Trojans communicate freely with one another in the Iliad",
        "claim_type": "pattern_identification",
        "claim_role": "supporting",
        "page": 299,
        "verbatim_quote": "On the one hand, Akhaians and Trojans communicate freely with one another; no hard linguistic dividing line between Akhaians and others emerges over the course of the epic, nor does it appear that the later, categorical Greek-Barbarian dichotomy has yet emerged.",
        "supporting_evidence": [],
        "related_claims": ["C006", "C008", "C009"]
    },
    {
        "id": "C008",
        "content": "No hard linguistic dividing line between Akhaians and others emerges over the course of the Iliad",
        "claim_type": "pattern_identification",
        "claim_role": "supporting",
        "page": 299,
        "verbatim_quote": "no hard linguistic dividing line between Akhaians and others emerges over the course of the epic",
        "supporting_evidence": [],
        "related_claims": ["C007", "C009"]
    },
    {
        "id": "C009",
        "content": "The later categorical Greek-Barbarian dichotomy has not yet emerged in the Iliad",
        "claim_type": "absence_claim",
        "claim_role": "intermediate",
        "page": 299,
        "verbatim_quote": "nor does it appear that the later, categorical Greek-Barbarian dichotomy has yet emerged.",
        "supporting_evidence": [],
        "related_claims": ["C007", "C008"]
    },
    {
        "id": "C010",
        "content": "Through poetic emphasis or suppression, linguistic diversity is limited to the Trojan epikouroi (allies/companions) defending the city",
        "claim_type": "pattern_identification",
        "claim_role": "core",
        "page": 299,
        "verbatim_quote": "through poetic emphasis or suppression, linguistic diversity is limited to the Trojan ejpÇkouroi (allies or companions) defending the city, while it is absent from the Akhaian forces besieging Troy.",
        "supporting_evidence": [],
        "related_claims": ["C006", "C011", "C012"]
    },
    {
        "id": "C011",
        "content": "Linguistic diversity is absent from the Akhaian forces besieging Troy",
        "claim_type": "pattern_identification",
        "claim_role": "core",
        "page": 299,
        "verbatim_quote": "linguistic diversity is limited to the Trojan ejpÇkouroi (allies or companions) defending the city, while it is absent from the Akhaian forces besieging Troy.",
        "supporting_evidence": [],
        "related_claims": ["C010", "C012"]
    },
    {
        "id": "C012",
        "content": "The differential treatment of Akhaian and Trojan forces reveals a notion of 'pan-Akhaian' linguistic uniformity distinct from the cacophony of the Trojan host",
        "claim_type": "interpretation",
        "claim_role": "core",
        "page": 299,
        "verbatim_quote": "This differential treatment of Akhaian and Trojan forces reveals a notion of \\\"pan-Akhaian\\\" linguistic uniformity, distinct from the cacophony of the Trojan host",
        "supporting_evidence": [],
        "related_claims": ["C010", "C011", "C013"]
    },
    {
        "id": "C013",
        "content": "The differential linguistic treatment perhaps indicates the coalescing of a non-oppositional but shared Greek identity",
        "claim_type": "interpretation",
        "claim_role": "core",
        "page": 299,
        "verbatim_quote": "perhaps indicating the coalescing of a non-oppositional but shared Greek identity.",
        "supporting_evidence": [],
        "related_claims": ["C012", "C014"]
    },
    {
        "id": "C014",
        "content": "The selective recognition of linguistic diversity among Trojan epikouroi versus Akhaian homogeneity offers a glimpse of an undeveloped and unstable proto-Panhellenism",
        "claim_type": "conclusion",
        "claim_role": "core",
        "page": 299,
        "verbatim_quote": "Even though no language barrier separates Akhaians from Trojans in the epics, the selective recognition of linguistic diversity among Trojan ejpÇkouroi, versus the homogeneity of the Akhaians, offers a glimpse of an undeveloped and unstable proto-Panhellenism.",
        "supporting_evidence": [],
        "related_claims": ["C012", "C013"]
    },
    {
        "id": "C015",
        "content": "Anyone employing the Iliad or Odyssey as historical source must grapple with uncertainties over dating of final form and historical society",
        "claim_type": "methodological",
        "claim_role": "supporting",
        "page": 299,
        "verbatim_quote": "Anyone employing the Iliad or Odyssey as an historical source must grapple with two related difﬁculties: uncertainties over the date when the poems reached more or less their ﬁnal form and over the date of the society from which the world of the epics is principally drawn.",
        "supporting_evidence": [],
        "related_claims": ["C016", "C017"]
    },
    {
        "id": "C016",
        "content": "Opinion varies widely on dating of poem composition/finalization and historical society reflected in poems",
        "claim_type": "scholarly_context",
        "claim_role": "supporting",
        "page": 299,
        "verbatim_quote": "Opinion varies widely on both issues.",
        "supporting_evidence": [],
        "related_claims": ["C015"]
    },
    {
        "id": "C017",
        "content": "The dating controversy is complex, involved, and perhaps ultimately irresolvable or even irrelevant",
        "claim_type": "methodological",
        "claim_role": "supporting",
        "page": 300,
        "verbatim_quote": "The controversy is complex and involved—and perhaps ultimately irresolvable or even irrelevant.",
        "supporting_evidence": [],
        "related_claims": ["C015", "C016"]
    },
    {
        "id": "C018",
        "content": "Ross believes the poems as we have them substantially preserve versions current during the late eighth century, with Iliad perhaps somewhat earlier than Odyssey",
        "claim_type": "methodological_position",
        "claim_role": "intermediate",
        "page": 300,
        "verbatim_quote": "I believe, however, that the poems as we have them substantially preserve versions current during the late eighth century, with the Iliad perhaps somewhat earlier than the Odyssey.",
        "supporting_evidence": [],
        "related_claims": ["C019", "C020", "C021"]
    },
    {
        "id": "C019",
        "content": "Ross settled on late eighth century dates because epics appear linguistically to be earlier than other Greek poetry",
        "claim_type": "methodological_justification",
        "claim_role": "supporting",
        "page": 300,
        "verbatim_quote": "I have settled on these dates not only because the epics appear, linguistically, to be earlier than other Greek poetry",
        "supporting_evidence": [],
        "related_claims": ["C018"]
    },
    {
        "id": "C020",
        "content": "Nagy proposed that by about 700 BCE the poems were so widely diffused that opportunities for recomposition would have been limited by expectations of large, diverse, informed audience",
        "claim_type": "theoretical_framework",
        "claim_role": "supporting",
        "page": 300,
        "verbatim_quote": "that by about 700 b.c.e. the poems were so widely diffused that opportunities for recomposition would have been limited by the expectations of a large, diverse, and informed audience.",
        "supporting_evidence": [],
        "related_claims": ["C018", "C021"]
    },
    {
        "id": "C021",
        "content": "Ross considers the world depicted in Iliad/Odyssey to reflect common aspects of Greek-speaking civilization during three generations leading up to content stabilization",
        "claim_type": "methodological_position",
        "claim_role": "intermediate",
        "page": 300,
        "verbatim_quote": "I consider the world depicted in the Iliad and Odyssey to reﬂect, with some exceptions, common aspects of Greek-speaking civilization during the three generations leading up to the time when the poems' content stabilized.",
        "supporting_evidence": [],
        "related_claims": ["C018", "C022"]
    },
    {
        "id": "C022",
        "content": "The features of interest in this paper (rise of Panhellenic sentiments reflected in speaking of different languages in Iliad) reflect the historical moment when poems reached present form around turn of eighth century",
        "claim_type": "methodological_claim",
        "claim_role": "core",
        "page": 300,
        "verbatim_quote": "More speciﬁcally, the features of interest in this paper—the rise of Panhellenic sentiments as reﬂected in the speaking of different languages in the Iliad—reﬂect the historical moment when the poems reached their present form, around the turn of the eighth century.",
        "supporting_evidence": [],
        "related_claims": ["C021", "C023", "C024"]
    },
    {
        "id": "C023",
        "content": "Oral tradition assimilates, forgets, and modifies different types of information at different rates",
        "claim_type": "theoretical_framework",
        "claim_role": "intermediate",
        "page": 300,
        "verbatim_quote": "Oral tradition assimilates, forgets, and modiﬁes different types of information at different rates.",
        "supporting_evidence": [],
        "related_claims": ["C024", "C025"]
    },
    {
        "id": "C024",
        "content": "Physical things (objects or places) are much more durable in oral tradition—hence appearance of boars' tusk helmets and preeminence of Mycenae in Iliad",
        "claim_type": "theoretical_framework",
        "claim_role": "supporting",
        "page": 300,
        "verbatim_quote": "Physical things, be they objects or places, are much more durable in oral tradition—hence the appearance of boars' tusk helmets and the preeminence of Mycenae in the Iliad.",
        "supporting_evidence": [],
        "related_claims": ["C023", "C025"]
    },
    {
        "id": "C025",
        "content": "While evolving through recomposition, oral tradition only tends to retain information about institutions and relationships so long as they are immediately relevant to poet's audience or relate directly to contemporary social structures",
        "claim_type": "theoretical_framework",
        "claim_role": "intermediate",
        "page": 300,
        "verbatim_quote": "By contrast, so long as it is evolving through recomposition, oral tradition only tends to retain information about institutions and relationships so long as they are immediately relevant to the poet's audience or relate directly to contemporary social structures.",
        "supporting_evidence": [],
        "related_claims": ["C023", "C024", "C026"]
    },
    {
        "id": "C026",
        "content": "Abstractions in oral tradition are often manipulated by the poet to explain or justify contemporary conditions, express group identity, or legitimize rights and privileges",
        "claim_type": "theoretical_framework",
        "claim_role": "supporting",
        "page": 300,
        "verbatim_quote": "Furthermore, such abstractions are often manipulated by the poet to explain or justify contemporary conditions, express group identity, or legitimize rights and privileges.",
        "supporting_evidence": [],
        "related_claims": ["C025", "C027"]
    },
    {
        "id": "C027",
        "content": "Precise linguistic arrangements (and the epics are very consistent in this regard) represent an abstraction, evolving rapidly through recomposition",
        "claim_type": "interpretation",
        "claim_role": "core",
        "page": 300,
        "verbatim_quote": "Precise linguistic arrangements (and the epics are very consistent in this regard) represent just such an abstraction, evolving rapidly through recomposition",
        "supporting_evidence": [],
        "related_claims": ["C022", "C026"]
    }
]

# Section 1: Implicit Arguments
implicit_arguments_section1 = [
    {
        "id": "IA001",
        "content": "The Iliad is the earliest available literary source for examining eighth-century Greek identity",
        "argument_type": "unstated_assumption",
        "page": 299,
        "trigger_text": [
            "Examination of one important component of mature Panhellenism—language—in what is arguably the earliest available literary source, the Iliad"
        ],
        "trigger_locations": [
            {"section": "Abstract", "subsection": None, "paragraph": 1}
        ],
        "inference_reasoning": "Ross qualifies 'earliest available literary source' with 'arguably', indicating awareness of debate, but proceeds on this assumption without defending it. The entire analysis depends on treating Iliad as evidence for eighth-century attitudes, assuming it's the best/earliest source available.",
        "related_claims": ["C004", "C022"],
        "implicit_metadata": {
            "basis": "assumption",
            "assessment_implication": "If Iliad not earliest or reflects later period, dating of proto-Panhellenism would be affected"
        }
    },
    {
        "id": "IA002",
        "content": "Eighth-century stabilization date for Iliad is accepted as basis for analysis despite acknowledging controversy as 'perhaps ultimately irresolvable'",
        "argument_type": "methodological_assumption",
        "page": 300,
        "trigger_text": [
            "The controversy is complex and involved—and perhaps ultimately irresolvable or even irrelevant.",
            "I believe, however, that the poems as we have them substantially preserve versions current during the late eighth century"
        ],
        "trigger_locations": [
            {"section": "Introduction", "subsection": None, "paragraph": 2},
            {"section": "Introduction", "subsection": None, "paragraph": 3}
        ],
        "inference_reasoning": "Ross acknowledges dating controversy may be 'irresolvable or even irrelevant' yet immediately proceeds to stake out a specific dating position (late eighth century). This reveals implicit assumption that analysis can proceed despite fundamental uncertainty—that the specific date matters less than accepting *some* dating framework.",
        "related_claims": ["C017", "C018", "C022"],
        "implicit_metadata": {
            "basis": "assumption",
            "assessment_implication": "Alternative dating (e.g., seventh century) would shift interpretation of when proto-Panhellenism emerged"
        }
    },
    {
        "id": "IA003",
        "content": "Linguistic arrangements are more reliable indicators of contemporary eighth-century attitudes than material culture references",
        "argument_type": "bridging_claim",
        "page": 300,
        "trigger_text": [
            "Physical things, be they objects or places, are much more durable in oral tradition—hence the appearance of boars' tusk helmets and the preeminence of Mycenae in the Iliad. By contrast, so long as it is evolving through recomposition, oral tradition only tends to retain information about institutions and relationships so long as they are immediately relevant",
            "Precise linguistic arrangements (and the epics are very consistent in this regard) represent just such an abstraction, evolving rapidly through recomposition"
        ],
        "trigger_locations": [
            {"section": "Introduction", "subsection": None, "paragraph": 3},
            {"section": "Introduction", "subsection": None, "paragraph": 3}
        ],
        "inference_reasoning": "Ross establishes that (1) physical things persist from earlier periods (boars' tusk helmets), (2) abstractions update to remain relevant, and (3) linguistic arrangements are abstractions. The unstated bridging claim is that linguistic arrangements therefore reflect eighth-century attitudes more reliably than material culture. This is crucial for justifying focus on language as evidence for eighth-century Panhellenism despite Bronze Age material survivals.",
        "related_claims": ["C022", "C023", "C024", "C025", "C027"],
        "implicit_metadata": {
            "basis": "logical_implication",
            "assessment_implication": "If linguistic arrangements can preserve earlier patterns like material culture, the dating framework collapses"
        }
    },
    {
        "id": "IA004",
        "content": "Nagy's diffusion theory is correct and applicable to linguistic patterns specifically (not just general content)",
        "argument_type": "unstated_assumption",
        "page": 300,
        "trigger_text": [
            "that by about 700 b.c.e. the poems were so widely diffused that opportunities for recomposition would have been limited by the expectations of a large, diverse, and informed audience",
            "Precise linguistic arrangements (and the epics are very consistent in this regard) represent just such an abstraction, evolving rapidly through recomposition"
        ],
        "trigger_locations": [
            {"section": "Introduction", "subsection": None, "paragraph": 3},
            {"section": "Introduction", "subsection": None, "paragraph": 3}
        ],
        "inference_reasoning": "Ross cites Nagy's diffusion theory as rationale for c. 700 BCE stabilization, then applies this to linguistic arrangements specifically. The implicit assumption is that Nagy's theory (developed for overall poem content) applies equally to specific linguistic details about diversity representation. This is never explicitly defended—just applied.",
        "related_claims": ["C018", "C020", "C027"],
        "implicit_metadata": {
            "basis": "assumption",
            "assessment_implication": "If linguistic details more fluid than overall content, patterns could reflect multiple periods or be less stable indicators"
        }
    },
    {
        "id": "IA005",
        "content": "Vansina's oral tradition theory developed for non-literate African societies applies to ancient Greek epic tradition",
        "argument_type": "disciplinary_assumption",
        "page": 300,
        "trigger_text": [
            "Oral tradition assimilates, forgets, and modiﬁes different types of information at different rates.",
            "Physical things, be they objects or places, are much more durable in oral tradition",
            "so long as it is evolving through recomposition, oral tradition only tends to retain information about institutions and relationships so long as they are immediately relevant"
        ],
        "trigger_locations": [
            {"section": "Introduction", "subsection": None, "paragraph": 3}
        ],
        "inference_reasoning": "Ross relies heavily on Vansina's oral tradition theory (cited footnote 4: Vansina 1985) without discussing whether Vansina's findings (based on African oral traditions) transfer to Greek epic context. The cross-cultural applicability is assumed, not defended. This is disciplinary common practice in orality studies but remains an unstated assumption.",
        "related_claims": ["C023", "C024", "C025"],
        "implicit_metadata": {
            "basis": "disciplinary_assumption",
            "assessment_implication": "If Greek epic tradition functions differently from Vansina's African examples, the differential preservation claims may not hold"
        }
    }
]

# Add to extraction
extraction["evidence"].extend(evidence_section1)
extraction["claims"].extend(claims_section1)
extraction["implicit_arguments"].extend(implicit_arguments_section1)

# Update extraction notes
extraction["extraction_notes"].append(
    "Pass 1 Section 1 (Abstract + Introduction, pp. 299-301): Extracted 27 claims, 0 evidence, 5 implicit arguments. "
    "Section establishes theoretical framework and dating assumptions. No primary source citations yet (those start Section 3). "
    "High implicit argument density (dating framework, oral tradition theory applicability). ~1300 words processed."
)

# Write updated extraction
with open(extraction_path, 'w', encoding='utf-8') as f:
    json.dump(extraction, f, indent=2, ensure_ascii=False)

print(f"✓ Section 1 extraction complete")
print(f"  - Claims: {len(claims_section1)}")
print(f"  - Evidence: {len(evidence_section1)}")
print(f"  - Implicit Arguments: {len(implicit_arguments_section1)}")
print(f"  - Total items this section: {len(claims_section1) + len(evidence_section1) + len(implicit_arguments_section1)}")
print(f"  - Running total: {len(extraction['claims'])} claims, {len(extraction['evidence'])} evidence, {len(extraction['implicit_arguments'])} implicit arguments")
