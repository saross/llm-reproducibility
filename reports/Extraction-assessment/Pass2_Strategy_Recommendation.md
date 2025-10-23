# Pass 2 Strategy Recommendation: Full Paper vs Section-by-Section

**Assessment Date:** 2025-10-23  
**Total Items:** 114 (46 evidence, 60 claims, 8 implicit arguments)

---

## Executive Recommendation

**Start with FULL PAPER Pass 2, with fallback to strategic splitting if needed.**

**Rationale:** The paper is manageable as a unit (114 items), cross-section relationships are important but minimal, and most consolidation is within-section. Full paper Pass 2 provides global view for consistency while remaining feasible.

---

## Analysis Supporting This Recommendation

### 1. **Volume is Manageable**

**Total: 114 items**
- Evidence: 46
- Claims: 60  
- Implicit Arguments: 8

**Assessment:** This is within the range for single-pass rationalization. Pass 2's consolidation task is less cognitively demanding than Pass 1's extraction because:
- Items already categorized and sourced
- Consolidation targets visible in cross-references
- Decision framework is clearer (lump or split)

**Comparison:** Pass 1 extracted 77 items from Discussion/Conclusion in one session. Pass 2 rationalization of 114 items should be feasible.

---

### 2. **Cross-Section Relationships Exist But Are Sparse**

**Evidence supporting claims in different sections: 5 instances**
- E001 (Abstract) → C011 (Introduction)
- E002 (Abstract) → C012 (Introduction)
- E005 (Results) → C004 (Abstract)
- etc.

**Claims supporting claims in different sections: 6 instances**
- C001 (Abstract) → C011 (Introduction)
- C017 (Introduction) → C016 (Abstract)
- etc.

**Assessment:** ~10% of relationships cross section boundaries. These are important for global coherence but don't dominate. **Full paper Pass 2 handles these naturally; section-by-section would need extra care to preserve them.**

---

### 3. **Consolidation is Primarily Within-Section**

| Section | Items | Consolidation Candidates |
|---------|-------|-------------------------|
| **Discussion** | 58 (51%) | 6 claims with 3+ evidence |
| **Conclusion** | 23 (20%) | 1 claim with 3+ evidence |
| **Results** | 12 (11%) | 2 claims with 3+ evidence |
| **Abstract** | 10 (9%) | - |
| **Introduction** | 3 (3%) | - |

**Key Insight:** Discussion contains 51% of items and most consolidation targets. Within-section work is primary; cross-section is secondary.

**Implication:** If you need to split, split is **Discussion/Conclusion vs Rest**, not strict section-by-section.

---

### 4. **Claim Hierarchy Spans Sections**

The claim hierarchy naturally flows across sections:
- **Core claims** appear in Abstract, Discussion, Conclusion
- **Supporting claims** concentrate in Discussion, Results
- Rationalization needs to assess whether core claims in Conclusion properly supersede supporting claims from earlier sections

**Example:**
- C051 (Discussion): "Crowdsourced digitisation proved unexpectedly successful" 
- C086 (Conclusion): "FAIMS facilitated multiple capabilities with high-quality results"

Are these separate core claims or should one be demoted? **Full paper view helps assess this.**

---

### 5. **Token Budget Consideration**

**Pass 1 experience:**
- Extracted 77 items (E018-E046, C051-C098, IA005-IA008) from Discussion/Conclusion in ~79,000 tokens
- Pass 2 rationalization should be MORE efficient because:
  - Items already extracted (no source text processing)
  - Decision framework clearer (consolidate or not)
  - Less writing required (editing existing items vs creating new)

**Rough estimate:** 114 items × 700 tokens per item = ~80,000 tokens for full paper Pass 2

**Assessment:** Feasible within token budget, especially if we're efficient about context loading.

---

## Recommended Approach

### **Strategy 1: Full Paper Pass 2 (Primary Recommendation)**

**Process:**
1. Load complete extraction (114 items)
2. Load Pass 2 consolidation prompt
3. Execute rationalization across entire paper
4. Monitor for:
   - Consistent consolidation logic across sections
   - Preservation of cross-section relationships
   - Proper claim hierarchy assessment
   - Token usage

**Advantages:**
- ✓ Global view of claim hierarchy
- ✓ Consistent consolidation decisions
- ✓ Cross-section relationships preserved naturally
- ✓ Single coherent rationalization pass
- ✓ Easier to assess core vs intermediate vs supporting across paper

**Risks:**
- ⚠️ Might hit token limits (but unlikely given 114 items)
- ⚠️ Could miss items in large context (but Pass 2 reviews all items systematically)

**When to use:** Default approach unless token issues emerge.

---

### **Strategy 2: Strategic Split (Fallback)**

**If full paper Pass 2 hits issues, split as:**

**Batch A: Abstract + Introduction + Results** (25 items)
- Minimal consolidation needed
- Foundational claims and evidence
- Quick pass

