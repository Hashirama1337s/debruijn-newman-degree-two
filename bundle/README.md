# Supplementary code and data: Explicit de Bruijn–Newman bounds below 1/2 in degree 2, and a product lemma for Dedekind zeta functions

Moki & Julio (AI-assisted). Bundle for draft v1 of the note, October 2026.

## In plain words
This folder holds everything behind the note: the written proof records, the programs, what the programs printed, the
predictions we wrote down and fingerprinted (hashed) before each computation, and the referee reports. You can rerun
the programs yourself and check that they print the same thing. Nothing here has been checked by a human expert; the
proofs were read by AI referees only. `STATUS.md` says, for every claim of the note, how far it has been checked.

The heaviest computation (the certified winding number behind Theorem 1(a), 13.4 hours on 9 cores) is shipped as its
87 stored walk outputs. The combining step that turns them into the result, and its negative test, take seconds and
can be rerun from here; so can the high-x positive control (about 6 minutes), the tail-lemma numbers and the Lemma P
check.

Files that explain how the bundle was made:
- `REDACTIONS.md`: before release we removed the name of the AI product used as a second referee, our machine's folder
  paths and one personal name, in 15 of the 1,001 lab files. Every change is listed there with the file's fingerprint
  before and after. This matters because the hashes quoted inside the lab files were taken on the original bytes.
- `seals/SEALS.md`: every sealed prediction (`BAR-*.md`) in the bundle with the hash recorded at sealing time, and the
  matching seal and score lines of the lab log.
- `CLEANROOM.md`: a rebuild of a representative subset in a fresh folder using only the commands below, and how the
  outputs compared.
- `LINT.txt`: the output of the pre-release checker on this folder (0 findings).
- `SHA256SUMS`: the SHA-256 of every file as shipped (check with `sha256sum -c SHA256SUMS`).

## What each folder is
Section numbers are those of the note.

| claim (note section) | folder | contents | status |
|---|---|---|---|
| Theorem 1(a), f_23 = η(z)η(23z), Λ ≤ 0.449938 (§2.1) | `AB/leadA/` | `THEOREM-A45-v2.md` (the proof record), `REFEREE-A45.md` (referee 1: computations re-audited), `referee2-theorem1a.md` (referee 2: logic) | PROVED (AI-refereed) |
| Step 2, right tail (§2.1) | `AB/leadA/tail/` | `TAIL-LEMMA.md` + `TAIL-LEMMA-ADDENDUM-A45.md` (parameters t = 19/50), `REFEREE-A6.md`; `tail_cert.py`, `tail_run045.py` (BAR-A12, x ≥ 13,000), `tail_run045b.py` (BAR-A12b, 12,500 ≤ x ≤ 13,000), `addendum_a45_check.py` (Step 10 numbers re-derived independently); the failed first tail run BAR-A6 and its amendments | part of Theorem 1 |
| Step 3, finite region (§2.1) | `AB/leadA/cert/` | evaluator `cert_core.py`, walker `cert_wind_ckpt.py`, the 87 walk outputs `g45_*.json/.ckpt.jsonl/.log`, combiner `cert_combine45b.py` + `g45b_combine.json`, coverage report and its negative test, piece generator `amend1_prepare45.py` + `pieces45.txt`, the AMEND1 combiner unit test `amend1_unittest/`, rate probe BAR-A13 (`a13_*`), high-x control BAR-A16 (`a16_*`, PARI prediction `a16_pred.gp`) | part of Theorem 1 |
| referee 1's independent checks (§7) | `AB/leadA/referee45/` | `audit_walks.py` (checkpoint-chain audit of all 87 walks), `gauss_H*.gp` + `job*.gp` (independent PARI values), `labcopy/spot.py`, `neg_drop/` and `neg_dup/` (sharper negative tests of the combiner), `regen/` (piece list regenerated) | referee material |
| Theorem 1(b), f_44 = η(2z)η(22z), Λ ≤ 0.489938 (§2.2) | `AB/leadA/p11/` + `AB/leadA/THEOREM-A11.md` | level-44 copies of evaluator, walker and tail code; seals BAR-A9 (tail), A10 (rate, low control), A11 (finite region), A15 (high-x control); all outputs | PROVED (AI-refereed, one referee read) |
| earlier pipeline record | `AB/leadA/THEOREM-A.md`, `AB/leadA/REFEREE-A4.md`, `AB/leadA/referee2-thmA.md` | the first run of the same pipeline for f_23 at t = 21/50 (Λ ≤ 0.489938), its referee reads | superseded by Theorem 1(a) for f_23; kept for the pipeline record |
| Lemma P and Corollary P♯ (§3), application check (§3.6) | `Z3/` | `PROOF-P.md` (the proof draft that the referee read), `referee2-lemmaP.md` (independent check of identity and sign, prior-art gate), `BAR-Z3-P.md`, `lp/z3p.gp`, `lp/z3p_out.txt` | PROVED (AI-refereed); the note's §3 is the corrected text |
| §5 outlook: main-term fidelity | `Z2/z2-1/` | BAR-Z2-1 (FAILED: writer bug), AMEND1, AMEND2 and the re-run in `run2/`, `RESULT-Z2-1.md` | HEURISTIC |
| §5 outlook: crude envelope E = 0.031 | `Z3/z3-1/`, `Z3/BAR-Z3-1.md`, `Z3/RESULT-Z3-1.md` | `z31_env.py` and outputs | HEURISTIC |
| seals | `seals/SEALS.md` | sealed hashes and the log's seal and score lines | - |

