#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-04-29 13:27:25
# @Last Modified by:   john
# @Last Modified time: 2016-04-29 22:17:39


import requests
import re
from colorama import *
import random
import html5print

def factor(number):

	number = str(number)

	url = 'http://factordb.com/index.php?query=<QUERY>'
	url = url.replace('<QUERY>', number)

	# print h.beautify( requests.get(url).text )
	pattern = ' = (.*)</td>'
	r =  requests.get(url).text

	factors = []
	match = re.search(pattern, r)
	if (match):

		found =  match.groups(1)[0]
		nums =  found.split('<font color="#000000">')
		for x in nums:
			match = re.search('^(\d*)', x)
			if match:
				factors.append(match.group(1))

		factors = [int(factor) for factor in factors[1:]]
	return factors

	#.replace('<a href="index.php?id=2"><font color="#000000">2^2</font></a> &middot;')


h = html5print.HTMLBeautifier()
url = 'https://giant-goannas.ctfcompetition.com/'

class SecurePrng(object):
    def __init__(self):
        # generate seed with 64 bits of entropy
        self.p = 4646704883L
        self.x = random.randint(0, self.p)
        self.y = random.randint(0, self.p)

    def next(self):
        self.x = (2 * self.x + 3) % self.p
        self.y = (3 * self.y + 9) % self.p
        return (self.x ^ self.y)

s = requests.Session()
r = s.get('https://giant-goannas.ctfcompetition.com/', verify=False)
r = s.get(url + 'start', verify=False)

pattern = 'you drop (\d*) or (\d*)?' 

init(autoreset=True)
count = 0

num = SecurePrng()

while ( True ):

	r = s.get(url + 'lake', verify=False)
	given = r.text
	match =  re.search(pattern, given)

	if ( match ): 

		count += 1
			# print "correct with:", first
		first, second = [ int(m) for m in match.groups() ]
		if ( count > 1 ):
			print Fore.GREEN + Style.BRIGHT + "[SUCCESS] " + Style.NORMAL + "GIVEN %s &- %s WITH Z BEING %s, SENT %s AND RECEIVED %s AND %s" %  ( x, y, z, x, first, second )


		x = first
		y = second

		p = 4646704883L
		x = (2 * x + 3) % p
		y = (3 * y + 9) % p
		z = (x ^ y)

		print Fore.YELLOW + "First:\t\t" + Style.BRIGHT + str(first)
		print Fore.YELLOW + " Factors:\t\t", Fore.YELLOW + Style.BRIGHT + str(factor(first))
		print Fore.YELLOW + "X:\t\t" + str(x)
		print Fore.YELLOW + " Factors:\t\t", Fore.YELLOW  + str(factor(x))
		print Fore.BLUE + "Second:\t\t" + Style.BRIGHT + str(second)
		print Fore.BLUE + " Factors:\t\t", Fore.BLUE +  str(factor(second))
		print Fore.BLUE + "Y:\t\t" + Style.BRIGHT + str(y)
		print Fore.BLUE + " Factors:\t\t", Fore.BLUE + str(factor(y))
		print Fore.MAGENTA + "Z:\t\t" + Style.BRIGHT + str(z)
		print Fore.MAGENTA + " Factors:\t\t", Fore.MAGENTA + str(factor(z))

		sent = s.post( url + 'lake', verify=False, data = {'number': str(first)} )
		given = sent.text
		
	else:
		print Fore.RED + Style.BRIGHT + "failed with ", first
		# print "correct with:", second
		print 
		count = 0
		r = s.get('https://giant-goannas.ctfcompetition.com/', verify=False)
		r = s.get(url + 'start', verify=False)	



	raw_input("Send the first value [hit enter]??")
	print ""