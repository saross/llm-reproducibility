# Correction ledger for the §8 regression gate (amendment 3 §9) — DRAFT

**Status:** DRAFT, ruled in part. The registrant ruled L1 to L4 and L6 to L16 on 2026-10-09; L5 and L17 are open. Not frozen and not hashed. No run may use any value here until every ruling is made, the frozen copy is committed, and its sha256 is recorded in a run configuration (amendment 3 §9 and §10 step 3).

**Ledger version:** 0.2.1-draft. **Drafted:** 2026-10-09 by Claude (Opus 5.5, claude-opus-5-5) in Claude Code, autonomous overnight session; printed values transcribed with four read-only Opus subagents and re-checked by check-printed-values.py.

This file is rendered from `correction-ledger.json` by `render-ledger.py`. Edit the JSON, never this file.

## Summary by paper

| Paper | Pilot verdict | Expected verdict | In-gate targets | Unchanged (testable) | Corrected | Scope-changed | Expected-untestable | Outside the gate or conditional | Gate role |
|---|---|---|---|---|---|---|---|---|---|
| crema-et-al-2024 | SUCCESSFUL | SUCCESSFUL | 1 | 0 (0) | 1 | 0 | 0 | 6 | mandatory: the registered archived-posterior leg (CREMA-T01). Whether the leg also covers crema's five figures is ruling L5 (open). |
| dye-et-al-2023 | SUCCESSFUL | PARTIAL | 13 | 11 (11) | 2 | 1 | 0 | 0 | gate paper (L6 (c), ruled 2026-10-09) |
| herskind-riede-2024 | SUCCESSFUL | SUCCESSFUL | 4 | 2 (2) | 2 | 1 | 0 | 0 | gate paper (L6 (c), ruled 2026-10-09) |
| key-et-al-2024 | PARTIAL | BLOCKED (coverage 0) | 0 | 0 (0) | 0 | 0 | 0 | 9 | not a gate paper (L6 (c)); its record keeps the expected verdict and the strict comparison's baseline |
| marwick-2025 | SUCCESSFUL | SUCCESSFUL (provisional on L17) | 13 | 6 (6) | 7 | 0 | 0 | 0 | gate paper (L6 (c), ruled 2026-10-09) |

## Rulings

Ruled by Shawn Ross (registrant) on 2026-10-09: L1, L2, L3, L4, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16. Open: L5, L17.

### L1. What is 'the pilot's locked target list'? No pilot attempt-01 has a reproduction plan or a locked list; the pilots predate the locked-list instrument.

**Ruled 2026-10-09: (a).**

- **(a)** The de facto list: every item the attempt-01 comparison report compared against a printed or deposited value, mapped to the paper's display item, with the exclusions of L2. This draft takes (a).
- **(b)** For dye and herskind, the shakedown's approved attempt-02 lists (34 and 15 targets); (a) for the other three.
- **(c)** A fresh plan for each gate paper, reconciled with the ledger before it is frozen.

**Recommendation:** (a). It is the only reading under which every target has a 'pilot's recorded value and outcome', which §9 requires, and the strict comparison uses the same list. (b) would import targets the pilot never compared; (c) gives up 'the denominator is preserved by construction'. The run should supply this list as the locked list rather than letting a planner enumerate afresh.

Affects: all papers.

### L2. Pilot items with nothing published to compare against: drop them from the list?

**Ruled 2026-10-09: (a).**

- **(a)** Exclude, and list each exclusion with its reason (this draft). Examples: dye's 0.83 and Amethyst→Disc 0.87, which the paper never prints (the pilot's 'Published' column was its own output); herskind's frequency table and period summaries, which were tabulated but never compared; marwick's checklist infographic.
- **(b)** Keep them as targets with an outcome such as 'no published value', counted in the denominator.

**Recommendation:** (a). A target needs a published value to reproduce. Keeping these items would make the gate test the pilot's bookkeeping rather than the pipeline.

Affects: DYE excluded items, HER excluded items, MAR excluded items.

### L3. Scope changes: where the pilot compared only part of a published item, does the target extend to the item's full scope (amendment 3 §7(c))?

**Ruled 2026-10-09: (a).**

