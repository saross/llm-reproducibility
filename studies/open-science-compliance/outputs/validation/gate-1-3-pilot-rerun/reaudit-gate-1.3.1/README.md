# Re-audit of the herskind pilot with gate 1.3.1

The gate 1.3 final review asked that the pilot's transcripts be re-audited
after the fixes, "not waived by ruling, and the old report not quietly
edited" (Astra, F1). This folder holds that re-audit, made on 2026-10-12 with
the code on branch `feat/gate-1-3-1-review-fixes`. The attempt's own gate 1.3
records (`herskind-riede-2024/reproduction/attempt-03/`) and the original
audit (`../audit-wf_7c18dfdc-298.json`) are unchanged.

`reaudit.py` repeats `audit-run`'s steps for workflow run `wf_7c18dfdc-298`,
writing here instead of into the attempt. `gate-report.json` is
`check-attempt --launch-commit cd5d54a…` under `GATE_VERSION` 1.3.1.

| | Gate 1.3 (original) | Gate 1.3.1 (this re-audit) |
|---|---|---|
| Transcript audit hard failures | 4 (all parser false positives, F1) | 0 |
| Transcript audit flags | 2 host-run | 2 host-run, 4 transcription-after-run (Figs 2, 4, and 5, and that folder's README; F6) |
| Receipt problems | 13 "declared pull not in transcript" (11 executor, 2 reviewer), from a Read-only check | the 3 genuine ones: 2 partial `sed -n` reads, 1 grep-only (F2), plus the version mismatch below |
| Gate issues | 4 obligations | adds `parsed-not-run` (A-new-1), `build-evidence` (F5), and `method-adherence` (F4) |
| Run audit (new, F8) | none | 3 escalations, the QUALIFIED review, 3 blinding warnings, and the launch message (F3) |

The receipts also show `agent_version` mismatches: the pilot's agents ran as
executor v1.6 and reviewer v1.2, and the manifest now pins v1.7 and v1.3.
That is expected when an old run is re-audited against new definitions. The
pilot is not study data, and nothing here is ruled.
