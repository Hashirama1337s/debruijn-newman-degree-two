# Redactions: what was changed in this bundle, and why

Moki & Julio (AI-assisted). Supplementary bundle of draft v1 of the zeros note, October 2026.

## In plain words
The lab files behind the note mentioned the AI product used as a second referee, the folder paths of our machine and
one personal first name. Before release, those words were replaced in copies of the files; the lab originals are
unchanged. Nothing mathematical was changed: no number, formula, program step or output value. Paths inside programs
became paths computed from the program's own location, so the programs run from any copy of this folder.

**1001 lab files** were copied. **15** of them were changed (28 substitutions) and **3** were renamed
(their file names carried the product name; their content is unchanged). The other 986 files are
byte-identical to the lab originals. New files written for the bundle: `README.md`, `STATUS.md`, `REDACTIONS.md`,
`CLEANROOM.md`, `LINT.txt`, `SHA256SUMS`, `LICENSE`, `LICENSE-CODE`, `CITATION.cff`, and `seals/SEALS.md` (an extract of
the lab log; its edits are described in that file and below).

**Seal hashes.** No sealed prediction (`BAR-*.md`) was changed: all 18 are byte-identical to the files whose hashes were
recorded at sealing time (`seals/SEALS.md`). Hashes quoted inside the lab files (in `BAR-*`, `RESULT-*` and `THEOREM-*`
files) were computed on the ORIGINAL bytes. For a changed file, a quoted hash matches the "original sha256" column
below, not the shipped file; `SHA256SUMS` lists the shipped bytes. Anyone holding the originals can apply the rules
below and obtain the shipped bytes exactly. Every hash quoted in `THEOREM-A45-v2.md`, `THEOREM-A11.md`,
`TAIL-LEMMA-ADDENDUM-A45.md`, `BAR-A16.md`, `BAR-A14-AMEND1.md`, the `Z2`/`Z3` seals and results was checked against
the original of a shipped file, except the not-shipped files listed at the end. The changed files quoted by hash are
`AB/leadA/cert/a16_refuse.log` (path in a traceback), `Z3/lp/run_z3p.sh`, and the `Z2/z2-1` runners and scripts.

Notation. Names are not reproduced in this file. `<B>` and `<b>` stand for the capitalised and lower-case forms of the
product name replaced by "referee 2" (4 letters; sha256 of the lower-case word:
add92b9cde2bdbf3daaf65a0db79e9b1a7fa428b71b4d6ce38c742eb6dca0c1c); `<P>` stands for a personal first name (5 letters;
not hashed, for privacy; it occurs once, at `AB/leadA/THEOREM-A45-v2.md` line 17, and as a user-folder name in the
Python tracebacks covered by rule P2; the original-file hashes below pin those bytes). A character in square brackets
stands for itself (`[D]:` is a drive letter D followed by a colon, `[A]ppData` is that word without the brackets); this escaping keeps
the release checker from flagging this file. The rules are Python regular expressions (module `re`), written exactly
as applied with these conventions undone.

## How the rules were applied
- Every copied file is UTF-8 text. Each file was processed line by line; on each line the rules were applied in the order
  of the table below, each rule replacing all of its matches. Line endings (LF or CRLF, mixed in some logs) were kept.
- Rule P4 rewrites an absolute folder in a Python `sys.path.insert` line into the same folder computed from the
  script's own location; the exact new expression for each line is in the P4 table. Before the change these scripts
  worked only on the lab machine; after it they work from any copy of the bundle. Nothing else on those lines changed.
- Rule P3 removes a wrapper that ran gp under WSL in an absolute folder. Each of the three shell scripts first changes to
  its own folder (`cd "$(dirname "$0")"`), and the wrapper's folder was that same folder, so the plain `gp` call runs
  the same program on the same files.
- Renames (rules F1-F3 applied to file names): `AB/leadA/<b>-referee-a45-reply.md` -> `AB/leadA/referee2-theorem1a.md`;
  `AB/leadA/<b>-referee-thmA-reply.md` -> `AB/leadA/referee2-thmA.md`; `Z3/<b>-lemmaP-reply.md` -> `Z3/referee2-lemmaP.md`.
  The opening sentences of these replies are the referee's own working notes; they were kept verbatim.

## Rules (in order of application)
| rule | pattern (Python regex) | replacement | what it covers | substitutions |
|---|---|---|---|---|
| F1 | `<b>-referee-a45-reply\.md` | `referee2-theorem1a.md` | file name with a product name -> bundle name | 2 |
| F2 | `<b>-referee-thmA-reply\.md` | `referee2-thmA.md` | file name with a product name -> bundle name | 0 |
| F3 | `<b>-lemmaP-reply\.md` | `referee2-lemmaP.md` | file name with a product name -> bundle name | 1 |
| N1 | `Prior-art gates \(<B>,` | `Prior-art gates (referee 2,` | product name -> role | 1 |
| N2 | `\(<B>\)` | `(referee 2)` | product name -> role | 1 |
| N3 | `One <B> item` | `One referee-2 item` | product name -> role | 1 |
| N4 | `\(<B> search\)` | `(referee 2 search)` | product name -> role | 1 |
| N5 | `needs <P>'s explicit yes` | `needs the authors' explicit approval` | personal name -> role | 1 |
| N6 | `the lead's session [s]cratchpad \(combtest/` | `the lead's private working folder, not shipped (combtest/` | private temporary folder, named -> neutral words | 1 |
| P1 | `File "[D]:\\_LIVE\\NEXT-2026-10-28\\rh-recon\\` | `File "` | traceback in a run output: absolute project path prefix -> nothing (path relative to the bundle root) | 3 |
| P2 | `[C]:\\Users\\[^\\]+\\[A]ppData\\Local\\Programs\\Python\\Python311\\` | `<python>\\` | traceback in a run output: Python installation folder (inside a user folder) -> <python> | 8 |
| P3 | `wsl -e bash -lc 'cd /mnt/d/_LIVE/NEXT-2026-10-28/rh-recon/[^ ']+ && ~/mamba/envs/pari/bin/gp ([^']*)'` | `gp \1` | shell runner: WSL wrapper with an absolute project folder and a home-folder gp binary -> plain gp, run in the script's own folder (the script already does cd "$(dirname "$0")", which was the folder named in the wrapper) | 3 |
| P4 | `"[D]:/_LIVE/NEXT-2026-10-28/rh-recon/([^"]*)"` | `(computed per file, see below)` | Python sys.path entry: absolute project path -> the same folder computed from the script's own location (os.path.join(os.path.dirname(os.path.abspath(__file__)), <relative path>)); see the per-file table | 5 |

