/* z21_ref1.gp -- BAR-Z2-1 degree-1 POSITIVE CONTROL reference: H_t(x+iy) for chi_-4 (m = 4, a = 1) in the
   FGMPS normalisation H_t(z) = pi^(-1/2) int e^(-u^2) xi_L((1+iz)/2 + sqrt(t) u) du  (their (4.1), p. 19),
   xi_L(s) = (m/pi)^((s+a)/2) Gamma((s+a)/2) L(s) = 2 * lfunlambda(lfuncreate(-4), s)  (factor 2 checked pre-seal:
   pre/norm_check_out.txt, ratio 2.000...). Trapezoid in u, |u| <= U = 12, step hu = 1/4 (as a16_pred.gp); one point
   is repeated with hu = 1/8 as a quadrature self-check (reported). Grid (sealed): t = 1/10, y in {1/5, 9/10},
   x = 1000 + k/2, k = 0..4. Output ref1.txt: x y re im per line. One core; nbthreads printed. */
default(nbthreads,1);
print("nbthreads=", default(nbthreads));
default(parisizemax, 4000000000);
default(realprecision,38);
print("realprecision=", default(realprecision));
L = lfuncreate(-4);
t = 1/10; st = sqrt(t); U = 12;
Li = lfuninit(L, [1/4, st*U + 0.6, 1003/2 + 1]);
H(x, y, hu) = {
  my(s0 = (1 - y + I*x)/2, S = 0, n = U/hu);
  for(k = -n, n, my(u = k*hu); S += exp(-u^2) * 2 * lfunlambda(Li, s0 + st*u));
  S * hu / sqrt(Pi);
}
OUT = "ref1.txt";
{
  my(t0 = getabstime());
  foreach([1/5, 9/10], y,
    for(k = 0, 4, my(x = 1000 + k/2, h = H(x, y, 1/4));
      write(OUT, Str(x, " ", y, " ", real(h), " ", imag(h)))));
  my(h4 = H(1000, 9/10, 1/4), h8 = H(1000, 9/10, 1/8));
  write(OUT, Str("selfcheck_hu x=1000 y=9/10 rel_diff ", abs(h4 - h8)/abs(h8)));
  write(OUT, Str("total_ms ", getabstime() - t0));
}
quit;
