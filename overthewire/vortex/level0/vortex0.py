#!/usr/bin/env python

import socket
import struct

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.connect( ( 'vortex.labs.overthewire.org', 5842 ) )

ints = []
for i in range( 4 ):

	ints.append( struct.unpack("I", s.recv(4) )[0] )
	# I read in 4 because that is the size of an unsigned integer

total = str( struct.pack( "I", sum(ints) ))
s.send(total)
print s.recv(4096)