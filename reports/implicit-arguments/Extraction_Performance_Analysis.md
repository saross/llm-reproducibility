# Self-Assessment: Why the Extraction Performed Well
## Lessons Learned for Reproducible Performance

**Context:** Discussion & Conclusion extraction from Sobotkova et al. 2023
**Performance:** 29 evidence items, 48 claims, 4 implicit arguments with proper sourcing
**User observation:** This level of performance is difficult to maintain consistently

---

## What Actually Happened (Honest Reflection)

### 1. **I Read the Fundamentals First (Critical)**

**What I did:**
- Started by calling `file_read` on `/mnt/skills/user/research-assessor/references/extraction-fundamentals.md`
- This was BEFORE attempting any extraction
- The fundamentals document emphasized mandatory sourcing requirements

**Why this mattered:**
The fundamentals framed my entire extraction approach. Key insight from that document:
> "Before extracting ANY item, ask: 'Can I point to the exact text that states or implies this?' If NO → DO NOT EXTRACT"

This became my mental filter for the entire extraction. Every time I considered extracting something, I heard that voice: "Where's the quote?"

**Lesson learned:** The prompt tells me to read fundamentals, but actually DOING it and internalizing the sourcing discipline made the difference.

---

### 2. **Manageable Scope (Token Budget and Focus)**

**What I did:**
- Focused only on Discussion (sections 4.1-4.3) and Conclusion (section 5)
- ~14 pages of paper, dense but bounded
- Could hold the argumentative structure in working memory

**Why this mattered:**
I wasn't trying to keep the entire 40-page paper in mind while making extraction decisions. I could:
- Remember what I'd just extracted (avoiding duplication)
- See relationships between adjacent claims
- Track the comparative analysis structure (desktop GIS → volunteers → mobile → ML)
- Notice when evidence supported multiple related claims

**Contrast with full-paper attempt:**
When I tried the full paper extraction (earlier chat), I got overwhelmed around Discussion. Too much context, couldn't maintain focus, stopped early despite claiming completeness.

**Lesson learned:** Section-by-section extraction isn't just about token limits—it's about cognitive load management.

---

### 3. **I Took "Liberal Extraction" Seriously**

**What I did:**
- When uncertain whether something qualified as evidence vs. claim: I extracted it
- When granularity seemed high (E018-E029 efficiency chain): I kept it separate
- When claims seemed related but distinct: I didn't consolidate

**Mental model that worked:**
"Pass 2 can merge things. Pass 1 cannot recover missed items."

**Why this mattered:**
I didn't waste cognitive energy on consolidation decisions during extraction. I focused on:
1. Finding the content
2. Sourcing it properly (verbatim quote)
3. Categorizing it (evidence type, claim type)
4. Mapping relationships

The result: 29 evidence items from Discussion (more than the 3 from full-paper attempt) because I wasn't self-censoring.

**Lesson learned:** "Liberal extraction" requires actively suppressing the urge to consolidate during Pass 1.

---

### 4. **The Verbatim Quote Requirement Was Constraining (In a Good Way)**

**What I did:**
For every evidence and claim item, I had to:
1. Find the exact quote
2. Copy it verbatim
3. Only THEN extract the item

**Why this mattered:**
The sourcing requirement prevented:
- ❌ Hallucinated evidence ("they must have measured X")
- ❌ Over-interpreted claims ("this implies Y")
- ❌ Synthetic aggregations ("combining these suggests Z")

If I couldn't find the quote, I couldn't extract the item. Simple rule, powerful constraint.

**Example from my extraction:**
When extracting E024 ("Student programmer cost: approximately AUD $2,000"), I had to find the actual quote: "completed by a student programmer for a modest cost (ca. AUD $2,000)". The "ca." indicated uncertainty, which I captured in the declared_uncertainty field.

Without the sourcing requirement, I might have just written "Student programmer cost $2000" without noting the approximation.

**Lesson learned:** The verbatim quote requirement is not bureaucratic overhead—it's the guardrail that prevents extraction from becoming creative writing.

---

### 5. **The Schema Provided Clear Containers**

**What I did:**
- Used evidence_type taxonomy (quantitative_performance, quantitative_calculation, etc.)
- Used claim_type taxonomy (methodological_recommendation, comparative_effectiveness, etc.)
- Used claim_role hierarchy (core, intermediate, supporting)

**Why this mattered:**
Having clear categories meant I spent less time wondering "what is this?" and more time categorizing accurately.

**Example:**
E018 ("Project staff digitise at sustained rate of 60-75 features per staff-hour") immediately mapped to:
- evidence_type: quantitative_performance
- evidence_basis: direct_observation

Having these fields populated forced me to think about evidential strength, not just capture content.

**Lesson learned:** The schema isn't just data structure—it's a cognitive scaffold that guides extraction decisions.

---

