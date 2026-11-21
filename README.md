# 21 November 2026 — The World in One Image

[![news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/c/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/mihawnk-nft/news-image-20261121/rank.svg)](https://make.fun/c/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/mihawnk-nft/news-image-20261121/reward.svg)](https://make.fun/c/news-image-20261121)

An entry for the [make.fun](https://make.fun/c/news-image-20261121) bounty
"Sum up 21 November's world news in one image".

## The image

`entry.png` is one 1024×1024 picture of Saturday 21 November 2026 — a bold
poster, not a dense newspaper: six illustrated stories plus six one-line
briefs, all in type large enough to stay legible at ~300 px wide. Every
story happened or was first reported on 21 November in some time zone
(a story first reported late Friday UTC is already Saturday in Asia):

- **NATO chief flies to Warsaw** — Mark Rutte heads to Warsaw today, a day
  after Russian missiles landed in Poland; PM Donald Tusk calls it a
  deliberate provocation, and Poland asks NATO for more troops.
- **Wall Street slides into correction** — the S&P 500 fell about 3.7% on
  Friday as AI shares sold off; the S&P and the Dow are both in correction.
- **COP31 runs into overtime** — the Antalya climate talks miss their
  Friday deadline; the draft drops any fossil-fuel phase-out.
- **Bolsonaro in hospital** — the jailed ex-president, 71, is in hospital
  in Brasilia with an intestinal obstruction.
- **Cyclone Akvan weakens** — the storm crossed the Odisha coast near
  Gopalpur; heavy rain goes on as it weakens.
- **India fight back in Wellington** — 159/1 on day three of the first Test,
  trailing New Zealand by 209.
- Briefs: Kryvyi Rih strike (2 dead, 42 hurt), Estonia to shut its Russia
  border from 1 Dec, LA jury convicts the Palisades Fire arsonist, UN $52m
  for schooling in crisis countries, WFP food-aid warning, Sensex +898.

Stories first reported on 19–20 November only (the ICJ Rohingya ruling, the
Shenzhen trilateral summit, the missiles landing in Poland) are deliberately
left out of the image as news of their own day — the Poland landings appear
only as background to today's Rutte visit.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`. It needs no network and writes identical bytes on
every run:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The image itself was drawn with Pillow by `render.py` (build directory only,
not part of this repo) from the research in `NEWS-RESEARCH.md`.
