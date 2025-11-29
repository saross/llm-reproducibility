#!/usr/bin/env python3
"""
Pass 1 Liberal Extraction - Section Group 1
Paper: Sobotkova et al. 2024 - Validating predictions of burial mounds
Section: Abstract + Introduction + Background (lines 21-253)
Estimated words: ~2,400

Extraction Philosophy: LIBERAL - When uncertain, INCLUDE IT
Sourcing Discipline: 100% - Every item must have verbatim_quote OR trigger_text

This script extracts:
- Evidence (observations, measurements, data)
- Claims (assertions, interpretations, findings)
- Implicit Arguments (systematic 4-type scan for all core claims)
"""

import json
from pathlib import Path

# Load existing extraction.json
extraction_file = Path("/home/shawn/Code/llm-reproducibility/outputs/sobotkova-et-al-2024/extraction.json")
with open(extraction_file, 'r') as f:
    extraction = json.load(f)

# Section Group 1: Abstract + Introduction + Background
# Core Claims Identified (for systematic implicit argument scanning):
# C001: ML/CNN approaches have limitations when detecting varied features in heterogeneous landscapes
# C002: Pre-trained CNN with low-touch training failed to detect burial mounds effectively
# C003: External validation with field data is essential for CNN workflows
# C004: Manual approaches may be more efficient than ML for this application
# C005: Publication bias exists in ML-for-archaeology literature (overwhelmingly positive tone)

#############################################################################
# EVIDENCE ITEMS
#############################################################################

