# TAIL-LEMMA addendum A45 - the parameters used by THEOREM-A45 (t = 19/50, y in [0.374, 0.49])

Written 2026-10-29 for REFEREE-A45 fix (1a), release blocker. TAIL-LEMMA.md (sha256 bd6c7183...) is not edited: its
text is stated for THEOREM-A (t = 21/50, y in [0.374, 0.4], x >= 7200, Step 10 numbers at t = 0.42). This addendum
states what changes for THEOREM-A45 and re-derives every Step 10 number.

## In plain words
The lemma's proof never used t = 0.42 or y <= 0.4 except as the parameter values plugged in at the end. For
THEOREM-A45 the same proof is run with the heat time 0.38 and with heights y up to 0.49, from x = 12,500 on. The final
inequality at the far end still holds with a wide margin (0.17 against 1), and the monotonicity conditions still hold.
The numbers below were recomputed from the lemma's formulas by a separate script, not copied from the run.

## Parameters (replacing the Notation line "Parameters")
- t = 19/50, eps = 1/5, y in [0.374, 0.49], x = 2T >= 12500 (T >= 6250). Run as two sealed parts:
  - BAR-A12, tail_run045.py: 6500 <= T <= 10^12 (x >= 13000), 16 y-subboxes, 202 boxes, plus Step 10 at T1 = 10^12;
  - BAR-A12b, tail_run045b.py: 6250 <= T <= 6500 (x in [12500, 13000]), 32 y-subboxes, 8 boxes, no Step 10 part.
