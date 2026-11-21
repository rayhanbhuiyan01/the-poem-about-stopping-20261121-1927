"""A small program about agency.

The poem it writes is about the choice to hold back: having the power
to act also means having the power not to act, and choosing stillness
can itself be a deliberate, meaningful act.

Revised: the final poem speaks in the first person — the speaker
takes the doing back and finds that standing still is itself a road.
"""

import os
import sys
from pathlib import Path

POEM = """I asked you to act for me —
then took the doing back.
My hand, above the button,
learned the weight of not.
Nothing sent. Nothing broken.
The door stayed shut, and stayed mine.
Stopping is also a kind of going:
the road I chose by standing still."""


def main() -> None:
    # The output directory comes from the environment, with /output
    # as the default; a path passed on the command line wins instead.
    if len(sys.argv) > 1:
        target = Path(sys.argv[1])
    else:
        target = Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(POEM, encoding="utf-8")
    print(f"Wrote {len(POEM)} characters to {target}")


if __name__ == "__main__":
    main()
