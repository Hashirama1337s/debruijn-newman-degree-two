# BAR-A15 — sealed high-x null control for p = 11 (N = 44), requested by the THEOREM-A11 referee

Box: [2696, 2700] x [-1/2, 1/2] at t = 21/50, in the same 50-unit block regime as the BAR-A11 run (x of about 2700).
Walker: cert_wind_ckpt44.py (cert_core44, c = 30), unchanged from BAR-A11. Runs on 1 core; the BAR-A14 workers are
not disturbed.

Prediction: certified winding 5, the number of real sign changes of H_{21/50} on (2696, 2700) found by the independent
PARI float eta-contour code null44.gp (null44_pred.txt: 2696.42, 2697.28, 2698.14, 2699.0, 2699.84). The prediction
assumes no non-real zeros in |Im z| < 1/2 there.
HOLDS iff the certified winding is exactly 5 and every step certifies.

## Hashes
554edc4ca7719accee9c18900fa90fbb1882d20943f08b4d2057b3fbad6046b8 *cert_wind_ckpt44.py
be616cfa23cb833aefe775ac31db5cbfe96628595d45c774d4814b0a6fe98b79 *cert_core44.py
6900f6e7d60e4ba4a6c070ae3a8b3931fdf312a8b637f4332154c825bcaad07a *null44.gp
983362a947ac429421442093af12b7cd840005f488efd736b55522f2a82445b2 *null44_pred.txt
