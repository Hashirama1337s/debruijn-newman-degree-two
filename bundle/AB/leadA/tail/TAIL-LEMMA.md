# TAIL LEMMA — right tail for the heat flow of L(s, eta(z)eta(23z))

Status: written 2026-10-28. Computer check: BAR-A6-AMEND1 HOLDS (BAR-A6 FAILED on a code gap, see LOG). Referee
REFEREE-A6: ACCEPTED WITH FIXES. This revision applies those fixes. The code fixes are sealed as BAR-A6-AMEND2; its
re-run is scheduled after BAR-A8 frees cores.

## In plain words
The heat-flowed function at a point is an average of the completed L-function over horizontal shifts, weighted by a
bell curve. Far up the critical strip, almost all of that average comes from shifts where the L-function is a
convergent sum dominated by its first term "1". Everything else can be bounded with explicit, published estimates,
so the first term wins and the function cannot vanish. A computer checks the resulting inequality in rigorous
interval arithmetic for every height from x = 7,200 to x = 2·10^12. A monotonicity argument (Step 10) covers all
larger heights.

## Notation
- f = eta(z)eta(23z), L(s) = sum a_n n^{-s}.
- gamma(s) = q^s Gamma(s), q = sqrt23/(2pi); xi(s) = gamma(s) L(s) = xi(1-s).
- H_t(z) = int e^{tu^2} Phi(u) e^{izu} du = xi_t((1+iz)/2) (Dobner arXiv:2005.05142 eq. (6), OPENED).
- Parameters: t = 21/50, eps = 1/5, y in [0.374, 0.4], x = 2T >= 7200.
- s0 = (1-y)/2 + iT, S0 = 1 - s0, s_v = s0 + v/2, S_v = 1 - s_v.
- w(v) = (4pi t)^{-1/2} e^{-v^2/(4t)}.
- v_A = y - 1 - 2eps < 0, v_B = 1 + y + 2eps > 0.
- a0 = 1/(4t), c = (1/8)(1/T^2 + pi/T), a = a0 - c.

## Step 1 (exact identity)
H_t(x+iy) = int_R w(v) xi(s_v) dv.

Proof:
- e^{tu^2} = int w(v) e^{uv} dv, so H_t(z) = int w(v) H_0(z - iv) dv. Fubini applies because int e^{tu^2}|Phi(u)| du is
  finite (doubly exponential decay of the even function Phi).
- H_0(z - iv) = xi(s0 + v/2).

## Step 2 (split)
By xi(s) = xi(1-s):
- v <= v_A: xi(s_v) = gamma(S_v) L(S_v), with Re S_v = (1+y-v)/2 >= 1+eps.
- v >= v_B: xi(s_v) = gamma(s_v) L(s_v), with Re s_v = (1-y+v)/2 >= 1+eps.

So H = M + E_A + E_B + E_M, where:
- M = int_{v<=v_A} w gamma(S_v) dv;
- E_A = int_{v<=v_A} w gamma(S_v)(L(S_v) - 1) dv;
- E_B = int_{v>=v_B} w gamma(s_v) L(s_v) dv;
- E_M = int_{v_A<v<v_B} w xi(s_v) dv.

If |M| > |E_A| + |E_B| + |E_M|, then H_t(x+iy) != 0.

## Step 3 (gamma along horizontal lines)
For z0 with |Im z0| = T >= 1, let g = log gamma on the half plane containing z0 + R. Then
g(z0 + v/2) = g(z0) + (v/2) g'(z0) + r(v), with |r(v)| <= c v^2.

- Proof: Taylor with integral remainder, |g''| = |psi'(z)| <= sum_{k>=0} |z+k|^{-2} <= 1/T^2 + pi/T. The summand is
  unimodal in k, so the sum is at most max + int_R du/(u^2+T^2).
