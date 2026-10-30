I'll boot house rules, then hunt the Borcea–Brändén sign, the heat-flow identity, and prior art on product Lambda.Local boot files aren't reachable from this tool set, so I'll search the papers and theorems directly.Identity sign matches the Fourier calculation; next I’ll open the stability theorems and the Freire/Dobner papers to pin the operator and prior art.**In plain words.** The identity and the minus sign are right. The sketch proves \(\Lambda(FG)\le\max(\Lambda(F),\Lambda(G),0)\). That is enough for the planned L-function corollaries, because Dobner already forces those \(\Lambda\) to be \(\ge 0\). The unrestricted claim \(\Lambda(FG)\le\max(\Lambda(F),\Lambda(G))\) when the max is negative is not given by this operator. No paper found states the product rule. Dedekind-zeta upper bounds are not found; the ingredients (zeta, Dirichlet \(L\), existence of \(\Lambda\)) exist separately.

---

**(i) Lemma P: CORRECT on the identity and on the sign for \(c=2t\ge 0\); the sketch does not prove the claim when \(\max(\Lambda_F,\Lambda_G)<0\).**

**(2) Identity — CORRECT.** With \(H_t(z)=\int e^{tu^2}\Phi(u)e^{izu}\,du\) and \(\Phi_{FG}=\Phi_F*\Phi_G\),

\[
e^{tu^2}(\Phi_F*\Phi_G)(u)=\iint e^{tv^2}e^{tw^2}e^{2tvw}\Phi_F(v)\Phi_G(w)\,dv\,dw.
\]

On the product \(H_t^F(x)H_t^G(y)\), \(\partial_x\partial_y\) multiplies the mode \(e^{ixv}e^{iyw}\) by \((iv)(iw)=-vw\), so \(\exp(-2t\partial_x\partial_y)\) multiplies by \(\exp(2tvw)\). Restricting to \(x=y=z\) recovers \(H_t^{FG}(z)\). (Direct expansion of the stated Fourier formula; not taken from a paper.)

**(1) Sign — CORRECT that \(\exp(-c\partial_x\partial_y)\) for \(c\ge 0\) is the stability-preserving choice; \(\exp(+c\partial_x\partial_y)\) is the other one.**

OPENED, Borcea–Brändén, *Multivariate Pólya–Schur classification…*, arXiv:math/0606360v6, Thm 1.3 (p. 4 of the HTML): “Let \(T\in\mathcal{A}_n[\mathbb{R}]\). Then \(T\in\mathcal{A}_n(\mathbb{R})\) if and only if \(F_T(z,-w)\in\mathcal{H}_{2n}(\mathbb{R})\).”

For \(T=(1-(c/n)\partial_x\partial_y)^n\), one has \(F_T(z,-w)=(1-(c/n)w_xw_y)^n\). The polynomial \(1-\varepsilon xy\) does not vanish for \(\operatorname{Im}x>0\), \(\operatorname{Im}y>0\) (a positive real is not a product of two open-UHP numbers). So each finite approximant preserves real stability, and \(\exp(-c\partial_x\partial_y)\) is the limit. The plus sign gives \(1+\varepsilon xy\), which vanishes at \((i/\sqrt{\varepsilon},i/\sqrt{\varepsilon})\).

OPENED, Borcea–Brändén, *Lee–Yang and Pólya–Schur II*, arXiv:0809.3087, Thm 8.3 (Lieb–Sokal): “If \(R\) is weakly Hurwitz stable (in \(2n\) variables) then \(S\) is either weakly Hurwitz stable or identically zero,” with \(S(z)=\sum P_i(\partial/\partial z)Q_i(z)\). Same paper, §6: “Lieb and Sokal proved that the operation that replaces one variable with differentiation with respect to another variable preserves weak Hurwitz stability” (citing Lieb–Sokal 1981, Prop. 2.2). The 1981 PDF first page was opened; Prop. 2.2 itself was not reached.

