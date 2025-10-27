#!/usr/bin/env python3
"""
Section-by-Section Implicit Arguments Extraction Template

Demonstrates extracting implicit arguments for core claims in a section.
Adapt for each section: Abstract, Introduction, Methods, Results, Discussion.

Key principle:
Each CORE claim requires systematic 4-type implicit argument scan:
- Type 1: Logical Implications
- Type 2: Unstated Assumptions
- Type 3: Bridging Claims
- Type 4: Disciplinary Assumptions

Common failure mode: Only extracting Type 1 (logical implications), missing
Types 2-4 which are often more assessment-critical.

Recognition patterns:
- Undefended quality judgments (Pattern 1)
- Comparison without baseline (Pattern 2)
- Capability assumptions (Pattern 3)
- Inferential leaps (Pattern 4)
- Definitional assumptions (Pattern 5)
- Causal assumptions (Pattern 6)
"""

import json

# Load existing extraction
with open('extraction.json', 'r') as f:
    data = json.load(f)

# ============================================
# IMPLICIT ARGUMENTS FOR CORE CLAIMS
# ============================================

# EXAMPLE 1: Type 3 (Bridging Claim) - Quality threshold assumption
# Pattern 1: Undefended Quality Judgment
# Core claim: "Data quality was high"
# Gap: What makes quality "high"?
implicit_argument_type3_quality = {
    "implicit_argument_id": "IA001",
    "implicit_argument_type": "bridging_claim",
    "implicit_argument_text": "95% spatial accuracy threshold defines 'high quality' data for archaeological survey purposes",

    # CRITICAL: trigger_text must be verbatim passages from paper
    "trigger_text": [
        "The resulting dataset had 95.7% spatial accuracy.",
        "Data quality was high, meeting project requirements.",
        "High-quality data enabled reliable spatial analysis."
    ],

    # CRITICAL: trigger_locations specify where each trigger found
    "trigger_locations": [
        {"section": "Results", "subsection": "3.2", "page": 8, "paragraph": 2},
        {"section": "Results", "subsection": "3.3", "page": 9, "paragraph": 1},
        {"section": "Discussion", "subsection": "4.1", "page": 10, "paragraph": 3}
    ],

    # CRITICAL: inference_reasoning explains how triggers imply the implicit argument
    "inference_reasoning": "Paper repeatedly asserts data quality was 'high' (3 locations) and suitable for analysis. However, the paper never defines what threshold or criteria constitute 'high quality'. The only quantitative quality measure mentioned is 95.7% spatial accuracy. The bridging claim—that 95% accuracy = 'high quality'—is required to connect the evidence (95.7% accuracy) to the claims (high quality, suitable for analysis), but this threshold adequacy is never defended or justified.",

    # CRITICAL: implicit_metadata required for implicit arguments
    "implicit_metadata": {
        "basis": "definitional_gap",
        "confidence": "high",
        "assessment_implication": "Cannot assess whether 95% accuracy threshold is appropriate for archaeological survey context. 'High quality' judgement may be inadequately justified if threshold is arbitrary or insufficiently rigorous for intended analyses."
    },

    "supports_claim": ["C015"],  # The "data quality was high" claim

    "location": {
        "section": "Results",
        "subsection": "3.2",
        "page": 8
    }
}

# EXAMPLE 2: Type 2 (Unstated Assumption) - Capability adequacy
# Pattern 3: Capability Assumption
# Core claim: "Mobile platform enabled comprehensive spatial data collection"
# Assumption: GPS precision adequate for research scale
implicit_argument_type2_capability = {
    "implicit_argument_id": "IA002",
    "implicit_argument_type": "unstated_assumption",
    "implicit_argument_text": "GPS coordinate precision of consumer-grade smartphones is adequate for archaeological feature mapping at survey scale",

    "trigger_text": [
        "Students used their personal Android smartphones to collect spatial data.",
        "GPS coordinates were automatically captured for each mapped feature.",
        "The mobile platform enabled comprehensive spatial coverage across 22 survey areas."
    ],

    "trigger_locations": [
        {"section": "Methods", "subsection": "2.3", "page": 5, "paragraph": 2},
        {"section": "Methods", "subsection": "2.4", "page": 6, "paragraph": 1},
        {"section": "Results", "subsection": "3.1", "page": 7, "paragraph": 1}
    ],

    "inference_reasoning": "Paper describes using consumer smartphone GPS for archaeological spatial data collection and claims this enabled 'comprehensive spatial coverage'. However, the paper never discusses GPS accuracy/precision specifications, never verifies coordinate accuracy against ground truth, and never addresses whether consumer GPS precision (typically 3-10m) is adequate for archaeological feature mapping. The entire spatial analysis assumes GPS precision is fit-for-purpose, but this critical assumption is never stated or justified.",

    "implicit_metadata": {
        "basis": "methodological_adequacy_assumption",
        "confidence": "high",
        "assessment_implication": "Cannot assess whether GPS precision is appropriate for archaeological feature mapping. If features are small (<5m) or precise locations critical, consumer GPS may be inadequate. Spatial analysis credibility depends on unstated and unverified GPS adequacy assumption."
    },

    "supports_claim": ["C003", "C008"],  # Claims about platform capabilities and spatial coverage

    "location": {
        "section": "Methods",
        "subsection": "2.3",
        "page": 5
    }
}

