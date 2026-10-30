#!/bin/bash
# run_z3p.sh -- BAR-Z3-P runner, one core, cap 20 min.
cd "$(dirname "$0")"
timeout 1200 gp -q z3p.gp > z3p_out.txt 2>&1; echo "exit $?" >> z3p_out.txt
