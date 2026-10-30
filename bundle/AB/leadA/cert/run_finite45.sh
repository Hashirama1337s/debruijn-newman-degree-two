#!/bin/bash
# run_finite.sh -- BAR-A14: certified winding of H_{19/50} around R = [0,12500] x [0.374, 0.50], c = 30, 9 workers.
# Each worker walks one bottom chunk (left->right) then the matching top chunk (right->left); worker 9 adds the right
# edge, worker 1 the left edge. Chunk boundaries ~ equal work (cost ~ x): 7200*sqrt(k/9) rounded to multiples of 25.
# Checkpoints every 25 units (cert_wind_ckpt.py). Re-running this script RESUMES every chunk from its checkpoint.
cd "$(dirname "$0")"
XS=(0 4175 5900 7225 8325 9325 10200 11025 11775 12500)
walk() { timeout 86400 py -3.11 -I cert_wind_ckpt.py "$1" 19 50 1/2 "$2" 30 25 >> "$1.log" 2>&1; echo "exit $?" >> "$1.log"; }
: > g45_pids.txt
for k in 1 2 3 4 5 6 7 8 9; do
  a=${XS[$((k-1))]}; b=${XS[$k]}
  if [ $k -eq 9 ]; then bot="$a,374/1000;$b,374/1000;$b,1/2"; else bot="$a,374/1000;$b,374/1000"; fi
  if [ $k -eq 1 ]; then top="$b,1/2;$a,1/2;$a,374/1000"; else top="$b,1/2;$a,1/2"; fi
  ( walk g45_b$k "$bot"; walk g45_t$k "$top" ) &
  echo "worker $k pid $! bottom [$bot] top [$top]" >> g45_pids.txt
done
wait
py -3.11 -I cert_combine45.py > g45_combine.log 2>&1
echo ALLDONE >> g45_combine.log
