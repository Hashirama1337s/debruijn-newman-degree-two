"""cert_combine45b.py -- BAR-A14-AMEND1 scoring with an exact coverage check.
Walks used: bottoms g45_b1..b9 (b9 includes the right edge), original tops g45_t1 (incl. left edge), g45_t2, g45_t5,
and all pieces in pieces45.txt. Superseded tops g45_t3,t4,t6..t9 are excluded and must show 0 points.
Coverage check: every walk's path is split into axis-parallel segments; bottom pieces (y = 374/1000, oriented +x),
top pieces (y = 1/2, oriented -x), right side (x = 12500, up) and left side (x = 0, down) must each tile their edge
exactly once (sorted, contiguous, no overlap, no gap). Only then is the winding sum (each walk's continuous arg change)
the arg change around the closed boundary."""
import json, math
from fractions import Fraction as Fr
import gmpy2
from gmpy2 import mpfr
gmpy2.get_context().precision = 192

X, Y0, Y1 = Fr(12500), Fr(374, 1000), Fr(1, 2)
base = ["g45_b%d" % k for k in range(1, 10)] + ["g45_t1", "g45_t2", "g45_t5"]
pieces = [l.split()[0] for l in open("pieces45.txt") if l.strip()]
superseded = ["g45_t3", "g45_t4", "g45_t6", "g45_t7", "g45_t8", "g45_t9"]
names = base + pieces
res = {"missing": [], "superseded_ok": True}
tot = mpfr(0); rad = 0.0; pts = 0
segs = {"bottom": [], "top": [], "right": [], "left": []}
for n in names:
    try:
        r = json.load(open(n + ".json"))
    except FileNotFoundError:
        res["missing"].append(n); continue
    tot += mpfr(r["argsum"]); rad += r["argrad"]; pts += r["points"]
    P = [tuple(Fr(c) for c in p.split(",")) for p in r["path"].split(";")]
    for (xa, ya), (xb, yb) in zip(P, P[1:]):
        if ya == yb == Y0 and xb > xa:
            segs["bottom"].append((xa, xb))
        elif ya == yb == Y1 and xb < xa:
            segs["top"].append((xb, xa))
        elif xa == xb == X and ya == Y0 and yb == Y1:
            segs["right"].append((ya, yb))
        elif xa == xb == 0 and ya == Y1 and yb == Y0:
            segs["left"].append((yb, ya))
        else:
            res.setdefault("bad_segments", []).append([n, str((xa, ya)), str((xb, yb))])
for n in superseded:
    r = json.load(open(n + ".json")) if __import__("os").path.exists(n + ".json") else None
    if r is None or r["points"] != 0 or mpfr(r["argsum"]) != 0:
        res["superseded_ok"] = False

def tiles(iv, lo, hi):
    iv = sorted(iv)
    if not iv or iv[0][0] != lo or iv[-1][1] != hi:
        return False
    return all(iv[i][1] == iv[i + 1][0] for i in range(len(iv) - 1))

cov = {"bottom": tiles(segs["bottom"], Fr(0), X), "top": tiles(segs["top"], Fr(0), X),
       "right": tiles(segs["right"], Y0, Y1), "left": tiles(segs["left"], Y0, Y1)}
coverage_ok = all(cov.values()) and "bad_segments" not in res
rad *= 1 + 1e-15
w = tot / (2 * gmpy2.const_pi()); n = round(float(w))
cert = (not res["missing"]) and coverage_ok and abs(float(w) - n) + rad / (2 * math.pi) < 0.5
res.update(dict(winding=n, value=float(w), radius=rad, coverage=cov, coverage_ok=coverage_ok, certified=cert,
                walks=len(names), points=pts, holds=bool(cert and n == 0 and res["superseded_ok"])))
print(res)
print("BAR-A14 MAIN (AMEND1 combine) =>", "HOLDS" if res["holds"] else "FAILED")
json.dump(res, open("g45b_combine.json", "w"), indent=1, default=str)
