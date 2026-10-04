# Gates ruling and D4 arm choice (2026-10-04)

**Registrant:** Shawn Ross. **Recorded by:** Claude (Opus 5.5).

**Inputs:**

- the six-arm concordance against E8-v2 (`../e8-v2-concordance-2026-10-03/summary.md`);
- the H13 blinded fresh-context re-derivation
  (`../h13-rederivation-2026-10-04/operator-comparison.md`).

H13 confirmed every figure the tool produced, so this ruling is about rules,
not arithmetic.

## Ruling 1: the concordance statistic is majority-vote item agreement

Amendment 1 §3 sets "a concordance floor of at least 0.90 (same statistic)
against the pilot reference scores" but does not say how three runs meet one
reference score. H13's blinded reader took four-way unanimity as the literal
reading (reading A). The analysis tool uses the majority of the three runs
against the reference (reading C).

**Ruled: C.** The reasons:

- it is the operationalisation in force before these data;
- the 2026-08-03 benchmark summary defined concordance this way
  (`../benchmark-2026-08/benchmark-summary.md`, lines 14–17);
- amendment 2, as lodged, reports that cycle's figures computed this way
  (0.773/0.807/0.820);
- reading A counts every unstable item as a concordance miss as well, so
  instability is penalised twice, although it has a gate of its own.

Per-run agreement (reading B) gives the same gate outcomes here.

The public clarification is erratum-log Entry 5, queued for amendment 3.

## Ruling 2: the BI-excluded concordance is admissible as the gate statistic

The 9 beyond-instrument (BI) items are reference scores that rest on
evidence the benchmark spawns were deliberately not given (`input`, all 9).
Four of them also rest on a principle adopted at adjudication that
instrument v2.1 does not state (`rule`). The convention is in the
adjudication log, "Beyond-instrument (BI) tags".

**Ruled: admissible. Both figures are reported.** The reasons:

- the criterion is defined by arm-independent properties;
- the tags were fixed on 2026-10-02, before concordance was computed on
  2026-10-03;
- an arm cannot fairly be graded on evidence it was denied.

**Stated limits:**

- The E8-v2 adjudication was unblinded: the worksheet showed per-arm
  majorities while the tags were assigned.
- Exclusion changes opus-5's eligibility.
- opus-5 at high clears with no room to spare (127/141 = 0.901; one more
  miss fails it).

The deviation is lodged publicly with amendment 3 (erratum-log Entry 5).

**Closing the gap:** census spawns will receive published supplements
(`protocol/supplements-as-inputs-2026-10-02.md`). The pre-census check runs
the selected arm on the five pilots with supplements, which tests the BI
items with their evidence in hand.

## Gate outcomes under the ruling

Both gates require at least 0.90. Concordance is reading C.

| Arm | Stability | Concordance, BI excluded (gate) | Concordance, all 150 (reported) | Eligible |
|---|---|---|---|---|
| sonnet-5 (xhigh) | 128/150 = 0.853 | 121/141 = 0.858 | 123/150 = 0.820 | no |
| sonnet-5 (high) | 122/150 = 0.813 | 125/141 = 0.887 | 127/150 = 0.847 | no |
| sonnet-5 (max) | 130/150 = 0.867 | 126/141 = 0.894 | 128/150 = 0.853 | no |
| opus-5 (xhigh) | 143/150 = 0.953 | 130/141 = 0.922 | 134/150 = 0.893 | **yes** |
| opus-5 (high) | 143/150 = 0.953 | 127/141 = 0.901 | 131/150 = 0.873 | **yes** |
| fable-5 (xhigh) | 142/150 = 0.947 | 133/141 = 0.943 | 137/150 = 0.913 | yes, but not selectable |

Under amendment 1 §3, fable-5 "cannot be selected for the census under any
outcome" on price. It stays the cross-model comparator.

## D4 arm choice: computed by the registered rule

The rule is "Among eligible models the cheapest scores the census". Cost is
evaluated "at selection time from the provider's published per-token
prices", and "agreement differences inside the confidence interval are
pre-declared not to be grounds for selection" (amendment 1 §3).

**Prices in force at selection.** These come from the claude-api skill's
model table, cached 2026-09-25, in USD per million tokens (input / output):

- claude-sonnet-5: 2 / 10;
- claude-opus-5: 5 / 25;
- claude-fable-5: 10 / 50.

The ordering is unchanged since amendment 1. `claude-opus-5` is listed as
Active.

**Model:** opus-5 is the only eligible, selectable model.

**Effort.** Effort is part of arm identity (plan decision log, 2026-08-17).
Cost was counted once per request (`selection-cost.py`, the F-013 method)
over each arm's 15 scoring spawns:

| opus-5 | Output tokens | Cache writes | Cache reads | API-equivalent cost (15 scorings) |
|---|---|---|---|---|
| xhigh | 390,165 | 1,208,294 | 4,302,199 | $19.46 |
| high | 249,033 | 1,413,452 | 4,409,257 | **$17.27** |

`high` is about 11% cheaper. It produces 36% fewer output tokens, although
its per-entry contract metric was slightly higher (F-013). This is the
empirical effort-to-cost datapoint required by the registrant's 2026-08-17
rider. The 15 Haiku reconciliation spawns cost $1.06–1.08 in either arm.

**Selection by rule: `claude-opus-5` at effort `high`.**

~~**Status: awaiting the registrant's confirmation.**~~ **Registrant
(2026-10-04): selection HELD. Validate Opus 5.5 first.** `claude-opus-5-5`
is to be benchmarked as a new arm through the same gates, and selection then
proceeds under an amendment. The `claude-opus-5` @ `high` computation above
stands as the rule's answer over the registered arms. After selection, under
amendment 1's within-phase ordering, the registered regression gate runs on
the selected configuration with both lanes pinned, and the census follows.

## Open questions recorded with the selection

- **Newer models.** Opus 5.5 (`claude-opus-5-5`, $4 / $20) and Fable 5.1
  are now published. The registered pins are `claude-opus-5` and
  `claude-fable-5`. Moving the census to Opus 5.5 would need its own
  benchmark arm through the same gates, plus an amendment. Comparing Fable
  5.1 with Opus 5.5 is open as exploratory work.
- **F-013** is still awaiting the registrant's ruling. This selection
  already uses the per-request count it proposes.
