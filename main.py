#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — one fortune-cookie line.

Writes the line to /output/entry.txt (UTF-8, 75 Unicode code points,
inside the 1-120 gate). Deterministic, standard library only, no network.

The line itself: Your future self is already on call for the shortcut
you are about to ship. It reads like a real fortune cookie — a quiet
warning phrased as fate — and it is true about a developer's day: every
shortcut becomes an incident, and the person paged for it is the same
person who shipped it, just older and more tired.
"""

import os

TEXT = "Your future self is already on call for the shortcut you are about to ship."


def main() -> None:
    # The grader mounts /output; create it defensively for local runs too.
    # TEXT is exactly 75 Unicode code points: inside the 1-120 gate.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