**Batch B: Discussion + Conclusion** (81 items)  
- Heavy consolidation work (7 claims with 3+ evidence)
- Most Pass 2 effort here
- Cross-references to Batch A preserved via IDs

**Process:**
1. Run Batch A first (establishes baseline)
2. Run Batch B with awareness of Batch A consolidations
3. Final pass: Verify cross-references still valid

**Advantages:**
- ✓ Discussion gets focused attention
- ✓ Token budget manageable
- ✓ Still maintains relationships via IDs

**Disadvantages:**
- ⚠️ Need to track consolidation decisions across batches
- ⚠️ Claim hierarchy assessment split
- ⚠️ Two separate rationalization contexts

**When to use:** If full paper Pass 2 exceeds token budget or becomes unwieldy.

---

### **Strategy 3: Section-by-Section (Not Recommended)**

**Why NOT section-by-section:**
- ❌ Overkill for 114 items
- ❌ Cross-section relationships require manual tracking
- ❌ Inconsistent consolidation decisions across 5 passes
- ❌ Claim hierarchy assessment fragmented
- ❌ More total work without clear benefit

**Exception:** If both Strategy 1 and 2 fail, you could go section-by-section, but this seems unlikely to be necessary.

---

## Decision Framework

```
START
  ↓
Try Full Paper Pass 2 (Strategy 1)
  ↓
  ├─ Success? → DONE (use full paper rationalization)
  ↓
  ├─ Token limits hit?
  │    ↓
  │    Try Strategic Split (Strategy 2: A+I+R, then D+C)
  │    ↓
  │    ├─ Success? → DONE (merge batches)
  │    ↓
  │    ├─ Still issues?
  │         ↓
  │         Consider section-by-section (Strategy 3)
  │         But this should be rare
```

---

## Specific Considerations for Pass 2

### **Items Requiring Cross-Section Awareness**

1. **Payoff thresholds** (C052 Discussion, C093 Conclusion) - Same topic, different sections
2. **Quality claims** (C004 Abstract, C090 Conclusion) - Hierarchical relationship
3. **Core findings** (Abstract vs Conclusion restatements) - Avoid duplication

**Full paper Pass 2 handles these naturally. Split approach needs to track them explicitly.**

### **Within-Section Consolidation Targets**

**Discussion (primary work):**
- Efficiency evidence chain (E018-E029): Decide whether to merge or preserve granularity
- Payoff threshold claims (C052, C070, C093, C094): Likely consolidation
- Qualitative factors (C064, C065, C066): Clear consolidation

**Conclusion:**
- Multiple methodological recommendation claims: Check for overlap with Discussion

**Results:**
- Error analysis evidence (high granularity): Assess whether to consolidate

---

## My Recommendation: Try Full Paper First

### **Why Full Paper:**

1. **Cognitive coherence** - You see the whole argument structure
2. **Consistent decisions** - Same consolidation logic throughout
3. **Natural relationships** - Cross-references work without extra effort
4. **Efficient** - One pass, one context, one rationalization
5. **Manageable volume** - 114 items is not excessive

### **Fallback Plan:**

If you hit token limits or find full paper unwieldy:
- Split at Discussion boundary (before/after)
- Discussion+Conclusion together (they form argumentative unit)
- Abstract+Intro+Results together (they're the foundation)

### **Don't Do Unless Necessary:**

Strict section-by-section Pass 2. The cross-references and claim hierarchy make this inefficient without clear benefit.

---

## Practical Next Steps

1. **Prepare Pass 2 prompt** (consolidation rules, decision framework)
2. **Load complete extraction** (sobotkova_extraction_pass1_COMPLETE.json)
3. **Execute full paper Pass 2** 
4. **Monitor for:**
   - Token usage (track throughout)
   - Consolidation quality (are decisions consistent?)
   - Cross-reference preservation (do IDs still work?)
   - Claim hierarchy (proper core/intermediate/supporting?)

5. **If issues arise:** Pivot to Strategy 2 (strategic split)

---

## Expected Outcomes

**Full paper Pass 2 should produce:**
- ~85-90 items (15-20% reduction from 114)
- Consolidated efficiency evidence (E018-E029 → fewer items)
- Merged payoff claims (C052/C070/C093/C094 → 1-2 items)
- Rationalized qualitative claims (C065/C066 → 1 item)
- Proper claim hierarchy (core/intermediate/supporting validated)
- Cross-references preserved and verified
- Consolidation metadata documenting all merges

If you achieve this in one pass, the full paper approach validated itself. If you need to split, you learned something about optimal scope for this paper's complexity.

---

## Final Recommendation

**Start with full paper Pass 2.** The volume is manageable, relationships are important, and it's the most cognitively coherent approach. Have strategic split as fallback, but don't preemptively split unless you hit issues.

Trust the data: 114 items, 10% cross-section relationships, clear consolidation targets—this is **designed** for full paper rationalization.
