# Implicit Extraction Architecture: Integrated vs Split

**Question:** Should implicit RDMAP extraction be condensed within Prompt 03, or split into a dedicated prompt?

**Context:**
- Prompt 01 (338 lines) successfully integrates implicit arguments extraction
- Prompt 03 (840 lines) newly integrates implicit RDMAP extraction - tested once successfully but reliability concerns

---

## Option A: Condense Within Prompt 03

**Structure:** 5 prompts total (current architecture)
- Prompt 01: Claims/Evidence Pass 1 (explicit + implicit arguments integrated) - 338 lines
- Prompt 02: Claims/Evidence Pass 2 - 425 lines
- Prompt 03: RDMAP Pass 1 (explicit + implicit integrated, CONDENSED) - ~590 lines ⬇ from 840
- Prompt 04: RDMAP Pass 2 - 541 lines
- Prompt 05: Validation - 506 lines

**Changes:** Reduce Prompt 03 by ~250 lines by mimicking implicit argument pattern

### Pros
- ✅ **Maintains workflow cohesion** - Explicit → implicit scanning in single pass
- ✅ **Fewer invocations** - More efficient execution
- ✅ **Context preservation** - Explicit items fresh in memory when scanning for implicit
- ✅ **Proven pattern** - Mirrors successful implicit argument structure
- ✅ **Simpler architecture** - Maintains 5-prompt design user validated
- ✅ **Natural flow** - Liberal extraction philosophy applies to both phases

### Cons
- ⚠️ **Still relatively long** - 590 lines is manageable but not short
- ⚠️ **Dual cognitive load** - Two mental models in one prompt:
  - Explicit scanning: "What procedures are DOCUMENTED in Methods?"
  - Implicit scanning: "What procedures are MENTIONED elsewhere or INFERRED?"
- ⚠️ **Risk of deprioritization** - Under cognitive pressure, implicit scanning might become superficial
- ⚠️ **No natural checkpoint** - No validation gate between explicit and implicit extraction

---

## Option B: Split Into Dedicated Implicit RDMAP Prompt

**Structure:** 6 prompts total (add implicit RDMAP as separate pass)
- Prompt 01: Claims/Evidence Pass 1 (with implicit arguments) - 338 lines [unchanged]
- Prompt 02: Claims/Evidence Pass 2 - 425 lines
- Prompt 03: RDMAP Pass 1 - Explicit only - ~300 lines ⬇ from 840
- **Prompt 04: RDMAP Pass 1b - Implicit only** - ~250 lines [NEW]
- Prompt 05: RDMAP Pass 2 - 541 lines
- Prompt 06: Validation - 506 lines

**Workflow sequence:**
```
Pass 1 (Claims/Evidence) → Pass 2 (Rationalize) →
Pass 3 (RDMAP Explicit) → Pass 4 (RDMAP Implicit) → Pass 5 (RDMAP Rationalize) →
Pass 6 (Validate)
```

### Pros
- ✅ **Dedicated focus** - Entire prompt devoted to single task: finding implicit RDMAP
- ✅ **Cognitive clarity** - Clear mental model: "Scan Results/Discussion for undocumented procedures"
- ✅ **Shorter prompts** - 300 + 250 lines vs 590 lines (more digestible)
- ✅ **Fresh executor state** - New invocation with singular clear goal
- ✅ **Natural quality gate** - Checkpoint: validate explicit RDMAP before scanning for implicit
- ✅ **Explicit items as seed list** - Already-extracted explicit RDMAP informs implicit scanning
- ✅ **Reduced cognitive load** - Not switching between documentation scanning and inference scanning
- ✅ **Mirrors successful architecture** - Pass 1/Pass 2 split works well (liberal/rationalize); explicit/implicit split is similar
- ✅ **Higher reliability** - Single-task focus reduces risk of superficial execution

### Cons
- ⚠️ **One more prompt** - 5 → 6 prompts (modest complexity increase)
- ⚠️ **Context switching** - Must reload extraction.json and understand what's already extracted
- ⚠️ **Maintenance overhead** - More files to keep synchronized
- ⚠️ **Potential connection loss** - Might miss relationships between explicit and implicit items (though cross-references can address this)

