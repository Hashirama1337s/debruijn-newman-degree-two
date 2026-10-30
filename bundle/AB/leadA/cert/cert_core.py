"""cert_core.py -- certified (ball-arithmetic) evaluation of H_t(z) and its z-derivatives for
L(s, f), f = eta(z) eta(23 z)  (23.1.b.a), via the contour-shifted Fourier integral

    H_t(z) = int_R e^{t w^2} e^{i z w} Phi(w) dw   along  w = u + i*theta,
    Phi(w) = 2 e^{w} f(i e^{2w}/sqrt23)   (u >= 0),   Phi(w) = Phi(-w)  (used for u < 0).
Evenness (AMEND1, no outside source): from eta(-1/tau) = sqrt(-i tau) eta(tau),
    f(-1/(23 tau)) = eta(-1/(23tau)) eta(-1/tau) = sqrt(-i 23 tau) sqrt(-i tau) f(tau) = -i sqrt23 tau f(tau)
(principal roots; both arguments in (-pi/2, pi/2)). With tau(w) = i e^{2w}/sqrt23 one has -1/(23 tau(w)) = tau(-w), hence
Phi(-w) = 2 e^{-w} f(tau(-w)) = 2 e^{-w} (-i sqrt23 tau(w)) f(tau(w)) = 2 e^{w} f(tau(w)) = Phi(w).
Assumption stated (AMEND1): libm exp/expm1/asin/sqrt on floats are within 1 ulp (covered by the UP inflations);
all ball midpoints use MPFR/MPC (correctly rounded).

Normalisation: H_0(z) = xi((1+iz)/2), xi(s) = (sqrt23/2pi)^s Gamma(s) L(s) (Dobner arXiv:2005.05142 eq. (6)).

RIGOUR
- Balls: midpoint = gmpy2.mpc (MPC, correctly rounded per component, precision PREC bits), radius = Python float,
  every float radius computation inflated by UP = 1 + 2^-50 (covers <= 8 float roundings of 2^-53).
  Rounding of each MPC op bounded by EPS*|result|, EPS = 2^-(PREC-1).
- eta(tau): SL2(Z) reduction with the exact identities eta(tau+1) = e^{i pi/12} eta(tau),
  eta(-1/tau) = sqrt(-i tau) eta(tau) (principal root, Re(-i tau) = Im tau > 0), then the pentagonal series
  eta(tau) = sum_n (-1)^n q^{(n(3n-1)/2 + 1/24)}, q = e^{2 pi i tau}, |n| <= 4, tail <= 2|q|^{35}/(1-|q|) (Im tau >= 0.8).
- Trapezoid rule on the line Im w = theta with step h: error <= 2 M/(e^{2 pi d/h} - 1),
  M = sup_{|v - theta| <= d} int |g(u+iv)| du  (Trefethen-Weideman 2014, Thm 5.1), bounded from above by an
  upper Riemann sum in mpmath.iv of an explicit majorant, plus an explicit tail; truncation of the node sum to
  |u| <= U bounded the same way.
- Majorant of |f|: |f(tau)| <= C Im(tau)^{-1/2}, C = 23^{-1/4} S^2, S >= sup |eta(tau)| (Im tau)^{1/4}
  (SL2(Z)-invariant; on the fundamental domain |eta| <= e^{-pi y/12} exp(|q|/(1-|q|)), |q| <= e^{-pi sqrt3});
  and |f(tau)| <= sum d(n) r^n <= r/(1-r)^2, r = e^{-2 pi Im tau}  (|a_n| <= d(n)).
"""
import math
import gmpy2
from gmpy2 import mpc, mpfr
from mpmath import iv

PREC = 192
gmpy2.get_context().precision = PREC
EPS = 2.0 ** (-(PREC - 1))
UP = 1.0 + 2.0 ** -50
DN = 1.0 - 2.0 ** -50
iv.prec = 120

def fab(m):
    return float(abs(m)) * UP

