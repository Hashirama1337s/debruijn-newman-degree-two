\\ refs44b.gp -- float sign changes of H_{21/50} (N = 44) on the real axis in (5, 15), by the Gaussian average of
\\ lfunlambda (independent of the certified evaluator). Prediction source for the P0 control of BAR-A10.
default(realprecision, 40);
L = lfunetaquo([2,1;22,1]);
Li = lfuninit(L, [1/2, 4, 12]);
t = 21/50;
Hr(x) = my(g = 0); for(k = -180, 180, my(u = k/20); g += exp(-u^2)/20/sqrt(Pi) * lfunlambda(Li, (1 + I*x)/2 + sqrt(t)*u)/2); real(g);
{
  my(prev = Hr(5), cnt = 0, v, zs = List());
  forstep(x = 5 + 1/20, 15, 1/20, v = Hr(x); if(sign(v) != sign(prev), cnt++; listput(zs, x)); prev = v);
  write("refs44.txt", Str("realsignchanges_5_15 ", cnt, " ", Vec(zs)));
}
