# Verification Procedures: Preventing Evidence Hallucination

## Overview: Why This Is Critical

**The hallucination problem:** When extracting evidence, claims, and implicit arguments, LLMs may fabricate plausible-sounding details rather than faithfully extracting what the paper actually states. This is catastrophic for credibility assessment because:

- **False evidence poisons everything:** Fabricated error rates, invented training methods, or non-existent entities undermine all downstream assessment
- **Cannot assess credibility with fabricated data:** The entire extraction becomes unreliable
- **Erodes trust in the system:** One major hallucination destroys confidence in all extractions

**Example from Sobotkova extraction:**
- **E018 claimed:** "72% of volunteers completed training video before beginning digitization work"
- **Reality:** The word "video" appears ZERO times in the entire paper. Completely fabricated.
- **E010-E015 claimed:** Detailed error breakdowns with specific numbers from Discussion 4.1.2
- **Reality:** Discussion 4.1.2 mentions errors briefly; actual data is in Results 3.5.2 with DIFFERENT numbers

**The solution:** Three-part verification with mandatory sourcing discipline for ALL content.

---

## Critical Distinction: Explicit vs Implicit Content

Before applying verification procedures, understand which type of content you're verifying:

### Explicit Content (Evidence & Claims)
- The content IS explicitly stated in the paper
- Requires `verbatim_quote` field containing the exact text stating this content
- Verification checks: Does the quote exist? Does it say what we claim?

### Implicit Content (Implicit Arguments)
- The content is NOT explicitly stated but IMPLIED by multiple passages
- Requires `trigger_text` array containing passages that together imply the argument
- Verification checks: Do trigger passages exist? Do they reasonably support the inference?

**Never confuse these:** If you're extracting something explicitly stated, use verbatim_quote. If you're inferring something unstated, use trigger_text.

---

## PART 1: Verification for Explicit Content (Evidence & Claims)

Apply these procedures to every evidence item and claim during Pass 3 validation.

### Step 1: Location Verification

**Question:** Does the stated location exist and discuss the relevant topic?

**Procedure:**
1. Navigate to the exact location specified (section, subsection, paragraph)
2. Verify section/subsection titles match what's stated
3. Confirm the paragraph at that location discusses the topic of this evidence/claim

**Decision Tree:**
```
Does section exist? 
  NO → FAIL: location_verified = false
  YES → Does subsection exist (if specified)?
    NO → FAIL: location_verified = false
    YES → Does paragraph number exist in this section?
      NO → FAIL: location_verified = false
      YES → Does this paragraph discuss the relevant topic?
        NO → FAIL: location_verified = false (wrong location cited)
        YES → PASS: location_verified = true
```

**Common Failures:**
- Section number/name incorrect (e.g., "4.1.2" when discussing Results but data is in "3.5.2")
- Paragraph number wrong (e.g., paragraph 3 when quote is actually in paragraph 5)
- Right section, but paragraph discusses different topic entirely

**Example PASS:**
- Evidence: "Total error rate 5.9% (49 errors from 834 features)"
- Location: Section 3.5.2 "Quality Control", paragraph 1
- Check: Section 3.5.2 exists ✓, is about Quality Control ✓, paragraph 1 discusses error rates ✓
- **Result:** location_verified = true

**Example FAIL:**
- Evidence: "Total error rate 2.5% (220 errors among 8,945 points)"
- Location: Discussion 4.1.2, paragraph 2
- Check: Section 4.1.2 exists ✓, but titled "Machine learning versus crowdsourcing" ✗
- Paragraph 2 mentions errors briefly but gives NO specific numbers ✗
- **Result:** location_verified = false

---

### Step 2: Quote Verification

**Question:** Is the verbatim_quote actually present in the stated location?

**Procedure:**
1. Navigate to the verified location (must pass Step 1 first)
2. Search for the EXACT text of verbatim_quote in that location
3. Verify the quote is truly verbatim (not paraphrased, not altered)
4. Confirm quote is in the SPECIFIC paragraph cited (not nearby paragraph)

**Decision Tree:**
```
Can you find exact quote text in stated location?
  NO → FAIL: quote_verified = false
  YES → Is it in the SPECIFIC paragraph cited?
    NO → FAIL: quote_verified = false (quote exists but wrong paragraph)
    YES → Is text exactly verbatim (no paraphrasing)?
      NO → FAIL: quote_verified = false (paraphrased)
      YES → PASS: quote_verified = true
```

**Critical Rules:**
- **Verbatim means VERBATIM:** Not "close enough", not paraphrased, not summarized
- **Exact location matters:** Quote in paragraph 3 when you cite paragraph 2 = FAIL
- **No partial matches:** Must find complete quote, not just fragments

**Example PASS:**
- verbatim_quote: "overall rate of 5.9% exceeded expectations"
- Location: Results 3.5.2, paragraph 1
- Search paragraph 1: Contains exact text "overall rate of 5.9% exceeded expectations" ✓
- **Result:** quote_verified = true

**Example FAIL:**
- verbatim_quote: "volunteers completed training video before fieldwork"
- Location: Discussion 4.2, paragraph 2
- Search paragraph 2: Mentions "volunteers" and "training" but NOT "video" ✗
- No sentence matches this quote ✗
- **Result:** quote_verified = false, FLAG: possible hallucination

**Example FAIL (Paraphrase):**
- verbatim_quote: "error rate was under 6%"
- Evidence text: "error rate under 6%"
- Actual paper text: "errors remained below the 6% threshold"
- Search: Cannot find EXACT quote "error rate was under 6%" ✗
- **Result:** quote_verified = false, NOTE: paraphrased not verbatim

---

### Step 3: Content-Quote Alignment

**Question:** Does the evidence/claim content actually match what the quote says?

**Procedure:**
1. Read the verbatim_quote (must pass Steps 1-2 first)
2. Read the evidence_text or claim_text
3. Compare: Does the extracted content faithfully represent what the quote states?
4. Check: Are numbers, categories, interpretations consistent with quote?

**Decision Tree:**
```
Does evidence/claim content appear in the quote?
  NO → Check: Is it a reasonable inference from quote?
    YES → WARNING: Should this be implicit argument instead?
    NO → FAIL: content_aligned = false
  YES → Are specific numbers/facts in the quote?
    NO (quote doesn't contain these) → FAIL: content_aligned = false
    YES → Is the interpretation faithful to quote meaning?
      NO (overinterpretation/distortion) → FAIL: content_aligned = false
      YES → PASS: content_aligned = true
```

**Red Flags:**
- Evidence contains specific numbers NOT in the quote
- Evidence mentions categories/breakdowns NOT in the quote
- Evidence claims precision quote doesn't support (e.g., "exactly 42" when quote says "about 40")
- Evidence interprets beyond what quote directly states

**Example PASS:**
- verbatim_quote: "57 hours of staff time were required to set up the crowdsourcing system"
- evidence_text: "57 staff hours required for crowdsourcing setup"
- Check: Number 57 in quote? ✓ Activity (setup) in quote? ✓ Metric (hours) in quote? ✓
- Interpretation faithful? ✓ (direct restatement)
- **Result:** content_aligned = true

