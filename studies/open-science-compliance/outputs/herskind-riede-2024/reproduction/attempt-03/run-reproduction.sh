#!/usr/bin/env bash
# =============================================================================
# run-reproduction.sh — lane entry point, Herskind & Riede 2024, attempt 03
# =============================================================================
#
# Purpose: the single entry the lane's run-container starts (bash, inside the
# container, networking off, as the invoking user, in the mounted work copy).
#   1. run-analysis.R    runs the authors' S2.R unmodified (see its header).
#   2. compare-results.R reads the run's captures and the deposited files
#                        read-only and writes value-level comparisons; it never
#                        touches the authors' code and runs in its own R
#                        process, so nothing it does can reach S2.R's session.
# The comparison step runs only if the analysis step exits 0.
#
# Usage (from the repository root; never run on the host):
#   venv/bin/python scripts/reproduction-lane.py run-container <attempt dir> \
#     --image llmr-herskind-riede-2024-attempt-03 --entry run-reproduction.sh \
#     --launch-commit <commit>
# =============================================================================
set -u

echo "LLMR: entry started $(date -u +%Y-%m-%dT%H:%M:%SZ) in $(pwd)"

mkdir -p wrapper-captures
# The console output of the analysis step (the values S2.R prints for
# Table 1 and Table 2) is also kept in a file, for compare-results.R to parse.
Rscript run-analysis.R 2>&1 | tee wrapper-captures/analysis-console.txt
analysis_status=${PIPESTATUS[0]}
echo "LLMR: run-analysis.R exit status ${analysis_status}"
if [ "${analysis_status}" -ne 0 ]; then
  exit "${analysis_status}"
fi

Rscript compare-results.R 2>&1 | tee wrapper-captures/compare-console.txt
compare_status=${PIPESTATUS[0]}
echo "LLMR: compare-results.R exit status ${compare_status}"
echo "LLMR: entry finished $(date -u +%Y-%m-%dT%H:%M:%SZ)"
exit "${compare_status}"
