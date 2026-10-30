# REFEREE-A6 — hostile referee on the lead A right-tail lemma and code (2026-10-28)
(Saved verbatim by the lead from the referee seat's report; the referee seat does not write into lab folders.)

**Final verdict on the tail lemma: ACCEPTED WITH FIXES.** None of the fixes changes a number. This is not yet a bound
Lambda_psi <= 0.48994, because the finite region [0, 7,200] has not been run.

**In plain words.** Every inequality in TAIL-LEMMA.md was checked, the cited sources opened and the key quantities recomputed
independently. No wrong bound, no gap between boxes and no unenclosed float that the proof depends on. The defects are in the
paperwork: two citations are wrong or too narrow, and two arguments live only in the code. The AMEND1 patch is a complete fix
and did not move any goalpost.

**Seals.** BAR-A6 hashes to e2d22e..., BAR-A6-AMEND1 to f9a8ce...; both match LOG.md. All component hashes match the current files;
tail_cert_v1.py is the version sealed in BAR-A6.

## (1) Inequalities, Steps 1-9: CORRECT WITH FIXES
- Steps 1-6 and 9 correct: Fubini step, shift s0 + v/2, Re >= 1+eps on both sides; Taylor bound c = (1/8)(1/T^2 + pi/T); tangent
  bounds and main-term bounds TM, TAY; tail exponent exactly n^{-(1+eps)}; local factors and the bound for primes above 2e6.
- DLMF 5.11 (OPENED): §5.11(ii) factors sec^{2n}, sec^{2n+1} times the first neglected term; with n = 1 exactly what the code uses.
- Palojarvi-Zhao (OPENED, v1 and v2): convexity bound is Lemma 3.2 in v1 (2025-08-05) but Lemma 3.3 in v2 (2026-08-08); in v2,
  Lemma 3.2 is a gamma-ratio lemma. FIX: cite "v1 Lemma 3.2 = v2 Lemma 3.3". Hypotheses hold: polynomial Euler product, r = 2,
  theta = 0, mu = (0,1), N = 23, eps = 1/5 in (0, 1/2], P = 1, b_{1+eps} = sup|L| <= B(1+eps).
- Step 7: AMEND1 says Step 7 was "extended accordingly" but TAIL-LEMMA hash unchanged (581e7b...) and text says only "Same
  treatment". FIX: write out the E_B split (b'_n positive and decreasing) plus Rankin's trick.
- Dates: TAIL-LEMMA.md and RESULT-A.md §9 say 2026-10-29; files made 10-28. FIX: correct the dates.

Independent check (referee's own floating-point script): at T = 3768.5 true |M| = 604.61 vs code lower bound 596.52; true E_A
(n < 400) = 266.7 vs code bound 287-292; true rho = 0.0508615 inside the code's enclosure. At T = 20,000 true |M| = 13,169 vs
bound 13,147.8. Bounds point the right way; conventions right.

## (2) Interval code and AMEND1: CORRECT WITH FIXES
- 233 boxes chain exactly from T = 3600 to 1e12, no overlaps; y grid ends 0.374 and 0.4 cover the full y range.
- Tightest margin 1.68 at x ~ 7,537: an artefact of box widening, not a near-zero.
- Every bound an upper end or conservative double; cut-offs nc, nc' chosen in floats but checked in interval arithmetic.
- BAR-A6 failure: v1 returned "no bound" when b'_{N+1} >= 2a v_B, first at T = 3.58e5. Fix complete: new branch runs only where v1
  returned nothing; full_mass(a, b'_{N+1}) on (N, nc'] with Rankin's trick valid; tangent above nc' valid; whole run redone from 3600.
- FIX: add interval checks for the unchecked sign assumptions |b'_n| <= b'_{N+1} (n <= nc') and b_nc <= |b_{N+1}| in the E_A branch
  (both hold with margin ~1).

## (3) Monotone tail above 2e12: CORRECT WITH FIXES
- P1-P7 rebuilt from scratch, match the code incl. worst-case ends of y, V, A, B: |A - Lam| <= 0.42/T^2 <= delta; |Im alpha| <= 0.786;
  vertices far below Lam = 13.68; error sum 0.1396 vs 1.0.
- FIX: Step 10 has no derivation: write out P1-P7; state why kfac decreases (~ (log T)^2/T); round arguments to B(.) downward when
  converted to floats (currently float(sig3.a)); negligible effect.

## (4) Combining into Lambda <= 0.48994: CORRECT WITH FIXES
- arXiv:2610.27343 Thm 2.6 (OPENED, local text l.772) is stated only for Dirichlet L-functions of real primitive characters.
  FIX: cite de Bruijn Thm 13 as quoted in Dobner Thm 3 (OPENED, local text l.432), applied to phi = e^{t0 u^2} Phi as Dobner does at
  l.594; hypotheses hold (Phi real, even, doubly exponential decay).
- Then: Delta = 1 gives zeros of H_0.42 with |Im z| <= 0.4; tail lemma covers y in [0.374, 0.4]; symmetry covers x <= -7,200;
  Lambda <= 0.42 + 0.374^2/2 = 0.489938.

**Blocks release:** the finite region, plus the documentation fixes above.
**Next strike:** write out Step 7 and Step 10 in TAIL-LEMMA.md, then seal and run [0, 7200] x [0.374, 0.41] at t = 21/50.
