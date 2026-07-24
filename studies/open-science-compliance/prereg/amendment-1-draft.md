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

---

## Amendment text (draft for the OSF field)

**Registration:** Phase 2 preregistration, DOI 10.17605/OSF.IO/DQNHG, lodged
2026-07-20, public 2026-07-21. Frozen artefact set at repository commit
`ee3fda3` (tag `osf-prereg-phase2-2026-07-20`).

**Nature of this amendment.** This amendment (a) corrects three clerical
defects found in one frozen artefact file, and (b) pre-specifies procedural
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

**Within-phase ordering.** Spot-check, then model selection, then the
registered regression gate run on the selected configuration with both lanes
pinned, then census.

**Run independence and provenance.** Each validation run is a fresh agent
spawn with no shared context and no persistent memory. Sampling seeds are not
controllable in the execution harness; each run therefore records session
identifier, timestamp, and the full receipt triple (instrument versions,
agent-definition version, model identifier), and reports state that
run-to-run variation reflects default-temperature sampling.

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
discarded.

---

## Pre-lodgement checklist

- [ ] Fold in any erratum-log entries added after 2026-07-24.
- [ ] Word-for-word consistency check of §1 against the canonical
      `fair-instrument.md` and the Pass 6 prompt mirror (maintenance rule 4);
      record deliberate differences.
- [ ] Registrant reads the final text; lodgement is by hand from the project
      view (five-file cap does not apply there), paste files unwrapped to
      flowing lines via `unwrap-paste-file.py`.
- [ ] Tag the repository state at lodgement and record the amendment DOI/URL
      here and in `erratum-log.md`.
