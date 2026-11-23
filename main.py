"""One-line entry for make.fun's "Warning Label for Humans" bounty.

The safety warning label that should come printed on every human being,
in the terse register of a real product label: a choking-hazard / small
parts notice, applied to the human itself. The joke is the label treating
a person as a boxed product — "ships with" a loose screw, no spare
patience, and an attention span small enough to choke on. Funny first,
plausible second: every clause reads like something a real label would say.
The punchline lands in the last few words ("small enough to choke on"),
which turns the familiar small-parts warning back on the human.
"""

import os
import sys

# The entry: one line, 1-160 characters, UTF-8, not whitespace-only.
# Angle: choking hazard / small parts — the human as a boxed product
# with loose screws and a swallowable attention span.
TEXT = (
    "WARNING: Contains small parts. This human ships with one loose screw, "
    "no spare patience, and an attention span small enough to choke on."
)


def main() -> int:
    """Write the entry to /output/entry.txt and verify it byte-for-byte."""
    if not (1 <= len(TEXT) <= 160):
        print(f"gate failed: entry is {len(TEXT)} characters, must be 1-160",
              file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in TEXT:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("gate failed: entry.txt does not match TEXT byte-for-byte",
              file=sys.stderr)
        return 1

    print(f"entry written: {len(TEXT)} characters -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
