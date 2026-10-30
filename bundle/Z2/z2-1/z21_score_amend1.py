"""z21_score_amend1.py -- BAR-Z2-1-AMEND1 scorer (parser fix only; bars unchanged). Reads ref1.txt (degree-1 PARI control) and ref2.jsonl (degree-2 certified
evaluator), computes the main terms (z21_core.py) and e = |H_t/B_t - f_t|, applies the sealed bars, writes
z21_score.json. Deterministic post-processing; no new reference data."""
import sys, json, math, statistics
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import mpmath as mp
import z21_core as zc

mp.mp.dps = 50
res = dict(points=[], control=[], verdict={})

# ---------- degree-1 positive control ----------
a1 = zc.coeffs_chim4(200)
G1 = zc.Deg1(4, 1)
ctrl_ok = True
for line in open("ref1.txt"):
    p = line.replace(" E", "E").split()   # AMEND1: PARI prints mantissa and exponent separated by a space
    if len(p) != 4:
        res.setdefault("control_notes", []).append(line.strip()); continue
    x, y = mp.mpf(mp.fraction(*map(int, p[0].split("/"))) if "/" in p[0] else p[0]), \
        mp.mpf(mp.fraction(*map(int, p[1].split("/"))) if "/" in p[1] else p[1])
    H = mp.mpc(mp.mpf(p[2]), mp.mpf(p[3]))
    f, lB, M = zc.main_term(G1, a1, x, y, mp.mpf(1) / 10)
    e = abs(H * mp.exp(-lB) - f)
    bnd = zc.eps66(4, 2, x, y, mp.mpf(1) / 10)
    res["control"].append(dict(x=float(x), y=float(y), M=M, absf=float(abs(f)), e=float(e), eps66=float(bnd)))
c = res["control"]
C1 = len(c) == 10 and all(r["e"] <= r["eps66"] for r in c)
f0 = [r for r in c if abs(r["x"] - 1000) < 1e-9 and abs(r["y"] - 0.9) < 1e-9]
C2 = len(f0) == 1 and 1.4 <= f0[0]["absf"] <= 1.8
e9 = [r["e"] for r in c if abs(r["y"] - 0.9) < 1e-9]
C3 = len(e9) == 5 and statistics.median(e9) <= 0.05
res["verdict"]["P0"] = dict(C1_e_le_eps66=C1, C2_absf_1000=C2, C3_median_e_y09_le_005=C3, holds=C1 and C2 and C3)

# ---------- degree 2 ----------
recs = [json.loads(l) for l in open("ref2.jsonl")]
Mmax = 80000
a23 = zc.coeffs_23(Mmax)
a31 = zc.coeffs_31(Mmax)
G23, G92 = zc.Deg2(23), zc.Deg2(92)
for r in recs:
    x = mp.mpf(r["x"][0]) / r["x"][1]; y = mp.mpf(r["y"][0]) / r["y"][1]; t = mp.mpf(r["t"][0]) / r["t"][1]
    val = mp.mpc(mp.mpf(r["re"]), mp.mpf(r["im"])); th = mp.mpf(r["theta_mid"])
    rel_rad = r["rad"] / float(abs(val))
    f, lB, M = zc.main_term(G23, a23, x, y, t)
    R = val * mp.exp(-x * th - lB)                     # H_t / B_t
    e = abs(R - f)
    fN1, _, _ = zc.main_term(G23, a31, x, y, t)
    eN1 = abs(R - fN1)
    fN2, lB92, M92 = zc.main_term(G92, a23, x, y, t)
    eN2 = abs(val * mp.exp(-x * th - lB92) - fN2)
    res["points"].append(dict(xc=r["xc"], t=float(t), x=float(x), y=float(y), M=M, rel_rad=rel_rad,
                              absR=float(abs(R)), absf=float(abs(f)), e=float(e), eN1=float(eN1), eN2=float(eN2)))
P = res["points"]
def sel(xc, t, y=None):
    return [p for p in P if p["xc"] == xc and abs(p["t"] - t) < 1e-12 and (y is None or abs(p["y"] - y) < 1e-12)]
void = [p for p in P if not p["rel_rad"] < 1e-6]
res["verdict"]["void_points"] = len(void)
# P1: viability at x_c = 10450, t = 1/4
p1 = sel(10450, 0.25)
res["verdict"]["P1"] = dict(n=len(p1), max_e=max(p["e"] for p in p1) if p1 else None,
                            holds=len(p1) == 10 and max(p["e"] for p in p1) <= 0.15)
# P2: decay of the median e with M at t = 1/4
med = {xc: (statistics.median([p["e"] for p in sel(xc, 0.25)]) if len(sel(xc, 0.25)) == 10 else None)
       for xc in (2000, 5000, 10450, 31400)}
P2 = None not in (med[2000], med[10450], med[31400]) and med[31400] < med[10450] < med[2000]
res["verdict"]["P2"] = dict(medians=med, holds=P2)
# nulls on x_c >= 10450 (all t)
big = [p for p in P if p["xc"] >= 10450]
etrue_med = statistics.median([p["e"] for p in big]) if big else None
fr1 = sum(p["eN1"] >= 0.03 for p in big) / len(big) if big else 0
mN1 = statistics.median([p["eN1"] for p in big]) if big else 0
N1 = len(big) >= 30 and fr1 >= 0.8 and mN1 >= 3 * etrue_med
fr2 = sum(p["eN2"] >= 0.3 for p in big) / len(big) if big else 0
N2 = len(big) >= 30 and fr2 >= 0.8
res["verdict"]["N1"] = dict(frac_ge_003=fr1, median_eN1=mN1, median_e_true=etrue_med, null_separated=N1)
res["verdict"]["N2"] = dict(frac_ge_03=fr2, null_separated=N2)
# reported only
res["verdict"]["R_t010_vs_t025_at_10450"] = dict(
    median_t010=statistics.median([p["e"] for p in sel(10450, 0.1)]) if sel(10450, 0.1) else None,
    median_t025=med[10450])
r100 = sel(100000, 0.25)
res["verdict"]["R_100000"] = dict(n=len(r100), e=[p["e"] for p in r100], M=[p["M"] for p in r100])
# slope of log(median e) vs log M (reported)
pts = [(statistics.median([p["M"] for p in sel(xc, 0.25)]), statistics.median([p["e"] for p in sel(xc, 0.25)]))
       for xc in (2000, 5000, 10450, 31400, 100000) if sel(xc, 0.25)]
if len(pts) >= 2:
    lx = [math.log(a) for a, b in pts]; ly = [math.log(b) for a, b in pts]
    mx, my = sum(lx) / len(lx), sum(ly) / len(ly)
    res["verdict"]["R_slope_logE_logM"] = sum((u - mx) * (v - my) for u, v in zip(lx, ly)) / sum((u - mx) ** 2 for u in lx)
v = res["verdict"]
v["MAIN"] = ("HOLDS" if (v["P0"]["holds"] and v["P1"]["holds"] and v["P2"]["holds"] and N1 and N2 and not void)
             else "FAILED")
json.dump(res, open("z21_score_amend1.json", "w"), indent=1)
print(json.dumps(v, indent=1))