**Example FAIL (Numbers not in quote):**
- verbatim_quote: "error rate under 6%"
- evidence_text: "Total error rate 2.5% (220 errors among 8,945 points, with 146 spatial errors and 74 attribute errors)"
- Check: Does quote mention 2.5%? ✗ Does quote give error counts? ✗ Does quote give breakdown? ✗
- **Result:** content_aligned = false, FLAG: severe hallucination

**Example FAIL (Categories not in quote):**
- verbatim_quote: "volunteers completed training before beginning work"
- evidence_text: "72% of volunteers completed training video before beginning digitization work"
- Check: Does quote mention 72%? ✗ Does quote mention "video"? ✗
- **Result:** content_aligned = false, FLAG: added details not in quote

**Example PASS (Faithful interpretation):**
- verbatim_quote: "The crowdsourcing approach reduced staff time from 300 hours in 2010 to 57 hours in 2017"
- evidence_text: "Crowdsourcing reduced staff time by 81% compared to 2010 traditional method"
- Check: Quote gives 300 hours (2010) and 57 hours (2017)? ✓
- Calculation: (300-57)/300 = 81% ✓ Interpretation faithful? ✓
- **Result:** content_aligned = true

---

## PART 2: Verification for Implicit Content (Implicit Arguments)

Apply these procedures to every implicit argument during Pass 3 validation.

### Step 1: Trigger Location Verification

**Question:** Do all stated trigger locations exist?

**Procedure:**
1. For EACH location in trigger_locations array:
2. Navigate to that exact location (section, subsection, paragraph)
3. Verify section/subsection exists and paragraph number valid
4. Confirm location relates to the implicit argument topic

**Decision Tree:**
```
For each trigger_location:
  Does section exist?
    NO → FAIL: trigger_locations_verified = false
    YES → Does subsection exist (if specified)?
      NO → FAIL: trigger_locations_verified = false
      YES → Does paragraph exist?
        NO → FAIL: trigger_locations_verified = false
        YES → Does location relate to argument topic?
          NO → FAIL: trigger_locations_verified = false
          YES → Continue to next location

All locations verified? 
  YES → PASS: trigger_locations_verified = true
```

**Critical Rules:**
- **ALL locations must pass:** One invalid location = entire check fails
- **Array indices must match:** trigger_locations[0] corresponds to trigger_text[0]
- **Locations should relate:** If arguing about efficiency, locations should discuss relevant aspects

**Example PASS:**
- Implicit argument: "Volunteer labor multiplies output with low staff overhead"
- trigger_locations: [
    {"section": "3.4", "paragraph": 2},  // output numbers
    {"section": "3.3", "paragraph": 5},  // staff hours
    {"section": "3.5.1", "paragraph": 1} // per-feature cost
  ]
- Check: All three sections exist ✓, paragraphs exist ✓, relate to efficiency ✓
- **Result:** trigger_locations_verified = true

---

### Step 2: Trigger Quote Verification

**Question:** Is each trigger_text passage found in its corresponding location?

**Procedure:**
1. For EACH passage in trigger_text array:
2. Navigate to corresponding location in trigger_locations array
3. Search for EXACT text of that trigger passage
4. Verify passage is verbatim (not paraphrased)

**Decision Tree:**
```
For each trigger_text passage:
  Navigate to corresponding trigger_location
  Search for exact passage text in that location
    Found? 
      NO → FAIL: trigger_quotes_verified = false
      YES → Is it verbatim?
        NO → FAIL: trigger_quotes_verified = false
        YES → Continue to next passage

All passages found?
  YES → PASS: trigger_quotes_verified = true
```

**Common Failures:**
- Passage paraphrased instead of verbatim
- Passage in different paragraph than cited
- Passage fragments from multiple paragraphs combined without noting
- Passage doesn't actually exist (hallucinated)

**Example PASS:**
- trigger_text[0]: "10,827 features were created by volunteers"
- trigger_locations[0]: {"section": "3.4", "paragraph": 2}
- Search section 3.4, paragraph 2: Contains exact text ✓
- **Result:** trigger_quotes_verified = true (if all passages verify)

**Example FAIL:**
- trigger_text[1]: "volunteers worked efficiently with minimal supervision"
- trigger_locations[1]: {"section": "4.1", "paragraph": 3}
- Search section 4.1, paragraph 3: Mentions "volunteers" but not "efficiently" or "minimal supervision" ✗
- **Result:** trigger_quotes_verified = false, NOTE: paraphrased or inferred

---

### Step 3: Inference Reasonableness

**Question:** Do the trigger passages reasonably support the implicit argument?

**Procedure:**
1. Read ALL trigger passages together
2. Read the implicit_text (the argument being made)
3. Read the inference_reasoning (explanation of connection)
4. Evaluate: Would a reasonable person reach this conclusion from these passages?

**Decision Tree:**
```
Read all trigger passages + inference_reasoning
Is implicit argument directly stated in any passage?
  YES → FLAG: Should be explicit claim, not implicit argument
  NO → Do passages together provide basis for argument?
    NO → FAIL: inference_reasonable = false
    YES → Is inference_reasoning clear and logical?
      NO → FAIL: inference_reasonable = false (weak explanation)
      YES → Is leap from passages to argument reasonable?
        NO (too speculative) → FAIL: inference_reasonable = false
        YES → PASS: inference_reasonable = true
```

**Red Flags - Unreasonable Inferences:**
- **Too speculative:** Big logical leap from passages to conclusion
- **Cherry-picking:** Ignores contradictory evidence elsewhere
- **Overconfident:** Treats possibility as certainty
- **Actually stated:** Argument is explicitly stated somewhere (should be claim)
- **Weak connection:** Trigger passages don't really support argument

**Reasonable Inference Standards:**
- **Multiple passages converge:** Several independent mentions pointing same direction
- **Logical connection clear:** inference_reasoning explains the link
- **Modest claim:** Argument is appropriately hedged given evidence
- **Disciplinary norms:** Inference type is standard practice in this field

**Example PASS:**
- implicit_text: "Volunteer crowdsourcing multiplies data collection output with minimal staff overhead"
- trigger_text: [
    "10,827 features created by volunteers",
    "57 hours total staff time for setup and management",
    "marginal cost per feature averaged 4.3 seconds of staff time"
  ]
- inference_reasoning: "Three passages together show: (1) large output (10,827 features), (2) low staff input (57 hours), (3) low per-unit cost (4.3s). Together these imply multiplication effect—volunteers amplify output without proportional staff increase."
- Check: Do passages support this? ✓ (specific numbers for output, input, efficiency)
- Is inference clear? ✓ (explicit logical connection)
- Is it reasonable? ✓ (direct calculation from stated figures)
- **Result:** inference_reasonable = true

**Example FAIL (Too Speculative):**
- implicit_text: "Most volunteers had prior GIS experience"
- trigger_text: ["volunteers completed tasks quickly"]
- inference_reasoning: "Fast completion suggests prior experience"
- Check: Does this follow? ✗ (many explanations for fast completion)
- Too speculative? ✓ (could be simple tasks, good training, etc.)
- **Result:** inference_reasonable = false, NOTE: speculative leap

**Example FAIL (Actually Stated):**
- implicit_text: "System deployed rapidly"
- trigger_text: ["deployed in 3 days from paper maps to live system"]
- Check: Is "rapid" explicitly stated? ✗ BUT "3 days" IS explicitly stated
- Should be explicit claim with this as verbatim_quote? ✓
- **Result:** inference_reasonable = false, ACTION: Reclassify as explicit claim

