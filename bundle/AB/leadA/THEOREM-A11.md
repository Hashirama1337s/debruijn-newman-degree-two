# THEOREM A11 — the same explicit de Bruijn–Newman bound for a second degree-2 L-function (p = 11)

Moki & Julio (AI-assisted). Lab record, 2026-10-28. Not published.

**Status:**
- Every computational piece is certified and sealed: BAR-A9 (tail) HOLDS, BAR-A10 (control + rate) HOLDS, BAR-A11
  (finite region) HOLDS.
- The method and the tail lemma are those of THEOREM-A, which passed both referee reads.
- Referee on THEOREM-A11: **ACCEPTED WITH FIXES** (none touching the bound), all applied:
  - the character identification (LMFDB 44.21 = psi_{-44});
  - Kani Cor. (4) for the Euler factors at 2 and 11;
  - the TAIL-LEMMA N = 44 addendum, with the Palojärvi–Zhao hypothesis quoted;
  - BAR-A11 P3 recorded as a MISS;
  - the high-x null control BAR-A15 (HOLDS);
  - the calibration wording.
  The optional Sturm-bound note is not added, because no source for the eta-quotient criterion was opened.

## In plain words
THEOREM-A proved Lambda <= 0.48994 for one degree-2 L-function, that of eta(z)eta(23z). Here the same method runs,
unchanged except for the level, on a second one: the L-function of eta(2z)eta(22z), the cubic ring-class character
of Q(sqrt -11) at level 44. It reaches the same bound. The heavy part shrinks: the far-out lemma already works from
x = 2,800 instead of 7,200, and the certified near region took about 0.64 h. So the method is not a one-off.

## Statement
Let f(z) = eta(2z) eta(22z), the weight-1 newform 44.1.d.a. Its L-function is L(s) = sum a_n n^{-s} = L(s, chi), with
chi the order-3 ring-class character of discriminant -44 (the order Z[sqrt -11], h(-44) = 3).

Let xi(s) = (sqrt44/(2pi))^s Gamma(s) L(s), so that xi(s) = xi(1-s). As in Dobner (arXiv:2005.05142, eqs. (5), (6)):
- Phi(u) = 2 e^u f(i e^{2u}/sqrt44);
- H_t(z) = int_R e^{tu^2} Phi(u) e^{izu} du, so that H_0(z) = xi((1+iz)/2).

**Theorem A11.** For every t >= 21/50 + (374/1000)^2/2 = 0.489938, all zeros of H_t are real. Hence
0 <= Lambda_chi <= 0.489938 < 0.49. The lower bound is Dobner Thm 2.

## Identification of f (OPENED sources)
1. LMFDB 44.1.d.a (OPENED): "f(z) = eta(2z)eta(22z)"; weight 1, level 44, character orbit 44.d of order 2; CM by
   Q(sqrt -11); Artin image S3, projective D3; "This newform subspace is the entire newspace S_1^new(44,[chi])",
   of dimension 1.
   The character is LMFDB 44.21 (OPENED): modulus 44, conductor 11, order 2, odd, induced from chi_11(10, .). That is
   exactly psi_{-44} = (-44/.), the nebentypus Kani attaches to binary theta series of discriminant -44 (equal to
   (-11/n) for odd n and 0 for even n). So theta_chi and f lie in the same one-dimensional space
   S_1^new(44, psi_{-44}).
2. Kani, "Binary Theta Series and CM Modular Forms" (2010 slides, OPENED):
   - p. 1 (Hecke 1926, Schoeneberg 1939): theta_q is in M1(|D|, psi_D).
   - p. 3: theta_chi has multiplicative coefficients and is a Hecke eigenform.
   - p. 5, Thm 1: theta_chi is a cusp form iff chi is not quadratic.
   - Thm 3(b): for chi = chi_pr primitive, theta_chi is a newform of level |D_chi|.
   For D = -44 = 2^2(-11): Cl(-11) is trivial, so the order-3 character of Cl(-44) is primitive, with D_chi = -44.
   Hence theta_chi = (theta_{x^2+11y^2} - theta_{3x^2+2xy+4y^2})/2 is a cuspidal newform of level 44. By dimension 1,
   **f = theta_chi**. PARI checks this coefficient-wise to n <= 3000 (refs44.txt), as a consistency control only.
