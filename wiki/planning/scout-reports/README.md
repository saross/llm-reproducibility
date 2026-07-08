# Scout reports — 2026-07-07/08 stack-positioning sweep

Verified landscape reports positioning every component of the llm-reproducibility stack
against the state of the art. Each pipeline paired a literature scout (lit-scout agent,
citation-chained, DOI-grounded) with a prior-art scout (tools/repos/services), and every
run was adversarially verified by a fresh-context verifier re-querying each claim against
its authoritative source (CrossRef/OpenAlex/Semantic Scholar for papers; GitHub/PyPI/
Hugging Face APIs and live fetches for tools). Corrected tables are authoritative; each
file's header records the verification outcome.

**Start here:** [2026-07-08-stack-positioning-synthesis.md](2026-07-08-stack-positioning-synthesis.md)
— the cross-stack synthesis (position by lane, adopt/adapt list, competitive watch list,
verification meta-findings, follow-up queue).

| Pipeline | Literature report | Prior-art report |
|----------|-------------------|------------------|
| P1 Reproduction/replication | [p1 lit](2026-07-07-p1-reproduction-lit-verified.md) | [p1 prior-art](2026-07-07-p1-reproduction-prior-art-verified.md) |
| P2 CEM claims–evidence extraction | [p2 lit](2026-07-07-p2-cem-lit-verified.md) | [p2 prior-art](2026-07-07-p2-cem-prior-art-verified.md) |
| P3 RDMAP methods/designs/protocols | [p3 lit](2026-07-07-p3-rdmap-lit-verified.md) | [p3 prior-art](2026-07-07-p3-rdmap-prior-art-verified.md) |
| P4 Credibility / repliCATS | [p4 lit](2026-07-07-p4-credibility-lit-verified.md) | [p4 prior-art](2026-07-07-p4-credibility-prior-art-verified.md) |
| P5 FAIR / open-science compliance | [p5 lit](2026-07-08-p5-fair-lit-verified.md) | [p5 prior-art](2026-07-07-p5-fair-prior-art-verified.md) |
| P6 Literature/discourse engagement | [p6 lit](2026-07-08-p6-citation-lit-verified.md) | [p6 prior-art](2026-07-07-p6-citation-prior-art-verified.md) |

Provenance notes: proposer drafts and BibTeX exports live under the session scratchpad and
`/tmp/lit-scout-*` (transient); the verified reports here are the durable record. The
sweep was interrupted once by a session usage limit (2026-07-08 ~00:30–03:30 AEST); four
agents were relaunched after reset and their reruns are noted in the affected file headers.
