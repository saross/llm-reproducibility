# Run audit — gate-1-3-pilot-rerun-2026-10

Workflow run `wf_7c18dfdc-298`, audited 2026-10-11T12:03:32+00:00. **Clean: False**

| Agent | Type | Paper | Receipts | Contaminating | Warnings | Writes out of scope | Output tok | Input-side tok | USD | Wall-clock (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| a3825ccd2e | reproduction-executor | herskind-riede-2024 | INVALID | 0 | 3 | 0 | 69693 | 33955729 | 10.4571 | 2103.8 |
| a49f673690 | adversarial-reviewer | herskind-riede-2024 | INVALID | 0 | 0 | 0 | 15547 | 5086929 | 2.273 | 397.8 |
| ab1a1f652d | general-purpose | herskind-riede-2024 | n/a | 0 | 0 | 0 | 957 | 99134 | — | 8.9 |

## Per paper

| Paper | Agents | Output tok | Input-side tok | USD (API-equivalent) | Agent wall-clock (min) |
|---|---|---|---|---|---|
| herskind-riede-2024 | 3 | 86197 | 39141792 | 12.73 (+1 unpriced) | 41.8 |

## Findings

- a3825ccd2e warning Bash `verification-strategies.md` (blinded path named in command output (review))
- a3825ccd2e warning Bash `references/verification-strategies.md` (blinded path named in command output (review))
- a3825ccd2e warning Bash `crema-et-al-2024.json` (blinded path named in command output (review))
- **a3825ccd2e** receipts: declared pull not in transcript: /home/shawn/Code/llm-reproducibility/.claude/skills/reproduction-assessor/references/dockerfile-patterns.md; declared pull not in transcript: /home/shawn/Code/llm-reproducibility/.claude/skills/reproduction-assessor/references/wrapper-script-patterns.md; declared pull not in transcript: /home/shawn/Code/llm-reproducibility/reproduction-system/templates/comparison-report-template.md; declared pull not in transcript: /home/shawn/Code/llm-reproducibility/reproduction-system/templates/environment-template.md; declared pull not in transcript: /home/shawn/Code/llm-reproducibility/reproduction-system/templates/log-template.md; declared pull not in transcript: /home/shawn/Code/llm-reproducibility/reproduction-system/templates/README.md; declared pull not in transcript: /home/shawn/Code/llm-reproducibility/reproduction-system/prompts/01-preparation.md; declared pull not in transcript: /home/shawn/Code/llm-reproducibility/reproduction-system/prompts/02-execution-and-verification.md; declared pull not in transcript: /home/shawn/Code/llm-reproducibility/reproduction-system/schemas/comparison-record.json; declared pull not in transcript: /home/shawn/Code/llm-reproducibility/reproduction-system/schemas/authors-code-manifest.json; declared pull not in transcript: /home/shawn/Code/llm-reproducibility/studies/open-science-compliance/protocol/instruments/data-availability-taxonomy.md
- **a49f673690** receipts: declared pull not in transcript: /home/shawn/Code/llm-reproducibility/studies/open-science-compliance/protocol/instruments/verdicts-and-precision.md; declared pull not in transcript: /home/shawn/Code/llm-reproducibility/studies/open-science-compliance/protocol/instruments/coverage-rules.md