def ball(m, r=0.0):
    return (mpc(m), float(r))

def badd(a, b):
    m = a[0] + b[0]
    return (m, (a[1] + b[1] + EPS * fab(m)) * UP)

def bsub(a, b):
    m = a[0] - b[0]
    return (m, (a[1] + b[1] + EPS * fab(m)) * UP)

def bneg(a):
    return (-a[0], a[1])

def bmul(a, b):
    m = a[0] * b[0]
    return (m, (fab(a[0]) * b[1] + fab(b[0]) * a[1] + a[1] * b[1] + EPS * fab(m)) * UP)

def bexp(a):
    m = gmpy2.exp(a[0])
    fm = fab(m)
    return (m, (fm * (1 + EPS) * math.expm1(a[1]) * UP + EPS * fm) * UP)

def brecip(a):
    alow = float(abs(a[0])) * DN
    if a[1] >= alow:
        raise ValueError("brecip: ball contains 0")
    m = 1 / a[0]
    den = alow * (alow - a[1]) * DN
    return (m, (a[1] / den * UP + EPS * fab(m)) * UP)

def bsqrt(a):
    # principal sqrt, requires Re > radius
    lowre = float(a[0].real) * DN - a[1]
    if lowre <= 0:
        raise ValueError("bsqrt: ball not in right half plane")
    m = gmpy2.sqrt(a[0])
    return (m, (a[1] / math.sqrt(lowre * DN) * UP + EPS * fab(m)) * UP)

# constants
PI = (mpc(gmpy2.const_pi()), EPS * 4)
I_B = ball(mpc(0, 1))
MINUS_I = ball(mpc(0, -1))
SQRT23 = (mpc(gmpy2.sqrt(mpfr(23))), EPS * 5 * 4.8)
INV_SQRT23 = brecip(SQRT23)
TWO_PI_I = bmul(ball(mpc(0, 2)), PI)
PI_I_12 = bmul(ball(mpc(0, 1)), bmul(PI, (mpc(1) / 12, EPS)))   # AMEND1: radius for the rounded 1/12
MULT = [bexp(bmul(ball(k), PI_I_12)) for k in range(24)]  # e^{i pi k/12}
EXPS = [(n, mpc(n * (3 * n - 1)) / 2 + mpc(1) / 24) for n in range(-4, 5)]
EXPS_RAD = [EPS * (1 + float(abs(e))) * 2 for _, e in EXPS]   # AMEND1: rounding of 1/24 etc.

def eta(tau):
    """ball enclosure of Dedekind eta(tau) for a ball tau in the upper half plane"""
    mult = ball(1)
    for _ in range(400):
        k = int(gmpy2.rint(tau[0].real))
        if k != 0:
            tau = bsub(tau, ball(k))
            mult = bmul(mult, MULT[k % 24])
        if float(abs(tau[0])) < 1.0 - 1e-12:
            if float(tau[0].imag) - tau[1] <= 0:
                raise ValueError("eta: Im tau not positive")
            s = bsqrt(bmul(MINUS_I, tau))         # sqrt(-i tau)
            mult = bmul(mult, brecip(s))          # eta(tau) = eta(-1/tau)/sqrt(-i tau)
            tau = bneg(brecip(tau))
        else:
            break
    else:
        raise RuntimeError("eta: reduction did not terminate")
    imlow = float(tau[0].imag) * DN - tau[1]
    if imlow < 0.8:
        raise RuntimeError("eta: reduced Im too small %g" % imlow)
    acc = None
    for (n, e), er in zip(EXPS, EXPS_RAD):
        term = bexp(bmul(bmul(TWO_PI_I, (e, er)), tau))
        if n % 2:
            term = bneg(term)
        acc = term if acc is None else badd(acc, term)
    # AMEND1: tail in MPFR with upward rounding (no float underflow); imlow is a lower bound of Im tau
    with gmpy2.local_context(gmpy2.get_context(), round=gmpy2.RoundDown):
        il = mpfr(imlow) * mpfr(DN)                     # lower bound of Im tau
        twopi_il_lo = 2 * gmpy2.const_pi() * il         # lower bound of 2 pi Im tau
    with gmpy2.local_context(gmpy2.get_context(), round=gmpy2.RoundUp):
        qa = gmpy2.exp(-twopi_il_lo)
        tail_m = 2 * qa ** 35
    with gmpy2.local_context(gmpy2.get_context(), round=gmpy2.RoundDown):
        den = 1 - qa
    with gmpy2.local_context(gmpy2.get_context(), round=gmpy2.RoundUp):
        tail_m = tail_m / den
    tail = math.nextafter(float(tail_m), math.inf)
    acc = (acc[0], (acc[1] + tail) * UP)
    return bmul(mult, acc)

