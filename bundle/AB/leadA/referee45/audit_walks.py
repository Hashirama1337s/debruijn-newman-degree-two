import json, os, sys, re
from fractions import Fraction as Fr
from decimal import Decimal, getcontext
getcontext().prec = 80
D = sys.argv[1]
os.chdir(D)
base = ["g45_b%d" % k for k in range(1, 10)] + ["g45_t1", "g45_t2", "g45_t5"]
pieces = [l.split() for l in open("pieces45.txt") if l.strip()]
names = base + [p[0] for p in pieces]
sup = ["g45_t3", "g45_t4", "g45_t6", "g45_t7", "g45_t8", "g45_t9"]
CH = Fr(25)
def subs_of(path):
    P = [tuple(Fr(c) for c in p.split(",")) for p in path.split(";")]
    subs = []
    for (xa, ya), (xb, yb) in zip(P, P[1:]):
        if ya == yb:
            lo, hi = min(xa, xb), max(xa, xb)
            m = (lo // CH + 1) * CH; inner = []
            while m < hi: inner.append(m); m += CH
            cuts = [xa] + (inner if xb > xa else inner[::-1]) + [xb]
            subs += list(zip(cuts, cuts[1:]))
        else:
            subs.append(((xa,), (xb,)))
    return P, subs
tot = Decimal(0); rad = 0.0; pts = 0; probs = []
edges = {"bottom": [], "top": [], "right": [], "left": []}
builds = {}
for n in names:
    r = json.load(open(n + ".json"))
    if r["t"] != "19/50" or r["c"] != 30.0: probs.append((n, "t/c", r["t"], r["c"]))
    P, subs = subs_of(r["path"])
    ck = [json.loads(l) for l in open(n + ".ckpt.jsonl") if l.strip()]
    dones = [c["done"] for c in ck]
    if dones != list(range(1, len(subs) + 1)): probs.append((n, "ckpt chain", dones[:3], len(dones), len(subs)))
    if ck[-1]["argsum"] != r["argsum"] or ck[-1]["npts"] != r["points"]: probs.append((n, "ckpt/json mismatch"))
    # each subsegment adds >=2 points
    np_prev = 0
    for c in ck:
        if c["npts"] - np_prev < 2: probs.append((n, "subseg with <2 pts", c["done"]))
        np_prev = c["npts"]
    log = open(n + ".log").read()
    if "resuming" in log: probs.append((n, "resumed"))
    ex = re.findall(r"^exit (\d+)", log, re.M)
    if ex != ["0"]: probs.append((n, "exits", ex))
    for m in re.finditer(r"BUILD xb=(\d+) nodes=(\d+)", log):
        builds[int(m.group(1))] = int(m.group(2))
    if n == "g45_q11000_11050" or n == "g45_q12450_12500" or n=="g45_b1":
        print(n, r["path"], "points", r["points"], "argsum", r["argsum"][:20], "argrad", r["argrad"])
    tot += Decimal(r["argsum"]); rad += r["argrad"]; pts += r["points"]
    X, Y0, Y1 = Fr(12500), Fr(374, 1000), Fr(1, 2)
    for (xa, ya), (xb, yb) in zip(P, P[1:]):
        if ya == yb == Y0 and xb > xa: edges["bottom"].append((xa, xb, n))
        elif ya == yb == Y1 and xb < xa: edges["top"].append((xb, xa, n))
        elif xa == xb == X and ya == Y0 and yb == Y1: edges["right"].append((ya, yb, n))
        elif xa == xb == 0 and ya == Y1 and yb == Y0: edges["left"].append((yb, ya, n))
        else: probs.append((n, "bad seg", (xa, ya), (xb, yb)))
for e, lo, hi in [("bottom", 0, 12500), ("top", 0, 12500), ("right", Fr(374,1000), Fr(1,2)), ("left", Fr(374,1000), Fr(1,2))]:
    iv = sorted(edges[e])
    ok = iv[0][0] == lo and iv[-1][1] == hi and all(iv[i][1] == iv[i+1][0] for i in range(len(iv)-1))
    print(e, len(iv), ok)
for n in sup:
    r = json.load(open(n + ".json")); ck = open(n + ".ckpt.jsonl").read().strip().splitlines(); log = open(n + ".log").read()
    print(n, r["points"], r["argsum"], len(ck), "BUILD" in log, "sub-segment" in log.replace("resuming after sub-segment",""))
import math
w = tot / (2 * Decimal("3.14159265358979323846264338327950288419716939937510582097494459"))
print("walks", len(names), "points", pts, "winding value", w, "rad", rad, "rad/2pi", rad/(2*math.pi))
print("problems", probs)
print("builds (xb:nodes) around 10700:", {k: v for k, v in sorted(builds.items()) if 10400 <= k <= 11000})
print("node count jumps:", [(k, v) for (k, v), (k0, v0) in zip(sorted(builds.items())[1:], sorted(builds.items())) if v > 1.5 * v0])
