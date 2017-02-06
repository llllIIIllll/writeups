#!/usr/bin/env python

from string import printable, maketrans
import string

import subprocess

# print (lambda j,m:(lambda f,t:t if len(t) <= 1 else j([f(f,x)for x in m(j,m(reversed,(lambda s:zip(*[iter(s)]*(len(s)/2)))(t+"\x01"*(len(t)%2))))]))(lambda f,t:t if len(t) <= 1 else j([f(f,x)for x in m(j,m(reversed,(lambda s: zip(*[iter(s)]*(len(s)/2)))(t+"\x01"*(len(t)%2))))]),raw_input("Plaintext:")))(''.join,map).replace("\x01","")

def get( string ):

	r = subprocess.Popen('./lambda.py', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	r.stdin.write(string + "\n")
	return r.stdout.read().split(":")[-1].strip()

encrypted = 'n1s4_t1An(f1ctdb@mpl_h3)m3lp3y__Eas'

enc_len = len(encrypted)

original = printable[:len(encrypted)]
new = get(original)

t = string.maketrans(original, new)
print string.translate(encrypted, t)