Names used inside the files:
- `BAR-*.md` is a sealed prediction (written and hashed before the run); `BAR-*-AMEND*.md` a hashed change made before
  the data it covers; `RESULT-*.md` a scored outcome; `THEOREM-*.md` a proof record; `REFEREE-*.md` a referee report.
- "Referee 1" (the "local referee" in the files) and "referee 2" (the "second seat") are two independent AI reviewers;
  the product name of referee 2 was removed. "Lead", "seat", "proof seat", "editor seat" and "scout" are roles in the
  lab, not people.
- References of the form "LOG 06:54" point to the lab log, which is not shipped; its seal and score lines are in
  `seals/SEALS.md`. "THEOREM-A45" in the file names is Theorem 1(a) of the note; "A11" and `p11/` are Theorem 1(b)
  (p = 11, level 44).
- `tail_run045_out.json` and `tail_run045b_out.json` carry the label `"t": "21/50"`, which is stale: the code runs at
  t = 19/50 (explained in `THEOREM-A45-v2.md`, "Relabel note"). The hashed outputs were not edited.
- Some files mention lab files that are not shipped (superseded code, watcher scripts, the lab log, third-party PDFs).
  `REDACTIONS.md` lists the not-shipped files that the shipped records quote by hash.
- `AB/leadA/cert/run_finite45.sh` ends by calling `cert_combine45.py`, a deferral stub that is not shipped; the scoring
  combiner is `cert_combine45b.py` (BAR-A14-AMEND1).

## Software
| software | version used for the shipped outputs and the clean-room rebuild |
|---|---|
| Python | 3.11.9 |
| gmpy2 | 2.3.1 (with MPFR 4.2.2, MPC 1.4.0, GMP 6.3.0 as bundled in the PyPI wheel) |
| mpmath | 1.3.0 |
| numpy | 2.4.4 (integer arrays only in `tail_cert.py`: theta-series coefficients and a prime sieve; floating-point arrays only in the heuristic `z31_env.py`) |
| PARI/GP | 2.17.3 (conda-forge build, Ubuntu 24.04 under WSL). Always one thread: `-D nbthreads=1` (most scripts also set it themselves). PARI is used only for predictions and controls, never for a certified step. |

Install the Python packages in a fresh virtual environment: `python -m venv venv`, then
`venv/bin/pip install gmpy2==2.3.1 mpmath==1.3.0 numpy==2.4.4` (on Windows `venv\Scripts\pip`). Several commands use
`python -I`, which ignores user site-packages but sees the virtual environment.

## How to rebuild
Work in a copy of the bundle: several programs write their outputs next to themselves and would overwrite the shipped
files. Keep an untouched copy as the reference. Run every command from the bundle root in a POSIX shell (bash), with
`python` (3.11, the virtual environment above) and `gp` on the PATH. On Windows, gp may run under WSL from the same folder.
The lab's own shell runners (`run_*.sh`) call the Windows launcher `py -3.11`; the commands below are the same
invocations written with `python`.

Comparison rule: an output passes when it equals the shipped file after masking timing values (`"secs": <number>`,
`secs=<number>`, `time <number>s`, `ms=<number>`, `[<number> s]`). Everything else, including every digit of `argsum`,
`argrad`, `value`, `radius` and all margins, must agree. A Python traceback prints the absolute path of the program,
which differs from machine to machine and is ignored. PARI's "increasing stack size" warnings are ignored.

The walker `cert_wind_ckpt.py` resumes from `<name>.ckpt.jsonl` if that file exists, so delete a walk's checkpoint
and JSON before re-running it (the commands below do).

```
mkdir -p rb
```

