# BAR-A16 - sealed high-x positive control for THEOREM-A45 (p = 23, f = eta(z)eta(23z), t = 19/50)

Requested by REFEREE-A45 item (3), release blocker. Sealed 2026-10-29 before the run.

## In plain words
The finite-region certificate (BAR-A14) found no zeros. For x >= ~10,700 its evaluator uses a 163,841-node quadrature,
and no control has yet shown that this regime detects a zero: the largest-x positive control at t = 19/50 was
[796, 800] (BAR-A4-AMEND1 C3). Here the same walker and evaluator, byte-identical to BAR-A14, walk around a small box
across the real axis at x of about 12,500, where an independent PARI computation counts 5 real zeros. The walker must
report winding exactly 5. A second walk goes straight through one of those zeros and must refuse.

## Instruments (pinned)
- Walker cert_wind_ckpt.py (6ba15815...) and evaluator cert_core.py (3c5f7f2b...), the hashes sealed in BAR-A14 and
  BAR-A14-AMEND1. Arguments identical to run_finite45.sh / run_pieces45.sh: t = 19/50, ymax 1/2, c = 30, chunk 25.
- Runner run_a16.sh (one core, sequential); verdict script score_a16.py.
- Prediction: a16_pred.gp, independent of the lab code (no eta function, no contour): the Gaussian average of PARI's
  completed L-function (lfunetaquo([1,1;23,1]), lfunlambda/2) of referee45/gauss_H2.gp, both Gaussian peaks
  (symmetric window), trapezoid in u = v/(2 sqrt t), |u| <= 12, step 1/4, realprecision 57, nbthreads 1 (printed).
  Instrument checks before use (a16_probe*.gp, LOG 07:15): (12500, 1/2) log|H| = -9807.871982413983593 vs the
  referee's -9807.871982413984; at (12496, 0) steps 1/4, 1/8, 1/16 agree to 3.7e-41 relative.
- PARI output a16_pred.txt (41 grid points x = 12496 + k/10, k = 0..40):
  `signchanges_12496_12500 5`, brackets (12496.3, 12496.4), (12497.1, 12497.2), (12497.9, 12498.0), (12498.6, 12498.7),
  (12499.4, 12499.5); no same-sign local minimum of |H| (so no sign is hidden between grid points by a close pair);
  H(12496) < 0, H(12500) > 0; the nearest sign changes are at distance >= 0.3 and >= 0.5 from these vertical edges
  (log|H| there -9806.06 and -9809.71; grid points next to zeros reach -9808.4 to -9811.2).

## Predictions (all required for HOLDS)
- P1 (positive control): the walk a16_box around [12496, 12500] x [-1/2, 1/2], path
  12496,-1/2 -> 12500,-1/2 -> 12500,1/2 -> 12496,1/2 -> 12496,-1/2 (counter-clockwise), exits 0 with every step
  certified, and its certified winding is exactly 5 (|w - 5| + radius/(2 pi) < 0.5).
- P2 (regime): the a16_box log shows `BUILD xb=12500 nodes=163841` (the doubled-node regime, as in g45_b9.log).
- P3 (refusal): the walk a16_refuse on the real-axis segment 124979/10 -> 12498 (y = 0), which contains the PARI sign
  change in (12497.9, 12498.0), must stop: exit code not 0, no a16_refuse.json, and a "cannot certify step" error in its
  log (the BAR-A4-AMEND1 C4 criterion).
- Consistency: score_a16.py checks that its hard-coded 5 equals the count in the sealed a16_pred.txt.
Score: HOLDS iff P1, P2, P3 and the consistency check. Anything else: FAILED, reported with the numbers.

Assumption stated: the prediction counts real zeros only. It assumes H_{0.38} has no non-real zeros with |Im z| < 1/2
in the box (de Bruijn gives |Im z| <= 0.4899 there; nothing here excludes non-real zeros below that). A winding above
5 would still be scored FAILED.

Descriptive only (not scored): wall time (expected 10-20 min: one block build of about 90 s per walk, about 100
points at about 5 s each), points, arg radius. New content: P1 and P2 test the evaluator at x ~ 12,500 in the
163,841-node regime with a nonzero count; nothing proved implies them.

## Hashes
6ba1581587df3ac93ded24df94ab9032f367dce81ee6fc40cfc7bd84df58e22c *cert_wind_ckpt.py
3c5f7f2b4ff148c1b380f6da8022e7c29e565c08491895c04fd3a41d679836df *cert_core.py
08d46af10e7764cd4acace486b64cb8614df1b582f55534069f11a4be4d3ac74 *run_a16.sh
58068e74cf2aec0337bc2268e7715475484ad641184220e1e610f925993db718 *score_a16.py
49f55089d021830a327b6b792e2d151316ac6a4559fefdac15e6fd77232850f5 *a16_pred.gp
c8cffd5409ed975a8e043977e928b96cf114ff4977c41df760f17832545d3384 *a16_pred.txt
f92d8312ad71d53b027d74f05fd7380596bf804fae498de0818538bf7c73b195 *a16_probe2.gp
0cdac205b32e9c4167ebd45b4363f86eed1dc820ee1836df28be2c99d422e9a5 *a16_probe2_out.txt
