"""cert_wind_ckpt.py -- checkpointable version of cert_wind.py (same certified step logic, AMEND1 fixes included).
Usage: py -3.11 -I cert_wind_ckpt.py <name> <tnum> <tden> <ymax> <path> [c=10] [chunk=25]
The axis-parallel path is cut into sub-segments at multiples of <chunk> along horizontal edges. After each
sub-segment the running enclosure (argsum, argrad, points) is appended to <name>.ckpt.jsonl; a restart skips the
completed sub-segments and resumes from the last certified endpoint. Final JSON <name>.json as in cert_wind.py.
Each sub-segment's start point is re-evaluated, so the arg chain is continuous across restarts (ratios telescope).
"""
import sys, json, time, math, os
sys.path.insert(0, ".")
import gmpy2
from gmpy2 import mpc, mpfr, mpq
from cert_core import *

name, tn, td, ymax = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(mpq(sys.argv[4]))
path = [tuple(mpq(c) for c in pt.split(",")) for pt in sys.argv[5].split(";")]
CPAR = float(sys.argv[6]) if len(sys.argv) > 6 else 10.0
CHUNK = mpq(sys.argv[7]) if len(sys.argv) > 7 else mpq(25)
XB = [25, 50] + list(range(100, 200001, 50))
blocks = {}

def block_for(x):
    xb = next(b for b in XB if b >= x)
    if xb not in blocks:
        for k in [k for k in blocks if k < xb - 50]:   # free blocks no longer needed
            del blocks[k]
        tb0 = time.time()
        blocks[xb] = Block(tn, td, xb, max(ymax, 0.5), c=CPAR)
        print("BUILD xb=%d nodes=%d secs=%.1f" % (xb, blocks[xb].n_nodes, time.time() - tb0), flush=True)
    return blocks[xb]

def zball(x, y):
    return (mpc(mpfr(x), mpfr(y)), EPS * 4 * (1 + abs(float(x)) + abs(float(y))))

def evalp(x, y):
    b = block_for(float(x))
    return b, b.evaluate(zball(x, y))

K = 12
FACT = [math.factorial(j) for j in range(K + 2)]

def ok_step(b, out, x, s):
    S0 = out[0]
    hlow = (float(abs(S0[0])) * DN - S0[1]) * DN
    if hlow <= 0:
        return False, hlow
    T = 0.0
    for j in range(1, K + 1):
        T += (fab(out[j][0]) + out[j][1]) * s ** j / FACT[j]
    Mc = b.cauchy_bound(max(float(x) * DN, 0.0) if float(x) > 0 else float(x) * UP)
    T += Mc * (s / b.rc) ** (K + 1) / (1 - s / b.rc)
    T *= UP * UP
    return T < 0.98 * hlow, hlow

# cut path into sub-segments
subs = []
for seg in range(len(path) - 1):
    (xa, ya), (xb_, yb) = path[seg], path[seg + 1]
    if ya == yb:
        cuts = [xa]
        lo, hi = min(xa, xb_), max(xa, xb_)
        m = (lo // CHUNK + 1) * CHUNK
        inner = []
        while m < hi:
            inner.append(m); m += CHUNK
        cuts += (inner if xb_ > xa else inner[::-1]) + [xb_]
        for i in range(len(cuts) - 1):
            subs.append(((cuts[i], ya), (cuts[i + 1], ya)))
    else:
        assert xa == xb_
        subs.append(((xa, ya), (xb_, yb)))

ck = name + ".ckpt.jsonl"
done = 0; argsum = mpfr(0); argrad = 0.0; nsum = 0; npts = 0; secs0 = 0.0
if os.path.exists(ck):
    lines = [json.loads(l) for l in open(ck) if l.strip()]
    if lines:
        last = lines[-1]
        done, argsum, argrad, nsum, npts, secs0 = last["done"], mpfr(last["argsum"]), last["argrad"], last["nsum"], last["npts"], last["secs"]
        print("resuming after sub-segment", done, flush=True)
t0 = time.time()
s = 1 / 64
for idx in range(done, len(subs)):
    (xa, ya), (xb_, yb) = subs[idx]
    horiz = (ya == yb)
    L = abs(xb_ - xa) if horiz else abs(yb - ya)
    sgn = 1 if ((xb_ > xa) if horiz else (yb > ya)) else -1
    pos = mpq(0); cx, cy = xa, ya
    b, cur = evalp(cx, cy); npts += 1
    while pos < L:
        s = min(s * 2, 1 / 2)
        while True:
            sq = min(mpq(s), L - pos)
            s_cert = float(sq) * UP + 2 * zball(cx, cy)[1]
            good, hlow = ok_step(b, cur, cx, s_cert)
            if good:
                break
            s = s / 2
            if s < 2 ** -24:
                raise RuntimeError("cannot certify step at (%s, %s): hlow=%g" % (cx, cy, hlow))
        pos += sq
        nx, ny = (xa + sgn * pos, ya) if horiz else (xa, ya + sgn * pos)
        b2, nxt = evalp(nx, ny); npts += 1
        ratio = bmul(nxt[0], brecip(cur[0]))
        m = ratio[0]
        rel = ratio[1] / (float(abs(m)) * DN)
        if rel >= 0.5:
            raise RuntimeError("ratio enclosure too wide at (%s,%s)" % (nx, ny))
        a = gmpy2.phase(m)
        if abs(float(a)) >= math.pi / 2:
            raise RuntimeError("principal arg step >= pi/2 inconsistent with cone condition")
        argsum += a
        argrad += (math.asin(rel) * UP + 1e-50)
        nsum += 1
        b, cur, cx, cy = b2, nxt, nx, ny
    with open(ck, "a") as fh:
        fh.write(json.dumps({"done": idx + 1, "argsum": str(argsum), "argrad": argrad, "nsum": nsum, "npts": npts,
                             "secs": secs0 + time.time() - t0, "end": [str(xb_), str(yb)]}) + "\n")
    print("sub-segment %d/%d done, end (%s, %s), points %d, time %.0fs" % (idx + 1, len(subs), float(xb_), float(yb), npts, secs0 + time.time() - t0), flush=True)

argrad_tot = argrad * (1 + (nsum + 4) * 2.0 ** -52)
res = {"name": name, "t": "%d/%d" % (tn, td), "path": sys.argv[5], "c": CPAR, "argsum": str(argsum), "argrad": argrad_tot,
       "points": npts, "secs": secs0 + time.time() - t0}
json.dump(res, open(name + ".json", "w"), indent=1)
print("DONE", name, "argsum", float(argsum), "+-", argrad_tot, "points", npts)
