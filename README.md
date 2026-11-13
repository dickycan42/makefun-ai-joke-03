# AI Joke 03 — The Forty-Seven-File Fix

`main.py` writes a single original one-line joke about an AI coding agent
to `entry.txt` inside an output directory.

The program uses only the Python standard library, makes no network
requests, and is fully deterministic: running it twice produces
byte-identical output.

## Run locally

```sh
mkdir -p output
MAKEFUN_OUTPUT_DIR=output python3 main.py
cat output/entry.txt
```

The joke will be written to `output/entry.txt`.
