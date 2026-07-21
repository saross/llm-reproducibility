#!/usr/bin/env python3
"""Generate the Cosmos form paste file from the verified working draft.

Extracts every paste block from wiki/planning/cosmos-application-draft.md
(so the paste file cannot diverge from the verified text), strips markdown,
unwraps hard line-breaks to one flowing line per paragraph (Airtable text
boxes render pasted line-breaks literally), and emits a plain-text file
with fields in form order, NOTE: lines clearly separated from copy text.
"""

import re
import sys
from pathlib import Path

REPO = Path("/home/shawn/Code/llm-reproducibility")
DRAFT = REPO / "wiki/planning/cosmos-application-draft.md"

sys.path.insert(0, str(REPO / "studies/open-science-compliance/prereg"))
unwrap_mod = {}
exec((REPO / "studies/open-science-compliance/prereg/unwrap-paste-file.py")
     .read_text(), unwrap_mod)
unwrap = unwrap_mod["unwrap"]

text = DRAFT.read_text()


def strip_md(s: str) -> str:
    """Remove bold/italic markers and backticks; keep dashes and unicode."""
    s = s.replace("**", "")
    s = re.sub(r"(?<!\w)\*(?!\s)([^*]+?)(?<!\s)\*(?!\w)", r"\1", s)
    s = s.replace("`", "")
    s = s.replace("<https://", "https://").replace(">", "") if s.strip().startswith("<http") else s
    return s


def section(start_pat: str, end_pat: str) -> str:
    """Return raw text between the first match of start_pat and end_pat."""
    m = re.search(start_pat, text)
    if not m:
        sys.exit(f"start not found: {start_pat}")
    rest = text[m.end():]
    e = re.search(end_pat, rest)
    if not e:
        sys.exit(f"end not found: {end_pat}")
    return rest[: e.start()]


def quoted(block: str) -> str:
    """Strip '> ' quote prefixes, drop placeholder lines, strip markdown."""
    out = []
    for line in block.splitlines():
        if line.startswith(">"):
            line = line[1:].lstrip()
            if line.startswith("[then the field 19"):
                continue
            out.append(strip_md(line))
        elif not line.strip():
            out.append("")
    return unwrap("\n".join(out)).strip()


def numbered_items(block: str) -> list[str]:
    """Split a wrapped numbered list into unwrapped items, markdown stripped."""
    items, current = [], None
    for line in block.splitlines():
        if re.match(r"^\d+\. ", line):
            if current:
                items.append(current)
            current = re.sub(r"^\d+\. ", "", line).strip()
        elif current is not None and line.strip():
            current += " " + line.strip()
        elif current is not None and not line.strip():
            items.append(current)
            current = None
    if current:
        items.append(current)
    return [re.sub(r"  +", " ", strip_md(i)) for i in items]


# --- extractions ---------------------------------------------------------
body = section(r"<!-- proposal-body-start -->\n", r"<!-- proposal-body-end -->")
body = strip_md(body).strip()          # already one line per paragraph

f19_evidence = quoted(section(r"## Field 19 draft[^\n]*\n", r"### Supporting bibliography"))
biblio_raw = section(r"### Supporting bibliography[^\n]*\n", r"\n## ")
biblio_lines = []
current = None
for line in biblio_raw.splitlines():
    if line.startswith("- "):
        if current:
            biblio_lines.append(current)
        current = line[2:].strip()
    elif current is not None and line.strip():
        current += " " + line.strip()
if current:
    biblio_lines.append(current)
biblio = "\n".join(strip_md(re.sub(r"  +", " ", b)) for b in biblio_lines)

f18 = quoted(section(r"### Field 18 paste block\n", r"### Field 19 paste block"))
f19_links = quoted(section(r"### Field 19 paste block[^\n]*\n", r"\n## "))

titles = numbered_items(section(r"### Project title \(field 15\)\n", r"### One-sentence"))
oneliners = numbered_items(section(r"### One-sentence description \(field 16\)\n", r"### Self-pitch"))
pitch_block = section(r"### Self-pitch[^\n]*\n", r"Credential fragments")
pitches = numbered_items(pitch_block)

# --- validations ---------------------------------------------------------
BODY_WORDS = len(body.split())
assert BODY_WORDS < 500, f"body over the form limit: {BODY_WORDS} words"
assert len(titles) == 3 and len(oneliners) == 2 and len(pitches) == 2, \
    (len(titles), len(oneliners), len(pitches))
for name, blob in [("body", body), ("f18", f18), ("f19", f19_evidence),
                   ("links", f19_links)]:
    assert "**" not in blob and "> " not in blob, f"markdown residue in {name}"

# --- compose -------------------------------------------------------------
BAR = "=" * 72


def field(header: str, *chunks: str) -> str:
    return f"{BAR}\n{header}\n{BAR}\n\n" + "\n\n".join(c for c in chunks if c) + "\n\n"


