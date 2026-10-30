# THEOREM A — an explicit de Bruijn–Newman bound for a degree-2 L-function

Moki & Julio (AI-assisted). Lab record, 2026-10-28. Not published.

**Status:**
- Every computational piece is certified and sealed.
- Referee verdicts:
  - REFEREE-A4 (finite-region method): accepted with fixes, applied.
  - REFEREE-A6 (tail): accepted with fixes, applied.
  - **Local referee on the full chain: ACCEPTED WITH FIXES**, applied (identification f = theta_chi from opened
    sources).
  - **Second referee (referee 2) on the full chain: ACCEPTED WITH FIXES**, applied: Step 1 in terms of xi, Dobner's axioms
    checked, Thm 3 hypotheses quoted, evenness proved on the ray only.
    - One referee-2 item was checked and **not adopted**: it said Palojärvi–Zhao v2 has no Lemma 3.3. I opened v2
      (header 08 Aug 2026): Lemma 3.2 is the gamma ratio and **Lemma 3.3 is the pointwise bound**, so the citation
      "v1 Lemma 3.2 = v2 Lemma 3.3" stands.
- Prior art (referee 2 search): **OPEN**. No published explicit upper bound below 1/2 for any degree-2 de Bruijn–Newman
  constant was found.

## In plain words
Every L-function has a "heat dial" t. Turn it up and the function's zeros are pushed onto a single line. The smallest
setting at which all zeros sit on the line is the de Bruijn–Newman constant, Lambda. The Riemann hypothesis for that
L-function is the statement Lambda <= 0. Lambda is known to be >= 0, and easy theory gives Lambda <= 1/2.

Until now, numbers below 1/2 had been proved only for the Riemann zeta function and, in October 2026, for real
Dirichlet characters. Both are "degree 1".

We prove **Lambda <= 0.48994** for the L-function of the modular form eta(z)eta(23z). That is a degree-2 L-function:
the L-function of the cubic class-group character of Q(sqrt -23). As far as our search found (search floor), this is
the first explicit bound below 1/2 for any degree-2 L-function.

How:
- At dial setting 0.42 we show that no zero lies above height 0.374.
- Far out (x >= 7,200), a lemma does this: the dominant term beats every error term. That lemma is checked by computer
  in interval arithmetic.
- Near the start (x <= 7,200), a certified winding-number count shows that no zero is enclosed.
- Then de Bruijn's classical theorem finishes the job: 0.42 + 0.374^2/2 = 0.48994.

The gain over 1/2 is small, and it is not a step toward the Riemann hypothesis. Its value is that the method now works
in degree 2.

## Statement
Let f(z) = eta(z) eta(23z), the weight-1 newform 23.1.b.a. Its L-function is L(s) = sum a_n n^{-s} = L(s, psi), with psi
the order-3 class-group character of Q(sqrt -23).

Let xi(s) = (sqrt23/(2pi))^s Gamma(s) L(s), so that xi(s) = xi(1-s). Following Dobner (arXiv:2005.05142, eq. (6)), define:
- Phi(u) = (1/2pi) int xi((1+ix)/2) e^{-ixu} dx = 2 e^u f(i e^{2u}/sqrt23);
- H_t(z) = int_R e^{t u^2} Phi(u) e^{izu} du, so that H_0(z) = xi((1+iz)/2).

**Theorem A.** For every t >= 21/50 + (374/1000)^2/2 = 0.489938, all zeros of H_t are real. Hence the de Bruijn–Newman
constant of L(s, psi) satisfies 0 <= Lambda_psi <= 0.489938 < 0.49. The lower bound is Dobner Thm 2.

## Proof chain
**Step 0 — properties of Phi.**
- Eta transformation, used only on the ray tau = i y, y > 0. There -i tau = y > 0 and -i 23 tau = 23y > 0, so both
  principal square roots are of positive reals and no branch question arises:
  f(-1/(23 tau)) = sqrt(23 y) sqrt(y) f(tau) = sqrt23 · y · f(tau).
  With tau = i e^{2u}/sqrt23 (y = e^{2u}/sqrt23), -1/(23 tau) = i e^{-2u}/sqrt23, so f(i e^{-2u}/sqrt23) = e^{2u} f(i e^{2u}/sqrt23).
  Hence Phi(-u) = 2 e^{-u} f(i e^{-2u}/sqrt23) = 2 e^{u} f(i e^{2u}/sqrt23) = Phi(u) for real u.
  The evaluator extends this by analytic continuation to the strip.