### 6. **I Mapped Relationships As I Went**

**What I did:**
For each evidence item, I immediately asked: "What claims does this support?"
For each claim, I asked: "What evidence supports this? What other claims does it connect to?"

**Why this mattered:**
The relationship mapping forced me to understand the argumentative structure, not just extract isolated items.

**Example:**
E022 ("FAIMS Mobile approach: 190 features per staff-hour") supports C057 AND C064.
- C057: "190 features understates value" (because it doesn't count outsourcing)
- C064: "Qualitative factors argue for mobile approach" (efficiency is one factor)

Mapping both relationships meant I understood E022's role in the argument, which helped me decide it was worth extracting separately (not consolidating with other performance metrics).

**Lesson learned:** Relationship mapping during extraction improves item selection quality.

---

### 7. **The Paper Was Well-Structured (Luck Factor)**

**What I had:**
- Sobotkova et al. is a methods paper with clear structure
- Explicit comparative analysis (4 approaches × multiple metrics)
- Quantitative evidence with error bars
- Numbered sections and subsections
- Table 4 and Table 5 with payoff thresholds

**Why this mattered:**
Good paper structure makes extraction easier. The authors did half the work by:
- Clearly stating claims ("our approach becomes worthwhile for...")
- Providing explicit evidence ("57 h of staff time")
- Organizing comparatively (desktop GIS vs. mobile vs. ML)

**Lesson learned:** Some papers are harder to extract from. Recognize when paper quality is helping (or hindering) extraction performance.

---

### 8. **I Used the Implicit Argument Framework Systematically**

**What I did for implicit arguments:**
For each core claim, I asked the 4-type checklist:
1. Logical implications? (if explicit claims true, what must also be true?)
2. Unstated assumptions? (what do they assume without stating?)
3. Bridging claims? (missing links between evidence and conclusions?)
4. Disciplinary assumptions? (field-specific taken-for-granted knowledge?)

**Example:**
IA005 ("Staff time efficiency is the primary metric") emerged from asking:
"Why do all their payoff calculations focus on staff time? They SAY they focus on staff time, but why is that the RIGHT metric? What's assumed?"

The trigger passages showed they frame it as a choice ("focus on our most limited resource: staff time"), but the implicit argument is that this framing is APPROPRIATE for their context.

**Lesson learned:** The 4-type framework for implicit arguments provides a systematic search strategy, not just a classification scheme.

---

## What Could Have Gone Wrong (But Didn't)

### Failure Mode 1: "I'll Extract Everything and Sort It Later"
**Didn't happen because:** The sourcing requirement constrained me. Can't extract without a quote.

### Failure Mode 2: "This Seems Too Granular, I Should Consolidate Now"
**Didn't happen because:** I internalized "liberal extraction" as "Pass 2's job is consolidation, Pass 1's job is capture."

### Failure Mode 3: "I'm Not Sure What This Is, Skip It"
**Didn't happen because:** The prompt said "when uncertain, err on side of inclusion."

### Failure Mode 4: "I'll Just Skim for Main Points"
**Didn't happen because:** Section-by-section scope meant I could read carefully, not skim.

### Failure Mode 5: "Close Enough on the Quote"
**Didn't happen because:** I copied quotes verbatim (even the "ca." in E024). Slight pain, but prevented paraphrasing drift.

---

## Specific Prompt/Skill Improvements

Based on what worked, here are concrete suggestions:

### 1. **Make Fundamentals Reading Mandatory and Early**

**Current prompt:**
"🚨 CRITICAL: Sourcing Requirements
READ FIRST: `/mnt/skills/user/research-assessor/references/extraction-fundamentals.md`"

**Problem:** Easy to skip or defer reading until hitting an issue.

**Improvement:**
```
STEP 0 (MANDATORY): Before extraction, you MUST:
1. Read `/mnt/skills/user/research-assessor/references/extraction-fundamentals.md`
2. Internalize the sourcing test: "Can I point to exact text?"
3. Acknowledge that you've read and understood the fundamentals
4. ONLY THEN proceed to extraction

WITHOUT completing Step 0, extraction will fail sourcing requirements.
```

### 2. **Add Scope Management Guidance**

**Current prompt:** Doesn't explicitly address scope management.

**Improvement:**
```
EXTRACTION SCOPE:
- Optimal: 10-20 pages or 2-3 major sections per pass
- If paper is >30 pages: Extract section-by-section or split at major boundaries
- If extracting full paper: Be aware of cognitive load; consider mid-extraction break

WHY: Maintaining sourcing discipline and relationship mapping requires focused attention.
Working memory limitations affect extraction quality beyond token limits.
```

### 3. **Strengthen the Liberal Extraction Framing**

**Current prompt:**
"When uncertain whether something qualifies: INCLUDE IT."

**Improvement:**
```
LIBERAL EXTRACTION MENTAL MODEL:
- Pass 1 job: CAPTURE (comprehensively)
- Pass 2 job: CONSOLIDATE (rationally)

Active rules during Pass 1:
✓ When uncertain: EXTRACT IT
✓ When granular: KEEP IT SEPARATE
✓ When related: DON'T CONSOLIDATE YET
✗ Never think: "This seems too detailed for final output"
✗ Never think: "These should probably merge"
✗ Never self-censor due to perceived over-extraction

Pass 2 can merge. Pass 1 cannot recover missed items.
```

### 4. **Add Relationship Mapping Prompt**

**Current prompt:** Mentions relationships but doesn't emphasize their role in extraction quality.

**Improvement:**
```
RELATIONSHIP MAPPING DISCIPLINE:
For EACH evidence item, immediately ask:
- "What claims does this support?" → populate supports_claims
- "What other evidence is related?" → populate related_evidence

For EACH claim, immediately ask:
- "What evidence supports this?" → populate supported_by_evidence
- "What claims does this support/connect to?" → populate supports_claims, supported_by_claims

WHY: Mapping relationships during extraction (not after) improves:
- Item selection quality (understand argumentative role)
- Coverage (notice gaps in support)
- Consolidation readiness (Pass 2 can see clusters)
```

### 5. **Strengthen Implicit Argument Search**

**Current prompt:** Provides 4-type framework but could emphasize systematic search.

**Improvement:**
```
IMPLICIT ARGUMENT SYSTEMATIC SEARCH:
For EACH core claim, run the 4-type checklist:

1. LOGICAL IMPLICATIONS: "If this claim is true, what MUST also be true?"
   - Look for unstated logical consequences
   
2. UNSTATED ASSUMPTIONS: "What must be true for this claim to hold?"
   - Look for prerequisites not acknowledged
   
3. BRIDGING CLAIMS: "How do they get from evidence to this claim?"
   - Look for missing argumentative steps
   
4. DISCIPLINARY ASSUMPTIONS: "What field-specific knowledge is taken for granted?"
   - Look for insider assumptions invisible to outsiders

Document trigger passages for each implicit argument found.
If no implicit arguments found after systematic search → OK.
But if skipping search → NOT OK.
```

### 6. **Add Verbatim Quote Quality Check**

**Current prompt:** Requires verbatim quotes but doesn't emphasize quality.

**Improvement:**
```
VERBATIM QUOTE QUALITY STANDARDS:
✓ EXACT reproduction (including "ca.", "about", "perhaps")
✓ Include hedging language ("may", "likely", "suggests")
✓ Include uncertainty markers (ranges, qualifiers)
✓ Copy punctuation precisely

✗ NEVER paraphrase (even slightly)
✗ NEVER "clean up" awkward phrasing
✗ NEVER omit qualifiers to make claims stronger

SELF-CHECK: Could someone find this exact quote by Ctrl+F in the PDF?
If NO → You paraphrased. Start over.
```

---

## The Meta-Lesson: Constraints Enable Quality

The extraction went well not despite the constraints (verbatim quotes, sourcing discipline, liberal extraction mandate) but **because of them**.

Each constraint removed a decision burden:
- Verbatim quote requirement → No paraphrasing decisions
- Liberal extraction mandate → No consolidation decisions
- Section-by-section scope → No full-paper cognitive load
- Relationship mapping → No deferred organization

**The prompt should embrace and strengthen constraints, not apologize for them.**

---

## What to Test

If you want to reproduce this performance:

**Test 1: Fundamentals Reading Compliance**
- Does the extractor actually read extraction-fundamentals.md first?
- Can they articulate the sourcing test before beginning?

**Test 2: Scope Management**
- Are they trying to extract 40-page papers in one pass?
- Is extraction quality declining after 15-20 pages?

**Test 3: Liberal Extraction Internalization**
- Are they consolidating during Pass 1? (failure mode)
- Are they skipping items due to "seems too detailed"? (failure mode)

**Test 4: Verbatim Quote Discipline**
- Are quotes actually verbatim? (Ctrl+F test)
- Are qualifiers preserved? ("ca.", "about", "suggests")

**Test 5: Relationship Mapping**
- Are supports_claims fields populated during extraction?
- Or are they added as afterthought? (less reliable)

---

## Final Thought: The "Zone" Factor

There's an element of being "in the zone" during extraction that's hard to codify:
- Deep focus on the paper's argument
- Pattern recognition (seeing the efficiency comparison structure)
- Intuition about what matters

But the constraints and structure created conditions for that zone to happen:
- Manageable scope (not overwhelmed)
- Clear task (not ambiguous)
- Concrete rules (not subjective)
- Immediate feedback (can I find the quote?)

**You can't force the zone, but you can create conditions for it.**

The prompt improvements above aim to make those conditions more reliable.
