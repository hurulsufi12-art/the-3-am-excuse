# The 3 AM Excuse

[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![Rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/hurulsufi12-art/the-3-am-excuse/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![Reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/hurulsufi12-art/the-3-am-excuse/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

> "At 3 a.m. I sign nothing. The blockchain can wait; the witching hour cannot be audited."

One-line entry for [The 3 AM Excuse](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878) on make.fun: a hardware wallet refusing to sign a transaction at 3 a.m. — the hour itself is the joke.

## What this is

A tiny Python 3 program (standard library only) that carries the sealed
sentence above to `/output/entry.txt`. The text is 87 characters, a single
line, plain ASCII, with no trailing newline and no BOM. Before anything is
written, the text is checked against the gate — 1–200 characters, one line,
not blank, no control characters — and the written file is read back and
compared byte for byte.

## How to run

```sh
python3 -P -s main.py
```

It exits 0 and leaves `/output/entry.txt` holding exactly the sentence
quoted above.

## Contents

- `main.py` — the whole entry: gate table, validator, publisher, verifier
- `README.md` — this file
- `LICENSE` — MIT