- Define alpha = -g'(S0)/2, beta = g'(s0)/2. Then:
  - gamma(S_v) = gamma(S0) e^{alpha v + r(v)};
  - |gamma(S_v)| <= |gamma(S0)| e^{Re(alpha) v + c v^2};
  - |gamma(s_v)| <= |gamma(s0)| e^{Re(beta) v + c v^2}.
- g' = log q + psi, with psi(z) = log z - 1/(2z) + R, |R| <= sec^3(ph z/2)/(12|z|^2) (DLMF 5.11.2 with the
  §5.11(ii) bound, OPENED).
- rho = |gamma(s0)|/|gamma(S0)| comes from DLMF 5.11.1:
  log Gamma(z) = (z-1/2) log z - z + log sqrt(2pi) + R1, |R1| <= sec^2(ph z/2)/(12|z|).
  The difference is written without the large T pi/2 terms:
  log rho = -y log q - (y/2)(log|z1| + log|z2|) + T(atan(s1/T) - atan(s2/T)) + y +- E,
  with z_j = s_j + iT, s1 = (1-y)/2, s2 = (1+y)/2.

## Step 4 (Gaussian facts)
- (G1) int_R w e^{alpha v} dv = e^{t alpha^2} (complex alpha).
- (G2) (4pi t)^{-1/2} int_R e^{-a v^2 + b v} dv = (4pi t)^{-1/2} sqrt(pi/a) e^{b^2/(4a)} =: F(a, b).
- (G3) Tangent bounds (concavity of -a v^2 + bv), with W := (4pi t)^{-1/2}:
  - W int_{-inf}^{u} e^{-a v^2+bv} <= W e^{-a u^2 + b u}/(b - 2au) if b > 2au;
  - W int_u^{inf} e^{-a v^2+bv} <= W e^{-a u^2+bu}/(2au - b) if 2au > b.
- F(a, b) is increasing in |b|.

## Step 5 (main term)
|M|/|gamma(S0)| >= e^{t Re(alpha^2)} - TM - TAY, where:
- TM = W int_{v>v_A} e^{-a0 v^2 + Re(alpha) v} is bounded by (G3);
- TAY = F(a, Re alpha) - F(a0, Re alpha), which bounds int_{v<=v_A} w e^{Re(alpha) v}(e^{c v^2} - 1).

The reason: int_{v<=v_A} w e^{alpha v + r} = (G1) - int_{v>v_A} w e^{alpha v} + int_{v<=v_A} w e^{alpha v}(e^{r} - 1),
with |e^r - 1| <= e^{c v^2} - 1.

## Step 6 (E_A)
- Using n^{-Re S_v} = n^{-(1+y)/2} n^{v/2} and Tonelli:
  |E_A|/|gamma(S0)| <= sum_{n>=2} |a_n| n^{-(1+y)/2} I_n, with I_n = W int_{v<=v_A} e^{-a v^2 + b_n v} dv and
  b_n = Re(alpha) + (log n)/2, increasing in n.
