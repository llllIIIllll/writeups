#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-15 00:24:36
# @Last Modified by:   john
# @Last Modified time: 2016-05-15 00:31:33

it = open('locked')
other = open('locked')

it.seek(7696)
other.seek(61751)

count = 0
while True:

	first = it.read(1)
	second = other.read(1)
	# print first, second
	
	if first != second:
		print "ENDS AT COUNT", count
		print first, second
		break
	else:
		print "counting... ", count
		count += 1

it.close()
other.close()

