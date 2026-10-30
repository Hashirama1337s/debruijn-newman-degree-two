\\ refs44.gp -- PARI references for p = 11 (N = 44): eta(2z)eta(22z) coefficient identity check, H_0 values,
\\ independent Gaussian-average H_{21/50} values, and float sign changes of H_{21/50} on (5,15) (P0 prediction).
default(realprecision, 60);
L = lfunetaquo([2,1;22,1]);
out = "refs44.txt";
{
  my(M = 3000, e, th);
  e = Vec(x*prod(n = 1, M, 1 - x^(2*n) + O(x^(M+1)))*prod(n = 1, M\22, 1 - x^(22*n) + O(x^(M+1))));
  th = vector(M, n, qfrep([2,0;0,22], M, 1)[n] - qfrep([6,2;2,8], M, 1)[n]);
  write(out, Str("eta_equals_forms_n<=3000 ", e[1..M] == th));
}
xi(s) = lfunlambda(L, s)/2;
{
  foreach([[100, 374/1000], [800, 41/100]], p, my(z = p[1] + I*p[2]); my(v = xi((1 + I*z)/2));
    write(out, Str("H0 ", p[1], " ", p[2], " ", real(v), " ", imag(v))));
  foreach([[100, 374/1000], [3000, 374/1000]], p,
    my(x = p[1], y = p[2], z = x + I*y, Li = lfuninit(L, [1/2, 4, x/2 + 4]), g = 0, t = 21/50);
    for(k = -180, 180, my(u = k/20); g += exp(-u^2)/20/sqrt(Pi) * lfunlambda(Li, (1 + I*z)/2 + sqrt(t)*u)/2);
    write(out, Str("GA ", x, " ", y, " ", real(g), " ", imag(g))));
  my(t = 21/50, Li = lfuninit(L, [1/2, 4, 12]), cnt = 0, prev, v);
  Hr(x) = my(g = 0); for(k = -180, 180, my(u = k/20); g += exp(-u^2)/20/sqrt(Pi) * lfunlambda(Li, (1 + I*x)/2 + sqrt(t)*u)/2); real(g);
  prev = Hr(5);
  forstep(x = 5 + 1/20, 15, 1/20, v = Hr(x); if(sign(v) != sign(prev), cnt++); prev = v);
  write(out, Str("realsignchanges_5_15 ", cnt));
}
