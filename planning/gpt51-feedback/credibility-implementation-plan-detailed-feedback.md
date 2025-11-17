# External Review: Credibility Assessment Implementation Plan

## Reviewer

GPT-5.1 Thinking

## Summary Assessment

The implementation plan is impressively clear, internally consistent with your prior frameworks, and unusually “implementation ready” for this stage. It shows a strong grasp of HASS methodological diversity, keeps the repliCATS Seven Signals structure intact, and cleanly separates stable “skill” knowledge from runtime prompts. The two-track design (Track A for system quality, Track B for paper credibility) is a particularly thoughtful response to the risk of over-interpreting automated outputs.

At the same time, several core design choices carry non-trivial risks. The heavy decomposition into 10 prompts (7 for individual signals) risks fragmenting reasoning that is inherently holistic, and the Track A/B relationship is not yet operationalised in a way that constrains or conditions Track B outputs. Approach-specific assessment remains conceptually rich but mechanically underspecified, and the validation strategy leans heavily on informal “does this feel right” checks rather than reproducible reliability measures or early repliCATS alignment tests.

Overall, I would characterise the plan as methodologically thoughtful but somewhat over-engineered at the prompt level and under-engineered in its validation and governance. With some consolidation of the assessment workflow, clearer gating via Track A, and a more explicit reliability and alignment strategy, this could be a very solid foundation for credible HASS-oriented assessment.

---

## Major Concerns (3–5 issues)

### 1. Fragmented Prompt Architecture vs Holistic Judgement

**Issue:**
The plan adopts a strict “discrete tasks = separate prompts” heuristic and instantiates this as 10 prompts, including 7 separate prompts for the Seven Signals that run in parallel once classification is done.  Yet the signals are *conceptually interacting*: plausibility, validity, robustness, and replicability in particular are not independent dimensions for most real papers, and transparency/comprehensibility condition how you should interpret *all* other signals.

**Impact:**
By forcing each signal into its own prompt, you risk:

* Cross-signal incoherence (e.g. high validity but very low evidence sufficiency or robustness, with no explanation).
* Loss of shared context and trade-off reasoning (“this looks plausible because X, but validity is limited because Y” is inherently joint).
* Higher variance: slight differences in what the model attends to in each independent prompt may drive inconsistent scoring.

This is particularly problematic if you later want to compare scores across papers or against repliCATS, where human assessors explicitly reason across signals in an integrated way.

**Recommendation:**
Loosen the “discrete tasks = separate prompts” heuristic for the assessment stage. Concretely:

* Consider a **two-layer architecture**: one prompt that produces a *single structured JSON* object with all seven signal scores + rationales (using the assessment schema), then a downstream prompt that fans this out into seven Markdown files and a report.
* Alternatively, cluster signals into 2–3 prompts (e.g. {Comprehensibility/Transparency}, {Plausibility/Validity}, {Robustness/Replicability/Generalisability}) that explicitly cross-reference each other.

You can preserve modularity at the schema level while allowing reasoning to remain holistic at the judgement level.

---

### 2. Track A Is Conceptually Strong but Operationally Toothless

**Issue:**
Track A is described as a quality-monitoring track that evaluates extraction accuracy, metric validity, and classification quality, and outputs a `track-a-quality.md` file.  But the plan does not specify *what happens* when Track A identifies serious issues, nor how its results mechanically affect Track B assessments or the final report. At present it is introspective commentary, not part of the control logic of the system.

**Impact:**

* There is a real risk that Track B outputs (signal scores and credibility report) will be read as authoritative, even when Track A has flagged “low extraction confidence” or “metrics misaligned with qualitative evidence”.
* Without explicit behavioural rules, Track A cannot prevent misleading reports in cases where the upstream extraction is badly wrong (e.g., misclassified methods, missing claims).
* This weakens your claim that you are explicitly distinguishing “system quality” from “paper credibility”; the distinction exists in documentation but not in runtime behaviour.

**Recommendation:**

Introduce **explicit gating and conditioning rules**, and bake them into both prompts and file naming:

* If Track A extraction confidence is **low**, either:

  * Suppress full credibility reports and emit an abbreviated, heavily caveated “provisional assessment”, or
  * Force all signal prompts into a mode that *must* prefix their outputs with a bold warning (and perhaps restrict scoring to broad bands rather than precise numbers).
* If Track A detects serious misalignment between metrics and qualitative assessment, require the report generator to:

  * Include a dedicated “Assessment Limitations” section at the top, and
  * Optionally refuse to compute any composite credibility summary.
