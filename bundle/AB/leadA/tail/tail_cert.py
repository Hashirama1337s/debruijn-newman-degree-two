"""tail_cert.py -- interval-arithmetic (mpmath.iv) check of the right-tail inequality of TAIL-LEMMA.md:

    Mlow - EA - rho*(EB + EM) > 0   for all (T, y) in a box,   T = x/2,

which implies H_t(x+iy) != 0 (Lemma T). Every quantity is an iv enclosure; only exp, log, sqrt, cos and the four
arithmetic operations of mpmath.iv are used (outward rounded). arg/atan by an alternating series with remainder.
psi and log|Gamma| by Stirling with the DLMF 5.11(ii) remainder bounds (sec^{2n+1} and sec^{2n} factors, n = 1).
Usage as a module: box_margin(t, eps, T_lo, T_hi, y_lo, y_hi) -> iv lower bound of the normalised margin.
"""
import math, sys
import numpy as np
from mpmath import iv, mpf
iv.prec = 110

# ---------------- coefficients |a_n| (exact integers) and Euler-product bound B(sigma) ----------------
def coeffs(M):
    def reps(A, B, C):
        r = np.zeros(M + 1, dtype=np.int64)
        ymax = int(math.isqrt(4 * A * M // (4 * A * C - B * B))) + 2
        for yv in range(-ymax, ymax + 1):
            disc = B * B * yv * yv - 4 * A * (C * yv * yv - M)
            if disc < 0:
                continue
            s = math.isqrt(disc) + 2
            xs = np.arange((-B * yv - s) // (2 * A) - 1, (-B * yv + s) // (2 * A) + 2, dtype=np.int64)
            v = A * xs * xs + B * xs * yv + C * yv * yv
            v = v[(v >= 1) & (v <= M)]
            r += np.bincount(v, minlength=M + 1)
        return r
    r0, r1 = reps(1, 1, 6), reps(2, 1, 3)
    assert np.all((r0 - r1) % 2 == 0)
    return (r0 - r1) // 2

PMAX = 2_000_000
_A = coeffs(PMAX)
assert list(_A[1:9]) == [1, -1, -1, 0, 0, 1, 0, 1] and _A[23] == 1 and _A[59] == 2
ABSA = np.abs(_A)

def primes_upto(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if s[p]:
            s[p * p::p] = False
    return np.nonzero(s)[0]
PRIMES = primes_upto(PMAX)

def B_upper(sigma):
    """upper bound of sum |a_n| n^-sigma = prod_p e_p(sigma) (|a_n| multiplicative)."""
    sg = iv.mpf(sigma)
    prod = iv.mpf(1)
    for p in PRIMES:
        p = int(p)
        u = iv.mpf(p) ** (-sg)
        ap = int(_A[p])
        if p == 23:
            e = 1 / (1 - u)
        elif ap == 0:                 # inert
            e = 1 / (1 - u * u)
        elif ap == 2:                 # split, principal prime ideals: a_{p^k} = k+1
            e = 1 / (1 - u) ** 2
        elif ap == -1:                # split, non-principal: |a_{p^k}| = 1,1,0 periodic
            e = (1 + u) / (1 - u ** 3)
        else:
            raise ValueError("unexpected a_p %d at p=%d" % (ap, p))
        prod = prod * e
    # primes > PMAX: e_p <= (1-p^-s)^-2; sum_{p>P} -log(1-p^-s) <= (1/(1-P^-s)) sum_{m odd > P} m^-s
    #                                                           <= (1/(1-P^-s)) (P-1)^{1-s}/(2(s-1))
    P = iv.mpf(PMAX)
    tail = (P - 1) ** (1 - sg) / (2 * (sg - 1)) / (1 - P ** (-sg))
    return (prod * iv.exp(2 * tail)).b

# ---------------- elementary helpers ----------------
def atan_small(u):
    """atan(u) for an interval |u| <= 1/2: alternating series to 30 terms + remainder bound."""
    s = iv.mpf(0)
    term = u
    u2 = u * u
    for k in range(30):
        s += term / (2 * k + 1) * (1 if k % 2 == 0 else -1)
        term = term * u2
    rem = abs(term).b / 61  # |u|^{61}/61 bound (alternating, decreasing)
    return s + iv.mpf([-rem, rem])

PI = iv.pi
LOGQ = iv.log(iv.sqrt(23) / (2 * PI))

def zinfo(sig, T):
    """for z = sig + iT (T > 0, |sig| << T): |z|^2, log|z|, arg z, sec(arg z /2)."""
    m2 = sig * sig + T * T
    lz = iv.log(m2) / 2
    ar = PI / 2 - atan_small(sig / T)
    sec = 1 / iv.cos(ar / 2)
    return m2, lz, ar, sec

def psi_re_im(sig, T):
    """enclosures of Re psi(z), Im psi(z), z = sig + iT: psi = log z - 1/(2z) + R, |R| <= sec^3/(12|z|^2)."""
    m2, lz, ar, sec = zinfo(sig, T)
    R = (sec ** 3 / (12 * m2)).b
    re = lz - sig / (2 * m2) + iv.mpf([-R, R])
    im = ar + T / (2 * m2) + iv.mpf([-R, R])
    return re, im

def loggamma_abs(sig, T):
    """log|Gamma(sig+iT)| = (sig-1/2) log|z| - T arg z - sig + log(2pi)/2 + E, |E| <= sec^2/(12|z|)."""
    m2, lz, ar, sec = zinfo(sig, T)
    E = (sec ** 2 / (12 * iv.sqrt(m2))).b
    return (sig - iv.mpf(0.5)) * lz - T * ar - sig + iv.log(2 * PI) / 2 + iv.mpf([-E, E])

# ---------------- Gaussian pieces (w(v) = e^{-v^2/4t}/sqrt(4 pi t)) ----------------
def full_mass(a, b, t):
    """(4 pi t)^{-1/2} int_R e^{-a v^2 + b v} dv = (4 pi t)^{-1/2} sqrt(pi/a) e^{b^2/(4a)}"""
    return iv.sqrt(PI / a) * iv.exp(b * b / (4 * a)) / iv.sqrt(4 * PI * t)

def left_tangent(a, b, u, t):
    """(4 pi t)^{-1/2} int_{-inf}^{u} e^{-a v^2+bv} <= e^{-a u^2 + b u}/((b - 2 a u) sqrt(4 pi t)), valid if b - 2au > 0"""
    d = b - 2 * a * u
    if not d.a > 0:
        return None
    return iv.exp(-a * u * u + b * u) / (d * iv.sqrt(4 * PI * t))

def right_tangent(a, b, u, t):
    """(4 pi t)^{-1/2} int_u^inf e^{-a v^2+bv} <= e^{-a u^2 + b u}/((2au - b) sqrt(4 pi t)), valid if 2au - b > 0"""
    d = 2 * a * u - b
    if not d.a > 0:
        return None
    return iv.exp(-a * u * u + b * u) / (d * iv.sqrt(4 * PI * t))

def hi(x):
    return x.b

# ---------------- the box check ----------------
NSUM = 20000
LOGN = [None] + [iv.log(iv.mpf(n)) for n in range(1, NSUM + 2)]
PARTIAL_CACHE = {}

def partial_sum(sigma, N):
    key = (str(sigma), N)
    if key not in PARTIAL_CACHE:
        s = iv.mpf(0); sg = iv.mpf(sigma)
        for n in range(1, N + 1):
            if ABSA[n]:
                s += int(ABSA[n]) * iv.exp(-sg * LOGN[n])
        PARTIAL_CACHE[key] = s
    return PARTIAL_CACHE[key]

B_CACHE = {}
def Bup(sigma):
    if sigma not in B_CACHE:
        B_CACHE[sigma] = B_upper(sigma)
    return B_CACHE[sigma]

def box_margin(tn, td, eps_num, eps_den, T_lo, T_hi, y_lo, y_hi, N=NSUM, mcells=200, detail=False):
    t = iv.mpf(tn) / td
    eps = iv.mpf(eps_num) / eps_den
    eps_f = eps_num / eps_den
    T = iv.mpf([T_lo, T_hi])
    y = iv.mpf([y_lo, y_hi])
    c = (1 / iv.mpf(T_lo) ** 2 + PI / iv.mpf(T_lo)) / 8          # c(T) decreasing: upper bound at T_lo
    c = iv.mpf(c.b)
    a0 = 1 / (4 * t)
    a = a0 - c
    # alpha = -(log q + psi(S0))/2, S0 = (1+y)/2 - iT  ->  psi(conj z) = conj psi(z), z = (1+y)/2 + iT
    re2, im2 = psi_re_im((1 + y) / 2, T)
    re_alpha = -(LOGQ + re2) / 2
    im_alpha = im2 / 2                                         # Im psi(S0) = -im2  ->  Im alpha = +im2/2
    re1, im1 = psi_re_im((1 - y) / 2, T)
    re_beta = (LOGQ + re1) / 2
    # rho = |gamma(s0)|/|gamma(S0)|
    # log|Gamma(z1)| - log|Gamma(z2)|, z1 = (1-y)/2 + iT, z2 = (1+y)/2 + iT, written without the large -T*pi/2 terms:
    # = (-y/2) log|z1| - (y/2) log|z2| + T (atan(s1/T) - atan(s2/T)) + y + E1 - E2   (arg z = pi/2 - atan(sig/T))
    s1, s2 = (1 - y) / 2, (1 + y) / 2
    m21, lz1, ar1, sec1 = zinfo(s1, T)
    m22, lz2, ar2, sec2 = zinfo(s2, T)
    E = (sec1 ** 2 / (12 * iv.sqrt(m21)) + sec2 ** 2 / (12 * iv.sqrt(m22))).b
    lrho = -y * LOGQ - y / 2 * lz1 - y / 2 * lz2 + T * (atan_small(s1 / T) - atan_small(s2 / T)) + y + iv.mpf([-E, E])
    rho = iv.exp(lrho)
    vA = y - 1 - 2 * eps
    vB = 1 + y + 2 * eps
    # ---- main term lower bound ----
    m_full = iv.exp(t * (re_alpha * re_alpha - im_alpha * im_alpha))
    tm = right_tangent(a0, re_alpha, vA, t)
    if tm is None:
        return None, "main: peak right of vA"
    taylor = full_mass(a, re_alpha, t) - full_mass(a0, re_alpha, t)
    Mlow = m_full - tm - taylor
    # ---- E_A ----
    EA = iv.mpf(0)
    for n in range(2, N + 1):
        if not ABSA[n]:
            continue
        bn = re_alpha + LOGN[n] / 2
        full = full_mass(a, bn, t)
        tg = left_tangent(a, bn, vA, t)
        val = full if tg is None else iv.mpf([0, min(hi(full), hi(tg))])
        EA += int(ABSA[n]) * iv.exp(-(1 + y) / 2 * LOGN[n]) * val
    # tail n > N
    bN = re_alpha + iv.log(iv.mpf(N + 1)) / 2
    sig_dn = math.nextafter(float((1 + eps).a), -math.inf)      # AMEND2: sigma' <= 1+eps (B decreasing in sigma)
    B1e = Bup(sig_dn)
    rest = iv.mpf(B1e) - partial_sum(sig_dn, N)                # >= sum_{n>N} |a_n| n^{-(1+eps)}
    if (bN - 2 * a * vA).a > 0:
        EA += iv.exp(-a * vA * vA + re_alpha * vA) / ((bN - 2 * a * vA) * iv.sqrt(4 * PI * t)) * rest
    else:
        # split at n_c: (N, n_c] full-mass with b_n^2 <= b_{N+1}^2 (b_n increasing, negative) + Rankin;
        # n > n_c tangent with denominator >= (b_{n_c+1} - 2 a vA) >= delta
        nc = int(math.exp(2 * float((2 * a * vA - re_alpha).b) + 0.5)) + 1
        bnc = re_alpha + iv.log(iv.mpf(nc + 1)) / 2
        if not (bnc - 2 * a * vA).a > 0:
            return None, "EA split"
        # AMEND2: b_n increasing on (N, nc], b_{N+1} < 0; need |b_n| <= |b_{N+1}|, i.e. b_nc <= -b_{N+1}
        b_at_nc = re_alpha + iv.log(iv.mpf(nc)) / 2
        if not (bN.b < 0 and (b_at_nc + bN).b <= 0):
            return None, "EA sign check"
        sig = (1 + y) / 2
        # sum_{N<n<=nc} |a_n| n^{-sig} <= nc^{1+eps-sig} * B(1+eps)
        part = full_mass(a, bN, t) * iv.exp((1 + eps - sig) * iv.log(iv.mpf(nc))) * B1e
        EA += part + iv.exp(-a * vA * vA + re_alpha * vA) / ((bnc - 2 * a * vA) * iv.sqrt(4 * PI * t)) * rest
    # ---- E_B ----
    EB = iv.mpf(0)
    for n in range(1, N + 1):
        if not ABSA[n]:
            continue
        bn = re_beta - LOGN[n] / 2
        full = full_mass(a, bn, t)
        tg = right_tangent(a, bn, vB, t)
        val = full if tg is None else iv.mpf([0, min(hi(full), hi(tg))])
        EB += int(ABSA[n]) * iv.exp(-(1 - y) / 2 * LOGN[n]) * val
    bN2 = re_beta - iv.log(iv.mpf(N + 1)) / 2
    if (2 * a * vB - bN2).a > 0:
        EB += iv.exp(-a * vB * vB + re_beta * vB) / ((2 * a * vB - bN2) * iv.sqrt(4 * PI * t)) * rest
    else:
        # AMEND (A6-1): split at n_c': for N < n <= n_c', b'_n in (2a vB, b'_{N+1}] is positive and decreasing, so the
        # (G2) bound full_mass(a, b'_n) <= full_mass(a, b'_{N+1}); Rankin: sum_{n<=nc'} |a_n| n^{-(1-y)/2}
        # <= nc'^{1+eps-(1-y)/2} B(1+eps). For n > n_c' the (G3) tangent with denominator >= (2a vB - b'_{nc'+1}).
        ncp = int(math.exp(2 * float((re_beta - 2 * a * vB).b) + 0.5)) + 1
        bnc2 = re_beta - iv.log(iv.mpf(ncp + 1)) / 2
        if not (2 * a * vB - bnc2).a > 0:
            return None, "EB split"
        if not bN2.a > 0:
            return None, "EB split sign"
        # AMEND2: b'_n decreasing on (N, nc']; need |b'_n| <= b'_{N+1}, i.e. b'_{nc'} >= -b'_{N+1}
        bp_at_nc = re_beta - iv.log(iv.mpf(ncp)) / 2
        if not (bp_at_nc + bN2).a >= 0:
            return None, "EB sign check"
        sig = (1 - y) / 2
        EB += full_mass(a, bN2, t) * iv.exp((1 + eps - sig) * iv.log(iv.mpf(ncp))) * B1e
        EB += iv.exp(-a * vB * vB + re_beta * vB) / ((2 * a * vB - bnc2) * iv.sqrt(4 * PI * t)) * rest
    # ---- E_M: integral over sigma in [-eps, 1+eps], v = 2 sigma - 1 + y, dv = 2 dsigma ----
    EM = iv.mpf(0)
    lo_s, hi_s = -eps_f, 1 + eps_f
    for k in range(mcells):
        s1 = lo_s + (hi_s - lo_s) * k / mcells
        s2 = lo_s + (hi_s - lo_s) * (k + 1) / mcells
        sg = iv.mpf([s1, s2])
        v = 2 * sg - 1 + y
        Qabs = 23 * iv.sqrt(((2 + sg) ** 2 + T * T) * ((3 + sg) ** 2 + T * T)) / (4 * PI * PI)
        f = iv.exp(-a * v * v + re_beta * v) / iv.sqrt(4 * PI * t) * iv.exp((1 + eps - sg) / 2 * iv.log(Qabs)) * 2
        EM += iv.mpf(hi(f)) * (iv.mpf(s2) - iv.mpf(s1))
    EM = EM * B1e
    margin = Mlow - EA - rho * (EB + EM)
    if detail:
        return margin, dict(Mlow=Mlow, EA=EA, EB=rho * EB, EM=rho * EM, rho=rho, re_alpha=re_alpha, im_alpha=im_alpha)
    return margin, None

if __name__ == "__main__":
    # small checks: B bounds, and a few boxes at t = 21/50, eps = 1/4, y in [0.374, 0.4]
    for s in [1.25, 1.3]:
        print("B(%.2f) <= %s" % (s, Bup(s)))
    for x in [12000, 18000, 25000, 50000]:
        T = x / 2
        m, d = box_margin(21, 50, 1, 4, T, T * (1 + 1 / 256), 0.374, 0.4, detail=True)
        print("x=%d margin %s  Mlow %s EA %s EB %s EM %s" % (x, m, d["Mlow"], d["EA"], d["EB"], d["EM"]), flush=True)