def f23(tau):
    return bmul(eta(tau), eta(bmul(ball(23), tau)))

def Phi(w):
    # u >= 0 directly; u < 0 via Phi(w) = Phi(-w)
    if float(w[0].real) < 0:
        w = bneg(w)
    tau = bmul(bmul(I_B, bexp(bmul(ball(2), w))), INV_SQRT23)
    return bmul(bmul(ball(2), bexp(w)), f23(tau))

# ---------------- majorant integrals (mpmath.iv, real intervals) ----------------
S_ETA = None
def C_const():
    """C >= 23^{-1/4} S^2 with S >= sup |eta(tau)| Im(tau)^{1/4}"""
    y = iv.mpf(3) / iv.pi
    s = iv.exp(-iv.pi * y / 12) * y ** iv.mpf(0.25)          # max of e^{-pi y/12} y^{1/4} (at y = 3/pi >= sqrt3/2)
    q = iv.exp(-iv.pi * iv.sqrt(3))
    s = s * iv.exp(q / (1 - q))
    c = iv.mpf(23) ** iv.mpf(-0.25) * s * s
    return c.b  # upper endpoint

CBOUND = C_const()

def Fmaj(Y):
    """upper bound of |f(tau)| for Im tau in interval Y (>0)"""
    b1 = CBOUND / iv.sqrt(Y)
    r = iv.exp(-2 * iv.pi * Y)
    b2 = r / (1 - r) ** 2
    return min(b1.b, b2.b)

def majorant_integral(t, vlo, vhi, xfac, ymax, j, umax, cosmin, cell=0.01):
    """Upper bound of int_R (|u|+vhi)^j e^{t(u^2 - vlo^2)} e^{xfac} e^{ymax|u|} 2 e^{|u|} F(e^{2|u|} cosmin/sqrt23) du.
    xfac: exponent (float, already an upper bound) for the e^{x(...)} scaling. Returns float upper bound."""
    tot = iv.mpf(0)
    n = int(math.ceil(umax / cell))
    sq23 = iv.sqrt(23)
    cm = iv.mpf(cosmin)
    for k in range(n):
        uc = iv.mpf([k * cell, (k + 1) * cell])
        Y = iv.exp(2 * uc) * cm / sq23
        F = Fmaj(Y)
        val = (uc + vhi) ** j * iv.exp(t * (uc * uc - iv.mpf(vlo) ** 2) + ymax * uc + uc) * 2 * F
        tot += iv.mpf(val.b) * (iv.mpf(uc.b) - iv.mpf(uc.a))
    tot = 2 * tot  # both signs of u
    # tail |u| > umax: log-derivative <= 2 t u + ymax + 1 + j/u - 4 pi Y(u) (from the r/(1-r)^2 majorant)
    U = iv.mpf(umax)
    Yu = iv.exp(2 * U) * cm / sq23
    kappa = (4 * iv.pi * Yu - 2 * t * U - ymax - 1 - iv.mpf(j) / U).a
    if kappa < 1:
        raise RuntimeError("majorant tail: umax too small")
    r = iv.exp(-2 * iv.pi * Yu)
    Bt = (U + vhi) ** j * iv.exp(t * (U * U - iv.mpf(vlo) ** 2) + ymax * U + U) * 2 * (r / (1 - r) ** 2)
    tot += 2 * iv.mpf(Bt.b) / iv.mpf(kappa)
    return float((tot * iv.exp(iv.mpf(xfac))).b) * UP * UP

