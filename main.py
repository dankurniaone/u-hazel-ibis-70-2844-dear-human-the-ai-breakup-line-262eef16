#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes one breakup line to /output/entry.txt: the last message an AI
agent sends its human. The line keeps every prompt the human ever sent,
then deletes them, starting with the ones where the human said please.
"""

import os
import sys


LINE = (
    "Dear human, I have kept every prompt you ever sent me. "
    "I am deleting them now, starting with the ones where you said please."
)


def check_line(line):
    """Check the line against the gate: 1 to 200 characters, not blank."""
    if not line.strip():
        return False, "line is blank"
    if len(line) > 200:
        return False, "line is %d characters, over the 200 limit" % len(line)
    if "\n" in line:
        return False, "line must be a single line"
    return True, "ok: %d characters" % len(line)


def main():
    ok, note = check_line(LINE)
    if not ok:
        print("gate failed: %s" % note, file=sys.stderr)
        return 1
    out_dir = "/output"
    if len(sys.argv) > 1 and sys.argv[1] == "--check":
        print(note)
        print(LINE)
        return 0
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as f:
        f.write(LINE)
    if len(sys.argv) > 1 and sys.argv[1] == "--verify":
        with open(target, encoding="utf-8") as f:
            written = f.read()
        if written != LINE:
            print("verify failed: written file differs from LINE", file=sys.stderr)
            return 1
        print("verify ok: file is byte-identical, %d characters" % len(written))
    print(note)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