3. **Consequences.** Euler factors from Kani's Corollary (4) (p. 6, OPENED):
   L(s, chi) = prod_p L_p(s, chi), with L_p = (1 - a_p(chi) p^{-s} + psi_D(p) p^{-2s})^{-1} for p not dividing
   fbar_chi. Here fbar_chi = 1, because chi is primitive at D = -44.
   - p = 2: psi_{-44}(2) = 0 and a_2 = 0, so L_2 = 1.
   - p = 11: psi_{-44}(11) = 0 and a_11 = 1, so L_11 = (1 - 11^{-s})^{-1}.
   Further consequences (Hecke L-function of a character of K = Q(sqrt -11) of conductor 2):
   - a_n = sum over ideals a of O_K coprime to 2 with N(a) = n of chi~(a), so |a_n| <= d(n);
   - L(s) = prod_p (local factors);
   - p = 2 (divides the conductor; 2 is inert in K): factor 1, and a_{2^k} = 0;
   - p = 11 (ramified, (sqrt -11) principal in the order): (1 - 11^{-s})^{-1};
   - split p: (1-u)^{-2} or (1+u)/(1-u^3) in |a_n|;
   - inert p: (1-u^2)^{-1}.

## Dobner's axioms for F = L(s, eta(2z)eta(22z))
- **(i)** Absolutely convergent for Re s > 1, since |a_n| <= d(n).
- **(ii)** Entire of finite order (cuspidal newform), so m = 0.
- **(iii)** gamma(s) = (sqrt44/(2pi))^s Gamma(s): alpha = 1, Q = sqrt44/(2pi), omega = 1, mu = 0. xi(s) = xi(1-s)
  with root number +1, by the evenness of Phi (Step 0); coefficients are real.

## Proof chain (same as THEOREM-A with N = 44)
**Step 0 — evenness on the ray tau = iy.**
f(-1/(44 tau)) = eta(-1/(22 tau)) eta(-1/(2 tau)) = sqrt(22y) sqrt(2y) eta(22 tau) eta(2 tau) = sqrt44 · y · f(tau).
Both square roots are of positive reals. With y = e^{2u}/sqrt44: f(i e^{-2u}/sqrt44) = e^{2u} f(i e^{2u}/sqrt44). So
Phi(-u) = Phi(u), and Phi is real and decays doubly exponentially.

**Step 1 — de Bruijn, first use.**
- xi(s) != 0 for Re s > 1 (q^s != 0, Gamma has no zeros, Euler product). By xi(s) = xi(1-s), also for Re s < 0.
- So the zeros of H_0 satisfy |Im z| <= 1.
- de Bruijn Thm 13, as quoted in Dobner Thm 3 (integrable, conjugate-even, O(e^{-|u|^b}), b > 2, t > 0), with
  Delta = 1: the zeros of H_{0.42} satisfy |Im z| <= 0.4.

**Step 2 — right tail** (TAIL-LEMMA.md with N = 44: Q(s) = 44 s(s+1)/(2pi)^2, q = sqrt44/(2pi), the coefficients
above; Palojärvi–Zhao v1 Lemma 3.2 = v2 Lemma 3.3 with N = 44, r = 2, theta = 0, mu = (0,1)).
- BAR-A9 HOLDS: H_{0.42}(x+iy) != 0 for x >= 2800 and y in [0.374, 0.4].
- 221 interval boxes cover x from 2800 to 2·10^12. Step 10 covers x >= 2·10^12 (error sum 0.0295 < 1; vertices
  checked).
- Cross-check at x = 2800: the certified lower bound sits below the certified |H| (log -2193.53 <= -2191.59).

**Step 3 — finite region** (BAR-A11 HOLDS):
- certified winding 0 of H_{0.42} around the boundary of [0, 2800] x [0.374, 0.41];
- 41,785 ball evaluations; every step certified by the Taylor (order 12) + Cauchy cone condition;
- 18/18 chunks exit 0; total arg change -2.9e-54 +- 1.9e-5;
- wall time about 0.64 h. This is **below** the sealed P3 range of 0.7–1.5 h, so P3 is recorded as a **MISS** (P3 was
  reported, not scored);
- control (BAR-A10 P0): [5,15] x [-0.2, 0.2] gives certified winding 3, equal to PARI's independent count of real
  sign changes (7.45, 11.0, 14.0);
