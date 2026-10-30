# BAR-Z3-1 — crude envelope sufficiency (design: Z2/IDEAS-Z3.md "Smallest first step", copied without change of bars)

Sealed 2026-10-30 by the proof seat before the run. Smoke: one off-grid call (x = 3000, y = 0.3, t = 0.2, and chi_-4 at
x = 1500) to check the code runs; not scored.

## Instruments (sha256)
- z3-1/z31_env.py dcf2d1bbc4c72a0fbe2d8abbbc6cf10b8262e4d21ee8c1feb033986b931f5291
- z3-1/run_z31.sh 5eeeeab8cb2242799418bab09ee3f6a86d488db6f86b5b25c1d70022ad7964a8 (1 core, cap 900 s)
- imported unchanged: Z2/z2-1/z21_core.py bbd199c933ed2f9cfbe6c3d9127d6b1a629a5328dbd08095be9b3e08ac3b264e,
  AB/leadA/tail/tail_cert.py 1441e756c8291387095e31d13a229224c74dad2ddae00a5644ba04f64036b7c7 (coeffs; cross-checked
  equal to z21_core.coeffs_23 up to n = 40000), measured e from Z2/z2-1/run2/z21_score_amend1.json
  9bd153c1773f36a7fe967446ae424342d01e6ad67fe34f85e2315797dc715ece.

## Quantity
E(x,y,t;K) = sum over integers n in (M - K sqrt M, M + K sqrt M] of |a_n| b_n (n^{-Re s*+} + |gamma| n^{-Re s*-});
s*, gamma, b_n, M exactly as Z2-1 (z21_core). K in {2, 3}.
Grid: the Z2-1 x values (x_c + {0, 1/2, 1, 3/2, 2} for x_c in {2000, 5000, 10450, 31400}; {100000, 100001})
x y in {0.1, 0.15, 0.2, 0.9} x t in {0, 1/10, 1/4, 0.28}.

## Bars (as designed; interpretations of the design written here BEFORE the run)
- P1: E(K=3) <= 0.05 at every x_c = 10450, t = 1/4 point with y >= 0.1 (y in {0.1, 0.15, 0.2, 0.9}; 20 points).
- P2: E(K=3) >= measured Z2-1 e at all 54 shared points.
- N (null): at t = 0, x_c = 10450: E(K=3) >= 0.5 at every point with y in {0.1, 0.15, 0.2} (interpretation: the design's
  heuristic 2.6 is for y = 0.2; y = 0.9 is reported only).
- PC: chi_-4 (degree 1, t = 1/10, the 10 Z2-1 control points, Deg1(4,1)): E(K=3) >= Z2-1 e at all 10.
## Decision (from the design)
- P1 + P2 hold: write lemma W with crude constants. P2 fails: cancellation is essential (Siegel 1943 / kernel route).
  P1 fails: push M up, or trade t0. PC failing voids the scoring.
