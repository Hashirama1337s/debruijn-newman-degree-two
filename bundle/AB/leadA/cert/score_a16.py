"""score_a16.py -- BAR-A16 verdict, exactly as sealed. Reads a16_box.json/.log, a16_refuse.log and a16_pred.txt.
P1: certified winding of the box = N_PRED (|w - N_PRED| + rad/(2 pi) < 0.5), walk exit 0.
P2: the box log shows BUILD xb=12500 nodes=163841 (the high-x regime of BAR-A14 at x >= 10,700).
P3: the refusal walk stops: exit code != 0, no a16_refuse.json, and its log contains "cannot certify step".
Also checks that N_PRED equals the count written in a16_pred.txt (the sealed PARI output)."""
import json, math, os
import gmpy2
from gmpy2 import mpfr
gmpy2.get_context().precision = 192

N_PRED = 5   # from a16_pred.txt (PARI, sealed in BAR-A16)
REFUSE_PATH = "124979/10,0;12498,0"   # PARI bracket 3 (sign change in (12497.9, 12498.0))

res = {}
pred_line = [l for l in open("a16_pred.txt") if l.startswith("signchanges_12496_12500")][0].split()
res["pred_file_count"] = int(pred_line[1])
res["pred_consistent"] = res["pred_file_count"] == N_PRED

blog = open("a16_box.log").read()
ok_exit = blog.strip().splitlines()[-1].strip() == "exit 0"
if os.path.exists("a16_box.json"):
    r = json.load(open("a16_box.json"))
    w = mpfr(r["argsum"]) / (2 * gmpy2.const_pi()); rad = r["argrad"] * (1 + 1e-15)
    n = round(float(w))
    cert = abs(float(w) - n) + rad / (2 * math.pi) < 0.5
    res["P1"] = dict(winding=n, value=float(w), radius=rad, certified=cert, exit0=ok_exit, points=r["points"], secs=r["secs"],
                     holds=bool(cert and ok_exit and n == N_PRED and r["t"] == "19/50" and r["c"] == 30.0))
else:
    res["P1"] = dict(holds=False, why="no a16_box.json", exit0=ok_exit)
builds = [l for l in blog.splitlines() if l.startswith("BUILD")]
res["P2"] = dict(builds=builds, holds=any(l.startswith("BUILD xb=12500 nodes=163841 ") for l in builds))
rlog = open("a16_refuse.log").read()
last = rlog.strip().splitlines()[-1].strip()
res["P3"] = dict(last_line=last, json_written=os.path.exists("a16_refuse.json"),
                 msg=[l for l in rlog.splitlines() if "cannot certify step" in l][-1:],
                 holds=bool(last.startswith("exit ") and last != "exit 0" and not os.path.exists("a16_refuse.json")
                            and "cannot certify step" in rlog))
res["HOLDS"] = bool(res["pred_consistent"] and res["P1"]["holds"] and res["P2"]["holds"] and res["P3"]["holds"])
for k in ("pred_consistent", "P1", "P2", "P3"):
    v = res[k]
    print(k, "HOLDS" if (v if isinstance(v, bool) else v["holds"]) else "FAILED", v)
print("BAR-A16 =>", "HOLDS" if res["HOLDS"] else "FAILED")
json.dump(res, open("a16_score.json", "w"), indent=1)
