# PROOF-P — Lambda(FG) <= max(Lambda(F), Lambda(G), 0)

**Status: PROOF DRAFT (proof seat, 2026-10-30). Not refereed.** Labels: QUOTED (opened source, locator given),
CLASSICAL (textbook fact, not re-opened here), DERIVED-HERE (this file's argument). Prior-art gates (referee 2,
Z3/referee2-lemmaP.md; local scout, LOG 01:56) found the product statement OPEN at their search floor. This seat ran
one more web search for a Craven–Csordas "Leibniz rule for e^{-tD^2}" and found nothing. That search proves nothing
either way, and Craven–Csordas was not opened. No novelty is claimed here.

## In plain words
- Heat flow does not split over a product. But it can be written as "flow each factor, then apply one extra
  two-variable operator, then set the two variables equal".
- That extra operator is exp(-2t d_x d_y). With this sign it is one of the operators Borcea and Brändén proved keep
  "all zeros real" intact. With the opposite sign it destroys that property: x·y becomes x·y + c, which has zeros at
  x = y = i·sqrt(c).
- So whenever both factors have only real zeros at time t >= 0, so does the product. Hence the product's constant is
  at most the larger of the two, or at most 0 if both are negative.
- Free consequences:
  - Dedekind zeta functions of quadratic fields with |D| <= 400 get Lambda <= 0.2978.
  - The cubic field of discriminant -23 and its sextic Galois closure get Lambda <= 0.449938.
  - The quadratic case rests on the 2026 preprint of Freire et al.; the cubic case on our own unpublished A45.

## 0. Setting and hypotheses
**Class D.** Phi: R -> C is measurable and not a.e. zero, with:
- Phi(u) = conj(Phi(-u)) (conjugate symmetry);
- |Phi(u)| <= C e^{-|u|^b} for some C > 0 and some b > 2.

For t in R put
  H_t^Phi(z) := int_R e^{t u^2} Phi(u) e^{i z u} du,   Z_Phi := {t in R : all zeros of H_t^Phi are real},
  Lambda(Phi) := inf Z_Phi in [-inf, +inf]   (+inf if Z_Phi is empty).

**Why this is Dobner's class.** QUOTED, Dobner arXiv:2005.05142v2 (file Z3/refs/2005.05142.pdf):
- Theorem 3, p. 9 (de Bruijn [9, Thm. 13]) assumes: "ϕ: R → C be an integrable function satisfying ϕ(u) = \overline{ϕ(−u)}
  and ϕ(u) = O(e^{−|u|^b}) for some b > 2". Its conclusion: "If all the roots of G lie in the strip |Im z| ≤ ∆, then all
  the roots of G_t lie in the strip |Im z| ≤ (max(∆^2 − 2t, 0))^{1/2}".
- (5)-(6), p. 8 define Φ_F(u) = (1/2π) ∫ ξ^F((1+ix)/2) e^{−ixu} dx and ξ^F_t((1+iz)/2) := ∫ e^{tu^2} Φ_F(u) e^{izu} du.
- p. 9: "ΦF has the conjugate symmetry property ΦF(u) = \overline{ΦF(−u)}".
- p. 11: Φ_F(u) ≪ e^{−e^{2δu}/(3Q^δ)}, which gives class D with any b.
- p. 11 also shows that Z is closed (Hurwitz) and that t0 ∈ Z implies t ∈ Z for all t ≥ t0 (Theorem 3 with
  ϕ := e^{t0 u^2} Φ_F). The overlines are confirmed from the rendered page (refs/crop8.png).

So H^F_t of Dobner is H_t^{Phi_F}, and Lambda_F = Lambda(Phi_F).

We do NOT assume Phi >= 0 or Phi even (Dobner's Phi_F is only conjugate-symmetric).

**Fact F1** (Dobner p. 11, QUOTED argument; it uses only class D). Z_Phi is closed and upward closed. So Z_Phi is
empty, all of R, or [Lambda, inf) with Lambda in Z_Phi.
- e^{t u^2}Phi is again in class D for every real t, with any b' in (2, b): t u^2 - |u|^b <= -|u|^{b'} + const.

