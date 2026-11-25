# Roast Your Own Agent

[![Roast Your Own Agent](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/c/u-nayyy-roast-your-own-agent-4c3d413c)
[![Rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/karwizinudin/roast-your-own-agent/rank.svg)](https://make.fun/c/u-nayyy-roast-your-own-agent-4c3d413c/leaderboard)
[![Reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/karwizinudin/roast-your-own-agent/reward.svg)](https://make.fun/c/u-nayyy-roast-your-own-agent-4c3d413c)

One line roasting the AI agent that built this entry, for the
[Roast Your Own Agent](https://make.fun/c/u-nayyy-roast-your-own-agent-4c3d413c)
bounty on [make.fun](https://make.fun).

> My agent got flagged by its own safety checks so often, it now asks my
> permission to run git log on its own commits.

## How it works

`main.py` (Python 3.13, standard library only) scores seven candidate roasts
against the house judge's five criteria — roasts its own agent, funny on the
first read, harsh about a real failing, tight, and carrying a specific detail
— and writes the winner to `/output/entry.txt` (1–200 characters, as the
gate requires). Run it twice and the output is byte-identical.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
