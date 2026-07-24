#!/usr/bin/env python3
"""
make_event_dds.py - turn any image into a HOI4 event picture.

Sizes and format are taken from the vanilla files, not guessed:

    report  210 x 176   (country events, GFX_report_event_*)
    news    397 x 153   (news events,    GFX_news_event_*)

Both are uncompressed 32-bit A8R8G8B8 with no mipmap chain, which is
what this writes.

Usage
-----
    python make_event_dds.py photo.jpg report out.dds
    python make_event_dds.py photo.jpg news   out.dds

    # custom size if you ever need one
    python make_event_dds.py photo.jpg 400x200 out.dds

    # blank transparent placeholder, no input image
    python make_event_dds.py --blank report out.dds

The image is scaled to cover the target and centre-cropped, so it
fills the slot without being stretched out of shape. Use --fit
instead if you'd rather letterbox than crop.

Requires Pillow:  pip install pillow
"""

import argparse
import struct
import sys

SIZES = {"report": (210, 176), "news": (397, 153)}


def parse_size(token):
    if token in SIZES:
        return SIZES[token]
    if "x" in token.lower():
        w, h = token.lower().split("x", 1)
        return int(w), int(h)
    raise argparse.ArgumentTypeError(
        f"size must be 'report', 'news', or WxH - got {token!r}"
    )


def dds_header(width, height):
    """128-byte header for uncompressed A8R8G8B8, matching vanilla."""
    flags = 0x1 | 0x2 | 0x4 | 0x8 | 0x1000     # CAPS HEIGHT WIDTH PITCH PIXELFORMAT
    h = b"DDS "
    h += struct.pack("<I", 124)                # header size
    h += struct.pack("<I", flags)
    h += struct.pack("<I", height)
    h += struct.pack("<I", width)
    h += struct.pack("<I", width * 4)          # pitch
    h += struct.pack("<I", 0)                  # depth
    h += struct.pack("<I", 0)                  # mipmap count
    h += b"\x00" * 44                          # reserved1[11]
    h += struct.pack("<I", 32)                 # pixelformat size
    h += struct.pack("<I", 0x1 | 0x40)         # ALPHAPIXELS | RGB
    h += struct.pack("<I", 0)                  # fourCC (none)
    h += struct.pack("<I", 32)                 # bits per pixel
    h += struct.pack("<I", 0x00FF0000)         # R mask
    h += struct.pack("<I", 0x0000FF00)         # G mask
    h += struct.pack("<I", 0x000000FF)         # B mask
    h += struct.pack("<I", 0xFF000000)         # A mask
    h += struct.pack("<I", 0x1000)             # caps: plain texture
    h += b"\x00" * 16                          # caps2/3/4 + reserved2
    assert len(h) == 128
    return h


def write_dds(img, path, size):
    """img is a Pillow RGBA image already at `size`, or None for blank."""
    w, h = size
    if img is None:
        body = b"\x00" * (w * h * 4)
    else:
        # A8R8G8B8 little-endian == B, G, R, A byte order on disk
        r, g, b, a = img.split()
        from PIL import Image
        body = Image.merge("RGBA", (b, g, r, a)).tobytes()
    with open(path, "wb") as fh:
        fh.write(dds_header(w, h) + body)
    print(f"wrote {path}  {w}x{h}  {128 + w * h * 4:,} bytes")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", nargs="?", help="input image (omit with --blank)")
    ap.add_argument("size", type=parse_size, help="report | news | WxH")
    ap.add_argument("output", help="output .dds path")
    ap.add_argument("--blank", action="store_true",
                    help="write a fully transparent placeholder, ignore source")
    ap.add_argument("--fit", action="store_true",
                    help="letterbox instead of centre-cropping")
    args = ap.parse_args()

    if args.blank:
        write_dds(None, args.output, args.size)
        return

    if not args.source:
        ap.error("need a source image unless --blank is given")

    try:
        from PIL import Image, ImageOps
    except ImportError:
        sys.exit("Pillow is required:  pip install pillow")

    img = Image.open(args.source).convert("RGBA")
    if args.fit:
        img = ImageOps.pad(img, args.size, color=(0, 0, 0, 0))
    else:
        img = ImageOps.fit(img, args.size, method=Image.LANCZOS)
    write_dds(img, args.output, args.size)


if __name__ == "__main__":
    main()
