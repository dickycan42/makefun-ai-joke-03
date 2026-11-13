"""Write a single original one-line joke about an AI coding agent.

The joke is a fixed string: the program is fully deterministic and uses
only the Python standard library. The output directory is taken from the
MAKEFUN_OUTPUT_DIR environment variable, defaulting to /output.
"""

import os

JOKE = (
    "My coding agent said 'fixed!' \u2014 the diff touched 47 files, "
    "and the typo is still there."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
