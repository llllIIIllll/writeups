#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-27 21:02:56
# @Last Modified by:   john
# @Last Modified time: 2016-05-27 23:25:54

data = '241 231 224 241 227 248 173 235 176 220 223 246 241 176 220 174 240 220 235 173 241 220 176 235 173 242 228 229 250 135'


# brute force
# for i in range(255):
# 	print i, ''.join([ chr(((int(x)-i)%255)) for x in data.split() ])

# for i in range(255):
print ''.join([ chr(((int(x)-125)%255)) for x in data.split() ])