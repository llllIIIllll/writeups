#!/usr/bin/env python

from string import ascii_uppercase as plaintext
from pwn import *

encrypted = "ZGUDJORPTOZRROMKJBLZRRVKQBZNSOQROODJIWSCQOOSDHORWWWMQLRDILPGMLDVPLRLRDIMNDCJCQHJPHKLEHDKPUDILLCODLLRDJBMOQKPIOZCLRBMXDHK"
context.log_level = 'error'

host = '104.196.116.141'
port = 49662

s = tubes.remote.remote(host, port)

ZAMBONI = 'ZAMBONI'
CALVINESQU = 'CALVINESQU'

def get_ciphertext( key, plaintext = plaintext ):
	ciphertext = plaintext
	for character in key:
		ciphertext = ciphertext.replace(character, '')
	ciphertext = key + ciphertext
	return ciphertext

def substitute_decrypt( encrypted, ciphertext ):
	decrypted = []

	for character in encrypted:
		try:
			i = ciphertext.index(character)
			decrypted.append( plaintext[i] )
		except:
			pass

	return ''.join(decrypted)

first_line = s.recv().rstrip()
# print first_line
print ""

# The first part...
cipher  = get_ciphertext('ZAMBONI')
print substitute_decrypt(first_line, cipher)
after_xxx = 'CRPSIGPQLCPIWQPSPSIGCFIHNHRMNQMOPJMIOQVIGPPHEIPPSINDCEROQGEAHPSDCYIMO'
other = 'QLRDILPGMLDVPLRLRDIMNDCJCQHJPHKLEHDKPUDILLCODLLRDJBMOQKPIOZCLRBMXDHK'

cipher  = get_ciphertext('CALVINESQU')
print ""
second = substitute_decrypt(after_xxx, cipher)
print second

def substitute_encrypt(string, ciphertext):
	encrypted = []

	for character in string:
		try:
			i = plaintext.index(character)
			encrypted.append( ciphertext[i] )
		except:
			pass

	return ''.join(encrypted)

print ""

cipher  = get_ciphertext('CALVINESQU')
send1 = substitute_encrypt("GEORGEWASHINGTON", cipher)
cipher  = get_ciphertext('ZAMBONI')
send2 = substitute_encrypt(send1, cipher)
print send2

s.sendline(send2)



second_line = s.recv().rstrip()
print second_line

print ""
cipher  = get_ciphertext('ZAMBONI')
a = substitute_decrypt(second_line, cipher)
print a
cipher  = get_ciphertext('CALVINESQU')
b = substitute_decrypt(a, cipher)
print b