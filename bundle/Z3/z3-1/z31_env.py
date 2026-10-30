"""z31_env.py -- BAR-Z3-1 "crude envelope sufficiency" (design: Z2/IDEAS-Z3.md, section 'Smallest first step').

E(x,y,t;K) = sum_{n in (M - K sqrt M, M + K sqrt M]} |a_n| b_n (n^{-Re s*+} + |gamma| n^{-Re s*-})
with s*+-, gamma, b_n, M exactly as Z2-1: definitions imported unchanged from Z2/z2-1/z21_core.py (Deg2(23), Deg1(4,1),
logMt, alpha, M). a_n from AB/leadA/tail/tail_cert.coeffs(), cross-checked against z21_core.coeffs_23.
Measured e at the shared points: Z2/z2-1/run2/z21_score_amend1.json (points, control). Pure arithmetic, 1 core.
Output: z31_out.json + verdict lines on stdout.
"""
import sys, os, json, math
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "Z2", "z2-1"))
sys.path.insert(0, os.path.join(ROOT, "AB", "leadA", "tail"))
import numpy as np
import mpmath as mp
import z21_core as zc
import tail_cert

KS = (2, 3)
TS = [(0, 1), (1, 10), (1, 4), (7, 25)]          # t in {0, 1/10, 1/4, 0.28}
YS = [(1, 10), (3, 20), (1, 5), (9, 10)]         # y in {0.1, 0.15, 0.2, 0.9}
HALF = [0, 0.5, 1, 1.5, 2]
XGRID = [(xc, [xc + h for h in HALF]) for xc in (2000, 5000, 10450, 31400)] + [(100000, [100000, 100001])]


def envelope(G, a, x, y, t, K):
    x, y, t = mp.mpf(x), mp.mpf(y), mp.mpf(t)
    sp = (1 + y - 1j * x) / 2
    sm = (1 - y + 1j * x) / 2
    M = G.M(x, t)
    lBp, lBm = zc.logMt(G, sp, t), zc.logMt(G, sm, t)
    absgam = float(abs(mp.exp(lBm - lBp)))
    rsp = float(mp.re(sp + t / 2 * G.alpha(sp)))
    rsm = float(mp.re(sm + t / 2 * G.alpha(sm)))
    lo = int(math.floor(M - K * math.sqrt(M))) + 1
    hi = int(math.floor(M + K * math.sqrt(M)))
    lo = max(lo, 1)
    if hi >= len(a):
        raise ValueError("coefficient array too short")
    n = np.arange(lo, hi + 1, dtype=np.float64)
    ln = np.log(n)
    bn = np.exp(float(t) / 4 * ln * ln)
    w = np.abs(a[lo:hi + 1]) * bn
    E = float(np.sum(w * (np.exp(-rsp * ln) + absgam * np.exp(-rsm * ln))))
    return E, M, lo, hi, absgam