out = []
out.append("""COSMOS GRANTS APPLICATION - FORM PASTE FILE
Generated 2026-07-21 from wiki/planning/cosmos-application-draft.md v0.7
(claim-verified by two independent passes; regenerate with
scratchpad build script if the draft changes).

How to use: fields appear in form order. Lines beginning NOTE: are
comments and are never pasted. Copy text sits alone between blank
lines, one unwrapped line per paragraph, plain text throughout (form
text boxes render pasted line-breaks literally). ALTERNATE blocks are
options, not additions.
""")

out.append(field("FIELDS 1-5 - First name / Last name / Email / Phone / Location (required)",
    "NOTE: factual, no drafted text. Suggested email shawn@fieldnote.au (CV\n"
    "NOTE: contact). Location: Sydney, NSW, Australia. CHECK THE PHONE - the CV\n"
    "NOTE: letterhead renders '+61 1 04 758 300', which looks like a typo."))

out.append(field("FIELD 6 - Pitch yourself in 1-2 sentences (required)",
    "NOTE: selected statement first (builder + scholar, no pipeline content -\n"
    "NOTE: the project lives in fields 16/17/19). Builder-only fragment kept\n"
    "NOTE: as fallback.",
    pitches[0],
    "ALTERNATE:",
    pitches[1]))

out.append(field("FIELD 7 - Website (optional)",
    "NOTE: no personal site on the CV. Options: EFN/Fieldmark company site\n"
    "NOTE: (supply URL) or leave blank."))

out.append(field("FIELD 8 - LinkedIn (optional)",
    "NOTE: supply or leave blank; the form says optional fields aid review."))

out.append(field("FIELD 9 - X (twitter) handle (optional)",
    "NOTE: supply or leave blank."))

out.append(field("FIELD 10 - GitHub repository (optional)",
    "NOTE: visibility re-confirmed PUBLIC 2026-07-21.",
    "https://github.com/saross/llm-reproducibility"))

out.append(field("FIELD 11 - Substack (optional)",
    "NOTE: supply or leave blank."))

out.append(field("FIELD 12 - Resume / CV upload (optional)",
    "NOTE: upload ~/Downloads/Ross_CV_Cosmos_Institute.pdf (15 pp, tailored\n"
    "NOTE: copy). Fix the letterhead phone first if it is indeed a typo."))

out.append(field("FIELD 13 - Which stream are you applying to? (required, single select)",
    "NOTE: select the verbatim option below - it is a dropdown, not a text box.",
    "AI and Truth-seeking: Cosmos x FIRE"))

out.append(field("FIELD 14 - Grant request ($) (required, integer, USD)",
    "NOTE: worked budget in the draft sums to this; lean variant 7000 without\n"
    "NOTE: honoraria.",
    "8000"))

out.append(field("FIELD 15 - Project title (required)",
    "NOTE: selected title first (statement-of-mission, no colon - the field 16\n"
    "NOTE: one-liner carries the explanation); colon-form alternates follow.",
    titles[0],
    "ALTERNATE:",
    titles[1],
    "ALTERNATE:",
    titles[2]))

out.append(field("FIELD 16 - 1 sentence project description (required)",
    "NOTE: recommended first; alternate follows.",
    oneliners[0],
    "ALTERNATE:",
    oneliners[1]))

out.append(field("FIELD 17 - Short proposal, under 500 words (required)",
    f"NOTE: {BODY_WORDS} words including the five section labels (limit <500).\n"
    "NOTE: Paste everything below this note block.",
    body))

out.append(field("FIELD 18 - Collaborators (optional)",
    "NOTE: LIVE FORM (2026-07-21): a long-text box - paste the full block\n"
    "NOTE: below, not just the name.",
    f18))

out.append(field("FIELD 19 - Project website / additional info (optional)",
    "NOTE: LIVE FORM DELTA (2026-07-21): renders links only, no long text.\n"
    "NOTE: The evidence pack is published at docs/cosmos-evidence-pack.md\n"
    "NOTE: instead; paste these links, one per line.",
    "https://github.com/saross/llm-reproducibility\n"
    "https://osf.io/dqnhg/\n"
    "https://github.com/saross/llm-reproducibility/blob/main/docs/cosmos-evidence-pack.md"))

out.append(field("FIELD 20 - How did you hear about Cosmos Grants? (required)",
    "NOTE: factual - the help text asks for the names of any person or\n"
    "NOTE: organisation recommending you. Shawn supplies."))

out.append(field("FIELD 21 - Applicant Agreement (required, checkbox)",
    "NOTE: tick to consent. Submitters are auto-added to the Cosmos Substack\n"
    "NOTE: (unsubscribable)."))

dest = REPO / "wiki/planning/cosmos-application-form-paste.txt"
dest.write_text("\n".join(out))
print("written:", dest)
print("field 17 words:", len(body.split()))
EOF_SENTINEL_NOT_USED = None
