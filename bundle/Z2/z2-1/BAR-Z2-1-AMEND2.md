# BAR-Z2-1-AMEND2 — writer fix and re-run (sealed before the re-run)

## What happened (BAR-Z2-1 as sealed)
The sealed run finished (22:35:22 -> 22:49:21, references 837 s, 54/54 degree-2 points, control 10/10). Every
degree-2 value in ref2.jsonl is lost: z21_ref2.py wrote numbers with "{:.55e}".format(mpfr), and this gmpy2
build returns the literal template "%.55.6RNe" instead of the number. The scorer (both versions) then stops on the
first record. **BAR-Z2-1 as sealed is scored FAILED (instrument: writer).** No scientific content was read: the values
were never stored.
The pre-seal smoke test missed it because it fed the scorer synthetic JSON and never ran the writer.

## Amendment
- run2/z21_ref2_v2.py = z21_ref2.py with fmt(v) = str(v), which gives gmpy2 at full precision, plus a start-up I/O
  self-check: a 192-bit value near 1e-4259 must round-trip through fmt -> mpmath to 1e-45, else abort. This is a
  positive control on the writer. Diff: run2/amend2_diff.txt.
- run2/z21_ref1.gp: a byte-identical copy (sha256 0d6f6340...), re-run so that both references come from one run.
- Scorer: ../z21_score_amend1.py, unchanged (AMEND1).
- Runner: run2/run_z21_v2.sh, with the same caps (300 s + 1500 s data, 300 s scorer) on one core.
- Grid, predictions, nulls, void rule, MAIN rule: unchanged from BAR-Z2-1.
- Outputs in run2/. The failed run's files are kept as they are in z2-1/.

## Hashes
a6d488b9d0c61f803668981311485d45ab93f9cd615a72ebf1c09526ab46e930 *run2/z21_ref2_v2.py
0d6f634093ae63ea66ffa236be92643bb0f8f315c64395e10b43b46531cc3697 *run2/z21_ref1.gp
36f17a6a51cb3d37c138ab8fdc6dc0cbc7d814585117660775075929de02d722 *run2/run_z21_v2.sh
5fc86740f4cdbb5f173837349b3b94c809a64d4b454357877b3f73c82b7b6c92 *run2/amend2_diff.txt
4111d65de8a186603db45f8bffa9c0f3d16aed51c6ab48ff5fba619967a7a08c *z21_score_amend1.py
bbd199c933ed2f9cfbe6c3d9127d6b1a629a5328dbd08095be9b3e08ac3b264e *z21_core.py