* Encode a small finite-state machine: `{OK → Full report}`, `{Caution → Report with strong caveats}`, `{Fail → No report; Track A only}` and document which states trigger which behaviours.

This keeps Track A from being a commentary appendage and turns it into a meaningful control mechanism.

---

### 3. Approach-Specific Assessment Is Conceptually Rich but Mechanically Vague

**Issue:**
Your frameworks carefully articulate how credibility criteria differ for inductive, deductive, and abductive research, and how different signals are emphasised for each approach.  However, in the implementation plan this becomes “approach-specific emphasis” without a clear mechanical specification of what that means: whether it changes scoring thresholds, modifies question sets, affects reporting only, or flows into any aggregate profile.

**Impact:**

* Without explicit rules, there is a danger of *hidden normative bias*: the model may internalise an implicit “deductive default” rubric and then just gesture at “inductive emphasis” verbally without actually changing how it scores.
* Comparisons across approaches become opaque. A score of 70 for “Replicability” in an inductive survey vs 70 in a computational genomics study does not mean the same thing, but your current design does not specify how that difference is represented or communicated.
* For repliCATS alignment, it will be very hard to know whether divergences are due to approach-specific adaptation or just general noise.

**Recommendation:**

You do not necessarily need 21 separate rubrics (7 × 3), but you do need **operational clarity**:

* For each signal, define explicit **approach-specific anchor descriptions** for the 0–100 scale (or at least for 20-point bands). E.g. “Replicability 80–100 for inductive field archaeology = analytic steps are fully documented and data are archived, *even though physical re-fieldwork is impossible*.”
* Consider outputting both a **raw score** and an **approach-normalised rating** (e.g. “Within typical expectations for inductive survey work in this field”) to make it clear that some scores should be interpreted relative to approach norms.
* In the classification JSON, you already plan a `signal_prioritisation` block; extend this to include *explicit textual guidance* that the assessment prompts must follow (e.g. primary signals must be elaborated at greater length; deemphasised signals may be scored but not highlighted in the executive summary).

This gives you a more auditable mapping from “approach” to “how signals are assessed and reported”.

---

### 4. Validation Strategy Is Under-Powered and Defers External Checks Too Late

**Issue:**
The validation plan relies primarily on manual inspection (“does this make sense?”), ad-hoc score distribution checks, and corpus-level face validity after the system is fully implemented. More formal reliability measures (test–retest, inter-model or inter-rater agreement) are not specified, and repliCATS-based external validation is explicitly postponed until *after* the full system has been deployed on your own corpus.

**Impact:**

* You may invest substantial effort in refining prompts and schemas for your 10-paper HASS corpus, only to discover later that the behaviour is structurally misaligned with repliCATS expert judgements or highly unstable across runs.
* Without quantitative reliability checks, you have no principled basis for deciding whether score differences of, say, ±5–10 points are meaningful or just noise.
* The emphasis on “independent development before external validation” is understandable methodologically, but in practice you risk building a system whose internal dynamics are hard to relate to your chosen benchmark.

**Recommendation:**

Introduce **lightweight but explicit reliability and external-sanity checks early**, without turning them into full calibration:

* For at least 2–3 papers, **run the full assessment multiple times** (with identical inputs) and record score variance for each signal. Decide in advance what SD (e.g. <10 points) is acceptable.
* Where possible, **have a human expert (you, or a collaborator)** independently score a subset of signals for one or two papers using your own rubrics, and compute simple agreement metrics (e.g. mean absolute difference).
* Even if you want to avoid full tuning to repliCATS, consider a *very small* early test on 1–2 repliCATS-assessed papers, not to calibrate but to confirm that you are at least in the right ballpark structurally (e.g. should not invert signal rankings).

This can be done alongside Phase 1–2 and will save you from discovering deep misalignments only after everything else is built.

---

### 5. Skill Boundary Creep and Single-Skill Overload

**Issue:**
The plan recommends extending the existing `research-assessor` skill to include all the new credibility-related reference material (approach taxonomy, signal definitions, HARKing guide, Track A criteria, schemas).  That skill already underpins the seven-pass extraction workflow. The new material covers a substantially broader task (interpretive assessment), not just extraction.

**Impact:**

