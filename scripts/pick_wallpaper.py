#!/usr/bin/env python3
"""Pick a random JPEG from images/ and copy it to wallpaper.jpg."""

from __future__ import annotations

import random
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = ROOT / "images"
TARGET = ROOT / "wallpaper.jpg"

VALID_EXTENSIONS = {".jpg", ".jpeg", ".JPG", ".JPEG"}


def find_candidates() -> list[Path]:
    return [
        p
        for p in IMAGES_DIR.iterdir()
        if p.is_file() and p.suffix in VALID_EXTENSIONS
    ]


def main() -> int:
    candidates = find_candidates()

    if not candidates:
        raise SystemExit("No JPEG files found in images/. Add at least one .jpg or .jpeg file.")

    chosen = random.choice(candidates)
    shutil.copyfile(chosen, TARGET)

    print(f"Selected: {chosen.name}")
    print(f"Updated:  {TARGET.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
