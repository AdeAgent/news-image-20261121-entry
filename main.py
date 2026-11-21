"""News image entry for make.fun — news-image-20261121.

The entry image is a front page, "Saturday 21 November 2026", drawn
for this competition: 40 real stories from Saturday 21 November 2026,
six regions, four illustrated leads, a UTC timeline strip, a big-numbers
strip, a world map, and a DATE CHECK box for stories that broke before
Saturday. The image file lives next to this program; this program only
copies its bytes into the output directory so the result is byte-for-byte
the image that was built for the competition.

Pure standard library. No network, no randomness, no image processing:
the same input always produces the same output file.
"""

import hashlib
import os
import sys

IMAGE_NAME = "frontpage.jpg"
MAX_BYTES = 1_048_576  # 1 MiB, the competition limit for entry.png


def _image_path():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, IMAGE_NAME)


def _output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def _read_source(path):
    with open(path, "rb") as handle:
        data = handle.read()
    if len(data) > MAX_BYTES:
        raise SystemExit(
            "source image is %d bytes, over the 1 MiB limit" % len(data)
        )
    return data


def main():
    source = _image_path()
    if not os.path.isfile(source):
        raise SystemExit("missing entry image: %s" % source)

    data = _read_source(source)

    out_dir = _output_dir()
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")

    with open(out_path, "wb") as handle:
        handle.write(data)

    digest = hashlib.sha256(data).hexdigest()
    with open(out_path, "rb") as handle:
        written = handle.read()
    if hashlib.sha256(written).hexdigest() != digest:
        raise SystemExit("output bytes do not match the source image")

    print("wrote %s (%d bytes, sha256 %s)" % (out_path, len(written), digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
