{
  "run_id": "gate-1-3-1-pilot-rerun-2026-10",
  "built_at": "2026-10-17T06:39:09+00:00",
  "queue": [
    "herskind-riede-2024: FLAG: run-05: statement 8 of original 'Herskind&Riede_S2.R' (lines 27) errored (arguments imply differing number of rows: 0, 1) and the evaluator tolerated: a target is credited only from statements that completed, so confirm it computes nothing that enters a result",
    "herskind-riede-2024: FLAG: T13: the comparison departed from the approved plan's method: The plan says to read the unigram frequencies from the authors' 'captured token_freqs'. That object exists only inside the authors' function ngramfunction() and is never a global object, so it cannot be captured without altering the authors' code. Decided during execution (2026-10-17, while writing  (a human rules on it; the original plan stands as approved)"
  ],
  "problems": [],
  "lost_in_relay": [],
  "issues": [
    {
      "slug": "herskind-riede-2024",
      "id": "tolerated-statement:Herskind&Riede_S2.R:27@run-05",
      "kind": "flag",
      "status": "unruled",
      "decision": null,
      "message": "FLAG: run-05: statement 8 of original 'Herskind&Riede_S2.R' (lines 27) errored (arguments imply differing number of rows: 0, 1) and the evaluator tolerated: a target is credited only from statements that completed, so confirm it computes nothing that enters a result"
    },
    {
      "slug": "herskind-riede-2024",
      "id": "method-deviation:T13",
      "kind": "flag",
      "status": "unruled",
      "decision": null,
      "message": "FLAG: T13: the comparison departed from the approved plan's method: The plan says to read the unigram frequencies from the authors' 'captured token_freqs'. That object exists only inside the authors' function ngramfunction() and is never a global object, so it cannot be captured without altering the authors' code. Decided during execution (2026-10-17, while writing  (a human rules on it; the original plan stands as approved)"
    },
    {
      "slug": "herskind-riede-2024",
      "id": "in-memory-patching:install-pins.R",
      "kind": "obligation",
      "status": "unruled",
      "decision": null,
      "message": "install-pins.R can patch functions in memory (body, formals, trace, assignInNamespace, unlockBinding, or <<-): confirm it changes no function of the authors' code"
    },
    {
      "slug": "herskind-riede-2024",
      "id": "docker-copy:Dockerfile",
      "kind": "obligation",
      "status": "unruled",
      "decision": null,
      "message": "Dockerfile copies attempt files into the image: confirm the run executes the mounted, checked tree and not the image's copy"
    },
    {
      "slug": "herskind-riede-2024",
      "id": "run-time-texts:deposit/Herskind&Riede_S2.R|promise",
      "kind": "obligation",
      "status": "unruled",
      "decision": null,
      "message": "run-05: 107 text(s) built at run time and evaluated in deposit/Herskind&Riede_S2.R, with no calling function (a promise, as in a dplyr data mask), match no original, no chunk of an original document, and no tool expression or package template: confirm what they ran. The texts: \"A1 == 1 & A24 == 1\"; \"A1 == 1 & A24 == 1 & ANT == 1\"; \"A1 == 1 & A24 == 1 & B10 == 1\"; \"A1 == 1 & A24 == 1 & B10 == 1 & ANT == 1\"; \"A1 == 1 & A24 == 1 & B10 == 1 & C1 == 1\"; \"A1 == 1 & A24 == 1 & B12 == 1 & ANT == 1\"; \"A1 == 1 & A24 == 1 & B2 == 1\"; \"A1 == 1 & A24 == 1 & B2 == 1 & C1 == 1\"; \"A1 == 1 & A24 == 1 & B2 == 1 & H1 == 1\"; \"A1 == 1 & A24 == 1 & C1 == 1\"; \"A1 == 1 & A24 == 1 & D5 == 1\"; \"A1 == 1 & A24 == 1 & D5 == 1 & ANT == 1\"; \"A1 == 1 & A24 == 1 & F5 == 1 & H1 == 1\"; \"A1 == 1 & A24 == 1 & H1 == 1\"; \"A1 == 1 & A3 == 1 & C1 == 1 & G1 == 1\"; \"A1 == 1 & ANT == 1\"; \"A1 == 1 & B10 == 1\"; \"A1 == 1 & B10 == 1 & B12 == 1\"; \"A1 == 1 & B10 == 1 & C1 == 1\"; \"A1 == 1 & B10 == 1 & C1 == 1 & E1 == 1\"; \"A1 == 1 & B12 == 1 & ANT == 1\"; \"A1 == 1 & B2 == 1\"; \"A1 == 1 & B2 == 1 & C1 == 1\"; \"A1 == 1 & B2 == 1 & C1 == 1 & G1 == 1\"; \"A1 == 1 & C1 == 1\"; \"A1 == 1 & C1 == 1 & C5 == 1 & G1 == 1\"; \"A1 == 1 & C1 == 1 & E1 == 1 & F14 == 1\"; \"A1 == 1 & C1 == 1 & F12 == 1 & G1 == 1\"; \"A1 == 1 & C1 == 1 & F13 == 1\"; \"A1 == 1 & C1 == 1 & F13 == 1 & G1 == 1\"; \"A1 == 1 & C1 == 1 & F14 == 1\"; \"A1 == 1 & C1 == 1 & F14 == 1 & G1 == 1\"; \"A1 == 1 & C1 == 1 & F5 == 1\"; \"A1 == 1 & C1 == 1 & G1 == 1\"; \"A1 == 1 & C1 == 1 & G1 == 1 & H1 == 1\"; \"A1 == 1 & C1 == 1 & H1 == 1\"; \"A1 == 1 & D33 == 1 & H1 == 1\"; \"A1 == 1 & D5 == 1 & ANT == 1\"; \"A1 == 1 & E1 == 1 & F14 == 1\"; \"A1 == 1 & F13 == 1 & G1 == 1\"; \"A1 == 1 & F5 == 1\"; \"A1 == 1 & G1 == 1\"; \"A1 == 1 & G1 == 1 & G7 == 1\"; \"A1 == 1 & G1 == 1 & H1 == 1\"; \"A1 == 1 & H1 == 1\"; \"A24 == 1 & ANT == 1\"; \"A24 == 1 & B10 == 1\"; \"A24 == 1 & B10 == 1 & ANT == 1\"; \"A24 == 1 & B10 == 1 & C1 == 1\"; \"A24 == 1 & B12 == 1 & ANT == 1\"; \"A24 == 1 & C1 == 1\"; \"A24 == 1 & C1 == 1 & G1 == 1 & H1 == 1\"; \"A24 == 1 & D5 == 1 & ANT == 1\"; \"A3 == 1 & C1 == 1 & G1 == 1\"; \"A3 == 1 & C1 == 1 & G1 == 1 & H1 == 1\"; \"B10 == 1 & C1 == 1\"; \"B10 == 1 & F38 == 1\"; \"B10 == 1 & F5 == 1 & F12 == 1\"; \"B12 == 1 & ANT == 1\"; \"B13 == 1 & E1 == 1\"; \"B2 == 1 & B10 == 1\"; \"B2 == 1 & B10 == 1 & F5 == 1\"; \"B2 == 1 & C1 == 1\"; \"B4 == 1 & C1 == 1 & F12 == 1\"; \"B4 == 1 & F12 == 1\"; \"C1 == 1 & C12 == 1 & C13 == 1\"; \"C1 == 1 & C12 == 1 & G1 == 1\"; \"C1 == 1 & C4 == 1 & C12 == 1\"; \"C1 == 1 & C4 == 1 & C5 == 1\"; \"C1 == 1 & C4 == 1 & C5 == 1 & C12 == 1\"; \"C1 == 1 & C5 == 1 & C12 == 1\"; \"C1 == 1 & C5 == 1 & G1 == 1\"; \"C1 == 1 & E1 == 1 & F14 == 1\"; \"C1 == 1 & F12 == 1\"; \"C1 == 1 & F12 == 1 & F13 == 1\"; \"C1 == 1 & F12 == 1 & F13 == 1 & G1 == 1\"; \"C1 == 1 & F13 == 1 & G1 == 1\"; \"C1 == 1 & F15 == 1 & G1 == 1\"; \"C1 == 1 & F5 == 1\"; \"C1 == 1 & G1 == 1\"; \"C1 == 1 & G1 == 1 & G2 == 1\"; \"C1 == 1 & G1 == 1 & H1 == 1\"; \"C1 == 1 & G2 == 1\"; \"C1 == 1 & H1 == 1\"; \"C12 == 1 & C13 == 1\"; \"C4 == 1 & C12 == 1\"; \"C4 == 1 & C5 == 1\"; \"C4 == 1 & C5 == 1 & C12 == 1\"; \"C5 == 1 & C12 == 1\"; \"C5 == 1 & C13 == 1\"; \"C5 == 1 & D7 == 1\"; \"D15 == 1 & G1 == 1 & G2 == 1\"; \"D3 == 1 & ZOO == 1\"; \"D5 == 1 & ANT == 1\"; \"E1 == 1 & E5 == 1\"; \"E1 == 1 & F12 == 1\"; \"E1 == 1 & F14 == 1\"; \"E1 == 1 & F5 == 1 & F12 == 1\"; \"E4 == 1 & E5 == 1\"; \"F12 == 1 & F13 == 1\"; \"F12 == 1 & F13 == 1 & G1 == 1\"; \"F14 == 1 & F35 == 1\"; \"G1 == 1 & G2 == 1\"; \"G1 == 1 & H1 == 1\"; \"I1 == 1 & I13 == 1\"; \"I1 == 1 & I5 == 1\"; \"I5 == 1 & I13 == 1\""
    },
    {
      "slug": "herskind-riede-2024",
      "id": "wrapper-semantics:wrappers",
      "kind": "obligation",
      "status": "unruled",
      "decision": null,
      "message": "wrapper semantics are not verified by the gate: its line-overlap check is a heuristic, so the reviewer confirms that each wrapper only mechanises the authors' code (paths, seeds, capture)"
    },
    {
      "slug": "herskind-riede-2024",
      "id": "method-adherence:targets",
      "kind": "obligation",
      "status": "unruled",
      "decision": null,
      "message": "the gate checks counts, not methods: the reviewer compares each target's executed comparison method and tolerance with the approved plan's wording, and names every departure, declared or not"
    },
    {
      "slug": "herskind-riede-2024",
      "id": "host-run:published-values/measure_fig3_bars.py",
      "kind": "flag",
      "status": "unruled",
      "decision": null,
      "message": "FLAG: the executor ran published-values/measure_fig3_bars.py on the host before the final run (python3 -I /home/shawn/Code/llm-reproducibility/studies/open-science-compliance/outputs/herskind-riede-2024/reproduction/attempt-04/published-values/measure_fig): credit comes only from sealed outputs, but invariant 5 is an environment rule, so a human rules on it"
    },
    {
      "slug": "herskind-riede-2024",
      "id": "host-run:published-values/detect_fig4_boxes.py",
      "kind": "flag",
      "status": "unruled",
      "decision": null,
      "message": "FLAG: the executor ran published-values/detect_fig4_boxes.py on the host before the final run (time python3 -I /home/shawn/Code/llm-reproducibility/studies/open-science-compliance/outputs/herskind-riede-2024/reproduction/attempt-04/published-values/detect): credit comes only from sealed outputs, but invariant 5 is an environment rule, so a human rules on it"
    },
    {
      "slug": "herskind-riede-2024",
      "id": "escalation:executor:PAPER_ERROR:T05",
      "kind": "flag",
      "status": "unruled",
      "decision": null,
      "message": "FLAG: the executor escalated PAPER_ERROR on T05: Table 1 differs from the authors' deposited S3 (tier 2) and from the authors' code run unmodified on their data (tier 3) in 8 of 130 cells, each by one type. Bigram frequency classes 8, 7, 4, 3, 2, 1: published 6, 8, 32, 59, 154, 1224; reproduced 5, 9, 31, 60, 153, 1225 (S3 gives 5, 9, 31, 60 for the classes it covers). Trigram classes 2, 1: published 222, 4094; reproduced 221, 4095. Header totals (a human confirms or rejects it)"
    },
    {
      "slug": "herskind-riede-2024",
      "id": "escalation:executor:OTHER:T03",
      "kind": "flag",
      "status": "unruled",
      "decision": null,
      "message": "FLAG: the executor escalated OTHER on T03: Scored MINOR_DISCREPANCY: 2 of 1176 culture-exclusive box cells in the GIMP-annotated Fig. 4 disagree with the read-only S1 lookup. C5-F13 is boxed Ertebølle, but its single bearing object is Kongemose; B1-B2 is exclusive to Maglemose but has no box. Both are single-object pairs not plotted in the heatmap. A human may instead rule these PAPER_ERROR (tier 2, deposited S1). The matrix (163 exact, 2  (a human confirms or rejects it)"
    },
    {
      "slug": "herskind-riede-2024",
      "id": "escalation:executor:CANNOT_COMPARE:T04",
      "kind": "flag",
      "status": "unruled",
      "decision": null,
      "message": "FLAG: the executor escalated CANNOT_COMPARE on T04: Fig. 5's motif-extent patches have no code or stated method, as the plan pre-declared. The ten pies match S1 exactly (10/10), and their positions agree with S1 coordinates (Spearman 0.997 and 1.000). The target is partially verified and counts against coverage. (a human confirms or rejects it)"
    },
    {
      "slug": "herskind-riede-2024",
      "id": "blinding-warning:executor:verification-strategies.md",
      "kind": "flag",
      "status": "unruled",
      "decision": null,
      "message": "FLAG: blinded path named in command output (review): ls reproduction-system/templates/ reproduction-system/schemas/ reproduction-system/prompts/ .claude/skills/reproduction-assessor/references/ && wc -l reproduction-system/templates/* reproduction-syste"
    },
    {
      "slug": "herskind-riede-2024",
      "id": "blinding-warning:executor:crema-et-al-2024.json",
      "kind": "flag",
      "status": "unruled",
      "decision": null,
      "message": "FLAG: blinded path named in command output (review): venv/bin/python scripts/reproduction-lane.py --help; venv/bin/python scripts/reproduction-lane.py build-image --help; venv/bin/python scripts/reproduction-lane.py run-container --help; ls corpus/evide"
    },
    {
      "slug": "herskind-riede-2024",
      "id": "blinding-warning:executor:wiki/planning/reproduction-gate-1-3-design.md",
      "kind": "flag",
      "status": "unruled",
      "decision": null,
      "message": "FLAG: blinded path named in command output (review): sed -n 1,80p scripts/reproduction-lane.py; sed -n 195,240p scripts/reproduction-lane.py; sed -n 6123,6390p scripts/reproduction-lane.py"
    },
    {
      "slug": "herskind-riede-2024",
      "id": "review:qualified",
      "kind": "flag",
      "status": "unruled",
      "decision": null,
      "message": "FLAG: the adversarial review is QUALIFIED (concerns: confirmation_bias, methodological_soundness; supports the verdict: True): a human resolves each concern before the result enters study data"
    },
    {
      "slug": "herskind-riede-2024",
      "id": "launch-message:cdbca2a1e5e4",
      "kind": "flag",
      "status": "unruled",
      "decision": null,
      "message": "FLAG: the workflow was launched with 'go', not the runbook's fixed phrase, and the harness relayed it to every agent ahead of the workflow's instructions: a human rules whether it could steer or unblind the run"
    }
  ],
  "unruled": 17
}
