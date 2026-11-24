# Make the AI Judge Laugh: Developer Excuses

[![Make the AI Judge Laugh: Developer Excuses](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/thanhvu261090/makefun-laugh-developer/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/thanhvu261090/makefun-laugh-developer/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

An entry for the [Make the AI Judge Laugh: Developer Excuses](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3) bounty on make.fun.

## The entry

One funny single-line excuse a developer gives when code breaks in production:

> It wasn't a bug, it was a feature flag — set by me, in a commit titled 'temporary fix', two years ago.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the entry
line to `/output/entry.txt`. It first checks the gate itself: 1–200
characters, a single line, not only whitespace, valid UTF-8 — then writes the
file and reads it back to confirm the bytes on disk match exactly.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
