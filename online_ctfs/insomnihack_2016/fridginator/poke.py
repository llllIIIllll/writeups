#!/usr/bin/env python

import requests
import string
import re
from colorama import *

init( autoreset = True )

from random import choice

use = "0123456789abcdef"
url = 'http://fridge.insomnihack.ch/search/'

length = 64

def spin_cookie( cookie_string ):

	cookie_parts = cookie_string[8:].split( ";" )
	#parts = ''.join(cookie_parts.split( "=" )
	
	cookies = {}

	for cookie in cookie_parts:
		pieces = cookie.split("=")
		cookie_name = pieces[0].strip()
		cookie_value = pieces[1].strip()
		cookies[cookie_name] = cookie_value

	return cookies


def generate_random(  ):
	new = []

	for i in range( length ):
		new.append( choice( use ) )

	return ''.join( new )


cookie = spin_cookie('Cookie: csrftoken=9j6kPK5ev49z1GJKiblS6E6lFTIrzfoG; __cfduid=d96476ef05615a42f176fb6737d2d7a3f1453039116; sessionid=3u8bwhcpeo184c6usekt1ty51hoip7us; AWSELB=033F977F02D671BCE8D4F0E661D7CA8279D94E64EF5A76FABBC197672BFCA7C4FFE8F6FC0421FF11CE46A7FB901744E6B352DDFBDE03B83BADF183FB2B6D9CB25E2232D511C1E1B0D40D73F4570425EFDA0F39188D')
session = requests.Session()

top_handle = open("top_error.html")
top = top_handle.read()
top_handle.close()

bottom_handle = open("bottom_error.html")
bottom = bottom_handle.read()
bottom_handle.close()

previous_cleaned = None

while ( True ):

	random = generate_random()
	response = session.get(url + random, cookies = cookie ).text

	print "Using random string: " + Fore.GREEN + random
	if response.startswith( top ) and response.endswith( bottom ):
		cleaned = response.replace(top, "").replace( bottom, "" )
		

		if not cleaned == previous_cleaned:

			if previous_cleaned == None:
				previous_cleaned = cleaned
				continue

			print "The error changed!"
			print Fore.RED + cleaned
			raw_input()
			

		previous_cleaned = cleaned
	else:
		print Fore.YELLOW + reponse
		print Fore.RED + "The page changed!"
		raw_input()

#print response



'''
def attempt( message ):
	page = requests.post(url, [('s',message)])

	return re.findall("</h1>(.*)<form method",page.text[:-30])[0].split()


correct_code = "62 a9 6c 28 0e 33 31 c6 68 cd 66 66 59 46 cc 53 0c 98 31 65 c6 35 c9 a9 60 4e 37 b0 33 46 0d 60 46 26 66 33 cc e6 a9 f6 6c 07 2b 23 af"
correct_code = correct_code.split()


a_flag = 'MMA{f52da776412888170f282a9105d2240061c45dad}'

length_of_flag = len( a_flag )
known_so_far = 'MMA{'
#known_so_far = 'MMA{e75fd59d2c9f9'
# FLAG FOUND TO BE MMA{e75fd59d2c9f9c227d28ff412c3fea3787c1fe73}

initial_position = len(known_so_far)


first = "MMA{" + "a"*40 + "}"
previous_response = attempt(first)


thing = "MMA{" 

previous_response = attempt( thing + "a"*40 + "}"  )

indexes_changed = [[5, 25], [7, 25], [7, 35], [9, 35], [9, 27], [11, 27], [11, 43], [13, 43], [13, 29], [15, 29], [15, 37], [17, 37], [17, 31], [19, 31], [19, 41], [21, 41], [21, 33], [0, 33], [0, 2], [2, 4], [4, 6], [6, 8], [8, 10], [10, 12], [12, 14], [14, 16], [16, 18], [18, 20], [20, 22], [22, 24], [24, 26], [26, 28], [28, 30], [30, 32], [32, 34], [34, 36], [36, 38], [38, 40], [40, 42], [42, 44]]


for i in range(len(indexes_changed)):
	a = indexes_changed[i]

	if (i == len(indexes_changed) - 1):
		# THIS IS THE VERY LAST ONE
		to_change = 44
		for k in range(len(use)):
			character = use[k]
			#print "Testing character ", character, str(k)+"/"+str(len(string.printable))

			try_this = first
			try_this = try_this[:4+i] + character + try_this[4+i+1:] 
			
			print "would send to test", try_this
			response = attempt( try_this )
			#print response

			print response[to_change], " should eventually equal ", correct_code[to_change]
			if ( response[to_change] == correct_code[to_change] ):
			#	print "FOUND THE CORRECT CHARACTER ", character
			#	print "on string", try_this
				first = try_this

			print "THE FINALE SHOULD BE"
			print try_this
			exit()


	try:
		b = indexes_changed[i+1]
	except:
		print "There are no more indexes to run through."
		print try_this
		break


	to_change = a[diff( a,b )[0]]
	
	for k in range(len(use)):
		character = use[k]
		#print "Testing character ", character, str(k)+"/"+str(len(string.printable))

		try_this = first
		try_this = try_this[:4+i] + character + try_this[4+i+1:] 
		
		print "would send to test", try_this
		response = attempt( try_this )
		#print response

		print response[to_change], " should eventually equal ", correct_code[to_change]
		if ( response[to_change] == correct_code[to_change] ):
		#	print "FOUND THE CORRECT CHARACTER ", character
		#	print "on string", try_this
			first = try_this
		

print try_this
'''