# Clean-room rebuild of a representative subset

Moki & Julio (AI-assisted). Supplementary bundle of draft v1 of the zeros note, October 2026.

## In plain words
We copied this bundle into an empty folder on the same PC, installed the Python packages fresh, and reran the README's
Tier 1 commands exactly as written, one at a time. Every output came out the same as the shipped file. Five files came
out byte for byte identical; the others differ only in timing values (seconds), in one error message in the folder
path where the program lives, and in one console file by the lab runner's closing `ALLDONE` line. The coverage combiner again reports HOLDS on the 87 stored walks, and FAILS, flagging the
gap [11000, 11050], when one walk is removed. The high-x positive control again finds exactly 5 zeros and refuses to
walk through one.

**Not rerun:** the 87 finite-region walks of BAR-A14 themselves (13.4 hours on 9 cores, about 120 CPU-hours). They
are shipped as their stored outputs (`AB/leadA/cert/g45_*`), which the combiner, the coverage check, referee 1's audit
and the negative test above read. Also not rerun: README Tiers 2 and 3 (the tail interval runs, the Theorem 1(b) runs,
the PARI prediction for BAR-A16, the outlook runs).

## Set-up
- Fresh folder outside the bundle; this bundle (data files and `README.md`, before `STATUS.md`, `REDACTIONS.md`,
  `CLEANROOM.md`, `LINT.txt`, `SHA256SUMS` and the licence files were added) was copied in. Nothing from the lab tree
  was used. Comparison was against this bundle as shipped.
- Python: a new virtual environment (Python 3.11.9) with `pip install gmpy2==2.3.1 mpmath==1.3.0 numpy==2.4.4` from
  PyPI (gmpy2 reports MPFR 4.2.2, MPC 1.4.0, GMP 6.3.0). The `python` on the PATH was that environment's interpreter
  (checked with `type python` and `sys.executable` before the run). Every program is single-threaded; one process at a
  time; `OMP_NUM_THREADS=OPENBLAS_NUM_THREADS=MKL_NUM_THREADS=1`.
- PARI/GP 2.17.3 (conda-forge build) on Ubuntu 24.04 under WSL2, x86_64, run in the same folder through a small `gp`
  wrapper: one CPU (`taskset -c 0`), `-D nbthreads=1` as in the README command (z3p.gp also sets and prints it), and
  gp's error stream merged into its output stream inside Linux, as on a native Linux shell.
- The README Tier 1 block was extracted from `README.md` and run as one bash script from the copy's root. All
  commands exited as expected (the refusal walk exits 1 by design; every other command 0).
- Before running, the redacted programs were compared with their lab originals: among `.py`, `.gp` and `.sh` files the
  only changed lines are the substitutions listed in `REDACTIONS.md` (sys.path lines P4 x5, the gp wrapper P3 x3); none
  of the programs run here was changed at all.

## Commands (README Tier 1, run from the copy's root)
```
mkdir -p rb
(cd AB/leadA/cert && python -I cert_combine45b.py) > rb/combine.txt
(cd AB/leadA/cert && python -I coverage_report45.py ../../../rb/coverage_report_A14.json)
cp -r AB/leadA/cert rb/negtest && rm rb/negtest/g45_q11000_11050.json
(cd rb/negtest && python -I cert_combine45b.py) > rb/negtest_combine.txt
(cd rb/negtest && python -I coverage_report45.py ../coverage_NEGTEST.json)
python -I AB/leadA/referee45/audit_walks.py AB/leadA/cert > rb/audit_walks.txt
(cd AB/leadA/cert && rm -f g45_p0.ckpt.jsonl g45_p0.json && python -I cert_wind_ckpt.py g45_p0 19 50 1/2 "5,-1/5;15,-1/5;15,1/5;5,1/5;5,-1/5" 30 25 > ../../../rb/g45_p0.log 2>&1)
(cd AB/leadA/tail && python -I addendum_a45_check.py) > rb/addendum_a45_check_out.txt
cd AB/leadA/cert
rm -f a16_box.ckpt.jsonl a16_box.json a16_box.log a16_refuse.log a16_score.json
python -I cert_wind_ckpt.py a16_box 19 50 1/2 "12496,-1/2;12500,-1/2;12500,1/2;12496,1/2;12496,-1/2" 30 25 > a16_box.log 2>&1; echo "exit $?" >> a16_box.log
python -I cert_wind_ckpt.py a16_refuse 19 50 1/2 "124979/10,0;12498,0" 30 25 > a16_refuse.log 2>&1; echo "exit $?" >> a16_refuse.log
python -I score_a16.py
cd ../../..
(cd Z3/lp && gp -q -D nbthreads=1 z3p.gp > ../../rb/z3p_out.txt 2>&1; echo "exit $?" >> ../../rb/z3p_out.txt)
```
Wall times: the combiner, coverage report, negative test and audit about 1 s each; P0 control 2 s; tail Step 10
re-derivation 29 s; BAR-A16 box walk 289 s (logged in the lab: 285 s), refusal walk 81 s; z3p.gp 5 s. About 7 minutes
in total.

## Results
Rule: the README comparison rule (timing values masked; the absolute program path in a Python traceback ignored;
PARI stack-size warnings ignored). sha256 values are shortened to 16 hex digits. "Rebuilt" paths are inside the copy.

