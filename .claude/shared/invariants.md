# Pipeline invariants v1.0 — canonical file

**Status: FROZEN by OSF registration 2026-07-20 (DOI 10.17605/OSF.IO/DQNHG)** —
anchored in preregistration §8 (Docker execution, fresh-context adversarial
review, orchestrator-verified persistence, batched human plan approval);
changes require the §8 regression gate + an erratum-log entry + an OSF
amendment before any affected analysis runs.
**Version:** 1.0 (the six invariants of agentic-modernisation plan §4.3,
preserved from reproduction protocol v1.1; extracted 2026-07-24)
**Canonical home** per routing design §4 — deliberately outside
`.claude/agents/` (that tree is parsed as agent definitions; review D7).
**Consumers:** `reproduction-planner`, `reproduction-executor`, and
`adversarial-reviewer` (pushed, with read receipt); registered in
`manifest.yaml` `shared_content`.

---

## The six invariants (non-negotiable)

1. Plan before execution; **human approval of plans** before any compute spend
   (batched).
2. Change *how* code runs, never *what* it computes (wrapper cardinal rule).
3. Every verification target accounted for — no silent scope reduction.
4. Adversarial review runs for **every** paper, always in a fresh context.
5. All execution inside Docker; host contamination is a review-detectable
   failure.
6. Artefact persistence verified by the orchestrator, not asserted by the
   agent.

## Operational corollaries

- Invariant 1 binds the planner: no execution stage may begin from an
  unapproved plan; approval is batched (triage report; approve/hold/reject per
  paper — modernisation plan §4.4).
- Invariant 2 binds the executor: wrapper scripts may change execution
  mechanics (paths, batching, output capture) but never statistical methods,
  parameters, data filtering, model specifications, or analysis steps.
- Invariant 3 is enforced by the denominator lock (`coverage-rules.md`).
- Invariant 4 is enforced structurally: the adversarial reviewer is spawned
  with no shared context and an artefacts-only tools allowlist.
- Invariants 5–6 are enforced by deterministic stage gates: image builds,
  scripts parse, expected artefacts exist and are non-empty, queue updated —
  checked by the orchestrator, never taken from agent self-report.
- On missing input, unreadable file, or ambiguity outside its brief, an agent
  emits `status: ESCALATE` with a reason and stops — escalate, don't improvise.

---

Receipt-token: f847020d25d57382
