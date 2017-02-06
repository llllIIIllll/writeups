#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-28 01:44:54
# @Last Modified by:   john
# @Last Modified time: 2016-05-28 01:46:34

from string import ascii_letters, digits
from itertools import permutations

chars = ascii_letters + digits

for item in permutations(chars, 16):
	print ''.join(item)