# EXAMPLE 3: Type 1 (Logical Implication) - Comparison baseline
# Pattern 2: Comparison Without Baseline
# Core claim: "Mobile platform was significantly more efficient than previous methods"
# Implication: Must have baseline measurement or expectations
implicit_argument_type1_comparison = {
    "implicit_argument_id": "IA003",
    "implicit_argument_type": "logical_implication",
    "implicit_argument_text": "Previous paper-based survey methods required substantially more time per feature (baseline comparison enabling 'more efficient' claim)",

    "trigger_text": [
        "The mobile platform was significantly more efficient than previous approaches.",
        "Traditional paper-based survey methods required extensive post-processing.",
        "Digital data collection reduced field time from weeks to days."
    ],

    "trigger_locations": [
        {"section": "Discussion", "subsection": "4.2", "page": 11, "paragraph": 2},
        {"section": "Introduction", "subsection": "1.2", "page": 2, "paragraph": 3},
        {"section": "Results", "subsection": "3.4", "page": 9, "paragraph": 4}
    ],

    "inference_reasoning": "'Significantly more efficient' is an explicit comparative claim requiring a baseline. Paper mentions 'previous approaches' and 'traditional methods' as comparison points, and notes 'weeks to days' improvement. This logically implies that previous methods had measured (or at minimum, estimated) time requirements that serve as the comparison baseline. However, paper never explicitly states previous method time requirements or how baseline was established (measured? estimated? remembered?). The comparison claim logically requires this baseline to exist, even though unstated.",

    "implicit_metadata": {
        "basis": "logical_requirement",
        "confidence": "high",
        "assessment_implication": "Cannot assess validity of efficiency claim without knowing baseline measurement rigour. If baseline is informal estimate rather than measured data, 'significantly more efficient' claim may be inadequately supported. Comparison credibility depends on baseline quality."
    },

    "supports_claim": ["C020"],  # The "more efficient" claim

    "location": {
        "section": "Discussion",
        "subsection": "4.2",
        "page": 11
    }
}

# EXAMPLE 4: Type 4 (Disciplinary Assumption) - Field-specific knowledge
# Pattern 4: Inferential Leap requiring disciplinary knowledge
# Core claim: "Student volunteers were capable of producing research-quality data"
# Assumption: Minimal training + supervision = adequate data quality (disciplinary norm)
implicit_argument_type4_disciplinary = {
    "implicit_argument_id": "IA004",
    "implicit_argument_type": "disciplinary_assumption",
    "implicit_argument_text": "In archaeological survey, non-experts with minimal training and remote supervision can produce data quality comparable to expert surveyors (disciplinary assumption about task accessibility)",

    "trigger_text": [
        "After a brief 2-hour training session, students began independent fieldwork.",
        "Remote supervision via mobile communication proved sufficient for quality control.",
        "Student volunteers were capable of producing research-quality data with minimal oversight."
    ],

    "trigger_locations": [
        {"section": "Methods", "subsection": "2.2", "page": 4, "paragraph": 4},
        {"section": "Results", "subsection": "3.3", "page": 8, "paragraph": 3},
        {"section": "Discussion", "subsection": "4.3", "page": 12, "paragraph": 1}
    ],

    "inference_reasoning": "Paper claims non-expert students with 2-hour training produced 'research-quality data' with 'minimal oversight'. This claim implicitly assumes that archaeological feature identification and digitisation are learnable tasks that don't require extensive expertise—a disciplinary assumption about task accessibility. This assumption is field-specific: some disciplines assume novice = lower quality (e.g., taxonomy requires expertise), while others assume tasks are accessible to trained non-experts. Paper treats this as obvious but outsiders might question whether 2 hours suffices for research-quality archaeological work.",

    "implicit_metadata": {
        "basis": "disciplinary_norm",
        "confidence": "medium",
        "assessment_implication": "Readers from fields assuming novice = lower quality may question data credibility. The assumption that archaeological feature mapping is accessible to minimally-trained non-experts is a field-specific norm that may not be shared across disciplines or even within archaeology for all feature types."
    },

    "supports_claim": ["C012"],  # The "capable of research-quality data" claim

    "location": {
        "section": "Discussion",
        "subsection": "4.3",
        "page": 12
    }
}

# ============================================
# Add implicit arguments to extraction
# ============================================

# Extend implicit_arguments array (do not replace - accumulate across sections)
data['implicit_arguments'].extend([
    implicit_argument_type3_quality,
    implicit_argument_type2_capability,
    implicit_argument_type1_comparison,
    implicit_argument_type4_disciplinary
])

# Write updated extraction
with open('extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Implicit arguments extraction complete:")
print(f"   - Type 1 (Logical Implications): 1")
print(f"   - Type 2 (Unstated Assumptions): 1")
print(f"   - Type 3 (Bridging Claims): 1")
print(f"   - Type 4 (Disciplinary Assumptions): 1")
print(f"\n💡 Remember: Systematic 4-type scan required for EACH core claim")
print(f"💡 Types 2-4 often more assessment-critical than Type 1")