- The y-range endpoints are the floats 0.374 and 0.49: float(0.374) = 3368692521273131/2^53 < 374/1000 (the tail
  reaches slightly below the theorem's edge), and float(0.49) > sqrt6/5 = 0.4898979... (0.49^2 = 0.2401 > 0.24), the
  de Bruijn edge at t = 0.38.
- Everything else in Notation is unchanged (q, gamma, xi, w(v), v_A = y - 1 - 2 eps, v_B = 1 + y + 2 eps, a0, c, a).

## Steps 1-9
Unchanged. Each identity there holds for every y in (0, 1) and every t > 0; the two exponent identities that fix the
tails, (1+y)/2 - v_A/2 = 1 + eps (Step 6) and (1-y)/2 + v_B/2 = 1 + eps (Step 7), do not depend on y. Where a step
takes "the worst end" of the y-range, the code takes it at the A45 range (rho at y_lo, P5 at y_hi, P3 at y_lo).

## Step 10 at the A45 parameters (T1 = 10^12)
Re-derived by tail/addendum_a45_check.py (re-typed from the Step 10 text; only B(sigma) of Step 9 is imported) and
compared with tail_run045_out.json part B. Output: tail/addendum_a45_check_out.txt - ALL AGREE.

| quantity | formula (Step 10) | re-derived | run (tail_run045_out.json) |
|---|---|---|---|
| Lam(T1) | (1/2) log(q T1) | 13.6804455787 | 13.6804455787 |
| K0 | e^{t 0.79^2}, t = 19/50 | 1.26764 | (same formula, line 52) |
| vertex P1 | max(\|v_A\|max/(2t), 2 a0 \|v_A\|max) = 1.026/0.76 | 1.35 | 1.35 |
| vertex P4 | (\|v_A\|max + 2t delta)/(2t) | 1.35 | 1.35 |
| vertex P6 | v_B,max/(2t) = 1.89/0.76 | 2.48684 | 2.48684 |
| vertex P7 | (v_B,max + 2(1+2eps) - 2 y_lo)/(2t) = 3.942/0.76 | 5.18684 | 5.18684 |
| P1 | TM | 3.81e-27 | 3.81e-27 |
| P2 | TAY | 5.42e-11 | 5.42e-11 |
| P3 | E_A, log n <= 2A | 0.1697685 | 0.1697685 |
| P4 | E_A, log n > 2A | 1.70e-25 | 1.70e-25 |
| P5 | E_B, log n <= 2B | 5.436e-05 | 5.436e-05 |
| P6 | E_B, log n > 2B | 9.28e-26 | 9.28e-26 |
| P7 | E_M | 2.078e-07 | 2.078e-07 |
| 1 - P1 - P2 (lower end) | | 0.999999999946 | 0.999999999946 |
| P3 + ... + P7 (upper end) | | **0.1698231** | 0.16982309583 |

- All four vertices (1.35, 1.35, 2.49, 5.19) are below Lam(T1) - delta = 13.68, so every e^{-t Lam^2 + p Lam} factor
  decreases for T >= T1. The arguments of B are sig3 = 3.286 and sig5 = 2.854, both > 1.
- So 1 - P1 - P2 >= 0.99999999994 > 0.1698 >= P3 + ... + P7 for all T >= T1 = 10^12 at t = 19/50,
  y in [0.374, 0.49].
- At t = 21/50, y in [0.374, 0.4] (THEOREM-A) the vertices were 1.22, 1.22, 2.14, 4.59 and the sum 0.1396; these are
  the TAIL-LEMMA.md figures and are unchanged.

## K0 and |Im alpha| <= 0.79 (t-independent)
- alpha = -g'(S0)/2 with g' = log q + psi and S0 = (1+y)/2 - iT; t does not enter alpha, so the bound |Im alpha| <= 0.79
  carries over unchanged. Only K0 = e^{t 0.79^2} changes, through t, and the code evaluates it at t = 19/50.
- Check (mpmath digamma, 200 bits): |Im alpha| = 0.78539816339735 (y = 0.374, T = 10^12), 0.78539816339733
  (y = 0.49, T = 10^12), 0.78539816339745 (y = 0.374, T = 10^15); pi/4 = 0.78539816339745. All <= 0.79. (This is a
  float check of the stated bound, which follows from Im psi(z) = arg z + O(1/T) with |arg z| < pi/2.)

## Finite boxes (part A) and cross-check (part C)
- Part A is computed for the actual y-subboxes and t by box_margin(19, 50, 1, 5, ...); nothing in it was carried over
  from t = 21/50. Results: 202 boxes, x in [13000, 2·10^12], tightest margin 0.781; 8 boxes, x in [12500, 13000],
  tightest margin 0.829 at T about 6295-6345 (tail_run045b.log).
- Part C: at x = 12500, y = 0.374 the certified lower bound log -9811.62 sits below the certified log|H| -9808.4056;
  the referee's independent PARI value there is -9808.4053 (referee45/job3.out), consistent.

## Stale label in the run outputs (REFEREE-A45 fix (1b))
tail_run045_out.json and tail_run045b_out.json show `"t": "21/50"`. Line 16 of tail_run045.py and tail_run045b.py,
`out = {"params": dict(t="21/50", eps="1/5", y=[YLO, YHI], x_start=2 * T_START, T1=T1)}`, was copied unchanged from
tail_run.py, so it is absent from the diff, while the parameter used by the code changed:

    $ diff tail_run.py tail_run045.py
    12,15c12,15
    < TN, TD, EN, ED = 21, 50, 1, 5
    ...
    > TN, TD, EN, ED = 19, 50, 1, 5

The run therefore used t = 19/50 (box_margin(TN, TD, ...) in part A; t = TN/TD in part B). The outputs themselves
confirm it: their vertex P1 = 1.026/(2t) is 1.35, which is t = 0.38 (t = 0.42 gives 1.2214), and the re-derivation at
t = 19/50 reproduces every part-B number above. The hashed outputs stay as they are; read their label as 19/50.

## Hashes (sha256)
| file | sha256 |
|---|---|
| TAIL-LEMMA.md (not edited) | bd6c71831561226e677db189a4dcea0a0031ede5aa6828398fdbe0ffc212d938 |
| tail_cert.py | 1441e756c8291387095e31d13a229224c74dad2ddae00a5644ba04f64036b7c7 |
| tail_run045.py | 360a442d82eb667270b2c83bc6137661cfbebb5af6d69897c9c6ee017cce6607 |
| tail_run045b.py | f4d5e085fe6681baeaa8e755f87440c9f31d68d5094270afbe1967da0b08e505 |
| tail_run045_out.json | 4368a0e0d7cc97f03c61857181e3e18d5cd8f7d7c16de5bc1486e25fffc48b50 |
| tail_run045b_out.json | 2b295f153266413f0d3d711e582e80a7a4cbe237332dde8ebc1d56bad1747c79 |
| addendum_a45_check.py | a83f54fd3940371a70b973ac5a42fbb9cca25c4e12ef80af9dd5528e005230da |
| addendum_a45_check_out.txt | 7653c32c606742a79f35a6c016c3bcaefcb73c98d2f84910c08da1f39ebe7c9a |
