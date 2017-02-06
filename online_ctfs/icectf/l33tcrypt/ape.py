#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-08-19 17:10:31
# @Last Modified by:   john
# @Last Modified time: 2016-08-21 12:59:08


from pwn import *
from colors import *
import base64 as b
from time import sleep
from string import printable
from string import *

context.log_level = 'error'

printable = "_}" + ascii_lowercase + ascii_uppercase + digits + punctuation 

# This generated the flag
flag = list('IceCTF{unleash_th3_Blocks_aNd_find_what_you_seek}')
# flag = list('')
print flag
# exit()
# flag = ['I','']
host = 'l33tcrypt.vuln.icec.tf'
port = 6001

prefix = 'l33tserver please'


def s_send( message ):
	print B("".join(flag))
	print B("sending:" + message)
	received = False
	data_back = ""
	while ( not received):
		s = tubes.remote.remote(host, port )
		s.recv()
		s.recv()
		sleep(.7)
		string = prefix + message	
		to_send = b.b64encode(string)
		s.sendline(to_send)
		try:
			got = s.recv()
		except EOFError:
			if ('\x00' in data_back):
				print R("THERE WAS AN EOF CHAR IN IT")

		data_back = got.replace('Your l33tcrypted data:\n', '')
		if ( data_back == "" ):
			print r("  NO ANSWER, trying again")
			received = False
		else:
			print y("  GOT AN ANSWER")
			received = True
			
	if (data_back != ""):	
		return data_back




# gotten =  s_send('a'*62)
# print gotten
# print "78,",repr(b.b64decode(gotten)[78])
# print "79,",repr(b.b64decode(gotten)[79])


initial_number = 62 - len(flag)
while ( initial_number > 11 ):
	print y("intial_number currently " + str(initial_number))
	sending = 'a'*initial_number
	gotten =  s_send(sending)
	print gotten
	print y("FOR NUMBER " + str(initial_number))

	needed_chars = b.b64decode(gotten)[76:79]


	print y("WE NEED: " + ",".join(needed_chars))
	the_goal = needed_chars

	for character in printable:

		get = s_send( sending + "".join([c for c in flag]) + character )
		important_chars = b.b64decode(get)[76:79]

		print y("we see important characters: " + ",".join(important_chars))

		# for ic in important_chars:
		# 	if ic in needed_chars:
		# 		found_an_important_character = True
		# 		break

		
		# if important_char == the_goal:
		if important_chars == needed_chars:
			print g("we found char: " + character)

			flag.append(character)
			initial_number -= 1
			break

	# print G(flag)
	print G("".join(flag))



# print G(flag)
print G("".join(flag))