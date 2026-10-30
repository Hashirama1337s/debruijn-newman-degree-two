"""addendum_a45_check.py -- re-derivation of the TAIL-LEMMA Step 10 numbers at the A45 parameters
(t = 19/50, eps = 1/5, y in [0.374, 0.49], T1 = 10^12), for TAIL-LEMMA-ADDENDUM-A45.md.

Re-typed from the TAIL-LEMMA.md Step 10 text (not copied from tail_run045.py). Only B(sigma) (Step 9 Euler-product
upper bound, tail_cert.Bup) is imported. Also checks |Im alpha| <= 0.79 at T >= T1 for both y endpoints with mpmath
digamma (high precision, not interval), and that alpha does not involve t.
Compares with tail_run045_out.json and prints AGREE / DISAGREE per number."""
import sys, json, math
sys.path.insert(0, ".")
from mpmath import iv, mp, mpf, mpc, digamma, sqrt as msqrt, pi as mpi, log as mlog
from tail_cert import Bup

iv.prec = 120
t = iv.mpf(19) / 50; eps = iv.mpf(1) / 5
YLO, YHI = iv.mpf(0.374), iv.mpf(0.49)          # the same float endpoints as the run (float(0.374), float(0.49))
T1 = iv.mpf(10) ** 12
PI = iv.pi
q = iv.sqrt(23) / (2 * PI)
Lam = iv.log(q * T1) / 2
delta = 1 / T1 ** 2
c = (1 / T1 ** 2 + PI / T1) / 8
a0 = 1 / (4 * t); a = a0 - c
kappa = 4 * t * c / (1 - 4 * t * c)
K0 = iv.exp(t * iv.mpf("0.79") ** 2)
# v_A = y - 1 - 2eps (negative), v_B = 1 + y + 2eps
vAabs_max = 1 + 2 * eps - YLO; vAabs_min = 1 + 2 * eps - YHI
vB_max = 1 + YHI + 2 * eps; vB_min = 1 + YLO + 2 * eps
rho = iv.exp(-2 * YLO * Lam + 1 / T1)            # worst y for rho is y_lo
W = 1 / iv.sqrt(4 * PI * t)
kfac = iv.sqrt(a0 / a) * iv.exp(t * kappa * (Lam + delta) ** 2)

def Bd(s):  # B at sigma rounded down (B decreasing => upper bound)
    return iv.mpf(Bup(math.nextafter(float(s.a), -math.inf)))

Bs = Bd(1 + eps)
P1 = K0 * iv.exp(-(2 * t * (Lam - delta) - vAabs_max) ** 2 / (4 * t)) * W / (Lam - delta - 2 * a0 * vAabs_max)
P2 = K0 * (kfac - 1)
P3 = K0 * kfac * (Bd((1 + YLO) / 2 + t * (Lam - delta) / 2) - 1)
P4 = K0 * iv.exp(-a * vAabs_min ** 2 + (Lam + delta) * vAabs_max - t * (Lam - delta) ** 2) * W / (2 * a * vAabs_min) * Bs
P5 = K0 * rho * kfac * iv.exp(4 * t * Lam * delta) * Bd((1 - YHI) / 2 + t * (Lam - delta) / 2)
P6 = K0 * rho * iv.exp(-a * vB_min ** 2 + (Lam + delta) * vB_max - t * (Lam - delta) ** 2) * W / (2 * a * vB_min) * Bs
P7 = K0 * rho * Bs * 2 * (1 + 2 * eps) * W * iv.exp((Lam + delta) * vB_max + 2 * Lam * (1 + 2 * eps) - t * (Lam - delta) ** 2) \
     * (1 + 25 / T1 ** 2) ** ((1 + 2 * eps) / 2)
lhs = 1 - P1 - P2
rhs = P3 + P4 + P5 + P6 + P7
# vertices: e^{-t Lam^2 + p Lam} decreases for Lam > p/(2t)
vert = {"P1": vAabs_max / (2 * t), "P1b(2a0|vA|)": 2 * a0 * vAabs_max, "P4": vAabs_max / (2 * t), "P6": vB_max / (2 * t),
        "P7": (vB_max + 2 * (1 + 2 * eps) - 2 * YLO) / (2 * t)}

mp.prec = 200
def im_alpha(y, T):
    S0 = (1 + mpf(y)) / 2 - 1j * mpf(T)          # S0 = 1 - s0, s0 = (1-y)/2 + iT
    g1 = mlog(msqrt(23) / (2 * mpi)) + digamma(mpc(S0))
    return (-g1 / 2).imag                        # alpha = -g'(S0)/2; no t anywhere

ims = {"y=0.374,T=1e12": float(abs(im_alpha(0.374, 10 ** 12))), "y=0.49,T=1e12": float(abs(im_alpha(0.49, 10 ** 12))),
       "y=0.374,T=1e15": float(abs(im_alpha(0.374, 10 ** 15))), "pi/4": float(mpi / 4)}

ref = json.load(open("tail_run045_out.json"))["B"]
rows = []
def cmp(name, mine, theirs, rel=1e-9):
    ok = abs(mine - theirs) <= rel * max(abs(theirs), 1e-300)
    rows.append((name, mine, theirs, "AGREE" if ok else "DISAGREE"))
cmp("Lam(T1)", float(Lam.a), ref["Lam"])
cmp("lhs_low", float(lhs.a), ref["lhs_low"])
cmp("rhs_high", float(rhs.b), ref["rhs_high"])
for k, v in dict(P1=P1, P2=P2, P3=P3, P4=P4, P5=P5, P6=P6, P7=P7).items():
    cmp(k, float(v.b), ref["parts"][k], rel=1e-6)
cmp("vertex P1", float(vert["P1"].b), ref["vertices"]["P1"]); cmp("vertex P6", float(vert["P6"].b), ref["vertices"]["P6"])
cmp("vertex P7", float(vert["P7"].b), ref["vertices"]["P7"])
for r in rows:
    print("%-12s mine=%.12g  run=%.12g  %s" % r)
print("vertices (upper ends):", {k: float(v.b) for k, v in vert.items()})
print("all vertices < Lam(T1) - delta:", all(float(v.b) < float((Lam - delta).a) for v in vert.values()))
print("K0 =", float(K0.b), " K0 = e^{t 0.79^2} with t = 19/50")
print("|Im alpha|:", ims, " <= 0.79:", all(v <= 0.79 for k, v in ims.items() if k != "pi/4"))
print("sig3 =", float(((1 + YLO) / 2 + t * (Lam - delta) / 2).a), " sig5 =", float(((1 - YHI) / 2 + t * (Lam - delta) / 2).a))
print("lhs - rhs > 0:", bool((lhs - rhs).a > 0))
print("ALL AGREE" if all(r[3] == "AGREE" for r in rows) else "SOME DISAGREE")
