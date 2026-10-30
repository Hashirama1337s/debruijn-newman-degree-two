/* a16_probe.gp -- timing probe for the BAR-A16 PARI prediction (not a scored item).
   Method of referee45/gauss_H2.gp (symmetric Gaussian window, lfunlambda), y = 0, t = 19/50, 57 digits.
   One lfuninit for the whole strip x in [12496, 12500], then single-point evaluations. */
default(nbthreads,1);
print("nbthreads=", default(nbthreads));
default(parisizemax, 6000000000);
default(realprecision,57);
print("realprecision=", default(realprecision));
L = lfunetaquo([1,1;23,1]);
t = 19/50;
Lam = log(sqrt(23)/(2*Pi)*(12500/2))/2;
R = 2*t*Lam + sqrt(4*t*60) + 1;
t0 = getabstime();
Li = lfuninit(L, [1/2, R/2 + 0.6, 12500/2 + 1]);
print("init ms=", getabstime()-t0, " R=", R);
H(x) = intnum(v = -R, R, exp(-v^2/(4*t)) * lfunlambda(Li, (1+v)/2 + I*x/2) / 2) / sqrt(4*Pi*t);
{
  foreach([12496, 12500], x,
    my(t1 = getabstime(), h = H(x));
    printf("x=%s H=%.20Pe + i*%.5Pe ms=%d\n", x, real(h), imag(h), getabstime()-t1));
  my(t1 = getabstime(), y = 1/2, h = intnum(v = y - R, y + R, exp(-v^2/(4*t)) * lfunlambda(Li, (1-y+v)/2 + I*12500/2) / 2) / sqrt(4*Pi*t));
  printf("instrument check (12500, 1/2): log|H|=%.12f arg=%.15f ms=%d (referee: -9807.871982413984)\n", log(abs(h)), arg(h), getabstime()-t1);
}
quit;