evidence_items = [
    {
        "evidence_id": "E001",
        "evidence_text": "False negative rates were 95-96% of tiles",
        "evidence_type": "quantitative_measurement",
        "evidence_status": "explicit",
        "verbatim_quote": "false negative rates were 95–96%",
        "location": {
            "section": "Abstract",
            "subsection": "Findings",
            "paragraph": 1
        },
        "uncertainty_declared": False,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C002", "C003", "C004"]
    },
    {
        "evidence_id": "E002",
        "evidence_text": "False positive rates were 87-95% of tagged tiles",
        "evidence_type": "quantitative_measurement",
        "evidence_status": "explicit",
        "verbatim_quote": "false positive rates were 87–95% of tagged tiles",
        "location": {
            "section": "Abstract",
            "subsection": "Findings",
            "paragraph": 1
        },
        "uncertainty_declared": False,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C002", "C003", "C004"]
    },
    {
        "evidence_id": "E003",
        "evidence_text": "True positives were only 5-13% of tagged tiles",
        "evidence_type": "quantitative_measurement",
        "evidence_status": "explicit",
        "verbatim_quote": "true positives were only 5–13%",
        "location": {
            "section": "Abstract",
            "subsection": "Findings",
            "paragraph": 1
        },
        "uncertainty_declared": False,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C002"]
    },
    {
        "evidence_id": "E004",
        "evidence_text": "Model development required approximately 135 person-hours of work",
        "evidence_type": "quantitative_measurement",
        "evidence_status": "explicit",
        "verbatim_quote": "Development of the model, meanwhile, required approximately 135 person-hours of work.",
        "location": {
            "section": "Abstract",
            "subsection": "Findings",
            "paragraph": 1
        },
        "uncertainty_declared": True,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C004"]
    },
    {
        "evidence_id": "E005",
        "evidence_text": "Model provided with training data for highly visible mounds performed worse than model with all mounds",
        "evidence_type": "comparative_observation",
        "evidence_status": "explicit",
        "verbatim_quote": "Counterintuitively, the model provided with training data selected for highly visible mounds (rather than all mounds) performed worse.",
        "location": {
            "section": "Abstract",
            "subsection": "Findings",
            "paragraph": 1
        },
        "uncertainty_declared": False,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C001", "C002"]
    },
    {
        "evidence_id": "E006",
        "evidence_text": "High success rates reported for burial mound detection in Siberia",
        "evidence_type": "literature_reference",
        "evidence_status": "explicit",
        "verbatim_quote": "High success rates reported for detecting and monitoring burial mounds in Siberia have highlighted CNNs as an effective approach for large-scale prospection (Caspari and Crespo, 2019).",
        "location": {
            "section": "Introduction",
            "subsection": None,
            "paragraph": 1
        },
        "uncertainty_declared": False,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C006"]
    },
    {
        "evidence_id": "E007",
        "evidence_text": "Siberian burial mounds are uniform features in environments with little vegetation or confounding factors",
        "evidence_type": "contextual_observation",
        "evidence_status": "explicit",
        "verbatim_quote": "Enthusiasm arising from this study, and similar outcomes from Egypt (Woolf, 2018) must, however, be tempered by the fact that the authors targeted uniform features situated in environments with little variation in terrain or vegetation – indeed, with relatively little vegetation or other confounding factors at all.",
        "location": {
            "section": "Introduction",
            "subsection": None,
            "paragraph": 1
        },
        "uncertainty_declared": False,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C001", "C006"]
    },
    {
        "evidence_id": "E008",
        "evidence_text": "Linear road feature classification with pre-trained model required 1,250 hours to digitise and annotate training datasets",
        "evidence_type": "quantitative_measurement",
        "evidence_status": "explicit",
        "verbatim_quote": "Correct classification of linear road features with a pre-trained model required 1,250 h to digitise and annotate training datasets (Can et al., 2021, p. 62,847).",
        "location": {
            "section": "Introduction",
            "subsection": None,
            "paragraph": 2
        },
        "uncertainty_declared": False,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C007"]
    },
    {
        "evidence_id": "E009",
        "evidence_text": "Estimates of surviving Bulgarian burial mounds range between 8,000-19,000 today, of perhaps 50,000 originally constructed",
        "evidence_type": "quantitative_measurement",
        "evidence_status": "explicit",
        "verbatim_quote": "Thousands of such mounds exist in the country; estimates range between 8,000 – 19,000 surviving today, of perhaps 50,000 originally constructed (Kitov, 1993, pp. 41–43; Shkorpil and Shkorpil, 1989, p. 20).",
        "location": {
            "section": "Burial mounds as heritage under threat",
            "subsection": None,
            "paragraph": 1
        },
        "uncertainty_declared": True,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C009"]
    },
    {
        "evidence_id": "E010",
        "evidence_text": "Burial mounds vary in diameter from 10m to 100m and <1m to >20m in height",
        "evidence_type": "quantitative_measurement",
        "evidence_status": "explicit",
        "verbatim_quote": "These rounded, conical piles of earth and stones vary in diameter from 10 m to 100 m and <1 m to >20 m in height (see Plates 1 and 2).",
        "location": {
            "section": "Burial mounds as heritage under threat",
            "subsection": None,
            "paragraph": 2
        },
        "uncertainty_declared": False,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C001", "C010"]
    },
    {
        "evidence_id": "E011",
        "evidence_text": "In 2008, burial mounds comprised nearly a quarter (57 of 257) of all excavations in Bulgaria",
        "evidence_type": "quantitative_measurement",
        "evidence_status": "explicit",
        "verbatim_quote": "In 2008, the last year for which data is available, burial mounds comprised nearly a quarter (57 of 257) of all excavations in Bulgaria (Cholakov and Chukalev, 2008, p. 91, Figure 2).",
        "location": {
            "section": "Burial mounds as heritage under threat",
            "subsection": None,
            "paragraph": 3
        },
        "uncertainty_declared": False,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C011"]
    },
    {
        "evidence_id": "E012",
        "evidence_text": "Authors inventoried over 2,000 burial mounds across two Bulgarian provinces",
        "evidence_type": "quantitative_measurement",
        "evidence_status": "explicit",
        "verbatim_quote": "In the course of nearly 20 years of intermittent fieldwork in Bulgaria, the authors have seen few examples of mounds that had not been damaged either by development, looting, or agriculture, despite having inventoried over 2,000 of them across two Bulgarian provinces (Ross et al., 2010, 2018; Sobotkova and Weissova, 2020).",
        "location": {
            "section": "Burial mounds as heritage under threat",
            "subsection": None,
            "paragraph": 5
        },
        "uncertainty_declared": False,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C012"]
    },
    {
        "evidence_id": "E013",
        "evidence_text": "Large mounds in flat landscapes with surface contrast are more visible than small mounds in hilly landscapes",
        "evidence_type": "comparative_observation",
        "evidence_status": "explicit",
        "verbatim_quote": "Large mounds in flat landscapes where a mound's surface contrasts with surrounding land cover (Figure 1a, b, e) are more visible than small mounds in hilly landscapes where their surfaces blend into the surroundings (Figure 1g-i).",
        "location": {
            "section": "Detecting archaeological features in satellite imagery",
            "subsection": None,
            "paragraph": 2
        },
        "uncertainty_declared": False,
        "uncertainty_missing": False,
        "confidence_declared": False,
        "supports_claims": ["C001", "C010"]
    }
]

