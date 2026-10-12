"""Read the published Fig. 2 bar chart segment by segment (transcription aid, host-side).

Purpose
    Transcribe the left panel of Herskind & Riede (2024) Fig. 2 (artefact
    types stacked by chronology) for comparison target T04: for each of the
    18 bars, the colour segments from left to right and their lengths in
    objects. It reads only the publisher's figure image; it runs no authors'
    code and computes nothing from the data.

Input
    The figure's embedded image, extracted from the paper PDF (publisher
    content, never stored in the repository):
        pdfimages -j -f 3 -l 3 <corpus>/herskind-riede-2024/vor.pdf fig
    gives fig-000.jpg (1836 x 905 px, 300 ppi); the bar chart is x < 620.

Method
    Bars: pixel rows whose colour is near one of the four fill colours set in
    S2.R line 63 (#FAD02E Ertebolle, #D98888 Kongemose, #E8BB8B
    Kongemose/Ertebolle, #B4A1C1 Maglemose; levels in alphabetical order) are
    grouped into bars, top to bottom. Calibration: the panel's vertical
    gridlines (major lines at 0, 25, 50, 75, 100 at x = 203.5, 283.0, 362.5,
    442.5, 522.0 px), i.e. 0 at x = 203.5 and 3.185 px per object. Along each
    bar's centre line, within the plot area (x from 0 to the panel's right
    edge at 549 px), a pixel belongs to the bar when it is within distance 70
    of a fill colour (the grey background and white gridlines are not), and
    takes the nearest fill colour; one-pixel runs (JPEG blur at a boundary)
    merge into the following run, and the remaining runs form segments. A
    segment's length is the difference of its rounded end positions in
    objects.

Usage
    python3 -I tools/read-published-fig2.py <fig-000.jpg> > published-values/fig2-left.csv
"""
import csv
import sys

import numpy as np
from PIL import Image

LABELS = ["axe", "shaft", "pendant", "dagger", "knife", "mattock-head", "point",
          "harpoon-head", "figurine", "long bone", "pick", "sleeve", "ulna dagger", "core",
          "flake", "plate", "slotted point", "other"]   # as printed, top to bottom
FILLS = {"Ertebølle": (250, 208, 46), "Kongemose": (217, 136, 136),
         "Kongemose/Ertebølle": (232, 187, 139), "Maglemose": (180, 161, 193)}
X0, PPU = 203.5, (522.0 - 203.5) / 100.0


X_RIGHT = 549   # right edge of the bar-chart panel (the map starts beyond it)


def classify(pixels: np.ndarray) -> list[str]:
    """Nearest fill colour for each bar pixel, or '' for background."""
    names = list(FILLS)
    dist = np.stack([np.sqrt(((pixels - np.array(FILLS[n])) ** 2).sum(axis=-1))
                     for n in names])
    best = dist.argmin(axis=0)
    return [names[b] if dist[b, i] < 70 else "" for i, b in enumerate(best)]


def main(path: str) -> None:
    """Write one CSV row per bar segment to standard output."""
    rgb = np.asarray(Image.open(path).convert("RGB")).astype(int)[:, :620]
    near = np.stack([np.sqrt(((rgb - np.array(c)) ** 2).sum(axis=-1))
                     for c in FILLS.values()]).min(axis=0) < 35
    rows = near.sum(axis=1)
    bars, start = [], None
    for y, n in enumerate(rows):
        if n > 5 and start is None:
            start = y
        elif n <= 5 and start is not None:
            if y - start > 20:
                bars.append((start + y - 1) // 2)
            start = None
    if len(bars) != len(LABELS):
        sys.exit(f"found {len(bars)} bars, expected {len(LABELS)}")
    out = csv.writer(sys.stdout, lineterminator="\n")
    out.writerow(["bar_rank", "artefact_type", "segment_order", "chronology", "start", "end",
                  "count"])
    for rank, (label, y) in enumerate(zip(LABELS, bars), start=1):
        x_left = int(X0) - 1
        cls = classify(rgb[y - 3:y + 4, x_left:X_RIGHT].mean(axis=0))
        runs = []
        for i, c in enumerate(cls):
            x = x_left + i
            if not c:
                continue
            if runs and runs[-1][0] == c and runs[-1][2] == x - 1:
                runs[-1][2] = x
            else:
                runs.append([c, x, x])
        # Merge one-pixel blur runs into the following run.
        merged = []
        for j, r in enumerate(runs):
            if r[2] == r[1] and j + 1 < len(runs) and runs[j + 1][1] == r[2] + 1:
                runs[j + 1][1] = r[1]
                continue
            merged.append(r)
        runs = merged
        order = 0
        for c, a, b in runs:
            start_u = round((a - 0.5 - X0) / PPU)
            end_u = round((b + 0.5 - X0) / PPU)
            if end_u - start_u <= 0:
                continue
            order += 1
            out.writerow([rank, label, order, c, start_u, end_u, end_u - start_u])


if __name__ == "__main__":
    main(sys.argv[1])
