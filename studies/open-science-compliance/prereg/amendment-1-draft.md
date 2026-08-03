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

**Promotion 2026-08-03 (registrant's decision).** The amendment text below is
the academic-prose re-expression, promoted after the registrant's read of
both versions. Content was verified token-invariant against the pre-promotion
text (all four token classes; generating session, 2026-08-03), the rule-4 §1
check was re-run against the promoted wording the same day (addendum in the
record below), and the skill-test file is archived at
`archive/prereg/amendment-1-draft-academic-prose.md`. §5 gains a two-sentence
cross-vendor pre-declaration (registrant's decision, 2026-08-03): a possible
extension to another provider's models is named as exploratory, not part of
this registration, and bound to the dated-amendment-plus-reliability-protocol
path that §7.1's FAIR4RS clause established.

---

## Amendment text (draft for the OSF field)

**Registration:** Phase 2 preregistration, DOI 10.17605/OSF.IO/DQNHG, lodged
2026-07-20, public 2026-07-21. Frozen artefact set at repository commit
`ee3fda3` (tag `osf-prereg-phase2-2026-07-20`).

**Nature of this amendment.** This amendment corrects clerical and
restatement defects found in one frozen artefact file, and pre-specifies
procedural detail that the registration left implicit for the registered
reliability checks (registration §8). Both actions precede any affected
analysis. No hypothesis, sampling frame, instrument scale, outcome
definition, or analysis is changed. No census or validation-phase data
existed when the amendment scope was fixed (ratified 2026-07-24), and the
amendment is lodged before the validation phase executes.

### 1. Erratum corrections to the Pass 6 instrument prompt

The frozen copy of `extraction-system/prompts/06-infrastructure_pass6_prompt.md`
contained three defects. Implementation review discovered them on 2026-07-22,
and the repository was corrected the same day (commit `abdc526`; erratum log
entry 1). First, a stale worked example read "14/16" and "87.5%",
contradicting the registered 15-sub-principle scale. The example now reads
14/15 and 93.3%. Second, a legacy "5-level access taxonomy" (Level 0–4)
collided in vocabulary with the registered six-level data-availability
taxonomy (§7.3). It has been renamed to "five-tier access classification
(Tier 0–4)" with an explicit demarcation note, and the L1–L6 taxonomy
remains assigned only at reproduction time from actual retrieval attempts,
exactly as registered. Third, a dead file pointer to a document removed in a
2026-07-03 repository reorganisation was repointed to the canonical schema
file. The registration's normative instrument statement (§7.1) is internally
consistent and unaffected, and all pilot scoring demonstrably used the /15
scale. These are erratum-class corrections that align an operational file
with the registration's own normative text.

A fourth correction to the same file followed on 2026-07-27 (erratum log
entry 2). The prompt's restatement of the instrument omitted four normative
statements that §7.1 carries: that unscoreable sub-principles score 0 (the
instrument scores evidenced practice); that data and code scores are never
aggregated into a combined score; the A1 completeness rule in full, namely
that A1 requires that a majority of the research data be retrievable via
standard protocol, with an exception for documented ethical or legal
restriction, where the prompt carried only the coverage-category trigger;
and the statement that FAIR for Research Software scoring is outside this
registration. The operational file now embeds a byte-exact copy of the
canonical instrument, and every repository commit now verifies that copy
mechanically rather than by assertion. The four omissions were checked
against the persisted pilot outputs, and none changed a recorded score.
Every pilot uses the 15-sub-principle scale, none leaves a sub-principle
unscored, and none records an aggregate score. In the one pilot where the A1
majority rule was decisive, A1 is recorded as absent with the supporting
count. This correction is likewise erratum-class, since the registration's
normative text governed throughout and is unchanged.

### 2. Below-threshold remediation ladder (reliability check §8(a))

The registration specifies that if mean per-sub-principle agreement falls
below 0.90, the census is scored by majority vote of three independent runs.
This amendment pre-specifies the permitted remediation path. One routing-fix
attempt is allowed, correcting the content-delivery mechanism only and
leaving instrument text untouched, followed by a single re-run of the §8(a)
stability check. If the re-run remains below threshold, the registered
majority-vote consequence applies with no further iteration. Both pre-fix
and post-fix reliability results are reported with study outcomes.

### 3. Validation-phase pre-specifications

**Agreement statistic.** The 3-run stability check uses the unanimity
proportion, the proportion of sub-principle items on which all three runs
agree. This is the strictest of the candidate agreement definitions. Since
candidate statistics cross the 0.90 gate at item-flip rates ranging from
roughly 10% to 30%, the choice cannot be left implicit.

**Pilot-paper set.** The stability check scores all five pilot papers, where
the registration requires at least three. This raises the item count from 90
to 150 and roughly halves the false-pass rate at a true agreement of 0.85,
from about 12% to about 5.5%. It is recorded for completeness, and it
strengthens rather than alters the registered check.

**Model-selection rule (gates plus cost).** The reliability spot-check
cannot statistically rank models. The confidence interval on an agreement
difference at the achievable n is approximately ±0.09, and no
registration-compliant sample size exists before the census. Accordingly,
any model that passes both (a) the registered 0.90 stability gate and (b) a
concordance floor of at least 0.90 (same statistic) against the pilot
reference scores is eligible, and among eligible models the cheapest scores
the census. Agreement differences inside the confidence interval are
pre-declared not to be grounds for selection.

Three model arms are benchmarked: `claude-sonnet-5`, `claude-opus-5`, and
`claude-fable-5`. Cost is evaluated at selection time from the provider's
published per-token prices. On pricing published at the time of this
amendment those three arms are strictly ordered, so the most capable and
most expensive arm cannot be selected for the census under any outcome of
the spot-check. It is run regardless, for two reasons stated in advance.
First, it establishes whether a more capable model clears the same
reliability gates, which is evidence about the instrument rather than about
the model. Second, it supplies the cross-model robustness data described in
§5. Should published pricing change the ordering before selection, the rule
applies to the prices in force at selection and the change is recorded with
the selection.

**Within-phase ordering.** Spot-check, then model selection, then the
registered regression gate run on the selected configuration with both lanes
pinned, then census.

**Run independence and provenance.** Each validation run is a fresh agent
spawn with no shared context and no persistent memory. Sampling seeds are
not controllable in the execution harness. Each run therefore records its
session identifier, its timestamp, and the full receipt triple (instrument
versions, agent-definition version, model identifier), and reports state
that run-to-run variation reflects default-temperature sampling.

One limit on that provenance is stated explicitly. The model identifiers
this study pins (`claude-sonnet-5`, `claude-opus-5`, `claude-fable-5`) are
the exact and complete identifier strings the provider publishes for those
models. The current generation carries no dated-snapshot variant to pin
instead, and appending a date produces an identifier the interface rejects.
A pinned identifier therefore names a model as the provider serves it at the
time of the call, not an immutable set of weights the study controls. The
receipt triple fixes what was requested and the run record fixes when, so
any provider-side change is bounded and visible in the archived artefacts,
although it is not prevented. Reports will describe model identity as
identifier plus run date on that basis. A provider-announced revision to a
pinned model is treated as a §8 regression-gate trigger in the same way as a
deliberate model change.

### 4. Read-scope isolation rule

Validation-phase scoring runs execute with read access restricted to the
paper source and the pushed or pulled instrument files. The repository holds
the pilot papers' canonical scores, so an unisolated scorer could reproduce
recorded answers and return perfect but uninformative agreement. Isolation
is enforced by tool allowlist and sandbox scope, and verified from the
harness transcript. Per-run file-access lists are archived with run
artefacts. The same hygiene applies at census scoring to any paper with
pre-existing repository artefacts.

### 5. Robustness annex

Scored runs from model arms that pass the gates but are not selected for the
census are archived and remain citable as cross-model robustness data. This
includes any arm that the cost rule in §3 excludes from selection by
construction. A cross-vendor extension, benchmarking models from
another provider on the same instrument, is a planned exploratory
direction and is not part of this registration. If implemented, it will
be lodged as a dated OSF amendment and will pass the same reliability
protocol (registration §8) before any cross-vendor scoring begins.

---

## Pre-lodgement checklist

- [x] Fold in any erratum-log entries added after 2026-07-24.
      (2026-07-27: Entry 2 folded into §1; model-identifier provenance limit
      added to §3. Re-check this item if further entries land.)
- [x] Word-for-word consistency check of §1 against the canonical
      `fair-instrument.md` and the Pass 6 prompt mirror (maintenance rule 4);
      record deliberate differences. (2026-08-02: done — record below. Three
      flags adjudicated same day: 1 fixed, 2 accepted as typography, 3
      dissolved by investigation. 2026-08-03: re-run against the promoted
      re-expression, PASS — addendum at the foot of the record below.)
- [ ] Registrant reads the final text; lodgement is by hand from the project
      view (five-file cap does not apply there), paste files unwrapped to
      flowing lines via `unwrap-paste-file.py`.
      (2026-08-03: registrant read both versions and promoted the
      re-expression; the §5 pre-declaration was displayed at promotion. Paste
      artefact built and verified — `osf-amendment-1.txt`. Hand-lodgement
      remains.)
- [ ] Tag the repository state at lodgement and record the amendment DOI/URL
      here and in `erratum-log.md`.

---

## §1 consistency check record — maintenance rule 4 (2026-08-02)

**Method.** Three-way comparison of §1's restatements against (a) the canonical
`protocol/instruments/fair-instrument.md`, (b) the Pass 6 prompt mirror, and
(c) preregistration §7.1 (`protocol/phase-2-preregistration-draft.md:382-392`),
with every quoted defect string re-verified against the frozen copy
(`git show ee3fda3:extraction-system/prompts/06-infrastructure_pass6_prompt.md`)
and every pilot-impact claim re-checked against the persisted
`outputs/*/extraction.json` files. The mirror region is byte-identical to the
canon region (5,123 bytes between markers, diffed this check), so (a) and (b)
are a single comparison target — which also re-confirms §1's "byte-exact copy,
verified mechanically" claim directly rather than by citing the gate.

**Verified at source.** The frozen-copy defect strings ("14/16", "87.5%",
"5-level access taxonomy" with Level 0-4 list, dead pointer) at `ee3fda3`
lines 662-663, 202-208, and 802, matching the erratum log's line references;
commit `abdc526` resolves and is dated 2026-07-22 ("the same day"); the
corrected worked example matches canon word-for-word ("total 14/15;
percentage 93.3%"); all four Entry 2 normative statements are present in
prereg §7.1 and in canon, and §1's restatements are word-for-word up to the
deliberate differences below; "never aggregated into a combined score" is
identical in all three sources; the four persisted FAIR assessments
(dye-et-al-2023, herskind-riede-2024, key-et-al-2024, marwick-2025) all use
`binary_sub_principles`, score 30 sub-principles each with zero left
unscored, carry no aggregate field, and key-et-al-2024 records A1
present=false with the "Only 3 of 13 datasets (23.1%)" count.

**Deliberate differences (recorded, no change made).**

1. **Range typography:** the amendment's prose uses en dashes ("Tier 0–4",
   "Level 0–4", "L1–L6") where the canonical file uses ASCII hyphens
   ("Tier 0-4", "L1-L6"). Wording identical.
2. **Unscoreable statement, parentheses not em dash:** §1's "(the instrument
   scores evidenced practice)" matches preregistration §7.1's exact rendering;
   canon carries the same statement with an em dash and bold. The amendment
   sides with the registration's own text.
3. **"ethical or legal restriction"** for canon's and §7.1's "ethical/legal
   restriction" — the slash expanded for flowing OSF prose. The only
   word-level difference found in any restated normative statement.
4. **Canon's italics on "majority" dropped** — formatting would not survive
   the OSF paste in any case.
5. **FAIR4RS statement summarised, not quoted** ("outside this registration"
   for canon/§7.1 "not part of the/this registration"); no quotation marks
   used, so a paraphrase, and consistent.
6. **"a 2026-07-03 repository reorganisation"** generalises the erratum log's
   "wiki migration" for an external audience.
7. **Mirror-verification claim narrower than the erratum log:** §1 says
   "on every repository commit"; the log adds "and at orchestrator
   pre-flight". The amendment claims the subset, which is true as stated.

**Flagged for the registrant's pre-lodgement read (E4) — verdicts 2026-08-02.**

1. **Quotation placement, second defect — RESOLVED (minimal fix applied,
   registrant's verdict 2026-08-02).** §1 quoted «"5-level access taxonomy
   (Level 0–4)"» with the parenthetical inside the quotation marks; the frozen
   copy contains "5-level access taxonomy" with Level 0…Level 4 as list items,
   never that literal string. The parenthetical now sits outside the closing
   quotation mark, matching erratum log entry 1.
2. **En dash inside the correction quote — ACCEPTED as typography
   (registrant's verdict 2026-08-02).** «"five-tier access classification
   (Tier 0–4)"» is quoted with an en dash where canon reads "(Tier 0-4)";
   subsumed by deliberate difference 1 above. No change.
3. **Scope of the pilot-impact sentence — PREMISE REVISED by the 2026-08-02
   investigation; no text change needed.** The flag claimed the persisted
   outputs carry FAIR assessments for four of the five pilots. Wrong: a fifth
   persisted assessment exists for crema-et-al-2024 at
   `outputs/crema-et-al-2024/run-02-session-per-pass/extraction.json`, under
   the pre-v2.6-convention top-level key `infrastructure` (the four later
   pilots use `reproducibility_infrastructure`) and one directory deeper than
   the `outputs/*/extraction.json` glob reaches — the two structural reasons
   both the erratum entry 2 sweep and this check's first pass missed it.
   Verified 2026-08-02: `binary_sub_principles`, data 12/15, code 12/15
   (matching pilot findings report v1.2 Table 5 exactly), 30 sub-principles
   scored, none unscored, no aggregate field, A1 present — so key-et-al-2024
   remains the one pilot where the A1 majority rule was decisive. §1's
   sentence is therefore fully supported for all five pilots as written.
   Related run-01 artefacts were archived, not lost (`c41242b`, 2026-01-13,
   100% rename into `archive/extraction-runs/`).

**Addendum — re-run against the promoted re-expression (2026-08-03).** The
academic-prose re-expression was promoted to lodgement text on the
registrant's decision. The rule-4 check re-ran against the promoted wording:
a token comparison across all four classes (backticked, quoted, numeric,
section references) is invariant against the pre-promotion text, and 13
frozen phrases (the four §7.1 normative restatements, the quoted defect and
correction strings, the DOI, tag, commit, and model identifiers) were each
verified verbatim in the promoted §1 and §3. The seven deliberate
differences above are unchanged in kind. The re-expression introduces
expression-only deltas: sentences split toward the register target, em
dashes removed, the "(a)/(b)" enumerators dropped from the
nature-of-amendment paragraph, and rhetorical antitheses trimmed where they
did not carry the claim. New content in this version is confined to the
registrant-commissioned §5 cross-vendor pre-declaration (two sentences,
2026-08-03), which restates the registered FAIR4RS extension pattern for a
possible other-provider benchmark and binds it to a dated amendment plus the
§8 reliability protocol.
