# P3 — differential effort probe (2026-08-17)

**Purpose:** design-note mitigation 1 (as amended): verify that `agent()`
workflow opts `effort` reaches served spawns, before any arm spend. Two
sonnet-5 spawns, identical reasoning prompt bar an attribution label
(`probe label: effort-low` / `effort-max`), pinned `low` vs `max` via the
same opts channel the scoring arms use (workflow v1.5).

**Run:** workflow `wf_e4458509-fbe` (session f605c78a, transcript dir
`subagents/workflows/wf_e4458509-fbe/`), 2 spawns, 71,245 subagent tokens,
33.9 s wall-clock, launched immediately after GO commit `a293fe1`.

## Recount (assembler v1.4 counting functions, per transcript)

| Metric | effort-low (`a277f2c6ec7a1bfc6`) | effort-max (`a17c84c3a58e5a964`) | ratio |
|---|---|---|---|
| output_tokens | 465 | 3,491 | **7.51×** |
| wallclock_seconds | 5.2 | 33.8 | 6.5× |
| thinking_blocks | 1 | 2 | — |
| contract_metric_tokens | 68,355 | 78,087 | 1.14× |

Qualitative corroboration: the max spawn added an unprompted computational
verification (brute-force enumeration via `fractions.Fraction`) beyond the
requested two methods; both spawns answered correctly (24/91).

## Verdict

**PASS.** Pre-registered criterion: a large thinking/output differential
proves the opts channel is honoured; near-identical telemetry halts the
study. Observed 7.5× output-token differential at identical prompts and
model. The `opts.effort` channel is honoured in the workflow lane; arm 1
(sonnet-5 @ max) is cleared to launch. Residual R1 (served-effort not
directly attested by the harness) remains covered by the telemetry-contrast
step at arm close.
