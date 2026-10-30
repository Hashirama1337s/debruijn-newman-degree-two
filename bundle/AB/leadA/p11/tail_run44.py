"""tail_run.py -- BAR-A6 decisive run of TAIL-LEMMA.md (t = 21/50, eps = 1/5, y in [0.374, 0.4], x >= 7200).
Parts:
  A. adaptive T-boxes covering [3600, 1e12] (T = x/2), 8 y-subboxes each; widths double on success, halve on failure.
  B. Step 10 asymptotic check at T1 = 1e12 (all T >= T1), with the vertex (monotonicity) conditions.
  C. cross-check: certified lower bound |gamma(S0)| * margin <= |H| enclosed by the certified evaluator (x = 7200).
Writes tail_run_out.json and tail_run.log (JSONL of boxes)."""
import sys, time, json, math
sys.path.insert(0, ".")
from mpmath import iv
from tail_cert44 import box_margin, Bup, LOGQ, PI, loggamma_abs   # p = 11, N = 44

TN, TD, EN, ED = 21, 50, 1, 5
YLO, YHI = 0.374, 0.4
YS = [YLO + (YHI - YLO) * k / 8 for k in range(9)]
T_START, T1 = 1400.0, 1e12   # p = 11: x >= 2800
out = {"params": dict(t="21/50", eps="1/5", y=[YLO, YHI], x_start=2 * T_START, T1=T1)}
t0 = time.time()
logf = open("tail_run.log", "w")

# ---------- A. boxes ----------
T = T_START; w = 1 / 1024; nbox = 0; minrel = 1e9; ok = True
while T < T1:
    Th = min(T * (1 + w), T1)
    lows = []
    good = True
    for i in range(8):
        m, why = box_margin(TN, TD, EN, ED, T, Th, YS[i], YS[i + 1], N=4000)
        if m is None or not m.a > 0:
            good = False; break
        lows.append(float(m.a))
    if good:
        nbox += 1
        logf.write(json.dumps({"T": T, "Th": Th, "min_low": min(lows)}) + "\n"); logf.flush()
        T = Th; w = min(w * 2, 0.5)
    else:
        w /= 2
        if w < 2 ** -16:
            ok = False
            out["A_fail"] = dict(T=T, why=str(why))
            break
out["A"] = dict(ok=ok, boxes=nbox, reached_T=T, secs=time.time() - t0)
print("A:", out["A"], flush=True)

# ---------- B. asymptotic check at T1 ----------
t = iv.mpf(TN) / TD; eps = iv.mpf(EN) / ED
T1i = iv.mpf(T1)
Lam = iv.log(iv.sqrt(44) / (2 * PI) * T1i) / 2
delta = 1 / (T1i * T1i)
c1 = (1 / T1i ** 2 + PI / T1i) / 8
a0 = 1 / (4 * t); a = a0 - c1
kappa = 4 * t * c1 / (1 - 4 * t * c1)
K0 = iv.exp(t * iv.mpf(0.79) ** 2)
vA_max = 1 + 2 * eps - YLO; vA_min = 1 + 2 * eps - YHI
vB_max = 1 + YHI + 2 * eps; vB_min = 1 + YLO + 2 * eps
rho = iv.exp(-2 * YLO * Lam + 1 / T1i)
B1e = iv.mpf(Bup(math.nextafter(float((1 + eps).a), -math.inf)))   # AMEND2: sigma rounded down
sq4pt = iv.sqrt(4 * PI * t)
kfac = iv.sqrt(a0 / a) * iv.exp(t * kappa * (Lam + delta) ** 2)
P1 = K0 * iv.exp(-(2 * t * (Lam - delta) - vA_max) ** 2 / (4 * t)) / (((Lam - delta) - 2 * a0 * vA_max) * sq4pt)
P2 = K0 * (kfac - 1)
sig3 = (1 + YLO) / 2 + t * (Lam - delta) / 2
P3 = K0 * kfac * (iv.mpf(Bup(math.nextafter(float(sig3.a), -math.inf))) - 1)
P4 = K0 * iv.exp(-a * vA_min ** 2 + (Lam + delta) * vA_max - t * (Lam - delta) ** 2) / (2 * a * vA_min * sq4pt) * B1e
sig5 = (1 - YHI) / 2 + t * (Lam - delta) / 2
P5 = K0 * rho * kfac * iv.exp(4 * t * Lam * delta) * iv.mpf(Bup(math.nextafter(float(sig5.a), -math.inf)))
P6 = K0 * rho * iv.exp(-a * vB_min ** 2 + (Lam + delta) * vB_max - t * (Lam - delta) ** 2) / (2 * a * vB_min * sq4pt) * B1e
P7 = K0 * rho * B1e * 2 * (1 + 2 * eps) / sq4pt * iv.exp((Lam + delta) * vB_max + 2 * Lam * (1 + 2 * eps) - t * (Lam - delta) ** 2) \
     * (1 + 25 / T1i ** 2) ** ((1 + 2 * eps) / 2)
