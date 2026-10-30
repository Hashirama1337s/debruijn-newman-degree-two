"""z21_core.py -- BAR-Z2-1 (main-term fidelity probe). Shared definitions; NO data, NO scoring.

Main term transcribed from arXiv:2610.27343 (FGMPS): eq. (4.40) p. 43, (2.2)-(2.4) pp. 9-10, B_t p. 10,
truncation Thm 4.3 p. 22. Degree 1 exactly as the paper; degree 2 = our transcription (READ-FGMPS.md, PLAN-Z2.md):
  log M0(s) = s log(sqrt(N)/2pi) + (s - 1/2) log s - s + log(2pi)/2         (Stirling form of (sqrt N/2pi)^s Gamma(s))
  alpha(s)  = log(sqrt(N)/2pi) + log s - 1/(2s)                              (= (log M0)')
  M_t(s) = exp((t/4) alpha(s)^2) M0(s);  s+ = (1+y-ix)/2, s- = (1-y+ix)/2;  B_t = M_t(s+);  gamma = M_t(s-)/M_t(s+)
  s*(+-) = s+- + (t/2) alpha(s+-);  b_n = exp((t/4) log^2 n)
  f_t = sum_{n<=M} b_n a_n n^{-s*(+)} + gamma sum_{n<=M} b_n a_n n^{-s*(-)}
  M = floor(sqrt(N) T'/(2pi)), T' = x/2 + pi t/4  (degree 2);   M = floor(sqrt(m T'/(2pi))), T' = x/2 + pi t/8 (degree 1)
Error bound eps_t of (6.6) pp. 58-59 (degree 1 only; D = 1; B*_m <= 3.33 sqrt(m)).
"""
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 50

# ---------------- coefficients ----------------
def reps(A, B, C, M):
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

