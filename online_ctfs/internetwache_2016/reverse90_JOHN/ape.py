#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-02-20 19:47:25
# @Last Modified by:   john
# @Last Modified time: 2016-02-21 00:40:34

from itertools import permutations
import requests
import base64

letters = '3DRC3'

possibilities = permutations(letters)

for possibility in possibilities:
	flag = 'IW{' + ''.join(possibility) + '}'
	print flag


# After testing all the possibilties, I found
# IW{3DRC3}
# to work!