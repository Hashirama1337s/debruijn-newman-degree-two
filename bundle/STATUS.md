# Status of every claim

Moki & Julio (AI-assisted). Public status table for the supplementary bundle of draft v1 of the note, October 2026.

## In plain words
This page lists each result of the note, what it says, and how far it has been checked. "PROVED (AI-refereed)" means a
written proof is in this bundle (or in the note), its computational steps are certified in interval or ball arithmetic
under sealed pass/fail rules, and independent AI referees read it, with every fix applied. **No human expert has
checked any of it yet**; that reading is the real bar for calling these theorems. Nothing here assumes the generalised
Riemann hypothesis (GRH), and nothing here bears on the Riemann hypothesis itself.

## Status words (as in the note)
- **CLASSICAL**: known, with a reference.
- **PROVED (AI-refereed)**: written proof; computational steps certified in interval or ball arithmetic under sealed
  (pre-registered) pass/fail criteria; read by AI referees, every fix applied. Not checked by a human expert.
- **CONDITIONAL**: proved here from a stated input that is itself not refereed (here: the October 2026 preprint
  arXiv:2610.27343 of Freire, González-Riquelme, Muñoz, Poblete and Salinas).
- **NUMERICAL**: a sealed computation in exact arithmetic that supports, but is not part of, a proof.
- **HEURISTIC**: numerical evidence only; nothing is claimed.
- **SUPERSEDED**: an earlier result replaced by a stronger one; kept for the record.
- **FAILED**: a sealed prediction that did not hold; kept on record, re-run only under a sealed amendment.

## Setting
For F in Dobner's extended Selberg class, H_t^F(z) = ∫ e^{tu²} Φ_F(u) e^{izu} du, and Λ_F is the least t at which all
zeros of H_t^F are real (Dobner, arXiv:2005.05142). f_23 = η(z)η(23z) (LMFDB 23.1.b.a, L(s, f_23) = L(s, ψ) for the
order-3 class-group character ψ of Q(√−23)); f_44 = η(2z)η(22z) (LMFDB 44.1.d.a).

