#!/bin/bash

for i in `seq 32 126`; do printf "\\\\x%x\\n" $i; done | echo -e `cat`