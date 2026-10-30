"""cert_combine3.py -- BAR-A11 scoring (p = 11): total certified winding of H_{21/50} around [0,2800] x [0.374, 0.41]."""
import json, math
import gmpy2
from gmpy2 import mpfr
gmpy2.get_context().precision = 192
names = ["fin_b%d" % k for k in range(1, 10)] + ["fin_t%d" % k for k in range(9, 0, -1)]
tot = mpfr(0); rad = 0.0; pts = 0; secs = 0.0; missing = []
for n in names:
    try:
        r = json.load(open(n + ".json"))
    except FileNotFoundError:
        missing.append(n); continue
    tot += mpfr(r["argsum"]); rad += r["argrad"]; pts += r["points"]; secs = max(secs, r["secs"])
rad *= 1 + 1e-15
w = tot / (2 * gmpy2.const_pi())
n = round(float(w))
cert = (not missing) and abs(float(w) - n) + rad / (2 * math.pi) < 0.5
res = dict(winding=n, value=float(w), radius=rad, certified=cert, missing=missing, points=pts, max_chunk_secs=secs,
           holds=cert and n == 0)
print(res)
print("BAR-A11 MAIN =>", "HOLDS" if res["holds"] else "FAILED")
json.dump(res, open("fin_combine.json", "w"), indent=1)
