# BAR-Z3-P — sealed exact test of the key step and of Lemma P (polynomial setting) + field check

Sealed 2026-10-30 by the proof seat, before any run of the data items. Smoke test (seed 7, 2 items per block, N = 60)
was run only to debug gp syntax; its output is lp/smoke_out.txt (instrument check, not scored).

## Instruments (sha256)
- lp/z3p.gp 83457a87075b996ad333b38f4b5541d745970d10c625437a8fa2796e1a8d24a1 (WSL PARI 2.17.3, prints nbthreads 1, setrand(20261030))
- lp/run_z3p.sh 1c8067f7c0bbe67dc99962fd92759970e3d99553b3813716922327c65d01523b (1 core, cap 1200 s)
All tests are exact: rational coefficients, real-rootedness = polsturm of the squarefree part equals its degree.

## Items and bars
- PC (positive controls, must hold or nothing is scored): Lambda(x^2+1) = 1/2 exactly (real-rooted at 1/2, not at
  1/2 - 2^-20, bisection bracket width < 1e-4 containing 1/2); D_c(x,x) = x^2 - c real, D_{-c}(x,x) = x^2 + c not (c=1).
- I (identity, algebra): e^{-tD^2}(pq) == [e^{-2t dx dy} p_t(x) q_t(y)]_{x=y} exactly; 100 random pairs x 4 values of
  t (including t < 0). Bar: 0 failures of 400.
- K (NEW content, key step and SIGN): 400 random real-rooted pairs (integer roots in [-10,10], degrees 1..8, repeats
  allowed), c in {1/8, ..., 5}. Bar: D_c = sum_k (-c)^k/k! p^(k) q^(k) real-rooted for ALL 400 (0 violations).
- K-null (opposite sign, e^{+c dx dy}): same pairs with -c. Prediction: violations in >= 30% of pairs.
- L (NEW content, Lemma P for polynomials): 300 random pairs, degrees 2..6, at least one factor with non-real roots.
  t* = max(Lambda_p^hi, Lambda_q^hi, 0) (bisection upper ends, exact dyadics; hypothesis asserted: p_t*, q_t* real-rooted).
  Bar: e^{-t* D^2}(pq) real-rooted for ALL 300. Reported: number with Lambda(pq) strictly below the max by > 1e-3.
- NL (null: the role of the 0): 300 pairs of real-rooted, distinct-integer-root polynomials (degrees 2..6) with
  Lambda < 0, t' = max(Lambda_p^hi, Lambda_q^hi) < 0. Prediction: pq at t' NOT real-rooted in >= 50% of pairs.
- F (classical identities, checks of the corollary normalisation): F1 zeta_K coefficients == 1 * a_f, n <= 3000
  (K = Q[x]/(x^3-x-1), f = eta(z)eta(23z)); F2 lfunparams reported (expect [23,1,[0,0,1]], [1,1,[0]], [23,1,[0,1]]);
  F3 Lambda_K/(Lambda_zeta Lambda_f) = 1 to 1e-25 at s = 0.3+5i and 2+i (PARI completed functions);
  F4 zeta_H == zeta * L(chi_-23) * L(f)^2, n <= 2000, H = nfsplitting(x^3-x-1). Bar: F1, F3, F4 true.

## Decision
- PC, I, K, L hold and both nulls fire: the numerics support the sign and Lemma P (support, not proof).
- K or L violated: Lemma P (or the key step) is FALSE as stated; PROOF-P must be withdrawn.
- A null misses: reported as a null failure (weak null), main bars still scored.
