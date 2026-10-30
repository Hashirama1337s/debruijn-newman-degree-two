# BAR-Z2-1-AMEND1 — scorer parser fix (sealed before any scoring)

Found at 22:36 by reading the raw control output ref1.txt (written by the sealed z21_ref1.gp). PARI writes
numbers as "-1.477... E-169", with a space between mantissa and exponent. The sealed z21_score.py splits each line on
whitespace and keeps only 4-token lines, so it would silently drop all 10 control points and score P0 FAILED (empty
control). This would be a conservative failure, never a false pass.

Fix: z21_score_amend1.py is z21_score.py with one change. Each ref1 line is joined (" E" -> "E") before splitting.
The output file name also changes (z21_score_amend1.json) and the docstring is updated. Diff: amend1_diff.txt.
Bars, grid, data and every other line are unchanged.

What had been seen when amending: the raw H values in ref1.txt (control references). No main term or e value had been
computed at any grid point, and no degree-2 reference existed yet (ref2.jsonl empty).

The original z21_score.py still runs at the end of run_z21.sh. Its output (z21_score.json) is kept and reported as
the unamended score. Scoring is by the AMEND1 scorer.

## Hashes
4111d65de8a186603db45f8bffa9c0f3d16aed51c6ab48ff5fba619967a7a08c *z21_score_amend1.py
a0da754ac5d8df2043555584ea775183630e03b0b35bddf17f20ec5de50066d7 *amend1_diff.txt
