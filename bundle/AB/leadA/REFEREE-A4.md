# REFEREE-A4: hostile referee read of the BAR-A4 finite-region certificate

Date: 2026-10-28. Reader: independent referee (read-only on lab files; reruns done in a private scratch copy).
Claim judged: "H_{0.38} for L(s, eta(z)eta(23z)) has no zeros with Im z >= 0.469 and |Re z| <= 800."

## In plain words
The certificate holds up. The definition, the error bounds and the winding logic are right, and the seal was scored
exactly as written. I reran the controls and got the same numbers. I also added two controls of my own, and both
behaved as they should. What I found are bookkeeping gaps in the error accounting: a few rounding errors are not
counted explicitly, but each is at least 10^4 times smaller than the slack already built in. None of them changes the
result. They should still be closed before anyone calls the code "fully enclosed".

## Seal and reproduction
- sha256 of BAR-A4.md = fb11be80...b023, matching LOG.md 02:32. All six code/ref hashes in BAR-A4 match the files on disk.
- My rerun (Python 3.11, gmpy2 2.3.1, MPFR 4.2.2, MPC 1.4.0, mpmath 1.3.0):
  - cert_test gives ALL INSIDE, with identical radii.
  - null gives argsum 12.566370614359172 +- 5.06e-17 (winding 2), identical to the lab run.
  - The main run was not rerun; its logs are consistent. The arg sums are -807.72, -1083.24, +1083.22 and +807.74;
    they total 1.3e-55 with a combined radius of 2.5e-16.
- P1-P3 were scored exactly as sealed. Wording nit: 8,611 is the number of evaluations. The number of cone steps is
  8,605 (6 segment starts).

## Verdicts
**(1) Definition and variable change: CORRECT WITH FIXES.**
- Mellin check (by hand): with y = e^{2u}/sqrt23, the integral of Phi(u) e^{izu} du equals
  23^{s/2}(2pi)^{-s}Gamma(s)L(s) at s = (1+iz)/2, so xi = Lambda_PARI/2. That matches the refs.gp convention. Zeros
  are unaffected by the constant.
- LMFDB L-function page, OPENED: "Lambda(s)=23^{s/2} Gamma_C(s) L(s)" with "Lambda(s) = Lambda(1-s)", "Sign (root
  number): 1".
- Dobner arXiv:2005.05142, OPENED, p. 8 eq. (6): "xi^F_t((1+iz)/2) := int e^{tu^2} Phi_F(u) e^{izu} du". This matches
  the lab definition.
- The H_0 controls against lfunlambda are independent and agree to about 1e-55. They exercise both signs of u, so
  they also confirm the evenness numerically.
- FIX: drop the convention-dependent phrase "Fricke sign +1". Prove evenness directly in two lines from
  eta(-1/tau) = sqrt(-i tau) eta(tau):
  - The eta transformation gives f(-1/(23tau)) = sqrt(-i23tau) sqrt(-i tau) f(tau) = -i sqrt23 tau f(tau).
  - Hence Phi(-u) = Phi(u) exactly. No outside source is needed.

**(2) Truncation and quadrature bounds: CORRECT WITH FIXES.**
- Trefethen-Weideman, SIAM Rev. 56 (2014), OPENED, Thm 5.1 (PDF p. 16): "Suppose w is analytic in the strip
  |Im(x)| < a ... w(x) -> 0 uniformly ... int |w(x+ib)| dx <= M for all b in (-a,a). Then ... |I_h - I| <= 2M/(e^{2 pi a/h} - 1)".
  The hypotheses are met:
  - a = delta, and the strip edge pi/4 - delta < pi/4 keeps Im tau > 0;
  - Phi decays doubly exponentially;
  - cos(2v) >= sin(2 delta) on the strip, which the code uses.
  The code uses math.pi < pi, which only enlarges qerr, so the error is conservative.
- Node-tail and majorant tails: the log-derivative bound kappa(u) = 4 pi Y - 2tu - ymax - 1 - j/u is correct (I
  derived it). kappa is increasing, so the bound integral <= G(U)/kappa is valid.
- The upper Riemann sums use mpmath.iv: rigorous.
- Fundamental-domain constant S: correct. The supremum of e^{-pi y/12} y^{1/4} is attained at y = 3/pi >= sqrt3/2.
- |a_n| <= d(n) <= n gives sum d(n) r^n <= r/(1-r)^2: valid. For a weight-1 newform, |a_n| <= d(n) is the standard
  Deligne-Serre consequence. I did NOT open a source for that.
