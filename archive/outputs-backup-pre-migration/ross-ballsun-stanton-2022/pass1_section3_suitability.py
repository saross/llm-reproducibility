#!/usr/bin/env python3
"""
Pass 1: Liberal Claims & Evidence Extraction
Section Group 3: Preregistration is Suitable for Archaeology
Pages: 7-8 (PDF pages, section 3)

Extraction Strategy:
- Claims about archaeology's methodological diversity
- Arguments about preregistration flexibility
- Claims about serendipity and unpredictability
- Implicit assumptions about research control and planning
- Focus on applicability arguments

Word count estimate: ~1000 words
"""

import json
from datetime import datetime

# Load existing extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'r') as f:
    data = json.load(f)

# Section Group 3: Preregistration is Suitable for Archaeology
# Pages 7-8 of PDF

# ============================================================================
# EVIDENCE ITEMS
# ============================================================================

evidence_items = [
    # This section is primarily argumentative - minimal new evidence items
]

# ============================================================================
# CLAIMS ITEMS
# ============================================================================

claims_items = [
    {
        "id": "C044",
        "content": "Preregistration can help resist the temptation of just-in-time research design by making built-in good practice more likely than bolt-on fixes.",
        "claim_type": "methodological",
        "reasoning_type": "pragmatic",
        "evidence_links": [],
        "verbatim_quote": "Preregistration can help resist the temptation of 'just-in-time' research design. It would make 'built-in' good practice more likely, as opposed to more common attempts to 'bolt-on' fixes after fieldwork (Marwick 2017b:441).",
        "page_number": 7,
        "context": "Opening of Section 3",
        "certainty_qualifier": "can (modal qualifier)"
    },
    {
        "id": "C045",
        "content": "Preregistration offers a mechanism to make approaches and assumptions explicit, allowing them to be scrutinised and counteracting cognitive biases.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Specifically, preregistration offers a mechanism to make approaches and assumptions explicit, allowing them to be scrutinized (Johnson 2010:3) and counteracting cognitive biases.",
        "page_number": 7,
        "context": "Benefits of preregistration",
        "certainty_qualifier": "stated as capability"
    },
    {
        "id": "C046",
        "content": "Preregistration helps researchers overcome the sociotechnical tendency to underinvest in preparation, instead of relying on remediation late in the research lifecycle.",
        "claim_type": "methodological",
        "reasoning_type": "pragmatic",
        "evidence_links": [],
        "verbatim_quote": "Preregistration also helps researchers overcome the sociotechnical tendency to underinvest in preparation for data acquisition and analysis, instead of relying on remediation of problems late in the research lifecycle.",
        "page_number": 7,
        "context": "Practical benefit of preregistration",
        "certainty_qualifier": "helps (modal)"
    },
    {
        "id": "C047",
        "content": "Combined with other aspects of reproducibility, preregistration holds potential to tangibly improve research practice in archaeology.",
        "claim_type": "methodological",
        "reasoning_type": "pragmatic",
        "evidence_links": [],
        "verbatim_quote": "Combined with a commitment to other aspects of reproducibility (Perkel 2018; Marwick 2017b; Wilkinson et al. 2016), preregistration holds the potential to improve research practice tangibly in our discipline.",
        "page_number": 7,
        "context": "Summary claim for preregistration value",
        "certainty_qualifier": "holds potential (modal)"
    },
    {
        "id": "C048",
        "content": "Preregistration can accommodate the diversity and transdisciplinarity of archaeological research.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Preregistration can, moreover, accommodate the diversity and transdisciplinarity of archaeological research.",
        "page_number": 7,
        "context": "Addressing potential objection about diversity",
        "certainty_qualifier": "can (modal)"
    },
    {
        "id": "C049",
        "content": "Archaeology can be deductive and predictive or inductive and postdictive, but most often might best be described as abductive.",
        "claim_type": "empirical",
        "reasoning_type": "characterization",
        "evidence_links": [],
        "verbatim_quote": "Archaeology can be deductive and predictive or inductive and postdictive. Most often, archaeology – like other fieldwork disciplines – might best be described as abductive (Tavory and Timmermans 2014).",
        "page_number": 7,
        "context": "Characterising archaeological methodology",
        "certainty_qualifier": "might best be (qualified assertion)"
    },
    {
        "id": "C050",
        "content": "Abductive research represents a synthesis of deductive and inductive approaches, gathering data according to specific methodology then applying a theory or framework that describes those facts.",
        "claim_type": "definitional",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Abductive research represents a synthesis of deductive and inductive approaches, gathering data according to a specific and intentional methodology (the inductive element), and then applying a theory or framework that describes those facts (deductive).",
        "page_number": 7,
        "context": "Defining abduction",
        "certainty_qualifier": "definitional from Tavory & Timmermans"
    },
    {
        "id": "C051",
        "content": "Abductive methodology used in interpretive social science research is seldom explicitly acknowledged or described.",
        "claim_type": "empirical",
        "reasoning_type": "observational",
        "evidence_links": [],
        "verbatim_quote": "Used in interpretive social science research, this methodology is seldom explicitly acknowledged or described (Lewis-Beck et al. 2003:1).",
        "page_number": 7-8,
        "context": "Problem with abductive research",
        "certainty_qualifier": "documented by Lewis-Beck"
    },
    {
        "id": "C052",
        "content": "Archaeology can be quantitative and statistical or qualitative and descriptive, idiographic or nomothetic, and these approaches can be combined, iterated, or synthesised in various ways.",
        "claim_type": "empirical",
        "reasoning_type": "characterization",
        "evidence_links": [],
        "verbatim_quote": "Archaeology can also be quantitative and statistical or qualitative and descriptive. It can be idiographic, seek an in-depth understanding of the specific, contingent, and unique in a particular place and time. Or, it can be nomothetic, attempting to derive or test general (if provisional or incomplete) principles or rules by looking at similarities across space and time... These approaches, however, can cut across disciplines and can be combined, iterated, or synthesized in various ways",
        "page_number": 8,
        "context": "Archaeological methodological diversity",
        "certainty_qualifier": "descriptive characterisation"
    },
    {
        "id": "C053",
        "content": "A preregistration regime does not privilege any approach over another but demands articulation of and public commitment to specific research design before research begins.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "A preregistration regime does not privilege any of these approaches over another but instead demands an articulation of, and a public commitment to, a specific research design at the beginning of a project, before research begins.",
        "page_number": 8,
        "context": "Key claim about preregistration neutrality",
        "certainty_qualifier": "strong normative statement"
    },
    {
        "id": "C054",
        "content": "The very complexity and diversity of archaeology makes articulation of research design particularly important.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Indeed, the very complexity and diversity of archaeology – spanning disciplines and approaches to knowledge – makes articulation of research design particularly important.",
        "page_number": 8,
        "context": "Why archaeology especially needs preregistration",
        "certainty_qualifier": "strong claim"
    },
    {
        "id": "C055",
        "content": "An explicit research design documented before research starts avoids unintentional conflation or elision of approaches that could undermine results.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "An explicit research design documented in detail before research starts, rather than during the writing-up stage, avoids the unintentional conflation or elision of approaches that could undermine research results.",
        "page_number": 8,
        "context": "Specific benefit for diverse discipline",
        "certainty_qualifier": "stated as logical consequence"
    },
    {
        "id": "C056",
        "content": "Archaeology is serendipitous - we often do not know what we will find until we get to the field.",
        "claim_type": "empirical",
        "reasoning_type": "characterization",
        "evidence_links": [],
        "verbatim_quote": "Archaeology is also serendipitous. Often, we do not know what we will find until we get to the field.",
        "page_number": 8,
        "context": "Addressing serendipity objection",
        "certainty_qualifier": "descriptive characterisation"
    },
    {
        "id": "C057",
        "content": "The problem of not knowing results beforehand is not unique to archaeology - even in deductive disciplines results are not under researcher control.",
        "claim_type": "methodological",
        "reasoning_type": "analogical",
        "evidence_links": [],
        "verbatim_quote": "This problem, however, is not unique to archaeology. Even in deductive disciplines, results are not and should not be under the control of the researcher (Chambers 2019).",
        "page_number": 8,
        "context": "Responding to serendipity objection",
        "certainty_qualifier": "cited from Chambers"
    },
    {
        "id": "C058",
        "content": "Research design, research questions or hypotheses, methods, and interpretive frameworks are under researcher control and can be articulated beforehand.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Research design, research questions or hypotheses, methods, and interpretive frameworks, however, are under researcher control. As a result, these elements can be articulated beforehand.",
        "page_number": 8,
        "context": "What can be preregistered despite serendipity",
        "certainty_qualifier": "strong assertion"
    },
    {
        "id": "C059",
        "content": "Training, prior fieldwork, knowledge of analogous sites, regulator requirements, and disciplinary expectations allow archaeologists to state why and how they plan to undertake research, if not what they will find.",
        "claim_type": "methodological",
        "reasoning_type": "pragmatic",
        "evidence_links": [],
        "verbatim_quote": "Training, prior fieldwork, knowledge of analogous sites or landscapes, regulator or funder requirements, and disciplinary expectations around fieldwork and publication all inform research. These prior requirements and similarities allow archaeologists to state why and how they plan to undertake research, if not what they will find.",
        "page_number": 8,
        "context": "Basis for preregistration despite serendipity",
        "certainty_qualifier": "practical argument"
    },
    {
        "id": "C060",
        "content": "Preregistration forces clarity and formalises a priori commitment to research design and recording strategy.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Preregistration forces a level of clarity and formalizes an a priori commitment to research design and recording strategy.",
        "page_number": 8,
        "context": "What preregistration accomplishes",
        "certainty_qualifier": "strong claim"
    },
    {
        "id": "C061",
        "content": "Since expected outcomes vary and are often externally dictated, articulation of research design is a particular benefit to archaeologists as it moves preparation to the less-fraught time before fieldwork.",
        "claim_type": "methodological",
        "reasoning_type": "pragmatic",
        "evidence_links": [],
        "verbatim_quote": "Indeed, since expected outcomes of research vary, and are often externally dictated (e.g., by heritage legislation), the articulation of research design is a particular benefit to archaeologists since it moves preparation to the less-fraught time before fieldwork begins.",
        "page_number": 8,
        "context": "Specific advantage for archaeology",
        "certainty_qualifier": "practical argument"
    },
    {
        "id": "C062",
        "content": "Preparatory work before fieldwork allows thoughtful development, testing, and revision of approaches, increasing chances that research design and collected data will support desired outcomes.",
        "claim_type": "methodological",
        "reasoning_type": "pragmatic",
        "evidence_links": [],
        "verbatim_quote": "This preparatory work allows thoughtful development, testing, and revision of approaches, increasing the chances that the research design and collected data will support the desired outcomes.",
        "page_number": 8,
        "context": "Benefits of advance planning",
        "certainty_qualifier": "increases chances (modal)"
    },
    {
        "id": "C063",
        "content": "Exigencies of fieldwork may suggest a pivot due to extraordinary finds or unsuitability of approach, but this argues for careful a priori research design.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "we recognize that exigencies of fieldwork may suggest a 'pivot' due to an extraordinary find or the late discovery of unsuitability in approach or documentation during execution. Preparing for the unexpected again argues for careful a priori research design",
        "page_number": 8,
        "context": "Addressing pivot objection",
        "certainty_qualifier": "acknowledging flexibility need"
    },
    {
        "id": "C064",
        "content": "The planning encouraged by preregistration should help avoid errors in design, especially if combined with pilot research.",
        "claim_type": "methodological",
        "reasoning_type": "pragmatic",
        "evidence_links": [],
        "verbatim_quote": "the planning encouraged by preregistration should help to avoid errors in design (especially if combined with pilot research)",
        "page_number": 8,
        "context": "How preregistration reduces need for pivots",
        "certainty_qualifier": "should (modal)"
    },
    {
        "id": "C065",
        "content": "The unpredictable nature of fieldwork should not preclude a best-effort at preregistration, and best-effort in an abductive discipline like archaeology should be considered sufficient.",
        "claim_type": "methodological",
        "reasoning_type": "normative",
        "evidence_links": [],
        "verbatim_quote": "Considering its potential value, the unpredictable nature of fieldwork should not preclude a 'best-effort' at preregistration – and a 'best-effort' in an abductive discipline like archaeology should be considered sufficient.",
        "page_number": 8,
        "context": "Concluding argument of section",
        "certainty_qualifier": "normative should statement"
    }
]

