/* a16_pred.gp -- BAR-A16 PARI prediction: number of real sign changes of H_{19/50} on (12496, 12500].
   Independent of the lab evaluator (no eta, no contour): Gaussian average of PARI's completed L-function, the method
   of referee45/gauss_H2.gp (symmetric window: both Gaussian peaks), written in u = v/(2 sqrt t):
     H_t(x) = pi^(-1/2) int e^(-u^2) xi(1/2 + i x/2 + sqrt(t) u) du,  xi = lfunlambda/2,  x real.
   For real x the integrand at -u is the conjugate of the one at +u (xi(1-s) = xi(s), real coefficients), so
     H_t(x) = hu pi^(-1/2) [xi(1/2 + i x/2) + 2 Re sum_{k=1}^{n} e^(-u_k^2) xi(1/2 + i x/2 + sqrt(t) u_k)],  u_k = k hu,
   trapezoid on |u| <= U = 12 (peaks at |u| = sqrt(t) Lam ~ 2.6; truncation ~ e^(-88)), step hu = 1/4 (checked against
   hu = 1/8, 1/16 and intnum in a16_probe_out.txt / a16_probe2_out.txt). 57 digits, one core.
   Grid: x = 12496 + k/10, k = 0..40. Any same-sign local minimum of |H| is re-sampled at 1/100 spacing on +-1/10 around it.
   Output: a16_pred.txt (one line per grid point, then the summary). */
default(nbthreads,1);
print("nbthreads=", default(nbthreads));
default(parisizemax, 6000000000);
default(realprecision,57);
print("realprecision=", default(realprecision));
L = lfunetaquo([1,1;23,1]);
t = 19/50;
st = sqrt(t);
U = 12;
hu = 1/4;
t0 = getabstime();
Li = lfuninit(L, [1/2, st*U + 0.6, 12500/2 + 1]);
print("init ms=", getabstime()-t0);
HR(x) = {
  my(n = U/hu, s0 = 1/2 + I*x/2, S = 0);
  for(k = 1, n, my(u = k*hu); S += exp(-u^2) * lfunlambda(Li, s0 + st*u));
  (real(lfunlambda(Li, s0)) + 2*real(S)) * hu / 2 / sqrt(Pi);
}
OUT = "a16_pred.txt";
{
  my(t1 = getabstime(), h0 = HR(12496));
  write(OUT, Str("check x=12496 hu=1/4 H=", h0, " ms=", getabstime()-t1, "  (intnum: -1.92363131384728166046 E-4259)"));
  my(N = 40, xs = vector(N+1, k, 12496 + (k-1)/10), hs = vector(N+1), cnt = 0, zs = List(), mins = List(), extra = List());
  for(k = 1, N+1, hs[k] = HR(xs[k]); write(OUT, Str("x ", xs[k], " sign ", sign(hs[k]), " log|H| ", log(abs(hs[k])))));
  for(k = 2, N+1, if(sign(hs[k]) != sign(hs[k-1]), cnt++; listput(zs, [xs[k-1], xs[k]])));
  for(k = 2, N, if(sign(hs[k-1]) == sign(hs[k]) && sign(hs[k]) == sign(hs[k+1]) && abs(hs[k]) < abs(hs[k-1]) && abs(hs[k]) < abs(hs[k+1]), listput(mins, xs[k])));
  foreach(mins, m, for(j = -9, 9, if(j != 0, my(xx = m + j/100, hh = HR(xx)); listput(extra, [xx, sign(hh)]); write(OUT, Str("refine ", xx, " sign ", sign(hh), " log|H| ", log(abs(hh)))))));
  write(OUT, Str("signchanges_12496_12500 ", cnt, " brackets ", Vec(zs)));
  write(OUT, Str("same_sign_local_minima ", Vec(mins), " refine_signs ", Vec(extra)));
  write(OUT, Str("total ms ", getabstime()-t0));
}
quit;
