/* a16_probe2.gp -- second timing/accuracy probe for the BAR-A16 PARI prediction (not a scored item).
   Same integral as referee45/gauss_H2.gp, written in u = v/(2 sqrt t):
     H_t(x+iy) = pi^(-1/2) int e^(-u^2) xi((1-y)/2 + i x/2 + sqrt(t) u) du,  xi = lfunlambda/2,
   evaluated by the trapezoid rule with step hu on |u| <= U (Gaussian-weighted entire integrand; refs3.gp used
   hu = 1/20 on |u| <= 9 at x <= 800). Checks: (i) one lfunlambda call cost; (ii) trapezoid vs the referee's 57-digit
   value log|H(12500 + i/2)| = -9807.871982413984 (REFEREE-A45 item 3); (iii) trapezoid at x = 12496, y = 0 vs
   intnum (a16_probe_out.txt); (iv) step halving hu = 1/8 vs 1/16 at x = 12496, y = 0. */
default(nbthreads,1);
print("nbthreads=", default(nbthreads));
default(parisizemax, 6000000000);
default(realprecision,57);
print("realprecision=", default(realprecision));
L = lfunetaquo([1,1;23,1]);
t = 19/50;
st = sqrt(t);
Lam = log(sqrt(23)/(2*Pi)*(12500/2))/2;
U = ceil(st*Lam + 9);
R = 2*st*U;
t0 = getabstime();
Li = lfuninit(L, [1/2, st*U + 0.6, 12500/2 + 1]);
print("init ms=", getabstime()-t0, " U=", U);
{
  my(t1 = getabstime(), z = lfunlambda(Li, 1/2 + I*12498/2));
  printf("one lfunlambda call ms=%d\n", getabstime()-t1);
}
HT(x, y, hu) = {
  my(n = round(U/hu), S = 0, s0 = (1-y)/2 + I*x/2);
  for(k = -n, n, my(u = k*hu); S += exp(-u^2) * lfunlambda(Li, s0 + st*u));
  S * hu / 2 / sqrt(Pi);
}
{
  my(t1 = getabstime(), h = HT(12500, 1/2, 1/8));
  printf("(12500, 1/2) hu=1/8: log|H|=%.15f arg=%.15f ms=%d  (referee 57-digit: -9807.871982413984)\n", log(abs(h)), arg(h), getabstime()-t1);
  my(t2 = getabstime(), g8 = HT(12496, 0, 1/8));
  printf("(12496, 0) hu=1/8:  H=%.25Pe + i*%.5Pe ms=%d\n", real(g8), imag(g8), getabstime()-t2);
  my(t3 = getabstime(), g16 = HT(12496, 0, 1/16));
  printf("(12496, 0) hu=1/16: H=%.25Pe + i*%.5Pe ms=%d\n", real(g16), imag(g16), getabstime()-t3);
  printf("rel diff 1/8 vs 1/16: %.3Pe\n", abs(g8-g16)/abs(g16));
}
quit;
