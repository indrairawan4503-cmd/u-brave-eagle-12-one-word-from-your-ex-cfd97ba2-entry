"""One Word From Your Ex — variant B (almost the one).

Entry: the single word ``almost`` (6 bytes, lowercase, no trailing
newline) — "you were almost the one". One word that opens like praise
and closes like a verdict, which is exactly why it ended.

Gate (from the contest brief): the entry must be exactly one word,
1-24 characters, no spaces or punctuation. ``almost`` is 6 chars,
a single lowercase word, so it passes the gate with room to spare.

Read-only-grader rationale: the grading sandbox mounts the repo
read-only, so writing the repo-root mirror copy (``entry.txt``) would
raise OSError and must never crash the run — that is why
``write_output()`` writes ``/output/entry.txt`` FIRST (the graded
file), then attempts the repo-root copy inside try/except, and
finally reads ``/output/entry.txt`` back and asserts it equals the
intended word. Deterministic, no network, no randomness; exit 0
on every run where the output directory is writable.
"""

import os
import sys

WORD = "almost"


def write_output() -> None:
    """Write the entry word, /output first, then a repo-root mirror.

    The grader sandbox mounts the repo read-only, so the repo-root copy
    is best-effort inside try/except and must never crash the run.
    After writing, /output/entry.txt is read back and asserted equal to
    WORD, so a silent write failure can never ship a wrong entry.
    """
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
        return
    assert written == WORD, "read-back mismatch: %r != %r" % (written, WORD)


def main() -> None:
    write_output()


if __name__ == "__main__":
    main()
