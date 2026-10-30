"""check44.py -- calibration (not sealed): N = 44 certified enclosures vs PARI references (refs44.txt)."""
import sys
sys.path.insert(0, ".")
import gmpy2
from gmpy2 import mpc, mpfr, mpq
from cert_core44 import *

ok = True
for line in open("refs44.txt"):
    raw = line.split(); p = []
    for tok in raw:
        if tok.startswith("E") and p:
            p[-1] += tok
        else:
            p.append(tok)
    if p[0] not in ("H0", "GA"):
        continue
    x = int(p[1]); y = mpq(p[2])
    tn, td = (0, 1) if p[0] == "H0" else (21, 50)
    ref = mpc(mpfr(p[3]), mpfr(p[4]))
    xb = 100 if x <= 100 else (800 if x <= 800 else 3000)
    b = Block(tn, td, xb, 0.5, c=30.0)
    out = b.evaluate((mpc(mpfr(x), mpfr(y)), EPS * 4 * (1 + x)))
    sc = gmpy2.exp(mpfr(x) * b.theta[0].real)
    err = float(abs(out[0][0] - ref * sc))
    tol = 1e-20 if p[0] == "GA" else 1e-45
    inside = err <= out[0][1] + tol * float(abs(ref * sc))
    ok &= inside
    print(p[0], x, p[2], "rel.rad %.2e" % (out[0][1] / float(abs(out[0][0]))), "|mid-ref|/|H| %.2e" % (err / float(abs(out[0][0]))), "inside", inside, flush=True)
print("ALL INSIDE", ok)