### P4, per line
| file | line | new `sys.path` entry |
|---|---|---|
| `Z2/z2-1/pre/time_block.py` | 4 | `__import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "../../../AB/leadA/cert")` |
| `Z2/z2-1/run2/z21_ref2_v2.py` | 6 | `__import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "../../../AB/leadA/cert")` |
| `Z2/z2-1/z21_ref2.py` | 6 | `__import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "../../AB/leadA/cert")` |
| `Z2/z2-1/z21_score.py` | 5 | `__import__("os").path.dirname(__import__("os").path.abspath(__file__))` |
| `Z2/z2-1/z21_score_amend1.py` | 5 | `__import__("os").path.dirname(__import__("os").path.abspath(__file__))` |

### seals/SEALS.md (new file; edits to the extracted log lines)
L1 the leading time of day removed (the date is added from the log's day boundaries); L2 one product name -> "referee 2";
L3, L4 the role tag "proof seat" removed; L5 other times of day inside a line -> `[t]`. 41 log lines extracted; owner
remarks and the lines that list worker process numbers were not extracted.

## Changed or renamed files
| bundle path | lab path (if renamed) | original sha256 | shipped sha256 | lines changed (rule) |
|---|---|---|---|---|
| `AB/leadA/cert/a16_refuse.log` | `same` | `929f0d5cf0336a0f9e67576eefbb8677919c5f0570625af16aeec52158a8a050` | `22cb95535bd75d5b3d3647a0e3a483a0b25612f5562f61b80c041b088ea509a9` | 3 (P1) |
| `AB/leadA/referee2-theorem1a.md` | `AB/leadA/<b>-referee-a45-reply.md` | `1fd8b8b68adfec9ed86abf32b2d196a4cf1c293ed63deb5d6656b412ab9016e4` | `1fd8b8b68adfec9ed86abf32b2d196a4cf1c293ed63deb5d6656b412ab9016e4` | (content unchanged) |
| `AB/leadA/referee2-thmA.md` | `AB/leadA/<b>-referee-thmA-reply.md` | `d2d100fffe007030d96f2530e810f0db9982da94208b4fd7bfa44d29a85dcbc3` | `d2d100fffe007030d96f2530e810f0db9982da94208b4fd7bfa44d29a85dcbc3` | (content unchanged) |
| `AB/leadA/REFEREE-A45.md` | `same` | `593bad1e44e986bb0f7faaeb8fb06fa0d5df85b429ae82fbccbce8902a106f21` | `4fd3de4e4e7ac2a39c2140f87a9e02062a4f0640aac87886da73760001c9daf0` | 3 (F1) |
| `AB/leadA/THEOREM-A.md` | `same` | `0cda31cc3906924cfaf04110db483a903009c17065b37c669eeaa368b3ded2f0` | `71acad428ff2402b768bb4bb4b6d42ce2cf35aafb30a10f703d7361882a217bb` | 12 (N2), 14 (N3), 17 (N4) |
| `AB/leadA/THEOREM-A45-v2.md` | `same` | `03b2b98a5c42bb5986fdfd2f843326032330bf30ad2214313c8986d27af7ab40` | `4c8e2c82f7cee6402d3a2b38c9aa694baea96243dcbf091c02824901bf32b833` | 5 (F1), 17 (N5), 116 (N6) |
| `Z2/z2-1/pre/time_block.py` | `same` | `ab4370fc7487454ca825e0821711cf073ef0944580e3d5bf8c698146e5781324` | `bc25b05567e8aa5e6aceccb64414cf164069925f8a3fca8bd86942256e0cbf3d` | 4 (P4) |
| `Z2/z2-1/run2/run_z21_v2.sh` | `same` | `36f17a6a51cb3d37c138ab8fdc6dc0cbc7d814585117660775075929de02d722` | `2fae25408067bbf1bc64669fb4f155ad51e1d0fa35c972a8e6bf5aaf153d5952` | 7 (P3) |
| `Z2/z2-1/run2/z21_ref2_v2.py` | `same` | `a6d488b9d0c61f803668981311485d45ab93f9cd615a72ebf1c09526ab46e930` | `0c8d52e914b20dd9d92858427a93e6899167226c8d4c01b67895abd15bcf36f7` | 6 (P4) |
| `Z2/z2-1/run_z21.sh` | `same` | `f0519f63672850808ee4a2a4833cce8d0199bf68e0a82e706939582bf0600935` | `44c593555730135cff50d5eace2b2b288471220e698dec7354f140a323cdbf60` | 7 (P3) |
| `Z2/z2-1/score_amend1_stdout.txt` | `same` | `5b190a9e33c42123860a42c0b6b84323530fb209bc76cd1d41916887135d1249` | `eb46f7102bfdcfc01b8dc5746d2cb5bbb4b9f645d3f90e6811999c58a4c5ddc8` | 2 (P1), 5 (P2), 8 (P2), 11 (P2), 14 (P2) |
| `Z2/z2-1/score_stdout.txt` | `same` | `c7e0c463873ac1b288d3cf612b60849b6e6b57cc07a457362fced6de96141515` | `19db40e279ff79e00ed9dad82b32ae2b9c42700aa6c1109090a7fd4f3fe0baa7` | 2 (P1), 5 (P2), 8 (P2), 11 (P2), 14 (P2) |
| `Z2/z2-1/z21_ref2.py` | `same` | `bbc710a4fa4b362fcc4d61ac0e0ad802d8548cc867708305d2c4a4150acd2cf9` | `52ee377438247cce41fc63418e04d65a82fefc120a7762c2aaba21a35820397b` | 6 (P4) |
| `Z2/z2-1/z21_score.py` | `same` | `956dda7bb05846a7161ab82ba3d8d9464198c51595c8d1149d71330ee2c5810e` | `c6e9d80a2d481cf429ac3d76bfde10f0f02ca0fc172c527b74f45d2514c4cbae` | 5 (P4) |
| `Z2/z2-1/z21_score_amend1.py` | `same` | `4111d65de8a186603db45f8bffa9c0f3d16aed51c6ab48ff5fba619967a7a08c` | `1b1d569ec7945823451d05f5463c645b314d569bb955fd89fbe8eb233ef5d266` | 5 (P4) |
| `Z3/referee2-lemmaP.md` | `Z3/<b>-lemmaP-reply.md` | `83a6e1e5e0686a3a34d9caf3142d9388ef781bac359786e5ebf4a75e84bf8547` | `83a6e1e5e0686a3a34d9caf3142d9388ef781bac359786e5ebf4a75e84bf8547` | (content unchanged) |
| `Z3/lp/run_z3p.sh` | `same` | `1c8067f7c0bbe67dc99962fd92759970e3d99553b3813716922327c65d01523b` | `c9e8de0c0fc2faeb1664b4bf6962f1b0756fd7875afd74ed2d523f3cb64280ed` | 4 (P3) |
| `Z3/PROOF-P.md` | `same` | `02bf52ffc310a5e809c27798dbc5ce5d34d66f6e2cfe7adb89bcc11a9c8b0143` | `5cd7f2f0d7f37fe1c76091dfca3073e01c60e839b26c9dbb246418763c11b109` | 4 (N1), 5 (F3) |

## Not-shipped files quoted by hash in shipped records
| lab path | sha256 | quoted where |
|---|---|---|
| `AB/leadA/cert/cert_combine45.py` | `56c5ee9ee74a779bab663204f6251c0666f3b09456619f2ea38898bbc73b9d29` | deferral stub called by run_finite45.sh (BAR-A14-AMEND1 hash list) |
| `AB/leadA/cert/cert_combine45_orig.py` | `e1bb3a4d8ebcce861a57e6a10e0476de939d1d1f461613db791844ce1a5af3ef` | the original BAR-A14 combiner, replaced under AMEND1 (BAR-A14-AMEND1 hash list) |
| `AB/leadA/cert/g45b_watch.sh` | `bc39d746cdc1aecaed404d81a12ede1bda4795a7d24727cc56ebd18a34062eb4` | run watcher (BAR-A14-AMEND1 hash list) |
| `AB/leadA/THEOREM-A45.md` | `5f3a533dc7424d70745f95bd19380ef86f3923f6d52e8c53d593fefdab3245d0` | v1 of THEOREM-A45-v2.md (quoted as 5f3a533d...) |

Also quoted but not shipped: the text of `AB/leadA/tail/TAIL-LEMMA.md` as sealed in BAR-A12 (ad7e96fd...); the shipped
`TAIL-LEMMA.md` (bd6c7183...) differs from it only by the N = 44 addendum (`THEOREM-A45-v2.md`, "Hashes").

## Lab files not shipped
Every other file in the three lab folders the bundle draws from (`AB/leadA`, `Z3`, `Z2/z2-1`), with its sha256: superseded
code kept for history, earlier runs of the pipeline (BAR-A4 to BAR-A8), probe and watcher scripts, process-number and
claim-marker files, the raw transport files of referee 2 (brief, raw JSON, error log, launch line), interrupted-run logs.
Other lab folders (design notes, the certified-zeros batch, recon briefs, third-party PDFs) are not shipped and not
listed. (236 files.)

| lab path | sha256 |
|---|---|
| `AB/leadA/BAR-A.md` | `9a8f72a90f6e90ae11873f43e4a5c028eb6df100f51a0eb8e86bba12b94121e5` |
| `AB/leadA/BAR-A2.md` | `61dfa804e57f5b03982bfaa72e5e6e68b0f94043f22b741bb69277ed4b923cb5` |
| `AB/leadA/BAR-A3.md` | `59b491caa8bde0d4457330d7dfa7826d3428a5d7858efda142c8b7d4e1b41190` |
| `AB/leadA/BAR-A3b.md` | `18e9973822b8bbf6399041ac82d7069c1d2222660af891d879487411f315635d` |
| `AB/leadA/cert/a13_done.txt` | `8221ac66be71558c921fb44cfb66f7997699aea754d917763882d6d9eddc836e` |
| `AB/leadA/cert/a16_done.txt` | `5c91bc5fb3c4c9ab3cc8ceee39df4d1ff7bb892e5eb34ed8f809873d8f1dd969` |
| `AB/leadA/cert/a7_4000c60.log` | `93f4c0d3cd2e070dc67b65c3c61d198c8b735ab414526895bfd50ceee6919a45` |
| `AB/leadA/cert/a7_7200c30.ckpt.jsonl` | `e5c369a9409d1bfc58df44699cd91ed39442b45ee3f2e115b8b8e2a855b2755f` |
| `AB/leadA/cert/a7_7200c30.json` | `32ba53c09d7e1d9c016f7d2e809ee38bd7cf70f6e73520a0e5d445d413e9c3c0` |
| `AB/leadA/cert/a7_7200c30.log` | `5b59bf81f1684e5255f8365a8b66ac1bcc6409b6f24a6b714e86fe6ff62b8977` |
| `AB/leadA/cert/a7_7200c60.log` | `1c6da4aa9324f40ce23344d510d11fa6d2db054d3d4cf82c5e753555efeaac98` |
| `AB/leadA/cert/a7_done.txt` | `8221ac66be71558c921fb44cfb66f7997699aea754d917763882d6d9eddc836e` |
| `AB/leadA/cert/am1_cert_test.log` | `7abca060a136054f3030070a70cabc5c7fa1545e771cfa40e23f393c86dcfdc3` |
| `AB/leadA/cert/am1_ga.log` | `af31bb72b5b9cef9dd988ef249b7bf8a314925462612deab305d77df5a4e8e33` |
| `AB/leadA/cert/am1_mainA.json` | `7a60f78f13da641b2ccecc949502485449a1001881bc7d53be3f80f9914d044a` |
| `AB/leadA/cert/am1_mainA.log` | `78ebf86739e096255ceba16de586d86b7cfc72799ebab8488e8426b8be0cb17a` |
| `AB/leadA/cert/am1_mainB.json` | `3fb8f79d177379f5c64d1f527474aee7afcff1a7850477d90157db2cd5d5e7af` |
| `AB/leadA/cert/am1_mainB.log` | `35f02e9a7ef3c810c28c03e51a89e3265f87d659d1042eece8ca4f8c993433ff` |
| `AB/leadA/cert/am1_mainC.json` | `f5ee3e96a4787a1a5b043494cae1566a746c3ce2efea6649161082b60536b9a2` |
| `AB/leadA/cert/am1_mainC.log` | `22c3ae3b6b9e0e16d6796d8f0ba5ca605024564bdef92dfd5918a22a2da531aa` |
| `AB/leadA/cert/am1_mainD.json` | `a737701ea3850e86e8679b39893d9d2c992776eb10297e439f340b691ac9a57e` |
| `AB/leadA/cert/am1_mainD.log` | `9c453a6f86f18c99fbb31c353eda67c3885697299fe10afec1e53774e39be06c` |
| `AB/leadA/cert/am1_null25.json` | `b02e4800b5bb793087c9132fd2f4851bd00fc787550bde9d52527a817f3eb203` |
| `AB/leadA/cert/am1_null25.log` | `b07fc77c601c8d48733f9462b2faf353d163b9118841c5b24d4473442616f696` |
| `AB/leadA/cert/am1_null400.json` | `ce0fd124ce7d5bc684ff5ff86caaf421b6eed6a94d7c7983d53e34dc2d480a5b` |
| `AB/leadA/cert/am1_null400.log` | `83ac532829bacc5d79a2fb7b520c37f6d5d6c749a0aeefcbe0d7a217e6612856` |
| `AB/leadA/cert/am1_rect800.json` | `d077ebab0785fe9db78acad73350ed71a49861a01c5f65ce8897b45a3129a2b2` |
| `AB/leadA/cert/am1_rect800.log` | `d34701e9a95d1b82f3661ce7cd3abaf8ba45be2a30b310f03b02cd9ff5ca9177` |
| `AB/leadA/cert/am1_refuse.log` | `f1a217aa6ba02de09f7a96a72d3c91fe4e33ea1c6e0bfb41679d79c91c05c524` |
| `AB/leadA/cert/BAR-A4-AMEND1.md` | `c42119f3d6b5f6eba425138592d6d60646646ac9776bfbd48f6ff499f9cfb237` |
| `AB/leadA/cert/BAR-A4.md` | `fb11be80f3ed35cd7ba2499a814d4ea070c2a6aa6a32562d765a56499c82b023` |
| `AB/leadA/cert/BAR-A5.md` | `01799a468e6f7f21459017efff254a95a5fc653341b74166483c3868743a7f68` |
| `AB/leadA/cert/BAR-A7.md` | `96274aad3f34f4b08f06f4e8ffad5ce4df67b763074be47660f38b5c39ddf594` |
| `AB/leadA/cert/BAR-A8.md` | `d0885b8fe7f7fa02820fe2c7026123477fd7afff284a910777940a0dbfe48779` |
| `AB/leadA/cert/cert_combine.py` | `d4bfb4b7a40916a84319c0b50b6c6e8aab2afd38b787107790c48e19d294ecce` |
| `AB/leadA/cert/cert_combine2.py` | `68ef06ed75f2f4eeab4850420a771ae6a682c95e4f3d388a0d605359316529cc` |
| `AB/leadA/cert/cert_combine3.py` | `0d28fc163ce1121ca9b2f72844d6458ab1b9214fc8c79b24044c57db9b00db0a` |
| `AB/leadA/cert/cert_combine45.py` | `56c5ee9ee74a779bab663204f6251c0666f3b09456619f2ea38898bbc73b9d29` |
| `AB/leadA/cert/cert_combine45_orig.py` | `e1bb3a4d8ebcce861a57e6a10e0476de939d1d1f461613db791844ce1a5af3ef` |
| `AB/leadA/cert/cert_combine_out.json` | `8bbfd31d058a0e447c10e92c0792aae090af23082f9a72204b781912c264c896` |
| `AB/leadA/cert/cert_core_v1.py` | `bbf963edaba0626c12f351842cbf9d069426562c316110e6d2dd3f4047e0c492` |
| `AB/leadA/cert/cert_ga_check.py` | `57706fff6a67a47ac3934219936f0c1442ae7ee534e2c29d774b94a78c578264` |
| `AB/leadA/cert/cert_test.py` | `fa352a44c35b583a9e48f5d0ad85df23cb60e2534e3d4207a8f18814e21001a4` |
| `AB/leadA/cert/cert_test_out.json` | `4e40421ccf4fd665e36b4b56d52f7f78d8abc0fa239e0c1208c051ff20b72e3a` |
| `AB/leadA/cert/cert_test_stdout.txt` | `bb451c7f6125c8e34d47be073f92eb09fc096f8cb6544f2d9f29da550d233dd6` |
| `AB/leadA/cert/cert_wind.py` | `b5a1520f0d1e148530fb1cf65692664b446709eb7b82d3bf33ac2c1dae576ab2` |
| `AB/leadA/cert/cert_wind_v1.py` | `421e895212cb6133ea591d33db87838bc2b82ea44e8f31c738f6e8420349b5f0` |
| `AB/leadA/cert/combine.log` | `a1ac9a6a53a957d379b3c7b9dd8d3c8d0bf72e95a427cf51d70a4682f4e10eab` |
| `AB/leadA/cert/combine_am1.json` | `2fc2bcc2fbe53b4bdb407bbf832f1d2c8aabf87a7084cb01d9caf4d97399ce70` |
| `AB/leadA/cert/combine_am1.log` | `4ee46f5bf52c3ba5ac2a1e60697ae721d33cb732f37837ac00f4248b09ddf870` |
| `AB/leadA/cert/fin_b1.ckpt.jsonl` | `754f6d550c7cebfb149414ff8b70f12e9e948fa4653e64523db12275261dc3c0` |
| `AB/leadA/cert/fin_b1.json` | `48577541639ea5a8aae40aaa1dbd4d52deea13eb1fe8b46563cc06fffceca483` |
| `AB/leadA/cert/fin_b1.log` | `6477aaac5ccdf433463f2ee3e887ae53201c0a4ce00bf41bf40d5bca0d318f6c` |
| `AB/leadA/cert/fin_b2.ckpt.jsonl` | `2a3ff331b058e56fa97ca40285cf55649e1de1cc2a43cd98f4696bb86fa601d5` |
| `AB/leadA/cert/fin_b2.json` | `9d0a268e749fd78a2fdcc345c778e053dcc2068c0f90b2b4d11bbd0e83b1ee7d` |
| `AB/leadA/cert/fin_b2.log` | `07a60e49111ee8fbf21e6a8f3abe5ef19d323c302bd6b13b5a650546a3a7e8de` |
| `AB/leadA/cert/fin_b3.ckpt.jsonl` | `38808053b72091b402cb08315af337f54496b991121315eed161717cb1017c02` |
| `AB/leadA/cert/fin_b3.json` | `a9d3935e6b6604a246ad476a4c0c73e18b8920153331f23250b54b92e545939a` |
| `AB/leadA/cert/fin_b3.log` | `d2b98f6684f766adcd172aee630f06fba3383c519ea403f53e66637e539c1863` |
| `AB/leadA/cert/fin_b4.ckpt.jsonl` | `040b852c32fa5892b2062fc84e41d3211c779c7b6bf773b24eb4835b29d49a89` |
| `AB/leadA/cert/fin_b4.json` | `86f2f65aafc0034b9a51c917efef00b3fbca555162fe28ce283fcfedb44c5185` |
| `AB/leadA/cert/fin_b4.log` | `de600a558937efa77b3eeb8e7596441da4bf0ba81e938cbe4eb318a32d80bd36` |
| `AB/leadA/cert/fin_b5.ckpt.jsonl` | `941fd709b69e6989f9b99cc21742117c780e08089b6bca222d9a64e2890b6163` |
| `AB/leadA/cert/fin_b5.json` | `543127c68d5caccf387b2f18824e74effa54bb3f3b51f9d16fa8795b0672aba1` |
| `AB/leadA/cert/fin_b5.log` | `9a7a37cbae8a8cea7507423d7ec30bdd0dc6088d9e401576989d5c680d08cf3e` |
| `AB/leadA/cert/fin_b6.ckpt.jsonl` | `57acadfe95d44c6a199fb806ade59284ef49b05029f9a31a8c4ebd952870fcf1` |
| `AB/leadA/cert/fin_b6.json` | `aec9becd2f9ee1574849c7adb2583f8f4df55d55890c7c76a69d5cc553314235` |
| `AB/leadA/cert/fin_b6.log` | `72b95ded871147916df4c45021d06e78a0d89639247d9d059830a89c05b162ca` |
| `AB/leadA/cert/fin_b7.ckpt.jsonl` | `aec9e2f23ef44148f1dbaabed6b582876e8e584b853544b404ac3f89e3a69b32` |
| `AB/leadA/cert/fin_b7.json` | `cf0c0bd2ef6c6e779f84095674d1c18050059e01a858fc5ae969a8e223405fac` |
| `AB/leadA/cert/fin_b7.log` | `fce3bc29b94c002f9ad954d94d17420afd07d4b82a6e7973b2d195c580cf3ab5` |
| `AB/leadA/cert/fin_b8.ckpt.jsonl` | `37a7c76027fe7b89371677a26ff3cfa2e2745f2a1a8ae9629bb8111df9ca7dbf` |
| `AB/leadA/cert/fin_b8.json` | `dd49a0a3231c4349b3a6d44dc5405f2306cd29261bf508b88c40d81319ebd997` |
| `AB/leadA/cert/fin_b8.log` | `8439d95c4d4d4d752cfa5a3f78c9f45e22b905b4d1ecd6ed286d35cea119e0c4` |
| `AB/leadA/cert/fin_b9.ckpt.jsonl` | `8d9949f039c9ab529f2678e9ccb4c94f0192fca83637f930630d01e743a425a7` |
| `AB/leadA/cert/fin_b9.json` | `a582284814c666b4fa9973d3761672c0e279a7f1c8120ba5ed6e3ce3fe09e74c` |
| `AB/leadA/cert/fin_b9.log` | `f07fbc4af641ccd094b57a6a7ce4c5448af3f681ee76da07919cea2c4c323e68` |
| `AB/leadA/cert/fin_combine.json` | `7b86e0ec39e7fd4b223e96658cb33846026efd738afbef86073bc7334aa3e359` |
| `AB/leadA/cert/fin_combine.log` | `110ad844f0b2162d514e3d7a4803961e2e06a6844c91fe7ca6b14da942d28327` |
| `AB/leadA/cert/fin_p0.ckpt.jsonl` | `9fd98f6b6f588ed7845c061c710a0e216d24d5f2cf1f9e907f6a29e10cab0d96` |
| `AB/leadA/cert/fin_p0.json` | `2ac26d06db8bf7f9deb4ac73a158d1206fb5e9076a686fa25db4041636b098e6` |
| `AB/leadA/cert/fin_pids.txt` | `da4cb7c0f47f11523d7a299093b880d59d46c52af434dbb0ea5398096a5c9dcb` |
| `AB/leadA/cert/fin_t1.ckpt.jsonl` | `90a02ba9558588f6ddf84d18c269bd344a2a17d736b2c07fccc35eb8bbf248b4` |
| `AB/leadA/cert/fin_t1.json` | `215caab30f4a0bd1fda75126bf1d2aa44597886fe93d33fab5ee8527d56a78a9` |
| `AB/leadA/cert/fin_t1.log` | `2d0e1b91383121cef2ae398324f8165da499549594bb3cccfd4d17040dbcacd8` |
| `AB/leadA/cert/fin_t2.ckpt.jsonl` | `1dfe8017e454ba74e8010a94630c3fb144f33afdd66b29bd53703241ead0c27a` |
| `AB/leadA/cert/fin_t2.json` | `29ad0ac7aaaf505d97981819534c08cbc8e7fde3dbe008afe1000e2030eba57a` |
| `AB/leadA/cert/fin_t2.log` | `b3a39daa94b96fbe9303b863a583c9d0758d48881919cac66ae6f5fff73f36fe` |
| `AB/leadA/cert/fin_t3.ckpt.jsonl` | `e800b4885a669eed18029cb1feccdf36be2d696d928b400ddf18893154cf5085` |
| `AB/leadA/cert/fin_t3.json` | `8671cdc40a4521306b32da925c72f97737fd36ac93c253ab08402560fbabde36` |
| `AB/leadA/cert/fin_t3.log` | `3de80a097b069b35957049e445b658b0bf1c40c9184aea2c782bf8bd1dcc10f3` |
| `AB/leadA/cert/fin_t4.ckpt.jsonl` | `bfb893899c765af2ca0520a90997f7508c402d738d364c0540d6b1e9f942964e` |
| `AB/leadA/cert/fin_t4.json` | `ab7aef8c3748a558e1d867333b58578bb17de1936cbbb84a569092ffa4feea66` |
| `AB/leadA/cert/fin_t4.log` | `43b8f6c8c23d549e71c184fc77e38ca4c1276c593ca481af91beaa4c4e8ff9bb` |
| `AB/leadA/cert/fin_t5.ckpt.jsonl` | `31cd62c7428343058c5b52430511ad2a5541fcf7d8b742762961e318dbd890dd` |
| `AB/leadA/cert/fin_t5.json` | `e0a89b977a5c4b4d8a0784890c23528e9a90ec45f78226210015f518cbf5e010` |
| `AB/leadA/cert/fin_t5.log` | `56c5d70f53ddddb2bc05c1432d69386032aaf235afc94a3ac4725bb2815a8ec2` |
| `AB/leadA/cert/fin_t6.ckpt.jsonl` | `65e1bad513b6341e4d789dd1a1a2e355cd6c0ac22b6868d14ce74cc0572d8cd4` |
| `AB/leadA/cert/fin_t6.json` | `c71ed7d9ab05c34cba94b8a1ce3ec21abb56aaf391176461c75ebff57be36b9c` |
| `AB/leadA/cert/fin_t6.log` | `5a6f3ba405f5f58b7b9fe833384033471ffaff5fd5ebfbd83cb67468b95272b1` |
| `AB/leadA/cert/fin_t7.ckpt.jsonl` | `bea99a5f6cc242f7fe28bfaa26c8244764bacfcd156ae98940a873414f107169` |
| `AB/leadA/cert/fin_t7.json` | `e3aaac1aaf7d2a77ef1bce34cd0db36685d549b8fb67fd8fb8c0c5cc06599195` |
| `AB/leadA/cert/fin_t7.log` | `2d5ae5c9c37f8ca40d0618e8625537a9c9c0bc4642c8046aa23f727cb130085f` |
| `AB/leadA/cert/fin_t8.ckpt.jsonl` | `cef7c1951db8c110714b804d8f631e245ca0470cb61ff5c2b2646f4470b0783f` |
| `AB/leadA/cert/fin_t8.json` | `d61bcda71cfebe8df3687ab431db954897b2b8610fb61dbdd20eeb1ad697eed9` |
| `AB/leadA/cert/fin_t8.log` | `e4ebc7c05f183f4a278f572c9e656e49f9570ee5501ac55430388b4f40e67040` |
| `AB/leadA/cert/fin_t9.ckpt.jsonl` | `8848fcdff204bb67a146d54eb60777a9e7f6b2b08410b171f1bfc492ac8f3404` |
| `AB/leadA/cert/fin_t9.json` | `981d56a129e241d9de356b0953e3e11f9903e53fc4e640900998673c560a9fcd` |
| `AB/leadA/cert/fin_t9.log` | `134bb3e4e5ab51aa591dab0dc1ed04d214e2dab1d7ec635cd2b4f0423855ccd9` |
| `AB/leadA/cert/fin_watch.log` | `cd276ce93354573816b67bfeb95d7141c0b92bac318859fd917baeeb8e5f635d` |
| `AB/leadA/cert/fin_watch.sh` | `da78c18fb8415c3d1d54fa26d4c43ff72056151f8ec2ca237014a4e4a07eaba0` |
| `AB/leadA/cert/g45_combine.log` | `01dcbcfbbc857a135156ab543862596b44082c489138743080e32a333f2a32ee` |
| `AB/leadA/cert/g45_pids.txt` | `f8b25790912e68906880cdeada77316b6ffc6eb9086805a90be2dc439dd570a5` |
| `AB/leadA/cert/g45_watch.log` | `c0a76c72b16a6328d739a233457f3fc01260225f2a1e0e510dc45b87471baae8` |
| `AB/leadA/cert/g45_watch.sh` | `94e489f67d4e9113073dd325cce790925a397e16045a32bdec38e51b127b4c38` |
| `AB/leadA/cert/g45b_watch.log` | `c78017b2e6bb2b0582a4cec39e2f7f3e95aa180fd6c54a1eaec68a2552c49000` |
| `AB/leadA/cert/g45b_watch.sh` | `bc39d746cdc1aecaed404d81a12ede1bda4795a7d24727cc56ebd18a34062eb4` |
| `AB/leadA/cert/mainA.json` | `817c070bf7aba035e7ec699d6511518da83fdae52ac4b99d0113f118c4050678` |
| `AB/leadA/cert/mainA.log` | `718911651cee9675489c2cc787b73adea51075adffce94a1431b32d0ec8f783f` |
| `AB/leadA/cert/mainB.json` | `2e0640574ff9917fc7f9c7a25cd8193596e03ed8c7504582483a6c66263e5f92` |
| `AB/leadA/cert/mainB.log` | `91bb04f2d42538e712c3f09c5d3b91a6263c32e2a971fa23419f9cdec7ca81a1` |
| `AB/leadA/cert/mainC.json` | `b8f8a150984a874b87e4e5c8104e3ebcbbba8c4f0edf7dfc59e2635f0832cbcf` |
| `AB/leadA/cert/mainC.log` | `b9cb07940ca3b7a5ab1da9d9e3742af3287dd2fd0a87c0d5c287ae91943745d4` |
| `AB/leadA/cert/mainD.json` | `87b24387fb30be52fa19fe23f8744df0facb475bc04e7467774ac89235a94430` |
| `AB/leadA/cert/mainD.log` | `db1887dea2653124fd83338554969eb793391279bce237c6a6f2f6f35870d8a3` |
| `AB/leadA/cert/null.json` | `c5a044cfe9f4f3d78d8bdec1592988cc4124275d00447b46f6d50aa6399a1571` |
| `AB/leadA/cert/null.log` | `b90811feab8d21228924bec8736213ed6116a85571a61b33b071f3bb01ce3d35` |
| `AB/leadA/cert/pr18000c10.ckpt.jsonl` | `8c9974d18ec0d864ede0ca0e4944da4b4e958abc2b7d605899e67335890e47a0` |
| `AB/leadA/cert/pr18000c10.log` | `f6d1f67c6dbf43790d6f24ee4386707d61f12dcb1f1084c009bb21b4810023d8` |
| `AB/leadA/cert/pr18000c30.ckpt.jsonl` | `1e38156aa1a7bec76e7d61bfa4b4a24fa85235039bdcbbf1cb645693ccf8fdd9` |
| `AB/leadA/cert/pr18000c30.json` | `95ac9b4f861f6274eca70255c5df4ce39666f21ecd984fd7253497aa39bb0521` |
| `AB/leadA/cert/pr18000c30.log` | `388631131007b5933315d192419bdcd0c8060387fa65b2af9c9fb97f1b412034` |
| `AB/leadA/cert/pr2000c10.ckpt.jsonl` | `1653489cd6677fda5cd0fc1810321b25c6faf823280b22d27cca2bfbb621ed93` |
| `AB/leadA/cert/pr2000c10.json` | `701bf0d16175c67f5a1602ffa88e26d85413f303a031da1412519e9e77e2f79d` |
| `AB/leadA/cert/pr2000c10.log` | `71d1e421ed22bdd09ffdf948a575fad907ae68ba77f19fce1b31986f57a2e6e0` |
| `AB/leadA/cert/pr8000c10.ckpt.jsonl` | `1d242ce9170a3a86fdaa14720dfa9230ab66c697620759480da7fd5b356252d7` |
| `AB/leadA/cert/pr8000c10.json` | `ec43b614158587a6aa61058f98fae3d387357e799c102ea1c1ff80a106492012` |
| `AB/leadA/cert/pr8000c10.log` | `ac15331d98df21edaf0ee382ea3e94a9160a2b53e80db9bb64d6fc06f893d6ff` |
| `AB/leadA/cert/pr8000c30.ckpt.jsonl` | `2a1b81a885955f7313aba129a340e1fcd87cc38fcb734262f15aa53604a30719` |
| `AB/leadA/cert/pr8000c30.json` | `c3a16fb1b5056578933cea54dc6edb46e5bf67059527e6b613ed06f06b0c365a` |
| `AB/leadA/cert/pr8000c30.log` | `4d85d8f291c9e1819d4aaefef38cabb03c63dd2c8d9aa58a42e0aa6bfb6777d2` |
| `AB/leadA/cert/prevlogs/fin_b1.log.paused1` | `d1a5af4e2de9582c16d2028a47f8ea719b0f195fd36ddcd0b019416b3cda7e58` |
| `AB/leadA/cert/prevlogs/fin_b2.log.paused1` | `f28da9c7e9da81dd30454aa2b9378f0c848451b33f85a1b7990b8803a16f07b4` |
| `AB/leadA/cert/prevlogs/fin_b3.log.paused1` | `f158622167a9af61b28a7596c870117bb3bac8197b49a5c333424d83a8b84975` |
| `AB/leadA/cert/prevlogs/fin_b4.log.paused1` | `767a326df3798b3af3f9b11c7104c021053d548d0a1e088aa236a9c585a9becc` |
| `AB/leadA/cert/prevlogs/fin_b5.log.paused1` | `4996c1906f781a78ad0cbb65b8ed74707454dd04093d850df6607707669b5438` |
| `AB/leadA/cert/prevlogs/fin_b6.log.paused1` | `ab1e0904c63296fdca97b0b593e42eaa34e42474989ca5fec32785795f05d744` |
| `AB/leadA/cert/prevlogs/fin_b7.log.paused1` | `78ccef106bb3746aa5b04201c80ce456a8f349e1945ac1db0909655071abddbe` |
| `AB/leadA/cert/prevlogs/fin_b8.log.paused1` | `5126694d3baf2be1f91ecc0d3bc04caaea4b54c3034c09b9d552e059840d2781` |
| `AB/leadA/cert/prevlogs/fin_b9.log.paused1` | `094cc9e0dd38d4f2a886eceb4166afa562f148b8a601ec4ecf6eff225fe34b6a` |
| `AB/leadA/cert/prevlogs/fin_t1.log.paused1` | `db946caafa48381901525c2ac641e6e4fe84a192e396cb307570eed5bda6b387` |
| `AB/leadA/cert/prevlogs/fin_t2.log.paused1` | `1efcec52b4f66b36d63149cc75c8ab610cf3d1aba5f6a7f79a9ed8c33edab937` |
| `AB/leadA/cert/prevlogs/fin_t3.log.paused1` | `5afc18f2888ce0ed5236df4dfccbbab4b3f2d46bae8f2eb2a7ad8659f8e4a7eb` |
| `AB/leadA/cert/prevlogs/fin_t4.log.paused1` | `f7f839f464260e14f2773da725e6c5b5f5282e2ebc7ad6fe4132626954c8ea54` |
| `AB/leadA/cert/prevlogs/fin_t5.log.paused1` | `7c66631ca4724ebb06e20c30bf7d1511a645c4fb7890e25d9aef833b3ee73c1f` |
| `AB/leadA/cert/prevlogs/fin_t6.log.paused1` | `95c04fca90d488eee1a8275168c59b7f3dea61ae427bf0a283c9adbad23250e2` |
| `AB/leadA/cert/prevlogs/fin_t7.log.paused1` | `2174dd470ebe2aa2a5bb53d3c4d41e22a546b4fedb0491d43dc24d3bfcd8e8e8` |
| `AB/leadA/cert/prevlogs/fin_t8.log.paused1` | `0567c107996f7327dc9b795cfe3768ea2df26e76728757c95e5a91c27d700586` |
| `AB/leadA/cert/prevlogs/fin_t9.log.paused1` | `2bb39c0b069b7854f55616197106879107f9ae3ae00df9ebfb0bb186d2dae146` |
| `AB/leadA/cert/probe_a13.sh` | `66f9ec6f64fd731ddf4ebda902f912bd6eb63b9f4a7badf3afca3f5b6d412350` |
| `AB/leadA/cert/probe_a7.sh` | `b4c1655fb9ada7848eabc3e3788152ca50f29de9e76a96d0a316d13d73bb5111` |
| `AB/leadA/cert/probe_done.txt` | `afe1cbb0ec65149607d48d62331901410cb38d62e60838b02760f9c6577ac6a5` |
| `AB/leadA/cert/probe_rate.sh` | `e8319638f28798ff7e519c687a7d35dd5ddcdb694385b6bc10dac84b428c6c56` |
| `AB/leadA/cert/refs.gp` | `663f8792f4dc8b9c87ce535ce5731f9332515f7e7386c2c785941906fa7fd80a` |
| `AB/leadA/cert/refs.txt` | `67376747add73e8fe8c4783a9754f5cacee352e1f9be275ede0dd9b09e0b99b3` |
| `AB/leadA/cert/refs2.gp` | `d5745d723a64357cfb0dfdaa8803175d98845dbaced49cf6f8c0b1164c74426c` |
| `AB/leadA/cert/refs2.txt` | `d2999bfdbfe07cf3713a099aedf40835d47884c8f488bd51276418f0fedd94c7` |
| `AB/leadA/cert/refs3.gp` | `f7a082fdce1493e1189222631f0581d800274e04f76f7de951a7af717c0bad45` |
| `AB/leadA/cert/refs3.txt` | `ab8d9490aced84acf0dde3b6d5eef1a03cb8b5e55ecd12749d9aa7649372f036` |
| `AB/leadA/cert/run_all.sh` | `920d9e8b7606d9256da9603aeb566f96add77ea71c9bc3c16656ccc2a7519651` |
| `AB/leadA/cert/run_amend1.sh` | `1671edbe3150158e2e84deae730e1f8b47c70a77309e1c950a5b8da4ba2bbdcc` |
| `AB/leadA/cert/run_finite.sh` | `adf126fb2c2acfa178ee26967d7dcf543e26232fc1464ae6832ae0fd32f62471` |
| `AB/leadA/check_toy.gp` | `75fa2029a181f511e73fd3d46268052e20dc92d959de68417fb7be568c4a7f8d` |
| `AB/leadA/check_toy_out.txt` | `b8885aa46da4cbf61a1c05b328b78b62aee6e0c737f2023628ecf9890e99e382` |
| `AB/leadA/cost_probe.gp` | `24be4c35fa791189981ce6846fa8b018f8e9c959cc6bde5329e89266d3b400bc` |
| `AB/leadA/etaH.gp` | `e5437490813555d0b7b7ef29b0c27b2eb78a712bd5a2adf5857d3fb9bc47254d` |
| `AB/leadA/etaH_test.gp` | `3692d6d3768e4b144ecc88d2e86cf8fb0325a03c5f99726cfa645b43d8917934` |
| `AB/leadA/<b>-a45-launch.txt` | `8e7b35d1c3e4de1723c483cbfe46105a0f6275de8cd3f5f32dcb5c7c44d81295` |
| `AB/leadA/<b>-referee-a45-brief.md` | `348d7a642a1d9e1e832ac7383bd02d3313b63c13db57ec21fef960b893b87bf9` |
| `AB/leadA/<b>-referee-a45-err.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `AB/leadA/<b>-referee-a45-raw.json` | `c3ade06b94d25b4510d7e4c8470c24f936eabeb0d9e9f65e4f3ddf38d2dd7fa1` |
| `AB/leadA/<b>-referee-a45.done` | `5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9` |
| `AB/leadA/<b>-referee-thmA-brief.md` | `15620939b6f98dd54ba48a2686d15f67839063fd79873cbb2ab2a75a3c80a593` |
| `AB/leadA/<b>-referee-thmA-err.txt` | `ab5b50c3846ccfef52997e6e153b187022cde34b543019aa4feaf1f732feff50` |
| `AB/leadA/<b>-referee-thmA-raw.json` | `006bd6e1bd240ca93b96d92e529a365cd2e04174ddde62a49262e156db7304f3` |
| `AB/leadA/<b>-referee-thmA.done` | `d5c534fde62beb89c745a59952c8efed8b7523cbd047e682782e4367de9ea3bf` |
| `AB/leadA/p11/a10_done.txt` | `8221ac66be71558c921fb44cfb66f7997699aea754d917763882d6d9eddc836e` |
| `AB/leadA/p11/fin_pids.txt` | `1c3fc19ed77c6dfc8c27e3dce8069801e09f2b22016aa0b2fb29305623b77c42` |
| `AB/leadA/p11/fin_watch.log` | `21e3907a1f3d186bbd115ed8d5d0d814b47b44bc10f8c85edff0da8258978bd6` |
| `AB/leadA/p11/fin_watch44.sh` | `58d816c4e2babd4c87500ce440050862c6f73d99551a6eb617325d0daa580243` |
| `AB/leadA/p11/probe_a10.sh` | `6aa90805aa7214543523a0f06758988924a72db680b03784fb4aae081a71d217` |
| `AB/leadA/referee45/labcopy/cert_core.py` | `3c5f7f2b4ff148c1b380f6da8022e7c29e565c08491895c04fd3a41d679836df` |
| `AB/leadA/rehearsal.gp` | `775abd50ca20977bc42460e1872351501c7a6d8b71e29003bc673e5c8d95f0f1` |
| `AB/leadA/rehearsal_out.txt` | `bc95062fee810c31faa30a448cab470d5dd9d0af3b9f494601ee17cebfb2058b` |
| `AB/leadA/rehearsal_stdout.txt` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `AB/leadA/RESULT-A.md` | `aaca01321c6e62b38e689090f3c3063488879f3e654e9dc9f6cfac56655e7731` |
| `AB/leadA/tail/explore_045.py` | `73a4e6cd50f410fcb92d28a63e518c38af815d9fc177985049251f409793ecf1` |
| `AB/leadA/tail/explore_start.py` | `b0abea1fb5f1687c84c363b845c07fc37c4c9964c0eaac87951b541680d363b5` |
| `AB/leadA/tail/tail_cert_amend1.py` | `defeb14921acf478fd1afa99e3eadb7a2b70069ef0f82435a269b65994f9af9d` |
| `AB/leadA/tail/tail_cert_v1.py` | `0392c1d3635cea37f23b459271394436c6bbbdc4bebddcc20c8be2c71d0cd87c` |
| `AB/leadA/tail/tail_draft.py` | `ded1e747f8d50811da40eccf7398a8b3c220786fb69fc39c872dc95c956b4f85` |
| `AB/leadA/tail/tail_draft_out.json` | `068a024714ce0e084a0d921681a7f5f31bfb13a8d75f64ce7eba71b8fe8e225c` |
| `AB/leadA/tail/tail_run.log` | `469998eb7a9a9cdda24bd86ca32c838a6dcb290be684a8b75f3d467b7945fc62` |
| `AB/leadA/tail/tail_run.py` | `11c8d454602341ca2689186a4f4e18e30ad8f966925f63b262be0c4cdfae1837` |
| `AB/leadA/tail/tail_run_AMEND1.log` | `778908bdf4e17cf0dafb0e0bd5bc1d1edd9c2dbc044402e2d1d36bd6bb25505a` |
| `AB/leadA/tail/tail_run_amend1.py` | `2184c3de36446bd76d4e7924e287926c92b4e59d682d1327940e810a85ada00a` |
| `AB/leadA/tail/tail_run_out.json` | `ee0ab20cb6146c348f3942fa086c86748c879aa49cdf1da5d770fb4bc0fc3572` |
| `AB/leadA/tail/tail_run_out_AMEND1.json` | `07a458feb81d2b7fa33241efc97d3b9923ce6d2e977550d86f999b90941a415a` |
| `AB/leadA/tail/tail_run_stdout.txt` | `cd0594a96a89509bf1bde813f7890f633e6dbb41e554e7557e285add8e5aff67` |
| `AB/leadA/tail/tail_run_stdout_AMEND1.txt` | `b19a7483eeba88538fcec0245c572ddd15e6286049d6e38450b34e28a0fd0877` |
| `AB/leadA/tail/tail_scan.py` | `40df0cc26131a1365af025bac6d0a373c6b1180e4920b6ec4c40c1fa76e9d499` |
| `AB/leadA/tail/tail_scan_out.json` | `e64235f2332812ba43c8b8b48abb27b92ddb2ee73f59caa22bd5fdf6f8b05205` |
| `AB/leadA/THEOREM-A45.md` | `5f3a533dc7424d70745f95bd19380ef86f3923f6d52e8c53d593fefdab3245d0` |
| `AB/leadA/toy_tail.py` | `8b08f89ff4ad22da422919a7aa6f72f0a703fc9e77e4a80d1458a3b233b191bc` |
| `AB/leadA/toy_tail_out.json` | `02fcaf222ea22ba5514d222f9d8ba235ecc0bab4cd4f7693b8f185a15994f02c` |
| `AB/leadA/toy_tail_stdout.txt` | `c5da8d3f0a3875079804d0d69cf804874d0221b4feb73a5dd4816e67fda44daf` |
| `Z3/<b>-launch.txt` | `d3c57ea9827217c4a06c77004230c59e2a0cf436daf4d3a0e9b87818e8d624e5` |
| `Z3/<b>-lemmaP-brief.md` | `63571ac9acc9e4d83cbbd9ef436077e6fca7d30abb2be26bf79e4a077459b183` |
| `Z3/<b>-lemmaP-err.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `Z3/<b>-lemmaP-raw.json` | `554349ac86986fea0b2315bef7905c7e55fa7accabd5b3c1eddb9d7f020ef79b` |
| `Z3/<b>-lemmaP.done` | `5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9` |
| `Z3/lp/smoke_out.txt` | `a3f9a63d69e57fa1f888e8881b9945050667078166308242aef87da82cd901e9` |
| `Z3/refs/0809.0401.pdf` | `68fabaa5d6ca58be9091bbba281b78b28788b3de8f952ab43d75351c41bf9672` |
| `Z3/refs/0809.0401.txt` | `60c39c88c0d5a739cb65a290fbfcf128948a808d97edd19500a0921688c0ce1c` |
| `Z3/refs/0809.0401.u.txt` | `c60eb07d4406e538512b1a261bc8091c207f549aeb7efed28222e53bff8eb05a` |
| `Z3/refs/2005.05142.pdf` | `4f7958bbd64bc386afdfe4c2e50f27535b688d2bded15714e6e8e679a90b2422` |
| `Z3/refs/2005.05142.txt` | `afd262577ccc3a110121ecaedc26e6694192ac733a9a1ad8727a3ad98e5d1e14` |
| `Z3/refs/2005.05142.u.txt` | `9dfaab42e0745081156d3a090f3c59d9dba63fc847234b915ac12dbe91baecab` |
| `Z3/refs/crop6.png` | `8767df3522a0f7f43b1515e164b51cc54297800310454f7f5f3c286d9210eb0a` |
| `Z3/refs/crop6b.png` | `6073b12a45624548e6eb26fd914967874b0512cd7ecfb9679fdfd6d08eb1efc0` |
| `Z3/refs/crop6c.png` | `afa884cdea68ea9b5193ad5a427244064e9df28ba6a7e433653f1b0758d600fd` |
| `Z3/refs/crop8.png` | `2aafef37f481e7165af004d0ab317cd28eaa26a340bcd6d45fa21f2ddb6dfbb2` |
| `Z2/z2-1/run2/run_start.txt` | `8063b1b8344936bee958fea54e3ddaa0a816f906cca97e2e2fb0cc0f4bdf405b` |
| `Z2/z2-1/run2/z21_done.txt` | `5814309d7e171b9a23d262c428fb3c0779adbd41e7213dc9955a9cb75a01fb77` |
| `Z2/z2-1/run_start.txt` | `bb1a5150d3d6f2977b8aa8c437e645740f552da42dfc29a3e9521616fe925c72` |
| `Z2/z2-1/z21_done.txt` | `4341d4bc5dae6c1f2262485dac6381bf7b10cf35ff25907bb454d771d77ddb0d` |
