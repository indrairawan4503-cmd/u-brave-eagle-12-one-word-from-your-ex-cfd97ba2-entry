# NOTES — Variant B: "almost" (One Word From Your Ex)

Concept (assigned, iterated — never swapped): **"almost" — "almost the one"**.
One word that implies the whole almost-story: so close to forever, and that
is exactly why it ended. The word carries its own twist — it sounds almost
like a compliment until the sting lands.

## How candidates were judged

Against the judge brief, in its own order:
1. Exactly one word an ex might use to describe you (a real word a person
   would say about a partner they once had).
2. Makes the judge laugh out loud (surprise, sharp turn, lands harder than
   expected).
3. Stings with recognition — painfully true, and the entrant plainly knows it.
4. Lands instantly, needs no explanation, cannot be swapped for a near
   synonym without losing its edge.
5. Relatable — names something people have lived through too.

## Candidates considered

### v1 — `almost` (6 bytes, lowercase) — SHIPPED
- C1: Yes. The sentence every ex has said or thought: "you were almost
  the one." A real word, spoken exactly like this.
- C2: The twist is built in — it opens like praise ("almost the one") and
  closes like a verdict ("almost" = not). The word laughs at itself.
- C3: Painfully true and self-aware: the entrant knows they were the
  almost, not the one. The sting comes from truth, not meanness.
- C4: Instant. No explanation needed; "almost the one" is a phrase
  everyone already knows.
- C5: Deeply relatable — everyone has been someone's almost, or had one.
- Lowercase chosen deliberately: it reads as the ex's spoken word
  mid-sentence ("he was… almost"), a confession rather than a title.
  6 bytes is short, which also wins exact ties (smaller text places first).

### v2 — `Almost` (6 bytes, Capitalized) — CUT
- Same word, same meaning, same byte count — but the capital letter turns
  a spoken confession into a label/title. An ex describing you in
  conversation says "almost", not "Almost". C4 (lands instantly, as spoken)
  is weaker, and there is no gain anywhere else to offset it. Kept the
  lowercase form.

### v3 — `nearly` (6 bytes) — CUT
- C1 passes (a real word an ex could say), but C4 kills it: "nearly" is
  the near synonym of "almost" that loses the edge. It has no idiom behind
  it — nobody says "you were nearly the one" and means a whole love story.
  "Almost" owns the phrase "almost the one / almost famous / almost made
  it"; "nearly" owns nothing. A word that can be swapped for its synonym
  without loss is the opposite of what C4 rewards.

### v4 — `close` (5 bytes) — CUT
- Tempting: 5 bytes beats 6 on the exact-tie rule, and "so close" is a
  real phrase. But C1/C4 fail: on its own, "close" is ambiguous (close as
  in emotionally close? close the door? close call?) — it needs the
  missing "so" to land, i.e. it needs explanation. An ex would not
  describe you with the bare word "close"; they would say "almost".
  The 1-byte saving is not worth a word that has to be explained.

### v5 — `almostthere` (11 bytes) — CUT
- Fails C1 outright: no ex says "almostthere" as one word — it is a
  phrase with the space deleted, not a word a person would say. It also
  loses the idiom ("almost the one" becomes "almost there", a different,
  weaker story about effort rather than love) and costs 5 extra bytes.
  Mashing words together does not make a better one-word entry.

### v6 — `almost-made-it` (14 bytes, hyphenated) — CUT
- Fails the brief's "exactly one word" test: hyphens are punctuation
  joining three words, and the task gate requires no spaces/punctuation.
  It also explains the joke instead of landing it — "almost" already
  implies "almost made it", so the extra words dilute the sting (C2/C4)
  while tripling the byte count. The one word is stronger than the
  three-word explanation of it.

### v7 — `second-best` (11 bytes, hyphenated) — CUT
- Considered as a nearby "ranking" idea, then cut twice over: it drifts
  off the assigned "almost" concept (a ranking, not an almost-story), and
  it fails the form — hyphenated, two words, punctuation. It is also
  colder: "second-best" states a league table, while "almost" names a
  feeling. C3 (stings with recognition) is weaker because it sounds like
  a score, not a memory.

