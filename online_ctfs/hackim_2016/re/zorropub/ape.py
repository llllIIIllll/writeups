#!/usr/bin/env python

import subprocess
import pwnlib

process = "./zorro_bin"
command = 'echo -e "1\\n{} |"' + process


for i in range( 1000 ):
	p = subprocess.Popen( "./zorro_bin", stdin=subprocess.PIPE, stdout=subprocess.PIPE )
	print p.communicate(input='1\n' + str(i))[0]