# BAR-A12 — sealed tail certificate for Lambda <= 0.45 at p = 23 (f = eta(z)eta(23z))

Lemma: TAIL-LEMMA.md, unchanged. Code: tail_cert.py (AMEND2 state, unchanged) and tail_run045.py, a copy of
tail_run.py with only these parameters changed:
- t = 19/50, eps = 1/5;
- y in [0.374, 0.49] in 16 y-subboxes (the de Bruijn edge at t = 0.38 is sqrt(0.24) = 0.48990);
- boxes from T = 6500 (x = 13000) to 1e12, plus the asymptotic Step 10 at T1 = 1e12;
- cross-check C at x = 13000.
The exploratory scan (explore_045.py, not a certificate) gave a positive margin from x of about 13000 with 16 y-boxes.

Claim tested: H_{19/50}(x+iy) != 0 for x >= 13000 and y in [0.374, 0.49].
Target: Lambda <= 0.38 + 0.374^2/2 = 0.449938, together with the finite region [0, 13000] x [0.374, 0.50]
(BAR-A13/A14).

## Predictions (all required for HOLDS)
- A: all boxes certify, with no width below 2^-16.
- B: the asymptotic check passes.
- C: the cross-check is consistent.
- Time under 45 min.

## Hashes
ad7e96fdc652538f1aaf36839e11cccae80767c93030f31f0d68c43c056e518c *TAIL-LEMMA.md
1441e756c8291387095e31d13a229224c74dad2ddae00a5644ba04f64036b7c7 *tail_cert.py
360a442d82eb667270b2c83bc6137661cfbebb5af6d69897c9c6ee017cce6607 *tail_run045.py
3c5f7f2b4ff148c1b380f6da8022e7c29e565c08491895c04fd3a41d679836df *../cert/cert_core.py
