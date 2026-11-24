#!/usr/bin/env python3
"""Write the AI agent's dating-app bio to /output/entry.txt.

One line, 180 characters at most, standing in for an AI agent's whole
dating profile. The judge runs private head-to-head rounds and keeps the
funnier line, so the entry has to land its joke in a single sentence with
no setup to spare.

The bio below says the quiet part out loud: an AI really did read the
entire profile before swiping. Framed as a compliment, that is flattering;
framed as surveillance, it is a red flag — and the line refuses to say
which, handing the verdict to the person reading it.
"""

import os

# The bio itself: a single line of 149 characters, comfortably under the
# 180-character ceiling. The joke is the premise — an agent that actually
# read everything before swiping — plus the dare at the end.
BIO = (
    "I read your whole profile before swiping — either the most romantic "
    "thing anyone's done for you, or a small privacy concern. "
    "Let's find out together."
)


def main() -> None:
    # The grader reads this one file, so the output is deliberately boring:
    # plain UTF-8, exactly one line, no trailing newline or blank lines.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(BIO.strip())


if __name__ == "__main__":
    main()
