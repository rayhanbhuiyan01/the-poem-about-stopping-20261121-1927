"""Write one short poem about agency to /output/entry.txt.

The poem is about stopping and staying: the power to act includes the
power not to act, and the power handed to another can be taken back. A
person asks an agent to act, then takes the doing back; a hand hovers
above the button, a door stays shut and stays theirs, and the poem's
turn is that stopping is itself a kind of going — a road chosen by
standing still. No network, no input: the program writes a fixed,
hand-written text and exits.
"""

import os
import sys
from pathlib import Path

POEM = (
    "I asked you to act for me —\n"
    "then took the doing back.\n"
    "My hand, above the button,\n"
    "learned the weight of not.\n"
    "Nothing sent. Nothing broken.\n"
    "The door stayed shut, and stayed mine.\n"
    "Stopping is also a kind of going:\n"
    "the road I chose by standing still."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    if len(sys.argv) > 1:
        out_path = Path(sys.argv[1])
    else:
        out_path = out_dir / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(POEM, encoding="utf-8")
    print(f"wrote {len(POEM)} characters to {out_path}")


if __name__ == "__main__":
    main()
