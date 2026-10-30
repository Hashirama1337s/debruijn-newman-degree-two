# BAR-A9 — sealed tail certificate for the second case p = 11 (f = eta(2z)eta(22z), LMFDB 44.1.d.a, N = 44)

## Parameter changes (PARAMS)
- Form: f = eta(2z)eta(22z). LMFDB 44.1.d.a (OPENED): newform, CM by Q(sqrt -11), projective image D3, and
  "This newform subspace is the entire newspace S_1^new(44,[chi])", dimension 1.
- Theta series: Kani 2010 slides (OPENED) Thm 3(b). The order-3 ring-class character of disc -44 = 2^2(-11) is
  primitive, because Cl(-11) is trivial. So theta_chi = (theta_{x^2+11y^2} - theta_{3x^2+2xy+4y^2})/2 is a newform of
  level 44, and it equals f by dimension 1. PARI checks this to n <= 3000.
- Consequences:
  - a_n = sum over ideals coprime to 2 of norm n of chi~(a), hence |a_n| <= d(n);
  - Euler product with local factors: p = 2 -> 1 (2 divides the conductor), p = 11 -> (1-u)^{-1}, split p ->
    (1-u)^{-2} or (1+u)/(1-u^3), inert p -> (1-u^2)^{-1}.
- Completed function: xi(s) = (sqrt44/2pi)^s Gamma(s) L(s), Gamma_C, mu = (0, 1), N = 44.
- Evenness of Phi, on the ray: f(-1/(44 tau)) = sqrt(22y) sqrt(2y) f(tau) = sqrt44 y f(tau). So Phi(u) = 2e^u f(ie^{2u}/sqrt44)
  is even, and the root number is +1.
- Palojärvi–Zhao lemma: same hypotheses (r = 2, theta = 0, mu = (0,1)), now with N = 44.
- Code: p11/tail_cert44.py and tail_run44.py, copies of the AMEND2 tail code with N = 44, the forms of disc -44 and
  the local types above. p11/cert_core44.py is the AMEND1 evaluator with f = eta(2tau)eta(22tau) and
  C = 44^{-1/4} S^2.
- Calibration, not sealed: check44.py enclosures contain 4 PARI references, 2 of them independent Gaussian averages
  at t = 0.42.

## Claim tested
H_{21/50}(x+iy) != 0 for x >= 2800 and y in [0.374, 0.4] (p = 11), with eps = 1/5. The exploratory scan (not a
certificate) gave a positive margin from x = 2800.

## Predictions (all required)
- A: boxes cover T in [1400, 1e12] with every margin > 0.
- B: the asymptotic check at T1 = 1e12 passes.
- C: the certified lower bound at x = 2800, y = 0.374 is <= the certified |H| from cert_core44.
- Time under 30 min.

## Hashes
be616cfa23cb833aefe775ac31db5cbfe96628595d45c774d4814b0a6fe98b79 *cert_core44.py
eb3e9004a64c80322706e320017087707eb6189d06269bc355cbcb73b83d928d *tail_cert44.py
a7261c28769f1992bb3e4457a3407749c6aa5fef0d3c2cce8843c39830deeb60 *tail_run44.py
