#!/bin/bash

prefix="$1"

( for i in {a..z} {A..Z} {0..9} ; do echo "$prefix$i" ; /levels/level06 /home/the-flag/.password "$prefix$i"a 2>&1 | ./a.out | grep \\. ; done ) | python process.py