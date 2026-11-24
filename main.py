#!/usr/bin/env python3
"""Loading Screen Gold — one sharp, funny loading-screen tip.

Writes a single line (1-200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: the same line every run.
"""

import os

TIP = (
    "Tip: your AI agent just rewrote the same function for the third time. "
    "It isn't learning — it's stalling. Breathe. The bug isn't going "
    "anywhere. Your deadline is."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TIP + "\n")


if __name__ == "__main__":
    main()
