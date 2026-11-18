"""Deliver the bundled front page to the folder the grader reads.

The picture itself, entry.png, lives next to this file. Nothing here
is generated at run time: the program only places a copy of that
picture where the grading harness looks for it, using the standard
library alone. No network is involved, and repeating the run writes
the same bytes again, so both grading runs see the identical image.
"""

from os import environ
from pathlib import Path


def ship():
    """Copy entry.png beside this file into the output directory."""
    folder = Path(__file__).resolve().parent
    picture = folder / "entry.png"
    if not picture.is_file():
        raise SystemExit("entry.png is missing next to main.py")
    destination = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "entry.png").write_bytes(picture.read_bytes())


ship()
