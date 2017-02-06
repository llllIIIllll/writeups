#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: John Hammond
# @Date:   2016-11-17 14:56:38
# @Last Modified by:   John Hammond
# @Last Modified time: 2016-11-17 20:23:12


handle = open('data.txt')
contents = handle.read()
handle.close()

# contents = contents.replace('0', ' ').replace('1', '#')

def string_to_matrix( string, width ):
	new_string = []
	
	for i in range( 0, len(string) ):
		# print i
		new_string.append( string[i] )

		if ( i % width == 0 ):
			if i == 0: continue
			# print "NEW LINE ????"
			new_string.append('\n')


	return ''.join( new_string )

# for k in range(147, 239):
for i in [1, 3, 7, 21, 49, 147, 239, 717, 1673, 5019, 11711, 35133][5:]:
	print string_to_matrix(contents, i )