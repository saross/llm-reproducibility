# Spend-tripwire event — fable-5 arm (contract hardening 4)

**Date:** 2026-08-17. **Fired at:** 7,100,984 contract-metric tokens
against the 7,000,000 wire (+1.4%).

**Cause:** the base run (15 scoring + 15 reconcile spawns) came in under
the wire; the two contract-mandated item re-runs (superseded spawns
`aab9fd20a0fcbbca0`, `ad362ea036c93fa88` — see the failure register)
added their spend to the same arm budget, per the wire's
count-everything-spent rule.

**Operator ruling (Shawn, 2026-08-17): arm ACCEPTED** with the overage
documented — the excess is small, fully explained, and produced by the
contract's own remediation machinery, not runaway behaviour.

**Wire rule amended (same ruling):** if X% of a run's items require
re-running, the wire increases by X% (remediation-scaled) — UNLESS an
indicator points to a stuck or repeating-not-resolving loop (the same
item failing repeatedly, or replacement spawns themselves failing
reconciliation), in which case the halt applies regardless of headroom.
Under the amended rule this arm's wire was 7,000,000 × (1 + 2/15) ≈
7,933,333, and 7,100,984 sits inside it; no loop indicator was present
(both replacement spawns reconciled clean on every layer, first
attempt).
