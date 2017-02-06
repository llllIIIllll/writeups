#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-02-20 13:11:32
# @Last Modified by:   john
# @Last Modified time: 2016-02-20 14:01:40

import sympy
from pwnlib import *
from string import printable
from time import sleep

mapping = {}

def generate_mapping():
	
	global mapping

	out = []
	for char in printable:
		q = bin((ord(char)^(2<<4))).lstrip("0b")
		q = "0" * ((2<<2)-len(q)) + q
		out.append(q)
		b = ''.join(out)
		pr = []
		s = ''
		for x in range(0,len(b),2):
			c = chr(int(b[x:x+2],2)+51)
			pr.append(c)
		s = '.'.join(pr)
		#print "'" + s + "' : '" +char + "',"
		mapping[s] = char
		
		out = []

	return mapping

def get_key( find_value ):
	# I use this to get the key I need from my dictionary mapping
	# based off a given value

	global mapping

	for key, value in mapping.iteritems():
		if value == find_value:
			return key


host = '188.166.133.53'
port = 11071

def main():

	generate_mapping()

	connection = tubes.remote.remote( host, port )

	while ( True ):
		print connection.recv()
		sequence = connection.recv()
		print sequence
		sequence = sequence.split(':')[-1].strip()

		part_length = 8
		equation = []
		for i in range( 0,  len( sequence ), part_length ):

			# Get it in the form we need...
			part = sequence[i:i+part_length]

			# Remove the trailing period, if it exists
			if part.endswith('.'): part = part[:-1]
			
			# Skip over the next period
			i +=1

			equation.append( mapping[part] )

		equation =  ''.join(equation)

		# Now solve this equation...
		equation = equation.split(':')[-1].strip()
		left_hand_side, right_hand_side = equation.split('=')

		left_hand_side = sympy.sympify(left_hand_side)
		right_hand_side = sympy.sympify(right_hand_side)

		answer = str(sympy.solve(sympy.Eq(left_hand_side, right_hand_side))[0])
		#print answer


		# Determine the mapped response of what to send back...
		send_back = '.'.join([ get_key(character) for character in answer ] )
		

		connection.sendline(send_back)
		

	connection.close()

if ( __name__ == '__main__' ):
	main()