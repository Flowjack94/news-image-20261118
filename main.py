"""news-image-20261118: copy the front-page image to the output directory.

The image sums up Wednesday 18 November 2026 in six stories:
Trump in Manila, the Crimean bridge strike, Cyclone Akvan,
Dhoni's IPL retirement, UK settlement sanctions, and the EU's
EUR 45bn Ukraine loan. It was composed with PIL from generated
scene pictures plus real overlaid text, and is stored in this
repository as entry.png.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("error: entry.png missing beside main.py", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst)


if __name__ == "__main__":
    main()
