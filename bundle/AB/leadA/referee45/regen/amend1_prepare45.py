"""amend1_prepare45.py -- BAR-A14-AMEND1 setup (run once, after sealing).
1. Marks the not-yet-started top chunks g45_t3, t4, t6, t7, t8, t9 as SUPERSEDED: a checkpoint stub with done = 10**9
   makes cert_wind_ckpt.py skip every sub-segment, so each worker's top walk exits at once (argsum 0, 0 points) and the
   worker's core is freed. The AMEND1 combiner EXCLUDES these six names and checks they did no work.
2. Writes pieces45.txt: the top-edge (y = 1/2) ranges [5900, 8325] and [9325, 12500] cut into pieces of about equal
   estimated work (100-unit pieces below x = 10700, 50-unit pieces above, where the dyadic quadrature step halves),
   ordered by decreasing x (largest cost first). Each piece is walked right -> left like the original tops.
"""
import json, os

SUPERSEDED = ["g45_t3", "g45_t4", "g45_t6", "g45_t7", "g45_t8", "g45_t9"]
for n in SUPERSEDED:
    ck = n + ".ckpt.jsonl"
    if os.path.exists(ck) or os.path.exists(n + ".log"):
        raise SystemExit("refusing: %s already started" % n)
    with open(ck, "w") as fh:
        fh.write(json.dumps({"done": 10 ** 9, "argsum": "0", "argrad": 0.0, "nsum": 0, "npts": 0, "secs": 0.0,
                             "end": ["SUPERSEDED", "BAR-A14-AMEND1"]}) + "\n")

pieces = []
def cut(a, b, step):
    x = a
    while x < b:
        y = min(x + step, b)
        pieces.append((x, y)); x = y
cut(5900, 8300, 100); pieces.append((8300, 8325))
pieces.append((9325, 9400)); cut(9400, 10700, 100); cut(10700, 12500, 50)
pieces.sort(key=lambda p: -p[1])
with open("pieces45.txt", "w") as fh:
    for a, b in pieces:
        fh.write("g45_q%05d_%05d %d %d\n" % (a, b, a, b))
print("superseded:", SUPERSEDED, " pieces:", len(pieces))
