# BAR-A13 — sealed rate probe, Lambda <= 0.45 finite region at p = 23: [0, 13000] x [0.374, 0.50], t = 19/50

Code: cert_wind_ckpt.py and cert_core.py (the BAR-A8 versions, unchanged), c = 30. Paths: about 2 units of the
bottom edge, the right side and the top edge at x of about 12950 and of about 6450. Cap 600 s each.

Predictions:
- P1: about 2.5–4.5 s per certified step at x of about 12950 and about 1.2–2.4 s at about 6450 (scaling the BAR-A5/A7
  rates proportionally to x), with 6–14 steps per unit length.
- P2: no certification failures.

ETA = 2 edges x density x integral of (sec/step) dx + builds; wall = CPU / 9.
Launch BAR-A14 only if the ETA range is within about 16 h.

## Hashes
66f9ec6f64fd731ddf4ebda902f912bd6eb63b9f4a7badf3afca3f5b6d412350 *probe_a13.sh
6ba1581587df3ac93ded24df94ab9032f367dce81ee6fc40cfc7bd84df58e22c *cert_wind_ckpt.py
3c5f7f2b4ff148c1b380f6da8022e7c29e565c08491895c04fd3a41d679836df *cert_core.py