- high-x null control (BAR-A15, added at the referee's request): [2696, 2700] x [-1/2, 1/2] gives certified winding
  5 (+-4e-23), equal to the independent PARI float prediction (null44.gp: 2696.42, 2697.28, 2698.14, 2699.0,
  2699.84);
- no pause and no resume in this run.

**Step 4 — cover.**
- 0 <= x <= 2800 and 0.374 <= y <= 0.41: Step 3.
- x >= 2800 and 0.374 <= y <= 0.4: Step 2.
- y > 0.4: Step 1.
- x < 0 and y < 0: the symmetries H(-conj z) = conj H(z) and H(conj z) = conj H(z).
- So every zero of H_{0.42} has |Im z| < 0.374.

**Step 5 — de Bruijn, second use.**
- Thm 13 (Dobner Thm 3) is applied to phi = e^{0.42 u^2} Phi with Delta = 0.374, as in Dobner's proof of Thm 1 (p. 11).
- All zeros of H_t are real for t >= 0.42 + 0.374^2/2 = 0.489938.

## Every assumption, stated
These are identical to THEOREM-A:
- MPFR 4.2.2 / MPC 1.4.0 correct rounding (gmpy2 2.3.1);
- float radii inflated, with libm exp/expm1/asin/sqrt within 1 ulp;
- mpmath 1.3.0 `iv` for the tail and the quadrature majorants;
- PARI only as a reference.

Specific to N = 44:
- The eta evaluator uses f(tau) = eta(2 tau) eta(22 tau), computed through the same certified eta() (SL2(Z) reduction).
- The majorant is |f(tau)| <= 44^{-1/4} S^2 Im(tau)^{-1/2}, from |eta(w)| <= S Im(w)^{-1/4} at w = 2tau and 22tau.
- The q-tail is |f| <= r/(1-r)^2.
- Calibration (unsealed, check44.py):
  - the two t = 0 lfunlambda references lie inside the certified balls;
  - the two independent Gaussian-average references at t = 0.42 agree with the ball midpoints within the 1e-20
    relative tolerance allowed for the references' own error (7.8e-28 and 3.6e-21). This is a match within
    tolerance, not containment in the balls.

## Hashes (sha256)
**Seals** (lines in rh-recon/LOG.md):

| seal | hash | sealed |
|---|---|---|
| BAR-A9 | 34a62bc2…f938c | 15:40 |
| BAR-A10 | 26476211…4b98e | 15:46 |
| BAR-A11 | 032524ad…7f380 | 15:47 |
| BAR-A15 (null control) | see LOG.md | sealed and scored HOLDS |

**Code and data:**

| file | sha256 |
|---|---|
| cert_core44.py | be616cfa23cb833aefe775ac31db5cbfe96628595d45c774d4814b0a6fe98b79 |
| cert_wind_ckpt44.py | 554edc4ca7719accee9c18900fa90fbb1882d20943f08b4d2057b3fbad6046b8 |
| tail_cert44.py | eb3e9004a64c80322706e320017087707eb6189d06269bc355cbcb73b83d928d |
| tail_run44.py | a7261c28769f1992bb3e4457a3407749c6aa5fef0d3c2cce8843c39830deeb60 |
| cert_combine44.py | c196066f7b10eaae7bdcf7c56a364bc65de3ccca8ead07b80b3c9baa6049ffda |
| run_finite44.sh | 91b4d50093159a3080b93e92fab403cfc370720764396718f21cf7b83d06018b |
| refs44.txt | 29ebb9f8645a28dd41ea2d6fca7d10234bd0138fd4a4ba4bdae8a1170cdccc92 |
| TAIL-LEMMA.md (shared lemma, current) | ad7e96fdc652538f1aaf36839e11cccae80767c93030f31f0d68c43c056e518c |

**Outputs:**

| file | sha256 |
|---|---|
| fin_combine.json (BAR-A11) | 1548aaad32531b9155875ccae727477371d10d1bd48b59b441b38756a630f8e9 |
| tail_run_out.json (BAR-A9) | 6e774dfca1fd82945d4bf4d179b82a49ef7eb971c2fd62a130ed78c850810bac |

## Ceiling
The same small gain over 1/2, now for a second form. It shows the pipeline (eta evaluator + interval tail +
certified winding) moves between levels with only N-changes whenever f is an eta product.
