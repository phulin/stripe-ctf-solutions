#!/bin/bash
# run the timing attack on a password starting with $1

rm dict; for i in `seq 1 100`; do echo $i; for j in `seq 1 10`; do ./loop.sh "$1"; done; (cat dict | python dict.py); echo; done
