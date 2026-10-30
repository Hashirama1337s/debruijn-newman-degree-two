I'll check the cited theorems and the region arithmetic against the papers, not the lab's sealed numbers.**In plain words.** The constant arithmetic and the two uses of de Bruijn’s strip theorem are right, and the rectangles written in the proof do cover the half-plane that the argument needs. The 12,500–13,000 slab is not a hole in the write-up. I did not re-run the sealed programs, so this is a logic read, not a second computation.

## Verdicts

| Link | Verdict |
|---|---|
| Reduction (Dobner Thm 3, twice) | **CORRECT** |
| Region coverage | **CORRECT** |
| Tail | **NOT CHECKED** (shape only) |
| Evaluator rigour | **NOT CHECKED** |
| Novelty against arXiv:2610.27343 | **CORRECT** (not subsumed) |
| Overall | **CORRECT** on the written chain, computations not re-executed |

## Reduction

**OPENED** Dobner, ar5iv HTML of arXiv:2005.05142, Theorem 3:

> “If all the roots of \(G\) lie in the strip \(|\operatorname{Im} z|\le\Delta\), then all the roots of \(G_t\) lie in the strip \(|\operatorname{Im} z|\le(\max(\Delta^2-2t,0))^{1/2}\).”

Hypotheses stated there: \(\phi(u)=\overline{\phi(-u)}\), and \(\phi(u)=O(e^{-|u|^b})\) for some \(b>2\), with \(t>0\). Equation (6) is \(\xi_t^F((1+iz)/2)=\int e^{tu^2}\Phi_F(u)e^{izu}\,du\). In the proof of Theorem 1 he applies the same theorem to \(\phi(u)=e^{t_0 u^2}\Phi_F(u)\), after showing \(\Phi_F(u)\ll\exp(-e^{2\delta u/(3Q^\delta)})\). Multiplying by \(e^{0.38 u^2}\) keeps a decay faster than \(e^{-|u|^b}\), \(b>2\).

So \(|\operatorname{Im}|\le\Delta\) at time \(t_0\) gives real zeros for every later time at least \(t_0+\Delta^2/2\), including equality, because the displayed bound is \(\le(\max(\Delta^2-2t,0))^{1/2}\).

- First use: \(\Delta=1\), \(t=19/50\), so \(2t=19/25=0.76\) and the half-width is \(\sqrt{6}/5=0.4898979\ldots\). Writing \(0.48990\) rounds up, which is a valid closed upper bound.
- Second use: \(\Delta=374/1000\). Then \((374/1000)^2/2=0.069938\) and \(19/50+0.069938=0.449938\). The lower bound \(0\le\Lambda\) is Dobner’s Theorem 2 for \(F\in\mathcal{S}^\sharp\), which this cusp form is.

The initial claim \(|\operatorname{Im} z|\le 1\) for \(H_0\) is the critical strip under \(s=(1+iz)/2\). It is inherited from the identification in THEOREM-A; this note does not re-prove it.

## Region coverage

No missing slab.

- Finite piece: \(0\le x\le 12500\), \(0.374\le y\le 0.50\).
- BAR-A12b, as written: \(12500\le x\le 13000\), \(0.374\le y\le 0.49\).
- BAR-A12: \(x\ge 13000\), same \(y\)-interval.
- Above the strip: \(\sqrt{6}/5<0.4899<0.49\), since \(0.4899^2=0.24000201>0.24\) and \(0.49^2=0.2401>0.24\). The sentence “\(y>0.4899\): Step 1” leaves out \(\sqrt{6}/5<y\le 0.4899\), but that closed slab sits inside both the finite top \(0.50\) and the tail top \(0.49\).
- A zero on \(y=0.374\) is inside the closed sets. A winding number that is defined already requires \(H\neq 0\) on the contour, so the conclusion \(|\operatorname{Im} z|<0.374\), hence \(\le 374/1000\), is the right direction for \(\Delta\).
- Left half-plane and lower half-plane are the two symmetries named in Step 4. For real \(\Phi\), \(H(-\overline{z})=\overline{H(z)}\) is the horizontal reflection.

## Tail

**OPENED** Palojärvi–Zhao, arXiv:2508.03023. In v1, Lemma 3.2 is the convexity bound: for \(\varepsilon\in(0,1/2]\) and \(\operatorname{Re}s\in[-\varepsilon,1+\varepsilon]\),

> “\(|L(s)|\le b_{1+\varepsilon}|Q(2+s)|^{(1+\varepsilon-\sigma)/2}|P(s-2)/P(s-1)|\).”

In v2 that display is Lemma 3.3 (v2 Lemma 3.2 is a gamma bound used inside its proof). The renumbering in the note is accurate. That lemma is an upper bound on \(|L|\). It is not a non-vanishing theorem for \(H_t\).

The non-vanishing claim is the sealed box arithmetic (margins 0.78 and 0.83, and \(0.1698<1-P_1-P_2\)). Those figures were not recomputed here. `TAIL-LEMMA.md` was not opened: not found from this seat.

## Evaluator

The certificate shape is the right one: an argument-change enclosure of radius \(4.8\times 10^{-4}\) about \(8.2\times 10^{-54}\) contains no nonzero integer, so the winding is 0 if the balls really stay off 0 and the 87 walks tile the boundary once. I did not open `cert_core.py`, `cert_wind_ckpt.py`, or `coverage_report_A14.json`. Rigour of the run is **not checked**. The control winding 2 on \([5,15]\times[-1/5,1/5]\) only shows that a nonempty count can come out.

## Novelty

**OPENED** arXiv:2610.27343 (abstract and PDF). Freire–González-Riquelme–Muñoz–Poblete–Salinas, 19 Oct 2026:

> “We prove the unconditional uniform bound \(\Lambda_L\le 953/3200=0.2978125\) for every primitive real-valued character of conductor \(3\le m\le 400\).”

That is degree 1, real primitive Dirichlet \(L\)-functions. Their Theorem 1.1 also uses the shape \(\Lambda\le D^2/2\) under an initial strip \(|\operatorname{Im} z|\le D\). It does not include \(L(s,\eta(z)\eta(23z))\). A prior bound for this form was **not found**.

Next strike: in `tail_run045b` and the finite contour, check by interval arithmetic that the certified \(y\)-interval contains \([\sqrt{6}/5,\,374/1000]\) with the lower endpoint’s right end \(\le 374/1000\), so one ulp cannot push \(\Delta\) past the zero-free edge.