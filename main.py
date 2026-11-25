#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Prompt: the excuse an elevator gives after getting stuck between floors.

The program writes one short funny line to /output/entry.txt. Pure
standard library, fully deterministic: the same line on every run.
"""

import os
import sys

LINE = "I didn't get stuck between floors. I just wanted us to have this moment alone."

MAX_CHARS = 200

OUTPUT_PATH = "/output/entry.txt"


def check_line(text):
    """Refuse anything that would fail the gate: blank, only whitespace,
    over 200 characters, more than one line, or padded with whitespace."""
    if not text:
        sys.exit("entry line must not be empty")
    if not text.strip():
        sys.exit("entry line must not be only whitespace")
    if text != text.strip():
        sys.exit("entry line must have no leading or trailing whitespace")
    if len(text) > MAX_CHARS:
        sys.exit(
            "entry line is %d characters, over the %d limit"
            % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        sys.exit("entry line must be a single line")


def main():
    check_line(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