#############################################################################
# CLAIMS ITEMS
#############################################################################

claims_items = [
    {
        "claim_id": "C001",
        "claim_text": "Pre-trained CNNs have significant limitations when detecting varied features of different sizes within heterogeneous landscapes containing confounding natural and modern features",
        "claim_type": "finding",
        "claim_role": "core",
        "claim_status": "explicit",
        "verbatim_quote": "Our attempt to deploy a pre-trained CNN demonstrates the limitations of this approach when it is used to detect varied features of different sizes within a heterogeneous landscape that contains confounding natural and modern features, such as roads, forests and field boundaries.",
        "location": {
            "section": "Abstract",
            "subsection": "Research limitations/implications",
            "paragraph": 1
        },
        "supported_by_evidence": ["E005", "E007", "E010", "E013"],
        "supported_by_claims": [],
        "supports_claims": [],
        "alternatives_mentioned": False,
        "qualifications": [],
        "contradicts": []
    },
    {
        "claim_id": "C002",
        "claim_text": "The pre-trained CNN model failed to identify burial mounds in the Kazanlak Valley study area",
        "claim_type": "finding",
        "claim_role": "core",
        "claim_status": "explicit",
        "verbatim_quote": "Indeed, both models failed to identify burial mounds in our study area.",
        "location": {
            "section": "Introduction",
            "subsection": None,
            "paragraph": 4
        },
        "supported_by_evidence": ["E001", "E002", "E003", "E005"],
        "supported_by_claims": [],
        "supports_claims": [],
        "alternatives_mentioned": False,
        "qualifications": [],
        "contradicts": ["C006"]
    },
    {
        "claim_id": "C003",
        "claim_text": "External validation with field data is an essential part of CNN workflows",
        "claim_type": "methodological",
        "claim_role": "core",
        "claim_status": "explicit",
        "verbatim_quote": "The model has detected incidental features rather than the mounds themselves, making external validation with field data an essential part of CNN workflows.",
        "location": {
            "section": "Abstract",
            "subsection": "Research limitations/implications",
            "paragraph": 1
        },
        "supported_by_evidence": ["E001", "E002"],
        "supported_by_claims": ["C002"],
        "supports_claims": [],
        "alternatives_mentioned": False,
        "qualifications": [],
        "contradicts": []
    },
    {
        "claim_id": "C004",
        "claim_text": "Manual inspection by experts or crowdsourcing may be more efficient than ML for identifying burial mounds",
        "claim_type": "recommendation",
        "claim_role": "core",
        "claim_status": "explicit",
        "verbatim_quote": "The degree of manual intervention required – particularly around the subsetting and annotation of training data – is so significant that it raises the question of whether it would be more efficient to identify all of the mounds manually, either through brute-force inspection by experts or by crowdsourcing the analysis to trained – or even untrained – volunteers.",
        "location": {
            "section": "Abstract",
            "subsection": "Practical implications",
            "paragraph": 1
        },
        "supported_by_evidence": ["E001", "E002", "E004"],
        "supported_by_claims": ["C002"],
        "supports_claims": [],
        "alternatives_mentioned": True,
        "qualifications": [],
        "contradicts": []
    },
    {
        "claim_id": "C005",
        "claim_text": "ML-for-archaeology literature is overwhelmingly positive, reflecting publication bias and rhetoric of unconditional success",
        "claim_type": "methodological_critique",
        "claim_role": "core",
        "claim_status": "explicit",
        "verbatim_quote": "The literature itself, however, is overwhelmingly positive, reflecting some combination of publication bias and a rhetoric of unconditional success.",
        "location": {
            "section": "Abstract",
            "subsection": "Social implications",
            "paragraph": 1
        },
        "supported_by_evidence": [],
        "supported_by_claims": [],
        "supports_claims": [],
        "alternatives_mentioned": False,
        "qualifications": ["reflecting some combination of"],
        "contradicts": []
    },
    {
        "claim_id": "C006",
        "claim_text": "CNNs have been promoted as effective for large-scale archaeological prospection",
        "claim_type": "literature_synthesis",
        "claim_role": "intermediate",
        "claim_status": "explicit",
        "verbatim_quote": "High success rates reported for detecting and monitoring burial mounds in Siberia have highlighted CNNs as an effective approach for large-scale prospection (Caspari and Crespo, 2019).",
        "location": {
            "section": "Introduction",
            "subsection": None,
            "paragraph": 1
        },
        "supported_by_evidence": ["E006"],
        "supported_by_claims": [],
        "supports_claims": [],
        "alternatives_mentioned": False,
        "qualifications": [],
        "contradicts": []
    },
    {
        "claim_id": "C007",
        "claim_text": "ML applied to archaeological prospection can be labour-intensive",
        "claim_type": "finding",
        "claim_role": "intermediate",
        "claim_status": "explicit",
        "verbatim_quote": "Although few publications report the time, expertise, or costs associated with applying ML to archaeological prospection, examples from projects trying to extract symbols and text from historical maps indicate that it can be labour-intensive (Can et al., 2021; Ekim et al., 2021; Ma et al., 2021).",
        "location": {
            "section": "Introduction",
            "subsection": None,
            "paragraph": 2
        },
        "supported_by_evidence": ["E008"],
        "supported_by_claims": [],
        "supports_claims": ["C004"],
        "alternatives_mentioned": False,
        "qualifications": ["can be"],
        "contradicts": []
    },
    {
        "claim_id": "C008",
        "claim_text": "Transfer learning with pre-trained models is proposed as solution to limited training data and small dataset size problems",
        "claim_type": "literature_synthesis",
        "claim_role": "supporting",
        "claim_status": "explicit",
        "verbatim_quote": "Transfer learning based on pre-trained models is sometimes proposed as solution to the problem of limited training data, as well as related problems like small dataset size (Casini et al., 2021, 2022; Character et al., 2021; Gallwey et al., 2019; Sech et al., 2023; Xiong et al., 2020).",
        "location": {
            "section": "Introduction",
            "subsection": None,
            "paragraph": 3
        },
        "supported_by_evidence": [],
        "supported_by_claims": [],
        "supports_claims": [],
        "alternatives_mentioned": False,
        "qualifications": ["sometimes proposed"],
        "contradicts": []
    },
    {
        "claim_id": "C009",
        "claim_text": "Burial mounds are endangered heritage in Bulgaria",
        "claim_type": "contextual",
        "claim_role": "supporting",
        "claim_status": "explicit",
        "verbatim_quote": "Despite the large number of burial mounds, they are endangered.",
        "location": {
            "section": "Burial mounds as heritage under threat",
            "subsection": None,
            "paragraph": 3
        },
        "supported_by_evidence": ["E009", "E011"],
        "supported_by_claims": ["C011", "C012"],
        "supports_claims": [],
        "alternatives_mentioned": False,
        "qualifications": [],
        "contradicts": []
    },
    {
        "claim_id": "C010",
        "claim_text": "Burial mound visibility in satellite imagery depends on size, terrain, and land cover",
        "claim_type": "finding",
        "claim_role": "supporting",
        "claim_status": "explicit",
        "verbatim_quote": "While burial mounds are readily identifiable on the ground due to their distinctive appearance, their visibility in satellite imagery depends on their size, surrounding terrain, and local land cover (see Figure 1).",
        "location": {
            "section": "Detecting archaeological features in satellite imagery",
            "subsection": None,
            "paragraph": 1
        },
        "supported_by_evidence": ["E010", "E013"],
        "supported_by_claims": [],
        "supports_claims": ["C001"],
        "alternatives_mentioned": False,
        "qualifications": [],
        "contradicts": []
    },
    {
        "claim_id": "C011",
        "claim_text": "Development in Bulgaria destroys dozens of mounds annually",
        "claim_type": "contextual",
        "claim_role": "supporting",
        "claim_status": "explicit",
        "verbatim_quote": "Development in Bulgaria destroys dozens of mounds annually (Loulanski and Loulanski, 2017).",
        "location": {
            "section": "Burial mounds as heritage under threat",
            "subsection": None,
            "paragraph": 3
        },
        "supported_by_evidence": ["E011"],
        "supported_by_claims": [],
        "supports_claims": ["C009"],
        "alternatives_mentioned": False,
        "qualifications": [],
        "contradicts": []
    },
    {
        "claim_id": "C012",
        "claim_text": "Few examples of undamaged burial mounds exist despite extensive inventory work",
        "claim_type": "finding",
        "claim_role": "supporting",
        "claim_status": "explicit",
        "verbatim_quote": "In the course of nearly 20 years of intermittent fieldwork in Bulgaria, the authors have seen few examples of mounds that had not been damaged either by development, looting, or agriculture, despite having inventoried over 2,000 of them across two Bulgarian provinces (Ross et al., 2010, 2018; Sobotkova and Weissova, 2020).",
        "location": {
            "section": "Burial mounds as heritage under threat",
            "subsection": None,
            "paragraph": 5
        },
        "supported_by_evidence": ["E012"],
        "supported_by_claims": [],
        "supports_claims": ["C009"],
        "alternatives_mentioned": False,
        "qualifications": [],
        "contradicts": []
    }
]

