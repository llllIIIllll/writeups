#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-04-29 21:52:55
# @Last Modified by:   john
# @Last Modified time: 2016-04-29 22:15:28

from colorama import *
import random

p = 4646704883L

init(autoreset=True)

handle = open('winners.txt')
winners = [ int(b) for b in handle.read().split('\n') ]
handle.close()


def attempt():
	o_x = random.randint(0, p)
	o_y = random.randint(0, p)

	# print Fore.CYAN + "using x %d " % o_x
	# print Fore.CYAN + "using y %d " % o_y

	x = (2 * o_x + 3) % p
	y = (3 * o_y + 9) % p
	z = (x ^ y)
	works = True

	for winner in winners:
		if ( z == winner ):
			print z, winner
			continue
		else:
			works = False
			break

	if (works):
		print Fore.GREEN + "%d == %d apparently?" % (z, winner)
		print Fore.GREEN + Style.BRIGHT + "SUCCESS WITH %d and %d" % (o_x, o_y)
		raw_input()
	else:
		print Fore.RED + Style.BRIGHT + "fail with %d and %d" % (o_x, o_y)

	del o_x, o_y, x, y, z

while True:
	attempt()