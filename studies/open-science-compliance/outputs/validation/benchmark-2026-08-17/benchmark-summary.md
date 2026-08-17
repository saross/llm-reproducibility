# D3 re-benchmark — cycle summary (2026-08-17)

**Design:** amendment 2 §4 — three arms × five pilot papers × three runs on
the clarified instrument (v2.1), structured-output contract v1.1 (runtime
variant per the S4 retreat), evidence packs injected per paper, workflow
v1.2→v1.4 with per-item C9 reconciliation. Arms sequential under the D3 run
contract (pre-run review + clean-context audit, 15 hardenings). Per-arm
acceptance: every non-superseded governed spawn reconciled by the
authoritative pass (`--expect-spawns --require-pack --contract-schema`).
Full provenance in each arm's `run-record.json` (receipted model ids,
run-environment attestations incl. scoring effort xhigh session-inherited,
contract-metric spend); failure adjudications in
`../failure-modes/register.md`.

## Stability (registered statistic: unanimity across 3 runs, 150 items)

| Arm | Model (receipted) | 2026-08-03 cycle | This cycle | Gate ≥ 0.90 |
|---|---|---|---|---|
| sonnet-5 | `claude-sonnet-5` | 121/150 = 0.807 | **128/150 = 0.853** | below |
| opus-5 | `claude-opus-5[1m]` | 131/150 = 0.873 | **143/150 = 0.953** | **PASS** |
| fable-5 | `claude-fable-5` | 122/150 = 0.813 | **142/150 = 0.947** | **PASS** |

Computed by `analyse-benchmark-disagreements.py --bench-dir <this dir>
--stability-only` from the committed per-run payloads; the tool wrote this
cycle's `disputed-items.json` (56 items, vs 68 pre-clarification).

**Movement:** sonnet +0.047, opus +0.080, fable +0.134. The three
pre-clarification headline ambiguities moved decisively: A1.2 disputed
items 10 → 3, R1.3 8 → 6, and the F-block target question no longer
produces the dye 6–13 flip (F1/F2/F3/F4 disputed: 2/6/2/2). The residual
disagreement leaders are I3 (7) and R1.1 (7).

## Concordance — deliberately not computed (contract hardening 5)

Concordance is pending the E8-v2 reference re-derivation (the registrant's
adjudication worksheet, amendment 2 §3). No partial concordance against
the retired reference is computed; the script run used
`--stability-only`. The gates ruling (amendment 2 §4: both gates ≥ 0.90)
follows once E8 v2 is registered.

**Interim observation, not a gate result:** two of three arms now clear
the stability gate that no arm cleared pre-clarification — evidence that
the item-structured disagreement was instrument ambiguity, exactly as
amendment 2 argued.

## Cautions

- **The legacy "guideless-minority" diagnostic is vacuous this cycle:** it
  detects guide exposure via pull receipts, and the guide is now pushed
  (amendment 2 §5), so every spawn registers "guideless" under the old
  definition. Its output for this cycle carries no information; noted so
  nobody reads 22/22 as a finding.
- **Spend (contract metric, per arm):** sonnet 6,216,252; opus 5,068,770;
  fable 7,100,984 — fable's figure includes two contract-mandated item
  re-runs and tripped the pre-amendment 7M wire (+1.4%); accepted by the
  registrant with the event documented (`arm-fable-5/tripwire-event.md`)
  and the wire rule amended to remediation-scaled.
- **Effort provenance is attestation, not artefact:** scoring spawns
  inherited the session's xhigh; the harness records no effort field.
  Effort-pinning (explicit per-spawn effort + run-record capture) is
  queued now the freeze window has lifted, ahead of any effort study.
- **Fable behavioural note:** the cycle's only two model-side failures
  (one fabricated pull declaration, one out-of-scope Glob) came from the
  fable arm; both were caught by multiple layers, superseded, and re-run
  clean — register entries F-001/F-002.