- Phi is real (real a_n). Evenness is the Mellin form of the functional equation xi(s) = xi(1-s) with root number +1:
  LMFDB L-function page (OPENED in the B probe: "Sign 1", "Lambda(s) = Lambda(1-s)"), and it is proved directly by the
  line above.
- Phi decays doubly exponentially as u -> +inf (q-expansion), and as u -> -inf by evenness.
- So H_t is entire and even, H_t(conj z) = conj H_t(z), and H_t(-conj z) = conj H_t(z).
- Code record: cert_core.py docstring (AMEND1).

**Step 1 — de Bruijn, first use.**
- The statement is about xi, the completed function. For Re s > 1: xi(s) = q^s Gamma(s) L(s), q^s != 0, Gamma has
  no zeros, and L(s) = prod_p (1 - chi(p) N(p)^{-s})^{-1} != 0 (absolutely convergent Euler product of the Hecke
  L-function; see the identification below). So xi(s) != 0 for Re s > 1.
- By xi(s) = xi(1-s), also xi(s) != 0 for Re s < 0. (L itself does vanish at s = 0, -1, -2, ..., where Gamma has
  poles; that is irrelevant here.)
- Zeros of H_0(z) = xi((1+iz)/2) therefore satisfy |Im z| <= 1.
- de Bruijn's Thm 13, as quoted in Dobner arXiv:2005.05142 Thm 3 (OPENED, p. 9): "Let phi: R -> C be an integrable
  function satisfying phi(u) = conj phi(-u) and phi(u) = O(e^{-|u|^b}) for some b > 2". For any t > 0, if all roots of G
  lie in |Im z| <= Delta, then all roots of G_t lie in |Im z| <= (max(Delta^2 - 2t, 0))^{1/2}.
  - Phi is integrable, real and even, hence conjugate-even.
  - Its doubly exponential decay gives O(e^{-|u|^b}) for every b.
- With phi = Phi and Delta = 1: all zeros of H_{0.42} satisfy |Im z| <= 0.4.

**Step 2 — right tail** (TAIL-LEMMA.md; certificate BAR-A6-AMEND1 HOLDS, re-run under BAR-A6-AMEND2 HOLDS, referee
REFEREE-A6 accepted with fixes, all applied).
H_{0.42}(x+iy) != 0 for all x >= 7200 and y in [0.374, 0.4]:
- interval boxes cover 7200 <= x <= 2·10^12 (233 boxes, 8 y-subboxes each);
- the monotonicity argument (Step 10 of the lemma) covers x >= 2·10^12.

**Step 3 — finite region** (certificate BAR-A8 HOLDS; method validated by BAR-A4-AMEND1, referee REFEREE-A4 accepted
with fixes, all applied).
- H_{0.42} has no zeros in the closed rectangle [0, 7200] x [0.374, 0.41].
- Certified winding number 0 along its boundary.
- 111,265 ball evaluations; each step is certified by a Taylor (order 12) + Cauchy cone condition
  |H(z) - H(p)| < |H(p)|.
- Total arg change -1.1e-53 +- 6.2e-4.
- Control P0: the rectangle [5,15] x [-0.2, 0.2] gives winding 2 (two real zeros).

**Step 4 — covering the half-plane Im z >= 0.374.**
- 0 <= x <= 7200, 0.374 <= y <= 0.41: Step 3.
- x >= 7200, 0.374 <= y <= 0.4: Step 2.
- y > 0.4, any x: Step 1.
- x < 0: H(-conj z) = conj H(z) maps the case to x > 0.

So H_{0.42} has no zeros with Im z >= 0.374. Since H_{0.42}(conj z) = conj H_{0.42}(z), it has none with
Im z <= -0.374 either.

