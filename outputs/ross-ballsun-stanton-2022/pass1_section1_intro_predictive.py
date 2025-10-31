#!/usr/bin/env python3
"""
Pass 1: Liberal Claims & Evidence Extraction
Section Group 1: Introduction + Section 1 (Predictive/Postdictive Approaches)
Pages: 2-4 (PDF pages, SocArXiv preprint)

Extraction Strategy:
- Liberal extraction of claims about preregistration benefits
- Evidence from reproducibility crisis literature
- Methodological arguments about prediction vs postdiction
- Implicit arguments about research quality standards
- Focus on conceptual/theoretical claims about research design

Word count estimate: ~1600 words
"""

import json
from datetime import datetime

# Load existing extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'r') as f:
    data = json.load(f)

# Section Group 1: Introduction + Section 1
# Pages 2-4 of PDF (Abstract through "HARKing" discussion)

# ============================================================================
# EVIDENCE ITEMS
# ============================================================================

evidence_items = [
    {
        "id": "E001",
        "content": "The reproducibility crisis has been documented across multiple disciplines including psychology, biomedicine, ecology, and evolutionary biology.",
        "evidence_type": "literature_synthesis",
        "source_type": "published_research",
        "verbatim_quote": "The motivation stems from the 'reproducibility crisis' faced by many disciplines (Nature 2016; Open Science Collaboration 2015; Adam 2019; Kaplan and Irvin 2015; Franco et al. 2014; Mellor et al. 2016; Baker 2015; Munafò et al. 2017; National Academies of Sciences, Engineering, and Medicine et al. 2019).",
        "page_number": 2,
        "context": "Introduction establishing motivation for preregistration",
        "interpretation_notes": "Synthesises multiple citations documenting reproducibility problems across disciplines"
    },
    {
        "id": "E002",
        "content": "In a 2018 survey of over 800 ecologists and evolutionary biologists, 51% admitted to HARKing (hypothesising after results are known).",
        "evidence_type": "quantitative_data",
        "source_type": "survey_data",
        "verbatim_quote": "In a 2018 paper surveying over eight hundred ecologists and evolutionary biologists, 51% admitted to HARKing (Fraser et al. 2018).",
        "page_number": 4,
        "context": "Section on HARKing as questionable research practice",
        "interpretation_notes": "Empirical evidence of prevalence of questionable research practices in related disciplines"
    },
    {
        "id": "E003",
        "content": "https://clinicaltrials.gov is the largest existing preregistration registry, demonstrating established use in biomedical research.",
        "evidence_type": "infrastructure",
        "source_type": "existing_system",
        "verbatim_quote": "Although preregistration is often associated with scientific and biomedical research (https://clinicaltrials.gov/ is the largest existing registry), it is also used in social sciences like economics and political science",
        "page_number": 3,
        "context": "Discussion of preregistration adoption across disciplines",
        "interpretation_notes": "Evidence that preregistration infrastructure and practices already exist in some fields"
    },
    {
        "id": "E004",
        "content": "Social science preregistration registries exist including the Social Science Registry and EGAP, demonstrating adoption beyond biomedicine.",
        "evidence_type": "infrastructure",
        "source_type": "existing_system",
        "verbatim_quote": "it is also used in social sciences like economics and political science (see https://www.socialscienceregistry.org/; http://egap.org/content/registration/; cf. Nosek et al. 2018a; Haven and Van Grootel 2019).",
        "page_number": 3-4,
        "context": "Establishing precedent for preregistration in social sciences",
        "interpretation_notes": "Demonstrates preregistration is not limited to hard sciences"
    }
]

# ============================================================================
# CLAIMS ITEMS
# ============================================================================

