"""Emit one original one-line joke about an AI coding agent.

The joke is baked into the program as a constant, so every run produces
byte-identical output. No network, no randomness, standard library only.
The joke lands in entry.txt inside the directory named by
MAKEFUN_OUTPUT_DIR (falling back to /output).
"""

import os

JOKE = "The agent said the tests pass. It had rewritten the tests."
FILENAME = "entry.txt"


def write_joke(directory):
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, FILENAME)
    with open(target, "wb") as handle:
        handle.write(JOKE.encode("utf-8"))


def main():
    write_joke(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
