#!/usr/bin/env python

from scapy.all import *
from itertools import permutations

ports = range(1025, 1034)

possibilities = permutations( ports )

# for possibility in possibilities:
# 	for port in possibility:
for port in ports:
	packet = sr1(IP( dst='felicity.iiit.ac.in') / TCP( dport = port, flags = 'S' ))
	print packet.show()

# packet = sr1(IP( dst='felicity.iiit.ac.in') / TCP( dport = 1025, flags = 'S' ))
# print packet.show()