---

## Key Insight: Cognitive Model Shift

**Why does implicit argument integration work?**
- **Tight coupling:** Claims and their implicit assumptions are part of same reasoning chain
- **Same section:** Reasoning happens where claims are stated
- **Small instruction set:** Only 32 lines
- **Natural flow:** Extract claim → immediately examine what it depends on

**Why is implicit RDMAP different?**
- **Loose coupling:** Methods documented in Methods, implicit items scattered in Results/Discussion
- **Different sections:** Must scan across multiple sections for mentions/inferences
- **Different cognitive model:**
  - Explicit: "What procedures are DOCUMENTED?" (linear Methods reading)
  - Implicit: "What procedures are MENTIONED or INFERRED?" (scanning Results/Discussion for verb phrases, effects, undocumented tools)
- **Large instruction set:** 4-pattern recognition × 3 tiers = substantial instructions

**The cognitive model shift from explicit → implicit RDMAP is much larger than from claims → implicit arguments.**

---

## Analogy: Why Pass 1 → Pass 2 Split Works

Pass 1 and Pass 2 require different mental models:
- **Pass 1:** Liberal extraction (inclusive mindset: "when uncertain, include it")
- **Pass 2:** Rationalization (consolidation mindset: "which items are duplicates?")

Splitting them works because the task requires fundamentally different approaches.

