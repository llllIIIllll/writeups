#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-04-29 12:48:37
# @Last Modified by:   john
# @Last Modified time: 2016-04-29 13:17:50

import readline
from colorama import *

def mix(a, b, c):

    a -= b+c; a ^= c >> 13
    b -= c+a; b ^=(a <<  8)
    c -= a+b; c ^= b >> 13
    a -= b+c; a ^= c >> 12
    b -= c+a; b ^=(a << 16)
    c -= a+b; c ^= b >>  5
    a -= b+c; a ^= c >>  3
    b -= c+a; b ^=(a << 10)
    c -= a+b; c ^= b >> 15

    print Fore.YELLOW + "A is " + str(a)
    print Fore.BLUE + "B is " + str(b)
    print Fore.GREEN + "C is " + str(c)

while True:
	e = raw_input(Fore."enter nums:" )

	a, b, c = [int(x) for x in e.split()]

	mix(a, b, c)