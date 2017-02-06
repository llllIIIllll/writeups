#!/bin/sh

python carver.py
cat inputs.txt | ./bowie.pl
eog *.gif