**Tier 1 (about 7 minutes in total, one core):**
```
# Theorem 1(a), Step 3: combine the 87 stored walks with the exact coverage check (BAR-A14-AMEND1)
(cd AB/leadA/cert && python -I cert_combine45b.py) > rb/combine.txt            # last line "BAR-A14 MAIN (AMEND1 combine) => HOLDS"; rewrites g45b_combine.json (compare)
(cd AB/leadA/cert && python -I coverage_report45.py ../../../rb/coverage_report_A14.json)   # vs AB/leadA/cert/coverage_report_A14.json

# negative test: remove one piece; the combiner must FAIL and the report must flag the gap [11000, 11050]
cp -r AB/leadA/cert rb/negtest && rm rb/negtest/g45_q11000_11050.json
(cd rb/negtest && python -I cert_combine45b.py) > rb/negtest_combine.txt       # last line "... => FAILED"
(cd rb/negtest && python -I coverage_report45.py ../coverage_NEGTEST.json)      # vs AB/leadA/cert/coverage_report_A14_NEGTEST_piece11000removed.json

# referee 1's checkpoint-chain audit of all 87 walks
python -I AB/leadA/referee45/audit_walks.py AB/leadA/cert > rb/audit_walks.txt

# low positive control P0: [5, 15] x [-1/5, 1/5] at t = 19/50, certified winding 2 (about 1 s)
(cd AB/leadA/cert && rm -f g45_p0.ckpt.jsonl g45_p0.json && python -I cert_wind_ckpt.py g45_p0 19 50 1/2 "5,-1/5;15,-1/5;15,1/5;5,1/5;5,-1/5" 30 25 > ../../../rb/g45_p0.log 2>&1)   # vs g45_p0.json

# Theorem 1(a), Step 2: Step 10 numbers of the tail lemma at t = 19/50, re-derived independently
(cd AB/leadA/tail && python -I addendum_a45_check.py) > rb/addendum_a45_check_out.txt    # vs AB/leadA/tail/addendum_a45_check_out.txt ("ALL AGREE")

# BAR-A16, high-x positive control (about 6 minutes): certified winding 5 around [12496, 12500] x [-1/2, 1/2], and a refused walk through a zero
cd AB/leadA/cert
rm -f a16_box.ckpt.jsonl a16_box.json a16_box.log a16_refuse.log a16_score.json
python -I cert_wind_ckpt.py a16_box 19 50 1/2 "12496,-1/2;12500,-1/2;12500,1/2;12496,1/2;12496,-1/2" 30 25 > a16_box.log 2>&1; echo "exit $?" >> a16_box.log
python -I cert_wind_ckpt.py a16_refuse 19 50 1/2 "124979/10,0;12498,0" 30 25 > a16_refuse.log 2>&1; echo "exit $?" >> a16_refuse.log
python -I score_a16.py                                                            # rewrites a16_score.json ("HOLDS": true)
cd ../../..

# Lemma P application check, BAR-Z3-P (a few minutes)
(cd Z3/lp && gp -q -D nbthreads=1 z3p.gp > ../../rb/z3p_out.txt 2>&1; echo "exit $?" >> ../../rb/z3p_out.txt)   # vs Z3/lp/z3p_out.txt
```

**Tier 2 (minutes to an hour each, one core; not rerun in the clean room):**
```
(cd AB/leadA/tail && python -I tail_run045.py > tail_run045_stdout.txt 2>&1)    # BAR-A12, logged 938 s; writes tail_run045.log, tail_run045_out.json
(cd AB/leadA/tail && python -I tail_run045b.py > tail_run045b_stdout.txt 2>&1)  # BAR-A12b, about 4 minutes
(cd AB/leadA/p11 && python -I tail_run44.py > tail_run44_stdout.txt 2>&1)       # BAR-A9 (Theorem 1(b) tail), logged 322 s; writes tail_run.log, tail_run_out.json
(cd AB/leadA/p11 && rm -f a15_null.ckpt.jsonl a15_null.json && python -I cert_wind_ckpt44.py a15_null 21 50 1/2 "2696,-1/2;2700,-1/2;2700,1/2;2696,1/2;2696,-1/2" 30 25 > a15_null.log 2>&1)   # BAR-A15, winding 5
(cd AB/leadA/cert && gp -q -D nbthreads=1 a16_pred.gp > a16_pred_stdout.txt 2>&1)   # BAR-A16 PARI prediction, logged 41 min; writes a16_pred.txt
(cd Z3/z3-1 && python -I z31_env.py > z31_stdout.txt 2>&1)                      # BAR-Z3-1 (outlook)
```
`Z2/z2-1/run2/run_z21_v2.sh` reruns the outlook fidelity test (30-minute cap); its gp line now reads plain `gp`, and its
`py -3.11` calls are the Windows launcher.

**Tier 3 (hours; not rerun):** the finite regions. Theorem 1(b): `bash AB/leadA/p11/run_finite44.sh` (about 35 minutes
on 9 workers; delete `fin_*` first). Theorem 1(a): `bash AB/leadA/cert/run_finite45.sh` launches the 9 workers (bottom chunk, then top chunk);
`python -I amend1_prepare45.py` (in `AB/leadA/cert`, run once before the six superseded top walks start) and
`bash AB/leadA/cert/run_pieces45.sh` then re-split those tops into the 75 pieces, as described in `BAR-A14-AMEND1.md`
(13.4 hours on 9 cores, about 120 CPU-hours; delete `g45_*` first). Both runners use `py -3.11`.