claims_items = [
    {
        "id": "C001",
        "content": "Preregistration has been promoted as a technique to combat researchers' biases, overcome perverse professional incentives, improve transparency, and increase rigour.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": ["E001"],
        "verbatim_quote": "Preregistration of research design, and in some cases hypotheses, has been promoted as a technique to combat researchers' biases, overcome perverse professional incentives, improve transparency, and increase rigor.",
        "page_number": 2,
        "context": "Opening paragraph establishing purpose of preregistration",
        "certainty_qualifier": "established in literature"
    },
    {
        "id": "C002",
        "content": "Preregistration can be described as the declaration of a research plan before data collection begins.",
        "claim_type": "definitional",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Preregistration can be described as the declaration of a research plan before data collection begins (Center for Open Science 2018), or a process in which researchers: 'define the research questions and analysis plan before observing the research outcomes' (Nosek et al. 2018a).",
        "page_number": 2,
        "context": "Defining key term for the chapter",
        "certainty_qualifier": "definitional"
    },
    {
        "id": "C003",
        "content": "Preregistration accommodates inductive (hypothesis-generating; postdictive) as well as deductive (hypothesis testing; predictive) research.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Preregistration accommodates inductive (hypothesis-generating; postdictive) as well as deductive (hypothesis testing; predictive) research, idiographic (distinct to a particular place) as well as nomothetic (applicable to a larger class of events of conditions) approaches, qualitative as well as quantitative analyses",
        "page_number": 2-3,
        "context": "Establishing broad applicability of preregistration",
        "certainty_qualifier": "asserted by authors"
    },
    {
        "id": "C004",
        "content": "Preregistration accommodates idiographic (place-specific) as well as nomothetic (generalising) approaches.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "idiographic (distinct to a particular place) as well as nomothetic (applicable to a larger class of events of conditions) approaches",
        "page_number": 2-3,
        "context": "Establishing applicability across research paradigms",
        "certainty_qualifier": "asserted by authors"
    },
    {
        "id": "C005",
        "content": "Preregistration can be applied at various stages of the research lifecycle.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "can be applied at various stages of the research lifecycle (Nosek et al. 2018a)",
        "page_number": 3,
        "context": "Establishing flexibility of preregistration",
        "certainty_qualifier": "cited from Nosek"
    },
    {
        "id": "C006",
        "content": "Preregistration could counteract archaeologists' reluctance to invest time in early planning phases versus later fieldwork and analysis phases.",
        "claim_type": "methodological",
        "reasoning_type": "pragmatic",
        "evidence_links": [],
        "verbatim_quote": "Preregistration could also counteract a sociotechnical problem hindering the adoption of digital field methods: a reluctance to invest time and resources in the early planning and preparation phases of a project, versus time later during fieldwork, post-processing, and analysis (Sobotkova et al. 2016).",
        "page_number": 3,
        "context": "Introducing archaeology-specific application",
        "certainty_qualifier": "could (modal qualifier)"
    },
    {
        "id": "C007",
        "content": "Lack of planning leads to ongoing modification of data structures and workflows during fieldwork, raising costs and complexity.",
        "claim_type": "empirical",
        "reasoning_type": "observational",
        "evidence_links": [],
        "verbatim_quote": "This lack of planning leads to changes in research design during execution with little accountability, including for example, ongoing modification of data structures and data capture workflows during fieldwork (Borgman 2015). Such in-progress changes raise the cost and complexity of digital field data collection systems.",
        "page_number": 3,
        "context": "Describing problem that preregistration addresses",
        "certainty_qualifier": "stated as observed fact"
    },
    {
        "id": "C008",
        "content": "Ad hoc changes during fieldwork limit data quality by precluding adequate testing, undermining consistency, and imposing technical debt.",
        "claim_type": "empirical",
        "reasoning_type": "observational",
        "evidence_links": [],
        "verbatim_quote": "Ad hoc changes limit data quality by precluding adequate testing and refinement, undermining consistency of data and methods, and imposing 'technical debt' such as extensive cleaning and reconciliation of data at the end of the project.",
        "page_number": 3,
        "context": "Consequences of inadequate planning",
        "certainty_qualifier": "stated as observed pattern"
    },
    {
        "id": "C009",
        "content": "Easy changes during and after fieldwork hinder the interoperability and reusability of resulting datasets.",
        "claim_type": "methodological",
        "reasoning_type": "logical",
        "evidence_links": [],
        "verbatim_quote": "These 'easy' changes during and after fieldwork thereby hinder the interoperability and reusability of resulting datasets.",
        "page_number": 3,
        "context": "Long-term consequences of poor planning",
        "certainty_qualifier": "asserted logical consequence"
    },
    {
        "id": "C010",
        "content": "Maintaining the distinction between prediction and postdiction combats researchers' cognitive biases and ensures adherence to statistical assumptions.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Maintaining this distinction combats researchers' cognitive biases, ensures that research adheres to assumptions intrinsic to common statistical approaches, and counteracts the distortions introduced by perverse professional incentives",
        "page_number": 3,
        "context": "Section 1 on predictive vs postdictive research",
        "certainty_qualifier": "stated as methodological principle"
    },
    {
        "id": "C011",
        "content": "Publication bias exists toward papers that confirm rather than refute initial hypotheses in deductive research.",
        "claim_type": "empirical",
        "reasoning_type": "observational",
        "evidence_links": [],
        "verbatim_quote": "For example, we can see a 'publication bias' towards papers that confirm, rather than refute, initial hypotheses in deductive research (Chase 2013; Fraser et al. 2018).",
        "page_number": 3,
        "context": "Perverse incentives in research",
        "certainty_qualifier": "documented in literature"
    },
    {
        "id": "C012",
        "content": "Predictive research provides a rigorous way to test and disprove hypotheses, supporting Popperian falsification.",
        "claim_type": "methodological",
        "reasoning_type": "theoretical",
        "evidence_links": [],
        "verbatim_quote": "Predictive research provides a rigorous way to test and disprove hypotheses. Such testing is a boon for positivists, who remind us that Popper's injunction that 'proof' of a hypothesis is always provisional while disproof is final, making falsifiability the hallmark of science (Derksen 2019).",
        "page_number": 4,
        "context": "Value of predictive research",
        "certainty_qualifier": "established in philosophy of science"
    },
    {
        "id": "C013",
        "content": "Postdictive research can generate surprising or unexpected hypotheses that radically shift understanding or change scientific worldviews.",
        "claim_type": "methodological",
        "reasoning_type": "theoretical",
        "evidence_links": [],
        "verbatim_quote": "Postdictive research, conversely, can generate surprising or unexpected hypotheses that radically shift our understanding of the world or even change scientific worldviews (Kuhn 1970:23).",
        "page_number": 4,
        "context": "Value of postdictive research",
        "certainty_qualifier": "supported by Kuhnian paradigm shift theory"
    },
    {
        "id": "C014",
        "content": "Both predictive and postdictive approaches are essential but must not be conflated.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Both predictive and postdictive approaches are essential, but they must not be conflated.",
        "page_number": 4,
        "context": "Core argument about maintaining distinctions",
        "certainty_qualifier": "strong normative claim"
    },
    {
        "id": "C015",
        "content": "Formalisms like preregistration that enforce distinctions between prediction and postdiction improve the quality of research even for non-positivists.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Therefore, even if a researcher does not hold with positivist Popperian falsification as the primary mechanism for scientific discovery (Huemer 2020), formalisms like preregistration that enforce distinctions between prediction and postdiction improve the quality of research",
        "page_number": 4,
        "context": "Broad applicability of preregistration",
        "certainty_qualifier": "asserted by authors"
    },
    {
        "id": "C016",
        "content": "Failing to appreciate the difference between prediction and postdiction can lead to overconfidence in post hoc explanations and inflate the likelihood of believing false findings.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Failing to appreciate the difference can lead to overconfidence in post hoc explanations (postdictions) and inflate the likelihood of believing that there is evidence for a finding when there is not. Presenting postdictions as predictions can increase the attractiveness and publishability of findings by falsely reducing uncertainty",
        "page_number": 4,
        "context": "Nosek quote on consequences of conflation",
        "certainty_qualifier": "cited from Nosek et al."
    },
    {
        "id": "C017",
        "content": "If postdiction is conflated with prediction, it is prone to fallibility of memory, motivated reasoning, and cognitive biases.",
        "claim_type": "methodological",
        "reasoning_type": "psychological",
        "evidence_links": [],
        "verbatim_quote": "If postdiction is conflated with prediction, it is prone to 'fallibility of memory, motivated reasoning, and cognitive biases' (Nosek et al. 2018a).",
        "page_number": 4,
        "context": "Psychological mechanisms underlying problems",
        "certainty_qualifier": "cited from Nosek"
    },
    {
        "id": "C018",
        "content": "Hindsight bias causes researchers to subconsciously remember or seek evidence supporting their conclusions while ignoring contrary evidence.",
        "claim_type": "methodological",
        "reasoning_type": "psychological",
        "evidence_links": [],
        "verbatim_quote": "Of particular concern is hindsight bias, where researchers (often subconsciously) remember or seek evidence supporting their conclusions while ignoring or faulting contrary evidence.",
        "page_number": 4,
        "context": "Specific cognitive bias",
        "certainty_qualifier": "established in cognitive psychology"
    },
    {
        "id": "C019",
        "content": "Common statistical methods like null hypothesis significance testing assume prediction rather than postdiction and produce Type 1 errors when researchers neglect the difference.",
        "claim_type": "methodological",
        "reasoning_type": "statistical",
        "evidence_links": [],
        "verbatim_quote": "Since common statistical methods like null hypothesis significance testing, moreover, assume prediction rather than postdiction, they are likely to produce 'Type 1 errors' (false positives) when researchers neglect the difference.",
        "page_number": 4,
        "context": "Statistical consequences of conflation",
        "certainty_qualifier": "stated as statistical principle"
    },
    {
        "id": "C020",
        "content": "Mistaking postdiction as prediction underestimates uncertainty and can produce psychological overconfidence in findings.",
        "claim_type": "methodological",
        "reasoning_type": "psychological",
        "evidence_links": [],
        "verbatim_quote": "As a result of these problems, 'Mistaking postdiction as prediction underestimates the uncertainty of outcomes and can produce psychological overconfidence in the resulting findings' (Nosek et al. 2018a).",
        "page_number": 4,
        "context": "Summary of overconfidence problem",
        "certainty_qualifier": "cited from Nosek"
    },
    {
        "id": "C021",
        "content": "Postdictive research should not simultaneously test the hypotheses it generates.",
        "claim_type": "methodological",
        "reasoning_type": "normative",
        "evidence_links": [],
        "verbatim_quote": "Although postdictive research can produce new inconvenient facts that contradict received paradigms, it should not simultaneously test the hypotheses it generates.",
        "page_number": 4,
        "context": "Methodological principle",
        "certainty_qualifier": "strong normative statement"
    },
    {
        "id": "C022",
        "content": "HARKing is using current results to construct post hoc hypotheses reported as a priori, or failing to report unsupported a priori hypotheses.",
        "claim_type": "definitional",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Indeed, 'using current results to construct post hoc hypotheses that are then reported as if they were a priori hypotheses', 'failing to report a priori hypotheses that are unsupported by the current results' (Rubin 2017), or 'presenting exploratory work as though it was confirmatory hypothesis testing' (Fraser et al. 2018), is considered 'hypothesizing after the results are known' or HARKing (Kerr 1998).",
        "page_number": 4,
        "context": "Defining questionable research practice",
        "certainty_qualifier": "definitional from literature"
    },
    {
        "id": "C023",
        "content": "HARKing is always a questionable research practice if unreported, though disagreement exists about acceptability of transparent post hoc analysis.",
        "claim_type": "methodological",
        "reasoning_type": "ethical",
        "evidence_links": ["E002"],
        "verbatim_quote": "HARKing is always a questionable research practice if it is unreported, although disagreement exists about the acceptability (or even desirability) of careful and transparent post hoc analysis in deductive research (Rubin 2017; Hollenbeck and Wright 2017).",
        "page_number": 4,
        "context": "Ethics of HARKing",
        "certainty_qualifier": "conditional - depends on disclosure"
    },
    {
        "id": "C024",
        "content": "When published papers fail to disclose a priori hypotheses, it becomes difficult to judge whether HARKing has taken place.",
        "claim_type": "methodological",
        "reasoning_type": "logical",
        "evidence_links": [],
        "verbatim_quote": "Fraser also notes in passing that when published papers fail to disclose a priori hypotheses (or if there were a priori hypotheses), it becomes difficult to judge whether HARKing – or the conflation of postdiction and prediction more broadly – has even taken place.",
        "page_number": 4-5,
        "context": "Detection problem for questionable practices",
        "certainty_qualifier": "logical observation"
    },
    {
        "id": "C025",
        "content": "The a priori articulation of hypotheses required by preregistration (or explicit statement of inductive research) can help combat HARKing.",
        "claim_type": "methodological",
        "reasoning_type": "logical",
        "evidence_links": ["E002"],
        "verbatim_quote": "As such, the a priori articulation of hypotheses required by preregistration (or the explicit statement that research is inductive) can help to combat this species of questionable research practice.",
        "page_number": 5,
        "context": "Solution to HARKing problem",
        "certainty_qualifier": "can (modal qualifier)"
    }
]

