#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-02-20 14:23:12
# @Last Modified by:   john
# @Last Modified time: 2016-02-20 14:46:29

import hashlib
from pwnlib import *
from time import sleep
from colorama import *

def trey():

	time = 1455994278 -18*60*60 - 51*60 -18 
	updatedtime = time + h*60*60 + minutes*60 + sec


	for s in range(-60,61):
	    for cint in range(256):
	        if hashlib.sha1(str(updatedtime + s) + ":" + chr(cint)).hexdigest() == "c51a8f7a25330b5f79fce357b6069b415151a24c":
	            print chr(cint)
	            #Time is 18:51:18, 051th day of 2016 +- 30 seconds

	            # SUBTRACT AN HOUR FR

	#1455994278


host = '188.166.133.53'
port = 11117

base_time = 1455994278 -18*60*60 - 51*60 -18 

def get_new_time( hours, minutes, seconds ):

	global base_time
	return  base_time + ( hours - 1) *60*60 + minutes*60 + seconds

flag = []

def main():

	global flag

	connection = tubes.remote.remote( host, port )


	# print Fore.YELLOW, "receiving", connection.recv()
	connection.recv()
	while ( True ):
		response = connection.recv()
		the_hash = response.split()[-1]	

		given_time = response.split()[4][:-1]
		# print given_time

		hours, minutes, seconds = [ int(x) for x in given_time.split(':') ]

		new_time = get_new_time(hours, minutes, seconds)
		# print new_time

		# print the_hash

		for s in range(-60,61):
		    for cint in range(256):
		    	to_send = str(new_time + s) + ":" + chr(cint)
		        if hashlib.sha1(to_send).hexdigest() == the_hash:
		            character = chr(cint)
		            flag.append(character)
		            connection.sendline(to_send)
		            # print Fore.CYAN, "sending", to_send 

		sleep(.06)
		# print Fore.YELLOW, "receiving", connection.recv()
		connection.recv()
		print Fore.GREEN, Style.BRIGHT, ''.join(flag)

	connection.close()

if ( __name__ == "__main__" ):
	main()