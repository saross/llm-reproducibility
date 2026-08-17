# Effort study — summary (2026-08-17)

**Status: all approved arms complete; spend closed.** Exploratory
instrument-development study under the operator's rulings of 2026-08-17
(design note in this directory; plan-of-record decision log). Stability
figures are single-arm recounts replicating the registered derivation;
the fresh-context re-derivation (D3 contract H13) remains due before any
gates ruling, and **concordance stays deliberately uncomputed pending
E8 v2**.

## Stability × effort × model (the datapoints)

| Arm | Effort channel | Stability | Gate ≥ 0.90 | Contract-metric tokens | Compliance |
|---|---|---|---|---|---|
| sonnet-5 @ high | pinned | 122/150 = 0.813 | below | 5,664,843 | clean first pass |
| sonnet-5 @ xhigh | session-attested (D3) | 128/150 = 0.853 | below | 6,216,252 | clean after verifier adjudication |
| sonnet-5 @ max | pinned | 130/150 = 0.867 | below | 21,245,484 | 4 items re-run; 14 dead attempts; key r2 × 3 |
| opus-5 @ high | pinned | **143/150 = 0.953** | **PASS** | 5,138,631 | clean first pass |
| opus-5 @ xhigh | session-attested (D3) | **143/150 = 0.953** | **PASS** | 5,068,770 | clean first pass |
| fable-5 @ xhigh (context) | session-attested (D3) | 142/150 = 0.947 | PASS | 7,100,984 | 2 contract-mandated re-runs |

## Findings

1. **Effort does not rescue the cheapest arm.** Sonnet's effort-response
   is monotone but shallow — 0.813 → 0.853 → 0.867 — never approaching
   the gate, with the high→xhigh step (+6 items) essentially free and the
   xhigh→max step (+2 items) costing 3.4× plus compliance degradation
   (F-008–F-011).
2. **Opus is effort-insensitive on this task.** Identical stability
   (143/150), near-identical cost, and near-identical pack-utilisation at
   high and xhigh. **opus-5 @ high is now the cheapest known passing
   configuration** — at roughly sonnet-xhigh cost.
3. **Effort→cost (the operator's measurand):** within a model, high ≈
   xhigh in cost; max triples-plus it. The presumed effort→cost
   monotonicity holds only at the top step, and the top step's stability
   return is marginal.
4. **Max effort degrades harness compliance (sonnet):** per-response
   output blow-outs (F-008, fixed by the 128K cap — confirmed causally),
   exploratory boundary Globs (F-010, verifier pattern-vs-path split
   OPEN), and one status-OK-without-scores payload (F-011, caught by C9
   as designed). The high arms of both models ran clean first pass.
5. **Citation integrity is clean study-wide:** across all six arms'
   payloads checked (2,700 sub-principle scores), zero unresolvable
   pack_refs and zero A1-rule violations (`check-payload-quality.py`).
6. **Pack-utilisation separates models, not efforts:** opus grounds ~80%
   of scores in rung-(i) pack evidence at either effort; sonnet sits at
   47–57% (climbing with effort); fable 60%. Quality-of-grounding tracks
   the stability ranking.
7. **Dispute concentration:** dye-et-al-2023's supplement-only-deposit
   boundary is the least stable judgement at every sonnet effort level
   (F2/F3/F4 flip as a block); opus@high's 7 disputes concentrate on
   R1.x code-side judgements for key-et-al-2024.

## Selection implication (for D4, not a ruling)

The "cheapest eligible arm" candidate set now includes **opus-5 @ high**:
it passes stability at ~18% less token cost than fable@xhigh and roughly
sonnet-xhigh cost, with the study's best evidence-grounding profile.
Sonnet is not rescued at any effort. No deficiency appeared in either
opus record, so **opus@max remains off** per the operator's ruling.
Concordance across ALL arms in one pass (once E8 v2 lands) remains the
outstanding accuracy leg before any gates ruling.

## Spend (contract-metric tokens, study arms only)

sonnet@max 21.25M + sonnet@high 5.66M + opus@high 5.14M + probes P3/P5
(~0.1M) ≈ **32.2M tokens** against the operator's continuation
authorisations (12M initial wire, tripped and adjudicated; completion +
two high arms explicitly approved).
