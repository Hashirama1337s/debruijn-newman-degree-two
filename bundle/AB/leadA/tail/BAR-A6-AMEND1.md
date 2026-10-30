# BAR-A6-AMEND1 — re-seal after BAR-A6 FAILED (implementation gap in the E_B tail)

BAR-A6 failed because box_margin had no branch for b'_{N+1} >= 2a v_B (the E_B tail). It returned "no bound" from
T = 3.58e5. The fix adds the same split already used for E_A:
- (N, n_c']: the (G2) bound with b'_n decreasing and positive, plus Rankin's trick;
- n > n_c': the (G3) tangent.
TAIL-LEMMA Step 7 is extended accordingly (same argument as Step 6). Diff: tail_cert_v1.py -> tail_cert.py.
Predictions and score rule are unchanged from BAR-A6: A (boxes [3600, 1e12]), B (asymptotic T >= 1e12) and C
(cross-check) must all hold. The whole run is redone from T = 3600.

## Hashes
581e7bdacea30ae891d7fc536cb0488ecd709cf0c304e1238650db0a5431b3c5 *TAIL-LEMMA.md
defeb14921acf478fd1afa99e3eadb7a2b70069ef0f82435a269b65994f9af9d *tail_cert.py
2184c3de36446bd76d4e7924e287926c92b4e59d682d1327940e810a85ada00a *tail_run.py
3c5f7f2b4ff148c1b380f6da8022e7c29e565c08491895c04fd3a41d679836df *../cert/cert_core.py
