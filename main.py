#!/usr/bin/env python3
"""news-image-20261118 v3 entrypoint.

Copies the front-page image (entry.png) that ships in this repository
into the output directory the grader reads. No network, no randomness,
no writes anywhere else: the image bytes are reproduced exactly.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    # The grader reads exactly one file: entry.png in the output dir.
    # MAKEFUN_OUTPUT_DIR names that dir; /output is the default.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    src = HERE / "entry.png"
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
