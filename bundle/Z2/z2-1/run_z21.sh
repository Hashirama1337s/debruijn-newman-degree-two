#!/bin/bash
# run_z21.sh -- BAR-Z2-1, one core, sequential, hard cap 30 min for data (300 s control + 1500 s degree-2 refs).
# Order: degree-1 positive control (WSL PARI 2.17.3, nbthreads 1 printed) -> degree-2 certified references -> scorer.
cd "$(dirname "$0")"
export PYTHONIOENCODING=utf-8 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
date +%T > run_start.txt
timeout 300 gp -q -s 2G z21_ref1.gp > ref1_stdout.txt 2>&1
echo "exit $?" >> ref1_stdout.txt
timeout 1500 py -3.11 -I z21_ref2.py > ref2_stdout.txt 2>&1
echo "exit $?" >> ref2_stdout.txt
timeout 300 py -3.11 -I z21_score.py > score_stdout.txt 2>&1
echo "exit $?" >> score_stdout.txt
date +%T > z21_done.txt
