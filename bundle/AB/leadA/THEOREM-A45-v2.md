# THEOREM A45 (v2) - Lambda <= 0.449938 for the L-function of eta(z)eta(23z)

Moki & Julio (AI-assisted). Lab record, 2026-10-29. Not published. v1 (THEOREM-A45.md, sha256 5f3a533d...) is kept
unchanged; this file applies every fix of REFEREE-A45.md (local referee, computations) and of the second seat
(referee2-theorem1a.md, logic), and adds the BAR-A16 result.

**Status:**
- Every computational piece is certified and sealed:
  - BAR-A12 (tail x >= 13000) HOLDS;
  - BAR-A12b (gap tail 12500-13000) HOLDS;
  - BAR-A13 (rate probe) HOLDS;
  - BAR-A14 (finite region, re-balanced by BAR-A14-AMEND1) HOLDS;
  - BAR-A16 (high-x positive control, requested by REFEREE-A45) HOLDS: winding 5 = PARI count 5.
- Two referee reads of v1: REFEREE-A45 (bound holds; links CORRECT or CORRECT WITH FIXES; two release blockers) and
  the second seat (reduction, coverage and novelty CORRECT; tail and evaluator not checked by that seat).
- Release blockers: (3) high-x positive control -> BAR-A16 (below); (1a) tail parameters -> TAIL-LEMMA-ADDENDUM-A45.md.
- Not published. Release goes through the publish gate and needs the authors' explicit approval.

## In plain words
THEOREM-A pushed the de Bruijn-Newman constant of this degree-2 L-function from the trivial 1/2 down to 0.489938.
Here the same machinery, run overnight, pushes it to **0.449938**.

The heat dial is now set lower, at 0.38 instead of 0.42, so the zeros have had less time to move toward the line. The
price is that the far-out estimate only takes over from x = 12,500, and the near region must be certified all the way
there. That region was split into 87 walks covering the boundary exactly once, and they took 13.4 hours on 9 cores.
A final control then checked that the same code, at the far end of that region, finds the zeros PARI says are there.

## Statement
f, L, xi, Phi and H_t are exactly as in THEOREM-A:
- f(z) = eta(z) eta(23z), the newform 23.1.b.a;
- xi(s) = (sqrt23/(2pi))^s Gamma(s) L(s);
- Phi(u) = 2 e^u f(i e^{2u}/sqrt23);
- H_t(z) = int e^{tu^2} Phi(u) e^{izu} du (Dobner eqs. (5), (6)).

**Theorem A45.** For every t >= 19/50 + (374/1000)^2/2 = 0.449938, all zeros of H_t are real. Hence
0 <= Lambda_psi <= 0.449938.