def coeffs_dihedral(form0, form1, M):
    """a_n of theta_chi = (theta_Q0 - theta_Q1)/2 (order-3 class-group character; THEOREM-A identification)."""
    r0, r1 = reps(*form0, M), reps(*form1, M)
    assert np.all((r0 - r1) % 2 == 0)
    return ((r0 - r1) // 2).astype(np.float64)

def coeffs_23(M):
    a = coeffs_dihedral((1, 1, 6), (2, 1, 3), M)
    assert list(a[1:9]) == [1, -1, -1, 0, 0, 1, 0, 1] and a[23] == 1 and a[59] == 2   # as in tail_cert.py
    return a

def coeffs_31(M):
    a = coeffs_dihedral((1, 1, 8), (2, 1, 4), M)
    assert a[1] == 1 and a[2] == -1 and a[3] == 0 and a[5] == -1 and a[7] == -1 and a[31] == 1
    return a

def coeffs_chim4(M):
    a = np.zeros(M + 1)
    for n in range(1, M + 1):
        a[n] = 0.0 if n % 2 == 0 else (1.0 if n % 4 == 1 else -1.0)
    return a

# ---------------- gamma sides ----------------
class Deg2:
    def __init__(self, N):
        self.N = N
        self.lq = mp.log(mp.sqrt(N) / (2 * mp.pi))
    def logM0(self, s):
        return s * self.lq + (s - mp.mpf(1) / 2) * mp.log(s) - s + mp.log(2 * mp.pi) / 2
    def alpha(self, s):
        return self.lq + mp.log(s) - 1 / (2 * s)
    def M(self, x, t):
        Tp = mp.mpf(x) / 2 + mp.pi * t / 4
        return int(mp.floor(mp.sqrt(self.N) * Tp / (2 * mp.pi)))

class Deg1:
    """FGMPS (2.2)-(2.3): log M0 = log(2pi)/2 + ((s+a)/2) log(m/pi) + ((s+a-1)/2) log((s+a)/2) - (s+a)/2."""
    def __init__(self, m, a):
        self.m, self.a = m, a
    def logM0(self, s):
        w = s + self.a
        return mp.log(2 * mp.pi) / 2 + w / 2 * mp.log(mp.mpf(self.m) / mp.pi) + (w - 1) / 2 * mp.log(w / 2) - w / 2
    def alpha(self, s):
        w = s + self.a
        return mp.log(mp.mpf(self.m) / mp.pi) / 2 + mp.log(w / 2) / 2 - 1 / (2 * w)
    def M(self, x, t):
        Tp = mp.mpf(x) / 2 + mp.pi * t / 8
        return int(mp.floor(mp.sqrt(self.m * Tp / (2 * mp.pi))))

def logMt(G, s, t):
    return (mp.mpf(t) / 4) * G.alpha(s) ** 2 + G.logM0(s)

def main_term(G, a, x, y, t, M=None):
    """returns (f_t, log B_t, M). a: numpy float array of coefficients, a[0] unused."""
    x, y, t = mp.mpf(x), mp.mpf(y), mp.mpf(t)
    sp = (1 + y - 1j * x) / 2
    sm = (1 - y + 1j * x) / 2
    if M is None:
        M = G.M(x, t)
    lBp, lBm = logMt(G, sp, t), logMt(G, sm, t)
    gam = mp.exp(lBm - lBp)
    ssp = sp + t / 2 * G.alpha(sp)
    ssm = sm + t / 2 * G.alpha(sm)
    n = np.arange(1, M + 1, dtype=np.float64)
    ln = np.log(n)
    bn = np.exp(float(t) / 4 * ln * ln)
    w = bn * a[1:M + 1]
    # n^{-s} = exp(-s log n); the large imaginary parts are reduced exactly enough in float64 (|Im s| log n < 1e7)
    sp_c = complex(ssp)
    sm_c = complex(ssm)
    S1 = np.sum(w * np.exp(-sp_c * ln))
    S2 = np.sum(w * np.exp(-sm_c * ln))
    f = mp.mpc(complex(S1)) + gam * mp.mpc(complex(S2))
    return f, lBp, M

# ---------------- FGMPS (6.6) bound, degree 1, D = 1 ----------------
def eps66(m, phim, x, y, t, D=1.0):
    x, y, t, D = mp.mpf(x), mp.mpf(y), mp.mpf(t), mp.mpf(D)
    q = m * x / (4 * mp.pi); l = mp.log(q)
    dplus = mp.sqrt(q * (1 + mp.pi * t / (4 * x)))
    am = mp.mpf("0.002") + mp.log(m) / 3800
    G = mp.exp(am * D + D / 2 * mp.log(1 + mp.pi * t / (4 * x)) + t * D / (2 * (x - 2)) * mp.log(dplus))
    dm = (t ** 2 / 16 * l ** 2 + mp.log(m) / 2250 + mp.mpf("1.3")) / (x - mp.mpf(5) / 2)
    th = (1 - y) / 2 + (3 + y) * t / (2 * x ** 2)
    epsAB = (mp.exp(dm) - 1) * (1 + G) * (1 + (dplus ** th - 1) / th)
    Tp = x / 2 + mp.pi * t / 8
    dx = x / 2 - mp.mpf(5) / 4
    V = mp.sqrt(Tp / mp.mpf("7.49")) - mp.mpf(3) / 2
    K = mp.exp((mp.sqrt(l ** 2 + mp.pi ** 2 / 4) / 4 + mp.mpf("1.54")) / (x - mp.mpf(5) / 2))
    lp = (12 * ((1 + y) / 2) ** 2 + 13) / (24 * dx)
    lm = (12 * ((1 - y) / 2) ** 2 + 13) / (24 * dx)
    S = mp.mpf(27) / 4 * (3 ** y + 3 ** (-y)) + 5 / (4 * mp.sqrt(2)) * (2 ** (y / 2) + 2 ** (-y / 2))
    Bstar = mp.mpf("3.33") * mp.sqrt(m)
    epsC = K * (m * Tp / (2 * mp.pi)) ** (-(1 + y) / 4) * mp.exp(-t * l ** 2 / 16) * \
        (Bstar * (mp.exp(lp) + mp.exp(lm)) + 2 * phim / (5 * V) * mp.exp(2 / dx) * S)
    return epsAB + epsC
