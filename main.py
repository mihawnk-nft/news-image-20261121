#!/usr/bin/env python3
"""Entrypoint for the news-image-20261121 make.fun entry.

The poster for Saturday 21 November 2026 is already drawn and shipped
in this repository as entry.png (1024x1024, six stories plus six
briefs). This script has a single responsibility: hand that picture
to the grader, byte for byte, at the location the grader reads.

How it works:
  * the picture is found next to this script, never via the working
    directory, so the result does not depend on where it is launched
  * the destination folder is taken from MAKEFUN_OUTPUT_DIR and
    defaults to /output when that variable is not set
  * only the Python standard library is used, and nothing touches
    the network, so the copy is deterministic on every run
  * after copying, the script checks the copy's size and SHA-256
    against the original and refuses to report success unless both
    match exactly
"""

import hashlib
import os
import shutil
import sys

IMAGE_FILENAME = "entry.png"
OUTPUT_DIR_ENV = "MAKEFUN_OUTPUT_DIR"
FALLBACK_OUTPUT_DIR = "/output"
READ_CHUNK = 65536
# Every PNG file opens with these eight bytes. Checking them before
# the copy means a damaged or accidentally swapped picture fails
# loudly here instead of being handed to the grader as the poster.
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def resolve_image_path():
    """Absolute path of the poster shipped beside this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, IMAGE_FILENAME)


def sha256_of(path):
    """Hex SHA-256 of a file, streamed so memory stays small."""
    digest = hashlib.sha256()
    with open(path, "rb") as stream:
        while True:
            block = stream.read(READ_CHUNK)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def deliver(source, destination_dir):
    """Copy the poster into destination_dir, proving it arrived intact."""
    os.makedirs(destination_dir, exist_ok=True)
    destination = os.path.join(destination_dir, IMAGE_FILENAME)
    shutil.copyfile(source, destination)
    source_size = os.path.getsize(source)
    if os.path.getsize(destination) != source_size:
        raise SystemExit(
            "size mismatch after copy: %s (%d bytes expected)"
            % (destination, source_size)
        )
    if sha256_of(destination) != sha256_of(source):
        raise SystemExit("checksum mismatch after copy: %s" % destination)
    return destination, source_size


def run():
    source = resolve_image_path()
    if not os.path.isfile(source):
        raise SystemExit("poster not found beside script: %s" % source)
    with open(source, "rb") as stream:
        magic = stream.read(len(PNG_MAGIC))
    if magic != PNG_MAGIC:
        raise SystemExit("poster is not a PNG file: %s" % source)
    destination_dir = os.environ.get(OUTPUT_DIR_ENV, FALLBACK_OUTPUT_DIR)
    destination, size = deliver(source, destination_dir)
    print(
        "%s: %d bytes, sha256 %s -> %s"
        % (IMAGE_FILENAME, size, sha256_of(destination), destination)
    )
    return 0


if __name__ == "__main__":
    sys.exit(run())