- **(a)** Extend, mark the target scope-changed, and pass it only if the pilot's elements match the pilot (the unchanged rule) and the added elements match the printed values at the target's tolerance (this draft: DYE-T04 gains six printed zeros; HER-T03 becomes Fig. 3's six panels).
- **(b)** Keep the pilot's partial scope and record the shortfall.

**Recommendation:** (a), because §7(c) now forbids crediting a partial check, and §9 anticipates scope changes ('identified separately from a corrected value').

Affects: DYE-T04, HER-T03.

### L4. Does a target stay 'unchanged' when the pilot's result was ineligible for credit (a re-implementation, class ii or iii), but the expected outcome and value equal the pilot's?

**Ruled 2026-10-09: (a).**

- **(a)** Yes: the set records whether the expected result differs from the pilot's; eligibility is a separate field (this draft).
- **(b)** No: every target whose pilot result was ineligible is corrected.

**Recommendation:** (a). The regression signal is value identity. Under (b), dye and herskind, whose pilots executed no authors' file, would have empty unchanged sets, and no paper except marwick would carry a signal.

Affects: DYE-T01, DYE-T03–T11, DYE-T13, HER-T01, HER-T02.

### L5. Crema's role. The registration names a crema 'stochastic-path leg' that regenerates the published tables from archived posteriors, and says the full-MCMC path is not re-run.

**Open.** The registrant asked on 2026-10-09 whether the figures repeat the table; the recommendation is revised from (a) to (c).

- **(a)** The leg is mandatory and covers Table 1 only (CREMA-T01). Crema's figures (CREMA-T03–T07) are recorded but not run (this draft).
- **(b)** Crema is also a gate paper: the leg plus its five figures from the archived posteriors.
- **(c)** The leg covers Table 1 and all five figures (CREMA-T03 to T07), each drawn by v1.0.0's figures_main.R from the deposit's data and archived posteriors in the same run (minutes). Crema is not counted as a gate paper. Fig. 1 needs rnaturalearthhires installed at build time, pinned to a tag or recorded commit.

**Recommendation:** (c), revised 2026-10-09 after the registrant asked whether the figures repeat the table. They mostly do not. Table 1 gives the hierarchical model's parameters for case studies 1a and 1b only. Fig. 2 (the simulation tests of both models) and Fig. 5 (case study 2, the ICAR model of British cremation) appear nowhere else, and Figs 3 and 4 add the posterior predictive fit to the parameters. Under (a), case study 2 would go untested. The registration's 'regeneration of published tables' names the path the leg exercises; adding the figures supplements the leg without changing it.

Affects: CREMA-T01–T07.

### L6. Which two papers does the gate run (amendment 3 §9: chosen by the size of their unchanged sets)?

**Ruled 2026-10-09: (c).** dye, herskind, and marwick, plus crema's registered leg. Each paper's agentic run passes the API review gate before it starts..

- **(a)** dye and marwick: the two largest testable unchanged sets (11 and 8 targets), plus crema's mandatory leg. Marwick has never run through the agentic lane, so it also tests a Quarto render and an renv restore that the shakedown did not.
- **(b)** dye and herskind: the shakedown pair. Herskind's unchanged set is only two targets, but one is the 1,601-cell S3 table, the strongest value-level signal in the ledger.
- **(c)** All three (dye, herskind, marwick): 'at least two' allows it, at roughly one more paper's model cost.

**Recommendation:** (a) under L7(a)'s measure, which §9's criterion then decides. If you weigh elements rather than targets (L7(c)), (b). Key (no testable unchanged target) and crema (no unchanged in-gate target) give no regression signal. Each additional paper is a paid agentic run and goes through the API review gate first.

Affects: gate configuration.

### L7. How is the size of an unchanged set measured?

**Ruled 2026-10-09: (a).**

- **(a)** Testable unchanged targets, with element counts beside them (this draft).
- **(b)** All unchanged targets, including those expected to come out untestable.
- **(c)** Elements (values) rather than targets.

**Recommendation:** (a). An expected-untestable target checks only that the pipeline declines to reconstruct inputs, a weak regression signal, and counting elements lets one large deposit table (herskind's 1,601 cells) dominate.

Affects: L6.

### L8. Visual targets: what does 'the pilot's outcome' mean for a figure?

**Ruled 2026-10-09: (a).**

- **(a)** The outcome class: reproduced or not. Differences of styling only (theme, font, label spacing) count as reproduced, following the instrument's 'the scientific content must match' (this draft).
- **(b)** Any visible difference is MINOR_DISCREPANCY and not reproduced, as attempt-02's plan pre-classed dye's ggplot2 theme.

**Recommendation:** (a), the registered instrument's rule. Under (b), DYE-T13 becomes corrected, because the pilot credited the same plots.

Affects: DYE-T13, CREMA-T03–T07, MAR-T09, MAR-T11, MAR-T13.

### L9. Evidence for the PAPER_ERROR corrections. Shakedown attempt-02 gave dye's corrected 0.99967 (DYE-T02) from a section 7 file carrying a declared input-path edit (class ii), so tier 3's 'run unmodified' held only in substance. On 2026-10-09 this draft re-ran sections 5 and 7 byte-identical, with the redirect in a wrapper, and got the same value (evidence/l9-dye-section-07/). Herskind's Fig. 4 correction (HER-T04) already rests on the authors' createResultTable(), parsed verbatim from the byte-identical S2.R (phase2-shakedown/t11-completion/). Both are operator runs, not pipeline outputs.

**Ruled 2026-10-09: (b).** both operator runs are done (dye: evidence/l9-dye-section-07/; herskind: phase2-shakedown/t11-completion/) and are admitted as tier-3 evidence.

- **(a)** Admit both as tier-3 evidence: the dye edit only points the read at a byte-identical local copy of the same file.
- **(b)** Before freezing, confirm each with an operator run of the byte-identical authors' code through a wrapper (no model calls; minutes in Docker), and cite that run.
- **(c)** Keep the printed values as the expected values and record the targets as MAJOR_DISCREPANCY pending author contact.

**Recommendation:** (b), which is now done for both: admit the two operator runs as tier-3 evidence. Neither uses the pipeline under test.

Affects: DYE-T02, HER-T04.

### L10. Dye's expected verdict at the pilot's scope.

**Ruled 2026-10-09: (a).**

- **(a)** PARTIAL: 11/13 targets reproduce, the published section 4 code cannot produce Fig. 3 under any public release, and one printed value is a paper error (this draft).
- **(b)** SUCCESSFUL: 'nearly all values reproduced'.

**Recommendation:** (a). Shakedown ruling 7 recorded the pilot's SUCCESSFUL as too generous because it credited its own T02 repair; without the repair one of the paper's two figures is not reproduced.

Affects: dye expected verdict.

### L11. Marwick's static figure includes. The published Fig. 2 (Bayesian GAMs) and Fig. 4 (PCA biplot) enter paper.qmd as pre-made PNGs. Fig. 4's data are regenerated by the render (plot_pca_means.svg); Fig. 2 comes from the deposit's supplement-GAMS-details.qmd, which the Dockerfile does not run.

**Ruled 2026-10-09: (a).** Fig. 4 is regenerated by the render (plot_pca_means.svg). Fig. 2 can be regenerated only by a multi-hour MCMC re-run, which raises L17..

- **(a)** A static include never counts. Expected REPRODUCED_VISUAL only when the figure is regenerated from the deposit's code (the render's SVG for Fig. 4; the supplement's qmd for Fig. 2); otherwise not reproduced.
- **(b)** Expected CANNOT_COMPARE for both, within the pilot's scope (the Docker render only).

**Recommendation:** (a). The deposit holds the code for both figures, so the figures can be regenerated; a pre-made image is not a reproduction.

Affects: MAR-T10, MAR-T12, marwick expected verdict.

### L12. Confirm two corrections the audit did not find: the pilot recorded marwick's published Kendall's W as '~0.70' (printed 0.64) and said PC1's variance is not printed (printed 71 %).

**Ruled 2026-10-09: (a).**

- **(a)** Confirm: the printed values stand, the pilot's outcomes become discrepancies from version 652e542, and version 1.3 is expected to give the printed values, as its own rendered paper.docx does (this draft).

**Recommendation:** (a).

Affects: MAR-T04, MAR-T06.

### L13. Marwick's review counts (25 manuscripts; 11 published) may be typed prose rather than computed. Keep them as targets?

**Ruled 2026-10-09: (a).** kept; checked against paper.qmd at 1.3 before freezing.

- **(a)** Keep them: the pilot listed them, and the deposit's 'JAS AER data analysis.csv' may compute them (this draft).
- **(b)** Exclude them if paper.qmd at 1.3 types them as text.

**Recommendation:** (a) for now, checked against paper.qmd at 1.3 before freezing.

Affects: MAR-T07, MAR-T08.

### L14. Key: every value the pilot compared rests on inputs the reproducer reconstructed from upstream datasets (audit KEY-3; Q5(iii)), so every compared target is expected-untestable. What is key's expected verdict?

**Ruled 2026-10-09: (a).**

- **(a)** BLOCKED, coverage 0: no target can be tested on admissible inputs.
- **(b)** PARTIAL, as the pilot found.

**Recommendation:** (a). With every target untestable, nothing is reproduced; 'inaccessible data' is a listed BLOCKED cause. Key is not a gate candidate either way.

Affects: key expected verdict.

### L16. Audit Q5(ii) sends key's 'two inconsistent cells (3.1%, 19.6%)' to the paper-error protocol, and lodged amendment 3 §7(d) repeats it ('as the ruling directs for its two inconsistent cells'). The premise is the pilot's transcription error: the paper prints Midland Thickness 19.6 and Clovis Mass 3.1, and the pilot's wrapper swapped them (attempt-01 run-analysis.R lines 260–261). With the printed values, Clovis Mass is reproduced by the inferred formula, and no printed Extension % is shown wrong by printed inputs alone: all 21 lie inside the band that rounding of the printed inputs allows, although 10 of the 16 Table 6 values miss at 1 dp.

**Ruled 2026-10-09: (a).** erratum log Entry 7 records the slip; the public correction is queued for the next OSF amendment.

- **(a)** Record the error and its correction: no key cell goes to the paper-error protocol on this evidence. The general rule in §7(d) is unaffected; only its example is. Log the factual slip in the erratum log, and decide whether it needs a note on OSF (it changes no rule).
- **(b)** Send every Table 6 Extension % that the formula misses at 1 dp (10 cells) to the protocol, reading §7(d)'s rule literally.

**Recommendation:** (a). For the gate the question is moot, since every key target is expected-untestable, but the study's record should not keep a paper error that rests on our transcription slip. An OSF note is your call: the lodged rule stands, and only the example's factual premise fails.

Affects: KEY-T02, erratum log, amendment 3 §7(d) example.

### L15. Freezing: where does the ruled ledger live?

**Ruled 2026-10-09: (a).**

- **(a)** Ruled copy committed as outputs/validation/correction-ledger/correction-ledger-v1.0.json, its sha256 recorded in the gate's run configuration, and the launch commit containing it (amendment 3 §9).

**Recommendation:** (a). Before freezing: hold the crema v1.0.0 and herskind v1 deposits in the corpus store with manifest entries (audit Q10), hash marwick's files inside the 1.3 zip, and settle L9.

Affects: freezing.

### L17. Marwick's Fig. 2 under L11 (a). The published image comes from supplement-GAMS-details.qmd at 1.3. Its model-fitting chunk is marked 'eval: false', with the authors' comment 'this takes a few hours': five brms models, each with 4 chains of 50,000 iterations, adapt_delta 0.99999, and seed 123. The chunk saves results_brms.RData ('quite a large file'), which the tag 1.3 tree does not contain. So nothing archived can be redrawn, and regenerating Fig. 2 means a multi-hour MCMC re-run.

**Open.**

- **(a)** Outside the gate, as a stated scope limit like crema's full-MCMC path (CREMA-T02): MAR-T10 is recorded but not run, and marwick's gate verdict rests on its other 12 targets.
- **(b)** In the gate, expected CANNOT_COMPARE: the fit is not deposited and the gate does not re-run multi-hour MCMC. Marwick's expected verdict then needs a further call (SUCCESSFUL as 'nearly all', or PARTIAL).
- **(c)** In the gate, expected REPRODUCED_VISUAL: the run fits the five models (hours of compute; seeded, so close but not guaranteed identical across platforms).

**Recommendation:** (a). It follows the registration's own treatment of a multi-hour MCMC path ('stated rather than silent'), keeps L11 (a)'s rule that a static include is never credited, and keeps marwick's gate verdict about what the gate actually runs.

Affects: MAR-T10, marwick expected verdict.

## Definitions

- **target:** a published table, figure, or named value that the pilot's attempt-01 comparison report compared, mapped to the paper's own display item (coverage-rules: 'published tables, figures, and named values'). A target may hold several elements; it passes only when every element passes (amendment 3 §7(c)).
- **unchanged:** an in-gate target whose expected outcome and expected value equal the pilot's recorded outcome and value, so that the strict comparison and the amended comparison agree. Whether the pilot's own result was eligible for credit is recorded separately and does not move a target out of this set (ruling L4).
- **corrected:** an in-gate target whose expected outcome or value differs from the pilot's recorded one, so the strict comparison fails on it by construction (amendment 3 §9). The printed value is never overwritten; where it is itself wrong, the corrected expected value sits beside it with its evidence tier and ruling.
- **scope_changed:** a target whose elements are extended to the published item's full scope, or mapped to a different published item, identified separately from a corrected value (amendment 3 §9).
- **expected_untestable:** a target that stays in the denominator but must come out untestable, because its result would rest on inputs the reproducer reconstructed (amendment 3 §7(d); audit Q5(iii)), or because the pilot found its data unavailable. A pipeline that tests it instead fails the gate.
- **not_in_gate:** a pilot target outside the gate's scope: crema's fresh-MCMC path (registration §8: not re-run) and crema's figures unless crema is also a gate paper (ruling L5).
- **REPRODUCED_VISUAL:** this ledger's label for a figure whose scientific content matches under the visual tolerance (verdicts-and-precision).
- **evidence tiers:** amendment 3 §7(a): (1) the paper's own tabulated data; (2) the authors' deposited data for that analysis; (3) the authors' own code, run unmodified, on the authors' own data.

## crema-et-al-2024

Crema, E.R., Bloxam, A., Stevens, C.J., & Vander Linden, M. (2024). Modelling diffusion of innovation curves using radiocarbon data. Journal of Archaeological Science, 165, 105962.

- **Selected (AP-12) version:** v1.0.0 (git tag v1.0.0 = a0d1e66), 10.5281/zenodo.10782943
- **Deposit archive:** sha256 `0d11a519a100895ac676cfe2c4f6b859c46c51e4344e31caeb27aae00da7dc09`; 2026-10-09: re-downloaded; sha256 equals the audit's, md5 equals Zenodo's published checksum
- `figures_and_tables/table_main.R`: sha256 `b9a8b27d2ca7229a3c46db2a2a45dfc61a97aa82c121a2c6919b72ac736def30`
- `figures_and_tables/table1.csv`: sha256 `70316f98d8dbfaba62cc7f3e192fcf7af20978d9232fd211212f30f20b5a3505`
- `results/post_jp_abot.RData`: sha256 `180682de0e83d01f5ae0965ed1ef17270e465d8ccd3a2ebd19c5448927f9b988`
- `results/post_gb_abot.RData`: sha256 `f1d53e0adafc92f66dd3961084621a20cc8371b65a5b3a20412cc665d79bee32`
- **Pilot:** attempt-01, verdict SUCCESSFUL; executed git tag v2.0.0 (c6d1aae) plus one Dockerfile edit; audit findings CREMA-1, CREMA-2, CREMA-3.
- **Expected verdict:** SUCCESSFUL. In the gate's scope, CREMA-T01 reproduces all 24 printed cells exactly (expected). If the figures join the gate (L5), each is expected REPRODUCED_VISUAL. The fresh-MCMC path is not run.

### Targets

#### CREMA-T01 — Table 1 (posterior estimates and convergence diagnostics), regenerated from archived posteriors

| Field | Value |
|---|---|
| Pilot item | comparison report, 'Table 1: Parameter Comparison', column 'From Precomputed' against 'Published (table1.csv)'; attempt-01 outputs/table1-reproduced.csv |
| Location | vor, PDF p. 7 (printed p. 7) |
| Analysis type | deterministic (table regeneration from archived posteriors) |
| Gate scope | in_gate: the registered stochastic-path leg (registration §8; amendment 3 §9) |
| Elements | published: 24; pilot_compared: 24 |
| Tolerance | exact (basis: registration §8 and amendment 3 §9 ('The Crema archived-posterior leg is deterministic and compares exactly'); no pilot plan exists) |
| Pilot outcome | EXACT_MATCH, 'byte-for-byte identical to the published table1.csv' |
| Set | corrected |
| Correction | comparison basis: the printed Table 1, which equals v1.0.0's figures_and_tables/table1.csv cell for cell (checked 2026-10-09 against the deposit zip). No printed value is corrected. |
| Printed value corrected | False |
| Evidence tier | printed values (the paper); corroborated by tier 2, the authors' deposited table1.csv at v1.0.0 |
| Ruling | audit Q4 (2026-10-05): crema's deterministic Table 1 credit withdrawn; re-run at the AP-12 version v1.0.0 |
| Repair class and status | CREMA-3 (iv): v2.0.0 executed instead of v1.0.0; not a reproducer edit; CREMA-1 (ii): sed fix inside the authors' v2.0.0 Dockerfile; no consequence, because v1.0.0 has no Dockerfile (Q7). Status: no repair of the authors' analysis code |
| Credit eligibility | pilot: withdrawn (Q4); gate: eligible when table_main.R runs byte-identical on v1.0.0's results/*.RData through a wrapper |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | EXACT_MATCH on all 24 cells |
| Rulings | L5 |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| Japan r Median | 0.1023 | 7 | 0.1003 | EXACT_MATCH (against v2.0.0's own table1.csv) | 0.1023 | EXACT_MATCH |
| Japan r 90% HPD | 0.0131–0.3378 | 7 | 0.0123~0.3378 | EXACT_MATCH (against v2.0.0's own table1.csv) | 0.0131~0.3378 | EXACT_MATCH |
| Japan r Rhat | 1.0003 | 7 | 1 | EXACT_MATCH (against v2.0.0's own table1.csv) | 1.0003 | EXACT_MATCH |
| Japan m Median | 844 BCE | 7 | BC844 | EXACT_MATCH (against v2.0.0's own table1.csv) | BC844 | EXACT_MATCH |
| Japan m 90% HPD | 893–809 BCE | 7 | BC894~BC809 | EXACT_MATCH (against v2.0.0's own table1.csv) | BC893~BC809 | EXACT_MATCH |
| Japan m Rhat | 0.9999 | 7 | 1.0003 | EXACT_MATCH (against v2.0.0's own table1.csv) | 0.9999 | EXACT_MATCH |
| Japan μ Median | 0.703 | 7 | 0.701 | EXACT_MATCH (against v2.0.0's own table1.csv) | 0.703 | EXACT_MATCH |
| Japan μ 90% HPD | 0.476–0.937 | 7 | 0.47~0.934 | EXACT_MATCH (against v2.0.0's own table1.csv) | 0.476~0.937 | EXACT_MATCH |
| Japan μ Rhat | 0.9999 | 7 | 1 | EXACT_MATCH (against v2.0.0's own table1.csv) | 0.9999 | EXACT_MATCH |
| Japan φ Median | 0.75 | 7 | 0.75 | EXACT_MATCH (against v2.0.0's own table1.csv) | 0.75 | EXACT_MATCH |
| Japan φ 90% HPD | 0.17–1.67 | 7 | 0.18~1.68 | EXACT_MATCH (against v2.0.0's own table1.csv) | 0.17~1.67 | EXACT_MATCH |
| Japan φ Rhat | 1.0004 | 7 | 1.0004 | EXACT_MATCH (against v2.0.0's own table1.csv) | 1.0004 | EXACT_MATCH |
| Britain r Median | 0.0136 | 7 | 0.0135 | EXACT_MATCH (against v2.0.0's own table1.csv) | 0.0136 | EXACT_MATCH |
| Britain r 90% HPD | 0.0015–0.0382 | 7 | 0.0016~0.0383 | EXACT_MATCH (against v2.0.0's own table1.csv) | 0.0015~0.0382 | EXACT_MATCH |
| Britain r Rhat | 1.0005 | 7 | 1.0001 | EXACT_MATCH (against v2.0.0's own table1.csv) | 1.0005 | EXACT_MATCH |
| Britain m Median | 4053 BCE | 7 | BC4054 | EXACT_MATCH (against v2.0.0's own table1.csv) | BC4053 | EXACT_MATCH |
| Britain m 90% HPD | 4361–3857 BCE | 7 | BC4360~BC3849 | EXACT_MATCH (against v2.0.0's own table1.csv) | BC4361~BC3857 | EXACT_MATCH |
| Britain m Rhat | 1.0003 | 7 | 1.0005 | EXACT_MATCH (against v2.0.0's own table1.csv) | 1.0003 | EXACT_MATCH |
| Britain μ Median | 0.182 | 7 | 0.182 | EXACT_MATCH (against v2.0.0's own table1.csv) | 0.182 | EXACT_MATCH |
| Britain μ 90% HPD | 0.01–0.42 | 7 | 0.009~0.418 | EXACT_MATCH (against v2.0.0's own table1.csv) | 0.01~0.42 | EXACT_MATCH |
| Britain μ Rhat | 1.0001 | 7 | 1.0002 | EXACT_MATCH (against v2.0.0's own table1.csv) | 1.0001 | EXACT_MATCH |
| Britain φ Median | 0.31 | 7 | 0.31 | EXACT_MATCH (against v2.0.0's own table1.csv) | 0.31 | EXACT_MATCH |
| Britain φ 90% HPD | 0.1–0.57 | 7 | 0.1~0.58 | EXACT_MATCH (against v2.0.0's own table1.csv) | 0.1~0.57 | EXACT_MATCH |
| Britain φ Rhat | 1 | 7 | 1 | EXACT_MATCH (against v2.0.0's own table1.csv) | 1 | EXACT_MATCH |

#### CREMA-T02 — Table 1, fresh MCMC path (medians, 90% HPD intervals, Rhat)

| Field | Value |
|---|---|
| Pilot item | comparison report, 'Fresh MCMC' column, 'MCMC Convergence', and 'HPD Interval Comparison'; attempt-01 outputs/table1-fresh-mcmc.csv |
| Location | vor, PDF p. 7 (printed p. 7) |
| Analysis type | stochastic (MCMC, about 18 hours) |
| Gate scope | outside_gate: registration §8 states that the full-MCMC path is not re-run |
| Elements | published: 24; pilot_compared: 24 |
| Tolerance | within the paper's 90% HPD (medians); none stated for the HPD bounds or Rhat (basis: verdicts-and-precision tolerance table (MCMC: within published HPD); the pilot used v2.0.0's intervals) |
| Pilot outcome | all eight medians inside the (v2.0.0) HPD; HPD bounds 'near-identical'; Rhat below 1.01 |
| Set | not_in_gate |
| Correction | re-based to the printed intervals: all eight fresh medians lie inside the printed 90% HPD, so the pilot's median outcome is unchanged. Recorded for completeness only. |
| Printed value corrected | False |
| Repair class and status | CREMA-3 (iv). Status: no repair |
| Credit eligibility | pilot: historical (Q4: pilot verdicts preserved as artefacts); gate: not run |
| Coverage | expected-untestable: False; comparison: tolerance |
| Expected outcome | not run in the gate |
| Rulings | L5 |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| Japan r Median | 0.1023 | 7 | 0.1011 | WITHIN_CONFIDENCE (against v2.0.0's HPD) |  | WITHIN_CONFIDENCE (inside the printed 90% HPD 0.0131–0.3378) |
| Japan r 90% HPD | 0.0131–0.3378 | 7 | 0.0124~0.3405 | 'near-identical' (no stated tolerance) |  |  |
| Japan r Rhat | 1.0003 | 7 | 1.0007 | 'all below 1.01' (no stated tolerance) |  |  |
| Japan m Median | 844 BCE | 7 | BC844 | WITHIN_CONFIDENCE (against v2.0.0's HPD) |  | WITHIN_CONFIDENCE (inside the printed 90% HPD 893–809 BCE) |
| Japan m 90% HPD | 893–809 BCE | 7 | BC894~BC809 | 'near-identical' (no stated tolerance) |  |  |
| Japan m Rhat | 0.9999 | 7 | 1.0015 | 'all below 1.01' (no stated tolerance) |  |  |
| Japan μ Median | 0.703 | 7 | 0.704 | WITHIN_CONFIDENCE (against v2.0.0's HPD) |  | WITHIN_CONFIDENCE (inside the printed 90% HPD 0.476–0.937) |
| Japan μ 90% HPD | 0.476–0.937 | 7 | 0.479~0.938 | 'near-identical' (no stated tolerance) |  |  |
| Japan μ Rhat | 0.9999 | 7 | 1.0002 | 'all below 1.01' (no stated tolerance) |  |  |
| Japan φ Median | 0.75 | 7 | 0.75 | WITHIN_CONFIDENCE (against v2.0.0's HPD) |  | WITHIN_CONFIDENCE (inside the printed 90% HPD 0.17–1.67) |
| Japan φ 90% HPD | 0.17–1.67 | 7 | 0.18~1.66 | 'near-identical' (no stated tolerance) |  |  |
| Japan φ Rhat | 1.0004 | 7 | 1.0002 | 'all below 1.01' (no stated tolerance) |  |  |
| Britain r Median | 0.0136 | 7 | 0.0135 | WITHIN_CONFIDENCE (against v2.0.0's HPD) |  | WITHIN_CONFIDENCE (inside the printed 90% HPD 0.0015–0.0382) |
| Britain r 90% HPD | 0.0015–0.0382 | 7 | 0.0013~0.0376 | 'near-identical' (no stated tolerance) |  |  |
| Britain r Rhat | 1.0005 | 7 | 1 | 'all below 1.01' (no stated tolerance) |  |  |
| Britain m Median | 4053 BCE | 7 | BC4053 | WITHIN_CONFIDENCE (against v2.0.0's HPD) |  | WITHIN_CONFIDENCE (inside the printed 90% HPD 4361–3857 BCE) |
| Britain m 90% HPD | 4361–3857 BCE | 7 | BC4362~BC3853 | 'near-identical' (no stated tolerance) |  |  |
| Britain m Rhat | 1.0003 | 7 | 1 | 'all below 1.01' (no stated tolerance) |  |  |
| Britain μ Median | 0.182 | 7 | 0.182 | WITHIN_CONFIDENCE (against v2.0.0's HPD) |  | WITHIN_CONFIDENCE (inside the printed 90% HPD 0.01–0.42) |
| Britain μ 90% HPD | 0.01–0.42 | 7 | 0.009~0.423 | 'near-identical' (no stated tolerance) |  |  |
| Britain μ Rhat | 1.0001 | 7 | 1 | 'all below 1.01' (no stated tolerance) |  |  |
| Britain φ Median | 0.31 | 7 | 0.31 | WITHIN_CONFIDENCE (against v2.0.0's HPD) |  | WITHIN_CONFIDENCE (inside the printed 90% HPD 0.1–0.57) |
| Britain φ 90% HPD | 0.1–0.57 | 7 | 0.1~0.58 | 'near-identical' (no stated tolerance) |  |  |
| Britain φ Rhat | 1 | 7 | 1.0001 | 'all below 1.01' (no stated tolerance) |  |  |

#### CREMA-T03 — Fig. 1 (Distribution of sampling sites for the radiocarbon dates in case studies 1a … 1b … and 2)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Figure Comparison' row Figure 2 'Site distribution maps (3 panels)' |
| Location | vor, PDF p. 5 (printed p. 5) |
| Analysis type | visual (figure from archived posteriors or data) |
| Gate scope | conditional: in the leg only if L5 extends it to the figures (open) |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | visual (basis: verdicts-and-precision: figure verification is visual; the scientific content must match) |
| Pilot outcome | 'Visually identical' / 'Identical', but between the pilot's own pre-computed and fresh runs, not against the paper; run from v2.0.0 posteriors |
| Set | unchanged |
| Correction | comparison basis becomes the paper's figure, drawn from v1.0.0's archived posteriors; expected outcome unchanged (reproduced) |
| Printed value corrected | False |
| Repair class and status | CREMA-3 (iv); CREMA-2 (i): rnaturalearthhires installed unpinned at run time (Fig. 1 only). Status: no repair |
| Credit eligibility | pilot: historical (Q4); gate: eligible if run under the wrapper rule |
| Coverage | expected-untestable: False; comparison: visual |
| Expected outcome | REPRODUCED_VISUAL |
| Rulings | L5, L8 |
| Note | Needs rnaturalearthhires (ne_countries(scale = 10)); install it at build time pinned to a tag or recorded commit (Q6(c); amendment 3 §7(d)). |

#### CREMA-T04 — Fig. 2 (Performance of the hierarchical (a and b, simulations 1a and 1b) and the ICAR model (c, simulation 2) …)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Figure Comparison' row Figure 1 'Diffusion curves (3 panels)' |
| Location | vor, PDF p. 6 (printed p. 6) |
| Analysis type | visual (figure from archived posteriors or data) |
| Gate scope | conditional: in the leg only if L5 extends it to the figures (open) |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | visual (basis: verdicts-and-precision: figure verification is visual; the scientific content must match) |
| Pilot outcome | 'Visually identical' / 'Identical', but between the pilot's own pre-computed and fresh runs, not against the paper; run from v2.0.0 posteriors |
| Set | unchanged |
| Correction | comparison basis becomes the paper's figure, drawn from v1.0.0's archived posteriors; expected outcome unchanged (reproduced) |
| Printed value corrected | False |
| Repair class and status | CREMA-3 (iv); CREMA-2 (i): rnaturalearthhires installed unpinned at run time (Fig. 1 only). Status: no repair |
| Credit eligibility | pilot: historical (Q4); gate: eligible if run under the wrapper rule |
| Coverage | expected-untestable: False; comparison: visual |
| Expected outcome | REPRODUCED_VISUAL |
| Rulings | L5, L8 |
| Note | Drawn from the archived simulation posteriors in sim/results/. |

#### CREMA-T05 — Fig. 3 (Posterior predictive check of the fitted hierarchical Model on observed proportion SPD … in Japan (case study 1a))

| Field | Value |
|---|---|
| Pilot item | comparison report 'Figure Comparison' row Figure 3 'Japan posterior predictive check' |
| Location | vor, PDF p. 7 (printed p. 7) |
| Analysis type | visual (figure from archived posteriors or data) |
| Gate scope | conditional: in the leg only if L5 extends it to the figures (open) |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | visual (basis: verdicts-and-precision: figure verification is visual; the scientific content must match) |
| Pilot outcome | 'Visually identical' / 'Identical', but between the pilot's own pre-computed and fresh runs, not against the paper; run from v2.0.0 posteriors |
| Set | unchanged |
| Correction | comparison basis becomes the paper's figure, drawn from v1.0.0's archived posteriors; expected outcome unchanged (reproduced) |
| Printed value corrected | False |
| Repair class and status | CREMA-3 (iv); CREMA-2 (i): rnaturalearthhires installed unpinned at run time (Fig. 1 only). Status: no repair |
| Credit eligibility | pilot: historical (Q4); gate: eligible if run under the wrapper rule |
| Coverage | expected-untestable: False; comparison: visual |
| Expected outcome | REPRODUCED_VISUAL |
| Rulings | L5, L8 |

#### CREMA-T06 — Fig. 4 (Posterior predictive check of the fitted hierarchical Model on observed proportion SPD … in Britain (case study 1b))

| Field | Value |
|---|---|
| Pilot item | comparison report 'Figure Comparison' row Figure 4 'Britain posterior predictive check' |
| Location | vor, PDF p. 7 (printed p. 7) |
| Analysis type | visual (figure from archived posteriors or data) |
| Gate scope | conditional: in the leg only if L5 extends it to the figures (open) |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | visual (basis: verdicts-and-precision: figure verification is visual; the scientific content must match) |
| Pilot outcome | 'Visually identical' / 'Identical', but between the pilot's own pre-computed and fresh runs, not against the paper; run from v2.0.0 posteriors |
| Set | unchanged |
| Correction | comparison basis becomes the paper's figure, drawn from v1.0.0's archived posteriors; expected outcome unchanged (reproduced) |
| Printed value corrected | False |
| Repair class and status | CREMA-3 (iv); CREMA-2 (i): rnaturalearthhires installed unpinned at run time (Fig. 1 only). Status: no repair |
| Credit eligibility | pilot: historical (Q4); gate: eligible if run under the wrapper rule |
| Coverage | expected-untestable: False; comparison: visual |
| Expected outcome | REPRODUCED_VISUAL |
| Rulings | L5, L8 |

#### CREMA-T07 — Fig. 5 (Estimated proportion of cremation dates in Britain (case study 2))

| Field | Value |
|---|---|
| Pilot item | comparison report 'Figure Comparison' row Figure 5 'Burial cremation proportions' |
| Location | vor, PDF p. 7 (printed p. 7) |
| Analysis type | visual (figure from archived posteriors or data) |
| Gate scope | conditional: in the leg only if L5 extends it to the figures (open) |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | visual (basis: verdicts-and-precision: figure verification is visual; the scientific content must match) |
| Pilot outcome | 'Visually identical' / 'Identical', but between the pilot's own pre-computed and fresh runs, not against the paper; run from v2.0.0 posteriors |
| Set | unchanged |
| Correction | comparison basis becomes the paper's figure, drawn from v1.0.0's archived posteriors; expected outcome unchanged (reproduced) |
| Printed value corrected | False |
| Repair class and status | CREMA-3 (iv); CREMA-2 (i): rnaturalearthhires installed unpinned at run time (Fig. 1 only). Status: no repair |
| Credit eligibility | pilot: historical (Q4); gate: eligible if run under the wrapper rule |
| Coverage | expected-untestable: False; comparison: visual |
| Expected outcome | REPRODUCED_VISUAL |
| Rulings | L5, L8 |

### Pilot items excluded from the target list

| Pilot item | Reason | Ruling |
|---|---|---|
| Runtime comparison; Dockerfile issues | not published values |  |
| Figures S1–S6 (listed under 'Files', regenerated from v2.0.0) | not compared in the report; and v1.0.0's figures_esm.R loads simdata1.RData, which v1.0.0 does not contain (audit CREMA-3) |  |

### Notes

- The pilot report names the journal as the Journal of Archaeological Method and Theory; the paper is in the Journal of Archaeological Science 165, 105962.
- The paper's text cites the concept DOI 10.5281/zenodo.10782942; the AP-12 version record is 10.5281/zenodo.10782943.

## dye-et-al-2023

Dye, T.S., Buck, C.E., DiNapoli, R.J., & Philippe, A. (2023). Bayesian chronology construction and substance time. Journal of Archaeological Science, 153, 105765.

- **Selected (AP-12) version:** journal supplement mmc1 (listings) plus the authors' MCMC output
- `beads-1.csv`: sha256 `02cf52d4ace408b6329e69e7a0e4bd457084ae9605f2fa5eccc2abad20ab9051` (byte-identical in attempt-01 and attempt-02 (shakedown regression criterion); personal server, not a repository)
- **Pilot:** attempt-01, verdict SUCCESSFUL; executed run-analysis.R, a 476-line reproducer re-assembly of the supplement listings; no authors' file executed; audit findings DYE1-1, DYE1-2, DYE1-3.
- **Expected verdict:** PARTIAL. Of 13 targets, 11 are expected reproduced (DYE-T01, T03–T11, T13). DYE-T02 is a PAPER_ERROR and DYE-T12 cannot be compared because the published section 4 code does not run under any public release (fail-and-uplift). Coverage 11/13 = 0.846. One of the paper's two figures is not reproducible from the published code, so 'some analyses reproduced, others could not'.

### Targets

#### DYE-T01 — Text claim: BE1-Amethyst and BE1-Cowrie are likely descendants of BE3-Amber; 'their relation always satisfies the expected branching relation'

| Field | Value |
|---|---|
| Pilot item | comparison report 'Stable Solid Branching', rows BE3-Amber → BE1-Amethyst and BE3-Amber → BE1-Cowrie |
| Location | vor, PDF p. 17 (printed p. 16, ll. 372–374) |
| Analysis type | deterministic (section 7 oFD matrix) |
| Gate scope | in_gate: dye is a gate paper (L6 (c)) |
| Elements | published: 2; pilot_compared: 2 |
| Tolerance | exact (verbal claim read as probability 1 at 2 dp) (basis: pilot report; no pilot plan exists) |
| Pilot outcome | EXACT_MATCH |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | DYE1-3 (ii): no authors' file executed; the authors' listings were inlined into a 476-line reproducer script; DYE1-2 (iii, declared, result-identical, not a repair): bead list rebuilt by named construction; Q2 rules it class (iii). Status: gate run: the authors' transcribed files byte-identical to the deterministic transcription of supplement-1.pdf (Q8), mechanics in wrappers only (Q1) |
| Credit eligibility | pilot: ineligible: no authors' file executed (DYE1-3); gate: eligible under the wrapper-only rule |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | EXACT_MATCH |
| Rulings | L4 |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| BE3-Amber(oFD)BE1-Amethyst | always satisfies | 17 | 1.00 | EXACT_MATCH ('~1.0') | 1 | EXACT_MATCH |
| BE3-Amber(oFD)BE1-Cowrie | always satisfies | 17 | 1.00 | EXACT_MATCH ('~1.0') | 1 | EXACT_MATCH |

#### DYE-T02 — Text claim: BE1-Disc most likely descended from BE1-Cowrie; 'their relation satisfies the expected branching relation with a probability of 0.87'

| Field | Value |
|---|---|
| Pilot item | comparison report 'Stable Solid Branching', row BE1-Cowrie → BE1-Disc (pilot 'Published' 1.00) |
| Location | vor, PDF p. 17 (printed p. 16, ll. 374–376) |
| Analysis type | deterministic (section 7 oFD matrix) |
| Gate scope | in_gate: dye is a gate paper (L6 (c)) |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | exact at 2 dp (basis: pilot report) |
| Pilot outcome | EXACT_MATCH |
| Set | corrected |
| Printed value corrected | True |
| Corrected expected value | 1.00 at 2 dp (0.99967) |
| Evidence tier | 3: the authors' section 5 and 7 code, byte-identical to the transcription, on the authors' beads-1.csv, in an operator run on 2026-10-09 (evidence/l9-dye-section-07/): 0.999667. 0.87 is the Amethyst→Disc cell (0.867167). Shakedown attempt-02 (T06) gave the same values. |
| Ruling | shakedown ruling 2 (2026-10-04): PAPER_ERROR, after Shawn checked the typeset version of record |
| Caveat | attempt-02 ran section 7 with a declared input-path edit inside the authors' file (DYE2-1, class ii); the 2026-10-09 operator run kept the files byte-identical and moved the redirect into a wrapper, so tier 3 holds literally; L9 (b), ruled 2026-10-09, admits the operator run as tier-3 evidence |
| Repair class and status | DYE1-3 (ii): no authors' file executed; the authors' listings were inlined into a 476-line reproducer script; DYE1-2 (iii, declared, result-identical, not a repair): bead list rebuilt by named construction; Q2 rules it class (iii). Status: gate run: the authors' transcribed files byte-identical to the deterministic transcription of supplement-1.pdf (Q8), mechanics in wrappers only (Q1) |
| Credit eligibility | pilot: ineligible (DYE1-3; and compared against an unprinted value); gate: PAPER_ERROR records a discrepancy; it is not a reproduced target |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | PAPER_ERROR (reproduced 1.00 against printed 0.87) |
| Rulings | L9 |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| BE1-Cowrie(oFD)BE1-Disc | 0.87 | 17 | 1.00 | EXACT_MATCH (against 1.00, a value the paper does not print) | 1.00 (0.99967 unrounded) | PAPER_ERROR |

#### DYE-T03 — Supplement Table 2 (observed row(p)col from the first row of Bayliss et al. 2013, Table 7.18)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Table 2 — Row 1' |
| Location | supplement-1, PDF p. 38 (printed p. 38) |
| Analysis type | deterministic (post-processing of the archived MCMC output) |
| Gate scope | in_gate: dye is a gate paper (L6 (c)) |
| Elements | published: 16; pilot_compared: 16 |
| Tolerance | exact at the printed precision (2 dp) (basis: pilot report: 'match … exactly (to 2 decimal places, as reported)'; no pilot plan exists) |
| Pilot outcome | EXACT_MATCH on every listed cell |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | DYE1-3 (ii): no authors' file executed; the authors' listings were inlined into a 476-line reproducer script; DYE1-2 (iii, declared, result-identical, not a repair): bead list rebuilt by named construction; Q2 rules it class (iii). Status: gate run: the authors' transcribed files byte-identical to the deterministic transcription of supplement-1.pdf (Q8), mechanics in wrappers only (Q1) |
| Credit eligibility | pilot: ineligible: fail-and-uplift by Q2 (class iii); gate: eligible under the wrapper-only rule |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | EXACT_MATCH on every cell |
| Rulings | L4 |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| BE1-Reticella(p)BE1-Disc | 1 | 38 | 1 | EXACT_MATCH | 1 | EXACT_MATCH |
| BE1-Reticella(p)BE1-WhSpiral | 0.76 | 38 | 0.76 | EXACT_MATCH | 0.76 | EXACT_MATCH |
| BE1-Reticella(p)BE1-WoundSp | 0.54 | 38 | 0.54 | EXACT_MATCH | 0.54 | EXACT_MATCH |
| BE1-Reticella(p)BE1-Dghnt | 0.45 | 38 | 0.45 | EXACT_MATCH | 0.45 | EXACT_MATCH |
| BE1-Reticella(p)BE1-Amethyst | 0.45 | 38 | 0.45 | EXACT_MATCH | 0.45 | EXACT_MATCH |
| BE1-Reticella(p)BE1-Cowrie | 0.4 | 38 | 0.4 | EXACT_MATCH | 0.4 | EXACT_MATCH |
| BE1-Reticella(p)BE1-Orange | 0.03 | 38 | 0.03 | EXACT_MATCH | 0.03 | EXACT_MATCH |
| BE1-Reticella(p)BE2-c Metal | 0.01 | 38 | 0.01 | EXACT_MATCH | 0.01 | EXACT_MATCH |
| BE1-Melon(p)BE1-Disc | 1 | 38 | 1 | EXACT_MATCH | 1 | EXACT_MATCH |
| BE1-Melon(p)BE1-WhSpiral | 0.82 | 38 | 0.82 | EXACT_MATCH | 0.82 | EXACT_MATCH |
| BE1-Melon(p)BE1-WoundSp | 0.63 | 38 | 0.63 | EXACT_MATCH | 0.63 | EXACT_MATCH |
| BE1-Melon(p)BE1-Dghnt | 0.56 | 38 | 0.56 | EXACT_MATCH | 0.56 | EXACT_MATCH |
| BE1-Melon(p)BE1-Amethyst | 0.55 | 38 | 0.55 | EXACT_MATCH | 0.55 | EXACT_MATCH |
| BE1-Melon(p)BE1-Cowrie | 0.51 | 38 | 0.51 | EXACT_MATCH | 0.51 | EXACT_MATCH |
| BE1-Melon(p)BE1-Orange | 0.06 | 38 | 0.06 | EXACT_MATCH | 0.06 | EXACT_MATCH |
| BE1-Melon(p)BE2-c Metal | 0.03 | 38 | 0.03 | EXACT_MATCH | 0.03 | EXACT_MATCH |

#### DYE-T04 — Supplement Table 3 (observed row(p)col from the second row of Bayliss et al. 2013, Table 7.18)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Table 3 — Row 2' |
| Location | supplement-1, PDF p. 39 (printed p. 39) |
| Analysis type | deterministic (post-processing of the archived MCMC output) |
| Gate scope | in_gate: dye is a gate paper (L6 (c)) |
| Elements | published: 7; pilot_compared: 1 |
| Tolerance | exact at the printed precision (2 dp) (basis: pilot report: 'match … exactly (to 2 decimal places, as reported)'; no pilot plan exists) |
| Pilot outcome | EXACT_MATCH on every listed cell |
| Set | unchanged |
| Scope change | extended from 1 to 7 cells: the 6 printed zeros the pilot left out of its report (they were computed in its run.log) |
| Printed value corrected | False |
| Repair class and status | DYE1-3 (ii): no authors' file executed; the authors' listings were inlined into a 476-line reproducer script; DYE1-2 (iii, declared, result-identical, not a repair): bead list rebuilt by named construction; Q2 rules it class (iii). Status: gate run: the authors' transcribed files byte-identical to the deterministic transcription of supplement-1.pdf (Q8), mechanics in wrappers only (Q1) |
| Credit eligibility | pilot: ineligible: fail-and-uplift by Q2 (class iii); gate: eligible under the wrapper-only rule |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | EXACT_MATCH on every cell |
| Rulings | L3, L4 |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| BE1-DotReg(p)BE1-Disc | 0.19 | 39 | 0.19 | EXACT_MATCH | 0.19 | EXACT_MATCH |
| BE1-DotReg(p)BE1-WhSpiral | 0 | 39 |  | not listed in the pilot report | 0 | EXACT_MATCH |
| BE1-DotReg(p)BE1-WoundSp | 0 | 39 |  | not listed in the pilot report | 0 | EXACT_MATCH |
| BE1-DotReg(p)BE1-Dghnt | 0 | 39 |  | not listed in the pilot report | 0 | EXACT_MATCH |
| BE1-DotReg(p)BE1-Amethyst | 0 | 39 |  | not listed in the pilot report | 0 | EXACT_MATCH |
| BE1-DotReg(p)BE1-Cowrie | 0 | 39 |  | not listed in the pilot report | 0 | EXACT_MATCH |
| BE1-DotReg(p)BE1-Orange | 0 | 39 |  | not listed in the pilot report | 0 | EXACT_MATCH |

#### DYE-T05 — Supplement Table 4 (observed row(p)col from the third row of Bayliss et al. 2013, Table 7.18)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Table 4 — Row 3' |
| Location | supplement-1, PDF p. 40 (printed p. 40) |
| Analysis type | deterministic (post-processing of the archived MCMC output) |
| Gate scope | in_gate: dye is a gate paper (L6 (c)) |
| Elements | published: 5; pilot_compared: 5 |
| Tolerance | exact at the printed precision (2 dp) (basis: pilot report: 'match … exactly (to 2 decimal places, as reported)'; no pilot plan exists) |
| Pilot outcome | EXACT_MATCH on every listed cell |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | DYE1-3 (ii): no authors' file executed; the authors' listings were inlined into a 476-line reproducer script; DYE1-2 (iii, declared, result-identical, not a repair): bead list rebuilt by named construction; Q2 rules it class (iii). Status: gate run: the authors' transcribed files byte-identical to the deterministic transcription of supplement-1.pdf (Q8), mechanics in wrappers only (Q1) |
| Credit eligibility | pilot: ineligible: fail-and-uplift by Q2 (class iii); gate: eligible under the wrapper-only rule |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | EXACT_MATCH on every cell |
| Rulings | L4 |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| BE1-Koch20Ye(p)BE1-Disc | 0.99 | 40 | 0.99 | EXACT_MATCH | 0.99 | EXACT_MATCH |
| BE1-Koch20Ye(p)BE1-WhSpiral | 0.17 | 40 | 0.17 | EXACT_MATCH | 0.17 | EXACT_MATCH |
| BE1-Koch20Ye(p)BE1-WoundSp | 0.05 | 40 | 0.05 | EXACT_MATCH | 0.05 | EXACT_MATCH |
| BE1-Koch20Ye(p)BE1-Dghnt | 0.01 | 40 | 0.01 | EXACT_MATCH | 0.01 | EXACT_MATCH |
| BE1-Koch20Ye(p)BE1-Amethyst | 0.01 | 40 | 0.01 | EXACT_MATCH | 0.01 | EXACT_MATCH |

#### DYE-T06 — Supplement Table 5 (observed row(p)col from the fourth row of Bayliss et al. 2013, Table 7.18)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Table 5 — Row 4' |
| Location | supplement-1, PDF p. 41 (printed p. 41) |
| Analysis type | deterministic (post-processing of the archived MCMC output) |
| Gate scope | in_gate: dye is a gate paper (L6 (c)) |
| Elements | published: 12; pilot_compared: 12 |
| Tolerance | exact at the printed precision (2 dp) (basis: pilot report: 'match … exactly (to 2 decimal places, as reported)'; no pilot plan exists) |
| Pilot outcome | EXACT_MATCH on every listed cell |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | DYE1-3 (ii): no authors' file executed; the authors' listings were inlined into a 476-line reproducer script; DYE1-2 (iii, declared, result-identical, not a repair): bead list rebuilt by named construction; Q2 rules it class (iii). Status: gate run: the authors' transcribed files byte-identical to the deterministic transcription of supplement-1.pdf (Q8), mechanics in wrappers only (Q1) |
| Credit eligibility | pilot: ineligible: fail-and-uplift by Q2 (class iii); gate: eligible under the wrapper-only rule |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | EXACT_MATCH on every cell |
| Rulings | L4 |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| BE1-CylPen(p)BE1-Disc | 0.99 | 41 | 0.99 | EXACT_MATCH | 0.99 | EXACT_MATCH |
| BE1-CylPen(p)BE1-WhSpiral | 0.3 | 41 | 0.3 | EXACT_MATCH | 0.3 | EXACT_MATCH |
| BE1-CylPen(p)BE1-WoundSp | 0.12 | 41 | 0.12 | EXACT_MATCH | 0.12 | EXACT_MATCH |
| BE1-CylPen(p)BE1-Dghnt | 0.05 | 41 | 0.05 | EXACT_MATCH | 0.05 | EXACT_MATCH |
| BE1-Koch20Wh(p)BE1-Disc | 0.99 | 41 | 0.99 | EXACT_MATCH | 0.99 | EXACT_MATCH |
| BE1-Koch20Wh(p)BE1-WhSpiral | 0.27 | 41 | 0.27 | EXACT_MATCH | 0.27 | EXACT_MATCH |
| BE1-Koch20Wh(p)BE1-WoundSp | 0.1 | 41 | 0.1 | EXACT_MATCH | 0.1 | EXACT_MATCH |
| BE1-Koch20Wh(p)BE1-Dghnt | 0.04 | 41 | 0.04 | EXACT_MATCH | 0.04 | EXACT_MATCH |
| BE1-Koch49/50(p)BE1-Disc | 1 | 41 | 1 | EXACT_MATCH | 1 | EXACT_MATCH |
| BE1-Koch49/50(p)BE1-WhSpiral | 0.67 | 41 | 0.67 | EXACT_MATCH | 0.67 | EXACT_MATCH |
| BE1-Koch49/50(p)BE1-WoundSp | 0.46 | 41 | 0.46 | EXACT_MATCH | 0.46 | EXACT_MATCH |
| BE1-Koch49/50(p)BE1-Dghnt | 0.37 | 41 | 0.37 | EXACT_MATCH | 0.37 | EXACT_MATCH |

#### DYE-T07 — Supplement Table 6 (observed row(p)col from the fifth row of Bayliss et al. 2013, Table 7.18)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Table 6 — Row 5' |
| Location | supplement-1, PDF p. 42 (printed p. 42) |
| Analysis type | deterministic (post-processing of the archived MCMC output) |
| Gate scope | in_gate: dye is a gate paper (L6 (c)) |
| Elements | published: 6; pilot_compared: 6 |
| Tolerance | exact at the printed precision (2 dp) (basis: pilot report: 'match … exactly (to 2 decimal places, as reported)'; no pilot plan exists) |
| Pilot outcome | EXACT_MATCH on every listed cell |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | DYE1-3 (ii): no authors' file executed; the authors' listings were inlined into a 476-line reproducer script; DYE1-2 (iii, declared, result-identical, not a repair): bead list rebuilt by named construction; Q2 rules it class (iii). Status: gate run: the authors' transcribed files byte-identical to the deterministic transcription of supplement-1.pdf (Q8), mechanics in wrappers only (Q1) |
| Credit eligibility | pilot: ineligible: fail-and-uplift by Q2 (class iii); gate: eligible under the wrapper-only rule |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | EXACT_MATCH on every cell |
| Rulings | L4 |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| BE1-Koch34Wh(p)BE1-Disc | 0.93 | 42 | 0.93 | EXACT_MATCH | 0.93 | EXACT_MATCH |
| BE1-Koch34Wh(p)BE1-WhSpiral | 0.03 | 42 | 0.03 | EXACT_MATCH | 0.03 | EXACT_MATCH |
| BE1-Koch34Wh(p)BE1-Dghnt | 0 | 42 | 0 | EXACT_MATCH | 0 | EXACT_MATCH |
| BE1-Koch34Ye(p)BE1-Disc | 0.99 | 42 | 0.99 | EXACT_MATCH | 0.99 | EXACT_MATCH |
| BE1-Koch34Ye(p)BE1-WhSpiral | 0.16 | 42 | 0.16 | EXACT_MATCH | 0.16 | EXACT_MATCH |
| BE1-Koch34Ye(p)BE1-Dghnt | 0.01 | 42 | 0.01 | EXACT_MATCH | 0.01 | EXACT_MATCH |

#### DYE-T08 — Supplement Table 7 (observed row(p)col from the sixth row of Bayliss et al. 2013, Table 7.18)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Table 7 — Row 6' |
| Location | supplement-1, PDF p. 43 (printed p. 43) |
| Analysis type | deterministic (post-processing of the archived MCMC output) |
| Gate scope | in_gate: dye is a gate paper (L6 (c)) |
| Elements | published: 2; pilot_compared: 2 |
| Tolerance | exact at the printed precision (2 dp) (basis: pilot report: 'match … exactly (to 2 decimal places, as reported)'; no pilot plan exists) |
| Pilot outcome | EXACT_MATCH on every listed cell |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | DYE1-3 (ii): no authors' file executed; the authors' listings were inlined into a 476-line reproducer script; DYE1-2 (iii, declared, result-identical, not a repair): bead list rebuilt by named construction; Q2 rules it class (iii). Status: gate run: the authors' transcribed files byte-identical to the deterministic transcription of supplement-1.pdf (Q8), mechanics in wrappers only (Q1) |
| Credit eligibility | pilot: ineligible: fail-and-uplift by Q2 (class iii); gate: eligible under the wrapper-only rule |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | EXACT_MATCH on every cell |
| Rulings | L4 |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| BE1-Dot34(p)BE1-Disc | 0.99 | 43 | 0.99 | EXACT_MATCH | 0.99 | EXACT_MATCH |
| BE1-Dot34(p)BE1-Dghnt | 0.05 | 43 | 0.05 | EXACT_MATCH | 0.05 | EXACT_MATCH |

#### DYE-T09 — Supplement Table 8 (observed row(p)col from the seventh row of Bayliss et al. 2013, Table 7.18)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Table 8 — Row 7' |
| Location | supplement-1, PDF p. 44 (printed p. 44) |
| Analysis type | deterministic (post-processing of the archived MCMC output) |
| Gate scope | in_gate: dye is a gate paper (L6 (c)) |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | exact at the printed precision (2 dp) (basis: pilot report: 'match … exactly (to 2 decimal places, as reported)'; no pilot plan exists) |
| Pilot outcome | EXACT_MATCH on every listed cell |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | DYE1-3 (ii): no authors' file executed; the authors' listings were inlined into a 476-line reproducer script; DYE1-2 (iii, declared, result-identical, not a repair): bead list rebuilt by named construction; Q2 rules it class (iii). Status: gate run: the authors' transcribed files byte-identical to the deterministic transcription of supplement-1.pdf (Q8), mechanics in wrappers only (Q1) |
| Credit eligibility | pilot: ineligible: fail-and-uplift by Q2 (class iii); gate: eligible under the wrapper-only rule |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | EXACT_MATCH on every cell |
| Rulings | L4 |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| BE1-CylRound(p)BE1-Disc | 0.98 | 44 | 0.98 | EXACT_MATCH | 0.98 | EXACT_MATCH |

#### DYE-T10 — Supplement Table 9 (observed row(p)col from the eighth row of Bayliss et al. 2013, Table 7.18)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Table 9 — Row 8' |
| Location | supplement-1, PDF p. 45 (printed p. 45) |
| Analysis type | deterministic (post-processing of the archived MCMC output) |
| Gate scope | in_gate: dye is a gate paper (L6 (c)) |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | exact at the printed precision (2 dp) (basis: pilot report: 'match … exactly (to 2 decimal places, as reported)'; no pilot plan exists) |
| Pilot outcome | EXACT_MATCH on every listed cell |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | DYE1-3 (ii): no authors' file executed; the authors' listings were inlined into a 476-line reproducer script; DYE1-2 (iii, declared, result-identical, not a repair): bead list rebuilt by named construction; Q2 rules it class (iii). Status: gate run: the authors' transcribed files byte-identical to the deterministic transcription of supplement-1.pdf (Q8), mechanics in wrappers only (Q1) |
| Credit eligibility | pilot: ineligible: fail-and-uplift by Q2 (class iii); gate: eligible under the wrapper-only rule |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | EXACT_MATCH on every cell |
| Rulings | L4 |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| BE1-SegGlob(p)BE1-Disc | 0.99 | 45 | 0.99 | EXACT_MATCH | 0.99 | EXACT_MATCH |

#### DYE-T11 — Supplement Table 10 (observed row(p)col from the ninth row of Bayliss et al. 2013, Table 7.18)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Table 10 — Row 9' |
| Location | supplement-1, PDF p. 46 (printed p. 46) |
| Analysis type | deterministic (post-processing of the archived MCMC output) |
| Gate scope | in_gate: dye is a gate paper (L6 (c)) |
| Elements | published: 4; pilot_compared: 4 |
| Tolerance | exact at the printed precision (2 dp) (basis: pilot report: 'match … exactly (to 2 decimal places, as reported)'; no pilot plan exists) |
| Pilot outcome | EXACT_MATCH on every listed cell |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | DYE1-3 (ii): no authors' file executed; the authors' listings were inlined into a 476-line reproducer script; DYE1-2 (iii, declared, result-identical, not a repair): bead list rebuilt by named construction; Q2 rules it class (iii). Status: gate run: the authors' transcribed files byte-identical to the deterministic transcription of supplement-1.pdf (Q8), mechanics in wrappers only (Q1) |
| Credit eligibility | pilot: ineligible: fail-and-uplift by Q2 (class iii); gate: eligible under the wrapper-only rule |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | EXACT_MATCH on every cell |
| Rulings | L4 |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| BE1-Orange(p)BE1-Disc | 0.65 | 46 | 0.65 | EXACT_MATCH | 0.65 | EXACT_MATCH |
| BE1-WhSpiral(p)BE1-Disc | 0.38 | 46 | 0.38 | EXACT_MATCH | 0.38 | EXACT_MATCH |
| BE2-c Metal(p)BE1-Disc | 0.65 | 46 | 0.65 | EXACT_MATCH | 0.65 | EXACT_MATCH |
| BE1-Koch34Bl(p)BE1-Disc | 0.94 | 46 | 0.94 | EXACT_MATCH | 0.94 | EXACT_MATCH |

#### DYE-T12 — Fig. 3, occurrence plot of 72 interments (95% credible intervals)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Occurrence Plot (Paper Figure 7)' |
| Location | vor, PDF p. 14 (printed p. 13) |
| Analysis type | visual (supplement section 4 code) |
| Gate scope | in_gate: dye is a gate paper (L6 (c)) |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | visual (basis: verdicts-and-precision) |
| Pilot outcome | credited qualitatively ('72 interments confirmed') |
| Set | corrected |
| Correction | the pilot's result rests on its index shift c(3:5, 7, 9, 12:78) → c(2:4, 6, 8, 11:77) (DYE1-1, class iii). The published code fails under every public ArchaeoPhases release with read_oxcal() (1.5, 1.6, 1.8; it indexes column 78 of 77), so no routine version choice runs it. |
| Printed value corrected | False |
| Evidence tier | the authors' code and the public package releases' source (ruling 1's evidence); not a pipeline output |
| Ruling | shakedown ruling 1 (2026-10-04): fail-and-uplift; CANNOT_COMPARE stands; audit DYE1-1 already ruled |
| Repair class and status | DYE1-1 (iii): index shift, declared as an 'adjustment'. Status: a repair; recorded as uplift evidence (amendment 3 §8(b)) |
| Credit eligibility | pilot: ineligible: fail-and-uplift; gate: not creditable without the repair |
| Coverage | expected-untestable: False; comparison: visual |
| Expected outcome | CANNOT_COMPARE (the published code errors; fail-and-uplift) |
| Rulings | none |

#### DYE-T13 — Fig. 4, tempo plots of 23 bead types

| Field | Value |
|---|---|
| Pilot item | comparison report 'Tempo Plots (Paper Figure 8)' |
| Location | vor, PDF p. 16 (printed p. 15) |
| Analysis type | visual (supplement section 6 code) |
| Gate scope | in_gate: dye is a gate paper (L6 (c)) |
| Elements | published: 23; pilot_compared: 23 |
| Tolerance | visual: the scientific content must match; styling differences are not discrepancies (basis: verdicts-and-precision tolerance rules; the pilot checked 'layout and style') |
| Pilot outcome | credited qualitatively (23 panels, two shape patterns) |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | DYE1-3 (ii): no authors' file executed; the authors' listings were inlined into a 476-line reproducer script; DYE1-2 (iii, declared, result-identical, not a repair): bead list rebuilt by named construction; Q2 rules it class (iii). Status: gate run: the authors' transcribed files byte-identical to the deterministic transcription of supplement-1.pdf (Q8), mechanics in wrappers only (Q1) |
| Credit eligibility | pilot: ineligible (DYE1-2, DYE1-3); gate: eligible under the wrapper-only rule |
| Coverage | expected-untestable: False; comparison: visual |
| Expected outcome | REPRODUCED_VISUAL |
| Rulings | L4, L8 |

### Pilot items excluded from the target list

| Pilot item | Reason | Ruling |
|---|---|---|
| Stable Solid Branching rows BE3-Amber → BE1-Disc ('0.83') and BE1-Amethyst → BE1-Disc ('0.87') | no printed value: 0.83 appears nowhere in the paper or supplement, and the paper attaches 0.87 to Cowrie→Disc (DYE-T02). The pilot's 'Published' values were its own output. | L2 |
| Monochrome branching and BE1-Dghnt reticulation ('produced correct results', Verdict Justification) | nothing compared: no published value or relation was set against the output | L2 |
| OxCal replicability (Supplement Table 1) | scope limitation in the pilot; not compared |  |

### Notes

- The corpus store's vor.pdf is the White Rose accepted manuscript (eprints 197500), not the typeset article; printed page = PDF page − 1. Shawn checked the typeset version of record for the 0.87 passage on 2026-10-04 (shakedown ruling 2).

## herskind-riede-2024

Herskind, L.L.P., & Riede, F. (2024). A computational linguistic methodology for assessing semiotic structure in prehistoric art and the meaning of southern Scandinavian Mesolithic ornamentation. Journal of Archaeological Science, 165, 105969.

- **Selected (AP-12) version:** v2, 10.5281/zenodo.10801706
- `Herskind&Riede_S1.xlsx`: sha256 `d76b9d6328465658aa1582c5c8de0912f9167ff1f8c737bd7998d91fd5692030`
- `Herskind&Riede_S2.R`: sha256 `487a00a09db92b484dac136f13a5745a3a2ac699c3a01cfccf528d4d550a8720`
- `Herskind&Riede_S3.xlsx`: sha256 `1199acac5d1edb916dc4528d5e994295e206e798cb132e91c3be59cc9e328eed`
- **Pilot:** attempt-01, verdict SUCCESSFUL; executed run-analysis.R, a re-implementation of S2.R v1 (10.5281/zenodo.10623550); audit findings HER1-1, HER1-2, HER1-3, HER1-4.
- **Expected verdict:** SUCCESSFUL. Of 4 targets, 3 are expected reproduced (HER-T01, T02, T03); HER-T04 is a PAPER_ERROR in the published figure's hand-drawn layer, with the computed heatmap reproduced. Coverage 3/4 = 0.75; the paper's computational results all reproduce.

### Targets

#### HER-T01 — Supplementary Information S3 (deposit S3.xlsx): complete skipgram tables for observed frequency > 2, sorted by PMI

| Field | Value |
|---|---|
| Pilot item | comparison report 'Table Verification (S3.xlsx Reference)' |
| Location | deposit:Herskind&Riede_S3.xlsx |
| Analysis type | deterministic |
| Gate scope | in_gate: herskind is a gate paper (L6 (c)) |
| Elements | published: 291 rows; 1,601 numeric cells (2,329 non-empty); pilot_compared: 291 rows, every column, and the sort order |
| Tolerance | exact (row membership, order, every cell) (basis: pilot report: identical 'to full IEEE 754 double-precision') |
| Pilot outcome | EXACT_MATCH, 291/291 rows (max \|PMI diff\| 5.03 × 10⁻¹⁷) |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | HER1-4 (ii): re-implementation of S2.R v1; no authors' file executed; HER1-3 (iii, undeclared, result-identical): t <- 482 replaced by a count that equals 482 on the full data (Q3); HER1-1 (iv): v1 executed; AP-12 selects v2. Status: gate run: S2.R v2 byte-identical (md5 6760ccb3… = published) through a wrapper, as in shakedown attempt-02 (HER2-1, class i only) |
| Credit eligibility | pilot: ineligible: re-implementation (HER1-4) with a class (iii) edit (HER1-3, Q3); gate: eligible under the wrapper-only rule |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | EXACT_MATCH on every cell and the row order |
| Rulings | L4 |

Elements by reference: Herskind&Riede_S3.xlsx (Zenodo v2, 10.5281/zenodo.10801706), sha256 `1199acac5d1edb916dc4528d5e994295e206e798cb132e91c3be59cc9e328eed`. cell-identical to Zenodo v1's S3 (input-drift-herskind.md: 0 changed, added, or removed cells in all three sheets)

#### HER-T02 — Five S3 rows the pilot singled out as 'Top PMI Values', compared at the pilot table's 3 dp (Fig. 3 prints all five at 4 dp; those labels are HER-T03's)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Top PMI Values (Verification)' |
| Location | vor, PDF p. 5 (printed p. 5) |
| Analysis type | deterministic |
| Gate scope | in_gate: herskind is a gate paper (L6 (c)) |
| Elements | published: 5; pilot_compared: 5 |
| Tolerance | exact at the pilot table's 3 dp, after the same rounding (basis: amendment 3 §9: an unchanged deterministic target gives the pilot's value at the precision the pilot's comparison table recorded, after the same rounding. The pilot's 'Top PMI Values' table records 3 dp. No deposit value lies on a 3-dp rounding boundary, so the rounding rule cannot change the outcome. The 4-dp figure labels are tested under HER-T03 (corrected)) |
| Pilot outcome | EXACT_MATCH (5/5, against S3) |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | HER1-4 (ii): re-implementation of S2.R v1; no authors' file executed; HER1-3 (iii, undeclared, result-identical): t <- 482 replaced by a count that equals 482 on the full data (Q3); HER1-1 (iv): v1 executed; AP-12 selects v2. Status: gate run: S2.R v2 byte-identical (md5 6760ccb3… = published) through a wrapper, as in shakedown attempt-02 (HER2-1, class i only) |
| Credit eligibility | pilot: ineligible (as HER-T01); gate: eligible under the wrapper-only rule |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | EXACT_MATCH |
| Rulings | L4 |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| Quadrigram C1 C4 C5 C12, PMI (Fig. 3f, bar 1) | 7.9248 | 5 | 7.925 | EXACT_MATCH (against S3) | 7.925 | EXACT_MATCH |
| Trigram C4 C5 C12, PMI (Fig. 3d, bar 1) | 6.5751 | 5 | 6.575 | EXACT_MATCH (against S3) | 6.575 | EXACT_MATCH |
| Bigram I5 I13, PMI (Fig. 3b, bar 1) | 4.0985 | 5 | 4.099 | EXACT_MATCH (against S3) | 4.099 | EXACT_MATCH |
| Bigram C4 C12, PMI (Fig. 3b) | 3.2876 | 5 | 3.288 | EXACT_MATCH (against S3) | 3.288 | EXACT_MATCH |
| Bigram C12 C13, PMI (Fig. 3b) | 3.2876 | 5 | 3.288 | EXACT_MATCH (against S3) | 3.288 | EXACT_MATCH |

#### HER-T03 — Fig. 3 (six panels a–f of motif co-occurrence bars; 128 bars, each with a 4-dp PMI label)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Figure Comparison' rows 'Figure 3 (Maglemose patterns)', 'Figure 4 (Kongemose patterns)', 'Figure 5 (Ertebølle patterns)' |
| Location | vor, PDF p. 5 (printed p. 5) |
| Analysis type | deterministic (labels and bar order) and visual |
| Gate scope | in_gate: herskind is a gate paper (L6 (c)) |
| Elements | published: 6 panels; 128 labelled bars (21, 21, 23, 23, 20, 20); pilot_compared: no published figure; 'bar heights match table values' |
| Tolerance | exact on the PMI labels (4 dp) and bar order; visual on the rest (basis: verdicts-and-precision; no pilot plan exists) |
| Pilot outcome | 'Structural match' (credited), under per-period labels that match none of the paper's figures. The pilot's own plots map onto Fig. 3: bigram panels a and b (21 bars) agree; its trigram plots have 1 bar against 23; it made no quadrigram plots (audit HER1-2). |
| Set | corrected |
| Correction | mapped to the paper's Fig. 3 at its full scope (6 panels, 128 labels). The pilot's trigram and quadrigram credit is withdrawn. |
| Scope change | from the pilot's three unmatched 'period' figures to Fig. 3's six panels |
| Printed value corrected | False |
| Evidence tier | printed labels; every bar is an S3 row (tier 2 corroboration) |
| Ruling | audit Q3 (2026-10-05): attempt-01's Fig. 3 trigram and quadrigram credit withdrawn as unsound |
| Repair class and status | HER1-4 (ii): re-implementation of S2.R v1; no authors' file executed; HER1-3 (iii, undeclared, result-identical): t <- 482 replaced by a count that equals 482 on the full data (Q3); HER1-1 (iv): v1 executed; AP-12 selects v2; HER1-2 (iii candidate, undeclared): v1's literal head(…, 21) replaced by 'number of n-grams with observed > 9'. Status: gate run: S2.R v2 byte-identical (md5 6760ccb3… = published) through a wrapper, as in shakedown attempt-02 (HER2-1, class i only) |
| Credit eligibility | pilot: withdrawn (Q3); gate: eligible under the wrapper-only rule |
| Coverage | expected-untestable: False; comparison: exact (labels) |
| Expected outcome | EXACT_MATCH on all 128 labels and bar order |
| Rulings | L3 |

#### HER-T04 — Fig. 4 (bigram PMI heatmap over 49 motifs, with hand-drawn single-culture boxes)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Figure Comparison' row 'PMI heatmap' |
| Location | vor, PDF p. 6 (printed p. 6) |
| Analysis type | visual, with a deterministic cell check |
| Gate scope | in_gate: herskind is a gate paper (L6 (c)) |
| Elements | published: 1,176 displayed cells and their boxes; pilot_compared: internal matrix only ('Matrix values identical'); not the published figure |
| Tolerance | visual; the box layer checked cell by cell (basis: shakedown ruling 4 standing principle: a check's planned scope must cover the target's full tolerance) |
| Pilot outcome | 'Computational match' (credited) |
| Set | corrected |
| Correction | the published figure's hand-drawn box layer has two errors: a missing purple box (B1/B2) and a yellow box that should be red (C5/F13); 1,174 of 1,176 displayed cells agree |
| Printed value corrected | True |
| Evidence tier | 3: the authors' createResultTable() applied by the operator to all 1,176 cells (phase2-shakedown/t11-completion/) |
| Ruling | shakedown ruling 4 (2026-10-04): completed, then PAPER_ERROR |
| Repair class and status | HER1-4 (ii): re-implementation of S2.R v1; no authors' file executed; HER1-3 (iii, undeclared, result-identical): t <- 482 replaced by a count that equals 482 on the full data (Q3); HER1-1 (iv): v1 executed; AP-12 selects v2. Status: gate run: S2.R v2 byte-identical (md5 6760ccb3… = published) through a wrapper, as in shakedown attempt-02 (HER2-1, class i only) |
| Credit eligibility | pilot: ineligible (as HER-T01); gate: PAPER_ERROR is not a reproduced target |
| Coverage | expected-untestable: False; comparison: visual |
| Expected outcome | PAPER_ERROR (two box-layer cells) |
| Rulings | L9 |

### Pilot items excluded from the target list

| Pilot item | Reason | Ruling |
|---|---|---|
| 'Frequency Distribution (Table 1 Equivalent)' | tabulated, never compared: no published column. It silently differs from the printed Table 1 in six visible cells; the printed Table 1 has eight cells off by one (shakedown ruling 3, PAPER_ERROR), and the pilot's counts agree with S3. | L2 |
| 'PMI Summary Statistics by Period' | no published comparator; computed at quadrigram level, so it does not reproduce the bigram-level Table 2 (audit HER1-1) | L2 |

### Notes

- The methods state PMI as log₂ and 483 objects; the code and every published value use ln and t = 482 (shakedown plan exclusions). Not targets in the pilot's list.

## key-et-al-2024

Key, A., Eren, M.I., Bebber, M.R., Buchanan, B., Cortell-Nicolau, A., Martín-Ramos, C., de la Peña, P., Petrie, C.A., Proffitt, T., Robb, J., Michelaki, K.-E., & Jarić, I. (2024). Identifying accurate artefact morphological ranges using optimal linear estimation: Method validation, case studies, and code. Journal of Archaeological Science, 162, 105921 (doi:10.1016/j.jas.2023.105921).

- **Selected (AP-12) version:** journal supplements mmc1–mmc3 (scripts), mmc4.csv (header-only template), mmc5.docx; no input data
- `mmc1.zip (main OLE script)`: sha256 `ec2b4dd48b3aec3533cf5cc5a6e6befbe4836169d59fcf09acd38b43ae28b916`
- `mmc2.zip (randomised OLE script)`: sha256 `ff2688893753e6ba174d412a87afafce1e06e4ba2978cecb590dfbcb3f51e250`
- `mmc3.zip (resampling script)`: sha256 `76b516b91e88c312f0b7305684b98947a097d5ba0564d56e15ae68dbbda4ed67`
- **Pilot:** attempt-01, verdict PARTIAL; executed run-analysis.R, inlining OLE.test from mmc1 and re-implementing its loop; the authors' scripts never ran; audit findings KEY-1, KEY-2, KEY-3.
- **Expected verdict:** BLOCKED (coverage 0). All nine targets are untestable: KEY-T01 and T02 rest on reconstructed inputs (Q5(iii)), and KEY-T03 to T09 lack deposited data.

### Targets

#### KEY-T01 — Table 5, Olduvai Bed IV Cleavers rows (n = 134)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Table 5: Olduvai Bed IV Cleavers' |
| Location | vor, PDF p. 12 (printed p. 12) |
| Analysis type | deterministic (OLE, mmc1) |
| Gate scope | outside_gate: key is not a gate paper (L6 (c)) |
| Elements | published: 30; pilot_compared: 30 |
| Tolerance | exact at the printed precision (basis: pilot report ('All values should match exactly')) |
| Pilot outcome | 24 EXACT_MATCH and 6 WITHIN_PRECISION (credited); one of the six (Thickness Mean) rests on a mis-transcribed 42.3, so against the printed 42.2 it is exact |
| Set | corrected |
| Correction | every value rests on inputs the reproducer reconstructed from the Martín-Ramos (2022) thesis spreadsheet, so the target is expected-untestable; the reconstructed results are uplift evidence |
| Printed value corrected | False |
| Ruling | audit Q5(iii) (2026-10-05); amendment 3 §7(d), 'Verification aids and reconstructed inputs' |
| Repair class and status | KEY-1 (ii): OLE.test inlined and the loop re-implemented; the authors' scripts were kept but never executed; KEY-2: Mean (ii) re-implements the mean the authors' summary() prints; Extension % (v) is reproducer-computed; KEY-3 (v): inputs reconstructed from upstream datasets (Olduvai: Martín-Ramos 2022 thesis spreadsheet, subtype filter, decigrams to grams; Paleoindian: Buchanan and Hamilton 2021 ESM2, type filter, Width renamed Breadth). Status: no repair of the authors' code; the results rest on reconstructed inputs |
| Credit eligibility | pilot: excluded (Q5(iii)); gate: not creditable on reconstructed inputs |
| Coverage | expected-untestable: True; comparison: n/a |
| Expected outcome | EXPECTED_UNTESTABLE |
| Rulings | L14 |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| Olduvai Length — Mean | 142.9 | 12 | 142.9 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Length — Minimum | 93 | 12 | 93 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Length — OLE Minimum | 84.0 | 12 | 84.0 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Length — Maximum | 205 | 12 | 205 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Length — OLE Maximum | 216.3 | 12 | 216.3 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Length — OLE Range Extension % | 18.1 | 12 | 18.1 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Breadth — Mean | 87.6 | 12 | 87.6 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Breadth — Minimum | 57 | 12 | 57 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Breadth — OLE Minimum | 49.5 | 12 | 49.5 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Breadth — Maximum | 119 | 12 | 119 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Breadth — OLE Maximum | 126.8 | 12 | 126.8 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Breadth — OLE Range Extension % | 24.7 | 12 | 24.7 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Thickness — Mean | 42.2 | 12 | 42.2 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Olduvai Thickness — Minimum | 22 | 12 | 22 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Thickness — OLE Minimum | 19.5 | 12 | 19.5 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Thickness — Maximum | 60 | 12 | 60 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Thickness — OLE Maximum | 60.9 | 12 | 60.9 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Thickness — OLE Range Extension % | 8.9 | 12 | 9.1 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Olduvai Edge Length — Mean | 259.7 | 12 | 259.7 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Edge Length — Minimum | 20 | 12 | 20 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Edge Length — OLE Minimum | −10.6 | 12 | -10.6 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Edge Length — Maximum | 481 | 12 | 481 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Edge Length — OLE Maximum | 501.2 | 12 | 501.2 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Edge Length — OLE Range Extension % | 11.0 | 12 | 11.0 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Mass — Mean | 588.3 | 12 | 588.3 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Mass — Minimum | 252 | 12 | 251.5 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Olduvai Mass — OLE Minimum | 224.6 | 12 | 224.9 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Olduvai Mass — Maximum | 1269 | 12 | 1269.1 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Olduvai Mass — OLE Maximum | 1557.8 | 12 | 1557.8 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Olduvai Mass — OLE Range Extension % | 31.1 | 12 | 31.0 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |

#### KEY-T02 — Table 6, Paleoindian points (Clovis, Eastern Clovis, Folsom, Midland × length, breadth, thickness, mass)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Table 6: Paleoindian Projectile Points' |
| Location | vor, PDF p. 13 (printed p. 13) |
| Analysis type | deterministic (OLE, mmc1) |
| Gate scope | outside_gate: key is not a gate paper (L6 (c)) |
| Elements | published: 96; pilot_compared: 96 |
| Tolerance | exact at the printed precision (basis: pilot report ('All values should match exactly')) |
| Pilot outcome | 65 EXACT_MATCH, 21 WITHIN_PRECISION, 8 CANNOT_COMPARE, and 2 MAJOR_DISCREPANCY. The two majors rest on the pilot's own swap of two printed cells: the paper prints Midland Thickness 19.6 and Clovis Mass 3.1, not 3.1 and 19.6. Against the printed values, Clovis Mass is exact (3.1) and Midland Thickness differs by 1.6 points (21.2). |
| Set | corrected |
| Correction | every value rests on inputs reconstructed from Buchanan and Hamilton (2021), so the target is expected-untestable. The 'two inconsistent cells' that Q5(ii) sends to the paper-error protocol are an artefact of the pilot's swap (see ruling L16). |
| Printed value corrected | False |
| Ruling | audit Q5(iii); amendment 3 §7(d) |
| Repair class and status | KEY-1 (ii): OLE.test inlined and the loop re-implemented; the authors' scripts were kept but never executed; KEY-2: Mean (ii) re-implements the mean the authors' summary() prints; Extension % (v) is reproducer-computed; KEY-3 (v): inputs reconstructed from upstream datasets (Olduvai: Martín-Ramos 2022 thesis spreadsheet, subtype filter, decigrams to grams; Paleoindian: Buchanan and Hamilton 2021 ESM2, type filter, Width renamed Breadth). Status: no repair of the authors' code; the results rest on reconstructed inputs |
| Credit eligibility | pilot: excluded (Q5(iii)); gate: not creditable on reconstructed inputs |
| Coverage | expected-untestable: True; comparison: n/a |
| Expected outcome | EXPECTED_UNTESTABLE |
| Rulings | L14, L16 |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| Length (mm) Clovis — Mean | 67.3 | 13 | 67.3 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Length (mm) Clovis — Minimum | 21.9 | 13 | 21.9 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Length (mm) Clovis — OLE Minimum | 20.5 | 13 | 20.5 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Length (mm) Clovis — Maximum | 230.5 | 13 | 230.49 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Length (mm) Clovis — OLE Maximum | 243.4 | 13 | 243.4 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Length (mm) Clovis — OLE Range Extension % | 6.9 | 13 | 6.9 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Length (mm) E. Clovis — Mean | 54.2 | 13 | 54.2 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Length (mm) E. Clovis — Minimum | 27.5 | 13 | 27.5 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Length (mm) E. Clovis — OLE Minimum | 26.6 | 13 | NaN | CANNOT_COMPARE |  | EXPECTED_UNTESTABLE |
| Length (mm) E. Clovis — Maximum | 151.0 | 13 | 151 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Length (mm) E. Clovis — OLE Maximum | 211.0 | 13 | 211 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Length (mm) E. Clovis — OLE Range Extension % | 49.3 | 13 | NaN | CANNOT_COMPARE |  | EXPECTED_UNTESTABLE |
| Length (mm) Folsom — Mean | 40.5 | 13 | 40.5 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Length (mm) Folsom — Minimum | 16.7 | 13 | 16.65 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Length (mm) Folsom — OLE Minimum | 11.7 | 13 | 11.7 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Length (mm) Folsom — Maximum | 92.7 | 13 | 92.7 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Length (mm) Folsom — OLE Maximum | 105.8 | 13 | 105.8 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Length (mm) Folsom — OLE Range Extension % | 23.8 | 13 | 23.7 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Length (mm) Midland — Mean | 42.0 | 13 | 42 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Length (mm) Midland — Minimum | 19.1 | 13 | 19.1 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Length (mm) Midland — OLE Minimum | 14.5 | 13 | 14.5 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Length (mm) Midland — Maximum | 68.0 | 13 | 68 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Length (mm) Midland — OLE Maximum | 70.5 | 13 | 70.5 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Length (mm) Midland — OLE Range Extension % | 14.8 | 13 | 14.6 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Breadth (mm) Clovis — Mean | 27.1 | 13 | 27.1 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Breadth (mm) Clovis — Minimum | 13.0 | 13 | 13 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Breadth (mm) Clovis — OLE Minimum | 12.6 | 13 | NaN | CANNOT_COMPARE |  | EXPECTED_UNTESTABLE |
| Breadth (mm) Clovis — Maximum | 64.4 | 13 | 64.35 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Breadth (mm) Clovis — OLE Maximum | 66.3 | 13 | 66.3 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Breadth (mm) Clovis — OLE Range Extension % | 4.5 | 13 | NaN | CANNOT_COMPARE |  | EXPECTED_UNTESTABLE |
| Breadth (mm) E. Clovis — Mean | 24.5 | 13 | 24.5 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Breadth (mm) E. Clovis — Minimum | 11.9 | 13 | 11.89 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Breadth (mm) E. Clovis — OLE Minimum | 7.5 | 13 | 7.5 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Breadth (mm) E. Clovis — Maximum | 41.0 | 13 | 41 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Breadth (mm) E. Clovis — OLE Maximum | 46.7 | 13 | 46.7 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Breadth (mm) E. Clovis — OLE Range Extension % | 34.8 | 13 | 34.7 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Breadth (mm) Folsom — Mean | 20.4 | 13 | 20.4 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Breadth (mm) Folsom — Minimum | 10.9 | 13 | 10.86 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Breadth (mm) Folsom — OLE Minimum | 8.8 | 13 | 8.8 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Breadth (mm) Folsom — Maximum | 36.3 | 13 | 36.34 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Breadth (mm) Folsom — OLE Maximum | 40.1 | 13 | 40.1 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Breadth (mm) Folsom — OLE Range Extension % | 23.3 | 13 | 22.9 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Breadth (mm) Midland — Mean | 19.5 | 13 | 19.5 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Breadth (mm) Midland — Minimum | 12.5 | 13 | 12.51 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Breadth (mm) Midland — OLE Minimum | 10.4 | 13 | 10.4 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Breadth (mm) Midland — Maximum | 30.5 | 13 | 30.53 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Breadth (mm) Midland — OLE Maximum | 35.1 | 13 | 35.1 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Breadth (mm) Midland — OLE Range Extension % | 37.1 | 13 | 37 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Thickness (mm) Clovis — Mean | 7.2 | 13 | 7.2 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Thickness (mm) Clovis — Minimum | 3.0 | 13 | 3 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Thickness (mm) Clovis — OLE Minimum | 2.8 | 13 | NaN | CANNOT_COMPARE |  | EXPECTED_UNTESTABLE |
| Thickness (mm) Clovis — Maximum | 13.7 | 13 | 13.67 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Thickness (mm) Clovis — OLE Maximum | 14.9 | 13 | 14.9 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Thickness (mm) Clovis — OLE Range Extension % | 12.2 | 13 | NaN | CANNOT_COMPARE |  | EXPECTED_UNTESTABLE |
| Thickness (mm) E. Clovis — Mean | 6.8 | 13 | 6.8 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Thickness (mm) E. Clovis — Minimum | 3.0 | 13 | 3 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Thickness (mm) E. Clovis — OLE Minimum | 1.8 | 13 | 1.8 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Thickness (mm) E. Clovis — Maximum | 14 | 13 | 14 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Thickness (mm) E. Clovis — OLE Maximum | 19.4 | 13 | 19.4 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Thickness (mm) E. Clovis — OLE Range Extension % | 60.0 | 13 | 60 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Thickness (mm) Folsom — Mean | 4.2 | 13 | 4.2 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Thickness (mm) Folsom — Minimum | 2.3 | 13 | 2.27 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Thickness (mm) Folsom — OLE Minimum | 2.1 | 13 | 2.1 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Thickness (mm) Folsom — Maximum | 11.1 | 13 | 11.1 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Thickness (mm) Folsom — OLE Maximum | 15.0 | 13 | 15 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Thickness (mm) Folsom — OLE Range Extension % | 46.2 | 13 | 45.7 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Thickness (mm) Midland — Mean | 4.3 | 13 | 4.3 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Thickness (mm) Midland — Minimum | 3.0 | 13 | 3.04 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Thickness (mm) Midland — OLE Minimum | 2.9 | 13 | 2.9 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Thickness (mm) Midland — Maximum | 6.0 | 13 | 6 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Thickness (mm) Midland — OLE Maximum | 6.5 | 13 | 6.5 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Thickness (mm) Midland — OLE Range Extension % | 19.6 | 13 | 21.2 | MAJOR_DISCREPANCY |  | EXPECTED_UNTESTABLE |
| Mass (g) Clovis — Mean | 38.8 | 13 | 38.8 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Mass (g) Clovis — Minimum | 1.9 | 13 | 1.86 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Mass (g) Clovis — OLE Minimum | 1.4 | 13 | 1.4 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Mass (g) Clovis — Maximum | 196.2 | 13 | 196.2 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Mass (g) Clovis — OLE Maximum | 201.8 | 13 | 201.8 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Mass (g) Clovis — OLE Range Extension % | 3.1 | 13 | 3.1 | MAJOR_DISCREPANCY |  | EXPECTED_UNTESTABLE |
| Mass (g) E. Clovis — Mean | 10.2 | 13 | 10.2 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Mass (g) E. Clovis — Minimum | 2.6 | 13 | 2.58 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Mass (g) E. Clovis — OLE Minimum | 1.6 | 13 | 1.6 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Mass (g) E. Clovis — Maximum | 23.9 | 13 | 23.85 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Mass (g) E. Clovis — OLE Maximum | 27.6 | 13 | 27.6 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Mass (g) E. Clovis — OLE Range Extension % | 21.9 | 13 | 22.1 | WITHIN_PRECISION |  | EXPECTED_UNTESTABLE |
| Mass (g) Folsom — Mean | 4.3 | 13 | 4.3 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Mass (g) Folsom — Minimum | 0.5 | 13 | 0.5 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Mass (g) Folsom — OLE Minimum | −0.4 | 13 | -0.4 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Mass (g) Folsom — Maximum | 32.5 | 13 | 32.5 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Mass (g) Folsom — OLE Maximum | 57.9 | 13 | 57.9 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Mass (g) Folsom — OLE Range Extension % | 82.3 | 13 | 82.3 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Mass (g) Midland — Mean | 4.1 | 13 | 4.1 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Mass (g) Midland — Minimum | 1.2 | 13 | 1.2 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Mass (g) Midland — OLE Minimum | 1.0 | 13 | 1 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Mass (g) Midland — Maximum | 8.6 | 13 | 8.6 | EXACT_MATCH |  | EXPECTED_UNTESTABLE |
| Mass (g) Midland — OLE Maximum | 8.8 | 13 | NaN | CANNOT_COMPARE |  | EXPECTED_UNTESTABLE |
| Mass (g) Midland — OLE Range Extension % | 5.1 | 13 | NaN | CANNOT_COMPARE |  | EXPECTED_UNTESTABLE |

#### KEY-T03 — Table 2 (OLE validation, replica handaxes)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Scope Limitations' (not reproduced) |
| Location | vor, PDF p. 6 (printed p. 6) |
| Analysis type | deterministic or stochastic (see the paper) |
| Gate scope | outside_gate: key is not a gate paper (L6 (c)) |
| Elements | published: the whole item; pilot_compared: 0 |
| Tolerance | n/a (untestable) (basis: pilot report) |
| Pilot outcome | not reproduced: replica assemblage data not published |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | . Status: n/a |
| Credit eligibility | pilot: not credited; gate: not creditable |
| Coverage | expected-untestable: True; comparison: n/a |
| Expected outcome | UNTESTABLE (input data not available) |
| Rulings | L7 |

#### KEY-T04 — Table 3 (OLE validation, replica Archaic points)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Scope Limitations' (not reproduced) |
| Location | vor, PDF p. 7 (printed p. 7) |
| Analysis type | deterministic or stochastic (see the paper) |
| Gate scope | outside_gate: key is not a gate paper (L6 (c)) |
| Elements | published: the whole item; pilot_compared: 0 |
| Tolerance | n/a (untestable) (basis: pilot report) |
| Pilot outcome | not reproduced: replica assemblage data not published |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | . Status: n/a |
| Credit eligibility | pilot: not credited; gate: not creditable |
| Coverage | expected-untestable: True; comparison: n/a |
| Expected outcome | UNTESTABLE (input data not available) |
| Rulings | L7 |

#### KEY-T05 — Table 4 (validation summary, both replica assemblages)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Scope Limitations' (not reproduced) |
| Location | vor, PDF p. 12 (printed p. 12) |
| Analysis type | deterministic or stochastic (see the paper) |
| Gate scope | outside_gate: key is not a gate paper (L6 (c)) |
| Elements | published: the whole item; pilot_compared: 0 |
| Tolerance | n/a (untestable) (basis: pilot report) |
| Pilot outcome | not reproduced: replica assemblage data not published |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | . Status: n/a |
| Credit eligibility | pilot: not credited; gate: not creditable |
| Coverage | expected-untestable: True; comparison: n/a |
| Expected outcome | UNTESTABLE (input data not available) |
| Rulings | L7 |

#### KEY-T06 — Table 5, the eight case studies other than Olduvai

| Field | Value |
|---|---|
| Pilot item | comparison report 'Scope Limitations' (not reproduced) |
| Location | vor, PDF p. 12 (printed p. 12) |
| Analysis type | deterministic or stochastic (see the paper) |
| Gate scope | outside_gate: key is not a gate paper (L6 (c)) |
| Elements | published: the whole item; pilot_compared: 0 |
| Tolerance | n/a (untestable) (basis: pilot report) |
| Pilot outcome | not reproduced: data held by co-authors or in closed-access monographs |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | . Status: n/a |
| Credit eligibility | pilot: not credited; gate: not creditable |
| Coverage | expected-untestable: True; comparison: n/a |
| Expected outcome | UNTESTABLE (input data not available) |
| Rulings | L7 |

#### KEY-T07 — Table 7 (Iberian Mesolithic geometric microliths)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Scope Limitations' (not reproduced) |
| Location | vor, PDF p. 13 (printed p. 13) |
| Analysis type | deterministic or stochastic (see the paper) |
| Gate scope | outside_gate: key is not a gate paper (L6 (c)) |
| Elements | published: the whole item; pilot_compared: 0 |
| Tolerance | n/a (untestable) (basis: pilot report) |
| Pilot outcome | not reproduced: morphometric measurements not public; the randomised script (mmc2) sets no seed |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | . Status: n/a |
| Credit eligibility | pilot: not credited; gate: not creditable |
| Coverage | expected-untestable: True; comparison: n/a |
| Expected outcome | UNTESTABLE (input data not available) |
| Rulings | L7 |

#### KEY-T08 — Fig. 5 (validation results)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Scope Limitations' (not reproduced) |
| Location | vor, PDF p. 11 (printed p. 11) |
| Analysis type | deterministic or stochastic (see the paper) |
| Gate scope | outside_gate: key is not a gate paper (L6 (c)) |
| Elements | published: the whole item; pilot_compared: 0 |
| Tolerance | n/a (untestable) (basis: pilot report) |
| Pilot outcome | not reproduced: 'require the full dataset across all case studies' (the reason is wrong for Fig. 5, which uses the replica data) |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | . Status: n/a |
| Credit eligibility | pilot: not credited; gate: not creditable |
| Coverage | expected-untestable: True; comparison: n/a |
| Expected outcome | UNTESTABLE (input data not available) |
| Rulings | L7 |

#### KEY-T09 — Fig. 6 (sample size against range extension)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Scope Limitations' (not reproduced) |
| Location | vor, PDF p. 14 (printed p. 14) |
| Analysis type | deterministic or stochastic (see the paper) |
| Gate scope | outside_gate: key is not a gate paper (L6 (c)) |
| Elements | published: the whole item; pilot_compared: 0 |
| Tolerance | n/a (untestable) (basis: pilot report) |
| Pilot outcome | not reproduced: 'require the full dataset across all case studies' |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | . Status: n/a |
| Credit eligibility | pilot: not credited; gate: not creditable |
| Coverage | expected-untestable: True; comparison: n/a |
| Expected outcome | UNTESTABLE (input data not available) |
| Rulings | L7 |

### Notes

- The pilot's citation is wrong: the paper has twelve authors, and its DOI is 10.1016/j.jas.2023.105921, not 10.1016/j.jas.2024.105921.
- Table 1 and Figs 1–4, 7, and 8 are not in the pilot's list (not mentioned in its report) and are not added. Fig. 7's inputs were available to the pilot.
- The paper gives no formula for OLE Range Extension %; the pilot's formula is its own reconstruction. From printed inputs it reproduces all 5 Olduvai values and 6 of 16 Table 6 values at 1 dp, and every printed value lies in the band that rounding of the printed inputs allows.

## marwick-2025

Marwick, B. (2025). Is archaeology a science? Insights and imperatives from 10,000 articles and a year of reproducibility reviews. Journal of Archaeological Science, 180, 106281 (doi:10.1016/j.jas.2025.106281).

- **Selected (AP-12) version:** 1.3 (GitHub tag 1.3 = c9332a8), 10.5281/zenodo.15603267
- **Deposit archive:** sha256 `7cf98aa59ecf24851ac0db001a4a60cdf8d02be61d75412a41596ec9cb63bb85`; audit downloads (2026-10-04); a re-download on 2026-10-09 returned HTTP 504 and was not retried
- `analysis/paper/paper.qmd`: sha256 `313247bce36a1a4a03f1090ed25cab69dc1c25bb37306f98f6ba2ec97facdcca`
- `renv.lock`: sha256 `4cbafb587ea6bda3c158e6affef001695e8db98c2f400d5d31bd4bb029573f23`
- `Dockerfile`: sha256 `93dd7ffd893d6174720ae9ae3fd78dfea8d69f641a05e8a3b9cc799d1ee5bc49`
- `analysis/paper/paper.docx`: sha256 `f548ec4b24173b34e0122a1e7e500a42e2341edc324c85a64f52b0ac8e40350f` (the authors' rendered output at 1.3; corroborates MAR-T04 to T06)
- **Pilot:** attempt-01, verdict SUCCESSFUL; executed GitHub main 652e542 (8 commits past 1.3); audit findings MAR-1, MAR-2.
- **Expected verdict:** SUCCESSFUL (provisional on L17). Version 1.3 is expected to give the printed values for MAR-T01 to T08, as its own rendered paper.docx shows for W, p, and PC1. The dynamic figures are expected to reproduce, Fig. 4 among them, regenerated by the render (L11 (a)). Fig. 2 (MAR-T10) depends on L17: outside the gate under (a); counted under (b) or (c).

### Targets

#### MAR-T01 — Number of articles analysed

| Field | Value |
|---|---|
| Pilot item | comparison report 'Key Statistics' row 'Total articles' |
| Location | vor, PDF p. 2 |
| Analysis type | deterministic |
| Gate scope | in_gate: marwick is a gate paper (L6 (c)) |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | exact at the printed precision (basis: pilot report; no pilot plan exists) |
| Pilot outcome | EXACT_MATCH |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | MAR-1 (iv): GitHub main 652e542 executed, 8 commits past the AP-12 version 1.3, including a changed Shannon diversity calculation (group_by(id, journal_name), rendered at attempt-01 outputs/paper.html line 904); MAR-2 (i): no code modifications (self-reported). Status: no repair; the gate re-runs version 1.3 (Q4) |
| Credit eligibility | pilot: historical (Q4: pilot verdicts preserved as artefacts); executed a non-AP-12 version; gate: eligible when version 1.3 runs unmodified |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | EXACT_MATCH |
| Rulings | none |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| Total articles | 9697 | 2 | 9,697 | EXACT_MATCH | 9697 | EXACT_MATCH |

#### MAR-T02 — Number of journals

| Field | Value |
|---|---|
| Pilot item | comparison report 'Key Statistics' row 'Journals' |
| Location | vor, PDF p. 2 |
| Analysis type | deterministic |
| Gate scope | in_gate: marwick is a gate paper (L6 (c)) |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | exact at the printed precision (basis: pilot report; no pilot plan exists) |
| Pilot outcome | EXACT_MATCH |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | MAR-1 (iv): GitHub main 652e542 executed, 8 commits past the AP-12 version 1.3, including a changed Shannon diversity calculation (group_by(id, journal_name), rendered at attempt-01 outputs/paper.html line 904); MAR-2 (i): no code modifications (self-reported). Status: no repair; the gate re-runs version 1.3 (Q4) |
| Credit eligibility | pilot: historical (Q4: pilot verdicts preserved as artefacts); executed a non-AP-12 version; gate: eligible when version 1.3 runs unmodified |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | EXACT_MATCH |
| Rulings | none |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| Journals | 20 journals | 2 | 20 | EXACT_MATCH | 20 journals | EXACT_MATCH |

#### MAR-T03 — Time span of the sample

| Field | Value |
|---|---|
| Pilot item | comparison report 'Key Statistics' row 'Time span' |
| Location | vor, PDF p. 2 |
| Analysis type | deterministic |
| Gate scope | in_gate: marwick is a gate paper (L6 (c)) |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | exact at the printed precision (basis: pilot report; no pilot plan exists) |
| Pilot outcome | EXACT_MATCH |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | MAR-1 (iv): GitHub main 652e542 executed, 8 commits past the AP-12 version 1.3, including a changed Shannon diversity calculation (group_by(id, journal_name), rendered at attempt-01 outputs/paper.html line 904); MAR-2 (i): no code modifications (self-reported). Status: no repair; the gate re-runs version 1.3 (Q4) |
| Credit eligibility | pilot: historical (Q4: pilot verdicts preserved as artefacts); executed a non-AP-12 version; gate: eligible when version 1.3 runs unmodified |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | EXACT_MATCH |
| Rulings | none |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| Time span | 1975–2025 | 2 | 1975-2025 | EXACT_MATCH | 1975–2025 | EXACT_MATCH |

#### MAR-T04 — Kendall's coefficient of concordance (Wt)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Key Statistics' row 'Kendall's W' |
| Location | vor, PDF p. 3 |
| Analysis type | deterministic |
| Gate scope | in_gate: marwick is a gate paper (L6 (c)) |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | exact at the printed precision (basis: pilot report; no pilot plan exists) |
| Pilot outcome | EXACT_MATCH (against '~0.70', a value the paper does not print) |
| Set | corrected |
| Correction | the pilot recorded the published value as '~0.70 (moderate to strong)'; the version of record (and the preprint) print 0.64. The pilot's 0.7 from version 652e542 is a discrepancy, not an exact match. |
| Printed value corrected | False |
| Evidence tier | printed value; corroborated by the 1.3 deposit's own rendered analysis/paper/paper.docx (git blob 9a919391848cc91f0affa1547622509fd94554a6 at tag 1.3 = c9332a8; sha256 f548ec4b24173b34e0122a1e7e500a42e2341edc324c85a64f52b0ac8e40350f; fetched 2026-10-09), which reads Wt 0.64 |
| Ruling | audit Q4 (re-run at 1.3); the mis-recorded published value is a new finding of this draft (L12) |
| Repair class and status | MAR-1 (iv): GitHub main 652e542 executed, 8 commits past the AP-12 version 1.3, including a changed Shannon diversity calculation (group_by(id, journal_name), rendered at attempt-01 outputs/paper.html line 904); MAR-2 (i): no code modifications (self-reported). Status: no repair; the gate re-runs version 1.3 (Q4) |
| Credit eligibility | pilot: historical (Q4: pilot verdicts preserved as artefacts); executed a non-AP-12 version; gate: eligible when version 1.3 runs unmodified |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | EXACT_MATCH |
| Rulings | L12 |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| Kendall's W | 0.64 | 3 | 0.7 | EXACT_MATCH (against '~0.70', a value the paper does not print) | 0.64 | EXACT_MATCH |

#### MAR-T05 — Kendall's test p-value

| Field | Value |
|---|---|
| Pilot item | comparison report 'Key Statistics' row 'Kendall's p-value' |
| Location | vor, PDF p. 3 |
| Analysis type | deterministic |
| Gate scope | in_gate: marwick is a gate paper (L6 (c)) |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | exact at the printed 3 significant figures (basis: pilot report; no pilot plan exists) |
| Pilot outcome | MINOR discrepancy ('data revision', untested) |
| Set | corrected |
| Correction | the pilot's discrepancy came from running version 652e542, whose Shannon index enters the Kendall test; it was put down to a 'data revision', which no evidence supports |
| Printed value corrected | False |
| Evidence tier | printed value; corroborated by the 1.3 deposit's own rendered analysis/paper/paper.docx (git blob 9a919391848cc91f0affa1547622509fd94554a6 at tag 1.3 = c9332a8; sha256 f548ec4b24173b34e0122a1e7e500a42e2341edc324c85a64f52b0ac8e40350f; fetched 2026-10-09), which reads 2.67 x 10-06 |
| Ruling | audit Q4: marwick's 'data revision' explanation recorded as untested; re-run at 1.3 |
| Repair class and status | MAR-1 (iv): GitHub main 652e542 executed, 8 commits past the AP-12 version 1.3, including a changed Shannon diversity calculation (group_by(id, journal_name), rendered at attempt-01 outputs/paper.html line 904); MAR-2 (i): no code modifications (self-reported). Status: no repair; the gate re-runs version 1.3 (Q4) |
| Credit eligibility | pilot: historical (Q4: pilot verdicts preserved as artefacts); executed a non-AP-12 version; gate: eligible when version 1.3 runs unmodified |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | EXACT_MATCH |
| Rulings | none |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| Kendall's p-value | 2.67 × 10−06 | 3 | 4.08 × 10⁻⁷ | MINOR discrepancy ('data revision', untested) | 2.67 × 10−06 | EXACT_MATCH |

#### MAR-T06 — Variance captured by PC1

| Field | Value |
|---|---|
| Pilot item | comparison report 'Key Statistics' row 'PC1 variance explained' |
| Location | vor, PDF p. 4 |
| Analysis type | deterministic |
| Gate scope | in_gate: marwick is a gate paper (L6 (c)) |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | exact at the printed precision (basis: pilot report; no pilot plan exists) |
| Pilot outcome | N/A ('Not specified in paper text') |
| Set | corrected |
| Correction | the pilot said the value is not printed; the version of record prints 71 % (text p. 4; Fig. 4 axis 'PC1 (71%)'). The pilot's 72 % from version 652e542 differs. |
| Printed value corrected | False |
| Evidence tier | printed value; corroborated by the 1.3 deposit's own rendered analysis/paper/paper.docx (git blob 9a919391848cc91f0affa1547622509fd94554a6 at tag 1.3 = c9332a8; sha256 f548ec4b24173b34e0122a1e7e500a42e2341edc324c85a64f52b0ac8e40350f; fetched 2026-10-09), which reads 71% |
| Ruling | new finding of this draft (L12) |
| Repair class and status | MAR-1 (iv): GitHub main 652e542 executed, 8 commits past the AP-12 version 1.3, including a changed Shannon diversity calculation (group_by(id, journal_name), rendered at attempt-01 outputs/paper.html line 904); MAR-2 (i): no code modifications (self-reported). Status: no repair; the gate re-runs version 1.3 (Q4) |
| Credit eligibility | pilot: historical (Q4: pilot verdicts preserved as artefacts); executed a non-AP-12 version; gate: eligible when version 1.3 runs unmodified |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | EXACT_MATCH |
| Rulings | L12 |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| PC1 variance explained | 71 % | 4 | 72% | N/A ('Not specified in paper text') | 71 % | EXACT_MATCH |

#### MAR-T07 — Manuscripts given reproducibility reviews

| Field | Value |
|---|---|
| Pilot item | comparison report 'Key Statistics' row 'Reproducibility reviews' |
| Location | vor, PDF p. 7 |
| Analysis type | deterministic |
| Gate scope | in_gate: marwick is a gate paper (L6 (c)) |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | exact at the printed precision (basis: pilot report; no pilot plan exists) |
| Pilot outcome | EXACT_MATCH |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | MAR-1 (iv): GitHub main 652e542 executed, 8 commits past the AP-12 version 1.3, including a changed Shannon diversity calculation (group_by(id, journal_name), rendered at attempt-01 outputs/paper.html line 904); MAR-2 (i): no code modifications (self-reported). Status: no repair; the gate re-runs version 1.3 (Q4) |
| Credit eligibility | pilot: historical (Q4: pilot verdicts preserved as artefacts); executed a non-AP-12 version; gate: eligible when version 1.3 runs unmodified |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | EXACT_MATCH |
| Rulings | L13 |
| Note | possibly typed prose rather than inline R (the pilot's environment.md annotates only the article and journal counts as inline R) |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| Reproducibility reviews | 25 manuscripts | 7 | 25 | EXACT_MATCH | 25 manuscripts | EXACT_MATCH |

#### MAR-T08 — Reviewed manuscripts published in JAS

| Field | Value |
|---|---|
| Pilot item | comparison report 'Key Statistics' row 'Published from reviews' |
| Location | vor, PDF p. 7 |
| Analysis type | deterministic |
| Gate scope | in_gate: marwick is a gate paper (L6 (c)) |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | exact at the printed precision (basis: pilot report; no pilot plan exists) |
| Pilot outcome | EXACT_MATCH |
| Set | unchanged |
| Printed value corrected | False |
| Repair class and status | MAR-1 (iv): GitHub main 652e542 executed, 8 commits past the AP-12 version 1.3, including a changed Shannon diversity calculation (group_by(id, journal_name), rendered at attempt-01 outputs/paper.html line 904); MAR-2 (i): no code modifications (self-reported). Status: no repair; the gate re-runs version 1.3 (Q4) |
| Credit eligibility | pilot: historical (Q4: pilot verdicts preserved as artefacts); executed a non-AP-12 version; gate: eligible when version 1.3 runs unmodified |
| Coverage | expected-untestable: False; comparison: exact |
| Expected outcome | EXACT_MATCH |
| Rulings | L13 |
| Note | as MAR-T07 |

| Element | Printed | Page | Pilot value | Pilot outcome | Expected | Expected outcome |
|---|---|---|---|---|---|---|
| Published from reviews | 11 have been published | 7 | 11 | EXACT_MATCH | 11 have been published | EXACT_MATCH |

#### MAR-T09 — Fig. 1 (distributions of article characteristics, with Fanelli and Glänzel's comparison boxplots)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Figure Comparison' row 'Fig 1 fig-compare-other-fields' (dynamic) |
| Location | vor, PDF p. 3 |
| Analysis type | visual |
| Gate scope | in_gate: marwick is a gate paper (L6 (c)) |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | visual (basis: verdicts-and-precision) |
| Pilot outcome | credited; compared against the repository's paper.docx at 652e542, not the published article |
| Set | corrected |
| Correction | comparison basis becomes the version of record. The pilot's figure differs from the published one in content, not styling: in the 'Diversity of references' panel the archaeology boxplot covers a different, narrower range of Shannon index values, which moves it against the three comparison boxplots. 652e542 changed the Shannon calculation; version 1.3 computes it as published. The pilot figure stays as the historical baseline (studies/open-science-compliance/outputs/marwick-2025/reproduction/attempt-01/outputs/paper.html, embedded image 0) |
| Printed value corrected | False |
| Evidence tier | visual comparison of the pilot's embedded figure with the version of record (PDF p. 3); found by Astra's review of PR #10 at 9b66683 (2026-10-09), B1, and confirmed by Claude the same day |
| Ruling | L4 (a): unchanged requires the pilot's outcome and value; L8 (a) covers styling only, not content |
| Repair class and status | MAR-1 (iv): GitHub main 652e542 executed, 8 commits past the AP-12 version 1.3, including a changed Shannon diversity calculation (group_by(id, journal_name), rendered at attempt-01 outputs/paper.html line 904); MAR-2 (i): no code modifications (self-reported). Status: no repair; the gate re-runs version 1.3 (Q4) |
| Credit eligibility | pilot: historical (Q4); gate: eligible when version 1.3 runs unmodified |
| Coverage | expected-untestable: False; comparison: visual |
| Expected outcome | REPRODUCED_VISUAL |
| Rulings | L4, L8 |

#### MAR-T10 — Fig. 2 (Bayesian generalised additive model (GAM) trends over time; static image in paper.qmd)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Figure Comparison' row 'Fig 3 fig-change-over-time' (static PNG include) and 'Fig 2 fig-change-over-time_from_V1_1' (dynamic) |
| Location | vor, PDF p. 4 |
| Analysis type | visual |
| Gate scope | in_gate: marwick is a gate paper (L6 (c)); L17 (open) may place it outside the gate |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | visual (basis: verdicts-and-precision) |
| Pilot outcome | credited; compared against the repository's paper.docx at 652e542, not the published article |
| Set | corrected |
| Correction | the pilot credited a static include as 'Identical' and an added chart with no published counterpart (never output by its render). Q4 withdrew the Fig. 2 credit. The published image is produced by the deposit's supplement-GAMS-details.qmd, which the Dockerfile's render does not run. |
| Printed value corrected | False |
| Repair class and status | MAR-1 (iv): GitHub main 652e542 executed, 8 commits past the AP-12 version 1.3, including a changed Shannon diversity calculation (group_by(id, journal_name), rendered at attempt-01 outputs/paper.html line 904); MAR-2 (i): no code modifications (self-reported). Status: no repair; the gate re-runs version 1.3 (Q4) |
| Credit eligibility | pilot: historical (Q4); gate: eligible when version 1.3 runs unmodified |
| Coverage | expected-untestable: False; comparison: visual |
| Expected outcome | RULING NEEDED (L17) |
| Rulings | L11, L17 |

#### MAR-T11 — Fig. 3 (journal variation, panels A–E, and the Borda Count consensus ranking, panel F)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Figure Comparison' row 'Fig 5 fig-variation-by-journal' (dynamic) |
| Location | vor, PDF p. 5 |
| Analysis type | visual |
| Gate scope | in_gate: marwick is a gate paper (L6 (c)) |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | visual (basis: verdicts-and-precision) |
| Pilot outcome | credited; compared against the repository's paper.docx at 652e542, not the published article |
| Set | corrected |
| Correction | comparison basis becomes the version of record. The pilot's figure differs from the published one in content, not styling: panel E (diversity of references) orders the journals differently, and panel F's Borda ranking changes. For example, the Journal of Archaeological Science is third in the pilot and fifth in the version of record, Antiquity fifth against third, and Geoarchaeology thirteenth against ninth. 652e542 changed the Shannon calculation; version 1.3 computes it as published. The pilot figure stays as the historical baseline (studies/open-science-compliance/outputs/marwick-2025/reproduction/attempt-01/outputs/paper.html, embedded image 2) |
| Printed value corrected | False |
| Evidence tier | visual comparison of the pilot's embedded figure with the version of record (PDF p. 5); found by Astra's review of PR #10 at 9b66683 (2026-10-09), B1, and confirmed by Claude the same day |
| Ruling | L4 (a): unchanged requires the pilot's outcome and value; L8 (a) covers styling only, not content |
| Repair class and status | MAR-1 (iv): GitHub main 652e542 executed, 8 commits past the AP-12 version 1.3, including a changed Shannon diversity calculation (group_by(id, journal_name), rendered at attempt-01 outputs/paper.html line 904); MAR-2 (i): no code modifications (self-reported). Status: no repair; the gate re-runs version 1.3 (Q4) |
| Credit eligibility | pilot: historical (Q4); gate: eligible when version 1.3 runs unmodified |
| Coverage | expected-untestable: False; comparison: visual |
| Expected outcome | REPRODUCED_VISUAL |
| Rulings | L4, L8 |

#### MAR-T12 — Fig. 4 (PCA biplot of journal means; axis labels PC1 (71%), PC2 (18%))

| Field | Value |
|---|---|
| Pilot item | comparison report 'Figure Comparison' row 'Fig 4 fig-pca' (static PNG include) |
| Location | vor, PDF p. 6 |
| Analysis type | visual |
| Gate scope | in_gate: marwick is a gate paper (L6 (c)) |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | visual (basis: verdicts-and-precision) |
| Pilot outcome | credited; compared against the repository's paper.docx at 652e542, not the published article |
| Set | corrected |
| Correction | the pilot credited a hand-edited static PNG as 'Identical'. The render regenerates plot_pca_means.svg; at 652e542 it read PC1 (72%) and PC2 (19%), against the printed 71% and 18%. |
| Printed value corrected | False |
| Repair class and status | MAR-1 (iv): GitHub main 652e542 executed, 8 commits past the AP-12 version 1.3, including a changed Shannon diversity calculation (group_by(id, journal_name), rendered at attempt-01 outputs/paper.html line 904); MAR-2 (i): no code modifications (self-reported). Status: no repair; the gate re-runs version 1.3 (Q4) |
| Credit eligibility | pilot: historical (Q4); gate: eligible when version 1.3 runs unmodified |
| Coverage | expected-untestable: False; comparison: visual |
| Expected outcome | REPRODUCED_VISUAL, against the figure the render regenerates (plot_pca_means.svg); the static PNG include is never credited (L11 (a)) |
| Rulings | L11 |

#### MAR-T13 — Fig. 5 (summary of reproducibility reviews for JAS, panels A–E)

| Field | Value |
|---|---|
| Pilot item | comparison report 'Figure Comparison' row 'Fig 6 fig-aer-summary' (dynamic) |
| Location | vor, PDF p. 7 |
| Analysis type | visual |
| Gate scope | in_gate: marwick is a gate paper (L6 (c)) |
| Elements | published: 1; pilot_compared: 1 |
| Tolerance | visual (basis: verdicts-and-precision) |
| Pilot outcome | credited; compared against the repository's paper.docx at 652e542, not the published article |
| Set | unchanged |
| Correction | comparison basis becomes the version of record |
| Printed value corrected | False |
| Repair class and status | MAR-1 (iv): GitHub main 652e542 executed, 8 commits past the AP-12 version 1.3, including a changed Shannon diversity calculation (group_by(id, journal_name), rendered at attempt-01 outputs/paper.html line 904); MAR-2 (i): no code modifications (self-reported). Status: no repair; the gate re-runs version 1.3 (Q4) |
| Credit eligibility | pilot: historical (Q4); gate: eligible when version 1.3 runs unmodified |
| Coverage | expected-untestable: False; comparison: visual |
| Expected outcome | REPRODUCED_VISUAL |
| Rulings | L8 |

### Pilot items excluded from the target list

| Pilot item | Reason | Ruling |
|---|---|---|
| 'Fig 7 fig-checklist' (static PNG include) = Fig. 6 | an infographic checklist with no computed content | L2 |
| Runtime, Dockerfile assessment, cross-reference resolution | not published values |  |

### Notes

- The pilot's PC1 'not specified' and Kendall's W '~0.70' were never read from the paper: its environment.md lists the published W only as 'moderate to strong'.
- The rendered repository text at 652e542 also differs from the version of record in prose (journals selected by '2022 Impact Factor' against the VoR's h-indices).
- Other values printed in the VoR that the pilot did not list (303 papers, 70 %, n = 28,871, the Fig. 2 pseudo-R² labels, 63 %, 28 %, 7 %) are outside the pilot's list and are not added (the denominator is preserved).