**Step 5 — de Bruijn, second use.**
- Apply Thm 13 (Dobner Thm 3) to phi = e^{0.42 u^2} Phi, which is still conjugate-even and of the required decay, as
  Dobner does in the proof of his Theorem 1 (arXiv:2005.05142, p. 11: "if t0 in Z, then by applying Theorem 3 with
  phi(u) := e^{t0 u^2} Phi_F(u), we may conclude t in Z for all t >= t0").
- e^{0.42u^2} Phi is still integrable, conjugate-even and O(e^{-|u|^b}).
- Take Delta = 0.374: every zero of G = H_{0.42} lies in |Im z| <= 0.374. Thm 3 is applied with s > 0.
- Then the zeros of H_{0.42+s} lie in |Im z| <= (max(0.374^2 - 2s, 0))^{1/2}. They are all real once
  s >= 0.374^2/2 = 0.069938.
- Hence the result for t >= 0.489938. QED, pending the final referee read.

## Dobner's axioms for F = L(s, eta(z)eta(23z)) (arXiv:2005.05142 §2, OPENED p. 7)
- **(i) Dirichlet series.** F(s) = sum a_n n^{-s} converges absolutely for Re s > 1, since |a_n| <= d(n) (identification
  below). Check: yes.
- **(ii) Meromorphic continuation.** (s-1)^m F(s) is entire of finite order for some m >= 0. Here m = 0: L(s, theta_chi)
  of a cuspidal newform is entire of finite order (Hecke). Check: yes, with no pole.
- **(iii) Functional equation.** gamma(s) = alpha s^m (s-1)^m Q^s prod Gamma(omega_i s + mu_i) with Re mu_i >= 0. Here
  alpha = 1, m = 0, Q = sqrt23/(2pi), one factor with omega = 1, mu = 0; Dobner's degree is 2 sum omega_i = 2.
  xi_F(s) = gamma(s) F(s) must equal xi_F(1-s) (Dobner's eq. (4); with real coefficients this is the same as
  conj xi_F(1 - conj s)). It holds with root number +1, by the evenness of Phi proved in Step 0 together with LMFDB's
  sign 1. Check: yes.
- Hence F is in S#. Dobner Thm 1 gives the existence of Lambda_F, and Thm 2 gives Lambda_F >= 0. His Phi_F and xi_t
  (eqs. (5), (6)) are exactly the Phi and H_t used here (gamma normalised with alpha = 1).

## Every assumption, stated
**Literature inputs (OPENED):**
- de Bruijn Thm 13 via Dobner Thm 3.
- Dobner's definitions and Thm 2.
- Palojärvi–Zhao arXiv:2508.03023 v1 Lemma 3.2 (= v2 Lemma 3.3), with Rademacher 1959 Thm 2.
- Kani 2010 slides (Hecke 1926, Schoeneberg 1939) and LMFDB 23.1.b.a, for the identification of f (see below).
- DLMF §5.11(ii) Stirling remainder bounds (sec^{2n} and sec^{2n+1} factors).
- Trefethen–Weideman, SIAM Rev. 56 (2014), Thm 5.1 (trapezoid rule in a strip).
- LMFDB 2-23-23.22-c0-0-0 / 23.1.b.a: sign +1, Gamma_C, conductor 23, Artin origin 2.23.3t2.b.

**Identification of f with the class-group theta series (OPENED sources; replaces the earlier finite check):**
1. **Weight-1 theta series.** Kani, "Binary Theta Series and CM Modular Forms" (Maine–Québec NT conference slides,
   2010, OPENED):
   - p. 1: "Hecke(1926), Schoeneberg(1939): ... theta_q in M1(|D|, psi_D)".
   - p. 3: theta_chi := (1/w_D) sum_q chi(q) theta_q has multiplicative coefficients and "is a Hecke eigenfunction".
   - p. 4, item 5: for a fundamental discriminant D, "each theta_chi is a primitive form (newform)".
   - p. 5, Theorem 1: theta_chi is a cusp form iff chi is not quadratic.
   For D = -23 (fundamental, h = 3) and chi of order 3: chi(Q1) = omega and chi(Q2) = omega^2, while
   theta_{Q1} = theta_{Q2} (the classes 2x^2 +- xy + 3y^2 are inverse). So theta_chi = (theta_{Q0} - theta_{Q1})/2
   is a normalised cuspidal newform in S1(23, psi_{-23}).
2. **Uniqueness.** LMFDB newform 23.1.b.a (OPENED): f(z) = eta(z)eta(23z) is a newform, CM by Q(sqrt -23), Artin
   image S3 / projective D3, and "This newform subspace is the entire newspace S_1^new(23,[chi])", of dimension 1.
   Both forms have a_1 = 1, so **f = theta_chi**.
3. **Consequences** (theory of the Hecke L-function of chi; Kani p. 4: L(s, theta_chi) is a classical Hecke
   L-function):
   - a_n = sum_{N(a) = n} chi(a) and L(s) = prod_p (1 - chi(p) N(p)^{-s})^{-1}, so a_n is multiplicative (Hecke
     eigenform).
   - |a_n| <= #{ideals of norm n} = sum_{d | n} chi_{-23}(d) <= d(n).
   - The local types (split with p principal, split non-principal, inert, ramified 23) follow, as used in TAIL-LEMMA
     Step 9.
   - The lattice-count check of a_n for n <= 2·10^6 is now only a consistency control, not part of the proof.
   - Gamma(z) has no zeros.

**Arithmetic assumptions:**
1. MPFR 4.2.2 / MPC 1.4.0 (gmpy2 2.3.1) are correctly rounded. All ball midpoints in Step 3 and in the cross-check
   use them.
2. Python float radii: every radius operation is inflated, by UP = 1 + 2^-50 per operation and by (1 + (n+4)2^-52)
   for n-term sums (AMEND1). libm exp, expm1, asin and sqrt are assumed within 1 ulp.
3. mpmath 1.3.0 `iv` (outward-rounded intervals) for:
   - all of Step 2 (tail);
   - the quadrature majorants of Step 3.
   Only +, -, *, /, exp, log, sqrt and cos are used; atan is an own alternating series with a remainder bound.
4. PARI/GP values serve only as references in controls. No PARI number enters any certificate.

**Run history** (honest record, all in LOG.md):
- BAR-A3: FAILED (crash).
- BAR-A4: HOLDS; then AMEND1 HOLDS.
- BAR-A6: FAILED (code gap); AMEND1 HOLDS; AMEND2 HOLDS.
- BAR-A7 rate probe: FAILED (out of band).
- BAR-A8: HOLDS.

**Pause/resume note (BAR-A8).**
- The owner paused the run once; the workers were stopped by PID. It was resumed by re-running run_finite.sh.
- A checkpoint line is written only after a whole 25-unit sub-segment is certified. An interrupted sub-segment is
  redone from its start. Each sub-segment begins by re-evaluating its start point, so the argument chain is
  continuous.
- All 18 checkpoint chains are contiguous (done = 1..n, verified). Pre-pause logs: cert/prevlogs/*.paused1.
- BAR-A8 P1 ("all 18 chunks exit 0") was scored on the resumed run. The pre-pause logs contain the non-zero exits
  caused by the owner-requested stop.

## Hashes (sha256)
**Seals** (lines in rh-recon/LOG.md):

| seal | hash | sealed |
|---|---|---|
| BAR-A4 | fb11be80…b023 | 02:32 |
| BAR-A4-AMEND1 | c42119f3…cb237 | 02:58 |
| BAR-A6 | e2d22e21…bd601 | 04:53 |
| BAR-A6-AMEND1 | f9a8cebe…fa9d4 | 04:57 |
| BAR-A6-AMEND2 | 903eca1e…2d97b | 05:18 |
| BAR-A8 | d0885b8f…48779 | 05:18 |

**Documents and code:**

| file | sha256 |
|---|---|
| TAIL-LEMMA.md (revised per REFEREE-A6) | 83b41165dd1261010879dc35a60d7ed1d5e4ffebaaac158ed6684fbb4f80dcc7 |
| tail_cert.py | 1441e756c8291387095e31d13a229224c74dad2ddae00a5644ba04f64036b7c7 |
| tail_run.py | 11c8d454602341ca2689186a4f4e18e30ad8f966925f63b262be0c4cdfae1837 |
| cert_core.py | 3c5f7f2b4ff148c1b380f6da8022e7c29e565c08491895c04fd3a41d679836df |
| cert_wind_ckpt.py | 6ba1581587df3ac93ded24df94ab9032f367dce81ee6fc40cfc7bd84df58e22c |
| cert_combine3.py | 0d28fc163ce1121ca9b2f72844d6458ab1b9214fc8c79b24044c57db9b00db0a |
| run_finite.sh | adf126fb2c2acfa178ee26967d7dcf543e26232fc1464ae6832ae0fd32f62471 |
| REFEREE-A4.md | e91504379b1702f00d75976510ef4f1344c57161ce4d79fc0992d59e19666a00 |
| REFEREE-A6.md | 59842ba9b6b64152a7789522a8960c8fff9346308f9b940e179b00022ce5b550 |

**Outputs:**

| file | sha256 |
|---|---|
| fin_combine.json (BAR-A8) | 7b86e0ec39e7fd4b223e96658cb33846026efd738afbef86073bc7334aa3e359 |
| tail_run_out.json (AMEND2 re-run) | ee0ab20cb6146c348f3942fa086c86748c879aa49cdf1da5d770fb4bc0fc3572 |

## Ceiling
- A first explicit sub-1/2 de Bruijn–Newman bound in degree 2, for one form. The method repeats for other dihedral
  forms.
- A sharper bound would need a longer finite region (cost about X^2) or an effective approximate functional equation
  in place of convexity in the tail.
- Nothing here bears on the Riemann hypothesis itself.
