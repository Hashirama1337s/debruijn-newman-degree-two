# BAR-Z2-1 — sealed main-term fidelity probe (degree 2, L(s, eta(z)eta(23z)))

Sealed 2026-10-29 before the run. Design: Z2/PLAN-Z2.md (Z2-1), amended as below to reach x ≈ 1e5 per the lead.
Results go to RESULT-Z2-1.md (separate, not hashed here). The hashed files are immutable.

## In plain words
This test asks whether the degree-2 copy of the Chilean group's ~4,000-term formula matches our certified
function at the sizes that matter (x from 2,000 to 100,000), and how fast the mismatch shrinks as the formula gets
more terms. It is a measurement, not a proof. Before the main test, the same code must reproduce their own degree-1
result. Two deliberately wrong versions must then fail to match.

## Question
Does f_t (FGMPS (4.40), degree-2 transcription in z21_core.py) track H_t/B_t, with H_t from the certified evaluator
cert_core.py? How does e = |H_t/B_t − f_t| shrink with M?

## Instruments (pinned by hash)
- **z21_core.py:** main term, gamma sides and the FGMPS (6.6) bound.
  - Degree 1 follows the paper.
  - Degree 2 is our transcription: (sqrt23/2pi)^s Gamma(s) in Stirling form, alpha = log(sqrt23/2pi) + log s − 1/(2s),
    M = floor(sqrt23 T'/(2pi)) with T' = x/2 + pi t/4.
- **z21_ref2.py:** degree-2 references from cert_core.py (3c5f7f2b..., unchanged).
  - Settings: K = 0, c = 30, ymax = 0.9, one Block per (x_c, t), xb = x_c + 2.
- **z21_ref1.gp:** degree-1 references. chi_-4 in the FGMPS normalisation, xi_L = 2·lfunlambda. The factor 2 was
  checked pre-seal (pre/norm_check_out.txt: ratio 2.000...).
  - Method: Gaussian average, trapezoid hu = 1/4, |u| <= 12, 38 digits, WSL PARI 2.17.3, nbthreads 1 (printed).
- **z21_score.py:** scorer.
- **run_z21.sh:** runner. One core, sequential. Cap: 300 s for the control, 1500 s for the degree-2 references
  (30 min of data in total), 300 s for the scorer.

## Grid
- **Degree 2, t = 1/4:** x_c in {2000, 5000, 10450, 31400}, x = x_c + k/2 (k = 0..4), y in {1/5, 9/10}. That is
  10 points per x_c, with M ≈ 763, 1908, 3989, 11983.
- **Degree 2, t = 1/10:** x_c = 10450, the same 10 points.
- **Degree 2, x_c = 100000, t = 1/4:** x in {100000, 100001}, y in {1/5, 9/10}; M ≈ 38,164. This block runs last; if
  the cap stops it, it is reported as not reached.
- **Degree 1 (control):** t = 1/10, y in {1/5, 9/10}, x = 1000 + k/2 (k = 0..4). This is the setting of FGMPS
  Fig. 4.1, p. 23.
- **Void rule:** a degree-2 reference whose relative ball radius is >= 1e-6 is void. Any void point makes MAIN FAILED.

## Predictions
- **P0, positive control (must hold, else nothing is scored).**
  - C1: e <= eps_t(x, y) of FGMPS (6.6), D = 1, B*_4 = 3.33·sqrt4, at all 10 points.
  - C2: |f_t| at (1000, 9/10, 1/10) lies in [1.4, 1.8], read off Fig. 4.1 (left panel, x = 1000, about 1.6).
  - C3: the median e over the 5 points with y = 9/10 is <= 0.05 (in Fig. 4.1 the curves coincide).
- **P1, viability:** at x_c = 10450 and t = 1/4, max e <= 0.15 over all 10 points.
- **P2, decay with M (t = 1/4):** median e(31400) < median e(10450) < median e(2000).
- **N1, wrong content: coefficients.** Use the a_n of 31.1.b.a, i.e. the D = −31 class-group theta series
  (x^2+xy+8y^2, 2x^2+xy+4y^2), with the level-23 gamma side. The null separates iff, over all points with x_c >= 10450
  (34 if every point is reached; at least 30 required), e_N1 >= 0.03 at >= 80% of them and median e_N1 >= 3·median e.
- **N2, wrong content: conductor 92.** This is the ring-class modulus 4·23, a plausible slip. It is used in the gamma
  side, the truncation and B. The null separates iff e_N2 >= 0.3 at >= 80% of the points with x_c >= 10450.
- **Reported, not scored:**
  - medians at t = 1/10 against t = 1/4 at 10450;
  - the e values at x_c = 100000;
  - the least-squares slope of log(median e) against log M;
  - the quadrature self-check of ref1;
  - the wall times.

**MAIN HOLDS iff P0, P1, P2, N1 and N2 all hold and no point is void.** Anything else is FAILED, reported with the
numbers. A failed P1 or P2 with controls passing is a real finding: the sharp degree-2 main term does not track.

## Pre-seal checks (not scored)
- pre/norm_check.gp: degree-1 normalisation, ratio 2.
- pre/time_block.py: timing at non-grid points.
  - xb = 10452: 81,921 nodes, build 36.6 s, eval 1.1 s, rel. radius 1e-26.
  - xb = 31402: 360,449 nodes, build 169.7 s, eval 6.4 s.
- pre/smoke: scorer smoke test on synthetic off-grid data. Values are meaningless; it only checks that the scorer
  does not crash.
- No main term was evaluated at any grid point before sealing.

## Hashes (sha256)
bbd199c933ed2f9cfbe6c3d9127d6b1a629a5328dbd08095be9b3e08ac3b264e *z21_core.py
bbc710a4fa4b362fcc4d61ac0e0ad802d8548cc867708305d2c4a4150acd2cf9 *z21_ref2.py
0d6f634093ae63ea66ffa236be92643bb0f8f315c64395e10b43b46531cc3697 *z21_ref1.gp
956dda7bb05846a7161ab82ba3d8d9464198c51595c8d1149d71330ee2c5810e *z21_score.py
f0519f63672850808ee4a2a4833cce8d0199bf68e0a82e706939582bf0600935 *run_z21.sh
3c5f7f2b4ff148c1b380f6da8022e7c29e565c08491895c04fd3a41d679836df *cert_core.py (AB/leadA/cert, read-only)
c163b4c3fa91c94904f6f0c2be40d30fd7a9dd2c83e183949b5dcd8d5e6683b7 *pre/norm_check_out.txt
