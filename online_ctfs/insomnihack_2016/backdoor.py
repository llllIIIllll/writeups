#!/usr/bin/env python

import time, sys, subprocess

p = subprocess.Popen(('/home/smartcat/readflag', '/home/smartcat/flag2'), stdin=subprocess.PIPE, stdout=subprocess.PIPE)

p.stdin.write('Give me a...')

time.sleep(2)

p.stdin.write('... flag!')

p.wait()

print p.stdout.read()
