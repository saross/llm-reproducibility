# Run audit — phase2-shakedown-2026-10

Workflow run `wf_bbf623d0-0ae`, audited 2026-10-03T08:53:08+00:00. **Clean: False**

| Agent | Type | Paper | Receipts | Contaminating | Warnings | Writes out of scope | Output tok | Input-side tok | USD | Wall-clock (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| a8de23de19 | reproduction-planner | herskind-riede-2024 | INVALID | 0 | 0 | 0 | 19385 | 765319 | 0.9567 | 369.4 |
| a9334166e5 | reproduction-planner | dye-et-al-2023 | INVALID | 0 | 1 | 0 | 27704 | 3134649 | 1.9752 | 534.9 |

## Per paper

| Paper | Agents | Output tok | Input-side tok | USD (API-equivalent) | Agent wall-clock (min) |
|---|---|---|---|---|---|
| dye-et-al-2023 | 1 | 27704 | 3134649 | 1.98 | 8.9 |
| herskind-riede-2024 | 1 | 19385 | 765319 | 0.96 | 6.2 |

## Findings

- **a8de23de19** receipts: declared pull not in transcript: studies/open-science-compliance/protocol/instruments/verdicts-and-precision.md (v1.0, Receipt-token fe9bca3d3c95f931)
- a9334166e5 warning Bash `studies/open-science-compliance/outputs/dye-et-al-2023/reproduction/attempt-01/supplement.pdf` (blinded path named in command output (review))
- **a9334166e5** receipts: declared pull not in transcript: /home/shawn/Code/llm-reproducibility/studies/open-science-compliance/protocol/instruments/verdicts-and-precision.md (v1.0, Receipt-token fe9bca3d3c95f931; read in full)
