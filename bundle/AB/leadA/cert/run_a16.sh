#!/bin/bash
# run_a16.sh -- BAR-A16: high-x positive control and refusal test for THEOREM-A45, one core, sequential.
# Same walker/evaluator and the same arguments as run_finite45.sh / run_pieces45.sh (t = 19/50, ymax 1/2, c = 30,
# chunk 25). Usage: bash run_a16.sh. Refusal path = PARI bracket (12497.9, 12498.0) from a16_pred.txt, sealed in BAR-A16.
cd "$(dirname "$0")"
walk() { timeout 7200 py -3.11 -I cert_wind_ckpt.py "$1" 19 50 1/2 "$2" 30 25 > "$1.log" 2>&1; echo "exit $?" >> "$1.log"; }
walk a16_box "12496,-1/2;12500,-1/2;12500,1/2;12496,1/2;12496,-1/2"
walk a16_refuse "124979/10,0;12498,0"
echo ALLDONE > a16_done.txt