---

## PART 3: Verification for RDMAP Objects (Research Designs, Methods, Protocols)

Apply these procedures to all research design, method, and protocol objects during Pass 3 validation.

### Understanding RDMAP Explicit vs Implicit Status

**RDMAP items have two distinct sourcing patterns:**

**EXPLICIT RDMAP (status = "explicit")**
- Documented in Methods section with procedural details
- Should have `verbatim_quote` from Methods section
- Verification similar to Evidence & Claims

**IMPLICIT RDMAP (status = "implicit")**  
- NOT documented in Methods section
- Either mentioned but undocumented, OR inferred from Results/Discussion
- Should have `trigger_text` + `trigger_locations` + `inference_reasoning`
- Verification similar to Implicit Arguments

**Critical:** Check the status field first to determine which verification procedure to apply.

---

### Explicit RDMAP Items (status = "explicit")

For RDMAP items documented in the Methods section, follow the same three-step procedure as Evidence & Claims:

#### Step 1: Location Verification

**Question:** Does the stated location exist in Methods section and discuss this RDMAP item?

**Procedure:**
1. Navigate to stated location (should be in Methods or subsections)
2. Verify section/subsection exists
3. Confirm paragraph discusses this design/method/protocol

**Decision Tree:**
```
Is location in Methods section (or subsections)?
  NO → WARNING: Explicit RDMAP should be in Methods
  YES → Does section exist?
    NO → FAIL: location_verified = false
    YES → Does subsection exist (if specified)?
      NO → FAIL: location_verified = false
      YES → Does paragraph exist?
        NO → FAIL: location_verified = false
        YES → Does paragraph discuss this RDMAP item?
          NO → FAIL: location_verified = false
          YES → PASS: location_verified = true
```

**Common Issues:**
- Location in Results/Discussion instead of Methods (should be implicit if not in Methods)
- Wrong subsection within Methods
- Paragraph discusses different method/protocol

**Example PASS:**
- Method: "Pedestrian survey with 50m transects covering 22 sites"
- Location: Methods 2.1 "Survey Strategy", paragraph 2
- Check: Section 2.1 exists ✓, is Methods subsection ✓, paragraph 2 discusses survey approach ✓
- **Result:** location_verified = true

**Example FAIL:**
- Protocol: "GPS coordinates recorded with ±5m accuracy"
- Location: Results 3.2, paragraph 1
- Check: Section 3.2 is Results, not Methods ✗
- **Result:** location_verified = false, NOTE: Should be implicit if not in Methods

---

#### Step 2: Quote Verification

**Question:** Is the verbatim_quote present in the stated Methods location?

**Procedure:**
1. Navigate to verified location
2. Search for EXACT text of verbatim_quote
3. Note: Methods descriptions often span multiple sentences

**Decision Tree:**
```
Can you find exact quote in stated location?
  NO → FAIL: quote_verified = false
  YES → Is quote from Methods section?
    NO → FAIL: quote_verified = false (wrong section)
    YES → Is text verbatim?
      NO → FAIL: quote_verified = false (paraphrased)
      YES → PASS: quote_verified = true
```