# ============================================================================
# IMPLICIT ARGUMENTS ITEMS
# ============================================================================

implicit_arguments = [
    {
        "id": "IA012",
        "content": "Built-in solutions are inherently superior to bolt-on fixes in research practice.",
        "reasoning": "This software engineering metaphor is presented as self-evidently applicable to research without justification.",
        "trigger_text": "It would make 'built-in' good practice more likely, as opposed to more common attempts to 'bolt-on' fixes after fieldwork",
        "page_number": 7,
        "context": "Marwick's metaphor adopted without critique",
        "theoretical_significance": "Imports engineering values (upfront specification) into humanistic research"
    },
    {
        "id": "IA013",
        "content": "Writing up stage is too late to properly document research design decisions.",
        "reasoning": "Assumes retrospective articulation is inherently problematic even if accurate.",
        "trigger_text": "An explicit research design documented in detail before research starts, rather than during the writing-up stage",
        "page_number": 8,
        "context": "Timing of documentation",
        "theoretical_significance": "Privileges prospective over retrospective documentation"
    },
    {
        "id": "IA014",
        "content": "Methodological diversity requires preregistration rather than making it inappropriate.",
        "reasoning": "Authors reframe potential objection (diversity makes preregistration inappropriate) into argument for preregistration, without acknowledging the objection's validity.",
        "trigger_text": "Indeed, the very complexity and diversity of archaeology... makes articulation of research design particularly important.",
        "page_number": 8,
        "context": "Addressing diversity argument",
        "theoretical_significance": "Rhetorical move to neutralise diversity objection"
    },
    {
        "id": "IA015",
        "content": "Best-effort preregistration is better than no preregistration.",
        "reasoning": "Assumes partial compliance with preregistration ideals is valuable even if incomplete.",
        "trigger_text": "the unpredictable nature of fieldwork should not preclude a 'best-effort' at preregistration – and a 'best-effort' in an abductive discipline like archaeology should be considered sufficient",
        "page_number": 8,
        "context": "Concluding argument",
        "theoretical_significance": "Pragmatic compromise on standards but still assumes preregistration valuable"
    },
    {
        "id": "IA016",
        "content": "Articulation of research design prevents unintentional conflation of approaches.",
        "reasoning": "Assumes researchers conflate approaches unintentionally rather than deliberately for productive theoretical synthesis.",
        "trigger_text": "avoids the unintentional conflation or elision of approaches that could undermine research results",
        "page_number": 8,
        "context": "Benefit of explicit design",
        "theoretical_significance": "Frames theoretical integration as error rather than synthesis"
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
    'section_extracted': 'Groups 1-3: Introduction through Suitability, pages 2-8',
    'extraction_strategy': 'Section 3: Liberal extraction focusing on: (1) claims about archaeological methodological diversity (deductive/inductive, quantitative/qualitative, idiographic/nomothetic, abductive synthesis), (2) arguments that preregistration accommodates this diversity, (3) serendipity objection and response, (4) implicit assumptions about built-in vs bolt-on and best-effort standards. Minimal new evidence - primarily argumentative section.',
    'known_uncertainties': [
        'Some claims about archaeological practice (e.g., C049, C052, C056) may reflect authors\' characterisation rather than documented patterns',
        'Distinction between claims about what preregistration "can" do vs "does" do important',
        'Best-effort standard (C065, IA015) introduces flexibility that may complicate later evaluation'
    ],
    'section_word_count_estimate': 3600
}

data['extraction_timestamp'] = datetime.now().isoformat() + 'Z'

# Save updated extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print("=" * 80)
print("PASS 1 - SECTION GROUP 3 EXTRACTION COMPLETE")
print("=" * 80)
print()
print(f"Section: Preregistration is Suitable for Archaeology")
print(f"Pages: 7-8")
print(f"Estimated word count: ~1000 words")
print()
print("Items extracted:")
print(f"  Evidence: {len(evidence_items)} items (no new evidence)")
print(f"  Claims: {len(claims_items)} items (C044-C065)")
print(f"  Implicit Arguments: {len(implicit_arguments)} items (IA012-IA016)")
print()
print(f"Total this section: {len(evidence_items) + len(claims_items) + len(implicit_arguments)} items")
print()
print("Cumulative extraction:")
print(f"  Evidence: 10 items total")
print(f"  Claims: 65 items total")
print(f"  Implicit Arguments: 16 items total")
print(f"  TOTAL: 91 items extracted so far")
print()
print("✓ Section 3 extraction complete")
print()
