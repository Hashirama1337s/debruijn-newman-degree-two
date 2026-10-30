#!/bin/bash
# run_pieces45.sh -- BAR-A14-AMEND1 lane runner. Nine lanes; lane k starts only after worker k of run_finite45.sh has
# finished both of its walks (its g45_tk.log gets an "exit" line), so at most 9 walkers ever run. Each lane then claims
# pieces from pieces45.txt (largest x first) with an atomic mkdir claim, skipping pieces whose .json already exists.
# Restart-safe: rerun this script after a pause; a fresh claim directory is used and unfinished pieces resume from
# their own checkpoints (cert_wind_ckpt.py). Final AMEND1 combine -> g45b_combine.log.
cd "$(dirname "$0")"
SESSION=q45_claims_$(date +%s); mkdir -p "$SESSION"
walk() { timeout 86400 py -3.11 -I cert_wind_ckpt.py "$1" 19 50 1/2 "$2" 30 25 >> "$1.log" 2>&1; echo "exit $?" >> "$1.log"; }
lane() {
  until grep -q "^exit" "$1" 2>/dev/null; do sleep 60; done
  while read -r name a b; do
    [ -f "$name.json" ] && continue
    if mkdir "$SESSION/$name" 2>/dev/null; then walk "$name" "$b,1/2;$a,1/2"; fi
  done < pieces45.txt
}
for k in 1 2 3 4 5 6 7 8 9; do lane "g45_t$k.log" & done
wait
py -3.11 -I cert_combine45b.py > g45b_combine.log 2>&1
echo ALLDONE >> g45b_combine.log