# ---------------- block (fixed contour) ----------------
class Block:
    """Fixed contour for points with 0 <= Re z <= xb, |Im z| <= ymax. Holds node data and error bounds."""
    def __init__(self, tnum, tden, xb, ymax, K=12, c=10.0, rc=1.5, target_rel=1e-12, Hlow=0.01):
        self.xb, self.ymax, self.K, self.rc = xb, ymax, K, rc
        t = iv.mpf(tnum) / tden
        self.t_iv = t
        self.tf = tnum / tden
        self.t_ball = (mpc(mpfr(gmpy2.mpq(tnum, tden))), EPS * 2)
        xe = max(xb, 20.0)
        self.delta = min(c / xe, 0.125)
        dlt = mpfr(self.delta)
        self.theta = bsub(bmul(PI, ball(mpc(1) / 4)), ball(mpc(2 * dlt)))
        th = float(self.theta[0].real)
        d = self.delta
        # node range: majorant negligible beyond U
        cosmin = math.sin(2 * d) * DN  # cos(2(theta+d)) = sin(2 delta) (theta+d = pi/4 - delta)
        self.U = self._choose_U(self.tf, cosmin, ymax, K)
        # quadrature-error majorants M_j (scaled by e^{x theta}: factor e^{x(theta - v)} <= e^{xb d})
        self.Mq = [majorant_integral(t, th - d, th + d, xb * d, ymax, j, self.U + 0.5, cosmin) for j in range(K + 1)]
        # target: absolute (scaled) error <= target_rel * Hlow * e^{-2 delta xb}
        tgt = target_rel * Hlow * math.exp(-2 * self.delta * xb)
        E = math.log(2 * max(self.Mq) / tgt + 1)
        hmax = 2 * math.pi * d / E
        m = math.ceil(-math.log2(hmax))
        self.h = 2.0 ** (-m)                      # dyadic step, exact
        self.qerr = [2 * Mj / math.expm1(2 * math.pi * d / self.h) * UP for Mj in self.Mq]
        # node-sum truncation: nodes |u| <= U; tail of the infinite sum <= int_{U-h}^inf (both sides) of majorant
        self.terr = [self._tail(t, th, d, xb, ymax, j, cosmin) for j in range(K + 1)]
        # Cauchy majorant for Taylor remainder: contour theta' = pi/4 - delta', delta' = 1/xe (<= 1/8)
        self.dp = min(1.0 / xe, 0.125)
        thp = math.pi / 4 - self.dp
        cosp = math.sin(2 * self.dp) * DN
        Up = self._choose_U(self.tf, cosp, ymax + rc, 0)
        self.Icauchy = majorant_integral(t, thp * DN, thp, 0.0, ymax + rc, 0, Up + 0.5, cosp)
        self.thp = thp
        self._build_nodes()

    def _choose_U(self, t, cosmin, ymax, j):
        U = 1.0
        while True:
            Y = math.exp(2 * U) * cosmin / math.sqrt(23)
            if 4 * math.pi * Y - 2 * t * U - ymax - 1 - j / U > 3 and 2 * math.pi * Y > 2 * t * U * U + 3 * ymax * U + 3 * U + 80:
                return U
            U += 0.25

    def _tail(self, t, th, d, xb, ymax, j, cosmin):
        # sum over nodes |u_k| > U of h*|g|  <=  int_{|u| > U - h} majorant  (majorant decreasing there)
        U = iv.mpf(self.U - self.h)
        Yu = iv.exp(2 * U) * iv.mpf(cosmin) / iv.sqrt(23)
        kappa = (4 * iv.pi * Yu - 2 * t * U - ymax - 1 - iv.mpf(j) / U).a
        if kappa < 1:
            raise RuntimeError("node tail: U too small")
        r = iv.exp(-2 * iv.pi * Yu)
        Bt = (U + th + d) ** j * iv.exp(t * U * U + ymax * U + U + iv.mpf(xb * d)) * 2 * (r / (1 - r) ** 2)
        return float((2 * iv.mpf(Bt.b) / iv.mpf(kappa)).b) * UP * UP

    def _build_nodes(self):
        K = self.K
        nst = int(math.ceil(self.U / self.h))
        self.n_nodes = 2 * nst + 1
        hb = ball(mpc(mpfr(self.h)))
        tb = self.t_ball
        self.Wi = []     # i*w_k  (balls)
        self.Bm = []     # per node: list of midpoints of A_k (i w_k)^j
        self.Bf = []     # per node: |midpoint| floats
        self.Br = []     # per node: radii
        thb = self.theta
        for k in range(-nst, nst + 1):
            w = badd(ball(mpc(mpfr(k) * mpfr(self.h))), bmul(I_B, thb))
            A = bmul(hb, bmul(bexp(bmul(tb, bmul(w, w))), Phi(w)))
            iw = bmul(I_B, w)
            self.Wi.append(iw)
            ms, fs, rs = [], [], []
            cur = A
            for j in range(K + 1):
                ms.append(cur[0]); fs.append(fab(cur[0])); rs.append(cur[1])
                cur = bmul(cur, iw)
            self.Bm.append(ms); self.Bf.append(fs); self.Br.append(rs)

    def evaluate(self, z):
        """z: ball with 0 <= Re z <= xb, |Im z| <= ymax. Returns list of balls for e^{x theta_mid}-scaled
        H^{(j)}(z), j = 0..K, and the scale exponent x*theta (as float, informational)."""
        K = self.K
        S = [mpc(0)] * (K + 1)
        R = [0.0] * (K + 1)
        absum = [0.0] * (K + 1)
        # scaled kernel: e^{i z w} e^{x theta_mid}, x = Re z mid (exact on our grids)
        xs = ball(mpc(z[0].real))
        shift = bmul(xs, ball(self.theta[0].real))   # x*theta (real ball)
        for k in range(self.n_nodes):
            e = bexp(badd(bmul(z, self.Wi[k]), shift))
            em, er = e
            fe = fab(em)
            ms, fs, rs = self.Bm[k], self.Bf[k], self.Br[k]
            for j in range(K + 1):
                S[j] += ms[j] * em
                a = fs[j] * fe
                absum[j] += a
                R[j] += fs[j] * er + fe * rs[j] + rs[j] * er + EPS * a
        n = self.n_nodes
        fsum = 1.0 + (n + 4) * 2.0 ** -52   # AMEND1: round-to-nearest float sums over n terms
        R = [r * fsum for r in R]
        absum = [a * fsum for a in absum]
        # theta radius: shift uses theta midpoint only; true scaling factor is e^{x theta_mid} exactly -> no error
        out = []
        sc = math.exp(0.0)
        for j in range(K + 1):
            rad = (R[j] * UP + (2 * n + 2) * EPS * absum[j] + self.qerr[j] * self._scalefix(z) + self.terr[j] * self._scalefix(z)) * UP
            out.append((S[j], rad))
        return out

    def _scalefix(self, z):
        # qerr/terr were computed for scaling e^{x(theta - v)} with x <= xb (uses e^{xb d}); the scaled
        # quantity here is e^{x theta_mid}*H; theta_mid vs theta radius is ~1e-57 -> factor <= 1 + 1e-50
        return 1.0 + 1e-40

    def cauchy_bound(self, x):
        """upper bound of e^{x theta_mid} * sup_{|xi - p| <= rc} |H(xi)| for Re p = x, |Im p| <= ymax"""
        th = float(self.theta[0].real)
        expo = x * th - (x - self.rc) * self.thp
        return self.Icauchy * math.exp(expo) * UP * UP
