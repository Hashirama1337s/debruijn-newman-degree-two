# BAR-A6 — sealed decisive run of the right-tail lemma (TAIL-LEMMA.md), t = 21/50, eps = 1/5

(BAR-A5 is the rate probe of 10-28, so this is A6.) Sealed before the run. Parameters were chosen from an
exploratory, non-certificate scan (explore_start.py): eps = 1/5 had the best margin, positive from x of about 7000.

Claim tested: H_{21/50}(x+iy) != 0 for all x >= 7200 and y in [0.374, 0.4].
Engine: own Python (tail_cert.py, tail_run.py), mpmath.iv interval arithmetic throughout. The cross-check uses the
certified evaluator cert_core.py (gmpy2 balls).

## Predictions (all required for HOLDS)
- A: adaptive T-boxes cover [3600, 1e12] (x in [7200, 2e12]) with 8 y-subboxes each. Every box gives a certified
  margin > 0, and no box width falls below 2^-16.
- B: the Step 10 asymptotic check at T1 = 1e12 passes: 1 - P1 - P2 > P3 + ... + P7, and Lam - delta exceeds every
  vertex.
- C: at x = 7200, y = 0.374, the certified lower bound |gamma(S0)| * margin is <= the certified |H| from the
  evaluator. This is the consistency control: the lemma cannot claim more than the true size.
- Time: under 30 min (reported).
Score: HOLDS iff A, B, C. Even if HOLDS, nothing is "proved" before a referee read of TAIL-LEMMA.md + code.

## Hashes
581e7bdacea30ae891d7fc536cb0488ecd709cf0c304e1238650db0a5431b3c5 *TAIL-LEMMA.md
0392c1d3635cea37f23b459271394436c6bbbdc4bebddcc20c8be2c71d0cd87c *tail_cert.py
2184c3de36446bd76d4e7924e287926c92b4e59d682d1327940e810a85ada00a *tail_run.py
3c5f7f2b4ff148c1b380f6da8022e7c29e565c08491895c04fd3a41d679836df *../cert/cert_core.py
