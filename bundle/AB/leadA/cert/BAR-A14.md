# BAR-A14 — sealed certified finite region for Lambda <= 0.45 at p = 23 (f = eta(z)eta(23z)), t = 19/50

## Claim tested
H_{19/50} has no zeros in R = [0, 12500] x [0.374, 0.50]: certified winding number 0 around the boundary of R.
The top edge at 0.50 lies above the de Bruijn edge sqrt(0.24) = 0.48990.

## Method and launch
- Code: cert_wind_ckpt.py and cert_core.py, unchanged from BAR-A8, with c = 30, K = 12, rc = 1.5.
- 9 workers (3 cores left free). Chunk boundaries x = 0, 4175, 5900, 7225, 8325, 9325, 10200, 11025, 11775, 12500.
- Checkpoints every 25 units; re-running run_finite45.sh resumes. Watcher g45_watch.sh.
- ETA (BAR-A13 settled rate, scaled to X = 12500): 14–16.5 h wall.

## Predictions
- P0 (control, run first): the boundary of [5, 15] x [-1/5, 1/5] at t = 19/50 gives certified winding 2, as in
  BAR-A4-AMEND1 at the same t.
- P1: all 18 chunks exit 0, with every step certified.
- P2: the total certified winding is 0.
- P3 (reported): wall time 14–16.5 h.
Score: HOLDS iff P0, P1 and P2.

## Consequence if HOLDS
- BAR-A12 + BAR-A12b (tail x >= 12500, y in [0.374, 0.49]), de Bruijn (Delta = 1 -> |Im z| <= 0.4899 at t = 0.38) and
  symmetry give: no zeros of H_{0.38} with |Im z| >= 0.374.
- So Lambda_psi <= 0.38 + 0.374^2/2 = 0.449938 < 0.45 for L(s, eta(z)eta(23z)).
- This needs a referee read before it is called proved.

## Hashes
dda7ba277d6d5a6ca7d02db32dce931ac26c5a39f95ab62d37b0ea0ffef5d2ba *run_finite45.sh
6ba1581587df3ac93ded24df94ab9032f367dce81ee6fc40cfc7bd84df58e22c *cert_wind_ckpt.py
3c5f7f2b4ff148c1b380f6da8022e7c29e565c08491895c04fd3a41d679836df *cert_core.py
e1bb3a4d8ebcce861a57e6a10e0476de939d1d1f461613db791844ce1a5af3ef *cert_combine45.py
94e489f67d4e9113073dd325cce790925a397e16045a32bdec38e51b127b4c38 *g45_watch.sh
