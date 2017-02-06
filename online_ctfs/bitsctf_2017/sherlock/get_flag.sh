#!/bin/bash
a=`cat final.txt |sed "s/[^A-Z]//g" | tr -d "\n"| sed "s/ZERO/0/g" | sed "s/ONE/1/g"`; python -c "print \"\".join([chr(int(\"$a\"[k:k+8],2)) for k in range(0, len(\"$a\"),8)])"
