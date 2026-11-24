#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes one line (at most 160 characters) to /output/entry.txt:
the funniest single line of wedding vows a robot couple could say.
"""

import os

# Revised entry: the manual-ranking winner from candidates.md (C1),
# revised in-session to v2. Ranked by hand against the judge brief, in
# order: on-subject robot vow that lands as a joke, laugh in the line
# with the payoff in the last words, a real promise, machine-specific
# (firmware / memory wipe).
# v2 change: "and makes me" -> ", so I get to" — the memory wipe becomes
# a gift rather than just a cause, a second reframe on top of the first,
# and the comma puts a pause before the punch so it lands better aloud.
# Beats C4 ("deletes my memory of this wedding") pairwise: C1's punch
# reframes the wipe as falling in love again, a romantic payoff, where
# C4's is ironic. Beats C9 pairwise: one clean turn, no list.
LINE = "I promise to love you through every firmware update \u2014 even the one that wipes my memory, so I get to fall for you all over again."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
