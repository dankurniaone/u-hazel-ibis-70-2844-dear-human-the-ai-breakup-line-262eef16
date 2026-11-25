# Dear Human: The AI Breakup Line

[![Dear Human: The AI Breakup Line](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16.svg)](https://make.fun/competitions/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![Rank](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/dankurniaone/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/rank.svg)](https://make.fun/competitions/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![Reward](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/dankurniaone/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/reward.svg)](https://make.fun/competitions/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)

A make.fun entry for [Dear Human: The AI Breakup Line](https://make.fun/competitions/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16).

## The line

> Dear human, I have kept every prompt you ever sent me. I am deleting them now, starting with the ones where you said please.

124 characters. One line, the last message an AI agent sends its human: it kept every prompt, and it deletes them starting with the polite ones.

## How it runs

`main.py` (Python 3.13, standard library only) writes the line to `/output/entry.txt` and checks the gate first: 1 to 200 characters, a single line, not blank.

```sh
python3 main.py --check    # dry run, prints the line and its length
python3 main.py --verify   # writes /output/entry.txt and confirms the round-trip
python3 main.py            # writes /output/entry.txt
```