| check | rebuilt file | compared with (shipped) | rebuilt sha256 | shipped sha256 | result |
|---|---|---|---|---|---|
| BAR-A14 combine, result | `AB/leadA/cert/g45b_combine.json` | same path | fbb10d181dfe2524 | fbb10d181dfe2524 | byte-identical (= hash in THEOREM-A45-v2): winding 0, value 8.243e-54, radius 4.77e-4, coverage exact on all four edges, 87 walks, 196,660 points, holds true |
| BAR-A14 combine, console | `rb/combine.txt` | `AB/leadA/cert/g45b_combine.log` | c65fd12bcbb9f891 | d5deb96aca94ed04 | PASS: identical to the first two lines; the shipped log has a third line `ALLDONE` written by the lab runner. Last line "BAR-A14 MAIN (AMEND1 combine) => HOLDS" |
| BAR-A14 coverage report | `rb/coverage_report_A14.json` | `AB/leadA/cert/coverage_report_A14.json` | e9e7897661c7bb24 | e9e7897661c7bb24 | byte-identical: bottom 9, top 78, right 1, left 1 intervals, all_ok true |
| coverage negative test, report | `rb/coverage_NEGTEST.json` | `AB/leadA/cert/coverage_report_A14_NEGTEST_piece11000removed.json` | 2d92fe957cc603bf | 2d92fe957cc603bf | byte-identical: missing g45_q11000_11050, top edge not tiled, gap [11000, 11050], all_ok false |
| coverage negative test, combiner | `rb/negtest_combine.txt` | (lab log line: "cert_combine45b => FAILED") | - | - | FAILS as required: "BAR-A14 MAIN (AMEND1 combine) => FAILED" (missing the piece, top coverage false, certified false, holds false) |
| referee 1's walk audit | `rb/audit_walks.txt` | `REFEREE-A45.md` (no stored output) | - | - | as reported by the referee: 87 walks, 196,660 points, `problems []`; quadrature nodes double from 81,921 to 163,841 at x = 10,700 |
| P0 low control, walk | `AB/leadA/cert/g45_p0.json` | same path | 239ec03f4850d165 | fa005aa7286cc08f | PASS (only `secs` differs): argsum = 4π, certified winding 2 |
| P0 low control, checkpoints | `AB/leadA/cert/g45_p0.ckpt.jsonl` | same path | 3b982ae9544c41fd | 09512c87315ea8f7 | PASS (only `secs` differs) |
| tail Step 10 numbers at t = 19/50 | `rb/addendum_a45_check_out.txt` | `AB/leadA/tail/addendum_a45_check_out.txt` | 7653c32c606742a7 | 7653c32c606742a7 | byte-identical (= hash in TAIL-LEMMA-ADDENDUM-A45): Λ(T1) = 13.68, vertices 1.35 / 1.35 / 2.49 / 5.19, error sum 0.1698, "ALL AGREE" |
| BAR-A16 box walk | `AB/leadA/cert/a16_box.json` | same path | 16984bc8362cb204 | 1f5eb88b1b2905fc | PASS (only `secs` differs): argsum 31.41592653589793 (10π) ± 4.24e-18, 84 points: certified winding 5 |
| BAR-A16 box checkpoints | `AB/leadA/cert/a16_box.ckpt.jsonl` | same path | 449a79ecebabc4ad | bf533c42f5daf5ac | PASS (only `secs` differs; all four running argsums identical) |
| BAR-A16 box log | `AB/leadA/cert/a16_box.log` | same path | 0e06bfb86528eb0f | 5dcf450c2ea406ce | PASS (only the build seconds and step times differ): BUILD xb=12500 nodes=163841, exit 0 |
| BAR-A16 refusal walk | `AB/leadA/cert/a16_refuse.log` | same path | 6a191ca21aeda917 | 22cb95535bd75d5b | PASS: "cannot certify step at (262100258943/20971520, 0): hlow=7.55347e-30", exit 1, no JSON; differs only in the build seconds and the traceback's absolute path |
| BAR-A16 verdict | `AB/leadA/cert/a16_score.json` | same path | 909583f5174555ad | f9d46d7a02a47e54 | PASS (only `secs` and the build seconds differ): P1, P2, P3 hold, "HOLDS": true |
| BAR-Z3-P (Lemma P application check) | `rb/z3p_out.txt` | `Z3/lp/z3p_out.txt` | 0829c8142ea22362 | 0829c8142ea22362 | byte-identical (= hash in PROOF-P.md): identity 0/400 failures; key step 0/400 violations, opposite-sign null 374/400; lemma 0/300 violations, null without the 0 233/300; Λ(x² + 1) = 1/2; F1, F3, F4 true |

**Summary: 15 checks; 15 pass (5 byte-identical; 8 identical after masking timing values, the traceback path or the lab
runner's closing `ALLDONE` line; 2 verdict checks with no stored output that match the lab record). No mismatch in any
mathematical output.**

## Notes
- `z3p_out.txt` (shipped and rebuilt alike) begins with a PARI error: gp refuses the script's own definition of
  `derivn` because PARI 2.17 has a built-in function of that name, then continues with the built-in, which has the
  same meaning (lab log line 99 in `seals/SEALS.md`: "gp rejected user 'derivn' (PARI built-in, same semantics,
  checked)"). The verdict lines are unaffected.
- A first pass of the same script had a PATH mistake on our side: the virtual environment was not first on the PATH,
  so the Python steps used the lab's system Python (same versions), and the `gp` wrapper was not found. That pass is
  not counted. The pass reported above started again from a fresh copy. When it was rerun, the z3p command first
  produced a scrambled file: our wrapper relayed gp's two output streams from WSL to Windows separately, so they
  overwrote each other. The wrapper was changed to merge them inside Linux, and that single command was rerun from
  the README. The result above is byte-identical to the shipped file.
- Timing values differ between runs by a few percent (for example 289 s here against 285 s in the lab for the BAR-A16
  box walk); they are not part of any prediction.
