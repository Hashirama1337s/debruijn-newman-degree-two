default(nbthreads,1); print("nbthreads=", default(nbthreads));
default(realprecision,38);
L = lfuncreate(-4);
s = 2;
xiL = (4/Pi)^((s+1)/2) * gamma((s+1)/2) * Catalan;
print("xi_L(2) paper normalisation = ", xiL);
print("lfunlambda(-4,2) = ", lfunlambda(L, s));
print("ratio xi_L / lfunlambda = ", xiL / lfunlambda(L, s));
quit;