- I_n <= min(F(a, b_n), (G3) if b_n > 2a v_A). Terms 2 <= n <= N = 4000 are summed exactly.
- Tail, case b_{N+1} > 2a v_A: n^{-(1+y)/2} e^{b_n v_A} = e^{Re(alpha) v_A} n^{-(1+eps)}, so
  sum_{n>N} <= W e^{-a v_A^2 + Re(alpha) v_A}/(b_{N+1} - 2a v_A) · R_N,
  with R_N := B(sigma') - sum_{n<=N} |a_n| n^{-sigma'} >= sum_{n>N} |a_n| n^{-(1+eps)}, for sigma' <= 1+eps
  (B is decreasing; sigma' is 1+eps rounded down).
- Tail, case b_{N+1} <= 2a v_A: choose n_c with b_{n_c+1} > 2a v_A (checked in intervals).
  - On (N, n_c], b_n is negative and increasing, and the code checks b_{N+1} < 0 and b_{n_c} <= -b_{N+1} in
    intervals. So |b_n| <= |b_{N+1}| and F(a, b_n) <= F(a, b_{N+1}).
  - Rankin: sum_{n<=n_c} |a_n| n^{-(1+y)/2} <= n_c^{1+eps-(1+y)/2} B(sigma').
  - n > n_c: the (G3) tail as above, with denominator b_{n_c+1} - 2a v_A.

## Step 7 (E_B, written out)
- |E_B|/|gamma(S0)| <= rho sum_{n>=1} |a_n| n^{-(1-y)/2} J_n, with J_n = W int_{v>=v_B} e^{-a v^2 + b'_n v} dv and
  b'_n = Re(beta) - (log n)/2, decreasing in n.
- J_n <= min(F(a, b'_n), (G3) if 2a v_B > b'_n). Terms n <= N are summed exactly.
- The tail identity is n^{-(1-y)/2} e^{b'_n v_B} = e^{Re(beta) v_B} n^{-(1+eps)}, since (1-y)/2 + v_B/2 = 1+eps.
- Tail, case 2a v_B > b'_{N+1}: sum_{n>N} <= W e^{-a v_B^2 + Re(beta) v_B}/(2a v_B - b'_{N+1}) · R_N.
- Tail, case 2a v_B <= b'_{N+1} (large T; added in AMEND1): choose n_c' with b'_{n_c'+1} < 2a v_B (checked).
  - On (N, n_c'], b'_n is positive (b'_{N+1} > 0 checked) and decreasing, and the code checks b'_{n_c'} >= -b'_{N+1}.
    So |b'_n| <= b'_{N+1} and F(a, b'_n) <= F(a, b'_{N+1}).
  - Rankin: sum_{n<=n_c'} |a_n| n^{-(1-y)/2} <= n_c'^{1+eps-(1-y)/2} B(sigma').
  - n > n_c': the (G3) tangent tail with denominator 2a v_B - b'_{n_c'+1}, times R_N.

## Step 8 (E_M, convexity)
- For sigma in [-eps, 1+eps]: |L(sigma+iT)| <= b_{1+eps} |Q(2+s)|^{(1+eps-sigma)/2}, with
  Q(s) = N prod_j (s+mu_j)/(2pi) = 23 s(s+1)/(2pi)^2.
- Source: Palojärvi–Zhao arXiv:2508.03023, **v1 Lemma 3.2 = v2 Lemma 3.3** (OPENED; in v2, Lemma 3.2 is a gamma-ratio
  lemma). It uses Rademacher's Phragmén–Lindelöf [Rad59, Thm 2].
- Hypotheses: polynomial Euler product, r = 2, theta = 0, mu = (0,1), N = 23, eps = 1/5 in (0, 1/2]. The L-function
  is entire, so P = 1. L(s, psi) is the Artin L-function of the 2-dim dihedral representation (LMFDB origin
  2.23.3t2.b, OPENED).
- b_{1+eps} = sup|L(1+eps+it)| <= B(1+eps) <= B(sigma').
- With v = 2 sigma - 1 + y:
  |E_M|/|gamma(S0)| <= rho B(sigma') int_{-eps}^{1+eps} 2W e^{-a v^2 + Re(beta) v} |Q(2+s_v)|^{(1+eps-sigma)/2} dsigma.
  This is an upper Riemann sum on 200 interval cells.

## Step 9 (B(sigma) = sum |a_n| n^{-sigma})
- |a_n| is multiplicative: f = theta_chi is the Hecke theta series of the order-3 class-group character (THEOREM-A,
  identification via Kani 2010 slides and LMFDB 23.1.b.a), with Euler product prod (1 - chi(p) N(p)^{-s})^{-1}.
  The local factors, with u = p^{-sigma}, are:
  - p = 23: (1-u)^{-1};
  - inert p: (1-u^2)^{-1};
  - split p with principal prime ideals (a_p = 2): (1-u)^{-2};
  - split, non-principal (a_p = -1): (1+u)/(1-u^3), from |sum_{i<=k} omega^{2i}| = 1, 1, 0 periodic.
- Exact product for p <= 2·10^6. Types are read from the exact a_p, i.e. the lattice counts, checked against
  eta(z)eta(23z).
- For p > P: each factor <= (1-u)^{-2}, and sum_{p>P} p^{-sigma} <= sum_{m odd>P} m^{-sigma} <= (P-1)^{1-sigma}/(2(sigma-1)).
- Every float argument sigma passed to B is rounded **downward** (nextafter). Since B is decreasing, the result stays an
  upper bound (AMEND2).

## Step 10 (all T >= T1 = 10^12; written out)
Let Lam = (1/2) log(qT), A = -Re alpha, B = Re beta.

**Facts used** (for T >= T1):
- |A - Lam|, |B - Lam| <= delta := 1/T^2. From Step 3, |Re psi(z) - log T| <= sigma^2/(2T^2) + sigma/(2T^2) + 1/(6T^2).
  The referee's sharper value is 0.42/T^2.
- |Im alpha| <= 0.79, so e^{t Re(alpha^2)} >= e^{tA^2}/K0 with K0 = e^{t·0.79^2}.
- rho <= e^{-2y Lam + 1/T}. Derivation: log|z_j| >= log T, and T(atan(s1/T) - atan(s2/T)) <= -y + s2^3/(3T^2),
  using atan u >= u - u^3/3. The Stirling errors are < 1/(2T).
- 1/(4a) = t(1+kappa), kappa = 4tc/(1 - 4tc).

**Bounds** (each divided by e^{tA^2}/K0; y, v_A, v_B are taken at the worst end of their ranges):
- P1 (TM) = K0 e^{-(2t(Lam - delta) - |v_A|max)^2/(4t)} / ((Lam - delta - 2a0|v_A|max) sqrt(4pi t)).
  This uses -a0 v_A^2 + A|v_A| - tA^2 = -(2tA - |v_A|)^2/(4t).
- P2 (TAY) = K0 (kfac - 1), with kfac = sqrt(a0/a) e^{t kappa (Lam + delta)^2}.
  This uses F(a, -A)/e^{tA^2} = sqrt(a0/a) e^{t kappa A^2} and F(a0, -A) = e^{tA^2}.
- P3 (E_A, l_n := log n <= 2A) = K0 kfac (B((1+y_lo)/2 + t(Lam - delta)/2) - 1).
  This uses (A - l/2)^2 <= A^2 - A l/2 for l <= 2A, so the n-th term is <= kfac n^{-(1+y)/2 - tA/2}.
- P4 (E_A, l_n > 2A; there b_n >= 0, so b_n - 2a v_A >= 2a|v_A|) =
  K0 e^{-a v_A^2 + (Lam + delta)|v_A|max - t(Lam - delta)^2} / (2a |v_A|min sqrt(4pi t)) · B(sigma').
- P5 (E_B, l_n <= 2B) = K0 rho kfac e^{4t Lam delta} B((1-y_hi)/2 + t(Lam - delta)/2).
  This uses (B - l/2)^2 <= B^2 - Bl/2 and B^2 - A^2 <= 4 Lam delta. The n = 1 term is included, hence no "-1".
- P6 (E_B, l_n > 2B; b'_n < 0) =
  K0 rho e^{-a v_B^2 + (Lam + delta) v_B,max - t(Lam - delta)^2} / (2a v_B,min sqrt(4pi t)) · B(sigma').
- P7 (E_M) = K0 rho B(sigma') 2(1+2eps)/sqrt(4pi t) · e^{(Lam + delta) v_B,max + 2 Lam (1+2eps) - t(Lam - delta)^2}
  · (1 + 25/T^2)^{(1+2eps)/2}. This uses e^{-av^2 + Bv} <= e^{B v_B} and |Q(2+s)| <= (qT)^2 (1 + 25/T^2).

**Why everything decreases in T for T >= T1:**
- kfac: kappa is about pi t/(2T), so t kappa Lam^2 is about (log T)^2/T, decreasing for T >= e^2.
- e^{4t Lam delta} = e^{4t Lam/T^2}: decreasing.
- rho bound: decreasing.
- B(sigma0 + t Lam/2): decreasing in Lam.
- Each e^{-t Lam^2 + p Lam} factor decreases for Lam - delta > p/(2t). The vertices are 1.22 (P1, P4), 2.14 (P6)
  and 4.59 (P7), against Lam(T1) = 13.68.
- The arguments of B exceed 1.

**Result at T1** (BAR-A6-AMEND1): 1 - P1 - P2 >= 0.99999999993 > P3 + ... + P7 <= 0.1396. The referee rebuilt
P1–P7 independently (0.1396).

## Conclusion (pending BAR-A8 and the final referee read)
- H_{21/50}(x+iy) != 0 for x >= 7200 and y in [0.374, 0.4] (this lemma). By symmetry H(-conj z) = conj H(z), the same
  holds for x <= -7200.
- Zeros of H_{21/50} satisfy |Im z| <= sqrt(1 - 2·0.42) = 0.4. This is de Bruijn's Thm 13 as quoted in Dobner,
  arXiv:2005.05142 Thm 3 (OPENED). Phi is real, even and decays doubly exponentially, and all zeros of
  H_0 = xi((1+iz)/2) lie in |Im z| <= 1.
- With the certified finite region [0, 7200] x [0.374, 0.41] (BAR-A8), H_{21/50} has no zeros with Im z >= 0.374.
- Applying de Bruijn Thm 13 again, to phi = e^{(21/50) u^2} Phi exactly as Dobner does (local text l.594), all zeros
  of H_t are real for t >= 0.42 + 0.374^2/2 = 0.489938.
- So Lambda_psi <= 0.489938 < 0.49.
- Note: the earlier citation "arXiv:2610.27343 Thm 2.6" is replaced. That theorem is stated only for real Dirichlet
  characters.

## Addendum — N = 44 (p = 11: f = eta(2z)eta(22z), THEOREM-A11)
The lemma is written for N = 23. For N = 44 every step holds verbatim with these replacements:
- q = sqrt44/(2pi); xi(s) = q^s Gamma(s) L(s); Q(s) = 44 s(s+1)/(2pi)^2.
- The coefficients a_n are those of eta(2z)eta(22z), i.e. of theta_chi for the order-3 ring-class character of disc -44
  (THEOREM-A11).
- Step 9 local factors (Kani Cor. (4), p. 6, OPENED):
  - p = 2: factor 1 (degree 0);
  - p = 11: (1-u)^{-1};
  - split p: (1-u)^{-2} or (1+u)/(1-u^3);
  - inert p: (1-u^2)^{-1}.
- **Step 8 at p = 2 (degree-0 local factor):** Palojärvi–Zhao's Artin setup (arXiv:2508.03023 v2 §1.2, OPENED)
  assumes "L(s) has a polynomial Euler product of order r", "where |alpha_j(p)| <= p^theta for some theta < 1/2", and
  that "for each p there is a permutation (alpha'_j(p)) of (alpha_j(p)) such that |alpha_j(p) alpha'_j(p)| <= 1".
  The local factor 1 at p = 2 is the case alpha_1(2) = alpha_2(2) = 0. That satisfies |alpha_j(2)| <= 2^theta and the
  permutation condition (0 * 0 = 0 <= 1). The paper does not discuss zero alpha's explicitly, but its stated
  hypotheses admit them.
- Code: p11/tail_cert44.py and p11/tail_run44.py (BAR-A9). Tail start x = 2800 (eps = 1/5, t = 21/50,
  y in [0.374, 0.4]).
