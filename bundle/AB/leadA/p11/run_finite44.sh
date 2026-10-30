#!/bin/bash
# run_finite.sh -- BAR-A11 (p = 11, N = 44): certified winding of H_{21/50} around R = [0,2800] x [0.374, 0.41], c = 30, 9 workers.
# Each worker walks one bottom chunk (left->right) then the matching top chunk (right->left); worker 9 adds the right
# edge, worker 1 the left edge. Chunk boundaries ~ equal work (cost ~ x): 7200*sqrt(k/9) rounded to multiples of 25.
# Checkpoints every 25 units (cert_wind_ckpt44.py). Re-running this script RESUMES every chunk from its checkpoint.
cd "$(dirname "$0")"
XS=(0 925 1325 1625 1875 2075 2275 2475 2650 2800)
walk() { timeout 43200 py -3.11 -I cert_wind_ckpt44.py "$1" 21 50 1/2 "$2" 30 25 >> "$1.log" 2>&1; echo "exit $?" >> "$1.log"; }
: > fin_pids.txt
for k in 1 2 3 4 5 6 7 8 9; do
  a=${XS[$((k-1))]}; b=${XS[$k]}
  if [ $k -eq 9 ]; then bot="$a,374/1000;$b,374/1000;$b,41/100"; else bot="$a,374/1000;$b,374/1000"; fi
  if [ $k -eq 1 ]; then top="$b,41/100;$a,41/100;$a,374/1000"; else top="$b,41/100;$a,41/100"; fi
  ( walk fin_b$k "$bot"; walk fin_t$k "$top" ) &
  echo "worker $k pid $! bottom [$bot] top [$top]" >> fin_pids.txt
done
wait
py -3.11 -I cert_combine44.py > fin_combine.log 2>&1
echo ALLDONE >> fin_combine.log
