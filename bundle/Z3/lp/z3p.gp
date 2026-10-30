\\ z3p.gp -- BAR-Z3-P: exact (rational, Sturm) tests of the key step and of Lemma P on polynomials, plus the
\\ field check zeta_K = zeta * L(eta(z)eta(23z)). One core. All arithmetic exact in Q[x] except item F3 (lfunlambda).
\\ Usage: gp -q z3p.gp   (writes z3p_out.txt via print to stdout; runner redirects)
default(nbthreads,1); print("nbthreads ", default(nbthreads));
default(parisize, 256*10^6);
setrand(20261030);

derivn(p,k) = { my(r=p); for(i=1,k, r=deriv(r,'x)); r; }
\\ e^{-t D^2} p  (D = d/dx), finite sum on polynomials
heat(p,t) = sum(k=0, poldegree(p)\2, (-t)^k/k! * derivn(p,2*k));
\\ [e^{-c d_x d_y} (p(x) q(y))]_{x=y}
Dop(p,q,c) = sum(k=0, min(poldegree(p),poldegree(q)), (-c)^k/k! * derivn(p,k)*derivn(q,k));
\\ exact real-rootedness: squarefree part has deg-many distinct real roots (polsturm counts distinct roots)
rr(P) = { my(S); if(P==0, error("zero polynomial")); if(poldegree(P)<=0, return(1));
  S = P/gcd(P,deriv(P,'x)); if(poldegree(S)<=0, return(1)); polsturm(S)==poldegree(S); }
\\ Lambda by bisection on [-64,64]; returns [lo,hi] with heat(p,lo) not real-rooted, heat(p,hi) real-rooted
lam(p) = { my(lo=-64, hi=64, m);
  if(rr(heat(p,lo)), error("lam: real-rooted at -64")); if(!rr(heat(p,hi)), error("lam: not real-rooted at 64"));
  for(i=1,22, m=(lo+hi)/2; if(rr(heat(p,m)), hi=m, lo=m)); [lo,hi]; }
rint(a,b) = a + random(b-a+1);
rrpoly(d,R) = prod(i=1,d, 'x - rint(-R,R));                     \\ real-rooted, integer roots, repeats allowed
rrdist(d,R) = { my(v=vecextract(numtoperm(2*R+1, random((2*R+1)!)), 2^d-1)); prod(i=1,d,'x - (v[i]-R-1)); } \\ distinct
genpoly(dmin,dmax) = { my(d=rint(dmin,dmax), p=1, nq);
  nq = rint(0, d\2); for(i=1,nq, p *= ('x - rint(-6,6))^2 + rint(1,3)^2);
  for(i=1, d-2*nq, p *= 'x - rint(-8,8)); p; }

\\ ---------- PC: positive controls ----------
pc1 = rr(heat('x^2+1, 1/2)) && !rr(heat('x^2+1, 1/2 - 2^-20));
pc2 = rr(Dop('x,'x,1)) && !rr(Dop('x,'x,-1));
pc3 = (Dop('x,'x,1) == 'x^2-1) && (Dop('x,'x,-1) == 'x^2+1);
L = lam('x^2+1); pc4 = (L[1] < 1/2 && 1/2 <= L[2] && L[2]-L[1] < 10^-4);
print("PC lambda(x^2+1)=1/2 exact: ", pc1, "  D_c(x,x) real / D_-c(x,x) not: ", pc2, "  explicit: ", pc3, "  bisect bracket ", L, " ", pc4);
pcfail = !(pc1 && pc2 && pc3 && pc4);

\\ ---------- I: identity e^{-tD^2}(pq) == [e^{-2t dxdy} p_t(x) q_t(y)]_{x=y}, exact ----------
ibad = 0; icnt = 0;
{for(j=1,100, my(p=genpoly(1,6), q=genpoly(1,6));
  foreach([-1/3, 1/2, 2, 7/5], t, icnt++; if(heat(p*q,t) != Dop(heat(p,t), heat(q,t), 2*t), ibad++)));}
print("I identity checks ", icnt, " failures ", ibad);

\\ ---------- K: key step on real-rooted pairs, c > 0 (should hold) and null c < 0 ----------
kbad = 0; knull = 0; kn = 400;
{for(j=1,kn, my(p=rrpoly(rint(1,8),10), q=rrpoly(rint(1,8),10), c=rint(1,40)/8);
  if(!rr(p) || !rr(q), error("K: input not real-rooted"));
  if(!rr(Dop(p,q,c)), kbad++; print("K VIOLATION ", p, " | ", q, " | c=", c));
  if(!rr(Dop(p,q,-c)), knull++));}
print("K pairs ", kn, " violations(c>0) ", kbad, " null violations(c<0) ", knull, " frac ", knull/kn*1.);

\\ ---------- L: Lemma P on polynomial pairs with complex roots ----------
lbad = 0; ln = 300; lstrict = 0; lgap = [];
{for(j=1,ln, my(p, q, Lp, Lq, ts, Lpq);
  until(poldegree(p)>=2 && poldegree(q)>=2 && (!rr(p) || !rr(q)), p=genpoly(2,6); q=genpoly(2,6));
  Lp = lam(p); Lq = lam(q); ts = vecmax([Lp[2], Lq[2], 0]);
  if(!rr(heat(p,ts)) || !rr(heat(q,ts)), error("L: hypothesis fails at t*"));
  if(!rr(heat(p*q,ts)), lbad++; print("L VIOLATION ", p, " | ", q, " t*=", ts));
  Lpq = lam(p*q); if(Lpq[2] < vecmax([Lp[1], Lq[1], 0]) - 10^-3, lstrict++);
  lgap = concat(lgap, vecmax([Lp[1],Lq[1],0]) - Lpq[2]));}
print("L pairs ", ln, " violations ", lbad, " strictly smaller (margin 1e-3) ", lstrict, " min gap ", vecmin(lgap)*1., " median gap ", vecsort(lgap)[ln\2]*1.);

\\ ---------- NL: null for the role of 0 -- real-rooted distinct-root pairs, Lambda < 0, t' = max(Lp,Lq) ----------
nlv = 0; nln = 300;
{for(j=1,nln, my(p=rrdist(rint(2,6),8), q=rrdist(rint(2,6),8), Lp, Lq, tp);
  Lp = lam(p); Lq = lam(q); tp = max(Lp[2], Lq[2]); if(tp >= 0, error("NL: Lambda not negative"));
  if(!rr(heat(p*q,tp)), nlv++));}
print("NL pairs ", nln, " violations without the 0 ", nlv, " frac ", nlv/nln*1.);

\\ ---------- F: zeta_K = zeta * L(eta(z)eta(23z)), K = Q[x]/(x^3-x-1); Hilbert class field check ----------
N = 3000;
Lk = lfuncreate('x^3-'x-1); ak = lfunan(Lk, N);
fq = 'q*eta('q+O('q^N))*eta('q^23+O('q^(N+1))); af = vector(N, n, polcoef(fq, n, 'q));
conv(a,b) = vector(#a, n, sumdiv(n, d, a[d]*b[n/d]));
one = vector(N, n, 1);
F1 = (conv(one, af) == ak);
print("F1 zeta_K coefficients == (1 * a_f) for n <= ", N, ": ", F1, "   a_f[1..9] ", af[1..9]);
Lf = lfunetaquo([1,1;23,1]); Lz = lfuncreate(1);
print("F2 lfunparams zeta_K ", lfunparams(Lk), "  zeta ", lfunparams(Lz), "  eta(z)eta(23z) ", lfunparams(Lf));
default(realprecision, 38);
r1 = lfunlambda(Lk, 3/10+5*I)/(lfunlambda(Lz,3/10+5*I)*lfunlambda(Lf,3/10+5*I));
r2 = lfunlambda(Lk, 2+I)/(lfunlambda(Lz,2+I)*lfunlambda(Lf,2+I));
print("F3 Lambda_K/(Lambda_zeta*Lambda_f) at 0.3+5i: ", r1, "  at 2+i: ", r2);
F3 = (abs(r1-1) < 10^-25 && abs(r2-1) < 10^-25);
H = nfsplitting('x^3-'x-1); print("F4 Hilbert class field polynomial ", H, " disc ", nfdisc(H));
NH = 2000; ah = lfunan(lfuncreate(H), NH);
chi = vector(NH, n, kronecker(-23, n)); af2 = af[1..NH];
F4 = (conv(conv(conv(one[1..NH], chi), af2), af2) == ah);
print("F4 zeta_H == zeta * L(chi_-23) * L(f)^2 coefficients n <= ", NH, ": ", F4);

print("SUMMARY pcfail=", pcfail, " ibad=", ibad, " kbad=", kbad, " knull_frac=", knull/kn*1., " lbad=", lbad, " nl_frac=", nlv/nln*1., " F1=", F1, " F3=", F3, " F4=", F4);
quit;
