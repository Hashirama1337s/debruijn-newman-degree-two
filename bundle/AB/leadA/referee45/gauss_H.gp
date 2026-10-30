/* Independent H_t via Gaussian average of PARI completed L-function (not the lab contour/eta method):
   H_t(x+iy) = int w(v) xi((1-y+v)/2 + i x/2) dv, w(v) = (4 pi t)^(-1/2) e^(-v^2/(4t)), xi = lfunlambda/2. */
default(nbthreads,1);
default(realprecision,38);
L = lfunetaquo([1,1;23,1]);
Hg(x, y, t, Linit) = {
  my(T = x/2, Lam = log(sqrt(23)/(2*Pi)*T)/2, vc = 2*t*Lam, R = sqrt(4*t*(40 + t*Lam^2)) + 1);
  intnum(v = vc - R, vc + R, exp(-v^2/(4*t)) * lfunlambda(Linit, (1-y+v)/2 + I*x/2) / 2) / sqrt(4*Pi*t);
}
run(x, y) = {
  my(t = 19/50, T = x/2, Lam = log(sqrt(23)/(2*Pi)*T)/2, vc = 2*t*Lam, R = sqrt(4*t*(40 + t*Lam^2)) + 1, lo, hi, Li, h, t0);
  lo = (1 - y + vc - R)/2; hi = (1 - y + vc + R)/2;
  t0 = getabstime();
  Li = lfuninit(L, [(lo+hi)/2, (hi-lo)/2 + 0.1, T + 1]);
  h = Hg(x, y, t, Li);
  printf("x=%s y=%s  H=%.25Pe + i*%.25Pe  log|H|=%.12f  arg=%.15f  ms=%d\n", x, y, real(h), imag(h), log(abs(h)), arg(h), getabstime()-t0);
}
