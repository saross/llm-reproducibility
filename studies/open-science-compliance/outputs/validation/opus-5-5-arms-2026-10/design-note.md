# Opus 5.5 validation arms — design note (2026-10-04)

**Status: RULED 2026-10-04 (Shawn).** Q1: **all three** effort levels
(medium, high, xhigh). Q2–Q7 adopted as drafted, including the pre-declared
use of results (Q4). API gate stage 1 (the P4 probe) is approved; the arms
need a separate approval after P4 passes. The governed-edit freeze (Q6)
runs from the P4 launch until the last arm is committed.

**P4 attempt 1 (2026-10-04, `wf_656e2363-534`): aborted before any spend.**
The agent definition, created mid-session, was not loaded (register F-018;
0 tokens). The args guard passed. P4 re-runs from a fresh session under the
same approval, with args rebuilt at that session's HEAD.

## Purpose

At the D4 step, the registrant held selection so that `claude-opus-5-5`
(Opus 5.5) could be validated first
(`../gates-ruling-2026-10-04/ruling.md`). Over the registered arms, the rule
selects `claude-opus-5` at effort `high`. Opus 5.5 is newer and cheaper
($4 / $20 per million tokens, against $5 / $25). It is benchmarked here
through the **same gates**:

- stability ≥ 0.90;
- majority-vote concordance ≥ 0.90 on the beyond-instrument (BI)-excluded
  statistic, with all 150 items reported.

Using it for the census needs an amendment.

Two questions:

1. **Eligibility.** Does any Opus 5.5 effort level clear both gates?
2. **Effort → cost and quality, measured** (the registrant's 2026-08-17
   rider). Opus 5.5's effort levels are recalibrated (its default is
   `medium`), so they are measured, not presumed.

## Design

- **Arms:** `claude-opus-5-5` at the effort levels the registrant rules (Q1),
  each a full arm: 5 pilot papers × 3 runs = 15 scoring spawns plus 15
  per-item reconciliation spawns (Haiku 4.5 at `low`).
- **Inputs identical to the registered arms**, verified 2026-10-04:
  - every evidence pack path and sha256 the args builder derives today equals
    those in the 2026-08-17 opus-5-high spawn prompts;
  - every pilot `vor.pdf` matches its corpus-manifest sha256;
  - the paper PDF stays the sole paper source, with supplements withheld
    (`fair-benchmark-arm.workflow.js:100`), exactly as the registered arms
    were scored.

  The supplement-inclusive census input
  (`protocol/supplements-as-inputs-2026-10-02.md`) applies at the
  pre-census check, not here.
- **Same instrument and agent text:**
  - FAIR instrument v2.1 and guide v1.1, pushed with receipts;
  - agent definition `fair-assessor-opus-5-5` v1.2, which is the opus-5 text
    with only the model identity changed (`.claude/agents/`, registered in
    `manifest.yaml`).

## Arm identity and provenance

- Directories: `arm-opus-5-5-<effort>/` under this directory. Effort is
  part of arm identity (plan decision log, 2026-08-17).
- Args are built fresh per arm at launch by
  `scripts/build-benchmark-args.py opus-5-5 --effort <level>` (v1.4). The
  builder refuses a tree with modified tracked files, and `launch_commit`
  is HEAD.
- The assembler (v1.6) parses the injected Provenance line, so effort and
  launch commit are artefact-derived.

## Contract (delta over the D3 run contract)

D3 hardenings H1–H15 carry over verbatim, except:

