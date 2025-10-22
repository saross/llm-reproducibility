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

## PART 3: Worked Examples

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

## PART 4: Red Flags for Hallucination

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

## PART 5: Edge Cases and Troubleshooting

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

## PART 6: Quality Metrics and Statistical Checks

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

## PART 7: Failure Handling Decision Tree

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

## PART 8: Verification Workflow Summary

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

---

**End of Verification Procedures**

These procedures are referenced by Pass 1 and Pass 3 prompts. Follow them systematically to prevent evidence hallucination and ensure extraction integrity.
