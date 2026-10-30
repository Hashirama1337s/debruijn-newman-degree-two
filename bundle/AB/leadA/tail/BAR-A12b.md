# BAR-A12b — sealed gap tail certificate: x in [12500, 13000], Lambda <= 0.45 at p = 23

Why: the BAR-A13 rate probe put [0, 13000] at 15–18 h, which straddles the ~16 h bar. An exploratory scan (not a
certificate) shows the tail certifies from x = 12500 with 32 y-boxes (minimum margin 16.5; x = 12000 fails at -1.1).
Moving the finite-region end to 12500 brings the ETA to about 14–16.5 h.

Code: tail_run045b.py, a copy of tail_run045.py with T in [6250, 6500], 32 y-subboxes of [0.374, 0.49], initial box
width 1/2048, and the cross-check at x = 12500. The asymptotic part is not needed: x >= 13000 is BAR-A12.
Lemma, tail_cert.py and t = 19/50, eps = 1/5 are unchanged.

## Predictions
- A: all boxes in T in [6250, 6500] certify.
- C: the cross-check at x = 12500 is consistent.
- Time under 30 min.
HOLDS iff A and C.

## Hashes
1441e756c8291387095e31d13a229224c74dad2ddae00a5644ba04f64036b7c7 *tail_cert.py
f4d5e085fe6681baeaa8e755f87440c9f31d68d5094270afbe1967da0b08e505 *tail_run045b.py
3c5f7f2b4ff148c1b380f6da8022e7c29e565c08491895c04fd3a41d679836df *../cert/cert_core.py
