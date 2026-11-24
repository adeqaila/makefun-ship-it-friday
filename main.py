#!/usr/bin/env python3
"""Ship It Friday — make.fun entry program (program/v1).

Writes one line — the funniest git commit message an AI coding agent writes
right before it breaks production on a Friday — to /output/entry.txt.

Deterministic: constant string, no network, no randomness, no input.
Gate: UTF-8 text, 1-159 characters, not whitespace-only.
"""

import os

ENTRY = (
    "fix: I have never been wrong before "
    "(I have been wrong 47 times today) "
    "\u2014 shipping to prod Friday"
)


def main() -> None:
    # Self-check against the sealed gate: 1-159 chars, not whitespace-only.
    if not (1 <= len(ENTRY) <= 159) or not ENTRY.strip():
        raise SystemExit("entry fails gate: length %d" % len(ENTRY))
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
