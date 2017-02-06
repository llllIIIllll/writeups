#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-13 20:11:13
# @Last Modified by:   john
# @Last Modified time: 2016-05-13 20:26:42

from morsecode import *
from pwnlib import *
import re 
from colorama import *
from pwnlib import context

init(autoreset=True)

host='146.148.102.236'
port = 24069

s = tubes.remote.remote(host, port)

while True:
	response = s.recv()
	if ( "TUCTF" in response ):
		print response.split('\n')[2]
		exit()

	s.sendline('garbage')
	task = s.recv()
	morse = re.findall('What is (.*)  decrypted?', task)[0]

	send_back = ' '.join( [ decodeMorse(word) for word in morse.split('   ') ] )

	# print Fore.GREEN + Style.BRIGHT + send_back
	s.sendline(send_back)


s.close()