- **H1 order.** Arms run sequentially with a per-arm hard stop, in the
  order `high` (like-for-like with the rule's current answer) → `medium` →
  `xhigh` (Q2).
- **H4 wire, re-based per request.** F-013 (ruled 2026-10-04) moved the
  spend metric to a per-request count.
  - The per-request opus-5 baselines are 2.10M (xhigh) and 2.16M (high)
    per 30-spawn arm (the replayed `usage_per_request`).
  - Wire: **4.5M per-request contract-metric tokens per arm** (about 2× the
    baseline).
  - The remediation-scaled rule carries over.
- **H13.** The gate statistics for these arms are derived by the analysis
  tool (v1.2) **and** by the committed blinded H13 script
  (`../h13-rederivation-2026-10-04/h13-rederive.py`), run unchanged as a
  second, independent implementation. Any disagreement goes to the
  registrant; the verifier never wins by default.
- **H7 probe, strictly first (Q3).**
  - **P4:** one Opus 5.5 scoring spawn (marwick-2025, run 1, at the first
    arm's effort) with its reconciliation.
  - It must pass before any arm launches: receipt gate clean;
    `model_id` = `claude-opus-5-5`; `agent_version` =
    `fair-assessor-opus-5-5 v1.2`; schema-valid payload; and assembler v1.6
    identity parsing on a real 2.1.289 FAIR transcript (the F-015 fix's
    first live use).
  - The probe spawn is not counted in any arm.

- **Args integrity, added before launch (2026-10-04).** Workflow v1.7 and
  args builder v1.5 port the reproduction lane's `args_checksum` guard. The
  roughly 9 KB of args (schema included) travel inline in the Workflow call,
  so the workflow recomputes the checksum over what arrived and refuses to
  start on any difference. No prompt text changes: scoring prompts are
  byte-identical to v1.6 runs, bar the launch commit.
  `tests/test_benchmark_args_checksum.py` covers it.

## Comparability residuals

- **R1 (carried): served effort.** The pin is a requested value; spawn
  metadata carries no effort field. The served-effort signal is the
  per-spawn thinking-block and output-token contrast across the levels.
- **R2 (new): harness version.** The registered arms ran on Claude Code
  2.1.233; this block runs on 2.1.289. Since 2.1.288 a spawn also receives
  the session's last user message, relayed verbatim
  (`[Workflow harness — user request]`; register F-015). Mitigation: launch
  each arm from a turn whose last user message is a neutral go-ahead, and
  record it in the run notes.
- **R3 (new): model generation.** Opus 5.5 is a different model, not a
  re-run of `claude-opus-5`. Its results bear on Opus 5.5's eligibility
  only. They do not revise any registered arm's figures.

## Governance and pre-declared use of results (Q4)

This is exploratory validation, recorded in this note and the plan's
decision log, with **no OSF amendment before the run**. **Pre-declared now,
before any data:**

1. An Opus 5.5 configuration is eligible if and only if it clears both
   gates under the 2026-10-04 ruling: stability ≥ 0.90, and majority-vote
   concordance ≥ 0.90 on the BI-excluded statistic.
2. Selection then applies amendment 1's rule unchanged across **all**
   eligible configurations, registered and Opus 5.5 alike:
   - the cheapest at the published prices in force at selection;
   - cost measured per request on the benchmark spawns;
   - agreement differences inside the confidence interval are not grounds
     for selection.
3. If an Opus 5.5 configuration is selected, its use enters amendment 3
   (running-list item 5) and is lodged before census scoring. If none
   qualifies, the registered-arm answer (`claude-opus-5` at `high`) stands
   for confirmation.

## Cost estimate (API gate input)

The estimate applies Opus 5.5's published prices to the measured opus-5
per-request token profiles (`../gates-ruling-2026-10-04/selection-cost.json`).
Cache writes are a floor of about $6–7 per arm whatever the effort.

| Arm | Estimated scoring cost | With Haiku reconciliation |
|---|---|---|
| medium | about $11.1 (output extrapolated; no measurement) | about $12.2 |
| high | about $12.9 | about $14.0 |
| xhigh | about $14.7 | about $15.8 |
| P4 probe | about $1 | about $1 |

All three arms plus the probe come to about **$43** API-equivalent; high plus
medium plus the probe to about **$27**. The run is billed through the Max
plan. Opus 5.5's token use per effort level is unmeasured, so treat these as
order-of-magnitude figures. The H4 wire, being token-denominated, is the hard
stop.

## Artefact set (per arm; contract H6 carried)

- `arm-opus-5-5-<effort>/run-record.json`, assembled by v1.6, with
  per-request usage and `provenance_pinned`;
- `run-<N>/<slug>.json` score payloads;
- `reconciliation/` report and log slices;
- one commit per arm.

## Questions for the registrant (delta pre-run review)

- **Q1.** Which effort levels: high + medium, or all three?
- **Q2.** Order: `high` first, then the others?
- **Q3.** Run the P4 probe strictly first?
- **Q4.** Adopt the pre-declared use of results above?
- **Q5.** The H4 wire of 4.5M per-request tokens per arm?
- **Q6.** The governed-edit freeze (H2) across the whole block, with no
  instrument, guide, definition, schema, or manifest-hash edit until the
  last arm is committed?
- **Q7.** Launch hygiene (R2): a neutral go-ahead as the last user message
  before each launch?
