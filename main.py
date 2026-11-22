#!/usr/bin/env python3
"""news-image-20261122 entry runner.

Copies the bundled poster (entry.png) from this script's own directory to
$MAKEFUN_OUTPUT_DIR/entry.png (default "output"), then verifies the copy is
byte-identical to the bundled image. Exits non-zero if anything is wrong.
Stdlib only, no arguments, deterministic.
"""
import hashlib
import os
import shutil
import sys

SOURCE_NAME = "entry.png"


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(script_dir, SOURCE_NAME)

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, SOURCE_NAME)

    if not os.path.isfile(source):
        print(f"error: bundled image not found: {source}", file=sys.stderr)
        return 1

    shutil.copyfile(source, destination)

    expected = sha256_of(source)
    actual = sha256_of(destination)
    if actual != expected:
        print(
            f"error: output verification failed: {destination} "
            f"sha256 {actual} != bundled {expected}",
            file=sys.stderr,
        )
        return 1

    print(f"copied {source} -> {destination} (sha256 {actual})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
