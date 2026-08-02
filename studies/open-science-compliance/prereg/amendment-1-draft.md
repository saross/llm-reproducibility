# OSF amendment 1 — consolidated draft (NOT YET LODGED)

**Status: DRAFT.** Lodgement timing per the registrant's 2026-07-24 decision:
this amendment lodges **just before the validation phase runs** (the hard
stop), so further errata found during the corpus and Phase 1 builds accumulate
here rather than generating piecemeal amendments. Scope RATIFIED by the
registrant 2026-07-24 from `erratum-log.md` (Queued amendment scope); wording
below is the lodgement draft. Before lodgement: re-run the consistency check
of amendment text against the canonical instrument files (maintenance rule 4),
append any new erratum-log entries, and convert to a paste artefact (flowing
lines, no tables — Open Science Framework (OSF) text boxes render breaks
literally and reduce tables to pipe soup; established 2026-07-20).

**Text change 2026-08-02 (registrant's decision).** §3 now pins three model
identifiers rather than two: the Fable 5 benchmark arm, authorised 2026-07-27
and authored the same day, is named in the registration. Two consequential
edits accompany it — §3 pre-declares that the arms are strictly price-ordered
and that the most expensive therefore cannot be selected for the census under
the cost rule (so its purpose is instrument evidence plus §5 robustness data,
stated in advance rather than reconstructed), and §5 confirms the annex covers
an arm excluded from selection by construction. The registrant's pre-lodgement
read covers this wording.

---

## Amendment text (draft for the OSF field)

**Registration:** Phase 2 preregistration, DOI 10.17605/OSF.IO/DQNHG, lodged
2026-07-20, public 2026-07-21. Frozen artefact set at repository commit
`ee3fda3` (tag `osf-prereg-phase2-2026-07-20`).

**Nature of this amendment.** This amendment (a) corrects clerical and
restatement defects found in one frozen artefact file, and (b) pre-specifies procedural
detail for the registered reliability checks (registration §8) that the
registration left implicit, before any affected analysis runs. No hypothesis,
sampling frame, instrument scale, outcome definition, or analysis is changed.
No census or validation-phase data existed when the amendment scope was fixed
(ratified 2026-07-24); the amendment is lodged before the validation phase
executes.

### 1. Erratum corrections to the Pass 6 instrument prompt

The frozen copy of `extraction-system/prompts/06-infrastructure_pass6_prompt.md`
contained three defects, discovered by implementation review on 2026-07-22 and
corrected in the repository the same day (commit `abdc526`; erratum log entry
1). First, a stale worked example read "14/16" and "87.5%", contradicting the
registered 15-sub-principle scale; corrected to 14/15 and 93.3%. Second, a
legacy "5-level access taxonomy (Level 0–4)" collided in vocabulary with the
registered six-level data-availability taxonomy (§7.3); renamed to "five-tier
access classification (Tier 0–4)" with an explicit demarcation note — the
L1–L6 taxonomy remains assigned only at reproduction time from actual
retrieval attempts, exactly as registered. Third, a dead file pointer to a
document removed in a 2026-07-03 repository reorganisation was repointed to
the canonical schema file. The registration's normative instrument statement
(§7.1) is internally consistent and unaffected; all pilot scoring
demonstrably used the /15 scale. These are erratum-class corrections aligning
an operational file with the registration's own normative text.

A fourth correction to the same file was found on 2026-07-27 (erratum log entry
2). The prompt's restatement of the instrument omitted four normative
statements that §7.1 carries: that unscoreable sub-principles score 0 (the
instrument scores evidenced practice); that data and code scores are never
aggregated into a combined score; the A1 completeness rule in full (A1 requires
that a majority of the research data be retrievable via standard protocol, with
an exception for documented ethical or legal restriction — the prompt carried
only the coverage-category trigger); and the statement that FAIR for Research
Software scoring is outside this registration. The operational file now embeds
a byte-exact copy of the canonical instrument, and the copy is verified
mechanically on every repository commit rather than by assertion. Checked
against the persisted pilot outputs, none of the four omissions changed a
recorded score: every pilot uses the 15-sub-principle scale, none leaves a
sub-principle unscored, none records an aggregate score, and the one pilot
where the A1 majority rule was decisive records A1 as absent with the
supporting count. This too is erratum-class: the registration's normative text
governed throughout and is unchanged.

### 2. Below-threshold remediation ladder (reliability check §8(a))

The registration specifies that if mean per-sub-principle agreement falls
below 0.90, the census is scored by majority vote of three independent runs.
This amendment pre-specifies the permitted remediation path: one routing-fix
attempt (correcting the content-delivery mechanism only; instrument text
untouched) followed by a single re-run of the §8(a) stability check. If the
re-run remains below threshold, the registered majority-vote consequence
applies with no further iteration. Both pre-fix and post-fix reliability
results are reported with study outcomes.

### 3. Validation-phase pre-specifications

**Agreement statistic.** The 3-run stability check uses the unanimity
proportion: the proportion of sub-principle items on which all three runs
agree. This is the strictest of the candidate agreement definitions;
candidate statistics cross the 0.90 gate at item-flip rates ranging from
roughly 10% to 30%, so the choice cannot be left implicit.

**Pilot-paper set.** The stability check scores all five pilot papers (the
registration requires at least three). This raises the item count from 90 to
150 and roughly halves the false-pass rate at a true agreement of 0.85 (from
about 12% to about 5.5%). Recorded for completeness; it strengthens rather
than alters the registered check.

**Model-selection rule (gates plus cost).** The reliability spot-check cannot
statistically rank models: the confidence interval on an agreement difference
at the achievable n is approximately ±0.09, and no registration-compliant
sample size exists before the census. Accordingly, any model that passes both
(a) the registered 0.90 stability gate and (b) a concordance floor of at
least 0.90 (same statistic) against the pilot reference scores is eligible;
among eligible models, the cheapest scores the census. Agreement differences
inside the confidence interval are pre-declared not to be grounds for
selection.

Three model arms are benchmarked: `claude-sonnet-5`, `claude-opus-5`, and
`claude-fable-5`. Cost is evaluated at selection time from the provider's
published per-token prices. On pricing published at the time of this
amendment those three arms are strictly ordered, so the most capable and most
expensive arm cannot be selected for the census under any outcome of the
spot-check. It is run regardless, for two reasons stated in advance rather
than reconstructed afterwards: to establish whether a more capable model
clears the same reliability gates, which is evidence about the instrument
rather than about the model; and to supply the cross-model robustness data
described in §5. Should published pricing change the ordering before
selection, the rule applies to the prices in force at selection and the
change is recorded with the selection.

**Within-phase ordering.** Spot-check, then model selection, then the
registered regression gate run on the selected configuration with both lanes
pinned, then census.

**Run independence and provenance.** Each validation run is a fresh agent
spawn with no shared context and no persistent memory. Sampling seeds are not
controllable in the execution harness; each run therefore records session
identifier, timestamp, and the full receipt triple (instrument versions,
agent-definition version, model identifier), and reports state that
run-to-run variation reflects default-temperature sampling.

One limit on that provenance is stated explicitly rather than left to be
inferred. The model identifiers this study pins (`claude-sonnet-5`,
`claude-opus-5`, `claude-fable-5`) are the exact and complete identifier
strings the provider publishes for those models — the current generation
carries no dated-snapshot variant to pin instead, and appending a date
produces an identifier the interface rejects. A pinned identifier therefore names a model as the provider
serves it at the time of the call, not an immutable set of weights the study
controls. The receipt triple fixes what was requested and the run record fixes
when, so any provider-side change is bounded and visible in the archived
artefacts; it is not prevented. Reports will describe model identity as
identifier plus run date on that basis, and a provider-announced revision to a
pinned model is treated as a §8 regression-gate trigger in the same way as a
deliberate model change.

### 4. Read-scope isolation rule

Validation-phase scoring runs execute with read access restricted to the
paper source and the pushed or pulled instrument files. The repository holds
the pilot papers' canonical scores, so an unisolated scorer could reproduce
recorded answers and return perfect but uninformative agreement. Isolation is
enforced by tool allowlist and sandbox scope and verified from the harness
transcript; per-run file-access lists are archived with run artefacts. The
same hygiene applies at census scoring to any paper with pre-existing
repository artefacts.

### 5. Robustness annex

Scored runs from model arms that pass the gates but are not selected for the
census are archived and citable as cross-model robustness data rather than
discarded. This includes any arm that the cost rule in §3 excludes from
selection by construction.

---

## Pre-lodgement checklist

- [x] Fold in any erratum-log entries added after 2026-07-24.
      (2026-07-27: Entry 2 folded into §1; model-identifier provenance limit
      added to §3. Re-check this item if further entries land.)
- [ ] Word-for-word consistency check of §1 against the canonical
      `fair-instrument.md` and the Pass 6 prompt mirror (maintenance rule 4);
      record deliberate differences.
- [ ] Registrant reads the final text; lodgement is by hand from the project
      view (five-file cap does not apply there), paste files unwrapped to
      flowing lines via `unwrap-paste-file.py`.
- [ ] Tag the repository state at lodgement and record the amendment DOI/URL
      here and in `erratum-log.md`.
