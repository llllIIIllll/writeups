#!/bin/bash


# I found this decimal number really easily with Hopper. 
flag=`echo "51239555" | ./rev2 | tail -n 1|rev | cut -d " " -f1|rev`
echo "sctf{${flag}}"
