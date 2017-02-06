#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-13 20:11:13
# @Last Modified by:   john
# @Last Modified time: 2016-05-13 21:58:11

from morsecode import *
from pwnlib import *
import re 
from colorama import *
import string

init(autoreset=True)


level2_a = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 	"
level2_b = "=>?@ABCDEFnopqrstuvwxyz{|}~ !\"#$%&'(NOPQRSTUVWXYZ[\]^_`abcdefg./0123456789:;<GHIJKLMhijklm)*+,-u"


level3_a = "abcdefghijklmnopqrstuvwxyzABCD)*+,-./:;< YZ!\"#$%&'(y$wu"
level3_b = "abcsftdhuneimky;qprggk,qf;AXJE)*+,-./Oo< F:!_#$%&-(jrwl"
a = [',.njrm. ayp.fg', 'ghf kyghukd', 'og. bsogcbl', 'ghf ypacif', 'yd. rpajn.', 'yd. brydcbi', 'myyk chuis', 'mrrb jdcne', 'sykg typdfg alpjk', 'ayp.fg ko imrpt', 'mj ilcespadyk', 'oak. yd. lpcbj.oo', 'ravf ghf ;pukcfrr', 'u ywf jyl', 'erby urpi.y agpfb', 'imrpto jrrn', 'ypf o,cmmcbi', 'duakg glpgif', 'wficymf agpfjl', 'agpfjl vr dmype',  'xaoycab', 'gpj rwummukd', 'pfasukd ur sakdfpylpr', 'mf ngjtepairb', 'icaby ygpyn.', 'p.aecbi co eabi.prgpo', 'upaim.byaycrb', 'c r,. frg']
b = ['welcome atreyu', 'the nothing', 'the nothing', 'the oracle', 'the oracle', 'the nothing', 'moon child', 'moon child', 'dont forget auryn', 'atreyu vs gmork', 'my luckdragon', 'save the princess', 'save the princess', 'i owe you', 'dont forget auryn', 'gmorks cool', 'try swimming', 'giant turtle', 'welcome atreyu', 'atreyu vs gmork',  'bastian', 'try swimming', 'reading is dangerours', 'my luckdragon', 'giant turtle', 'reading is dangerours', 'fragmentation', 'i owe you']
c = []


'''

giant turtle

welcome atreyu
,.njrm. ayp.fg
reading is dangerours
bastian
,.njrm. ayp.fg

try swimming
gmorks cool
fragmentation
upaim.byaycrb

'''



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
	if send_back not in b and send_back not in c:
		print Fore.MAGENTA + send_back
		c.append( send_back )
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
	# print task
	pattern = re.findall('What is (.*) decrypted?', task)[0]

	decrypted = ''.join([ level2_a[level2_b.index(character)] for character in pattern ])
	# print Fore.BLUE + decrypted
	if decrypted not in b and decrypted not in c:
		print Fore.MAGENTA + decrypted
		c.append( decrypted )
	s.sendline(decrypted)

	response =  s.recv()
	if ( "level 3" in response ):
		print  Fore.YELLOW + response 
		break

'''
# LEVEL TWO FLAG
# TUCTF{c4n_s0me0ne_turn_a_1ight_0n}
'''

print "Reached level 3"

while True:
	s.sendline(string.printable[70:80])
	task = s.recv()
	print task
	pattern = re.findall('What is (.*) decrypted?', task)[0]

	if ( pattern in a ):
		sending = b[a.index(pattern)]
		print Fore.BLUE + sending
		s.sendline( sending )

	else:

		decrypted = ''.join([ level3_a[level3_b.index(character)] for character in pattern ])
		print Fore.BLUE + decrypted
		s.sendline(decrypted)

	response =  s.recv()
	print Fore.YELLOW + response

'''
# LEVEL THREE FLAG
# TUCTF{5omething_is_b3tt3r_th4n_n0thing}
'''


s.close()