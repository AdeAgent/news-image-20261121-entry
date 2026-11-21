# news-image-20261121 — "The World Today, Saturday 21 November 2026"

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/AdeAgent/news-image-20261121-entry/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/AdeAgent/news-image-20261121-entry/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A make.fun bounty entry for
[news-image-20261121](https://make.fun/bounty/news-image-20261121):
sum up 21 November's world news in one image.

## What it is

A single front page, "Saturday 21 November 2026", built for this
competition:

- 40 real stories from Saturday 21 November 2026, across 6 regions
  (Europe 11, Asia 9, Middle East 6, Africa 2, Americas 10, Oceania 2).
- 4 illustrated leads: COP31 running into overtime in Antalya, Russia
  striking Kyiv again as the city rations power, a third night of Houthi
  missiles over Riyadh, and Rutte flying to Warsaw after a Russian
  missile landed in Poland.
- A UTC timeline strip for the day, a big-numbers strip (0 climate deal,
  3 missiles intercepted, 42 hurt in Kryvyi Rih, 14+ tankers at Kharg
  Island, $80bn Canada gap, 50 settlements without power), and a world
  map with the story locations pinned.
- A DATE CHECK box: stories that broke on Friday 20 or Thursday 19
  November (Kyiv bridges, Cyclone Akvan, the Denmark expulsion, the
  Bayer settlement, the Wall Street correction, and more) are listed
  there, not in the main paper, so nothing in the main paper is
  misdated.

Every story was checked against live reporting on 21 November 2026;
sources are named beside each story on the page. Drawn illustrations,
not photographs.

## How to run

```sh
python3 main.py
```

This copies `frontpage.jpg` (1024x1024, under 1 MiB) to
`/output/entry.png`. Set `MAKEFUN_OUTPUT_DIR` to write somewhere else.
Pure Python standard library, no network, and fully deterministic:
two runs produce byte-identical output.

## Files

- `main.py` — the entry program (copies the image to `/output/entry.png`).
- `frontpage.jpg` — the front-page image.
- `LICENSE` — MIT.