#############################################################################
# IMPLICIT ARGUMENTS (Systematic 4-type scan for each CORE claim)
#############################################################################

implicit_arguments = [
    {
        "implicit_argument_id": "IA001",
        "implicit_argument_text": "Self-reported model performance metrics (F1 scores) are insufficient for assessing real-world ML efficacy without field validation",
        "implicit_argument_type": "unstated_assumption",
        "trigger_text": [
            "Validation of results against field data showed that self-reported success rates were misleadingly high, and that the model was misidentifying most features.",
            "The model has detected incidental features rather than the mounds themselves, making external validation with field data an essential part of CNN workflows."
        ],
        "trigger_locations": [
            {"section": "Abstract", "subsection": "Findings", "paragraph": 1},
            {"section": "Abstract", "subsection": "Research limitations/implications", "paragraph": 1}
        ],
        "inference_reasoning": "The paper contrasts 'self-reported success rates' (internal model metrics) with 'field validation' outcomes, asserting the former were 'misleadingly high'. This implicitly argues that standard ML performance metrics alone cannot reliably assess real-world detection efficacy, requiring the unstated assumption that field validation is necessary to reveal actual performance. Without stating this assumption explicitly, the authors position field validation as essential—implying internal metrics are systematically inadequate for assessment.",
        "location": {
            "section": "Abstract",
            "subsection": "Findings",
            "paragraph": 1
        },
        "supports_claims": ["C002", "C003"],
        "assessment_implication": "Critical for assessing transparency. Papers reporting only internal ML metrics without field validation may overstate real-world performance. This assumption affects interpretation of success claims in ML-for-archaeology literature."
    },
    {
        "implicit_argument_id": "IA002",
        "implicit_argument_text": "More curation of training data does not necessarily improve model performance when fundamental approach limitations exist",
        "implicit_argument_type": "logical_implication",
        "trigger_text": [
            "Counterintuitively, the model provided with training data selected for highly visible mounds (rather than all mounds) performed worse.",
            "Despite increased effort in the selection of training data, the second run of the model reported a lower F1 score (0.62) and at >60% probability produced even more false positives (94.8%) and false negatives (96.2%)."
        ],
        "trigger_locations": [
            {"section": "Abstract", "subsection": "Findings", "paragraph": 1},
            {"section": "Introduction", "subsection": None, "paragraph": 4}
        ],
        "inference_reasoning": "The paper reports that additional curation (selecting only highly visible mounds) led to worse performance. This counterintuitive outcome implies that when core methodological limitations exist (fixed tile size, heterogeneous backgrounds), data curation cannot compensate. The logical implication is that training data quality improvements have limits—fundamental approach constraints must be addressed first. This challenges the common ML assumption that better training data improves performance.",
        "location": {
            "section": "Abstract",
            "subsection": "Findings",
            "paragraph": 1
        },
        "supports_claims": ["C001", "C002"],
        "assessment_implication": "Affects assessment of methodological adequacy. Reveals that data curation is insufficient when detection approach is mismatched to feature characteristics. Challenges reproducibility if similar projects assume data quality is primary constraint."
    },
    {
        "implicit_argument_id": "IA003",
        "implicit_argument_text": "Computational infrastructure and technical expertise requirements exclude most cultural heritage practitioners from implementing effective ML",
        "implicit_argument_type": "bridging_claim",
        "trigger_text": [
            "Correcting the model would require refining the training data as well as adopting different approaches to model choice and execution, raising the computational requirements beyond the level of most cultural heritage practitioners.",
            "The degree of manual intervention required – particularly around the subsetting and annotation of training data – is so significant that it raises the question of whether it would be more efficient to identify all of the mounds manually"
        ],
        "trigger_locations": [
            {"section": "Abstract", "subsection": "Research limitations/implications", "paragraph": 1},
            {"section": "Abstract", "subsection": "Practical implications", "paragraph": 1}
        ],
        "inference_reasoning": "The paper bridges from evidence (135 person-hours, need for specialists, computational requirements) to recommendation (manual approaches may be preferable) via an unstated claim about practitioner capacity. The bridge is: 'most cultural heritage practitioners lack' the resources/expertise/infrastructure to implement corrections. Without this assumption, the leap from 'model needs improvement' to 'manual may be better' is incomplete. The bridging claim makes the recommendation logical.",
        "location": {
            "section": "Abstract",
            "subsection": "Practical implications",
            "paragraph": 1
        },
        "supports_claims": ["C004"],
        "assessment_implication": "Critical for assessing applicability. If most practitioners cannot implement these methods effectively, generalisability of successful ML approaches is limited. Affects transparency about accessibility of methods."
    },
    {
        "implicit_argument_id": "IA004",
        "implicit_argument_text": "Publication bias in favour of positive ML results systematically misrepresents technology effectiveness to potential adopters",
        "implicit_argument_type": "logical_implication",
        "trigger_text": [
            "The literature itself, however, is overwhelmingly positive, reflecting some combination of publication bias and a rhetoric of unconditional success.",
            "This paper presents the failure of a good-faith attempt to utilise these approaches as a counterbalance and cautionary tale to potential adopters of the technology."
        ],
        "trigger_locations": [
            {"section": "Abstract", "subsection": "Social implications", "paragraph": 1},
            {"section": "Abstract", "subsection": "Social implications", "paragraph": 1}
        ],
        "inference_reasoning": "The paper identifies 'overwhelmingly positive' literature and positions their failure report as 'counterbalance' and 'cautionary tale'. This implies that positive bias systematically misrepresents effectiveness—potential adopters receive skewed information affecting their technology decisions. Without stating this explicitly, the authors argue that failure to report negative outcomes causes systematic misinformation about ML efficacy, affecting adoption decisions. This is a logical implication of publication bias: if failures are underreported, success rates appear higher than reality.",
        "location": {
            "section": "Abstract",
            "subsection": "Social implications",
            "paragraph": 1
        },
        "supports_claims": ["C005"],
        "assessment_implication": "Affects assessment of literature credibility and technology adoption guidance. Suggests systematic bias in evidence base affects reproducibility expectations and resource allocation decisions."
    },
    {
        "implicit_argument_id": "IA005",
        "implicit_argument_text": "Successful ML applications in uniform environments do not generalise to heterogeneous landscapes",
        "implicit_argument_type": "unstated_assumption",
        "trigger_text": [
            "Enthusiasm arising from this study, and similar outcomes from Egypt (Woolf, 2018) must, however, be tempered by the fact that the authors targeted uniform features situated in environments with little variation in terrain or vegetation",
            "Fewer studies explore the challenges presented by more difficult environments where cultural heritage lies in diverse or thick vegetation, surrounded by obtrusive natural and artificial features"
        ],
        "trigger_locations": [
            {"section": "Introduction", "subsection": None, "paragraph": 1},
            {"section": "Introduction", "subsection": None, "paragraph": 1}
        ],
        "inference_reasoning": "The paper distinguishes 'uniform features' in simple environments (Siberia, Egypt successes) from 'more difficult environments' with 'diverse vegetation' and 'obtrusive features' (their case). The tempering caveat implies that success in uniform settings provides limited evidence for heterogeneous settings. This unstated assumption—that environmental complexity fundamentally affects ML transferability—underlies their methodological positioning. Without stating this explicitly, they argue Siberian success does not predict Bulgarian performance due to landscape differences.",
        "location": {
            "section": "Introduction",
            "subsection": None,
            "paragraph": 1
        },
        "supports_claims": ["C001", "C006"],
        "assessment_implication": "Critical for assessing methodological transferability. Success claims from simple environments may not apply to complex settings. Affects reproducibility expectations and comparative assessment."
    },
    {
        "implicit_argument_id": "IA006",
        "implicit_argument_text": "Pre-trained CNN approach was reasonable to attempt despite ultimately failing",
        "implicit_argument_type": "unstated_assumption",
        "trigger_text": [
            "This paper offers a cautionary tale about the challenges, limitations, and demands of ML applied to archaeological prospection.",
            "We set out to detect burial mounds in the Kazanlak Valley, Bulgaria, using IKONOS high-resolution satellite imagery. We developed a pre-trained CNN that was further trained using two datasets"
        ],
        "trigger_locations": [
            {"section": "Introduction", "subsection": None, "paragraph": 4},
            {"section": "Introduction", "subsection": None, "paragraph": 4}
        ],
        "inference_reasoning": "The paper positions their attempt as a 'cautionary tale' rather than methodological error, and describes their approach in neutral terms ('we set out to', 'we developed'). This framing implicitly assumes the approach was reasonable and well-intentioned despite failure—i.e., failure resulted from inherent limitations, not poor execution. Without this assumption, the paper could be read as documenting researcher error rather than technology limitation. The unstated assumption legitimises the attempt, making failure informative rather than simply mistaken.",
        "location": {
            "section": "Introduction",
            "subsection": None,
            "paragraph": 4
        },
        "supports_claims": ["C001", "C002"],
        "assessment_implication": "Affects assessment of methodological adequacy. Positions failure as informative about technology limits rather than execution problems. Supports credibility of negative findings."
    }
]

