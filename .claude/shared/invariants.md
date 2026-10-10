# Pipeline invariants v1.1 — canonical file

**Status: FROZEN by OSF registration 2026-07-20 (DOI 10.17605/OSF.IO/DQNHG)** —
anchored in preregistration §8 (Docker execution, fresh-context adversarial
review, orchestrator-verified persistence, batched human plan approval);
changes require the §8 regression gate + an erratum-log entry + an OSF
amendment before any affected analysis runs. v1.1 applies OSF amendment 3
§7(d) (lodged 2026-10-08) under erratum-log Entry 6.
**Version:** 1.1 (the invariant 2 corollary of amendment 3 §7(d), 2026-10-09;
v1.0: the six invariants of agentic-modernisation plan §4.3,
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

## Invariant 2: routine and fail-and-uplift (v1.1, amendment 3 §7(d))

Quoted from OSF amendment 3 (lodged 2026-10-08, revision
`6ac775afb5ed5b4afee88a4a`, tag `osf-amendment-3-2026-10-08`), word for word,
with the amendment's own reading where it gives one. Section numbers inside
are amendment 3's.

Routine (execution environment): choosing among publicly available versions of
dependencies and language runtimes, meaning releases from the package's
official archive (for example CRAN or PyPI) or a tagged public repository,
preferring the version current at publication. The search and the chosen
versions are recorded. Fail-and-uplift: any edit to the authors' code that
changes logic, indices, data selection, parameters, or the functions called,
however obvious the intent. A deprecated function is handled by pinning a
public version that still runs it; if none exists, replacing it is an edit,
and so fail-and-uplift. A repaired result is recorded as uplift evidence and
never counts toward coverage or the verdict.

- **Supplied pins take precedence.** The authors' environment specification is
  built as supplied, as the preparation procedure already does, so a lockfile
  is restored, a container specification is built, and an explicit runtime or
  package version is used. Whether a component is specified is judged per
  dependency, not per project, because a container image can pin the runtime
  and a package snapshot date without naming each package. The version search
  below governs what the specification leaves unspecified, anchored on the
  release current at publication, and a specified component whose build fails,
  anchored on its supplied pin. Each such fallback is logged against the
  component. The run reports, beside the verdict (section 8(a)), whether the
  pins were honoured in full, with how many fallbacks, or not at all. Supplied
  pins keep precedence so that registered H3, which compares build effort
  between pinned and unpinned environments, measures the authors' pins and not
  a reconstructed environment.
- **Version-search cap.** A specified dependency is first built at its
  supplied pin, and an unspecified dependency at the release current at the
  article's first online appearance. If a dependency fails to build at that
  anchor, its immediately preceding release is tried, then its immediately
  following release, stopping at the first that builds, so a dependency has at
  most three attempts. A failed pin is never replaced by the release current
  at publication. Where a repository publishes commits but no releases, the
  release current at publication is the last commit on the default branch at
  or before first online appearance, and a pinned commit is its own anchor.
  The adjacent attempts are the nearest earlier and later commits that change
  the package's declared version, or, where none does, that change the
  package's files. The cap governs build failures only. A deprecated function
  is handled by a separate logged search backwards to the last public release
  that still carries it, without this cap. Each attempt is logged.
- **Wrapper boundary cases.** Mechanics are applied in wrappers only, never in
  the authors' files. They are recorded, and they include: setting a random
  seed where the authors set none (stochastic tolerances still apply);
  converting an input file's format, allowed only when a mechanical check
  confirms every value is unchanged (any change of value is fail-and-uplift);
  and choosing the language runtime version, which is routine like any
  dependency.
- **Mechanics placed in an authors' file (RULED 2026-10-05).** A mechanical
  change made inside an authors' file rather than in a wrapper, such as a
  changed input path, breaks the wrapper rule even when it changes nothing
  computed. A result that rests on such a file does not count toward coverage
  or the verdict until it is re-run with the mechanics moved into a wrapper
  and the authors' file restored byte-identical. A change of logic, indices,
  data selection, parameters, or functions called remains fail-and-uplift
  whatever its effect, including a restructuring that gives the same result.
- **Further boundary cases (RULED 2026-10-05, executed-code audit Q6).** A
  wrapper may make an authors' statement error-tolerant only where the
  statement computes nothing that enters a result, such as registering a font;
  the tolerance is declared, and the run log records whether it fired.
  Per-section error capture is routine, but a target is credited only from a
  section that completed without error and whose inputs come only from
  sections that also completed. Sections may run in another order only when
  they are independent, none reading an object another defines; otherwise
  re-ordering changes the execution logic and is fail-and-uplift. A dependency
  fetched from a public repository is installed when the environment is built,
  pinned to a tagged release or, where the repository has none, to a recorded
  commit, preferring the one current at publication. An unpinned install at
  run time is not routine. Independence between sections is judged on every
  state a section can pass to another, namely named objects, files written and
  read, global options, and random-number state. The dependency sentence is
  read with the precedence rule above, so where the authors pinned the
  dependency, their pin is used.
- **Verification aids and reconstructed inputs (RULED 2026-10-05,
  executed-code audit Q5).** Where no authors' code produces a published
  result, the reproducer may test it with a labelled verification aid: a
  read-only lookup in the deposited data, or a call to a documented function
  of the package the authors used, making no new statistical choice. A formula
  the reproducer infers from the paper's wording qualifies only where it
  reproduces the paper's own printed values from the paper's own printed
  inputs, and it is credited only where its inputs come from executing the
  authors' code. A result resting on inputs the reproducer reconstructed, for
  example from upstream datasets the authors cite, never counts toward
  coverage or the verdict: the target stays in the denominator as
  expected-untestable, and the reconstructed result is reported as uplift
  evidence. A printed value that the formula does not reproduce is never
  credited and goes to the paper-error protocol of section 7(a), as the ruling
  directs for its two inconsistent cells.

---

Receipt-token: c70d484af7e75ec4
