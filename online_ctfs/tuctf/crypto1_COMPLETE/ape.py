#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-13 20:11:13
# @Last Modified by:   john
# @Last Modified time: 2016-05-13 20:22:49

from morsecode import *
from pwnlib import *
import re 
from colorama import *

init(autoreset=True)

host='146.148.102.236'
port = 24069

s = tubes.remote.remote(host, port)

while True:
	print Fore.YELLOW + s.recv()
	s.sendline('garbage')
	task = s.recv()
	morse = re.findall('What is (.*)  decrypted?', task)[0]

	send_back = ' '.join( [ decodeMorse(word) for word in morse.split('   ') ] )

	print Fore.GREEN + Style.BRIGHT + send_back
	s.sendline(send_back)

s.close()