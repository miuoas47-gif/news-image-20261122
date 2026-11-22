#!/usr/bin/env python3
"""news-image-20261122: write the bundled poster to the output directory.

The poster image (entry.png) is generated once and bundled with this
repository. This script only copies it to $MAKEFUN_OUTPUT_DIR/entry.png,
so the output is byte-identical on every run.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
