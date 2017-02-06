#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-09-02 20:24:41
# @Last Modified by:   john
# @Last Modified time: 2016-09-02 21:00:54


from itertools import permutations
from re import findall
from pwn import *

context.log_level = 'error'

host = 'ppc1.chal.ctf.westerns.tokyo'
port = 31111


s = tubes.remote.remote(host, port)
s.recv()

def get_palindrome( string ):
	array = string.split()
	for possib in permutations(array):

		new_string = "".join(possib)
		if new_string == new_string[::-1]:
			return " ".join(possib)
			break



# prompt = " ".join(s.recv().split("\n")[1].split(" ")[2:])
for i in range(30):
	prompt = s.recvuntil("Answer: ")
	# print prompt
	output = re.findall("Judge: (.*)", prompt)
	if ( output ): output = output[0]
	print "output", output
	challenge = re.findall("Input: \d* (.*)", prompt)
	if ( challenge ): challenge = challenge[0]
	# print "challenge", challenge
	palindrome = get_palindrome(challenge)
	# print palindrome
	s.sendline(palindrome)

print s.recv()



# # for i in range(3):
# next_stage = s.recv().split("\n")
# output = next_stage[0]
# print output
# # print next_stage
# next_prompt = " ".join(next_stage[2].split(" ")[2:])
# print next_prompt
# palindrome = get_palindrome(next_prompt)
# print palindrome
# s.sendline(palindrome)
# print s.recv()

# next_stage = s.recv().split("\n")
# output = next_stage[0]
# print output
# # print next_stage
# next_prompt = " ".join(next_stage[2].split(" ")[2:])
# print next_prompt
# palindrome = get_palindrome(next_prompt)
# print palindrome
# s.sendline(palindrome)
# x =  s.recv()

# next_stage = x.split("\n")
# output = next_stage[0]
# print output
# next_prompt = " ".join(next_stage[2].split(" ")[2:])
# print "NEXT", next_prompt
# palindrome = get_palindrome(next_prompt)
# print palindrome
# s.sendline(palindrome)
# print s.recv()

# next_stage = nex.split("\n")
# output = next_stage[0]
# print output
# next_prompt = " ".join(next_stage[2].split(" ")[2:])
# print "NEXT", next_prompt
# palindrome = get_palindrome(next_prompt)
# print palindrome
# s.sendline(palindrome)
# print s.recv()




s.close()