lhs = 1 - P1 - P2
rhs = P3 + P4 + P5 + P6 + P7
vert = {  # monotone-decreasing conditions (Lam - delta must exceed each vertex)
    "P1": max(float((vA_max / (2 * t)).b), float((2 * a0 * vA_max).b)),
    "P4": float(((vA_max + 2 * t * delta) / (2 * t)).b),
    "P6": float((vB_max / (2 * t)).b),
    "P7": float(((vB_max + 2 * (1 + 2 * eps) - 2 * YLO) / (2 * t)).b),
    "sig3>1": 1.0, "sig5>1": 1.0,
}
vert_ok = all(float((Lam - delta).a) > v for k, v in vert.items() if not k.startswith("sig")) and sig3.a > 1 and sig5.a > 1
B_ok = bool((lhs - rhs).a > 0) and vert_ok
out["B"] = dict(ok=B_ok, Lam=float(Lam.a), lhs_low=float(lhs.a), rhs_high=float(rhs.b),
                parts={k: float(v.b) for k, v in dict(P1=P1, P2=P2, P3=P3, P4=P4, P5=P5, P6=P6, P7=P7).items()}, vertices=vert)
print("B:", out["B"], flush=True)

# ---------- C. cross-check with the certified evaluator at x = 7200, y = 0.374 ----------
sys.path.insert(0, ".")
import gmpy2
from gmpy2 import mpc, mpfr, mpq
import cert_core44 as cc
x0, y0 = 2800, mpq(374, 1000)
blk = cc.Block(TN, TD, 2800, 0.5, c=30.0)
val = blk.evaluate((mpc(mpfr(x0), mpfr(y0)), cc.EPS * 4 * 2801))[0]
logH_lo = math.log(float(abs(val[0])) * cc.DN - val[1]) - float(mpfr(x0) * blk.theta[0].real) - 1e-12
m, _ = box_margin(TN, TD, EN, ED, 1400.0, 1400.0, YLO, YLO, N=4000)
Tq = iv.mpf(1400); yq = iv.mpf(YLO)
log_gS0 = (1 + yq) / 2 * LOGQ + loggamma_abs((1 + yq) / 2, Tq)
logLB_hi = float((log_gS0 + iv.log(m)).b)
out["C"] = dict(ok=logLB_hi <= logH_lo, log_lower_bound=logLB_hi, log_H_certified_low=logH_lo)
print("C:", out["C"], flush=True)

out["HOLDS"] = bool(out["A"]["ok"] and out["B"]["ok"] and out["C"]["ok"])
out["secs"] = time.time() - t0
json.dump(out, open("tail_run_out.json", "w"), indent=1)
print("BAR-A6 =>", "HOLDS" if out["HOLDS"] else "FAILED", "secs %.0f" % out["secs"])