- The pentagonal tail 2|q|^35/(1-|q|) is valid: exponents 35, 40, 51, 57, ... are distinct integers plus 1/24.
- FIX: in eta(), qabs**35 underflows to 0.0 for large reduced Im tau, and math.exp underflows for Im tau > ~118.
  The tail is then covered only by the UP slack on acc[1]. Compute the tail in mpfr or iv.

**(3) Every arithmetic step enclosed: CORRECT WITH FIXES (formal gaps, no effect on the outcome).**
- No numpy anywhere. The only mpmath code is iv. MPC/MPFR operations are correctly rounded, and the radius formulas
  in bmul, bexp, brecip and bsqrt are valid (bsqrt even has a spare factor of 2).
- Gaps:
  - (a) The float radius sums R[j], absum and argrad use round-to-nearest over up to 8,705 terms, but UP = 1+2^-50
    covers only about 8 roundings. Fix: multiply by (1 + n*2^-52), or sum in MPFR with round-up.
  - (b) The constants 1/24 (EXPS) and 1/12 (PI_I_12) are rounded at 192 bits but given radius 0. That is about 1e-58
    relative error, below the radii of about 1e-54. Fix: give them radius EPS*|value|.
  - (c) ok_step certifies radius float(sq), which can be 1 ulp below the exact mpq step, and the rounded vertices
    drift by about 1e-57. Fix: pass float(sq)*UP + 2*zball radius.
  - (d) cauchy_bound uses float(cx), while the scaling uses mpfr(cx). Since expo decreases in x, pass the x lower bound.
  - (e) Trusting libm exp/expm1/asin to within 1 ulp is acceptable but should be stated as an assumption.
- Every gap is at least 10^4 below the 2% cone margin and the about 1e-20 relative radii.

**(4) Argument principle and region coverage: CORRECT.**
- The cone condition |H(z)-H(p)| < 0.98|H(p)| on the closed step disk (Taylor to order 12 plus the Cauchy tail
  M(s/rc)^13/(1-s/rc)) keeps H(z)/H(p) in Re > 0 along each step. So the principal arg equals the continuous change.
  It also proves H != 0 on the whole boundary.
- The positive scalings e^{x theta} cancel in the args.
- The arg enclosure via asin(rel) with rel < 0.5 and |arg| < pi/2 cannot cross the branch cut.
- Winding 0 for an entire function, nonzero on the boundary, means no zeros in the closed rectangle.
- Coverage:
  - L(s) != 0 for Re s > 1 (Euler product) and, by the functional equation, for Re s < 0. So Delta = 1.
  - Dobner Thm 3, OPENED, p. 9: "If all the roots of G lie in the strip |Im z| <= Delta, then all the roots of G_t lie
    in the strip |Im z| <= (max(Delta^2 - 2t, 0))^{1/2}". With t = 0.38 this gives 0.4899 < 0.5.
  - Phi is real and even, so H(-conj z) = conj H(z). The region [-800,0] follows by reflection.
- The claim follows as stated.

**(5) Controls: CORRECT WITH FIXES.**
- P2 is a genuine positive control for the walker, but only in block xb=25 (delta 0.125, 385 nodes). About 98% of the
  main contour runs in blocks xb >= 100 (delta down to 0.0125, 8,705 nodes).
- The H_{0.38} references in refs.txt come from the same contour formula in PARI floats (etaH.gp), so they share the
  method. Only the H_0 references are independent; the Gaussian-average check (6e-14) was unsealed.
- My added controls (POST HOC, not sealed):
  - Rectangle [796,800] x [-1/2,1/2] at t = 19/50: certified winding **4** (argsum 8pi +- 3.5e-20, 80 points, 24 s).
    This matches the 4 sign changes of H on the real axis, certified by the same evaluator, at 796.61, 797.67, 798.67
    and 799.69.
  - Path (9,0) to (10,0), which passes through a zero: the walker correctly REFUSES, stopping at x = 9.627 with
    hlow 1.3e-8 (zero near 9.65).
- FIX: add the large-x rectangle and the refusal test to the sealed control suite. Label the t > 0 references as
  "same method".

## Not checked
- Novelty or priority.
- The right tail |Re z| > 800. The lab states correctly that this tail is not done.

## Final verdict: ACCEPTED WITH FIXES
- Nothing blocks the finite-region claim as stated.
- Before any public "fully enclosed" wording, close gaps 3(a)-(e) and 2 (eta tail), replace the Fricke wording with
  the eta identity, and seal the two extra controls.
- RESULT-A section 6 says "Every evaluation is enclosed in a rigorous ball". It should read "enclosed, with the formal
  float-sum slack listed in REFEREE-A4".
