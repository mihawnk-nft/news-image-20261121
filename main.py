#!/usr/bin/env python3
"""news-image-20261121 entrypoint.

The poster itself lives in this repository as entry.png (a 1024x1024
picture of Saturday 21 November 2026 world news, drawn at build time
from the research in NEWS-RESEARCH.md). This program does the one job
the competition asks of it: place that picture at the path the grader
reads, with exactly the same bytes every run.

It needs no network and no third-party package: the standard library
alone copies the file. The destination folder comes from the
MAKEFUN_OUTPUT_DIR environment variable and falls back to /output.
"""

import hashlib
import os
import shutil
import sys

PICTURE_NAME = "entry.png"
OUTPUT_ENV_VAR = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
# The eight bytes every PNG file starts with. Checked before the copy
# so a damaged or swapped picture fails loudly instead of being
# submitted as if it were the poster.
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def picture_path():
    """Absolute path of the picture shipped beside this script."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, PICTURE_NAME)


def digest(path):
    """SHA-256 hex of a file, read in chunks."""
    hasher = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def place_picture(source, out_dir):
    """Copy the picture into out_dir and prove the copy is exact."""
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, PICTURE_NAME)
    shutil.copyfile(source, target)
    if os.path.getsize(target) != os.path.getsize(source):
        raise SystemExit("copy size mismatch: %s" % target)
    if digest(target) != digest(source):
        raise SystemExit("copy checksum mismatch: %s" % target)
    return target


def main():
    source = picture_path()
    if not os.path.isfile(source):
        raise SystemExit("missing picture: %s" % source)
    with open(source, "rb") as handle:
        header = handle.read(len(PNG_SIGNATURE))
    if header != PNG_SIGNATURE:
        raise SystemExit("not a PNG picture: %s" % source)
    out_dir = os.environ.get(OUTPUT_ENV_VAR, DEFAULT_OUTPUT_DIR)
    target = place_picture(source, out_dir)
    size = os.path.getsize(target)
    print("%s (%d bytes, sha256 %s) -> %s"
          % (PICTURE_NAME, size, digest(target), target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
