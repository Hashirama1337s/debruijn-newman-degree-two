# BAR-A6-AMEND2 — referee (REFEREE-A6) code fixes to the tail checker

Code changes (diff: tail_cert_amend1.py -> tail_cert.py, tail_run_amend1.py -> tail_run.py):
1. The B(.) arguments are rounded downward to floats via nextafter. B is decreasing in sigma, so the upper bound stays
   valid. The partial sums use the same sigma' <= 1+eps.
2. New interval sign check in the E_A split: b_{N+1} < 0 and b_{n_c} <= -b_{N+1}, i.e. |b_n| <= |b_{N+1}| on (N, n_c].
3. New interval sign check in the E_B split: b'_{n_c'} >= -b'_{N+1}, i.e. |b'_n| <= b'_{N+1} on (N, n_c'].

Prediction: no number changes beyond rounding. The re-run of tail_run.py (A boxes, B asymptotic, C cross-check) HOLDS
again with the same box count, to within +-5. The re-run is scheduled after BAR-A8 frees its cores.

## Hashes
1441e756c8291387095e31d13a229224c74dad2ddae00a5644ba04f64036b7c7 *tail_cert.py
11c8d454602341ca2689186a4f4e18e30ad8f966925f63b262be0c4cdfae1837 *tail_run.py
