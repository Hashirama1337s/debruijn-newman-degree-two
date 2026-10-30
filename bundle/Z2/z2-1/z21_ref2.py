"""z21_ref2.py -- BAR-Z2-1 degree-2 reference values H_t(x+iy) for L(s, eta(z)eta(23z)) from the lab's certified
evaluator AB/leadA/cert/cert_core.py (sha256 3c5f7f2b..., unchanged, imported read-only), K = 0, c = 30, ymax = 0.9,
one Block per (x_c, t) with xb = x_c + 2. Stores the scaled ball e^{x theta_mid} H (midpoint, radius) and theta_mid.
No main term is computed here. Output: ref2.jsonl (one JSON line per point, flushed), in the sealed grid order."""
import sys, time, json
sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "../../AB/leadA/cert"))
import gmpy2
from gmpy2 import mpc, mpfr, mpq
import cert_core as cc

def fmt(v):
    return "{:.55e}".format(v)

# sealed grid: (x_c, (tnum, tden), xs as (num, den), ys as (num, den))
HALF = [(0, 1), (1, 2), (1, 1), (3, 2), (2, 1)]
Y2 = [(1, 5), (9, 10)]
GRID = [
    (2000, (1, 4), HALF, Y2),
    (5000, (1, 4), HALF, Y2),
    (10450, (1, 4), HALF, Y2),
    (10450, (1, 10), HALF, Y2),
    (31400, (1, 4), HALF, Y2),
    (100000, (1, 4), [(0, 1), (1, 1)], Y2),
]
out = open("ref2.jsonl", "a")
T0 = time.time()
for xc, (tn, td), xs, ys in GRID:
    tb = time.time()
    blk = cc.Block(tn, td, xc + 2, 0.9, K=0, c=30.0)
    build = time.time() - tb
    th = blk.theta[0].real
    for (xn, xd) in xs:
        for (yn, yd) in ys:
            te = time.time()
            x = mpq(xc) + mpq(xn, xd)
            y = mpq(yn, yd)
            z = (mpc(mpfr(x), mpfr(y)), cc.EPS * 4 * (xc + 3))
            v = blk.evaluate(z)[0]
            rec = dict(xc=xc, t=[tn, td], x=[int(x.numerator), int(x.denominator)], y=[yn, yd],
                       re=fmt(v[0].real), im=fmt(v[0].imag), rad=v[1], theta_mid=fmt(th),
                       nodes=blk.n_nodes, build_s=round(build, 1), eval_s=round(time.time() - te, 1),
                       elapsed_s=round(time.time() - T0, 1))
            out.write(json.dumps(rec) + "\n"); out.flush()
            print(json.dumps(rec)[:160], flush=True)
    del blk
print("REF2 DONE elapsed %.0f" % (time.time() - T0), flush=True)
