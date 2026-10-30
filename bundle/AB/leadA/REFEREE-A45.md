# REFEREE-A45 - hostile referee on THEOREM-A45 (Lambda <= 0.449938, L(eta(z)eta(23z))); 2026-10-29; saved by the lead
Referee scripts: referee45/ (audit_walks.py, gauss_H2.gp, labcopy/spot.py, neg_drop/, neg_dup/, regen/). Second seat (logic only):
referee2-theorem1a.md - reduction CORRECT, coverage CORRECT, novelty CORRECT, tail/evaluator NOT CHECKED.

## In plain words
The bound holds up. The de Bruijn step, the arithmetic and the piecing-together of regions are right. The referee re-audited all 87 walks
and checked the evaluator at 4 visited points against a method sharing none of its code (largest disagreement 4e-14, x up to 12,500).
Findings are paperwork plus ONE missing control: nothing has shown that the walker detects zeros in the new high-x regime (x >= 10,700,
163,841 nodes). Novelty stands only as "first in degree 2" (arXiv:2610.27343's degree-1 bound 0.2978 is much stronger).

| # | Link | Verdict |
|---|---|---|
| 1 | reduction to 0.38 + 0.374^2/2 | CORRECT WITH FIXES (documentation) |
| 2 | finite region and overlaps | CORRECT |
| 3 | evaluator rigour | CORRECT WITH FIXES (missing high-x positive control) |
| 4 | AMEND1 re-split, coverage | CORRECT WITH FIXES |
| 5 | seal order | CORRECT WITH FIXES (wording) |
| 6 | scoring as sealed | CORRECT |
| 7 | novelty and scope | CORRECT WITH FIXES |

(1) Dobner 2005.05142v2 p.9 Thm 3 (OPENED): "If all the roots of G lie in the strip |Im z| <= Delta, then all the roots of G_t lie in the
strip |Im z| <= (max(Delta^2 - 2t, 0))^{1/2}"; p.11 "if t0 in Z, then by applying Theorem 3 with phi(u) := e^{t0 u^2} Phi_F(u), we may
conclude t in Z for all t >= t0". sqrt(1 - 0.76) = 0.4898979; 0.374^2/2 = 0.069938; 19/50 + 0.069938 = 0.449938. Cover (closed): finite
region to y = 0.5; tail to float(0.49) > 0.4898979; tail lower edge float(0.374) < 374/1000; symmetries for x < 0, y < 0.
FIX (a): TAIL-LEMMA.md still states t = 21/50, y in [0.374, 0.4] with t = 0.42 Step 10 numbers - add an A45 addendum (t = 19/50,
y in [0.374, 0.49]; vertices 1.35/1.35/2.49/5.19 all < Lam(T1) = 13.68; rhs 0.1698; K0 uses |Im alpha| <= 0.79, t-independent).
FIX (b): tail_run045_out.json and tail_run045b_out.json are labelled "t": "21/50" but the code runs 19/50 (TN, TD = 19, 50 in the diff vs
tail_run.py); stale docstrings (8 y-boxes, x = 7200). Relabel and say so in THEOREM-A45.
(2) Rectangle [0, 12500] x [0.374, 0.50]; gap [12500, 13000] covered by BAR-A12b (8 boxes, T 6250-6500, min margin 0.829 at x ~ 12,592);
BAR-A12 contiguous T 6500 to 1e12 (202 boxes, min margin 0.781 on x ~ 13,398-13,608). Top edge 0.5 above the de Bruijn edge (double
cover, harmless).
(3) cert_core.py (3c5f7f2b) and cert_wind_ckpt.py (6ba15815) byte-identical to BAR-A8; qerr from the h actually used (dyadic switch changes
cost only); BUILD lines xb 10650 81,921 nodes, xb 10700 163,841; fsum factor covers n = 163,841. Spot checks vs own PARI Gaussian average
(57 digits): (100, 0.374) log|H| -75.751049807394 identical, arg diff 1e-15; (800, 1/2) -623.482218857459 identical, 4e-15; (4000, 0.374)
-3134.357367594623 identical, 4e-14; (12500, 1/2) -9807.871982413984 vs ...983, 9e-15. All inside lab radii ((800, 1/2) radius 8e-8
relative: loose but valid). Referee's own instrument bug disclosed (one-sided PARI window -> fake 3e-4 gap; fixed by a symmetric window at
57 digits). MISSING CONTROL: the largest-x positive control at t = 19/50, p = 23 is [796, 800] (BAR-A4-AMEND1 C3); the 73k-164k-node blocks
have never been shown to detect a zero. FIX: seal a high-x box, e.g. [12496, 12500] x [-1/2, 1/2] at t = 19/50, predicted winding = PARI
count of real sign changes in the box, plus a refusal test there.
(4) Independent audit of all 87 used walks (checkpoint chains done = 1..n with n from the declared path; last checkpoint = JSON argsum and
point count; >= 2 points per sub-segment; single "exit 0", no resume; t = 19/50, c = 30). Edges tile once (bottom 9, top 78, right 1, left
1); 196,660 points; winding value ~1e-53, radius 4.77e-4. Superseded tops 0 points. The lab's negative test deleted the JSON (failed on
"missing" too - not isolated); sharper tests: removing the piece from pieces45.txt as well -> FAILED on top coverage; a duplicated piece ->
FAILED on top coverage. Coverage check genuine. FIX (a): the combiner trusts the declared path and never checks the checkpoint chain - add
done = 1..len(subs) and points >= 2 len(subs). FIX (b): the AMEND1 "unit test on synthetic data" has no file / LOG entry - log or withdraw.
Regeneration of pieces45.txt byte-identical (5946a63a).
(5) All 5 seal hashes + code hashes match. Birth times: A12 seal 16:26:59 / run 16:27:17; A13 16:28:01.3 / 16:28:01.5; A12b 16:33:40 /
16:33:57; A14 16:43:39.9 / P0 16:43:41 / walkers 16:43:45. AMEND1 created 17:42:03.76, pieces + stubs 17:42:04.16, AMEND1 last written
17:42:23.91, runner 17:42:29, first piece 21:52. FIX: reword "generated after the seal" -> "generated in the sealing minute; content fixed
by the sealed generator (regeneration byte-identical)".
(6) P0 argsum 12.566370614359172953 = 4 pi +- 5e-17 -> winding 2; P1 live walks exit 0 (say the 6 superseded exits are vacuous by design);
P2 holds; P3 MISS (13.40 h vs 14-16.5 h). A12 A, B, C pass (938 s); A12b A, C pass (212 s; B excluded by the sealed HOLDS rule, hard-coded in
the hashed tail_run045b.py); A13 timings in band.
(7) arXiv:2610.27343 ABSTRACT only: degree 1 (Lambda_L <= 953/3200, conductors 3..400; Polymath-style effective approximation, Platt's GRH
verification, interval arithmetic). L(s, psi) here is primitive degree 2 (irreducible dihedral rep from the cubic class character).
"First explicit sub-1/2 bound in degree 2" survives at the search floor. FIX: add a novelty paragraph (one L-function; 0.45 far weaker
than 0.298 in degree 1; their method probably transfers; no "first" beyond the search floor).

Blocks release: (3) the sealed high-x positive control and (1a) the TAIL-LEMMA parameter addendum. Rest is wording.
Next strike: seal and run [12496, 12500] x [-1/2, 1/2] at t = 19/50 (predicted winding from a PARI sign-change count), same walker and
evaluator, ~10-20 min on one core.
Not checked: body of 2610.27343; tail_cert.py internals beyond REFEREE-A6; regeneration of any walk.
