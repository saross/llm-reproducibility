# Run audit — gate-1-3-1-pilot-rerun-2026-10

Workflow run `wf_4fd7a886-ada`, audited 2026-10-17T06:38:48+00:00. **Clean: True**

| Agent | Type | Paper | Receipts | Contaminating | Warnings | Writes out of scope | Output tok | Input-side tok | USD | Wall-clock (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| a23bd74af4 | reproduction-executor | herskind-riede-2024 | valid | 0 | 3 | 0 | 85566 | 34322319 | 10.7056 | 2059.9 |
| a2ca872e44 | adversarial-reviewer | herskind-riede-2024 | valid | 0 | 0 | 0 | 32396 | 5966306 | 3.3045 | 464.7 |
| a96bb181a9 | general-purpose | herskind-riede-2024 | n/a | 0 | 0 | 0 | 1415 | 212358 | 0.0092 | 15.4 |

## Per paper

| Paper | Agents | Output tok | Input-side tok | USD (API-equivalent) | Agent wall-clock (min) |
|---|---|---|---|---|---|
| herskind-riede-2024 | 3 | 119377 | 40500983 | 14.02 | 42.3 |

## Findings

- a23bd74af4 warning Bash `verification-strategies.md` (blinded path named in command output (review))
- a23bd74af4 warning Bash `crema-et-al-2024.json` (blinded path named in command output (review))
- a23bd74af4 warning Bash `wiki/planning/reproduction-gate-1-3-design.md` (blinded path named in command output (review))
