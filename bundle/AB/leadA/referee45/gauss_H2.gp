/* v2: symmetric window. |xi(sigma+iT)| is symmetric about sigma = 1/2, so the integrand has two Gaussian peaks,
   at v ~ y - 2 t Lam (dominant, left) and v ~ y + 2 t Lam. Window covers both with 12 sigma margin. */
default(nbthreads,1);
default(realprecision,38);
L = lfunetaquo([1,1;23,1]);
run2(x, y) = {
  my(t = 19/50, T = x/2, Lam = log(sqrt(23)/(2*Pi)*T)/2, R = 2*t*Lam + sqrt(4*t*60) + 1, a, b, lo, hi, Li, h, t0);
  a = y - R; b = y + R;
  lo = (1 - y + a)/2; hi = (1 - y + b)/2;
  t0 = getabstime();
  Li = lfuninit(L, [(lo+hi)/2, (hi-lo)/2 + 0.1, T + 1]);
  h = intnum(v = a, b, exp(-v^2/(4*t)) * lfunlambda(Li, (1-y+v)/2 + I*x/2) / 2) / sqrt(4*Pi*t);
  printf("x=%s y=%s window=[%.2f,%.2f] H=%.25Pe + i*%.25Pe  log|H|=%.12f  arg=%.15f  ms=%d\n", x, y, a, b, real(h), imag(h), log(abs(h)), arg(h), getabstime()-t0);
}
