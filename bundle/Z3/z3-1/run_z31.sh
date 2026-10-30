#!/bin/bash
# run_z31.sh -- BAR-Z3-1 runner, one core, cap 15 min.
cd "$(dirname "$0")"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONIOENCODING=utf-8
timeout 900 py -3.11 -I z31_env.py > z31_stdout.txt 2>&1; echo "exit $?" >> z31_stdout.txt
