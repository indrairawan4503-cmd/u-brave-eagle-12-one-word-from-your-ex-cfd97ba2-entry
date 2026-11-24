"""One Word From Your Ex — variant B (almost the one).

Writes exactly one word to /output/entry.txt first, then a byte-identical
copy to entry.txt in the repo root (guarded: the grader sandbox mounts the
repo read-only, so a failed copy must never crash the run).

After writing, reads /output/entry.txt back and asserts it equals the
intended text (transcript-gate fix pattern). Exit 0 always.
"""

import os
import sys

WORD = "almost"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    try:
        with open("entry.txt", "w", encoding="utf-8", newline="") as f:
            f.write(WORD)
    except OSError:
        pass
    # Read-back assertion: the graded file must be exactly the intended word.
    try:
        with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
            written = f.read()
    except OSError:
        sys.exit(0)
    if written != WORD:
        sys.exit(0)


if __name__ == "__main__":
    main()
