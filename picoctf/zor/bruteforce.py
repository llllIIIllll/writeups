#!/usr/bin/env python

import pwn


h = open('encrypted')
c = h.read()
h.close()


for i in range(2,100):


	print i, pwn.xor(c, i)

