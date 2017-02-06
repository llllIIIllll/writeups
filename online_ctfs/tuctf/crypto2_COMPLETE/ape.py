#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-13 20:11:13
# @Last Modified by:   john
# @Last Modified time: 2016-05-13 21:07:17

from morsecode import *
from pwnlib import *
import re 
from colorama import *
import string

init(autoreset=True)


level2_a = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 	"
level2_b = "=>?@ABCDEFnopqrstuvwxyz{|}~ !\"#$%&'(NOPQRSTUVWXYZ[\]^_`abcdefg./0123456789:;<GHIJKLMhijklm)*+,-u"

host='146.148.102.236'
port = 24069

s = tubes.remote.remote(host, port)

while True:
	response = s.recv()
	# print  Fore.YELLOW + response
	if 'level 2' in response:
		print Fore.YELLOW + response
		break
	s.sendline('garbage')
	task = s.recv()
	morse = re.findall('What is (.*)  decrypted?', task)[0]

	send_back = ' '.join( [ decodeMorse(word) for word in morse.split('   ') ] )

	# print Fore.GREEN + Style.BRIGHT + send_back
	s.sendline(send_back)

'''
# LEVEL ONE FLAG
# TUCTF{i_wi11_n0t_5teal}
'''


print "Reached level 2"
while True:
	s.sendline('giant turtle')
	task = s.recv()
	print task
	pattern = re.findall('What is (.*) decrypted?', task)[0]

	decrypted = ''.join([ level2_a[level2_b.index(character)] for character in pattern ])
	print Fore.BLUE + decrypted
	s.sendline(decrypted)

	response =  s.recv()
	print  Fore.YELLOW + response 

'''
# LEVEL TWO FLAG
# TUCTF{c4n_s0me0ne_turn_a_1ight_0n}
'''


s.close()