**Similarly:**
- **Explicit RDMAP:** Documentation scanning (what's written in Methods)
- **Implicit RDMAP:** Inference scanning (what's mentioned elsewhere or implied by Results)

These also require fundamentally different approaches → splitting makes sense.

---

## What Would Prompt 04 (Implicit RDMAP) Look Like?

**Task:** Load extraction.json with explicit RDMAP already populated. Systematically scan for implicit RDMAP items.

**Structure (~250 lines):**

```markdown
# RDMAP Extraction Prompt - PASS 1b: Implicit RDMAP Scanning

## Your Task
Scan for implicit RDMAP items: strategic decisions, methods, and protocols that are:
- Mentioned but not documented (procedure referenced without description)
- Inferred from results (effects implying methodological causes)
- Undocumented but operationally necessary (tools/processes mentioned without specs)

**Input:** extraction.json with explicit RDMAP already populated
**Output:** Same extraction.json with implicit RDMAP items added

---

## Systematic Scanning Process

For EACH major section (Abstract, Introduction, Methods, Results, Discussion):

### Research Designs Scan (4 patterns)
1. Mentioned strategic decision without rationale?
2. Outcomes suggesting unstated design objectives?
3. Frameworks referenced without specification?
4. Strategic positioning without explicit design statement?

### Methods Scan (4 patterns)
1. Procedure mentioned without description?
2. Results implying unstated methodological approach?
3. Tools/approaches referenced without specification?
4. Analysis mentioned without method documentation?

### Protocols Scan (4 patterns)
1. Operational procedure mentioned without details?
2. Effects implying undocumented operational protocols?
3. Equipment/tools mentioned without specifications?
4. Data processing mentioned without procedure?

---

## For Each Implicit Item Found
[Detailed sourcing requirements: trigger_text, trigger_locations, inference_reasoning, implicit_metadata]

---

## Quality Checkpoints
- [ ] Completed 4-pattern scan for EACH section
- [ ] Documented scan methodology in extraction_notes
- [ ] All implicit items properly sourced
- [ ] Cross-referenced with explicit RDMAP (no duplication)

---

## Expected Outcomes
- Typical papers: 20-40% of RDMAP items implicit
- If zero implicit items: Document why (exceptional Methods documentation)
```

**Key features:**
- Singular focus: Finding implicit RDMAP
- Explicit items already known (can reference to avoid duplication)
- Clear 4-pattern structure per tier
- Liberal extraction still applies
- ~250 lines total (digestible)

---

## Historical Evidence

User stated: "An early test run in the Sonnet 4.5 chatbot successfully captured implicit RDMAP items, but it's been failing ever since I migrated to Claude Code."

**Hypothesis:** Early test may have had:
- Separate explicit instruction to scan for implicit RDMAP
- Interactive session allowing course correction
- Simpler, more focused prompt structure

This supports the split architecture.

---

## Comparative Analysis: Why Different Recommendations?

| Aspect | Implicit Arguments (Keep Integrated) | Implicit RDMAP (Split Out) |
|--------|--------------------------------------|----------------------------|
| **Coupling strength** | Tight (part of same reasoning chain) | Loose (methods vs results sections) |
| **Section location** | Same section as claims | Different sections (Methods vs Results/Discussion) |
| **Cognitive model shift** | Small (reasoning → assumptions) | Large (documentation → inference) |
| **Instruction complexity** | Simple (~32 lines) | Complex (4 patterns × 3 tiers) |
| **Total prompt length** | Manageable (338 lines) | Concerning (840 lines) |
| **Working status** | Proven reliable (7 items consistently) | Tested once (success but unproven) |
| **Integration rationale** | Natural workflow continuation | Requires separate mental model |

**Conclusion:** Different extraction types warrant different architectural choices.

---

## Recommendation: Split (Option B)

**I recommend Option B: Split implicit RDMAP into dedicated Prompt 04**

### Reasoning

1. **Cognitive clarity trumps efficiency**
   - The mental model shift from documentation scanning to inference scanning is substantial
   - Splitting respects this cognitive boundary

2. **Reliability under pressure**
   - Single-task 250-line prompt more reliable than dual-mode 590-line prompt
   - Fresh invocation state reduces risk of superficial execution
   - Proven: 338-line integrated prompt works; unproven: 590-line integrated prompt works consistently

3. **Natural quality gating**
   - Checkpoint: Extract explicit → validate → scan for implicit
   - Prevents rushing through implicit scanning

4. **Architectural consistency**
   - Pass 1/Pass 2 split works because different mental models
   - Explicit/Implicit split is analogous

5. **Empirical evidence**
   - Implicit RDMAP had systemic failure (0 items across all runs)
   - Single successful test at 840 lines insufficient to trust consistency
   - Early chatbot test suggests focused approach worked

6. **Asymmetric treatment justified**
   - Keep implicit arguments integrated (tight coupling, works reliably, 338 lines total)
   - Split implicit RDMAP (loose coupling, unproven at scale, would be 840 lines)

### Implementation

**New workflow:**
1. Claims/Evidence Pass 1 (with implicit arguments) [338 lines] - no change
2. Claims/Evidence Pass 2 [425 lines] - no change
3. RDMAP Pass 1 - Explicit extraction only [~300 lines] - remove implicit sections
4. **RDMAP Pass 1b - Implicit RDMAP scanning** [~250 lines] - new dedicated prompt
5. RDMAP Pass 2 [541 lines] - no change
6. Validation [506 lines] - no change

**Total:** 6 prompts (up from 5)
**Net line count:** ~2,360 lines (down from ~2,547 with 840-line Prompt 03)

---

## Counter-Arguments (Why Condense Might Be Better)

1. **User's original 5-prompt design** - Carefully considered architecture
2. **Implicit arguments work integrated** - Proves integration viable
3. **Context preservation** - Explicit items fresh when scanning for implicit
4. **Workflow simplicity** - 5 prompts cleaner than 6
5. **Real problem was workflow integration** - Now fixed with Phase A/B structure
6. **Single test success** - Maybe underestimating consistency at 840 lines?

**Response:** These are valid concerns, but:
- Implicit arguments work *because* of tight coupling and short instructions
- Context preservation can be achieved by loading explicit RDMAP at start of Prompt 04
- One additional prompt is modest complexity increase
- Phase A/B fixes the *integration* problem but doesn't address *cognitive load* problem
- Single test at 840 lines is insufficient evidence for consistent production use

---

## Verdict

**Split architecture (Option B) produces superior and more consistent results.**

The cognitive model shift between explicit and implicit RDMAP extraction is large enough to warrant separation, unlike implicit arguments where the tight coupling justifies integration.

**Confidence level:** High (75%)

**Recommended next step:** Implement split architecture before further testing.

---

**Version:** 1.0
**Date:** 2025-10-28
**Status:** Architectural recommendation