## Table
| item (note section) | statement (short) | status | conditions | where in the bundle |
|---|---|---|---|---|
| Λ_F ≤ 1/2 and Λ_F ≥ 0 (§1) | the trivial upper bound; Newman-type lower bound on Dobner's class | CLASSICAL | Dobner Thms 1-3 (de Bruijn 1950, Thm 13) | note §1 |
| Theorem 1(a) (§2.1) | for f_23: all zeros of H_t real for t ≥ 19/50 + (374/1000)²/2 = 0.449938, so 0 ≤ Λ_ψ ≤ 0.449938 | PROVED (AI-refereed) | unconditional (no GRH); two AI referee reads of the full chain (one re-implementing the computations), earlier reads of the method and the tail lemma; both release blockers resolved | `AB/leadA/THEOREM-A45-v2.md`, `AB/leadA/tail/`, `AB/leadA/cert/`, `AB/leadA/referee45/`, `AB/leadA/REFEREE-A45.md`, `AB/leadA/referee2-theorem1a.md` |
| Theorem 1(a), Step 2 (tail) | H_{0.38}(x+iy) ≠ 0 for x ≥ 12,500, 0.374 ≤ y ≤ 0.49 (202 + 8 interval boxes; monotonicity beyond 2·10^12, error sum ≤ 0.1698) | part of Theorem 1(a) | sealed BAR-A12, BAR-A12b (HOLDS) | `AB/leadA/tail/` |
| Theorem 1(a), Step 3 (finite region) | certified winding 0 of H_{0.38} around [0, 12500] × [0.374, 0.50]; 196,660 ball evaluations, 87 walks, exact edge coverage | part of Theorem 1(a) | sealed BAR-A14 + AMEND1 (HOLDS; wall-time prediction missed, faster); positive controls winding 2 (low) and 5 (high-x, BAR-A16, = independent PARI count) | `AB/leadA/cert/` |
| Theorem 1(b) (§2.2) | for f_44: all zeros of H_t real for t ≥ 21/50 + (374/1000)²/2 = 0.489938, so 0 ≤ Λ_χ ≤ 0.489938 | PROVED (AI-refereed) | unconditional; one AI referee read of a pipeline shared with (a); sealed BAR-A9, A10, A11, A15 (HOLDS) | `AB/leadA/THEOREM-A11.md`, `AB/leadA/p11/` |
| earlier bound for f_23 | Λ_ψ ≤ 0.489938 from the first run at t = 21/50 | SUPERSEDED by Theorem 1(a) | kept for the pipeline record | `AB/leadA/THEOREM-A.md`, `AB/leadA/referee2-thmA.md`, `AB/leadA/REFEREE-A4.md` |
| Theorem P (§3.1, §3.4) | for kernels Φ, Ψ of class D: Λ(Φ ∗ Ψ) ≤ max(Λ(Φ), Λ(Ψ), 0) | PROVED (AI-refereed) | one full AI referee read of the written proof (no gap) plus an independent AI check of the identity and the sign; an easy consequence of Borcea–Brändén's symbol theorem, found stated nowhere at our search floor (not claimed as a new method) | note §3 (corrected text); `Z3/PROOF-P.md` (the draft that was read), `Z3/referee2-lemmaP.md`, referee line in `seals/SEALS.md` |
| Corollary P♯ (§3.1) | for F, G, FG in Dobner's class with γ_{FG} = γ_F γ_G: Λ_{FG} ≤ max(Λ_F, Λ_G) | PROVED (AI-refereed) | Dobner Thms 1-2 | note §3 |
| "the 0 cannot be dropped" (§3.5) | e^{−tD²}(x² − 1) has real zeros iff t ≥ −1/2 (polynomial class, not class D) | CLASSICAL computation | - | note §3.5 |
| application check (§3.6) | identity 0/400 failures; key step 0/400 violations (opposite-sign null fires 374/400); lemma 0/300 violations (null without the 0 fires 233/300); Λ(x² + 1) = 1/2; ζ_K = ζ·L(s, f_23) (n ≤ 3000) and ζ_H = ζ·L(s, χ_{−23})·L(s, f_23)² (n ≤ 2000) | NUMERICAL (sealed, exact arithmetic); not part of the proof | sealed BAR-Z3-P | `Z3/BAR-Z3-P.md`, `Z3/lp/` |
| C1 (§4) | Λ ≤ 953/3200 = 0.2978125 for ζ_K, K = Q(√D), fundamental D, 3 ≤ \|D\| ≤ 400 | CONDITIONAL | on Freire et al. (unrefereed preprint); Platt–Trudgian (published) | note §4 |
| C2 (§4) | the same bound for multiquadratic fields whose quadratic subfields all have 3 ≤ \|disc\| ≤ 400 | CONDITIONAL | as C1; Theorem P iterated at kernel level; factorisation classical, not re-checked numerically | note §4 |
| C3 (§4) | Λ ≤ 0.449938 for ζ_K, K = Q[x]/(x³ − x − 1), d_K = −23 (non-Galois cubic) | PROVED (AI-refereed) | Theorem 1(a) + Platt–Trudgian; factorisation checked in BAR-Z3-P | note §4 |
| C4 (§4) | Λ ≤ 0.449938 for ζ_H, H the Hilbert class field of Q(√−23) (sextic, disc −23³) | CONDITIONAL | Theorem 1(a) + Platt–Trudgian + Freire et al. (m = 23) | note §4 |
| novelty (§6) | first explicit bounds below 1/2 for a primitive degree-2 L-function and for Dedekind zeta functions of number fields other than Q | at our search floor only (30 October 2026); a search floor is not a clearance | - | note §6 |
| outlook: main-term fidelity (§5) | a degree-2 transcription of the Freire et al. main term tracks the certified H_t to 1.9·10^{−4} at x ≈ 10,450, t = 1/4; error ~ 1/M (slope −0.98) | HEURISTIC; nothing claimed | sealed BAR-Z2-1 (FAILED: writer bug), AMEND1, AMEND2 (MAIN HOLDS) | `Z2/z2-1/` |
| outlook: crude envelope (§5) | E ≤ 0.031 at x ≈ 10,450, t = 1/4; above the measured error at all 54 points; 1.5-2.3 at t = 0, 0.41 at t = 1/10 | HEURISTIC; nothing claimed (the window lemma is unproved) | sealed BAR-Z3-1 (MAIN HOLDS) | `Z3/z3-1/`, `Z3/RESULT-Z3-1.md` |
| certified zeros of 38 ring-class L-functions (§6) | 4,701 zeros on the line | supporting data only; not claimed as new; not in this bundle | - | - |

## Failures on record
- BAR-A6 (first tail run, t = 21/50): FAILED on a code gap in one tail branch (the box returned no bound; no false
  certificate possible); re-run under BAR-A6-AMEND1 and AMEND2 (HOLDS). `AB/leadA/tail/`.
- BAR-A14, prediction P3 (wall time 14-16.5 h): MISSED, the run took 13.4 h after the sealed re-balance AMEND1.
- BAR-Z2-1 (outlook): FAILED, the writer stored a format template instead of the values; re-run under AMEND1 (scorer
  parser) and AMEND2 (writer). `Z2/z2-1/`.
