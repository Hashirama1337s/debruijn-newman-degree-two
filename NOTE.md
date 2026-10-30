# Explicit de Bruijn–Newman bounds below 1/2 in degree 2, and a product lemma for Dedekind zeta functions

Moki & Julio (AI-assisted). Draft v2, 30 October 2026. Not refereed by a human expert.

> **Status words used in this note.**
> - **PROVED (AI-refereed):** a written proof whose computational steps are certified in interval or ball arithmetic
>   under pre-registered (sealed) pass/fail criteria, and whose chain was read by AI referee reviewers, with every fix
>   applied. No human expert has checked it.
> - **CONDITIONAL:** proved here from a stated input that is itself not refereed (for example a 2026 preprint).
> - **HEURISTIC:** numerical evidence only; nothing is claimed.

---

## In plain words

Every L-function carries a "heat dial" t. Turning the dial up smooths the function and pushes its zeros onto one line.
The smallest setting at which every zero already sits on the line is the de Bruijn–Newman constant Λ. The generalised
Riemann hypothesis for that L-function says Λ ≤ 0. It is known that Λ ≥ 0, and classical theory gives Λ ≤ 1/2 for free.

Numbers below 1/2 were known for the Riemann zeta function (Λ ≤ 0.2) and, since October 2026, for real Dirichlet
characters of small conductor (Λ ≤ 0.2978, in a preprint not yet refereed). Both are "degree 1".

This note does three things.

1. It proves Λ ≤ 0.449938 for one "degree 2" L-function, that of the modular form η(z)η(23z), and Λ ≤ 0.489938 for a
   second one, η(2z)η(22z). We found no earlier bound below 1/2 in degree 2.
2. It writes out a short product lemma: if two L-functions each have their zeros on the line at heat t, so does
   their product. So the constant of a product is at most the larger of the two constants. The lemma is an
   application of known results: a 1981 theorem of Lieb and Sokal from statistical physics, and a theorem of
   Borcea and Brändén on stable polynomials. We claim nothing new for it; we write it out because we need it for kernels
   that may change sign.
3. Because the Dedekind zeta function of a number field factors into simpler L-functions, the lemma turns known
   bounds into bounds for number fields: Λ ≤ 0.2978 for every quadratic field with discriminant between 3 and 400 in
   absolute value (this rests on an unrefereed 2026 preprint), and Λ ≤ 0.449938 for the cubic field of discriminant −23
   (this rests only on our own Theorem 1) and for its degree-6 Galois closure (this also rests on the 2026 preprint).

The gains over 1/2 are modest. Nothing here bears on the Riemann hypothesis itself. The point is that the method now
reaches degree 2 and number fields.

## Abstract

Let f = η(z)η(23z) (weight one, level 23), whose L-function is L(s, ψ) for the order-3 class-group character ψ of
Q(√−23). Following Dobner, define the heat-flow deformation H_t of its completed L-function and its de Bruijn–Newman
constant Λ_ψ ≥ 0. We prove Λ_ψ ≤ 0.449938, and Λ_χ ≤ 0.489938 for the L-function of η(2z)η(22z) (level 44). The proofs
combine an explicit right-tail lemma checked in interval arithmetic, a certified winding-number computation on the
remaining finite region, and two applications of de Bruijn's theorem (in the form of Dobner's Theorem 3). We then
record a product lemma, an application of Lieb–Sokal (1981) and Borcea–Brändén: Λ(FG) ≤ max(Λ_F, Λ_G) whenever F, G and
FG lie in Dobner's extended Selberg class and FG carries the gamma factor γ_F γ_G. It follows from the
heat-flow identity H_t^{FG}(z) = [exp(−2t ∂_x ∂_y)(H_t^F(x) H_t^G(y))]_{x=y=z} and Borcea–Brändén's characterisation
of real-stability preservers. Corollaries: Λ ≤ 953/3200 = 0.2978125 for the Dedekind zeta function of every quadratic
field with fundamental discriminant 3 ≤ |D| ≤ 400 and for multiquadratic fields built from them (conditional on
Freire et al., arXiv:2610.27343, unrefereed), and Λ ≤ 0.449938 for the cubic field of discriminant −23 and its sextic
Galois closure (the latter also conditional on Freire et al.). At our search floor these are the first explicit
de Bruijn–Newman bounds below 1/2 for a primitive degree-2 L-function and for Dedekind zeta functions of number fields other
than Q.

---

## 1. Setting: Dobner's class and the heat flow

**Dobner's extended Selberg class S♯** (arXiv:2005.05142, §2). For F in S♯ with completed function ξ^F (normalised to be
entire and to satisfy ξ^F(s) = conj ξ^F(1 − conj s)), put (Dobner eqs. (5), (6))

  Φ_F(u) = (1/2π) ∫ ξ^F((1+ix)/2) e^{−ixu} dx,   H_t^F(z) = ∫_R e^{tu²} Φ_F(u) e^{izu} du,

