# H13 — operator comparison and audit (2026-10-04)

**What this is.** This is the operator's record for D3 run-contract item
H13 (`wiki/planning/instrument-clarification-plan.md`, "Summary
verification pass"): the gate statistics were re-derived in a fresh context
before the registrant's gates ruling. The re-derivation was approved by
Shawn under the API gate (1 Opus 5.5 agent, real-time). It was run by a
fresh general-purpose agent with no shared context, blinded from every
earlier derivation of these figures.

- `report.md`, `h13-rederive.py`, and `h13-results.json` are the agent's own
  outputs. The harness blocked the agent from writing `report.md` itself
  ("Subagents should return findings as text"). The operator saved the
  content of that blocked write verbatim, extracted programmatically from
  the agent's transcript, not retyped.
- This file is the operator's.

## Blinding audit

Every tool-call input in the agent's transcript (26 calls, full text) was
scanned for the blinded paths:

- the 2026-10-03 concordance directory;
- run records and reconciliation directories;
- the effort-study summary and design note;
- the analysis tool and its tests;
- `wiki/`, `manifest.yaml`, and amendment 2;
- the E8-v2 worksheet and adjudication log;
- git history.

The only matches are in the blocked `report.md` write, which lists those
paths as *not opened*. No blinded file was opened, listed, or grepped.
The agent's own access log (`report.md` §5) agrees.

## Comparison with the analysis tool

| Statistic | Result |
|---|---|
| Stability, 6 arms | **identical** to `analyse-benchmark-disagreements.py` v1.2 (`e8-v2-concordance-2026-10-03/*/summary.json`) |
| Concordance, 6 arms × {all items, BI excluded}, with over/under split | **identical** to the tool in all 12 cells under the agent's **reading C** (majority vote of three runs against the reference) |

The computation is therefore confirmed, and there is no arithmetic
disagreement to adjudicate.

**The interpretive disagreement is the finding.** Working from the
registered text alone, the agent took reading **A** (four-way unanimity: all
three runs agree *and* equal the reference) as its primary reading of
amendment 1 §3's "concordance floor … (same statistic)". It also reported
readings B (per-run agreement) and C (majority vote).

- **The tool's majority-vote reading is not newly chosen.** The 2026-08-03
  benchmark summary defined concordance as "majority-vote item agreement
  … (same statistic, per amendment §3)"
  (`benchmark-2026-08/benchmark-summary.md`, lines 14–17).
- **That reading's figures are already public.** Amendment 2, lodged on
  OSF, reports that cycle's concordance figures (0.773/0.807/0.820),
  which were computed that way.
- **But no registered text defines it.**

Under the contract's disagreement rule (a third derivation or operator
adjudication, never verifier-wins), this goes to the registrant. The
reading shapes the gates ruling.

| Reading (stability-passing arms only) | All 150 items | BI excluded (141) |
|---|---|---|
| A — four-way unanimity | none | fable-5 |
| B — per-run, pooled | fable-5 | fable-5, opus-5, opus-5-high |
| C — majority vote (tool; amendment 2 record) | fable-5 | fable-5, opus-5, opus-5-high |

## Other anomalies the agent reported (none changes a gate outcome)

- **fable-5 run 1, key-et-al-2024, data section:** marked
  `available: false` but carries item scores. The sensitivity is reported in
  `report.md` §4.5; no outcome changes.
- **Model identifier:** both opus arms record `claude-opus-5[1m]` against
  the pinned `claude-opus-5`. This was already known and recorded in the
  2026-08 benchmark summary.
- **Instrument version:** payloads record FAIR instrument v2.1, while
  registration §7.1 names v2.0. The step is the D1 governed-edit window
  (instrument v2.1) lodged with amendment 2.