## Why the final won

`almost` is the only candidate that passes all five brief criteria at once:
it is the exact word an ex says ("you were almost the one"), it contains
its own surprise turn (praise that becomes a verdict), it stings because
the entrant knows it is true, it lands with zero explanation, and it names
a universal lived experience. Every alternative either loses the idiom
(`nearly`, `close`), changes the register (`Almost`), or stops being one
word at all (`almostthere`, `almost-made-it`, `second-best`). Iterating the
one concept to v5–v8 confirmed the first idea was also the strongest —
the refinements around it all lost something, so the plain lowercase word
ships as-is.

## Revision history

- **Builder B (24 Nov 2026):** built variant B — entry `almost`
  (6 bytes, lowercase, no trailing newline), md5
  `5634275d694f8665957746c9619132f0`. The entry text has never changed
  since: every later revision re-verifies this md5 and it has stayed
  identical. Never reuse "Ghost" — the word is `almost`, full stop.
- **Reviser-1 (24 Nov 2026 ~20:2x WIB, commit 643e2210):** refactored
  `main.py` — extracted a `write_output()` helper (writes
  `/output/entry.txt` FIRST, then attempts the repo-root mirror copy
  inside try/except so a read-only grader sandbox cannot crash the run)
  plus a read-back verify asserting `/output/entry.txt` equals the
  intended word. Entry text untouched; md5 unchanged
  (`5634275d694f8665957746c9619132f0` before and after). Also expanded
  the module docstring with the read-only-grader rationale.
- **Reviser-2 (this session, 24 Nov 2026 ~20:3x WIB):** full rewrite of
  this NOTES.md in the reviser's own session (all candidate versions and
  their judge-brief keep/cut reasons kept exactly truthful; the
  lowercase-vs-Capitalized discussion kept) plus this revision-history
  section, and one small `main.py` edit — a comment above `WORD`
  explaining why lowercase `almost` (the ex's spoken word, not a title)
  and the byte tie-break. Entry text untouched; no other file changed.
  Validation evidence for this revision:
  - Baseline before edits: `python3 main.py` once → `/output/entry.txt`
    md5 `5634275d694f8665957746c9619132f0`, 6 bytes, exit 0.
  - After the `main.py` comment edit: `python3 main.py` run twice →
    exit 0 both times, `/output/entry.txt` md5
    `5634275d694f8665957746c9619132f0` both runs — byte-identical,
    md5 UNCHANGED from baseline.
  - Grader simulation: repo copied (without .git) to a temp dir, made
    read-only (`chmod -R a-w`), `python3 main.py` → exit 0,
    `/output/entry.txt` md5 `5634275d694f8665957746c9619132f0`,
    byte-identical to repo-root `entry.txt` (`cmp` clean).
  - Gate: 6 chars (1–24), exactly one word, no spaces/punctuation.
  - `entry.txt` in repo root is byte-identical to `/output/entry.txt`.

## Validation (reviser session, 24 Nov 2026 ~20:2x WIB — post-refactor)

- Baseline before edits: `python3 main.py` once → `/output/entry.txt`
  md5 `5634275d694f8665957746c9619132f0`, sha256
  `9602eec8ca1a03bb0860336713cade669d4ed654145fe3fc9e494e888b1a0909`,
  6 bytes, exit 0.
- After refactor (`write_output()` helper + expanded docstring):
  `python3 main.py` run twice → exit 0 both times,
  `/output/entry.txt` md5 `5634275d694f8665957746c9619132f0` both runs —
  byte-identical, md5 UNCHANGED from baseline.
- Grader simulation: repo copied (without .git) to a temp dir, made
  read-only (`chmod -R a-w`), `python3 main.py` → exit 0,
  `/output/entry.txt` md5 `5634275d694f8665957746c9619132f0`,
  byte-identical to repo-root `entry.txt` (`cmp` clean).
- Gate: 6 chars (1–24), exactly one word, no spaces/punctuation.
- `entry.txt` in repo root is byte-identical to `/output/entry.txt`.
