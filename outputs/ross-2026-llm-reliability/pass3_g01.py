#!/usr/bin/env python3
"""Pass 3 (explicit RDMAP) — G1: Abstract + Introduction (pp. 1-3).

Liberal extraction: research designs dominate this group (framing, scope,
theoretical grounding). No methods or protocols are described procedurally here;
the two-episode structure is extracted as design, with methods deferred to the
groups where procedures are documented.
"""

from rdmap_lib import save_group

designs = [
    {
        "design_id": "RD001",
        "design_text": (
            "Research framing: set aside broader questions about AI's trajectory and focus on "
            "narrower questions facing working researchers — what LLMs can actually do as "
            "research tools, and under what conditions their output can be trusted, especially "
            "on larger-scale, longer-running tasks where errors accumulate."
        ),
        "design_type": "research_question",
        "design_status": "explicit",
        "verbatim_quote": (
            "In the spirit of Mowshowitz's mundane utility (Mowshowitz, 2023), we set aside the "
            "broader questions about artificial intelligence's trajectory and focus on narrower "
            "questions that researchers face: what can these systems actually do as research "
            "tools, and under what conditions can their output be trusted, particularly on "
            "larger-scale, longer-running tasks where errors accumulate?"
        ),
        "location": {"section": "Introduction", "page": 2},
        "expected_information_missing": [
            "No explicit statement of hypotheses or predictions attached to the research questions",
        ],
    },
    {
        "design_id": "RD002",
        "design_text": (
            "Two-episode grounding design: claims are grounded in two episodes a year apart — a "
            "2025 evaluation of commercial LLMs applied to a research-software longevity study, "
            "and a partial 2026 re-application via an agent built in a current framework — so "
            "that persistence of failure modes across a model generation can support the claim "
            "that reliability is structural rather than model-specific."
        ),
        "design_type": "study_design",
        "design_status": "explicit",
        "verbatim_quote": (
            "We ground these claims in two episodes a year apart. The first is a 2025 evaluation "
            "of commercial LLMs applied to a study of archaeological research-software longevity "
            "involving system customisation and prompts, the levers available at the time. The "
            "second is a partial 2026 re-application: an agent built within a current framework."
        ),
        "location": {"section": "Introduction", "page": 2},
        "expected_information_missing": [
            "No discussion of alternative designs considered (e.g., controlled replication rather than incidental re-application)",
        ],
    },
    {
        "design_id": "RD003",
        "design_text": (
            "Theoretical framework: scaffolding in its original pedagogic sense (Wood, Bruner and "
            "Ross 1976; van de Pol et al. 2010) applied to LLM-assisted research — the structure "
            "a researcher builds around a model to supply judgement — grounding the paper's "
            "central thesis about the locus of reliability."
        ),
        "design_type": "theoretical_framework",
        "design_status": "explicit",
        "verbatim_quote": (
            "We use 'scaffolding' in its original, pedagogic sense, the support a more capable "
            "partner supplies so that a learner can complete a task beyond unaided competence "
            "(Wood, Bruner, and G. Ross, 1976; Pol, Volman, and Beishuizen, 2010). Applied to "
            "LLM-assisted research, scaffolding denotes the structure a researcher builds around "
            "a model to supply judgement."
        ),
        "location": {"section": "Introduction", "page": 1},
        "expected_information_missing": [],
    },
    {
        "design_id": "RD004",
        "design_text": (
            "Definitional scope decision: the scaffolding/harness boundary is drawn functionally "
            "rather than architecturally, because the argument concerns the source of judgement "
            "rather than its location in the software stack."
        ),
        "design_type": "scope_definition",
        "design_status": "explicit",
        "verbatim_quote": (
            "We draw the boundary functionally rather than architecturally because our argument "
            "concerns the source of judgement rather than its location in the stack."
        ),
        "location": {"section": "Introduction", "page": 2},
        "expected_information_missing": [],
    },
    {
        "design_id": "RD005",
        "design_text": (
            "Analytic framework: the augmentation-versus-automation distinction — augmentation "
            "requires a human to supply judgement the system cannot (through scaffolding and "
            "targeted verification), automation would require the system to supply that "
            "judgement itself — structures the paper's assessment of LLM research use."
        ),
        "design_type": "theoretical_framework",
        "design_status": "explicit",
        "verbatim_quote": (
            "Our answer turns on a distinction: LLMs can augment a researcher but not yet "
            "automate research. Augmentation in this case requires a human to supply judgement "
            "the system cannot, primarily through construction of scaffolding to guide the "
            "model, secondarily through targeted verification. Automation would require the "
            "system to supply that judgement itself."
        ),
        "location": {"section": "Introduction", "page": 2},
        "expected_information_missing": [],
    },
    {
        "design_id": "RD006",
        "design_text": (
            "Scope division with companion paper: the epistemic argument (models lack intrinsic "
            "judgement) is assigned to a companion paper, while this paper takes the "
            "practitioner's complement — what the model cannot supply from within can be "
            "elicited from without."
        ),
        "design_type": "scope_definition",
        "design_status": "explicit",
        "verbatim_quote": (
            "A companion paper argues that these systems lack intrinsic judgement as an "
            "epistemic capability Ballsun-Stanton and S. A. Ross, 2026. The argument here is "
            "the practitioner's complement: what the model cannot supply from within can be "
            "elicited from without."
        ),
        "location": {"section": "Introduction", "page": 2},
        "expected_information_missing": [],
    },
]

save_group(
    {
        "group": "G1",
        "section_title": "Abstract + Introduction",
        "page_range": "1-3",
        "scan_note": (
            "Design-dense framing group: research questions, two-episode grounding, scaffolding "
            "framework, definitional scope, augment/automate frame, companion-paper division. "
            "No procedural methods or protocols documented in this group; episode procedures "
            "deferred to Methods/Results groups."
        ),
    },
    research_designs=designs,
)