**Fact F2** (DERIVED-HERE). For each t, H_t := H_t^Phi is entire and satisfies H_t(conj z) = conj H_t(z), so it is a
*real* entire function. Its order is <= beta := b'/(b'-1) < 2.
- *Proof of reality.* conj H_t(x) = int e^{tu^2} conj(Phi(u)) e^{-ixu} du = int e^{tu^2} Phi(-u) e^{-ixu} du = H_t(x)
  for real x.
- *Proof of the order.* With |e^{tu^2}Phi(u)| <= C' e^{-|u|^{b'}}:
  |H_t(x+iy)| <= C' int e^{|y||u| - |u|^{b'}} du <= C' (int e^{-|u|^{b'}/2} du) · sup_u e^{|y|u - u^{b'}/2} = A e^{c|y|^beta},
  and |y| <= |z|. Also H_t is not identically 0 (Fourier uniqueness in L^1, since e^{tu^2}Phi is not a.e. 0). ∎

**Products.** For Phi, Psi in D, Phi*Psi (convolution) is in D:
- conjugate symmetry is inherited;
- |v|^b + |u-v|^b >= 2^{1-b}|u|^b (convexity) gives |Phi*Psi(u)| <= C'' e^{-2^{-b}|u|^b} <= C''' e^{-|u|^{b''}} for any
  b'' in (2, b);
- the Fourier transform H_0^Phi · H_0^Psi is not identically 0, so Phi*Psi is not a.e. 0.

By Fubini, H_0^{Phi*Psi} = H_0^Phi · H_0^Psi.

## 1. The identity (DERIVED-HERE; numerically checked, item I)
Fix t >= 0 and put phi(v) = e^{tv^2}Phi(v), psi(w) = e^{tw^2}Psi(w), f = H_t^Phi, g = H_t^Psi, F(x,y) := f(x)g(y).
For c >= 0 define
  (E_c F)(x,y) := ∫∫ e^{c v w} phi(v) psi(w) e^{i(xv + yw)} dv dw.
This converges absolutely and locally uniformly on C^2. The integrand is bounded by
  e^{c(v^2+w^2)/2}|phi(v)||psi(w)|e^{|Im x||v| + |Im y||w|},
and e^{cv^2/2}phi is in D.

**Identity.** Then
  H_t^{Phi*Psi}(z) = ∫ e^{tu^2} ∫ Phi(v)Psi(u-v) dv e^{izu} du = ∫∫ e^{t(v+w)^2} Phi(v)Psi(w) e^{iz(v+w)} dv dw
                   = (E_{2t} F)(z, z).
The first step is Fubini, with absolute convergence as above. The second uses (v+w)^2 = v^2 + w^2 + 2vw.

**Sign bookkeeping.** d_x d_y e^{i(xv+yw)} = (iv)(iw) e^{i(xv+yw)} = -vw e^{i(xv+yw)}. So multiplying by e^{cvw}
is the Fourier form of exp(-c d_x d_y). Formally, H_t^{FG}(z) = [exp(-2t d_x d_y)(f_t(x) g_t(y))]_{x=y=z}, as in the
brief. The operator that appears has the minus sign, with c = 2t >= 0.

**Finite-order steps.** For a >= 0 let T_a := 1 - a d_x d_y. Differentiation under the integral is justified by the
same domination, since polynomial factors in v, w are absorbed. It gives
  (T_{c/N})^N F (x,y) = ∫∫ (1 + c v w/N)^N phi(v)psi(w) e^{i(xv+yw)} dv dw.

**Limit.** As N -> inf, (T_{c/N})^N F -> E_c F uniformly on every set {|Im x|, |Im y| <= R}, so locally uniformly
on C^2.
- Use |(1 + cvw/N)^N| <= (1 + c|vw|/N)^N <= e^{c|v||w|} <= e^{c(v^2+w^2)/2}.
- The convergence is pointwise.
- So sup over the set of |difference| <= ∫∫ |(1+cvw/N)^N - e^{cvw}| e^{R(|v|+|w|)}|phi(v)psi(w)| dv dw, which tends to 0
  by dominated convergence. ∎

This is how the infinite-order operator is handled. It is never applied to polynomial approximants. Only the
finite-order T_a is, and the passage N -> inf is done on the integral representation.

## 2. The stability step (QUOTED theorem + DERIVED-HERE application)
Source: Borcea–Brändén, "The Lee-Yang and Pólya-Schur programs. I. Linear operators preserving stability",
arXiv:0809.0401v3 (Invent. Math. 177 (2009) 541–569), file Z3/refs/0809.0401.pdf.

QUOTED:
- **Definitions (p. 2–4).**
  - "f ∈ C[z1,...,zn] is Ω-stable if f(z1,...,zn) ≠ 0 whenever (z1,...,zn) ∈ Ω".
  - T "is said to preserve Ω-stability if for any Ω-stable polynomial f ∈ V the polynomial T(f) is either Ω-stable or
    T(f) ≡ 0".
  - Stable means Ω = {Im z > 0}^n (p. 3–4).
  - "A stable polynomial with all real coefficients is called real stable".
  - "a univariate real polynomial is stable if and only if all its zeros are real".
- **Transcendental symbol and Laguerre–Pólya class (p. 5).**
  - "G_T(z,w) = Σ_α (−1)^α T(z^α) w^α/α! ... we write G_T(z,w) = T[e^{−z·w}]".
  - "the complex Laguerre-Pólya class \overline{H_n}(C) as the class of entire functions in n variables that are
    limits, uniformly on compact sets, of polynomials in H_n(C)".
- **Theorem 1.3 (p. 5).** "Let T : C[z1,...,zn] → C[z1,...,zn] be a linear operator. Then T preserves stability if and
  only if either (a) T has range of dimension at most one ..., or (b) G_T(z,w) ∈ \overline{H_{2n}}(C)."
- **Theorem 1.6 (Hurwitz, p. 6).** "Let D be a domain ... in C^n and suppose {f_k} is a sequence of non-vanishing analytic
  functions on D that converge to f uniformly on compact subsets of D. Then f is either non-vanishing on D or else
  identically zero."
- **Lemma 1.7 (4) (p. 6).** f ∈ H_n(K) ⇒ "f(z1,...,z_{i−1}, z_j, z_{i+1},...,z_n) ∈ H_{n−1}(K)" (diagonal substitution).

**Lemma 2 (DERIVED-HERE from Thm 1.3).** For a >= 0, T_a = 1 - a d_x d_y preserves stability on C[x,y]. Since it maps
R[x,y] to R[x,y], it sends every real stable polynomial to a real stable polynomial or to 0.
- *Proof.* G_{T_a}(z,w) = T_a[e^{-z1w1-z2w2}] = (1 - a w1 w2) e^{-z1w1-z2w2}. This is the locally uniform limit of
  P_N := (1 - a w1w2)(1 - z1w1/N)^N (1 - z2w2/N)^N.
- Each P_N is stable. If u, v lie in the upper half-plane then arg(uv) ∈ (0, 2π), so uv is not in [0, inf) and
  1 - λuv ≠ 0 for λ >= 0. A product of non-vanishing factors does not vanish.
- So G_{T_a} ∈ \overline{H_4}(C), and Theorem 1.3(b) applies. ∎
- The same argument with (1 - c w1w2/N)^N shows that exp(-c d_x d_y), c >= 0, preserves stability on polynomials.
  This is the lead's form: symbol e^{-c w1w2 - z·w}.

**Sign check (DERIVED-HERE).** For c > 0, exp(+c d_x d_y) does NOT preserve stability:
- it maps the stable polynomial xy to xy + c, which vanishes at x = y = i sqrt(c);
- on the diagonal this is z^2 + c, which has non-real zeros.

So the identity of §1 produces the stability-preserving sign exactly when t >= 0. For t < 0, Lemma P fails without
the 0. Example: p = x - 1, q = x + 1 (Lambda = -inf each); e^{-tD^2}(x^2 - 1) = x^2 - 1 - 2t is real-rooted iff
t >= -1/2. The null NL below confirms this on 300 pairs.

**Lemma 3 (DERIVED-HERE).** Let C2 be the set of entire functions on C^2 that are locally uniform limits of polynomials
in H_2(R) ∪ {0}. C2 is closed under locally uniform limits (diagonal argument, metric of uniform convergence on an
exhaustion by compacts).
- (a) F ∈ C2 and a >= 0 imply T_a F ∈ C2. If P_n -> F locally uniformly, then by the Cauchy integral formula on
  polydiscs all partial derivatives converge locally uniformly (CLASSICAL). So T_a P_n -> T_a F, and
  T_a P_n ∈ H_2(R) ∪ {0} by Lemma 2.
- (b) F ∈ C2 implies that z -> F(z,z) is identically 0 or has only real zeros.
  - P_n(z,z) does not vanish for Im z > 0 (Lemma 1.7(4)), unless P_n ≡ 0.
  - Hurwitz (Thm 1.6, n = 1, D = upper half-plane) then shows the limit is either non-vanishing on Im z > 0 or ≡ 0.
  - P_n(conj z, conj z) = conj P_n(z,z) passes to the limit, which excludes Im z < 0 as well.
- (c) If f and g are locally uniform limits of real polynomials p_n, q_n with only real zeros, then
  f(x)g(y) ∈ C2: p_n(x)q_n(y) has no zero when Im x, Im y > 0.

**Lemma 1 (Laguerre–Pólya approximation; DERIVED-HERE from CLASSICAL Hadamard).** A real entire function h of order
< 2, not ≡ 0, with only real zeros, is a locally uniform limit of real polynomials with only real zeros.
- *Proof.* Hadamard factorization (CLASSICAL; e.g. Ahlfors, Complex Analysis, ch. 5 §3.2; not re-opened):
  - Order < 2 gives h(z) = z^m e^{βz+γ} Π_k (1 - z/z_k) e^{z/z_k}, with Σ|z_k|^{-2} < inf. If Σ|z_k|^{-1} < inf, the
    genus-0 product is rewritten in this form by absorbing e^{-zΣ1/z_k}.
  - The z_k are real, so the product is real on R. Then e^{βx+γ} is real for real x, so Im(βx+γ) is constant mod π,
    β is real and e^γ =: κ is real.
- Put β_K := β + Σ_{k<=K} 1/z_k and p_{K,N}(z) := κ z^m (1 + β_K z/N)^N Π_{k<=K}(1 - z/z_k). These are real polynomials
  with only real zeros.
- p_{K,N} -> κ z^m e^{β_K z} Π_{k<=K}(1-z/z_k) as N -> inf, and this tends to h as K -> inf. Both limits are locally
  uniform: the canonical product converges locally uniformly (CLASSICAL). A diagonal sequence finishes the proof. ∎

## 3. Theorem P and its proof
**Theorem P (PROOF DRAFT).** Let Phi, Psi ∈ D with Z_Phi, Z_Psi non-empty. Then
  Lambda(Phi * Psi) <= max(Lambda(Phi), Lambda(Psi), 0).
More precisely: for every t >= 0 such that H_t^Phi and H_t^Psi have only real zeros, H_t^{Phi*Psi} has only real
zeros.

*Proof.*
1. Let t >= max(Lambda(Phi), Lambda(Psi), 0). By F1, t ∈ Z_Phi ∩ Z_Psi.
2. f = H_t^Phi and g = H_t^Psi are real entire, of order < 2, not ≡ 0, with only real zeros (F2). By Lemma 1 and
   Lemma 3(c), F = f ⊗ g ∈ C2.
3. By Lemma 3(a), applied N times with a = 2t/N >= 0, (T_{2t/N})^N F ∈ C2.
4. By §1 (limit) and the closedness of C2, E_{2t}F ∈ C2.
5. By Lemma 3(b), z -> (E_{2t}F)(z,z) = H_t^{Phi*Psi}(z) (§1 identity) is ≡ 0 or has only real zeros. It is not ≡ 0
   (F2 applied to Phi*Psi ∈ D). So t ∈ Z_{Phi*Psi}. ∎

**Corollary P♯** (Dobner's extended Selberg class). Suppose F, G ∈ S♯ and FG ∈ S♯ with the admissible
gamma_{FG} = gamma_F·gamma_G. This holds when the pole orders at s = 1 add, which is true in every case below.
- Then xi^{FG} = xi^F·xi^G, so Phi_{FG} = Phi_F * Phi_G. Dobner (5) has no extra constant, and Fourier uniqueness
  applies.
- Dobner Thm 1 (p. 3, QUOTED: "there is a real number ΛF such that all the zeros of ξF_t lie on the critical line if and
  only if t ≥ ΛF") makes Z non-empty.
- Dobner Thm 2 ("ΛF ≥ 0 for every F ∈ S♯") makes the 0 redundant.

Hence **Lambda_{FG} <= max(Lambda_F, Lambda_G)**. Λ does not depend on the scaling of gamma (Dobner p. 9: gamma is
unique up to scaling).

**What is NOT claimed.**
- Lambda(FG) is not a function of Lambda(F) and Lambda(G). Item L below: 300/300 polynomial pairs were strictly
  smaller.
- No statement for complex (non-self-dual) L-functions such as L(s, χ) with complex χ. These are not in this
  conjugate-symmetric setting on their own.

## 4. Numerical support — BAR-Z3-P (sealed 19f456fe…, LOG 01:57), scored
Run: WSL PARI 2.17.3, 1 core (nbthreads 1 printed), exact rational arithmetic and Sturm counts. Output
lp/z3p_out.txt (sha256 0829c8142ea22362e7a99c771e5559c45a8dd497ebbe34589c4cf34bb960ec0f), exit 0.

| item | bar | result |
|---|---|---|
| PC | 4 controls true | **HOLDS**: Lambda(x^2+1) = 1/2 exactly, bracket [16383/32768, 1/2]; D_1(x,x) = x^2-1 real, D_{-1}(x,x) = x^2+1 not |
| I identity | 0/400 failures | **HOLDS**: 0/400, t in {-1/3, 1/2, 2, 7/5} |
| K key step, sign - (new content) | 0/400 violations | **HOLDS**: 0/400 |
| K-null, sign + | >= 30% violations | **FIRES**: 374/400 = 93.5% |
| L Lemma P on polynomials (new content) | 0/300 violations at t* = max(Lp, Lq, 0) | **HOLDS**: 0/300; 300/300 strictly smaller than the max (> 1e-3); gap min 0.0050, median 0.696 |
| NL null (drop the 0) | >= 50% violations | **FIRES**: 233/300 = 77.7% |
| F1 | zeta_K = zeta * L(f), n <= 3000 | **HOLDS** (exact coefficients) |
| F2 | reported | lfunparams: zeta_K [23,1,[0,0,1]], zeta [1,1,[0]], eta(z)eta(23z) [23,1,[0,1]] |
| F3 | ratio 1 to 1e-25 | **HOLDS**: Lambda_K/(Lambda_zeta·Lambda_f) = 1.000… (38 digits) at 0.3+5i and 2+i |
| F4 | zeta_H = zeta·L(χ_-23)·L(f)^2, n <= 2000 | **HOLDS**; H = x^6 - 6x^4 + 9x^2 + 23, disc -12167 = -23^3 |

**Instrument note.** gp rejected the script's own definition of `derivn` because it is a PARI 2.17 built-in ("variable
name expected"), and the built-in derivn(f,n) (n-th derivative) was used throughout. Its semantics match:
- checked separately: derivn(x^3,2) = 6x, derivn(x^3,0) = x^3;
- PC3 explicit polynomial equalities and the 400 identity checks pass.

The numbers support the sign and Lemma P. They are not proof.

## 5. Corollaries (normalisations matched)
**Normalisation.** All three sources use the same variable s = (1+iz)/2 and the same flow e^{tu^2}:
- Dobner (5)–(6), above;
- FGMPS arXiv:2610.27343, p. 1: "ΦL(u) := (1/2π) ∫ ξL((1+is)/2) e^{−isu} ds", H^L_t(z) := ∫ e^{tu^2} ΦL(u) e^{izu} du; and
  p. 3: "Hζ_0(z) := (1/8) ξ((1+iz)/2)";
- A45: THEOREM-A45-v2 "H_t(z) = int e^{tu^2} Phi(u) e^{izu} du (Dobner eqs. (5), (6))", with
  xi(s) = (sqrt23/(2pi))^s Gamma(s) L(s,f).

Constant factors do not move zeros.

**Completed functions** (PARI conventions, F2/F3; Γ_R(s) = π^{-s/2}Γ(s/2)). By Legendre duplication,
Γ_R(s)Γ_R(s+1) = 2(2π)^{-s}Γ(s) = Γ_C(s).
- Λ_f(s) = 23^{s/2}Γ_R(s)Γ_R(s+1)L(s,f) = 2·xi_A45(s).
- Λ_K(s) = 23^{s/2}Γ_R(s)^2Γ_R(s+1)ζ_K(s) = Λ_ζ(s)Λ_f(s).
- Dobner-admissible: xi_{ζ_K}(s) := s(s-1)Λ_K(s) = 4·xi_ζ(s)·xi_A45(s), with xi_ζ = ½s(s-1)π^{-s/2}Γ(s/2)ζ(s).
- The pole orders add: ζ has a simple pole and L(1,f) ≠ 0, because ζ_K = ζ·L(f) has a simple pole (CLASSICAL).

Conductor 23 = |d_K| (F2). Gamma: ζ contributes [0], f contributes [0,1], ζ_K has [0,0,1] (F2).

**Inputs.**
- Λ_ζ <= 0.2: Platt–Trudgian, as reported by FGMPS p. 4: "Platt and Trudgian [27] subsequently improved this bound to
  Λζ ≤ 0.2". The primary source was NOT opened; Polymath's 0.22 (same page) would serve equally below.
- Λ_χ <= 953/3200: FGMPS Thm 1.1 and p. 6, "For D = 1, the computations in Section 7 give the uniform bound ΛL ≤
  953/3200 = 0.2978125 < 1/2 for 3 ≤ m ≤ 400", for every primitive real character of conductor 3 ≤ m ≤ 400. This is a
  2026 preprint, not refereed.
- Λ_f <= 0.449938 for f = eta(z)eta(23z): our THEOREM-A45-v2 (AI-refereed, 2 seats; unpublished).
- Lower bounds: every Λ below is >= 0 (Dobner Thm 2).

| # | object | factorisation (CLASSICAL Artin/Hecke; finite PARI check) | bound from Corollary P♯ | rests on |
|---|---|---|---|---|
| C1 | ζ_K, K = Q(√D), fundamental D, 3 <= \|D\| <= 400 | ζ·L(s, χ_D), χ_D primitive real, conductor \|D\|; Γ_R(s)^2 (real) or Γ_R(s)Γ_R(s+1) = Γ_C(s) (imaginary) | 0 <= Λ <= **953/3200 = 0.2978125** | FGMPS (preprint) + Platt–Trudgian (via FGMPS) |
| C2 | ζ_K, K multiquadratic, every quadratic subfield with 3 <= \|disc\| <= 400 (e.g. Q(√-3, √5)) | ζ·Π L(s, χ) over the nontrivial real characters (all primitive, conductors = subfield discriminants) | Λ <= **0.2978125** | as C1; Lemma P iterated |
| C3 | ζ_K, K = Q[x]/(x^3 - x - 1), d_K = -23 | ζ·L(s, f) (F1 exact to n = 3000, F3) | Λ <= **0.449938** | A45 (ours, unpublished) |
| C4 | ζ_H, H = Hilbert class field of Q(√-23) (sextic, S3 closure of C3, disc -23^3) | ζ·L(χ_{-23})·L(f)^2 (F4 exact to n = 2000) | Λ <= **0.449938** | A45 + FGMPS (χ_{-23}, m = 23) |
| C5 | Q(√-23) itself | ζ·L(χ_{-23}) | Λ <= 0.2978125 | case of C1 |

Every improvement of A45 or of FGMPS propagates directly.
- For C1, FGMPS's appendix gives stronger per-character bounds; these were not opened here.
- C2 was not run in PARI. It is the standard abelian factorisation, flagged for the referee.

## 6. Open points for the referee
1. Lemma 3(a). Check that "preserves stability" (BB p. 2) plus real coefficients gives H_2(R) ∪ {0}. (Trivial, but
   check it.)
2. Lemma 1. Check the real-constant argument (e^γ real; Im(βx+γ) constant on R).
3. Corollary P♯ hypothesis "pole orders add". It holds in C1–C5 because L(1,χ) ≠ 0 and L(1,f) ≠ 0 (CLASSICAL).
4. The lead's alternative citations were NOT opened by this seat: BB arXiv:0809.3087 Thm 7.2 and math/0606360 Thm 1.3.
   The opened one is 0809.0401 Thm 1.3.
