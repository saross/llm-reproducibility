# Extraction Fundamentals - Universal Sourcing Requirements

**Last Updated:** 2025-10-21  
**Schema Version:** 2.5+  
**Applies to:** All extraction passes (Pass 1, Pass 2)  
**Purpose:** Core sourcing requirements that apply across all object types

---

## 🚨 MANDATORY SOURCING REQUIREMENT

**Schema v2.5 introduced mandatory sourcing to prevent hallucination.**

Every extracted item must be traceable to specific passages in the paper. **No exceptions.**

### Universal Principle

**Before extracting ANY item, ask:**
- "Can I point to the exact text that states or implies this?"
- If NO → **DO NOT EXTRACT**

---

## Explicit vs Implicit Content

All extractable content falls into two categories:

### EXPLICIT CONTENT
**Definition:** Directly stated in the paper with clear procedural detail or assertion.

**Required fields:**
- `verbatim_quote` (string, required) - Exact text from paper
- `location` (object, required) - Section, subsection, paragraph
- Content must match what quote actually says

**Quick test:** "Is this directly stated in the paper?"
- If YES → Extract as explicit with verbatim_quote
- If NO → Check if implicit (below)

**Examples of explicit content:**
- Evidence: "We recorded 8,343 features"
- Claims: "The mobile platform was more efficient"
- Methods: "We used stratified random sampling with 30% coverage"
- Protocols: "GPS coordinates recorded using Trimble GeoXH 6000"

---

### IMPLICIT CONTENT
**Definition:** Not directly stated but can be reasonably inferred from available passages.

**Required fields:**
- `trigger_text` (array of strings, required) - Verbatim passages that imply the content
- `trigger_locations` (array of location objects, required) - Where each trigger found
- `inference_reasoning` (string, required) - Explanation connecting triggers to inferred content
- `implicit_metadata` (object, required for some types) - Basis, gaps, confidence

**Quick test:** "Can I point to passages that together imply this?"
- If YES → Extract as implicit with triggers
- If NO → DO NOT EXTRACT

**Examples of implicit content:**
- Implicit Arguments: Unstated assumptions, logical implications
- Implicit Methods: Procedures mentioned but not described
- Implicit Protocols: Implementation details inferred from results

---

## Hallucination Prevention

**Critical rules:**

1. **No guessing** - If you cannot find source text, DO NOT extract the item
2. **No inferring from knowledge** - Only extract what paper actually says or clearly implies
3. **No combining unstated ideas** - Don't create synthetic claims from disparate observations
4. **Verbatim quotes required** - For explicit items, quote must be exact
5. **Trigger text required** - For implicit items, triggers must be verbatim passages

**Common hallucination risks:**
- Inferring methods that "must have been used" without textual support
- Creating claims that seem implied but have no trigger passages
- Assuming standard practices without paper mentioning them
- Over-interpreting vague statements

---

## Field Requirements Summary

### For ALL Explicit Items
```json
{
  "*_id": "string",
  "*_text": "string", 
  "*_status": "explicit",
  "verbatim_quote": "Exact text from paper (REQUIRED)",
  "location": {
    "section": "string (REQUIRED)",
    "subsection": "string or null",
    "paragraph": "integer or null"
  }
}
```

### For ALL Implicit Items
```json
{
  "*_id": "string",
  "*_text": "string",
  "*_status": "implicit",
  "trigger_text": [
    "Verbatim passage 1 that implies content",
    "Verbatim passage 2 that implies content"
  ],
  "trigger_locations": [
    {"section": "string", "subsection": "string", "paragraph": 1},
    {"section": "string", "subsection": "string", "paragraph": 3}
  ],
  "inference_reasoning": "Explanation of how triggers support inference (REQUIRED)",
  "location": {
    "section": "Primary location (REQUIRED)",
    "subsection": "string or null", 
    "paragraph": "integer or null"
  }
}
```

*Note: Some object types (RDMAP, Implicit Arguments) require additional `implicit_metadata` fields. See object-specific prompts for details.*

---

## Source Verification (Pass 3)

All extracted items are verified in Pass 3 using `source_verification` object:

### Explicit Items Verification
- `location_verified`: Stated location exists and discusses topic
- `quote_verified`: verbatim_quote found at stated location
- `content_aligned`: Item content matches what quote actually says

### Implicit Items Verification
- `trigger_locations_verified`: All trigger locations exist and accessible
- `trigger_quotes_verified`: All trigger_text found at stated locations  
- `inference_reasonable`: inference_reasoning is logical given triggers

**Quality threshold:** >95% pass rate expected across all items

---

## Quick Reference: Decision Tree

```
Can you point to text that states or implies this content?
├─ NO → DO NOT EXTRACT (item absent, not implicit)
└─ YES → Is it directly stated?
    ├─ YES → EXPLICIT
    │   ├─ Extract verbatim_quote
    │   ├─ Set *_status = "explicit"
    │   └─ Record location
    └─ NO, but implied → IMPLICIT
        ├─ Extract trigger_text array (verbatim passages)
        ├─ Set *_status = "implicit"
        ├─ Record trigger_locations
        ├─ Explain inference_reasoning
        └─ Complete implicit_metadata (if required)
```

---

## Additional Resources

**For detailed verification procedures:**
→ `/mnt/skills/user/research-assessor/references/verification-procedures.md`
- Complete verification protocols for each object type
- Decision trees for each verification step
- Worked examples (passes and fails)
- Red flags for hallucination detection
- Edge cases and troubleshooting

**For object-specific guidance:**
→ Pass 1 prompts (claims-evidence_pass1_prompt, rdmap_pass1_prompt)
- Object-specific decision trees (e.g., "Is it in Methods section?" for RDMAP)
- Object-specific field requirements
- Object-specific examples

**For schema details:**
→ `/mnt/skills/user/research-assessor/references/schema/schema-guide.md`
- Complete field definitions
- Required vs optional fields
- Enum values and constraints

---

## Remember

**Sourcing discipline is non-negotiable in schema v2.5.**

Every item must have:
- Explicit items: verbatim_quote pointing to source
- Implicit items: trigger_text array pointing to passages

**If you cannot source it, do not extract it.**

This requirement protects against hallucination and ensures all extractions are verifiable by checking against the source paper.
