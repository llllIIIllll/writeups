#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-02-20 14:54:46
# @Last Modified by:   john
# @Last Modified time: 2016-02-21 01:19:24

from pwnlib import *
from colorama import *
from time import sleep

from itertools import permutations

tubes.ssh.context.log_level = 'CRITICAL'

host = '188.166.133.53'
port = 11491

delay = .2

def get_prompt( prompt ):

	return prompt.split(':')[-1].strip()

def rotate_left(array, number):
	return array[number:] + array[:number]

def rotate_right(array, number):
	return array[-number:] + array[:-number]

def main( count = 0 ):

	connection = tubes.remote.remote( host, port )

	print connection.recv()
	sleep(delay)

	prompt = get_prompt( connection.recvuntil(']\n') )

	connection.sendline(prompt)

	print connection.recv()
	sleep(delay)
	prompt = get_prompt( connection.recvuntil(']\n') )
	print prompt


	array = eval( prompt )
	
	if array[1] < array[2]:
		array = [ array[0] ] + rotate_left(array[1:], 1)
		print Fore.YELLOW, array
	else:
		array = [ array[0] ] + rotate_right(array[1:], 1)
		print Fore.RED, array

	to_send = str( array )

	# perms = permutations(array)
	
	# to_send = ''
	# for i in range( count + 1 ):
		
	# 	to_send = str( list(perms.next()) )
	
	# print "SENDING", i, to_send
	connection.sendline(to_send)
	response = connection.recv()
	sleep(delay)

	if 'Yay' in response:
		print Fore.GREEN, response, Fore.RESET
		print connection.recv()
		connection.interactive()
	else:
		print response
		main()

	connection.close()

if ( __name__ == "__main__" ):
	

	# i = 0
	# while (True):

	# 	main( i )
	# 	i += 1

	main()