OPENED, Craven–Csordas, *Differential operators of infinite order…*, Hawaii PDF of J. Math. Anal. Appl. 186 (1994), Thm 3.10: “Let \(f\in\mathrm{L}\text{-}\mathrm{P}\) and suppose the order \(\rho(f)<2\). Let \(u(x,t)=e^{-tD^2}f(x)\) for all \(t>0\). Then, for each fixed \(t>0\), we have \(u(x,t)\in\mathrm{L}\text{-}\mathrm{P}\) and the zeros of \(u(x,t)\) are all simple.” Univariate analogue of the minus sign.

Diagonal restriction is immediate: a real-stable \(f(x,y)\) gives a stable \(f(z,z)\).

**The exact gap.** If \(t=\max(\Lambda_F,\Lambda_G)\ge 0\), the operator has \(c=2t\ge 0\) and the sketch works, so \(\Lambda(FG)\le\max(\Lambda_F,\Lambda_G)\). If the max is negative, the same identity is \(\exp(+2|t|\partial_x\partial_y)\), which does not preserve stability. At \(t=0\) one does have \(H_0^{FG}=H_0^F H_0^G\), hence \(\Lambda(FG)\le 0\) whenever both factors already have only real zeros. That is weaker than \(\le\max<0\). Remaining analytic gap: BB theorems as quoted are for polynomials / finite-order operators; passage to these order-2 Fourier integrals is the usual Hurwitz/LP limit, not written out.

---

**(ii) Prior art.**

- **Lemma P: OPEN.** Searches of arXiv and Zenodo for “de Bruijn-Newman” with product / Dedekind / Laguerre–Pólya / number field did not turn up a statement \(\Lambda(FG)\le\max(\Lambda(F),\Lambda(G))\). Say **not found**, not “absent from all literature.”
- **Dedekind-zeta \(\Lambda\) bounds: PARTIAL.** Components exist; the product bound does not.

OPENED, Freire–González-Riquelme–Muñoz–Poblete–Salinas, arXiv:2610.27343v1, abstract: “We prove the unconditional uniform bound \(\Lambda_L\le 953/3200=0.2978125\) for every primitive real-valued character of conductor \(3\le m\le 400\).” The paper treats Dirichlet \(L\), not Dedekind zeta. Same intro: “Platt and Trudgian subsequently improved this bound to \(\Lambda^\zeta\le 0.2\).”

OPENED, Platt–Trudgian, arXiv:2004.09765v1, Corollary 2: “We have \(\Lambda\le 0.2\).”

OPENED, Dobner, arXiv:2005.05142v2, Thm 1: “For every \(F\in\mathcal{S}^\sharp\), there is a real number \(\Lambda_F\) such that all the zeros of \(\xi_t^F\) lie on the critical line if and only if \(t\ge\Lambda_F\).” Extended Selberg class includes Dedekind zetas; this gives existence and \(\Lambda\ge 0\), not an upper bound.

The number \(0.449938\) and a de Bruijn–Newman bound for \(\eta(z)\eta(23z)\) or the cubic field of discriminant \(-23\): **not found** on arXiv or Zenodo.

---

**(iii) Closest sources.**

| Item | Source | Role |
|---|---|---|
| Sign / symbol | BB math/0606360 Thm 1.3; 0809.3087 Thm 7.3, 8.3 | OPENED |
| Univariate heat | Craven–Csordas 1994 Thm 3.10 | OPENED |
| \(\Lambda_L\le 953/3200\) | Freire et al. 2610.27343 | OPENED |
| \(\Lambda_\zeta\le 0.2\) | Platt–Trudgian 2004.09765 Cor. 2 | OPENED |
| \(\Lambda\ge 0\) on \(\mathcal{S}^\sharp\) | Dobner 2005.05142 Thm 1 | OPENED |
| Quadratic Dirichlet family | Stopple, arXiv:1301.3158 ABSTRACT | \(\Lambda_{Kr}=\sup\Lambda_{-D}\), not a product rule |
| Dedekind \(\Lambda\) upper bound | — | not found |
| Product lemma | — | not found |

**Next strike:** write Lemma P as \(\Lambda(FG)\le\max(\Lambda_F,\Lambda_G,0)\), then the quadratic Dedekind bound \(\Lambda(\zeta_K)\le 953/3200\) from Freire + Platt–Trudgian + Dobner.