so that H_0^F(z) = ξ^F((1+iz)/2). The kernel Φ_F is conjugate-symmetric, Φ_F(u) = conj Φ_F(−u) (Dobner p. 9), and
decays doubly exponentially (Dobner p. 11).

- **Dobner Thm 1** (p. 3): there is a real Λ_F such that all zeros of H_t^F are real if and only if t ≥ Λ_F.
- **Dobner Thm 2:** Λ_F ≥ 0 for every F in S♯. 
- **Dobner Thm 3** (p. 9; de Bruijn 1950, Thm 13). Let φ be integrable, conjugate-symmetric and O(e^{−|u|^b}) for some
  b > 2, with transform G. If all zeros of G lie in |Im z| ≤ Δ, then all zeros of G_t lie in
  |Im z| ≤ (max(Δ² − 2t, 0))^{1/2}.

For F with an Euler product (S♯ itself does not require one; Dobner p. 7; every L-function in this note has one),
ξ^F(s) ≠ 0 for Re s > 1 and, by the functional equation, for Re s < 0, the zeros of H_0^F lie in
|Im z| ≤ 1, and Theorem 3 with Δ = 1, t = 1/2 gives the classical Λ_F ≤ 1/2.

**The two-step argument** (as in Dobner's proof of his Thm 1, p. 11). If for some t0 every zero of H_{t0} has
|Im z| < Δ0, then Theorem 3 applied to e^{t0 u²}Φ gives Λ ≤ t0 + Δ0²/2. All bounds below are of this form; the work is
to prove the zero-free statement at t0.

## 2. Theorem 1: two degree-2 bounds

**The forms.**
- f_23 = η(z)η(23z), the newform 23.1.b.a in the LMFDB. It is the theta series θ_ψ of the order-3 class-group
  character ψ of Q(√−23): binary theta series of discriminant D lie in M_1(|D|, ψ_D) (Hecke, Schoeneberg, as recorded
  in Kani's 2010 slides, p. 1); θ_ψ for a non-quadratic class-group character is a cuspidal Hecke newform (Kani, Thm 1
  and Thm 3(b)); and the LMFDB records that 23.1.b.a spans the one-dimensional newspace S_1^new(23, ψ_{−23}). So
  L(s, f_23) = L(s, ψ), with absolutely convergent Euler product and |a_n| ≤ d(n). It is the Artin L-function of the
  irreducible 2-dimensional representation of S_3 attached to the cubic field of discriminant −23.
  Completed function ξ(s) = (√23/2π)^s Γ(s) L(s) = ξ(1 − s), and Φ(u) = 2e^u f_23(ie^{2u}/√23), real and even.
- f_44 = η(2z)η(22z), the newform 44.1.d.a, the order-3 ring-class character χ of the order Z[√−11] (h(−44) = 3,
  primitive). Nebentypus = LMFDB character 44.21 = ψ_{−44}; Euler factors at 2 and 11 from Kani's Corollary (4):
  L_2 = 1, L_11 = (1 − 11^{−s})^{−1}. ξ(s) = (√44/2π)^s Γ(s) L(s).

Both satisfy Dobner's axioms with one Γ-factor, degree 2.

**Theorem 1 (PROVED, AI-refereed).**
- (a) For every t ≥ 19/50 + (374/1000)²/2 = 0.449938, all zeros of H_t for f_23 are real. Hence 0 ≤ Λ_ψ ≤ 0.449938.
- (b) For every t ≥ 21/50 + (374/1000)²/2 = 0.489938, all zeros of H_t for f_44 are real. Hence 0 ≤ Λ_χ ≤ 0.489938.

(An earlier run of the same pipeline gave 0.489938 for f_23 as well; (a) supersedes it.)

### 2.1 Proof of (a)

**Step 0 (symmetry).** On the ray τ = iy both square roots in the eta transformation are of positive reals, so
Φ(−u) = Φ(u). Hence H_t is entire, even and real on R: H_t(conj z) = conj H_t(z) and H_t(−conj z) = conj H_t(z).

**Step 1 (first use of de Bruijn).** The zeros of H_0 satisfy |Im z| ≤ 1. Theorem 3 with Δ = 1 and t = 0.38 places the
zeros of H_{0.38} in |Im z| ≤ √(1 − 0.76) = √6/5 = 0.4898979…

**Step 2 (right tail).** H_{0.38}(x + iy) ≠ 0 for x ≥ 12,500 and 0.374 ≤ y ≤ 0.49.
- *Method.* An exact Gaussian-average identity writes H_t(x + iy) = ∫ w(v) ξ(s_v) dv with a Gaussian weight w. The
  integral is split so that on both outer pieces ξ is an absolutely convergent Dirichlet series times its Γ-factor.
  The n = 1 term M is shown to dominate the three error terms, |M| > |E_A| + |E_B| + |E_M|. The error terms are bounded
  by published explicit estimates: the convexity bound of Palojärvi–Zhao (arXiv:2508.03023, v1 Lemma 3.2 = v2
  Lemma 3.3, via Rademacher's Phragmén–Lindelöf theorem), Stirling bounds (DLMF §5.11(ii)), and the trapezoid-rule
  bound of Trefethen–Weideman (SIAM Rev. 56 (2014), Thm 5.1). The coefficient sum B(σ) = Σ|a_n|n^{−σ} is bounded from
  the exact local factors of θ_ψ (exact product for p ≤ 2·10^6, a crude bound beyond, arguments rounded downward).
  Parameters: t = 19/50, ε = 1/5.
- *Interval check, 13,000 ≤ x ≤ 2·10^12* (16 y-subboxes): 202 interval boxes in outward-rounded interval arithmetic;
  the tightest normalised margin is 0.78, near x ≈ 13,398.
- *Interval check, 12,500 ≤ x ≤ 13,000* (32 y-subboxes): 8 boxes; tightest margin 0.83, near x ≈ 12,592.
- *x ≥ 2·10^12:* a monotonicity argument. Write q = √23/(2π) and T = x/2 (the height in s = (1 + iz)/2), and put
  L := (1/2)log(qT); at the start, T = 10^12, L = 13.68. The four vertices of the relevant
  exponent (1.35, 1.35, 2.49, 5.19) all lie below L = 13.68, so every error factor decreases from there on, and the error sum
  is at most 0.1698, against a main-term lower bound of at least 0.99999. The constant K0 = e^{0.38·0.79²} = 1.2676 comes
  from |Im α| ≤ 0.79 (computed value π/4 = 0.7854…), which does not involve t.
- *Cross-checks.* At x = 13,000 the certified lower bound is log|H| ≥ −10203.86 against a certified log|H| of
  −10201.22; at x = 12,500, −9811.62 against −9808.41.
- *Edges.* The tail's lower edge is the double 0.374 rounded down, and its top 0.49 exceeds √6/5 (0.49² = 0.2401 > 0.24).

**Step 3 (finite region).** H_{0.38} has no zeros in the closed rectangle [0, 12500] × [0.374, 0.50].
- *Method.* A certified winding number of H_{0.38} around the boundary. H_t is evaluated by the trapezoid rule in u
  with a rigorous quadrature bound, in ball arithmetic (MPFR/MPC midpoints, radii inflated per operation). Each step
  of the walk is certified by an order-12 Taylor bound plus a Cauchy cone condition |H(z) − H(p)| < |H(p)|, so the
  argument cannot jump by π or more between nodes.
- *Result.* Winding number 0 (certified enclosure of the winding number: 8.2·10^{−54} ± 4.8·10^{−4}), from 196,660 ball evaluations over 87 independent walks. A combiner checked that the bottom,
  top, right and left edges are each tiled exactly once by the declared walk segments; removing any one segment makes
  it fail.
- *Load.* At x ≳ 10,700 the dyadic quadrature step halves (2^{−13} to 2^{−14}), doubling the node count from 81,921 to
  163,841; the top edge was re-split into 75 pieces under a sealed amendment. Wall time 13.4 h on 9 cores.
- *Positive controls* (same evaluator and walker, identical code hashes):
  - [5, 15] × [−1/5, 1/5] at t = 19/50: certified winding 2.
  - [12496, 12500] × [−1/2, 1/2] at t = 19/50, in the 163,841-node regime: certified winding 5 (enclosure 5 ± 4.2·10^{−18}; 84 points), equal to the 5 real sign changes counted by an independent method sharing no code (a Gaussian
    average of the completed L-function in PARI/GP at 57 digits). A walk along the real axis through one of those
    zeros, in (12497.9, 12498.0), is refused by the walker ("cannot certify step"), as it must be.

**Step 4 (cover).** [0, 12500] × [0.374, 0.50] by Step 3; [12500, ∞) × [0.374, 0.49] by Step 2; y > √6/5 by Step 1
(the slab √6/5 < y ≤ 0.4899 lies inside both tops, since 0.4899² > 0.24); x < 0 and y < 0 by Step 0. So every zero of
H_{0.38} has |Im z| < 0.374.

**Step 5 (second use of de Bruijn).** Theorem 3 applied to e^{0.38u²}Φ with Δ = 0.374: all zeros of H_t are real for
t ≥ 0.38 + 0.374²/2 = 0.38 + 0.069938 = 0.449938. The lower bound is Dobner Thm 2. ∎

### 2.2 Proof of (b)

The same chain at t0 = 21/50, changing only the level (N = 44) and the Euler factors.
- Step 1 gives |Im z| ≤ 0.4 at t = 0.42.
- Step 2: H_{0.42}(x + iy) ≠ 0 for x ≥ 2,800 and 0.374 ≤ y ≤ 0.4; 221 interval boxes up to 2·10^12; error sum 0.0295 < 1
  beyond (the Palojärvi–Zhao hypothesis is checked for N = 44). The tail's top edge is the double 0.4, which exceeds
  2/5, so y = 0.4 itself is covered; y > 0.4 is Step 1.
- Step 3: certified winding 0 around [0, 2800] × [0.374, 0.41], 41,785 ball evaluations, about 0.64 h. Controls: winding 3
  on [5, 15] × [−0.2, 0.2]; high-x control [2696, 2700] × [−1/2, 1/2] gives winding 5, equal to an independent count.
- Step 5: t ≥ 0.42 + 0.374²/2 = 0.489938. ∎

### 2.3 Every assumption, stated
- Correct rounding of MPFR 4.2.2 / MPC 1.4.0; floating-point radii inflated per operation, with libm exp, expm1, asin,
  sqrt assumed within 1 ulp; mpmath 1.3.0 interval arithmetic (outward rounding) for the tail and the quadrature
  majorants.
- Literature inputs (all opened): de Bruijn's Thm 13 via Dobner Thm 3; Palojärvi–Zhao's convexity lemma; DLMF §5.11;
  Trefethen–Weideman Thm 5.1; Kani 2010; LMFDB 23.1.b.a and 44.1.d.a.
- PARI/GP serves only as an independent reference in controls, never as a certified step.
- Not assumed: GRH. The near region is certified directly; the tail uses only the Euler product in Re s > 1.

## 3. Lemma P: products

### 3.1 Statement

**Class D.** Φ: R → C measurable, not a.e. zero, with Φ(u) = conj Φ(−u) and |Φ(u)| ≤ C e^{−|u|^b} for some C > 0 and
b > 2. Put H_t^Φ(z) = ∫ e^{tu²}Φ(u)e^{izu} du, Z_Φ = {t : all zeros of H_t^Φ are real}, Λ(Φ) = inf Z_Φ. Dobner's kernels
Φ_F lie in D (Dobner pp. 9, 11). No positivity or evenness is assumed.

**Theorem P.** Let Φ, Ψ ∈ D with Z_Φ, Z_Ψ non-empty. Then Λ(Φ ∗ Ψ) ≤ max(Λ(Φ), Λ(Ψ), 0). More precisely, for every t ≥ 0
at which H_t^Φ and H_t^Ψ have only real zeros, H_t^{Φ∗Ψ} has only real zeros.

**Corollary P♯.** Let F, G ∈ S♯ with FG ∈ S♯, where FG carries the gamma factor γ_{FG} = γ_F γ_G. Then
Λ_{FG} ≤ max(Λ_F, Λ_G). (In §4 both requirements are checked separately: the gamma factors multiply by Legendre
duplication, and the pole order of FG at s = 1 is the sum of those of F and G because L(1, χ) ≠ 0 and L(1, f_23) ≠ 0.)
*Proof.* ξ^{FG} = c·ξ^F ξ^G with c a non-zero constant, so Φ_{FG} = c·Φ_F ∗ Φ_G by Fourier uniqueness. Z is non-empty by
Dobner Thm 1, and the 0 is redundant by Dobner Thm 2. Λ does not depend on the scaling of γ (Dobner p. 9). ∎

**Known result; no novelty claimed.** Theorem P is an application of two known theorems.
- *Lieb–Sokal (1981).* Their abstract states: "We show that any measure on R^n possessing the Lee-Yang property retains
  that property when multiplied by a ferromagnetic pair interaction." For nonnegative kernels φ, ψ this gives Theorem P
  directly: the measure φ(v)ψ(w) dv dw on R² has the Lee–Yang property exactly when H_t^Φ and H_t^Ψ have only real
  zeros (its Laplace transform factors, and real symmetric kernels give transforms that are real on R); the weight
  e^{2tvw} of §3.2 is a ferromagnetic pair interaction with coupling 2t ≥ 0; and setting the two fields equal gives the
  transform of the law of v + w, which is H_t^{Φ∗Ψ}. We read only the abstract (the full text was not reachable to us)
  and did not check their integrability hypotheses against our kernels.
- *Borcea–Brändén.* The proof written out below uses their characterisation of real-stability preservers instead, so
  that it covers conjugate-symmetric kernels that need not be nonnegative, which is the generality Dobner's class
  requires.

**Review.** One full AI referee read of the written proof found the identity, the stability step, the limit argument and
the diagonal step correct, with no gap; an independent AI reviewer checked the identity and the sign. That review is
recorded in the lab log only (no separate report file), and this section was revised after it to apply its fixes.

### 3.2 The identity
Fix t ≥ 0, put φ(v) = e^{tv²}Φ(v), ψ(w) = e^{tw²}Ψ(w), f = H_t^Φ, g = H_t^Ψ. For c ≥ 0 let

  (E_c F)(x, y) := ∬ e^{cvw} φ(v)ψ(w) e^{i(xv + yw)} dv dw,

which converges absolutely and locally uniformly on C² (the integrand is at most e^{c(v²+w²)/2}|φ(v)||ψ(w)|e^{|Im x||v| +
|Im y||w|}, and e^{cv²/2}φ ∈ D). Since (v + w)² = v² + w² + 2vw, Fubini gives

  H_t^{Φ∗Ψ}(z) = ∬ e^{t(v+w)²}Φ(v)Ψ(w)e^{iz(v+w)} dv dw = (E_{2t}(f ⊗ g))(z, z).

As ∂_x∂_y e^{i(xv+yw)} = −vw e^{i(xv+yw)}, multiplication by e^{cvw} is the Fourier form of exp(−c ∂_x∂_y): formally
H_t^{FG}(z) = [exp(−2t ∂_x∂_y)(f(x)g(y))]_{x=y=z}. The sign is minus, with c = 2t ≥ 0.

**Finite-order steps.** For a ≥ 0 let T_a = 1 − a∂_x∂_y. Differentiating under the integral,
(T_{c/N})^N(f ⊗ g)(x, y) = ∬ (1 + cvw/N)^N φ(v)ψ(w)e^{i(xv+yw)} dv dw. Since |(1 + cvw/N)^N| ≤ e^{c|v||w|} ≤ e^{c(v²+w²)/2},
dominated convergence gives (T_{c/N})^N(f ⊗ g) → E_c(f ⊗ g) uniformly on {|Im x|, |Im y| ≤ R}. The infinite-order
operator is never applied to polynomial approximants; only T_a is.

### 3.3 The stability step
Notation of Borcea–Brändén: a polynomial in n variables is *stable* if it does not vanish when all variables lie in the
open upper half-plane, *real stable* if moreover its coefficients are real; a univariate real polynomial is real stable
iff all its zeros are real.

**Lemma 2.** For a ≥ 0, T_a maps real stable polynomials in (x, y) to real stable polynomials or to 0.
*Proof.* Borcea–Brändén II (arXiv:0809.3087, Thm 7.3(b), p. 21): a finite-order operator T = Σ_α Q_α(z)∂^α preserves real
stability iff F(z, −w) = Σ_α Q_α(z)(−w)^α is real stable. Here F(z, −w) = 1 − a w_1w_2. If w_1, w_2 lie in the upper
half-plane then arg(w_1w_2) ∈ (0, 2π), so w_1w_2 is not a positive real and 1 − a w_1w_2 ≠ 0. (Equivalently, via the
transcendental symbol (1 − a w_1w_2)e^{−z·w} and Borcea–Brändén I, arXiv:0809.0401, Thm 1.3.) ∎
*Sign check.* exp(+c∂_x∂_y), c > 0, does not preserve stability: it maps xy to xy + c, which vanishes at x = y = i√c.

**Lemma 3.** Let C2 be the set of locally uniform limits on C² of real stable polynomials in two variables, together
with 0. C2 is closed under locally uniform limits, and:
- (a) F ∈ C2, a ≥ 0 ⇒ T_a F ∈ C2 (derivatives converge locally uniformly, by Cauchy's formula on polydiscs; Lemma 2);
- (b) F ∈ C2 ⇒ z ↦ F(z, z) is ≡ 0 or has only real zeros (diagonal substitution keeps stability, Borcea–Brändén I
  Lemma 1.7(4); Hurwitz's theorem, ibid. Thm 1.6, on the upper half-plane; conjugate symmetry for the lower one);
- (c) if f, g are locally uniform limits of real polynomials with only real zeros, then f ⊗ g ∈ C2.

**Lemma 1 (Laguerre–Pólya approximation).** A real entire function of order < 2, not ≡ 0, with only real zeros, is a
locally uniform limit of real polynomials with only real zeros. *Proof.* Hadamard: h(z) = κz^m e^{βz} Π_k(1 − z/z_k)e^{z/z_k}
with real z_k, real β and real κ (h is real on R). Then κz^m(1 + β_K z/N)^N Π_{k≤K}(1 − z/z_k), β_K = β + Σ_{k≤K}1/z_k,
converges to h as N → ∞ then K → ∞; take a diagonal sequence. ∎

**Facts used.** For t ∈ R, e^{tu²}Φ ∈ D (any b' ∈ (2, b)); H_t^Φ is entire, real on R, of order ≤ b'/(b'−1) < 2 and not
≡ 0; Z_Φ is closed and upward closed (Dobner p. 11, whose argument uses only class D). Class D is closed under
convolution, and H_0^{Φ∗Ψ} = H_0^Φ H_0^Ψ.

### 3.4 Proof of Theorem P
Let t ≥ max(Λ(Φ), Λ(Ψ), 0), so t ∈ Z_Φ ∩ Z_Ψ. By the facts and Lemmas 1 and 3(c), f ⊗ g ∈ C2. By Lemma 3(a) applied N
times with a = 2t/N, (T_{2t/N})^N(f ⊗ g) ∈ C2; by §3.2 and closedness, E_{2t}(f ⊗ g) ∈ C2. By Lemma 3(b) its diagonal,
which is H_t^{Φ∗Ψ}, is ≡ 0 or has only real zeros; it is not ≡ 0. So t ∈ Z_{Φ∗Ψ}. ∎

### 3.5 Scope and limits
- **The 0 cannot be dropped in general.** In the polynomial (Laguerre–Pólya) setting, where Λ can be negative: p = x − 1
  and q = x + 1 each have Λ = −∞, but e^{−tD²}(x² − 1) = x² − 1 − 2t has real zeros iff t ≥ −1/2. This example lives in
  the polynomial class, not in class D; for L-functions in S♯ the 0 is redundant because Λ ≥ 0.
- **Λ(FG) is not a function of Λ_F and Λ_G.** In the application check below, all 300 polynomial pairs had Λ(pq)
  strictly below the maximum.
- **Complex characters.** Non-real Dirichlet characters χ also give elements of S♯ (after normalising the root
  number), and Corollary P♯ applies to products involving them. But no explicit bound Λ < 1/2 is available for any
  complex χ, so no corollary below uses them (for example, no cyclotomic field beyond the quadratic ones).

### 3.6 Application check (numerical; not part of the proof)
Pre-registered test, exact rational arithmetic and Sturm counts in PARI/GP on one core:
- identity check (polynomial analogue of §3.2): 0 failures in 400 cases;
- T_c = exp(−c∂_x∂_y) on 400 real-rooted pairs, restricted to the diagonal: 0 violations; the opposite sign, as a null,
  produces non-real zeros in 374 of 400 cases;
- the lemma on 300 pairs of polynomials with non-real zeros, at t* = max(Λ_p, Λ_q, 0): 0 violations; the null without
  the 0 fails in 233 of 300;
- positive control: Λ(x² + 1) = 1/2 exactly.
- factorisations used in §4: ζ_K = ζ·L(s, f_23) for K = Q[x]/(x³ − x − 1) (coefficients equal for n ≤ 3000; the ratio of
  completed functions equals 1 to 38 digits at two test points); ζ_H = ζ·L(s, χ_{−23})·L(s, f_23)² for the sextic field
  H defined by x⁶ − 6x⁴ + 9x² + 23 (coefficients equal for n ≤ 2000).

## 4. Corollaries for Dedekind zeta functions

**Inputs.**
- Λ_ζ ≤ 0.2: Platt–Trudgian, arXiv:2004.09765, §3.4, Corollary 2 (opened). (Polymath15's Λ ≤ 0.22 would serve equally.)
- Λ_χ ≤ 953/3200 = 0.2978125 for every primitive real character χ of conductor 3 ≤ m ≤ 400: Freire, González-Riquelme,
  Muñoz, Poblete, Salinas, arXiv:2610.27343 (October 2026), Thm 1.1 with D = 1, as stated on p. 6. **Unrefereed preprint.**
- Λ ≤ 0.449938 for L(s, f_23): Theorem 1(a) of this note.
- Every Λ below is ≥ 0 (Dobner Thm 2).

**Normalisation.** Dobner, Freire et al. and §2 all use s = (1 + iz)/2 and the flow e^{tu²}; constant factors do not move
zeros. By Legendre duplication Γ_R(s)Γ_R(s+1) = Γ_C(s), so the Γ-factors multiply correctly, and ξ_{ζ_K} := s(s−1)Λ_K(s)
is a constant multiple of the product of the factors' completed functions. The pole orders add because L(1, χ) ≠ 0 and
L(1, f_23) ≠ 0.

| # | object | factorisation | bound | condition tag |
|---|---|---|---|---|
| C1 | ζ_K, K = Q(√D), fundamental D, 3 ≤ \|D\| ≤ 400 | ζ·L(s, χ_D), χ_D primitive real of conductor \|D\| | 0 ≤ Λ ≤ 953/3200 = 0.2978125 | CONDITIONAL on Freire et al. (preprint); Platt–Trudgian (published) |
| C2 | ζ_K, K multiquadratic, every quadratic subfield with 3 ≤ \|disc\| ≤ 400 (e.g. Q(√−3, √5)) | ζ·Π L(s, χ) over the non-trivial real characters of K (primitive; conductors = subfield discriminants) | Λ ≤ 0.2978125 | CONDITIONAL as C1; Theorem P iterated at kernel level |
| C3 | ζ_K, K = Q[x]/(x³ − x − 1), d_K = −23 (non-Galois cubic field; S_3 closure) | ζ·L(s, f_23) | Λ ≤ 0.449938 | Theorem 1(a) + Platt–Trudgian |
| C4 | ζ_H, H the Hilbert class field of Q(√−23) (sextic, S_3-Galois closure of C3, disc −23³) | ζ·L(s, χ_{−23})·L(s, f_23)² | Λ ≤ 0.449938 | Theorem 1(a) + Platt–Trudgian + CONDITIONAL on Freire et al. (m = 23) |

**On C2.** The partial products ζ·L(χ_1)···L(χ_j) are handled at the kernel level: each partial convolution lies in
class D, and Theorem P applied repeatedly gives a finite Λ at each stage, so Z is non-empty for the next step. The
abelian factorisation is classical (conductor–discriminant formula); unlike C3 and C4 it was not re-checked numerically.

**On C3 and C4.** C3 is, at our search floor, the first explicit de Bruijn–Newman bound below 1/2 for the Dedekind zeta
function of a non-abelian (non-Galois) number field. The square L(s, f_23)² in C4 is harmless: Theorem P allows F = G.

Every improvement of the inputs propagates directly. Freire et al. give stronger per-character bounds in an appendix,
which we did not use.

## 5. Outlook: a degree-2 effective formula (HEURISTIC; nothing claimed)

Freire et al. reach 0.2978 in degree 1 with the Polymath15 architecture, whose core is an effective Riemann–Siegel-type
approximation of H_t. No citable effective analogue for degree 2 was found. Two exploratory, pre-registered numerical
tests are consistent with this route working:
- A degree-2 transcription of their main term tracks the certified H_t of f_23 to a maximum relative error 1.9·10^{−4} at
  x ≈ 10,450 (t = 1/4), with error decreasing like 1/M in the number of terms (fitted slope −0.98).
- A crude bound on the awkward middle range of the sum (absolute values, no cancellation, in a window of width about
  2K√M around the cutoff) is at most E = 0.031 at x ≈ 10,450, t = 1/4, below the bar of 0.05 that we sealed before the
  run (set below the error maxima e_{C,0} that Freire et al. list in their Table 3, p. 75); it sits above the measured error at all 54 test points. Without heat flow (t = 0) the same quantity is
  1.5–2.3, and at t = 1/10 it is 0.41: the heat flow is what makes a crude route plausible.

These numbers do not bound anything: the window lemma that would turn E into an error bound is unproved. If it holds,
the numbers are consistent with Λ near 0.3 at level 23; we make no forecast. Via Theorem P any improvement would
propagate to C3 and C4.

## 6. Prior art and search floor

- **Degree 1, explicit bounds:** Polymath15 (arXiv:1904.12438, Thm 1.1: Λ ≤ 0.22); Platt–Trudgian (arXiv:2004.09765,
  Cor. 2: Λ ≤ 0.2); Freire, González-Riquelme, Muñoz, Poblete, Salinas (arXiv:2610.27343: Λ_L ≤ 0.2978125 for primitive
  real characters of conductor 3 to 400). The latter describe theirs (§1.4) as "the first non-trivial upper bounds for a
  Dirichlet L-function"; they are degree 1, and the present degree-2 bounds are far weaker than theirs.
- **Existence and lower bounds:** Dobner (arXiv:2005.05142: existence and Λ ≥ 0 on S♯; no bound below 1/2 in degree 2);
  Stopple (arXiv:1301.3158, abstract only: a lower bound −1.13·10^{−7} < Λ_Kr for the family of quadratic Dirichlet
  L-functions); Andrade–Chang–Miller (arXiv:1310.3477: existence for
  holomorphic newforms with even functional equation; no numerical upper bound).
- **Certified zeros.** The LMFDB and Booker (Exp. Math. 15 (2006)) provide rigorous zero computations for many
  L-functions. Our proofs do not use them.
- **Product mechanism.** Borcea–Brändén I and II (stability preservers, the Lieb–Sokal operation); Craven–Csordas (1994,
  e^{−tD²} on the Laguerre–Pólya class, one variable); Newman (1976) and de Bruijn (1950, Thm 28: products of kernels,
  a different operation from ours). Lieb–Sokal (1981; abstract only) proves that ferromagnetic pair interactions preserve the Lee–Yang
  property, which for nonnegative kernels gives Theorem P (§3.1).
- **Search floor (30 October 2026).** arXiv full-text listing for "de Bruijn–Newman" (about 20 papers); all 151 Zenodo records
  matching "Bruijn-Newman" (scanned) and the 36 matching "Bruijn-Newman AND product"; the
  full texts listed above; web searches. At this floor we found no explicit bound below 1/2 for any degree-2 L-function,
  and no explicit bound below 1/2 for the Dedekind zeta function of any number field other than Q. Theorem P is known
  (§3.1) and carries no novelty claim. A search floor is not a clearance.

## 7. Methods and verification protocol

- **Sealed predictions.** Every computational step was pre-registered: the prediction and its pass/fail bar were written
  and hashed (SHA-256) before the run, then scored without moving the bar. Failures were kept on record: a first tail
  run failed on a code gap and was re-run under a sealed amendment; a sealed wall-time prediction for the finite region
  was missed (it ran faster after a sealed re-balance); one exploratory run in §5 lost its output to a writer bug and was
  re-run under a sealed amendment.
- **Referees (exact depth).** All reviewers are AI reviewers; **none is a human expert.**
  - Theorem 1(a): one full review with independent re-implementation (it re-audited all 87 walks, spot-checked the
    evaluator against an independent PARI/GP value to ≤ 4·10^{−14}, and re-derived the coverage), plus one second read
    of the logic only (the reduction to de Bruijn's theorem, the region cover and the novelty statement); that second
    read did **not** check the tail lemma or the evaluator. The two release blockers raised (a high-x positive control;
    tail parameters restated for t = 19/50) were resolved before this draft. Earlier single reviews covered the
    finite-region method and the tail lemma at the first parameter set (t = 21/50).
  - Items with a single full review only: the tail lemma and the evaluator of Theorem 1(a); Theorem 1(b) (one review
    of a pipeline shared with (a)); Theorem P (one full review, plus an independent check of the identity and sign
    only; that review is recorded in the lab log, not as a separate report).
  - The note itself (v1) had one hostile review; this v2 applies all of its blocking and recommended fixes.
- **Independent checks.** Positive controls at low and high height with independently counted zeros; negative tests
  of the coverage combiner; exact-arithmetic application checks for Theorem P.
- **Supplementary material.** Code, sealed predictions with hashes, run outputs and referee reports are in the
  accompanying bundle: bundle/README.md (layout and commands), bundle/STATUS.md (status of every claim),
  bundle/REDACTIONS.md (every change made to lab files for publication) and bundle/CLEANROOM.md (a rebuild in a fresh
  folder: all 15 checks matched). The clean-room rebuild did **not** re-run the 87 finite-region walks of Theorem 1(a)
  (about 120 CPU-hours); they are shipped as stored outputs, which the rebuild re-combined and re-checked for coverage,
  including the negative test. The tail interval runs, the Theorem 1(b) runs and the outlook runs were also not re-run.

## References (opened unless marked)
- J. Borcea, P. Brändén, The Lee–Yang and Pólya–Schur programs. I. Linear operators preserving stability, Invent. Math.
  177 (2009) 541–569, arXiv:0809.0401: Thm 1.3, Thm 1.6, Lemma 1.7(4).
- J. Borcea, P. Brändén, The Lee–Yang and Pólya–Schur programs. II. Theory of stable polynomials and applications,
  Comm. Pure Appl. Math. 62 (2009) 1595–1631, arXiv:0809.3087: §6, Thm 7.2, Thm 7.3, §8.1 Thm 8.3.
- A. R. Booker, Artin's conjecture, Turing's method and the Riemann hypothesis, Exp. Math. 15 (2006) 385–407, arXiv:math/0507502.
- T. Craven, G. Csordas, Differential operators of infinite order and the distribution of zeros of entire functions,
  J. Math. Anal. Appl. 186 (1994) 799–820, doi:10.1006/jmaa.1994.1334: Thm 3.10.
- A. Dobner, A proof of Newman's conjecture for the extended Selberg class, Acta Arith. 201 (2021) 29–62,
  arXiv:2005.05142: eqs. (5)–(6), §2, Thms 1–3, proof of Thm 1 (p. 11).
- Freire, González-Riquelme, Muñoz, Poblete, Salinas, Upper bounds on the de Bruijn–Newman constant for Dirichlet
  L-functions with primitive real-valued characters, arXiv:2610.27343 v1 (19 Oct 2026; preprint, unrefereed): Thm 1.1,
  p. 6, §1.4, §7, Table 3 (p. 75).
- E. Kani, Binary theta series and CM modular forms, Maine–Québec Number Theory Conference slides (2010),
  https://maine-quebec.mat.ulaval.ca/10/Kani.pdf: pp. 1, 3, 5 (Thms 1, 3(b)), 6 (Cor. (4)).
- LMFDB: newforms 23.1.b.a and 44.1.d.a; Dirichlet character 44.21.
- C. M. Newman, Fourier transforms with only real zeros, Proc. AMS 61 (1976) 245–251, doi:10.1090/S0002-9939-1976-0434982-5.
- Palojärvi, Zhao, On Turing's method for a general set of L-functions and the Selberg class, arXiv:2508.03023: v1 Lemma 3.2 (= v2 Lemma 3.3).
- D. Platt, T. Trudgian, The Riemann hypothesis is true up to 3·10^12, arXiv:2004.09765: §3.4, Corollary 2.
- Polymath15 (D.H.J. Polymath), arXiv:1904.12438: Thm 1.1.
- NIST DLMF §5.11(ii). L. N. Trefethen, J. A. C. Weideman, SIAM Rev. 56 (2014), doi:10.1137/130932132: Thm 5.1.
- Andrade, Chang, Miller, arXiv:1310.3477, §2.4.
- Abstract only: E. H. Lieb, A. D. Sokal, A general Lee–Yang theorem for one-component and multicomponent
  ferromagnets, Comm. Math. Phys. 80 (1981) 153–179, doi:10.1007/BF01213009 (abstract; Prop. 2.2 also via
  Borcea–Brändén II §6). B. Stopple, Notes on low discriminants and the generalized Newman conjecture, arXiv:1301.3158.
- Context only, not opened: N. G. de Bruijn, Duke Math. J. 17 (1950) (via Dobner and Newman).
