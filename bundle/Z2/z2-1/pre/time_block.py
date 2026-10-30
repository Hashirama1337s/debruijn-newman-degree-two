"""Pre-seal instrument timing (not scored): cert_core Block build + one evaluate, K = 0, at a NON-grid point.
Prints only timings, node count and relative radius; no comparison with any main term."""
import sys, time, math
sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "../../../AB/leadA/cert"))
import gmpy2
from gmpy2 import mpc, mpfr, mpq
import cert_core as cc
xb = float(sys.argv[1]); xp = mpq(sys.argv[2]); yp = mpq(sys.argv[3])
t0 = time.time()
blk = cc.Block(1, 4, xb, 0.9, K=0, c=30.0)
t1 = time.time()
z = (mpc(mpfr(xp), mpfr(yp)), cc.EPS * 4 * (xb + 1))
val = blk.evaluate(z)[0]
t2 = time.time()
print("xb", xb, "nodes", blk.n_nodes, "h", blk.h, "build_s %.1f" % (t1 - t0), "eval_s %.1f" % (t2 - t1),
      "rel_radius %.3e" % (val[1] / float(abs(val[0]))))
