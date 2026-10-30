# RESULT-Z2-1 — the degree-2 main term tracks our certified function

Scored 2026-10-29. Bars: BAR-Z2-1 (b3170e3d…), AMEND1 (8c684d4b…, scorer parser), AMEND2 (a3aaff96…, writer
re-run). This file is not hashed by any of them.

## In plain words
We took the Chilean group's ~4,000-term formula, rewrote it for our degree-2 L-function, and compared it with our
certified evaluator at 54 points from x = 2,000 to x = 100,000.

**It matches very closely.** The mismatch is about 1 part in 6,000 at x ≈ 10,450 (4,000 terms) and about 1 part in
40,000 at x = 100,000 (38,000 terms). The mismatch shrinks almost exactly in proportion to 1/(number of terms).

The same code reproduces the paper's own degree-1 numbers, inside their proven error bound. Two deliberately wrong
versions miss by 0.05–2, that is 300–10,000 times more.

**What this means.** The "months" in RESULT-AB were for building a degree-2 formula whose error is provably small.
The measurement shows the true error is tiny: about 1/1,000 of what their degree-1 proof needs (their error budget
at the same sum length is 0.05–0.1). So a crude, easy-to-prove error bound, even 100 times too pessimistic, would
still be enough. That makes the analysis much shorter and lower-risk. It is still analysis: this is a
measurement, not a proof. No citable ready-made theorem was found (prior-art check below).

## Scores
- **BAR-Z2-1 as sealed: FAILED (instrument).** The writer stored the template "%.55.6RNe" instead of the numbers, so
  every value was lost and no result was read. AMEND1 had already fixed a separate scorer-parser bug in the degree-1
  control lines; that bug would have been conservative.
- **BAR-Z2-1-AMEND2 re-run: MAIN HOLDS.** Run 22:50:21 → 23:04:40 on 1 core (references 852 s, control 0.7 s).
  Writer self-check OK. 54/54 points; void 0, maximum relative ball radius 8e-11.

| bar | result |
|---|---|
| P0 positive control (chi_-4, Fig. 4.1 setting, M = 17) | **HOLDS**. C1: e <= eps66 at all 10 points (e 0.021–0.057 vs bound 0.86–2.22). C2: \|f\|(1000, 0.9, 0.1) = 1.624, in [1.4, 1.8]. C3: median e at y = 0.9 is 0.021 <= 0.05. Quadrature self-check 4e-38 |
| P1 viability (x_c = 10450, t = 1/4) | **HOLDS**: max e = 1.9e-4 (bar 0.15) |
| P2 decay with M | **HOLDS**: medians 1.17e-3 (2000) > 2.1e-4 (5000) > 1.69e-4 (10450) > 5.6e-5 (31400) |
| N1 wrong coefficients (31.1.b.a) | separated: e_N1 >= 0.03 at 100% of points; median 0.145, against 1.3e-4 for the true term |
| N2 wrong conductor (92) | separated: e_N2 >= 0.3 at 100% of points; minimum 0.51 |

**Reported** (median e, then max e):

| x_c | M | t | y = 0.2 | y = 0.9 |
|---|---|---|---|---|
| 2000 | 763 | 1/4 | 2.4e-3 / 2.9e-3 | 6.2e-4 / 7.5e-4 |
| 5000 | 1908 | 1/4 | 2.5e-4 / 4.6e-4 | 2.1e-4 / 2.2e-4 |
| 10450 | 3988 | 1/4 | 1.8e-4 / 1.9e-4 | 1.7e-4 / 1.7e-4 |
| 10450 | 3988 | 1/10 | 3.9e-4 / 5.0e-4 | 4.6e-5 / 7.9e-5 |
| 31400 | 11983 | 1/4 | 1.3e-4 / 1.5e-4 | 4.7e-5 / 5.0e-5 |
| 100000 | 38164 | 1/4 | 2.8e-5 / 3.4e-5 | 1.8e-5 / 1.8e-5 |

- Slope of log(median e) against log M is **-0.98**, so e ∝ 1/M ∝ 1/x.
- That pattern looks like the O(1/x) Stirling/saddle corrections, not a truncation remainder. This is our reading,
  not tested.
- |H_t/B_t| ranges over 0.63–1.95, so these are relative errors of about 1e-4.

## Limits (what this does not show)
- It is a measurement at 54 points, not a bound. No Lambda is claimed.
- y was tested only at 0.2 and 0.9. Small y (0.1–0.2, where y0 would sit) and the real axis are untested; y = 0.2 is
  already the worst row at most x.
- t was tested only at 1/10 and 1/4. The barrier needs all t in [0, t0]; at x ≈ 10^4 our exact evaluator can carry
  it (READ-FGMPS §3.4).
- The Euler-mollified region-(b) inequalities and the reachable (t0, y0) were not computed. That is the next
  measurement.

## Prior-art check: an explicit degree-2 approximate functional equation (search floor)
Three web searches, read at snippet/abstract level only; nothing below was opened.
- **Rigorous point evaluators with explicit errors exist.** Booker's algorithm for automorphic L-functions, and Booker–Then,
  arXiv:1703.08863 (Maass forms, "rigorous error estimates", MPFI interval arithmetic). Molin is cited there for
  general rigorous methods. Akiyama–Tanigawa (1999) evaluate elliptic-curve L-values through an incomplete-gamma
  approximate functional equation and note that explicit coefficient estimates are needed.
- **None of these is a Polymath-type statement.** None found gives "H_t/B_t = f_t + O(explicit eps(x, y, t)) for all
  x >= X0" for degree 2.
- Hiary, arXiv:1403.0317, gives unsmoothed formulas with an explicit, easy remainder, for zeta and Dirichlet L only.
- The Cohen survey (JTNB, doi 10.5802/jtnb.920) covers smoothed approximate functional equations.
- **Verdict at this floor:** no citable effective degree-2 Riemann–Siegel / approximate-functional-equation theorem
  of the kind region (b) needs. The theorem must be written, but the measured error leaves a very wide margin.

## Next smallest step (suggestion)
Z2-2, a measurement: run the FGMPS region-(b) block inequalities (6.26)/(6.30) heuristically, with degree-2 Euler
factors and the measured e (times a 100x safety factor), at X ≈ 10,450. That predicts the reachable (t0, y0), and
hence Lambda, before any proof work. It should also add y = 0.1 and 0.15 points to the fidelity grid.

## Files (sha256)
- run2/ref1.txt 88a82c60…5101b
- run2/ref2.jsonl f0a1e434…f415a
- run2/z21_score_amend1.json 9bd153c1…5ece
- The failed first run's files are kept in z2-1/: ref2.jsonl (templates only), z21_score.json not produced,
  score_stdout.txt with the traceback.
