\\ null44.gp -- PARI float prediction (independent code path) for the p = 11 high-x null control:
\\ number of real sign changes of H_{21/50} (N = 44) on (2696, 2700), via the float eta-contour evaluator
\\ (same formula as ../etaH.gp with N = 44 and f = eta(2 tau) eta(22 tau)).
default(realprecision, 60);
N = 44;
f(tau) = eta(2*tau, 1) * eta(22*tau, 1);
Phi(w) = 2 * exp(w) * f(I * exp(2*w) / sqrt(N));
Hteta(z, t, dl = 20, hfac = 1.0) =
{
  my(x = max(real(z), 20), delta = min(dl/max(real(z), 20), 1/8), th = Pi/4 - 2*delta, umax, h, S = 0, w, nst);
  umax = log(40*sqrt(N)/(2*Pi*sin(2*delta)))/2 + 1;
  h = hfac/x; nst = ceil(umax/h);
  for(k = -nst, nst, w = k*h + I*th; S += exp(t*w^2 + I*z*w) * Phi(w));
  S * h;
}
{
  my(t = 21/50, prev = real(Hteta(2696, t)), cnt = 0, v, zs = List());
  forstep(x = 2696 + 1/50, 2700, 1/50, v = real(Hteta(x, t)); if(sign(v) != sign(prev), cnt++; listput(zs, x)); prev = v);
  write("null44_pred.txt", Str("signchanges_2696_2700 ", cnt, " ", Vec(zs)));
}
