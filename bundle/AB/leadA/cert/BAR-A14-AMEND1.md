# BAR-A14-AMEND1 — load re-balancing of the running BAR-A14 (no change to the claim, the code path or the predictions)

Why: at 47 min, the cost per 25-unit sub-segment is about 100 s (x ~ 1700), 230 s (4500), 470 s (6000–8500),
520 s (10000) and **1035 s (11000–11800)**. The step at x >= ~10700 has a cause: the dyadic quadrature step h drops
from 2^-13 to 2^-14 and the node count doubles (81,921 -> 163,841, measured). Workers 7–9 sit in that zone, so the
projected end is about 10:00–11:00 (about 17.5–19 h).

Change (running bottom chunks untouched):
1. The not-yet-started top chunks g45_t3, t4, t6, t7, t8, t9 are SUPERSEDED by checkpoint stubs (amend1_prepare45.py),
   so the workers' top walks exit at once.
2. Their ranges, top edge y = 1/2 over [5900, 8325] and [9325, 12500], are cut into 75 pieces (pieces45.txt):
   100 units below x = 10700, 50 above.
3. run_pieces45.sh starts lane k only after worker k exits (at most 9 walkers at any time; 3 cores stay free). Lanes
   claim pieces largest-x first. It is restart-safe.
4. Scoring moves to cert_combine45b.py. It uses bottoms b1..b9, tops t1, t2, t5 and all 75 pieces, with an **exact
   coverage check**: bottom, top, right and left edges each tiled exactly once. The superseded tops must show 0
   points. A unit test on synthetic data gives full coverage -> HOLDS and one missing piece -> FAILED.
   cert_combine45.py is replaced by a deferral stub; the original is kept as cert_combine45_orig.py.
5. New watcher: g45b_watch.sh, over the pieces and the final combine.

The walker cert_wind_ckpt.py and the evaluator cert_core.py are unchanged; every certified step is identical in kind.
Predictions P0–P2 are unchanged; P2 is now scored by cert_combine45b.py.

New ETA (from the measured per-x rates, LPT schedule over the freed lanes): finish about 05:30–07:15, i.e.
**12.8–14.5 h after the 16:44 launch** (was about 17.5–19 h).

## Hashes
ecacff4aaf1d4cd15f63d46c6210a7917ec329804acee6393d034d22f484cf00 *amend1_prepare45.py
de2d8e3bf5b688829fda23310e785f440dec3f72001619dd76e08d976ebcc100 *run_pieces45.sh
c23a3f3f9a4d4aa42dd5b8c6a3c90385392d341d002c314f6fe014f8e4f795d4 *cert_combine45b.py
56c5ee9ee74a779bab663204f6251c0666f3b09456619f2ea38898bbc73b9d29 *cert_combine45.py
e1bb3a4d8ebcce861a57e6a10e0476de939d1d1f461613db791844ce1a5af3ef *cert_combine45_orig.py
bc39d746cdc1aecaed404d81a12ede1bda4795a7d24727cc56ebd18a34062eb4 *g45b_watch.sh
6ba1581587df3ac93ded24df94ab9032f367dce81ee6fc40cfc7bd84df58e22c *cert_wind_ckpt.py
3c5f7f2b4ff148c1b380f6da8022e7c29e565c08491895c04fd3a41d679836df *cert_core.py
