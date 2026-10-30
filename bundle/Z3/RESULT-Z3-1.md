# RESULT-Z3-1 — crude envelope sufficiency: MAIN HOLDS

Scored 2026-10-30 by the proof seat. Bar: BAR-Z3-1.md (sha256 430f3b58…, LOG 01:57); design from Z2/IDEAS-Z3.md, with the
bars unchanged. Run on 1 core (run_z31.sh), exit 0.

The first launch was a background chain together with BAR-Z3-P. It ended before z31 wrote anything: z31_stdout.txt
was empty, with no exit line and no output read. The run was then repeated in the foreground with the identical
sealed instruments.

## In plain words
- We bounded the awkward middle of the degree-2 sum crudely, adding absolute values with no clever cancellation.
- With the heat dial at t = 1/4 and about 4,000 terms (x ≈ 10,450), that crude bound is at most 0.031. The budget the
  Chilean proof works with is about 0.05–0.1.
- The same crude bound sits above the true error at every point where we had measured the true error. So it is a
  real upper envelope there, not an underestimate.
- Without heat flow (t = 0) it is 1.5–2.3, far too big. The heat flow is what makes the crude route possible.

## Scores (z3-1/z31_out.json, sha256 3f998fac9d3d23f68aab5e1a045d0d2a6036910d1df9219e4fba5667e1139655)
| bar | result |
|---|---|
| PC (chi_-4, degree 1, 10 Z2-1 control points) | **HOLDS**: E3 >= e everywhere, min ratio 74.5 |
| P1 (x_c = 10450, t = 1/4, y in {0.1, 0.15, 0.2, 0.9}, 20 pts) | **HOLDS**: max E3 = 0.0310 (y = 0.1); by y: 0.0310 / 0.0252 / 0.0205 / 0.0011 (bar 0.05) |
| P2 (E3 >= measured e, 54 shared points) | **HOLDS**: min E3/e = 1.41, at x = 100000, y = 0.9. E2 (K = 2) is below e at 2 points (x = 1e5 and 1e5+1, y = 0.9; ratio 0.96–0.97), so K = 2 is too narrow there |
| N (null, t = 0, x_c = 10450, y <= 0.2, 15 pts) | **FIRES as predicted**: min E3 = 1.51 >= 0.5 (y = 0.9 reported: 0.083) |

**MAIN: HOLDS.** Decision per the design: write lemma W with crude constants.

**Reported** (max over the x points; E3 / E2):

| x_c (M at t=1/4) | t = 0, y=0.1 | t = 1/10, y=0.1 | t = 1/4, y=0.1 | t = 1/4, y=0.2 | t = 0.28, y=0.1 |
|---|---|---|---|---|---|
| 2000 (763) | 2.65 / 1.66 | 0.88 / 0.55 | 0.169 / 0.106 | 0.121 / 0.076 | 0.121 / 0.076 |
| 5000 (1908) | 2.52 / 1.70 | 0.61 / 0.41 | 0.071 / 0.048 | 0.049 / 0.033 | 0.046 / 0.031 |
| 10450 (3988) | 2.28 / 1.46 | 0.41 / 0.26 | 0.031 / 0.020 | 0.021 / 0.013 | 0.019 / 0.012 |
| 31400 (11983) | 1.95 / 1.28 | 0.22 / 0.14 | 0.0079 / 0.0052 | 0.0049 / 0.0032 | 0.0041 / 0.0027 |
| 100000 (38164) | 1.87 / 1.27 | 0.12 / 0.079 | 0.0018 / 0.0012 | 0.0011 / 0.0007 | 0.0008 / 0.0005 |

## Limits (read before using this)
- **E is not a bound.** It is the absolute size of the terms in a window of width 2K·sqrt(M) around the cutoff.
  - It bounds the error only if lemma W is true: outside the window the smoothing weights are exactly 1 or negligible,
    and the window width ~ sqrt(M) is right. Both are still HEURISTIC (IDEAS-Z3 §A).
  - P2 shows E3 >= e at 54 points. That is consistent with the heuristic, not a proof of it.
- **Small t fails the budget.** At t = 1/10, E3 = 0.41 at x ≈ 10,450, and the crude window bound only clears the
  ~0.05 budget for t near 1/4 and above at this x.
  - Under the Polymath/FGMPS architecture, the large-x region is needed only at t = t0. The barrier strip for t in
    [0, t0] is certified by our exact evaluator (READ-FGMPS §3.4), so this does not block the route. A referee should
    confirm that reading of FGMPS Lemma 3.3.
- **The margin over e at large x is thin.** E3/e = 1.41 at x = 1e5, y = 0.9. K = 3 is needed; K = 2 undershoots
  there.
- Coefficients: tail_cert.coeffs equals z21_core.coeffs_23 up to n = 40000 (asserted in the run).

## Files (sha256)
- z3-1/z31_env.py dcf2d1bbc4c72a0fbe2d8abbbc6cf10b8262e4d21ee8c1feb033986b931f5291
- z3-1/run_z31.sh 5eeeeab8cb2242799418bab09ee3f6a86d488db6f86b5b25c1d70022ad7964a8
- z3-1/z31_out.json 3f998fac9d3d23f68aab5e1a045d0d2a6036910d1df9219e4fba5667e1139655
- z3-1/z31_stdout.txt f1f1cee0703d16798a87a8fee8244ff8913dbbf2d6cbce27cd8beabee992b795
