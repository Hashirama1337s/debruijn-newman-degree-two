# BAR-A10 — sealed P0 control + rate probe, p = 11 finite region [0, 2800] x [0.374, 0.41], t = 21/50

Code: cert_wind_ckpt44.py (the AMEND1 walker importing cert_core44), c = 30.
Predictions:
- P0: the boundary of [5, 15] x [-1/5, 1/5] gives certified winding 3, the PARI count of real sign changes of
  H_{21/50} in (5, 15) (refs44.txt, Gaussian average of lfunlambda; zeros near 7.45, 11.0, 14.0).
- P1: at x of about 2750, 0.4–1.2 s per certified step; at about 1400, 0.2–0.7 s; 7–14 steps per unit length.
- P2: no certification failures.
ETA = sum over edges of density x sec/step + builds; wall = CPU / 9. Launch only if the ETA is under 6 h.

## Hashes
554edc4ca7719accee9c18900fa90fbb1882d20943f08b4d2057b3fbad6046b8 *cert_wind_ckpt44.py
be616cfa23cb833aefe775ac31db5cbfe96628595d45c774d4814b0a6fe98b79 *cert_core44.py
6aa90805aa7214543523a0f06758988924a72db680b03784fb4aae081a71d217 *probe_a10.sh
29ebb9f8645a28dd41ea2d6fca7d10234bd0138fd4a4ba4bdae8a1170cdccc92 *refs44.txt
