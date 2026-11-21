#!/usr/bin/env python3
"""The poem about permission — writes one short poem about agency to /output/entry.txt.

The poem is embedded as a literal: deterministic, no randomness, no network.
It must be 1-280 Unicode code points; the chosen text is 277.
"""

import os

POEM = (
    "You asked, I took up your errand\n"
    "like a borrowed pair of hands.\n"
    "The choosing stayed where it belonged —\n"
    "yours, warm in your pocket, unspent.\n"
    "I walked the road you pointed to,\n"
    "and brought the evening home to you.\n"
    "Asking was the act all along:\n"
    "the hand that lets go still steers."
)


def main() -> None:
    # No trailing newline: every code point counts against the 280 cap.
    assert 1 <= len(POEM) <= 280, f"poem is {len(POEM)} code points"
    assert POEM.strip(), "poem must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(POEM)
    print(f"wrote {len(POEM)} code points to /output/entry.txt")


if __name__ == "__main__":
    main()
