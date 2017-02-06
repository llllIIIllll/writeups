#!/usr/bin/env python

import pwn


h = open('encrypted')
c = h.read()
h.close()


print pwn.xor(c, 58)
