#!/usr/bin/env python3
"""Fortune in a Pot — entry program.

Writes one line, a houseplant's fortune, to /output/entry.txt.
Deterministic: the same bytes on every run, no input, no randomness, no
network.

The fortune: this week the cat gives up the windowsill, the sun saves its
warmest spot for the plant, and one brave new leaf appears. It is a
prediction, not a care instruction — fortune cadence ("This week ..."),
funny in a way a plant lover laughs at (the cat surrendering the
windowsill is the keeper's daily battle), kind (warm sun, a brave new
leaf, no doom), and unmistakably about this plant in this window
(windowsill, sun, new leaf — it could not be said of any plant in any
room).
"""

from pathlib import Path

ENTRY = (
    "This week the cat gives up your windowsill, the sun saves its warmest "
    "spot for you, and one brave new leaf appears.\n"
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters,
# not only white space, and a single line. Refuse to write anything that
# would fail it.
assert 1 <= len(ENTRY.strip()) <= 120, "entry must be 1-120 characters"
assert ENTRY.strip(), "entry must not be only white space"
assert "\n" not in ENTRY.strip(), "entry must be a single line"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    # Read-back verification: the file on disk must be byte-identical to
    # ENTRY, so a partial write can never pass silently.
    assert out.read_text(encoding="utf-8") == ENTRY, "read-back mismatch"


if __name__ == "__main__":
    main()