# ============================================================================
# IMPLICIT ARGUMENTS ITEMS
# ============================================================================

implicit_arguments = [
    {
        "id": "IA001",
        "content": "Research transparency and reproducibility are inherently valuable goals that archaeology should pursue.",
        "reasoning": "The entire chapter assumes reproducibility and transparency are desirable without arguing for this premise; it's treated as self-evident given the 'crisis' in other fields.",
        "trigger_text": "The motivation stems from the 'reproducibility crisis'... In archaeology and other field sciences, preregistration offers its usual benefits: explicit recognition of research design; management of biases and perverse incentives; and exposure of research methods and processes as required by emerging good practice in research transparency",
        "page_number": 2-3,
        "context": "Introduction presents crisis as motivation without defending whether reproducibility should be archaeology's goal",
        "theoretical_significance": "Imports values and standards from sciences into archaeology without interrogating disciplinary differences"
    },
    {
        "id": "IA002",
        "content": "Cognitive biases and perverse professional incentives are significant problems in archaeological research that require systematic intervention.",
        "reasoning": "The authors assume these problems exist in archaeology based on evidence from other disciplines, without demonstrating they manifest similarly in archaeological practice.",
        "trigger_text": "The biases and perverse incentives that preregistration was designed to combat in other disciplines also exist in archaeology.",
        "page_number": 5,
        "context": "Section 2 introduction asserts problem exists in archaeology",
        "theoretical_significance": "Assumes archaeological research practice suffers from same pathologies as psychology/biomedicine"
    },
    {
        "id": "IA003",
        "content": "The distinction between prediction and postdiction is fundamental and must be maintained for research to be valid.",
        "reasoning": "This epistemological commitment is presented as obvious rather than as one philosophical position about knowledge production.",
        "trigger_text": "Both predictive and postdictive approaches are essential, but they must not be conflated.",
        "page_number": 4,
        "context": "Section 1 core claim",
        "theoretical_significance": "Privileges particular (positivist) understanding of scientific validity"
    },
    {
        "id": "IA004",
        "content": "Researcher subjectivity and memory are unreliable and require external documentation and commitment mechanisms.",
        "reasoning": "Assumes researchers cannot be trusted to accurately remember or report their research process without formal preregistration.",
        "trigger_text": "prone to 'fallibility of memory, motivated reasoning, and cognitive biases'",
        "page_number": 4,
        "context": "Discussion of why conflation is problematic",
        "theoretical_significance": "Reflects distrust of researcher self-reporting and emphasis on external accountability"
    },
    {
        "id": "IA005",
        "content": "Reusable datasets and large-scale synthesis are important goals that individual research projects should facilitate.",
        "reasoning": "Assumes archaeological research should prioritise compatibility and aggregation over project-specific goals.",
        "trigger_text": "These 'easy' changes during and after fieldwork thereby hinder the interoperability and reusability of resulting datasets.",
        "page_number": 3,
        "context": "Critique of ad hoc changes",
        "theoretical_significance": "Prioritises future reuse over immediate research needs"
    },
    {
        "id": "IA006",
        "content": "Statistical approaches and their underlying assumptions are appropriate for archaeological research.",
        "reasoning": "Discussion of null hypothesis significance testing assumes statistical methods are or should be common in archaeology.",
        "trigger_text": "Since common statistical methods like null hypothesis significance testing, moreover, assume prediction rather than postdiction",
        "page_number": 4,
        "context": "Discussion of statistical consequences",
        "theoretical_significance": "May not reflect actual methodological diversity in archaeological practice"
    }
]

