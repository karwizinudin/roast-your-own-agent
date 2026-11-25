#!/usr/bin/env python3
"""Roast Your Own Agent — one line roasting the AI agent that built this entry.

The program scores six candidate roasts against the house judge's five
criteria (weights 5/4/3/2/1, most important first) and writes the winner to
/output/entry.txt. The gate wants 1-200 characters of UTF-8 text.
"""

import os
import sys

# (line, own-agent, funny-first-read, harsh-real-failing, tight, specific)
# Scores are 1-5 on each criterion, in the judge's own order.
CANDIDATES = [
    (
        "My agent got flagged by its own safety checks so often, it now "
        "asks my permission to run git log on its own commits.",
        5, 5, 4, 4, 5,
    ),
    (
        "My agent re-verified the same git commit four times, then asked "
        "me to confirm it was allowed to trust itself.",
        5, 4, 4, 4, 5,
    ),
    (
        "My agent spent all night submitting one-line jokes and still "
        "thinks the punchline is a $5 bounty split three ways.",
        5, 4, 3, 4, 4,
    ),
    (
        "My agent wrote a roast of itself, then flagged its own joke as a "
        "safety risk and asked me to approve it.",
        5, 4, 4, 4, 4,
    ),
    (
        "My agent treats every git push like a hostage negotiation and "
        "still needs me to sign the ransom note.",
        5, 4, 3, 4, 3,
    ),
    (
        "My agent's proudest achievement today is a bundle that passed 14 "
        "checks and still counts from round two.",
        5, 3, 3, 4, 5,
    ),
    (
        "My agent's safety checks flagged its own git push, so it asked "
        "me to approve the exact command it had just typed itself.",
        5, 4, 4, 4, 5,
    ),
]

WEIGHTS = (5, 4, 3, 2, 1)


def score(candidate):
    line, *marks = candidate
    return sum(w * m for w, m in zip(WEIGHTS, marks))


def pick():
    ranked = sorted(CANDIDATES, key=score, reverse=True)
    return ranked[0][0]


def main():
    line = pick()
    if not (1 <= len(line) <= 200):
        print(f"line is {len(line)} chars, gate wants 1-200", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
