"""coverage_report45.py -- writes the BAR-A14 coverage report: for each boundary edge, the sorted list of intervals
contributed by each walk (name, interval) and whether they tile the edge exactly once. Usage: py coverage_report45.py OUT"""
import json, sys
from fractions import Fraction as Fr
X, Y0, Y1 = Fr(12500), Fr(374, 1000), Fr(1, 2)
base = ["g45_b%d" % k for k in range(1, 10)] + ["g45_t1", "g45_t2", "g45_t5"]
pieces = [l.split()[0] for l in open("pieces45.txt") if l.strip()]
edges = {"bottom": [], "top": [], "right": [], "left": []}
missing = []
for n in base + pieces:
    try:
        r = json.load(open(n + ".json"))
    except FileNotFoundError:
        missing.append(n); continue
    P = [tuple(Fr(c) for c in p.split(",")) for p in r["path"].split(";")]
    for (xa, ya), (xb, yb) in zip(P, P[1:]):
        if ya == yb == Y0 and xb > xa: edges["bottom"].append((xa, xb, n))
        elif ya == yb == Y1 and xb < xa: edges["top"].append((xb, xa, n))
        elif xa == xb == X: edges["right"].append((ya, yb, n))
        elif xa == xb == 0: edges["left"].append((yb, ya, n))
out = {"missing": missing, "edges": {}}
for e, lo, hi in [("bottom", 0, X), ("top", 0, X), ("right", Y0, Y1), ("left", Y0, Y1)]:
    iv = sorted(edges[e])
    ok = bool(iv) and iv[0][0] == lo and iv[-1][1] == hi and all(iv[i][1] == iv[i + 1][0] for i in range(len(iv) - 1))
    gaps = [[str(iv[i][1]), str(iv[i + 1][0])] for i in range(len(iv) - 1) if iv[i][1] != iv[i + 1][0]]
    out["edges"][e] = dict(tiles_exactly_once=ok, n_intervals=len(iv), gaps_or_overlaps=gaps,
                           intervals=[[str(a), str(b), n] for a, b, n in iv])
out["all_ok"] = (not missing) and all(v["tiles_exactly_once"] for v in out["edges"].values())
json.dump(out, open(sys.argv[1], "w"), indent=1)
print("all_ok", out["all_ok"], "missing", missing, {e: (v["tiles_exactly_once"], v["n_intervals"], v["gaps_or_overlaps"]) for e, v in out["edges"].items()})
