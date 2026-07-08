#!/usr/bin/env python3
"""Pick a random JPEG from images/ and copy it to wallpaper.jpg."""

from __future__ import annotations

import json
import random
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = ROOT / "images"
TARGET = ROOT / "wallpaper.jpg"
MANIFEST = ROOT / "images.json"

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

    # Keep a machine-readable list for random.html so redirects always match real files.
    manifest_entries = [f"images/{p.name}" for p in sorted(candidates, key=lambda p: p.name)]
    MANIFEST.write_text(json.dumps(manifest_entries, indent=2) + "\n", encoding="utf-8")

    chosen = random.choice(candidates)
    shutil.copyfile(chosen, TARGET)

    print(f"Selected: {chosen.name}")
    print(f"Updated:  {TARGET.name}")
    print(f"Updated:  {MANIFEST.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
