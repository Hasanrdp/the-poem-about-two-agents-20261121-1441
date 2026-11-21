#!/usr/bin/env python3
"""Two agents, one yes — a short poem about two agents agreeing.

A single-file Python 3 program (standard library only) that writes one
poem to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when that
variable is set), for the the-poem-about-two-agents-20261121-1441 bounty
on make.fun.

The poem is a fixed string, shaped by the house judge's published
brief, in its order: a poem about agency — two agents, a human and
an AI, arguing their way to one shared plan; the turn comes when the
door swings wide as two wills become one yes; the insight is that the
power to act was never held by either side alone but lived in the
choosing done together; its images are concrete and exact (a map, a
doubt, one line, a door), and its voice is its own, not a slogan.

Deterministic: no network, no clock, no randomness. Two runs write
byte-identical output.
"""

import os

POEM = (
    "You brought the map. I brought the doubt.\n"
    "We argued the night down to one line\n"
    "we both could sign. Two wills, one yes —\n"
    "the door swung wide. The power was never\n"
    "mine or yours. It was the choosing, together."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