* You risk violating your own separation-of-concerns principle. The skill will now contain both extraction-oriented and assessment-oriented frameworks, making it harder to reason about which parts are stable and which are still experimental.
* Prompt authorship and maintenance become more fragile: changes to credibility frameworks might have unintended knock-on effects on extraction prompts that also reference the skill.
* Future reuse becomes harder: you may want to use the extraction skill in contexts that *do not* involve credibility assessment, but the skill will now carry extra baggage and assumptions about repliCATS, HARKing, etc.

**Recommendation:**

At minimum, **strongly compartmentalise** credibility content within the skill; more robustly, consider a separate skill:

* Keep `research-assessor` focused on extraction, RDMAP, CEM, infrastructure, etc.
* Create a `credibility-assessor` skill that contains approach taxonomy, signal definitions, assessment frameworks, Track A criteria, and schemas.
* Your prompts can then explicitly load both skills when needed, and you can version them independently (e.g. extraction skill v2.5 stable; credibility skill v0.9 experimental).

This would align better with your stated “skills = stable knowledge” philosophy and make it easier to evolve the credibility framework without destabilising extraction.

---

## Medium Concerns (3–5 issues)

### 1. Ambiguous Handling of Low-Confidence Classification

**Issue:**
The classification framework allows for “low/medium/high” confidence and explicit mismatches (HARKing, methodological confusion, disciplinary convention), but the implementation plan does not say how *low confidence* or ambiguous classification states should affect downstream assessment.

**Impact:**

* An unstable or low-confidence approach label may still be treated as decisive in selecting an assessment framework or signal emphasis, potentially mis-framing the whole credibility evaluation.
* Papers that resist clean inductive/deductive/abductive categorisation (e.g. some software or methods papers) may be forced into an ill-fitting assessment regime.

**Recommendation:**

Add explicit rules such as:

* If `revealed_confidence = low` *or* `expressed_vs_revealed = mismatched` with unclear mismatch type, fall back to a **generic assessment mode** with minimal approach-specific weighting and strong caveats.
* Include a visible classification-confidence statement in the report’s methods section, indicating when approach classification is particularly uncertain.

---

### 2. File Format Choices and Downstream Automation

**Issue:**
The plan mixes JSON files (for classification and metrics), Markdown files (for signals and Track A), and even YAML embedded inside a `.json` file in the example classification structure.  This is workable for human reading but potentially fragile for automated tooling, versioning, or future visualisation.

**Impact:**

* Inconsistent serialisation increases the risk of subtle parsing errors, especially if you later want to compute corpus-level stats (e.g. mean signal scores across papers) or feed outputs into dashboards.
* Embedding YAML in a `.json` file is confusing for both humans and tools.

**Recommendation:**

Choose a **single canonical machine-readable format** for structured assessment data:

* Use JSON or YAML consistently for `classification`, `signal_assessments` and a global `assessment.json` (even if you still generate Markdown for human-readable reports).
* Keep Markdown purely for narrative reports and human-facing artefacts.
* Reserve filenames and extensions to reflect content faithfully (no YAML-in-JSON hybrids).

---

### 3. Normative Stance on “No Expressed Method” for Some HASS Traditions

**Issue:**
The classification framework treats “no expressed methodological framework” as, by default, indicative of methodological naivete or weak research design.  While often true, this is not universally valid across all HASS subfields or historical periods, where methodological commitments may be implicit, genre-specific, or expressed through narrative rather than explicit “methodology” sections.

**Impact:**

* You may systematically penalise certain subfields (or older scholarship) for norm divergences that are partly rhetorical or generic rather than genuinely methodological.
* This may skew transparency and plausibility scores and entrench a particular (often more recent, Anglophone) view of what “good HASS methodology” looks like.

**Recommendation:**

* Make the link between “none_stated” and “weak design” **explicitly defeasible**: include alternative explanations (genre conventions, historical period, journal norms) in the classification and assessment prompts.
* In Track A, monitor whether “none_stated” cases correlate with particular domains or eras; if so, you may need domain-specific adjustments rather than treating all such cases as straightforward weaknesses.

---

### 4. Report Length and Rhetorical Authority at Early Stages

**Issue:**
Generating 3–5 page reports from the outset, with detailed signal narratives and recommendations, risks creating rhetorically authoritative documents from a still-experimental system.

**Impact:**

* Readers may over-interpret fine-grained distinctions that are not yet supported by robust reliability evidence.
* The review burden on you and collaborators is high: each report is substantial, and manual validation across many pages per paper is labour-intensive.

**Recommendation:**

For the pilot phase:

