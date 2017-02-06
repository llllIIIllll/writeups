from socket import socket
import sys
from Crypto.Cipher import AES
from key import key
from Crypto.Util import Counter

ctr = Counter.new(16 * 8)
cryptor = AES.new(key, AES.MODE_CTR, counter=ctr)

s = socket()

s.connect((sys.argv[1], 54321))

while True:
	print cryptor.decrypt(s.recv(100300))
	sys.stdout.write(">> ")
	s.send(cryptor.encrypt(raw_input()))
