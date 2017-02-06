#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-27 23:41:01
# @Last Modified by:   john
# @Last Modified time: 2016-05-27 23:55:22

from itertools import product

it = 'gqxgu{m0g_z_xz3h4i_x1ks3i}'

from string import ascii_lowercase as letters
letters_reversed = letters[::-1]

found = []
for char in it:
	try:
		index = letters.index(char)
		found.append(letters_reversed[index])
	except:
		found.append(char)


print ''.join(found)