* Use a **shorter, highly structured report template** (e.g. 1–2 pages with bulletised strengths, weaknesses, and score tables), and only later expand to 3–5 pages once reliability and alignment are better understood.
* Include a conspicuous “Experimental System – Do Not Use for High-Stakes Decisions” note in early outputs.

---

### 5. Metrics–Signals Integration Is Lightly Specified

**Issue:**
You have eight quantitative metrics from Phase 6 (ESD, TCI, RTI, etc.), and the plan notes that signal prompts will receive `metrics.json` as input. However, the mapping from metrics to signal judgements (and to Track A) is left implicit. 

**Impact:**

* Without explicit guidance, the model may either ignore metrics (wasting prior engineering effort) or overfit to them in idiosyncratic ways.
* The relationship between signal scores and metric values will be hard to interpret or analyse statistically.

**Recommendation:**

* For each signal, define which metrics are **primary evidence** and how they should be interpreted (e.g. “If ESD < X, then Validity cannot exceed Y unless the narrative provides a strong defence.”).
* In Track A, systematically log cases where metric-based expectations and narrative signal scores diverge strongly, and investigate patterns.

---

## Opportunities (2–3 suggestions)

### 1. Introduce a Single Canonical Assessment Object

Instead of treating `classification.json`, seven signal Markdown files, and `track-a-quality.md` as loosely linked artefacts, you could define a **single canonical `assessment.json` object** that encapsulates:

* Classification results
* Signal scores and rationales
* Track A quality indicators
* Metric summaries

Markdown reports and per-signal narrative files can then be generated from this canonical object. This would:

* Simplify cross-paper analysis and downstream tooling.
* Make it easier to check cross-signal consistency programmatically.
* Provide a natural location for versioning and change-tracking of assessments.

---

### 2. Exploit Cross-Model or Cross-Run Ensembles for Reliability

You are already thinking in terms of Claude Code as the main engine. An easy extension is to occasionally:

* Run the same assessment prompt with different random seeds or configurations and **compare outputs**.
* For high-stakes or exemplar papers, run the assessment both with Claude and with a second model (e.g. GPT) and treat disagreements as valuable signals.

This can be folded into Track A and give you a richer picture of epistemic uncertainty than single-run scores.

---

### 3. Early “Gold Standard” Micro-Corpus

Before tackling repliCATS in earnest, you could build a tiny **gold standard micro-corpus**:

* 3–5 papers from your own corpus, each with human-authored signal assessments using your rubrics.
* Treat these as regression tests: every time you change prompts or skills, rerun the pipeline and check how far you drift from the human baselines.

This would give you a concrete reference point that is structurally closer to your domain than psychology-focused repliCATS papers, and would nicely complement external validation later.

---

## Top 5 Recommendations (Prioritised)

1. **Re-architect the assessment prompts to reduce fragmentation.**
   Move from 7 fully independent signal prompts to either a single integrated assessment prompt (producing all signal scores/rationales) or a small number of clustered prompts, and use schemas rather than separate prompts for modularity.

2. **Give Track A real teeth.**
   Define explicit rules where low extraction/assessment quality gates or conditions Track B outputs (e.g. warning states, suppressed reports, constrained scoring) and ensure the report generator enforces these.

3. **Make approach-specific assessment operational, not just descriptive.**
   Specify how inductive/deductive/abductive status concretely alters scoring anchors, narrative emphasis, and interpretation, and bake this into both the classification JSON and the assessment prompts.

4. **Add early, lightweight reliability and alignment checks.**
   Introduce repeated-run variance checks, small human-coded baselines, and at least a minimal early test with a couple of repliCATS-assessed papers, so that you can detect structural misalignments before the system hardens.

5. **Separate extraction and credibility into distinct skills or clearly partitioned sub-skills.**
   Avoid overloading `research-assessor` with both extraction and assessment frameworks; instead, create a dedicated credibility skill or a clearly separated namespace to keep maintenance and evolution manageable.

---

## Overall Grade

**Grade: A- / B+ boundary**

The plan is thoughtful, well-documented, and clearly grounded in both HASS realities and repliCATS’s conceptual apparatus. It is “over-specified” in some good ways (file structures, checkpoints) and “under-specified” in some crucial ways (how approach and Track A actually affect behaviour; how reliability and alignment will be quantified). With the adjustments above—especially around prompt architecture, Track A governance, and explicit operationalisation of approach-specific assessment—you have the basis for a robust and genuinely interesting credibility-assessment pipeline.