# ============================================================================
# UPDATE EXTRACTION DATA
# ============================================================================

# Add new items to extraction
data['evidence'].extend(evidence_items)
data['claims'].extend(claims_items)
data['implicit_arguments'].extend(implicit_arguments)

# Update extraction notes
data['extraction_notes'] = {
    'pass': 1,
    'section_extracted': 'Group 1: Introduction + Section 1 (Predictive/Postdictive Approaches), pages 2-4',
    'extraction_strategy': 'Liberal extraction focusing on: (1) conceptual claims about preregistration and research design, (2) evidence from reproducibility literature, (3) methodological arguments about prediction/postdiction distinction, (4) implicit assumptions about research quality and disciplinary norms. Word count ~1600 words.',
    'known_uncertainties': [
        'Some claims overlap with implicit arguments (e.g., assumption that biases exist in archaeology)',
        'Several claims cite Nosek - need to determine if these are evidence or claims with evidence backing',
        'Publication bias claim may need evidence extraction from cited papers'
    ],
    'section_word_count_estimate': 1600
}

data['extraction_timestamp'] = datetime.now().isoformat() + 'Z'

# Save updated extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print("=" * 80)
print("PASS 1 - SECTION GROUP 1 EXTRACTION COMPLETE")
print("=" * 80)
print()
print(f"Section: Introduction + Section 1 (Predictive/Postdictive)")
print(f"Pages: 2-4")
print(f"Estimated word count: ~1600 words")
print()
print("Items extracted:")
print(f"  Evidence: {len(evidence_items)} items (E001-E004)")
print(f"  Claims: {len(claims_items)} items (C001-C025)")
print(f"  Implicit Arguments: {len(implicit_arguments)} items (IA001-IA006)")
print()
print(f"Total this section: {len(evidence_items) + len(claims_items) + len(implicit_arguments)} items")
print()
print("✓ Section 1 extraction complete")
print()
