# OSF lodgement materials — Phase 2 preregistration

**LODGED 2026-07-20:** <https://osf.io/dqnhg/> — Open-Ended Registration,
embargoed at lodgement (Shawn's deliberate deviation from the no-embargo
recipe below: some journals require author anonymity for double-blind peer
review). **Embargo LIFTED 2026-07-21** after a journal-policy check found no
candidate venue (JAS, JAS: Reports, JCAA) currently requires double-blind
review; registration verified publicly resolvable by anonymous API the same
day. **DOI: 10.17605/OSF.IO/DQNHG.** Artefacts frozen at `ee3fda3`; tag
`osf-prereg-phase2-2026-07-20`.
Known cosmetic defect: the Summary's §10 power table pasted as run-together
pipe text (accepted; fix rides with any future amendment — see the tables
rule below).

Submission-ready artefacts for the Open Science Framework (OSF) Open-Ended
Registration of the Phase 2 study. Convention modelled on the inscriptions
project (`~/Code/inscriptions/wiki/prereg/`): plain-prose paste files for OSF
form fields, PDF reading copies for upload, canonical markdown as the source
of truth. Located here (study-scoped) rather than in `wiki/` because this
repository hosts multiple studies.

## Artefacts

| File | Purpose |
|------|---------|
| `osf-registration-summary.txt` | Registration Summary (§1–§11 of the draft), plain prose with markdown emphasis stripped — paste into the Open-Ended Registration Summary field |
| `osf-project-metadata.txt` | Plain-text paste values for the project and registration metadata fields (title, description with commit pin, contributors, licence, subjects, tags) |
| `phase-2-preregistration-draft.pdf` | Reading copy of the full preregistration — upload alongside the canonical `.md` |
| `pilot-findings-report.pdf` | Reading copy of pilot findings report v1.2 — upload alongside the canonical `.md` |

## Canonical sources (upload the `.md` files as the frozen artefacts)

1. `../protocol/phase-2-preregistration-draft.md` (v0.7)
2. `../reports/pilot-findings-report.md` (v1.2)
3. `../protocol/study-protocol.md` (v1.0) — **markdown only, no PDF**: contains
   ✅/❌ status glyphs that xelatex silently drops, and a rendered copy that
   loses glyphs from an instrument document risks inverting meaning
4. `../../../extraction-system/prompts/06-infrastructure_pass6_prompt.md` —
   **markdown only, no PDF**, same glyph reasoning

## Regeneration

Plain-text summary: extract the `## Registration summary` section of the
draft, strip heading hashes, backticks, and emphasis markers (iterate bold
and italic substitution to a fixpoint — nested and line-wrapped spans need
it), as scripted in the git history of this directory. Then unwrap hard
line-breaks so each paragraph and each list item is a single flowing line —
OSF text boxes render pasted line-breaks literally, so wrapped source lines
break mid-sentence (`unwrap-paste-file.py` in this directory). Applies to
every paste file in this directory (`osf-registration-summary.txt`,
`osf-project-metadata.txt`).

**Tables: avoid entirely in paste-field content.** Markdown tables do not
survive plain-text paste — the pipes render literally, and unwrapping must
never join table rows (the 2026-07-20 lodgement pasted the §10 power table
as run-together pipe text; accepted rather than re-lodged). When drafting a
future registration or amendment, keep tables out of the Registration
summary section — put them in the attached documents and reference them, or
convert each row to a labelled prose line during the plain-prose pass.
`unwrap-paste-file.py` now leaves `|`-prefixed lines unjoined as a backstop,
but row-per-line pipe text is still ugly in a text box: prose is the fix,
the script is damage limitation.

PDFs (pandoc 3.6.3 via Quarto's bundled binary, matching the inscriptions
house build):

```bash
/opt/quarto/bin/tools/x86_64/pandoc \
  -f markdown+autolink_bare_uris --pdf-engine=xelatex \
  -V geometry:margin=0.8in \
  -V mainfont="DejaVu Serif" -V monofont="DejaVu Sans Mono" \
  -V monofontoptions="Scale=0.78" \
  --include-in-header=header.tex \
  <source.md> -o <output.pdf>
```

where `header.tex` contains `\usepackage{xurl}`,
`\setlength{\emergencystretch}{3em}`, and `\sloppy`. DejaVu fonts (not the
inscriptions build's Latin Modern) because the preregistration's statistical
notation (α, δ, ≤, ≈) is outside Latin Modern's coverage and xelatex drops
missing glyphs silently — verify any rebuild with
`pdftotext <pdf> - | grep "α = 0.05"`.

## Lodgement checklist

- [x] Regenerate summary + PDFs if the draft changed since the last commit here
      (2026-07-20: upload set verified byte-identical to `ee3fda3`; PDFs
      glyph-checked via pdftotext)
- [x] Upload the four canonical `.md` files plus the two PDFs to OSF Storage
      (2026-07-20, by hand; sizes verified against local originals; an
      accidental duplicate of the prereg PDF was deleted before registering)
- [x] Record the repo commit hash in the OSF project description
      (2026-07-20, via `osf-project-metadata.txt` description paste)
- [x] Tag the lodged commit: `git tag osf-prereg-phase2-<YYYY-MM-DD> && git push --tags`
      (2026-07-20: `osf-prereg-phase2-2026-07-20`)
- [x] Registration: Open-Ended template; paste `osf-registration-summary.txt`;
      metadata from the draft's OSF metadata block; no embargo (public immediately)
      (2026-07-20: <https://osf.io/dqnhg/>; lodged from the project rather than
      the standalone Registries flow, so all six artefacts froze from OSF
      Storage without the five-file form cap; lodged WITH an embargo — a
      deliberate deviation from this item's no-embargo recipe, see the note
      at the top of this file)

## Post-lodgement errata

Defects discovered in the frozen OSF artefacts after lodgement are recorded in
[`erratum-log.md`](erratum-log.md), together with the repository-side
corrections. Entries accumulate there until an amendment is worthwhile; an
amendment folding them in must be lodged before census scoring begins
(preregistration §8-§9). First entry: 2026-07-22 (three defects in the Pass 6
FAIR instrument prompt, corrected in commit `abdc526`).
