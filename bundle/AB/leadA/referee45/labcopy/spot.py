import sys, math, time
sys.path.insert(0, ".")
import gmpy2
from gmpy2 import mpc, mpfr, mpq
import cert_core as cc
pts = [(int(a), mpq(b)) for a, b in (p.split(",") for p in sys.argv[1:])]
for x, y in pts:
    t0 = time.time()
    xb = next(b for b in [25, 50] + list(range(100, 200001, 50)) if b >= x)
    blk = cc.Block(19, 50, xb, 0.5, c=30.0)
    z = (mpc(mpfr(x), mpfr(y)), cc.EPS * 4 * (1 + x + float(y)))
    v = blk.evaluate(z)[0]
    sc = mpfr(x) * blk.theta[0].real
    m = v[0]
    logabs = gmpy2.log(abs(m)) - sc
    print("x=%d y=%s xb=%d nodes=%d h=2^%d  logH=%.12f arg=%.15f relrad=%.3e  re=%s im=%s  secs=%.0f" % (
        x, y, xb, blk.n_nodes, round(math.log2(blk.h)), float(logabs), float(gmpy2.phase(m)), v[1] / float(abs(m)),
        gmpy2.mpfr(m.real * gmpy2.exp(-sc)).__format__('.20e'), gmpy2.mpfr(m.imag * gmpy2.exp(-sc)).__format__('.20e'), time.time() - t0), flush=True)