**RDMAP-Specific Considerations:**
- Methods descriptions may span multiple sentences (that's OK)
- Quote may reference other parts of methods (that's OK)
- Technical terminology should match exactly

**Example PASS:**
- verbatim_quote: "Survey teams walked 50m wide transects across each site, recording all visible surface artifacts with handheld GPS units"
- Location: Methods 2.1, paragraph 3
- Check: Found exact multi-sentence quote in Methods 2.1, paragraph 3 ✓
- **Result:** quote_verified = true

**Example FAIL:**
- verbatim_quote: "GPS accuracy set to ±5 meters"
- Location: Methods 2.2, paragraph 1
- Search: Mentions "GPS" but NOT "accuracy" or specific values ✗
- **Result:** quote_verified = false, FLAG: Details may be implicit

---

#### Step 3: Content-Quote Alignment

**Question:** Does the RDMAP item description match what the quote actually says?

**Procedure:**
1. Read verbatim_quote
2. Read design_text / method_text / protocol_text
3. Compare: Are the procedural details consistent?
4. Check: Are specifics (numbers, equipment, steps) from the quote?

**Decision Tree:**
```
Does RDMAP description appear in quote?
  NO → FAIL: content_aligned = false
  YES → Are specific details (numbers, equipment, steps) in quote?
    NO → FAIL: content_aligned = false (added details)
    YES → Is interpretation faithful?
      NO → FAIL: content_aligned = false (overinterpretation)
      YES → PASS: content_aligned = true
```

**RDMAP Red Flags:**
- Adding specificity not in quote (e.g., "±5m accuracy" when quote doesn't give precision)
- Naming equipment not mentioned in quote
- Claiming standardization when quote doesn't state it
- Over-interpreting vague method descriptions

**Example PASS:**
- verbatim_quote: "Teams systematically walked 50m transects recording all visible artifacts"
- method_text: "Systematic pedestrian survey using 50m wide transects with total coverage artifact collection"
- Check: "systematic" in quote ✓, "50m transects" in quote ✓, "artifacts" in quote ✓
- Interpretation faithful to quote ✓
- **Result:** content_aligned = true

**Example FAIL (Adding specificity):**
- verbatim_quote: "GPS units used to record artifact locations"
- protocol_text: "GPS coordinates recorded with ±5m horizontal accuracy using Garmin eTrex units"
- Check: Quote mentions GPS ✓, but doesn't give accuracy ✗, doesn't name model ✗
- **Result:** content_aligned = false, FLAG: Added details beyond quote

**Example FAIL (Over-interpreting vague description):**
- verbatim_quote: "artifacts were carefully recorded"
- method_text: "Standardized recording protocol implemented with systematic quality checks"
- Check: Quote says "carefully" but doesn't claim "standardized protocol" ✗
- **Result:** content_aligned = false, FLAG: Overinterpretation

---

### Implicit RDMAP Items (status = "implicit")

For RDMAP items NOT documented in Methods, follow the same three-step procedure as Implicit Arguments:

#### Step 1: Trigger Location Verification

**Question:** Do all stated trigger locations exist and relate to this RDMAP item?

**Procedure:**
1. For EACH location in trigger_locations array
2. Verify section/subsection/paragraph exists
3. Confirm location relates to this RDMAP topic
4. Note: Triggers may be in Results, Discussion, or Introduction (not Methods)

**Decision Tree:**
```
For each trigger_location:
  Does section exist?
    NO → FAIL: trigger_locations_verified = false
    YES → Does paragraph exist?
      NO → FAIL: trigger_locations_verified = false  
      YES → Does location relate to RDMAP item?
        NO → FAIL: trigger_locations_verified = false
        YES → Continue to next location

All locations verified?
  YES → PASS: trigger_locations_verified = true
```

**RDMAP Implicit Triggers Often Appear In:**
- Results: Descriptions of output implying procedures used
- Discussion: Mentions of approach without details
- Introduction: Mentions of planned methods without documentation
- Captions: Figure/table descriptions revealing procedures

**Example PASS (Implicit Protocol):**
- Protocol: "Spatial coordinates captured with sub-10m accuracy"
- Basis: "inferred_from_results" (precision mentioned but procedure not)
- trigger_locations: [
    {"section": "3.2", "paragraph": 1},  // Results mentions accuracy
    {"section": "Figure 2", "paragraph": "caption"}  // Caption shows GPS data
  ]
- Check: Section 3.2 exists ✓, Figure 2 caption exists ✓, both relate to coordinates ✓
- **Result:** trigger_locations_verified = true

---

#### Step 2: Trigger Quote Verification

**Question:** Are all trigger passages found in their stated locations?

**Procedure:**
1. For EACH passage in trigger_text array
2. Navigate to corresponding trigger_locations[i]
3. Search for exact text
4. Verify verbatim match

**Decision Tree:**
```
For each (trigger_text[i], trigger_locations[i]) pair:
  Can you find exact trigger text in stated location?
    NO → FAIL: trigger_quotes_verified = false
    YES → Is text verbatim (not paraphrased)?
      NO → FAIL: trigger_quotes_verified = false
      YES → Continue to next trigger

All triggers verified?
  YES → PASS: trigger_quotes_verified = true
```

**RDMAP Trigger Considerations:**
- Triggers may be fragments or partial sentences (that's OK)
- Triggers should IMPLY procedure, not STATE it (if stated = should be explicit)
- Multiple triggers may be needed to establish implicit item

**Example PASS:**
- trigger_text[0]: "accuracy of ±5m or better"
- trigger_text[1]: "GPS coordinates for each artifact"
- trigger_locations[0]: Results 3.2, paragraph 1
- trigger_locations[1]: Methods 2.3, paragraph 2
- Check: First passage found in Results 3.2 ✓, second found in Methods 2.3 ✓
- **Result:** trigger_quotes_verified = true

**Example FAIL:**
- trigger_text: "GPS calibrated daily"
- trigger_locations: Methods 2.3, paragraph 1
- Check: Methods 2.3 mentions "GPS" but not "calibrated" or "daily" ✗
- **Result:** trigger_quotes_verified = false, FLAG: Invented detail

---

#### Step 3: Inference Reasonableness

**Question:** Do the trigger passages reasonably support inferring this RDMAP item?

**Procedure:**
1. Read all trigger passages together
2. Read the implicit RDMAP item text
3. Read inference_reasoning
4. Evaluate: Does inference follow reasonably from triggers?
5. Check: Is RDMAP item truly implicit (not stated explicitly elsewhere)?

**Decision Tree:**
```
Is RDMAP item explicitly stated in Methods?
  YES → FAIL: Should be explicit RDMAP, not implicit
  NO → Do trigger passages together provide basis for inference?
    NO → FAIL: Weak inference
    YES → Is inference explained in inference_reasoning?
      NO → FAIL: Missing explanation
      YES → Is reconstruction_confidence appropriate?
        NO → FAIL: Over/under confidence
        YES → PASS: inference_reasonable = true
```

**Two Types of Implicit RDMAP Basis:**

**Type 1: mentioned_undocumented**
- Procedure/tool/approach NAMED but details not provided
- Example: "GPS units" mentioned but no accuracy/model/protocol
- Triggers should show WHERE mentioned
- Inference: Reasonable to infer standard commercial GPS procedures

**Type 2: inferred_from_results**
- Procedure NEVER mentioned but implied by Results/outputs
- Example: Results show 0.5m precision but Methods silent on how achieved  
- Triggers should show WHAT results imply procedure
- Inference: Must be conservative (high uncertainty)

**RDMAP Inference Red Flags:**
- Inferring specific equipment/procedures from vague outputs
- Assuming standardization not mentioned
- Inventing quality control procedures
- Over-confident reconstruction from minimal triggers

**Example PASS (mentioned_undocumented):**
- Protocol: "Standard GPS data collection procedures"
- trigger_text: ["handheld GPS units were used", "coordinates recorded for each point"]
- inference_reasoning: "GPS units and coordinate recording mentioned in Methods but specific protocols (accuracy requirements, calibration, error handling) not documented. Standard consumer GPS procedures can be inferred."
- implicit_metadata.basis: "mentioned_undocumented"
- implicit_metadata.reconstruction_confidence: "medium"
- Check: GPS mentioned ✓, procedures not detailed ✓, inference reasonable ✓
- **Result:** inference_reasonable = true

**Example PASS (inferred_from_results):**
- Protocol: "Sub-meter GPS accuracy achieved through differential correction or high-precision receivers"
- trigger_text: ["coordinate accuracy of ±0.5m reported", "precision suitable for feature-level analysis"]
- inference_reasoning: "Results report 0.5m accuracy but Methods doesn't explain how achieved. This precision exceeds standard consumer GPS (±5-10m), requiring either differential correction or survey-grade equipment. Cannot determine which."
- implicit_metadata.basis: "inferred_from_results"
- implicit_metadata.reconstruction_confidence: "low"
- Check: Precision implies procedure ✓, uncertainty acknowledged ✓, conservative ✓
- **Result:** inference_reasonable = true

**Example FAIL (Over-confident inference):**
- Protocol: "GPS calibrated daily using known control points"
- trigger_text: ["GPS units achieved high accuracy"]
- inference_reasoning: "High accuracy mentioned, therefore calibration must have been performed"
- implicit_metadata.reconstruction_confidence: "high"
- Check: "High accuracy" doesn't imply specific procedure ✗, many paths to accuracy ✗, confidence too high ✗
- **Result:** inference_reasonable = false, FLAG: Speculative leap

**Example FAIL (Should be explicit):**
- Implicit protocol: "50m wide transects"
- trigger_text: ["Teams walked 50m wide transects"]
- Check: This IS explicitly stated ✗, should be explicit RDMAP not implicit ✗
- **Result:** inference_reasonable = false, ACTION: Reclassify as explicit

---

### RDMAP-Specific Red Flags

Watch for these common RDMAP verification issues:

**For Explicit RDMAP:**
- ❌ Quote in Results/Discussion instead of Methods (should be implicit)
- ❌ Adding equipment models/specifications not in quote
- ❌ Claiming standardization when Methods doesn't state it
- ❌ Adding precision/accuracy values not in quote
- ❌ Inventing quality control procedures

**For Implicit RDMAP:**
- ❌ Actually stated in Methods (should be explicit)
- ❌ Inferring specific procedures from vague mentions
- ❌ High reconstruction confidence with weak triggers
- ❌ Inventing calibration/validation procedures
- ❌ Assuming "standard" procedures without basis

**Transparency Gap Flags:**
- Methods mentions approach but gives no procedural details
- Equipment named but specifications not provided
- Protocol claimed but steps not documented
- Quality control mentioned but procedures not described

---

### RDMAP Implicit Metadata Requirements

All implicit RDMAP items must have complete `implicit_metadata`:

**basis:**
- "mentioned_undocumented" - Tool/approach named but not detailed
- "inferred_from_results" - Never mentioned, inferred from output/results

**transparency_gap:**
- What specific information is missing from Methods?
- "Methods mentions GPS but doesn't document accuracy requirements, calibration procedures, or error handling"
- "Precision of results suggests specialized equipment but Methods silent on instruments used"

**assessability_impact:**
- How does this gap affect credibility assessment?
- "Cannot assess calibration practices or equipment quality without documentation"
- "Unable to evaluate whether accuracy claims match procedural capabilities"

**reconstruction_confidence:**
- "high" - Strong basis for inferring procedure, narrow range of possibilities
- "medium" - Reasonable inference but some uncertainty
- "low" - Weak basis, multiple possible procedures, high uncertainty

**Example Complete Implicit Metadata:**
```json
{
  "basis": "mentioned_undocumented",
  "transparency_gap": "Methods section mentions 'handheld GPS units' and 'coordinate recording' but provides no details on: accuracy requirements, equipment models, calibration procedures, differential correction use, or quality control checks",
  "assessability_impact": "Cannot assess GPS data quality, equipment capabilities, or accuracy claims without documented procedures. Cannot evaluate whether reported precision (±5m) matches equipment capabilities.",
  "reconstruction_confidence": "medium"
}
```

---

### Worked Examples

#### Example 1: Explicit Method - PASS ✓

**Method M003:**
```json
{
  "method_id": "M003",
  "method_text": "Systematic pedestrian survey using 50m wide transects with complete surface coverage",
  "method_type": "data_collection",
  "method_status": "explicit",
  "location": {"section": "2.1", "subsection": "Survey Strategy", "paragraph": 2},
  "verbatim_quote": "Teams conducted systematic pedestrian survey walking 50m wide transects to ensure complete surface coverage of each site",
  "source_verification": {}
}
```

**Verification:**
- **Step 1:** Section 2.1 exists ✓, is Methods subsection ✓, paragraph 2 discusses survey ✓
- **Step 2:** Found exact quote in Methods 2.1, paragraph 2 ✓
- **Step 3:** "systematic" in quote ✓, "50m transects" in quote ✓, "complete coverage" in quote ✓
- **Result:** ALL PASS ✓

**source_verification:**
```json
{
  "location_verified": true,
  "quote_verified": true,
  "content_aligned": true,
  "verification_notes": "Complete match - survey strategy fully documented in Methods",
  "verified_by": "validator"
}
```

---

#### Example 2: Explicit Protocol - FAIL (Added Details)

**Protocol P012:**
```json
{
  "protocol_id": "P012",
  "protocol_text": "GPS coordinates recorded with ±5m horizontal accuracy using Garmin eTrex 20x units with WAAS correction",
  "protocol_status": "explicit",
  "location": {"section": "2.3", "paragraph": 1},
  "verbatim_quote": "GPS units used to record coordinates for all artifacts",
  "source_verification": {}
}
```

**Verification:**
- **Step 1:** Section 2.3 exists ✓, paragraph discusses GPS ✓
- **Step 2:** Found quote "GPS units used to record coordinates" ✓
- **Step 3:** Quote mentions GPS ✓, but doesn't give accuracy ✗, doesn't name model ✗, doesn't mention WAAS ✗
- **Result:** FAIL - content_aligned = false

**Issue:** Protocol text adds specific details (±5m, model name, WAAS) not present in verbatim_quote

**Action:** If these details appear elsewhere as implicit information, reclassify as implicit protocol with proper trigger_text

**source_verification:**
```json
{
  "location_verified": true,
  "quote_verified": true,
  "content_aligned": false,
  "verification_notes": "FAIL: Protocol adds specificity (accuracy, model, WAAS) not in quote. Quote only states 'GPS units used to record coordinates'. Added details are invention unless found elsewhere as implicit.",
  "verified_by": "validator"
}
```

---

#### Example 3: Implicit Protocol - PASS ✓

**Protocol P015:**
```json
{
  "protocol_id": "P015",
  "protocol_text": "Standard consumer GPS procedures with estimated ±5-10m horizontal accuracy typical of handheld units without differential correction",
  "protocol_status": "implicit",
  "trigger_text": [
    "handheld GPS units were used",
    "Spatial accuracy adequate for site-level analysis"
  ],
  "trigger_locations": [
    {"section": "2.3", "paragraph": 1},
    {"section": "4.1", "paragraph": 3}
  ],
  "inference_reasoning": "Methods mentions handheld GPS but provides no accuracy specifications, calibration procedures, or equipment models. Discussion states accuracy 'adequate for site-level analysis' suggesting general-purpose consumer GPS. Standard consumer handheld GPS (without differential correction) provides ±5-10m accuracy, consistent with 'site-level' spatial resolution.",
  "implicit_metadata": {
    "basis": "mentioned_undocumented",
    "transparency_gap": "GPS units mentioned but no documentation of: equipment models, accuracy requirements, calibration procedures, differential correction use, or quality control checks",
    "assessability_impact": "Cannot verify equipment specifications or assess data quality procedures. Cannot determine if accuracy claims match equipment capabilities.",
    "reconstruction_confidence": "medium"
  },
  "source_verification": {}
}
```

**Verification:**
- **Step 1:** Locations verified: Section 2.3 exists ✓, Section 4.1 exists ✓, both discuss GPS ✓
- **Step 2:** 
  - Trigger[0] "handheld GPS units" found in Methods 2.3 ✓
  - Trigger[1] "adequate for site-level analysis" found in Discussion 4.1 ✓
- **Step 3:** 
  - GPS mentioned but not detailed ✓
  - Inference reasonable (standard GPS accuracy) ✓
  - Confidence appropriate (medium - reasonable inference but uncertainty) ✓
  - Not stated explicitly anywhere ✓
- **Result:** ALL PASS ✓

**source_verification:**
```json
{
  "location_verified": true,
  "quote_verified": true,
  "content_aligned": true,
  "verification_notes": "PASS: Implicit protocol reasonably inferred. GPS mentioned without details, standard accuracy inferred conservatively. Reconstruction confidence appropriately medium given limited documentation.",
  "verified_by": "validator"
}
```

---

#### Example 4: Implicit Method - FAIL (Weak Inference)

**Method M008:**
```json
{
  "method_id": "M008",
  "method_text": "Daily calibration of GPS equipment using known survey control points",
  "method_status": "implicit",
  "trigger_text": [
    "GPS units achieved high spatial accuracy"
  ],
  "trigger_locations": [
    {"section": "3.2", "paragraph": 1}
  ],
  "inference_reasoning": "Results mention high accuracy, therefore daily calibration must have been performed",
  "implicit_metadata": {
    "basis": "inferred_from_results",
    "transparency_gap": "No calibration procedures documented",
    "assessability_impact": "Cannot assess quality control practices",
    "reconstruction_confidence": "high"
  },
  "source_verification": {}
}
```

**Verification:**
- **Step 1:** Section 3.2 exists ✓, discusses accuracy ✓
- **Step 2:** Trigger found "high spatial accuracy" ✓
- **Step 3:** 
  - "High accuracy" mentioned ✓
  - But: Many paths to accuracy (equipment quality, differential correction, post-processing) ✗
  - Inference: Assuming specific procedure (daily calibration) not justified ✗
  - Confidence: "high" inappropriate for speculative inference ✗
- **Result:** FAIL - inference_reasonable = false

**Issue:** Single trigger "high accuracy" doesn't imply specific calibration procedure. Multiple pathways to accuracy. Reconstruction confidence too high for weak evidence.

**Action:** DELETE this implicit method - inference too speculative

**source_verification:**
```json
{
  "location_verified": true,
  "quote_verified": true,
  "content_aligned": false,
  "verification_notes": "FAIL: Inference unreasonable. Single mention of 'high accuracy' doesn't imply daily calibration procedures. Many alternative explanations (equipment quality, differential correction, post-processing). Reconstruction confidence 'high' inappropriate for speculative leap. DELETE.",
  "verified_by": "validator"
}
```

---

## PART 4: Worked Examples

### Example 1: Evidence Verification - PASS ✓

**Evidence E022:**
```json
{
  "evidence_id": "E022",
  "evidence_text": "Crowdsourcing reduced staff time by 81% compared to 2010 traditional method (300 hours → 57 hours)",
  "location": {"section": "3.3", "paragraph": 5},
  "verbatim_quote": "The crowdsourcing approach required 57 hours of staff time compared to 300 hours for the traditional 2010 desktop GIS approach"
}
```

**Verification:**
- **Step 1 - Location:** Section 3.3 exists ✓, paragraph 5 exists ✓, discusses staff time comparison ✓
  - **Result:** location_verified = true ✓
  
- **Step 2 - Quote:** Navigate to 3.3 para 5, search for quote ✓, exact text found ✓, verbatim ✓
  - **Result:** quote_verified = true ✓
  
- **Step 3 - Content:** Quote states 57 hours vs 300 hours ✓, calculation (300-57)/300 = 81% ✓, interpretation faithful ✓
  - **Result:** content_aligned = true ✓

**Verification Status:** ✅ PASS - All three checks pass

---

### Example 2: Evidence Verification - FAIL (Wrong Location) ✗

**Evidence E010 (from Sobotkova extraction):**
```json
{
  "evidence_id": "E010",
  "evidence_text": "Random sample of 4 maps revealed total error rate of 2.5% (220 errors among 8,945 points, with 146 spatial errors and 74 attribute errors)",
  "location": {"section": "4.1.2", "paragraph": 2},
  "verbatim_quote": "error rate under 6%"
}
```

**Verification:**
- **Step 1 - Location:** Section 4.1.2 exists ✓, titled "Machine learning versus crowdsourcing" ⚠️, paragraph 2 mentions errors BRIEFLY ⚠️
  - Paragraph 2 does NOT contain detailed error data ✗
  - **Result:** location_verified = false ✗
  
- **Step 2 - Quote:** Search 4.1.2 para 2 for "error rate under 6%" ✗ (phrase not found exactly)
  - **Result:** quote_verified = false ✗
  
- **Step 3 - Content:** Evidence claims 2.5%, 220 errors, breakdown—NONE in quote ✗
  - Quote only says "under 6%", no specific numbers ✗
  - **Result:** content_aligned = false ✗

**Verification Status:** ❌ FAIL - All three checks fail
**Action:** DELETE or FLAG for manual review
**Note:** Actual data is in Results 3.5.2 with DIFFERENT numbers (5.9%, 49 errors, different breakdown)

---

### Example 3: Evidence Verification - FAIL (Quote Not Found) ✗

**Evidence E018 (from Sobotkova extraction):**
```json
{
  "evidence_id": "E018",
  "evidence_text": "72% of volunteers completed training video before beginning digitization work",
  "location": {"section": "4.2", "paragraph": 2},
  "verbatim_quote": "volunteers completed training video before beginning work"
}
```

**Verification:**
- **Step 1 - Location:** Section 4.2 exists ✓, paragraph 2 discusses recruitment ⚠️
  - **Result:** location_verified = true (marginal)
  
- **Step 2 - Quote:** Search for "volunteers completed training video before beginning work"
  - Word "video" appears ZERO times in entire paper ✗
  - No matching sentence found ✗
  - **Result:** quote_verified = false ✗
  
- **Step 3 - Content:** Evidence mentions "72%" not in quote ✗, mentions "video" not in paper ✗
  - **Result:** content_aligned = false ✗

**Verification Status:** ❌ FAIL - Complete fabrication
**Action:** DELETE immediately
**Red Flag:** ⚠️ HIGH - invented entity (training video) that doesn't exist

---

### Example 4: Evidence Verification - FAIL (Content Misalignment) ✗

**Evidence E999:**
```json
{
  "evidence_id": "E999",
  "evidence_text": "Survey achieved 87% response rate with 234 completed responses",
  "location": {"section": "3.2", "paragraph": 3},
  "verbatim_quote": "We received approximately 230 responses to our survey instrument"
}
```

**Verification:**
- **Step 1 - Location:** Section 3.2 exists ✓, paragraph 3 discusses survey ✓
  - **Result:** location_verified = true ✓
  
- **Step 2 - Quote:** Exact text "We received approximately 230 responses to our survey instrument" found ✓
  - **Result:** quote_verified = true ✓
  
- **Step 3 - Content:** 
  - Quote says "approximately 230" but evidence claims exact "234" ✗
  - Quote says nothing about "87% response rate" ✗
  - **Result:** content_aligned = false ✗

**Verification Status:** ❌ FAIL - Adding precision and data not in quote
**Action:** Flag for correction - extract only what quote states
**Correct extraction:** "Approximately 230 survey responses received" (no response rate, no exact count)

---

### Example 5: Implicit Argument Verification - PASS ✓

**Implicit Argument IA002:**
```json
{
  "implicit_id": "IA002",
  "implicit_text": "Volunteer crowdsourcing multiplies data collection output with minimal staff overhead",
  "trigger_text": [
    "volunteers created 10,827 features across the 4 survey maps",
    "total staff time investment was 57 hours for setup and management",
    "marginal cost per feature averaged 4.3 seconds of staff time"
  ],
  "trigger_locations": [
    {"section": "3.4", "paragraph": 2},
    {"section": "3.3", "paragraph": 5},
    {"section": "3.5.1", "paragraph": 1}
  ],
  "inference_reasoning": "Three passages together demonstrate multiplication effect: (1) Large output (10,827 features), (2) Low total staff input (57 hours), (3) Low per-unit cost (4.3s per feature). These figures together imply volunteers amplify output without proportional staff overhead—classic multiplication dynamic not explicitly stated but evident from numbers."
}
```

**Verification:**
- **Step 1 - Trigger Locations:** All three sections exist ✓, paragraphs exist ✓, all discuss relevant metrics ✓
  - **Result:** trigger_locations_verified = true ✓
  
- **Step 2 - Trigger Quotes:** 
  - Passage 1 found in 3.4 para 2 ✓
  - Passage 2 found in 3.3 para 5 ✓
  - Passage 3 found in 3.5.1 para 1 ✓
  - **Result:** trigger_quotes_verified = true ✓
  
- **Step 3 - Inference:**
  - Is "multiplication effect" stated explicitly anywhere? ✗ (genuinely implicit)
  - Do passages provide basis? ✓ (concrete numbers for output, input, efficiency)
  - Is reasoning clear? ✓ (explains logical connection)
  - Is inference reasonable? ✓ (direct calculation from stated data)
  - **Result:** inference_reasonable = true ✓

**Verification Status:** ✅ PASS - All three checks pass

---

### Example 6: Implicit Argument Verification - FAIL (Weak Inference) ✗

**Implicit Argument IA999:**
```json
{
  "implicit_id": "IA999",
  "implicit_text": "Most volunteers had prior GIS experience",
  "trigger_text": [
    "volunteers completed digitization tasks rapidly"
  ],
  "trigger_locations": [
    {"section": "3.4", "paragraph": 5}
  ],
  "inference_reasoning": "Rapid task completion suggests volunteers already had GIS skills"
}
```

**Verification:**
- **Step 1 - Trigger Locations:** Section 3.4 exists ✓, paragraph 5 exists ✓
  - **Result:** trigger_locations_verified = true ✓
  
- **Step 2 - Trigger Quotes:** Passage found in 3.4 para 5 ✓
  - **Result:** trigger_quotes_verified = true ✓
  
- **Step 3 - Inference:**
  - Is inference stated explicitly? ✗ (genuinely implicit)
  - Does passage provide basis? ⚠️ (only one weak indicator)
  - Is reasoning clear? ✓ (logical connection explained)
  - Is inference reasonable? ✗ Many alternative explanations:
    - Tasks might be simple (doesn't require experience)
    - Training might be effective
    - Interface might be intuitive
    - Sample might be small/unrepresentative
  - Too speculative—single observation, many explanations ✗
  - **Result:** inference_reasonable = false ✗

**Verification Status:** ❌ FAIL - Inference too speculative
**Action:** Delete or revise to more modest claim with appropriate hedging

---

## PART 5: Red Flags for Hallucination

Watch for these warning signs during extraction and verification:

### During Extraction

**🚩 RED FLAG:** You remember reading something but can't find the exact quote
- **Action:** Search thoroughly; if not found, do NOT extract

**🚩 RED FLAG:** Section mentions topic generally but lacks specific details
- **Example:** Discussion says "error rates were acceptable" but gives no numbers
- **Action:** Extract the general statement, NOT invented details

**🚩 RED FLAG:** You're inferring numbers/categories not explicitly stated
- **Example:** Paper says "most volunteers" → inventing "72%"
- **Action:** Only extract exact language used; if inferring, make it implicit argument

**🚩 RED FLAG:** Quote is paraphrased rather than verbatim
- **Action:** Find the actual verbatim text or flag as paraphrase

**🚩 RED FLAG:** Evidence seems obvious/expected but isn't in the text
- **Action:** Obvious ≠ stated; extract only what's written

**🚩 RED FLAG:** Location mentions topic X but details are in different section
- **Example:** Discussion mentions errors, Results has error data
- **Action:** Extract from Results where details actually are, cite correct location

### During Verification

**🚩 RED FLAG:** Location verification fails but quote verification passes
- **Likely:** Wrong location cited; quote is elsewhere
- **Action:** Find correct location or delete

**🚩 RED FLAG:** All three verification checks fail
- **Likely:** Complete fabrication
- **Action:** Delete immediately, investigate extraction quality

**🚩 RED FLAG:** Content contains details not in quote
- **Likely:** Invention or inference beyond quote
- **Action:** Revise to match quote exactly or reclassify

**🚩 RED FLAG:** Verbatim quote looks paraphrased
- **Signs:** Slightly different wording, synonyms used, restructured sentence
- **Action:** Find actual verbatim text

---

## PART 6: Edge Cases and Troubleshooting

### Edge Case 1: Discussion Mentions Topic Without Details

**Scenario:** Discussion 4.1 says "error rates were low" but gives no specific data. Results 3.5.2 contains detailed error analysis.

**Correct Approach:**
- ✓ Extract from Results 3.5.2 where details actually are
- ✗ Do NOT invent details and attribute to Discussion
- ✓ If needed, extract from Discussion: "Error rates characterized as low" (what's actually stated)

**Verification:**
- Location: Cite Results 3.5.2 (where detailed data is)
- Quote: Use actual numbers from Results
- Content: Match the detailed data from Results

---

### Edge Case 2: Multiple Sections Discuss Same Topic

**Scenario:** Methods 2.3 describes procedure briefly. Discussion 4.2 elaborates on same procedure with additional context.

**Correct Approach:**
- Extract SEPARATE items from each section
- Note in extraction_notes: "Additional detail in Discussion 4.2"
- Use related_evidence to link the items
- Each extraction cites its own location and quote

**Verification:**
- Each item verified independently
- Quotes must match their cited locations
- Content must align with quote from that specific section

---

### Edge Case 3: Paraphrased vs Verbatim Quotes

**Scenario:** Paper says "errors remained below the 6% threshold" but extractor writes "error rate under 6%"

**Problem:** This is paraphrase, not verbatim

**Correct Approach:**
- verbatim_quote must be EXACT: "errors remained below the 6% threshold"
- evidence_text can summarize: "Error rate below 6%"
- But quote must be word-for-word from paper

**Verification:**
- Quote verification will FAIL if not exact
- Fix: Update verbatim_quote to actual text from paper

---

### Edge Case 4: Implicit Argument vs Explicit Claim Boundary

**Scenario:** Paper states "3 days from paper maps to live system" but doesn't use word "rapid"

**Question:** Is "rapid deployment" implicit or explicit?

**Decision Tree:**
```
Does paper use the word "rapid" or synonym?
  YES → Explicit claim (use that text as verbatim_quote)
  NO → Is "rapid" a reasonable characterization of "3 days"?
    Arguable → Could be either; prefer explicit
    Clear → Implicit argument (use "3 days" as trigger_text)
```

**Recommended:** When in doubt, extract explicitly
- Explicit claim: "System deployed in 3 days from paper maps to live system"
- verbatim_quote: "3 days from paper maps to live system"
- Let assessor decide if 3 days counts as "rapid"

---

### Edge Case 5: Implicit Argument Trigger from Multiple Scattered Passages

**Scenario:** Efficiency argument requires combining information from Introduction, Methods, Results, and Discussion

**Correct Approach:**
- trigger_text: Array with ALL relevant passages (can be 5-10 passages)
- trigger_locations: Corresponding array with all locations
- inference_reasoning: Explain how all passages together support argument

**Verification:**
- Each trigger location must verify independently
- Each trigger passage must be found in its location
- Inference reasoning must explain connections

**Example:**
```json
{
  "trigger_text": [
    "passage from Introduction about goals",
    "passage from Methods about approach",
    "passage from Results about output",
    "passage from Results about staff time",
    "passage from Discussion about implications"
  ],
  "trigger_locations": [
    {"section": "1", "paragraph": 3},
    {"section": "2.1", "paragraph": 2},
    {"section": "3.4", "paragraph": 1},
    {"section": "3.3", "paragraph": 5},
    {"section": "4.3", "paragraph": 2}
  ],
  "inference_reasoning": "Introduction establishes efficiency goal, Methods describes approach, Results quantify output (10,827 features) and input (57 hours), Discussion notes this achieves goal. Together these passages imply [implicit argument] though never stated explicitly."
}
```

---

## PART 7: Quality Metrics and Statistical Checks

After completing verification for all items, calculate quality metrics:

### Per-Item Metrics

For each evidence/claim item, calculate:
```
verification_pass_rate = items_passing_all_three_checks / total_items
location_failure_rate = items_failing_location_check / total_items  
quote_failure_rate = items_failing_quote_check / total_items
content_failure_rate = items_failing_content_check / total_items
```

### Aggregate Metrics

```
overall_pass_rate = (evidence_passing + claims_passing) / (total_evidence + total_claims)

hallucination_indicators:
- items_failing_all_checks (likely complete fabrication)
- items_failing_quote_check (likely wrong location or invented)
- items_failing_content_check (likely inference beyond source)
```

### Quality Thresholds

**Target metrics:**
- `overall_pass_rate` > 95% (acceptable quality)
- `items_failing_all_checks` = 0 (no complete fabrications)
- `location_failure_rate` < 5% (acceptable citation errors)

**Red flags triggering review:**
- `overall_pass_rate` < 90% → Systemic extraction quality issue
- `items_failing_all_checks` > 5% → Likely hallucination problem
- `quote_failure_rate` > 10% → Location citation issues

### Per-Section Metrics

Calculate pass rates by section:
```
results_section_pass_rate = items_from_results_passing / items_from_results
discussion_section_pass_rate = items_from_discussion_passing / items_from_discussion
```

**Expected pattern:** Results should have higher pass rate than Discussion (Discussion more likely to mention without details)

---

## PART 8: Failure Handling Decision Tree

When verification fails, follow this decision tree:

```
Item fails verification
  ↓
ALL three checks fail?
  YES → DELETE (likely complete fabrication)
  NO → Continue
    ↓
Location fails only?
  YES → SEARCH for correct location
    Found? → UPDATE location, re-verify
    Not found? → DELETE
  NO → Continue
    ↓
Quote fails only?
  YES → SEARCH for correct quote
    Found? → UPDATE quote, re-verify
    Not found? → DELETE (fabricated)
  NO → Continue
    ↓
Content fails only?
  YES → REVISE content to match quote exactly
    Can fix? → UPDATE content, re-verify
    Cannot fix? → DELETE
```

### When to DELETE vs FLAG for Manual Review

**DELETE immediately if:**
- All three verification checks fail
- Quote not found anywhere in paper
- Evidence contains invented entity (e.g., "training video" that doesn't exist)
- Clear hallucination with no basis in paper

**FLAG for manual review if:**
- Location wrong but quote exists elsewhere (fixable)
- Quote paraphrased but correct location and content (fixable)
- Content slightly misaligned with quote (fixable)
- Ambiguous whether implicit vs explicit

**NEVER retain if:**
- Cannot find verbatim quote in paper
- Content contains details not in any quote
- Clear fabrication

---

## PART 9: Verification Workflow Summary

### Pass 3 Verification Checklist

For EACH evidence item and claim:

□ **Step 1:** Navigate to stated location
  - □ Section exists?
  - □ Subsection exists (if specified)?
  - □ Paragraph exists?
  - □ Paragraph discusses relevant topic?
  - → Populate `location_verified` (true/false)

□ **Step 2:** Search for verbatim_quote
  - □ Exact text found in stated location?
  - □ Text is verbatim (not paraphrased)?
  - □ In correct paragraph?
  - → Populate `quote_verified` (true/false)

□ **Step 3:** Compare content to quote
  - □ Specific numbers/facts in quote?
  - □ Categories/terms in quote?
  - □ Interpretation faithful to quote?
  - → Populate `content_aligned` (true/false)

□ **Step 4:** Populate verification_notes
  - Explain any failures
  - Note any concerns

□ **Step 5:** Set verified_by = "validator"

□ **Step 6:** If any check failed, follow failure handling decision tree

---

For EACH implicit argument:

□ **Step 1:** Verify all trigger locations
  - □ Each section/subsection exists?
  - □ Each paragraph exists?
  - □ Each location relates to argument?
  - → Populate `trigger_locations_verified` (true/false)

□ **Step 2:** Verify all trigger quotes
  - □ Each passage found in corresponding location?
  - □ Each passage verbatim?
  - → Populate `trigger_quotes_verified` (true/false)

□ **Step 3:** Evaluate inference
  - □ Argument explicitly stated anywhere? (if yes → reclassify)
  - □ Passages provide basis?
  - □ Reasoning clear?
  - □ Inference reasonable (not too speculative)?
  - → Populate `inference_reasonable` (true/false)

□ **Step 4:** Populate verification_notes
□ **Step 5:** Set verified_by = "validator"
□ **Step 6:** If any check failed, follow failure handling

---

For EACH explicit RDMAP item (research design, method, or protocol with status = "explicit"):

□ **Step 1:** Navigate to stated location
  - □ Location in Methods section (or subsections)?
  - □ Section exists?
  - □ Subsection exists (if specified)?
  - □ Paragraph exists?
  - □ Paragraph discusses this RDMAP item?
  - → Populate `location_verified` (true/false)

□ **Step 2:** Search for verbatim_quote
  - □ Exact text found in Methods location?
  - □ Text is verbatim (not paraphrased)?
  - □ In correct paragraph?
  - → Populate `quote_verified` (true/false)

□ **Step 3:** Compare RDMAP text to quote
  - □ Procedural details in quote?
  - □ Equipment/tools/steps match quote?
  - □ No added specificity beyond quote?
  - → Populate `content_aligned` (true/false)

□ **Step 4:** Populate verification_notes
□ **Step 5:** Set verified_by = "validator"
□ **Step 6:** If any check failed, follow failure handling

---

For EACH implicit RDMAP item (with status = "implicit"):

□ **Step 1:** Verify all trigger locations
  - □ Each section/subsection exists?
  - □ Each paragraph exists?
  - □ Each location relates to RDMAP item?
  - → Populate `trigger_locations_verified` (true/false)

□ **Step 2:** Verify all trigger quotes
  - □ Each passage found in corresponding location?
  - □ Each passage verbatim?
  - → Populate `trigger_quotes_verified` (true/false)

□ **Step 3:** Evaluate inference
  - □ RDMAP explicitly documented in Methods? (if yes → reclassify as explicit)
  - □ Passages provide basis for inference?
  - □ inference_reasoning clear?
  - □ Inference reasonable (not speculative)?
  - □ implicit_metadata complete (basis, transparency_gap, etc.)?
  - □ reconstruction_confidence appropriate?
  - → Populate `inference_reasonable` (true/false)

□ **Step 4:** Populate verification_notes
□ **Step 5:** Set verified_by = "validator"
□ **Step 6:** If any check failed, follow failure handling

---

## Critical Reminders

1. **Verbatim means VERBATIM** - not "close enough", not paraphrased

2. **Location must be EXACT** - right section, right paragraph

3. **Content must MATCH quote** - no adding details, no inventing numbers

4. **When in doubt, DELETE** - better to miss detail than invent it

5. **All three checks must PASS** - one failure = item needs attention

6. **Implicit vs Explicit matters** - use correct verification procedure

7. **Multiple trigger passages allowed** - capture ALL relevant text

8. **Inference must be REASONABLE** - not speculative leaps

9. **Hallucination is CATASTROPHIC** - zero tolerance for fabrication

10. **Trust but VERIFY** - extraction confidence ≠ verification confidence

11. **RDMAP status matters** - Check status field first: explicit (in Methods) vs implicit (not in Methods)

12. **Implicit RDMAP needs full metadata** - basis, transparency_gap, assessability_impact, reconstruction_confidence

---

**End of Verification Procedures**

These procedures are referenced by Pass 1 and Pass 3 prompts. Follow them systematically to prevent evidence hallucination and ensure extraction integrity.
