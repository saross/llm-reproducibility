{
  "run_id": "gate-1-3-pilot-rerun-2026-10",
  "built_at": "2026-10-11T12:03:33+00:00",
  "queue": [],
  "problems": [],
  "lost_in_relay": [],
  "issues": [
    {
      "slug": "herskind-riede-2024",
      "id": "dynamic-evaluation:Dockerfile",
      "kind": "obligation",
      "status": "unruled",
      "decision": null,
      "message": "Dockerfile evaluates code dynamically (parse, eval, source of a computed path, or exec): confirm it evaluates only the declared authors' files, unmodified"
    },
    {
      "slug": "herskind-riede-2024",
      "id": "dynamic-evaluation:run-analysis.R",
      "kind": "obligation",
      "status": "unruled",
      "decision": null,
      "message": "run-analysis.R evaluates code dynamically (parse, eval, source of a computed path, or exec): confirm it evaluates only the declared authors' files, unmodified"
    },
    {
      "slug": "herskind-riede-2024",
      "id": "run-time-texts:run-analysis.R|promise",
      "kind": "obligation",
      "status": "unruled",
      "decision": null,
      "message": "run-04: 107 text(s) built at run time and evaluated in run-analysis.R, with no calling function (a promise, as in a dplyr data mask), match no original, no chunk of an original document, and no tool expression or package template: confirm what they ran. The texts: \"A1 == 1 & A24 == 1\"; \"A1 == 1 & A24 == 1 & ANT == 1\"; \"A1 == 1 & A24 == 1 & B10 == 1\"; \"A1 == 1 & A24 == 1 & B10 == 1 & ANT == 1\"; \"A1 == 1 & A24 == 1 & B10 == 1 & C1 == 1\"; \"A1 == 1 & A24 == 1 & B12 == 1 & ANT == 1\"; \"A1 == 1 & A24 == 1 & B2 == 1\"; \"A1 == 1 & A24 == 1 & B2 == 1 & C1 == 1\"; \"A1 == 1 & A24 == 1 & B2 == 1 & H1 == 1\"; \"A1 == 1 & A24 == 1 & C1 == 1\"; \"A1 == 1 & A24 == 1 & D5 == 1\"; \"A1 == 1 & A24 == 1 & D5 == 1 & ANT == 1\"; \"A1 == 1 & A24 == 1 & F5 == 1 & H1 == 1\"; \"A1 == 1 & A24 == 1 & H1 == 1\"; \"A1 == 1 & A3 == 1 & C1 == 1 & G1 == 1\"; \"A1 == 1 & ANT == 1\"; \"A1 == 1 & B10 == 1\"; \"A1 == 1 & B10 == 1 & B12 == 1\"; \"A1 == 1 & B10 == 1 & C1 == 1\"; \"A1 == 1 & B10 == 1 & C1 == 1 & E1 == 1\"; \"A1 == 1 & B12 == 1 & ANT == 1\"; \"A1 == 1 & B2 == 1\"; \"A1 == 1 & B2 == 1 & C1 == 1\"; \"A1 == 1 & B2 == 1 & C1 == 1 & G1 == 1\"; \"A1 == 1 & C1 == 1\"; \"A1 == 1 & C1 == 1 & C5 == 1 & G1 == 1\"; \"A1 == 1 & C1 == 1 & E1 == 1 & F14 == 1\"; \"A1 == 1 & C1 == 1 & F12 == 1 & G1 == 1\"; \"A1 == 1 & C1 == 1 & F13 == 1\"; \"A1 == 1 & C1 == 1 & F13 == 1 & G1 == 1\"; \"A1 == 1 & C1 == 1 & F14 == 1\"; \"A1 == 1 & C1 == 1 & F14 == 1 & G1 == 1\"; \"A1 == 1 & C1 == 1 & F5 == 1\"; \"A1 == 1 & C1 == 1 & G1 == 1\"; \"A1 == 1 & C1 == 1 & G1 == 1 & H1 == 1\"; \"A1 == 1 & C1 == 1 & H1 == 1\"; \"A1 == 1 & D33 == 1 & H1 == 1\"; \"A1 == 1 & D5 == 1 & ANT == 1\"; \"A1 == 1 & E1 == 1 & F14 == 1\"; \"A1 == 1 & F13 == 1 & G1 == 1\"; \"A1 == 1 & F5 == 1\"; \"A1 == 1 & G1 == 1\"; \"A1 == 1 & G1 == 1 & G7 == 1\"; \"A1 == 1 & G1 == 1 & H1 == 1\"; \"A1 == 1 & H1 == 1\"; \"A24 == 1 & ANT == 1\"; \"A24 == 1 & B10 == 1\"; \"A24 == 1 & B10 == 1 & ANT == 1\"; \"A24 == 1 & B10 == 1 & C1 == 1\"; \"A24 == 1 & B12 == 1 & ANT == 1\"; \"A24 == 1 & C1 == 1\"; \"A24 == 1 & C1 == 1 & G1 == 1 & H1 == 1\"; \"A24 == 1 & D5 == 1 & ANT == 1\"; \"A3 == 1 & C1 == 1 & G1 == 1\"; \"A3 == 1 & C1 == 1 & G1 == 1 & H1 == 1\"; \"B10 == 1 & C1 == 1\"; \"B10 == 1 & F38 == 1\"; \"B10 == 1 & F5 == 1 & F12 == 1\"; \"B12 == 1 & ANT == 1\"; \"B13 == 1 & E1 == 1\"; \"B2 == 1 & B10 == 1\"; \"B2 == 1 & B10 == 1 & F5 == 1\"; \"B2 == 1 & C1 == 1\"; \"B4 == 1 & C1 == 1 & F12 == 1\"; \"B4 == 1 & F12 == 1\"; \"C1 == 1 & C12 == 1 & C13 == 1\"; \"C1 == 1 & C12 == 1 & G1 == 1\"; \"C1 == 1 & C4 == 1 & C12 == 1\"; \"C1 == 1 & C4 == 1 & C5 == 1\"; \"C1 == 1 & C4 == 1 & C5 == 1 & C12 == 1\"; \"C1 == 1 & C5 == 1 & C12 == 1\"; \"C1 == 1 & C5 == 1 & G1 == 1\"; \"C1 == 1 & E1 == 1 & F14 == 1\"; \"C1 == 1 & F12 == 1\"; \"C1 == 1 & F12 == 1 & F13 == 1\"; \"C1 == 1 & F12 == 1 & F13 == 1 & G1 == 1\"; \"C1 == 1 & F13 == 1 & G1 == 1\"; \"C1 == 1 & F15 == 1 & G1 == 1\"; \"C1 == 1 & F5 == 1\"; \"C1 == 1 & G1 == 1\"; \"C1 == 1 & G1 == 1 & G2 == 1\"; \"C1 == 1 & G1 == 1 & H1 == 1\"; \"C1 == 1 & G2 == 1\"; \"C1 == 1 & H1 == 1\"; \"C12 == 1 & C13 == 1\"; \"C4 == 1 & C12 == 1\"; \"C4 == 1 & C5 == 1\"; \"C4 == 1 & C5 == 1 & C12 == 1\"; \"C5 == 1 & C12 == 1\"; \"C5 == 1 & C13 == 1\"; \"C5 == 1 & D7 == 1\"; \"D15 == 1 & G1 == 1 & G2 == 1\"; \"D3 == 1 & ZOO == 1\"; \"D5 == 1 & ANT == 1\"; \"E1 == 1 & E5 == 1\"; \"E1 == 1 & F12 == 1\"; \"E1 == 1 & F14 == 1\"; \"E1 == 1 & F5 == 1 & F12 == 1\"; \"E4 == 1 & E5 == 1\"; \"F12 == 1 & F13 == 1\"; \"F12 == 1 & F13 == 1 & G1 == 1\"; \"F14 == 1 & F35 == 1\"; \"G1 == 1 & G2 == 1\"; \"G1 == 1 & H1 == 1\"; \"I1 == 1 & I13 == 1\"; \"I1 == 1 & I5 == 1\"; \"I5 == 1 & I13 == 1\""
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
      "id": "host-run:tools/read-published-fig4.py",
      "kind": "flag",
      "status": "unruled",
      "decision": null,
      "message": "FLAG: the executor ran tools/read-published-fig4.py on the host before the final run (python3 -I tools/read-published-fig4.py <fig-000.jpg> > published-values/fig4-cells.csv): credit comes only from sealed outputs, but invariant 5 is an environment rule, so a human rules on it"
    },
    {
      "slug": "herskind-riede-2024",
      "id": "host-run:tools/read-published-fig2.py",
      "kind": "flag",
      "status": "unruled",
      "decision": null,
      "message": "FLAG: the executor ran tools/read-published-fig2.py on the host before the final run (python3 -I tools/read-published-fig2.py <fig-000.jpg> > published-values/fig2-left.csv): credit comes only from sealed outputs, but invariant 5 is an environment rule, so a human rules on it"
    }
  ],
  "unruled": 6
}
