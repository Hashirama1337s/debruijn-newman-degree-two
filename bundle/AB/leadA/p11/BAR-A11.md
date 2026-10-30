# BAR-A11 — sealed certified finite region for p = 11 (f = eta(2z)eta(22z), N = 44), t = 21/50

## Claim tested
H_{21/50} (N = 44) has no zeros in R = [0, 2800] x [0.374, 0.41]: certified winding number 0 around the boundary of R.

## Method and launch
- Same walker logic as BAR-A8: cert_wind_ckpt44.py with cert_core44, c = 30, K = 12, rc = 1.5, 192-bit balls.
- 9 workers, chunk boundaries x = 0, 925, 1325, 1625, 1875, 2075, 2275, 2475, 2650, 2800 (equal work).
- Checkpoints every 25 units; watcher fin_watch44.sh.
- The P0 control already HOLDS in BAR-A10 (winding 3).

## Predictions
- P1: all 18 chunks exit 0, with every step certified.
- P2: the total certified winding is 0.
- P3 (reported): wall time 0.7–1.5 h.

## Consequence if HOLDS
- With BAR-A9 (tail, x >= 2800), de Bruijn Thm 13 as quoted in Dobner Thm 3 (Delta = 1 -> |Im z| <= 0.4),
  and symmetry: H_{0.42} (N = 44) has no zeros with |Im z| >= 0.374.
- So Lambda <= 0.489938 for L(s, eta(2z)eta(22z)) as well.
- Same chain as THEOREM-A, with the N = 44 identification from BAR-A9 PARAMS.
- Needs a referee read before being called proved.

## Hashes
91b4d50093159a3080b93e92fab403cfc370720764396718f21cf7b83d06018b *run_finite44.sh
554edc4ca7719accee9c18900fa90fbb1882d20943f08b4d2057b3fbad6046b8 *cert_wind_ckpt44.py
be616cfa23cb833aefe775ac31db5cbfe96628595d45c774d4814b0a6fe98b79 *cert_core44.py
c196066f7b10eaae7bdcf7c56a364bc65de3ccca8ead07b80b3c9baa6049ffda *cert_combine44.py
58d816c4e2babd4c87500ce440050862c6f73d99551a6eb617325d0daa580243 *fin_watch44.sh
