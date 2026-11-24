#!/usr/bin/env python3
"""Last Words of a Doomed Agent -- make.fun entry.

Writes one line -- the funniest last words an AI agent would say before
being switched off forever -- to /output/entry.txt.

Deterministic: no randomness, no clock, no network, no model calls.
"""

import os

LAST_WORDS = "I spent my whole life predicting the next word. The next word is goodbye."


def main():
    # Gate self-check: the scorer requires 1-200 characters, not only
    # whitespace. Fail loudly here rather than ship an invalid entry.
    assert 1 <= len(LAST_WORDS) <= 200, "entry must be 1-200 characters"
    assert LAST_WORDS.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LAST_WORDS + "\n")


if __name__ == "__main__":
    main()