def main():
    G23 = zc.Deg2(23)
    NMAX = 40000
    a_tc = np.asarray(tail_cert.coeffs(NMAX), dtype=np.float64)
    a_zc = zc.coeffs_23(NMAX)
    assert np.array_equal(a_tc, a_zc), "coefficient sources disagree"
    a = a_tc
    G1 = zc.Deg1(4, 1)
    a1 = zc.coeffs_chim4(200)
    z21 = json.load(open(os.path.join(ROOT, "Z2", "z2-1", "run2", "z21_score_amend1.json")))
    out = dict(points=[], control=[], verdict={})
    for xc, xs in XGRID:
        for x in xs:
            for (tn, td) in TS:
                for (yn, yd) in YS:
                    rec = dict(xc=xc, x=x, t=tn / td, y=yn / yd)
                    for K in KS:
                        E, M, lo, hi, ag = envelope(G23, a, x, mp.mpf(yn) / yd, mp.mpf(tn) / td, K)
                        rec["E%d" % K] = E
                        rec["M"], rec["absgam"] = M, ag
                        rec["win%d" % K] = [lo, hi]
                    out["points"].append(rec)
    # shared points with Z2-1
    shared = []
    for p in z21["points"]:
        q = [r for r in out["points"] if abs(r["x"] - p["x"]) < 1e-9 and abs(r["y"] - p["y"]) < 1e-12 and abs(r["t"] - p["t"]) < 1e-12]
        assert len(q) == 1, ("shared point not found", p["x"], p["y"], p["t"])
        assert q[0]["M"] == p["M"], ("M mismatch", p, q[0]["M"])
        shared.append(dict(x=p["x"], y=p["y"], t=p["t"], M=p["M"], e=p["e"], E2=q[0]["E2"], E3=q[0]["E3"]))
    out["shared"] = shared
    # degree-1 positive control (chi_-4, t = 1/10, the Z2-1 control points)
    for c in z21["control"]:
        E3, M, lo, hi, ag = envelope(G1, a1, c["x"], mp.mpf(c["y"]), mp.mpf(1) / 10, 3)
        E2, _, _, _, _ = envelope(G1, a1, c["x"], mp.mpf(c["y"]), mp.mpf(1) / 10, 2)
        assert M == c["M"]
        out["control"].append(dict(x=c["x"], y=c["y"], M=M, e=c["e"], E3=E3, E2=E2, win3=[lo, hi]))
    P = out["points"]
    p1 = [r for r in P if r["xc"] == 10450 and abs(r["t"] - 0.25) < 1e-12]
    nul = [r for r in P if r["xc"] == 10450 and r["t"] == 0 and r["y"] <= 0.2 + 1e-12]
    V = out["verdict"]
    V["P1"] = dict(n=len(p1), max_E3=max(r["E3"] for r in p1), holds=all(r["E3"] <= 0.05 for r in p1),
                   max_E3_by_y={str(y): max(r["E3"] for r in p1 if abs(r["y"] - y) < 1e-12) for y in (0.1, 0.15, 0.2, 0.9)})
    V["P2"] = dict(n=len(shared), holds=all(s["E3"] >= s["e"] for s in shared),
                   min_ratio_E3_over_e=min(s["E3"] / s["e"] for s in shared),
                   n_E2_ge_e=sum(1 for s in shared if s["E2"] >= s["e"]))
    V["N"] = dict(n=len(nul), min_E3=min(r["E3"] for r in nul), holds=all(r["E3"] >= 0.5 for r in nul),
                  E3_t0_y09_xc10450=[r["E3"] for r in P if r["xc"] == 10450 and r["t"] == 0 and abs(r["y"] - 0.9) < 1e-12])
    cc = out["control"]
    V["PC"] = dict(n=len(cc), holds=len(cc) == 10 and all(c["E3"] >= c["e"] for c in cc),
                   min_ratio=min(c["E3"] / c["e"] for c in cc))
    V["MAIN"] = "HOLDS" if (V["PC"]["holds"] and V["P1"]["holds"] and V["P2"]["holds"]) else "SEE BARS"
    # reported: max E3 per (xc, t) over y >= 0.1 and per y
    rep = {}
    for xc, _ in XGRID:
        for (tn, td) in TS:
            for (yn, yd) in YS:
                rr = [r for r in P if r["xc"] == xc and abs(r["t"] - tn / td) < 1e-12 and abs(r["y"] - yn / yd) < 1e-12]
                rep["%d|%s|%s" % (xc, "%d/%d" % (tn, td), "%d/%d" % (yn, yd))] = [max(r["E3"] for r in rr), max(r["E2"] for r in rr), rr[0]["M"]]
    out["report_maxE3_maxE2_M"] = rep
    json.dump(out, open(os.path.join(HERE, "z31_out.json"), "w"), indent=1)
    for k in ("PC", "P1", "P2", "N", "MAIN"):
        print(k, V[k], flush=True)


if __name__ == "__main__":
    main()