## Proof chain (THEOREM-A with t0 = 19/50)
**Steps 0-1** (unchanged from THEOREM-A: identification f = theta_chi, Dobner's axioms, evenness on the ray).
- The zeros of H_0 satisfy |Im z| <= 1.
- de Bruijn Thm 13, as quoted in Dobner Thm 3 (arXiv:2005.05142v2 p. 9), with Delta = 1 and t = 0.38: the zeros of
  H_{0.38} satisfy |Im z| <= sqrt(1 - 0.76) = sqrt6/5 = 0.4898979...

**Step 2 - right tail.** TAIL-LEMMA.md as written is stated for t = 21/50, y in [0.374, 0.4] (THEOREM-A). For this
theorem read it with **TAIL-LEMMA-ADDENDUM-A45.md** (t = 19/50, eps = 1/5, y in [0.374, 0.49]; Step 10 vertices
1.35 / 1.35 / 2.49 / 5.19 all < Lam(T1) = 13.68; rhs 0.1698; K0 from |Im alpha| <= 0.79, which does not involve t;
every number re-derived from the run outputs there). Code: tail_cert.py in the AMEND2 state, run by tail_run045.py and
tail_run045b.py.
H_{0.38}(x+iy) != 0 for x >= 12500 and y in [0.374, 0.49]:
- **BAR-A12 HOLDS** (x >= 13000; 16 y-subboxes):
  - 202 interval boxes for 13000 <= x <= 2·10^12, tightest margin 0.78 at x of about 13,398;
  - Step 10 for x >= 2·10^12: error sum <= 0.1698 < 1 - P1 - P2 (>= 0.99999), vertices checked;
  - cross-check at x = 13000: log lower bound -10203.86 <= log certified |H| -10201.22.
- **BAR-A12b HOLDS** (gap 12500 <= x <= 13000; 32 y-subboxes):
  - 8 boxes, tightest margin 0.83 at x of about 12,592;
  - cross-check at x = 12500: -9811.62 <= -9808.41;
  - its asymptotic printout is excluded by its seal, since x >= 13000 is BAR-A12 (the HOLDS rule without part B is
    hard-coded in the hashed tail_run045b.py).
- **Relabel note.** tail_run045_out.json and tail_run045b_out.json carry `"t": "21/50"` in their "params" block. The
  label is stale: line 16 of both scripts (`out = {"params": dict(t="21/50", ...`) was copied unchanged from
  tail_run.py, so it does not appear in the diff, while the parameter the code uses did change:
  `< TN, TD, EN, ED = 21, 50, 1, 5` / `> TN, TD, EN, ED = 19, 50, 1, 5` (`diff tail_run.py tail_run045.py`, hunk
  12,15c12,15; tail_run045b.py has the same line 12). Every box_margin call and part B use TN/TD = 19/50. The docstrings
  (8 y-subboxes, [3600, 1e12], x = 7200) are also stale. The hashed outputs are not edited; read their label as 19/50.
- Edges of the tail rectangle: its lower edge float(0.374) = 3368692521273131/2^53 < 374/1000, and its top
  float(0.49) > sqrt6/5 (0.49^2 = 0.2401 > 0.24).

**Step 3 - finite region** (BAR-A14 HOLDS; evaluator cert_core.py and walker cert_wind_ckpt.py unchanged from BAR-A8).
H_{0.38} has no zeros in the closed rectangle [0, 12500] x [0.374, 0.50]:
- certified winding 0 of H_{0.38} around the boundary (value 8.2e-54, radius 4.8e-4);
- 196,660 ball evaluations over 87 walks, all exit 0;
- **coverage** (cert_combine45b.py, coverage_report_A14.json): bottom (9 intervals), top (78), right (1) and left (1)
  each tile their edge exactly once;
- the 6 superseded tops (g45_t3, t4, t6-t9) did no work (0 points). Their "exit 0" is **vacuous by design**: the
  AMEND1 stub sets done = 10^9, so the walker skips every sub-segment and writes a 0-point JSON;
- negative test: removing one piece (g45_q11000_11050) makes the combiner FAIL and flags the gap [11000, 11050]. The
  referee's sharper tests (piece removed from pieces45.txt as well; a duplicated piece) both FAIL on top coverage;
- **combiner caveat.** cert_combine45b.py trusts each walk's declared path and its JSON (argsum, points); it does not
  check the checkpoint chain (done = 1..len(subs), points >= 2 len(subs)). No such case occurred: the referee's
  independent audit (referee45/audit_walks.py) found, for all 87 walks, chains done = 1..n with n from the declared
  path, last checkpoint = JSON argsum and point count, >= 2 points per sub-segment, a single "exit 0" and no resume. A
  future combiner should make that check itself;
- control P0: [5, 15] x [-1/5, 1/5] gives certified winding 2 at t = 19/50;
- **high-x control (BAR-A16 HOLDS)**: the same walker and evaluator (identical hashes, same arguments) around
  [12496, 12500] x [-1/2, 1/2] at t = 19/50, in the 163,841-node regime (BUILD xb=12500 nodes=163841), give
  certified winding **5** (argsum 10 pi, radius 4.2e-18; 84 points), equal to the 5 real sign changes PARI counts there
  with a method sharing no code (Gaussian average of lfunlambda, 57 digits). A walk along the real axis through the
  PARI zero in (12497.9, 12498.0) is refused ("cannot certify step" at x = 12497.914, exit 1, no JSON).

**Step 4 - cover.**
- 0 <= x <= 12500 and 0.374 <= y <= 0.50: Step 3.
- x >= 12500 and 0.374 <= y <= 0.49: Step 2.
- y > sqrt6/5 = 0.4898979...: Step 1. The slab sqrt6/5 < y <= 0.4899 needs no separate argument: it lies inside both
  the finite-region top (y <= 0.50) and the tail top (y <= 0.49), since 0.4899^2 = 0.24000201 > 0.24. (v1's sentence
  "y > 0.4899: Step 1" left this slab unstated.)
- x < 0 and y < 0: the symmetries H(-conj z) = conj H(z) and H(conj z) = conj H(z).
- So every zero of H_{0.38} has |Im z| < 0.374.

**Step 5 - de Bruijn, second use.**
- Thm 13 (Dobner Thm 3) is applied to phi = e^{0.38u^2} Phi with Delta = 0.374, as in Dobner's proof of Thm 1 (p. 11).
- All zeros of H_t are real for t >= 0.38 + 0.069938 = 0.449938.

## Run record (honest)
- **BAR-A13:** the probe gave 15-18 h for X = 13000, which straddled the ~16 h bar.
  - Smarter fix: BAR-A12b moved the tail start to 12500 with finer y-boxes, giving an ETA of 14-16.5 h.
- **BAR-A14:** launched 16:44 on 9 workers.
  - At 47 min the load proved lopsided: at x >= ~10700 the dyadic quadrature step halves (2^-13 -> 2^-14), doubling
    the nodes (81,921 -> 163,841) and the cost per step.
  - **BAR-A14-AMEND1** (sealed 17:42) superseded the six unstarted top chunks and cut them into 75 pieces. The pieces
    ran on cores freed by finished workers (never more than 9). Scoring moved to a combiner with an exact coverage
    check.
  - The 75-piece list was **generated in the sealing minute; its content is fixed by the sealed generator**
    (amend1_prepare45.py, hash in the seal; regeneration in a clean directory is byte-identical, LOG 18:31 and the
    referee's regen/). Birth times: AMEND1 created 17:42:03.76, pieces + stubs 17:42:04.16, AMEND1 last written
    17:42:23.91, runner 17:42:29.
  - **AMEND1's "unit test on synthetic data".** Its files survive in the lead's private working folder, not shipped (combtest/: synthetic
    walk JSONs, written 17:41:45-46, before the seal, with the sealed cert_combine45b.py c23a3f3f). Only the last half
    survived: one piece (g45_q05900_06000) missing -> holds false (g45b_combine.json 5d2cf6f4); the full-coverage
    half's output was overwritten and is not on file. Archived in cert/amend1_unittest/orig_scratch/ and reproduced
    POST HOC on 10-29 (cert/amend1_unittest/): 75/75 pieces -> HOLDS; one piece missing -> FAILED, with output
    byte-identical to the surviving original (LOG 06:54).
  - The original combiner was replaced by a deferral stub; the original is kept as cert_combine45_orig.py.
- **Wall time:** 13.4 h, finishing 06:07.
  - BAR-A14 P3 (sealed 14-16.5 h): MISS, below the range because of the re-balance.
  - Inside the AMEND1 ETA of 12.8-14.5 h.
- No pause and no resume in this run.
- **BAR-A16** (10-29, after REFEREE-A45): PARI prediction first (a16_pred.gp, 41 grid points, 41 min on one core;
  instrument checked against the referee's 57-digit value at (12500, 1/2) to 1e-15), seal 07:58, run 1 core, 285 s for
  the box plus the refusal walk; scored HOLDS by score_a16.py (P1, P2, P3 and the count consistency). The largest-x
  positive control at t = 19/50 moves from x = 800 (BAR-A4-AMEND1 C3) to x = 12,500.

## Every assumption, stated
These are identical to THEOREM-A:
- MPFR 4.2.2 / MPC 1.4.0 correct rounding (gmpy2 2.3.1);
- float radii inflated, with libm exp/expm1/asin/sqrt within 1 ulp;
- mpmath 1.3.0 `iv` for the tail and the quadrature majorants;
- literature inputs: de Bruijn via Dobner Thm 3, Palojärvi-Zhao v1 Lemma 3.2 = v2 Lemma 3.3, DLMF 5.11,
  Trefethen-Weideman Thm 5.1, Kani 2010 and LMFDB 23.1.b.a;
- PARI only as a reference (in BAR-A16 it supplies the predicted count, never a certified step).

## Novelty and scope
- This is one L-function: L(s, eta(z)eta(23z)), primitive of degree 2 (the Artin L-function of the irreducible
  2-dimensional dihedral representation induced from the order-3 class-group character of Q(sqrt-23)).
- The bound is far weaker than what is known in degree 1: arXiv:2610.27343 (Freire, González-Riquelme, Muñoz, Poblete,
  Salinas, 19 Oct 2026; title checked with the arXiv API) proves Lambda_L <= 953/3200 = 0.2978125 for every primitive
  real character of conductor 3 to 400 (abstract read: Polymath-style effective approximation, Platt's GRH
  verification, interval arithmetic). Their method probably transfers to degree 2 and would likely give a much
  stronger bound here.
- No prior explicit bound below 1/2 for this form, or for any degree-2 L-function, was found at our search floor
  (the lead's prior-art refresh, LOG 04:18, and the second seat). We make no "first" claim beyond that search floor.
- Nothing here bears on the Riemann hypothesis itself.

## Hashes (sha256)
**Seals** (lines in rh-recon/LOG.md):

| seal | hash | sealed |
|---|---|---|
| BAR-A12 | 3d28430e…3fd63f | 16:26 |
| BAR-A13 | 0c103233…0101b2 | 16:28 |
| BAR-A12b | 27ded69a…261912 | 16:33 |
| BAR-A14 | 9b84d6e0…cb2636 | 16:43 |
| BAR-A14-AMEND1 | 1f052dbb…ddc530b | 17:42 |
| BAR-A16 | 9007c732…52d793 | 07:58 (10-29) |

**Code:**

| file | sha256 |
|---|---|
| tail_cert.py | 1441e756c8291387095e31d13a229224c74dad2ddae00a5644ba04f64036b7c7 |
| tail_run045.py | 360a442d82eb667270b2c83bc6137661cfbebb5af6d69897c9c6ee017cce6607 |
| tail_run045b.py | f4d5e085fe6681baeaa8e755f87440c9f31d68d5094270afbe1967da0b08e505 |
| cert_core.py | 3c5f7f2b4ff148c1b380f6da8022e7c29e565c08491895c04fd3a41d679836df |
| cert_wind_ckpt.py | 6ba1581587df3ac93ded24df94ab9032f367dce81ee6fc40cfc7bd84df58e22c |
| run_finite45.sh | dda7ba277d6d5a6ca7d02db32dce931ac26c5a39f95ab62d37b0ea0ffef5d2ba |
| run_pieces45.sh | de2d8e3bf5b688829fda23310e785f440dec3f72001619dd76e08d976ebcc100 |
| amend1_prepare45.py | ecacff4aaf1d4cd15f63d46c6210a7917ec329804acee6393d034d22f484cf00 |
| pieces45.txt | 5946a63a52b441fb863770c5da63928eef30fb471b9e8726ea690c84e8b57d69 |
| cert_combine45b.py | c23a3f3f9a4d4aa42dd5b8c6a3c90385392d341d002c314f6fe014f8e4f795d4 |
| a16_pred.gp | 49f55089d021830a327b6b792e2d151316ac6a4559fefdac15e6fd77232850f5 |
| run_a16.sh | 08d46af10e7764cd4acace486b64cb8614df1b582f55534069f11a4be4d3ac74 |
| score_a16.py | 58068e74cf2aec0337bc2268e7715475484ad641184220e1e610f925993db718 |

TAIL-LEMMA.md: the text sealed in BAR-A12 is ad7e96fd…; the current file is bd6c7183…, which adds only the N = 44
addendum. The A45 parameters are in TAIL-LEMMA-ADDENDUM-A45.md (e8cc75fa…54e69cc).

**Outputs:**

| file | sha256 |
|---|---|
| g45b_combine.json | fbb10d181dfe252471da9a0d1e966e53ea8ef3f97cef86ec877e30e5324aed04 |
| coverage_report_A14.json | e9e7897661c7bb2475bfcdac6c45c7eb44b60d53f1443104d7bc775943b4f1ee |
| tail_run045_out.json | 4368a0e0d7cc97f03c61857181e3e18d5cd8f7d7c16de5bc1486e25fffc48b50 (label "21/50" stale; runs 19/50) |
| tail_run045b_out.json | 2b295f153266413f0d3d711e582e80a7a4cbe237332dde8ebc1d56bad1747c79 (same) |
| a16_pred.txt | c8cffd5409ed975a8e043977e928b96cf114ff4977c41df760f17832545d3384 |
| a16_box.json | 1f5eb88b1b2905fcf2b0ce1d4cd23b3250bf6affeaa06313507280a0b79ab891 |
| a16_refuse.log | 929f0d5cf0336a0f9e67576eefbb8677919c5f0570625af16aeec52158a8a050 |
| a16_score.json | f9d46d7a02a47e546389a67051739002dc6eaecee761e176db82ff647f7f34c3 |

## Ceiling
- From 1/2 to 0.449938 in degree 2 for this one form.
- Going lower (e.g. 0.40) makes the tail start grow quickly: about 2.5·10^4 at t0 = 0.32 in the toy model. The
  finite-region cost grows like X^2, and doubles again at each power-of-two step of the quadrature grid.
- A non-dyadic step (h = 3·2^-m) and an effective approximate functional equation for the middle strip are the two
  levers; the degree-1 method of arXiv:2610.27343 is the obvious one to borrow.