#############################################################################
# Add items to extraction
#############################################################################

extraction["evidence"].extend(evidence_items)
extraction["claims"].extend(claims_items)
extraction["implicit_arguments"].extend(implicit_arguments)

# Update extraction notes
extraction["extraction_metadata"]["extraction_notes"].append({
    "pass1_section1": {
        "section_group": "Abstract + Introduction + Background",
        "word_count_estimate": 2400,
        "sections_combined": [
            "Abstract",
            "Introduction",
            "Burial mounds as heritage under threat",
            "Detecting archaeological features in satellite imagery"
        ],
        "extraction_date": "2025-10-30",
        "items_extracted": {
            "evidence": len(evidence_items),
            "claims": len(claims_items),
            "implicit_arguments": len(implicit_arguments)
        },
        "core_claims_identified": 5,
        "implicit_argument_scan_completed": True,
        "notes": "Liberal extraction applied. Systematic 4-type implicit argument scan completed for all 5 core claims (C001-C005). All evidence and claims have verbatim_quote sourcing. All implicit arguments have trigger_text arrays with proper inference_reasoning."
    }
})

# Save updated extraction
with open(extraction_file, 'w') as f:
    json.dump(extraction, f, indent=2, ensure_ascii=False)

print("✓ Pass 1 Section 1 extraction complete")
print(f"  Evidence: {len(evidence_items)} items")
print(f"  Claims: {len(claims_items)} items")
print(f"  Implicit Arguments: {len(implicit_arguments)} items")
print(f"  Total: {len(evidence_items) + len(claims_items) + len(implicit_arguments)} items")
