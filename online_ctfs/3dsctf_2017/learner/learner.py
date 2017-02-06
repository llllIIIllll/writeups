#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-12-21 21:17:30
# @Last Modified by:   john
# @Last Modified time: 2016-12-22 11:30:42


from pwn import *
import re
import random

known_answers = {}
h = open('known_answers.txt')
known_answers = eval(h.read())
h.close()
# possible_answers = [ "3", "2", "4" ]


host = '54.175.35.248'
port = 8001

while ( 1 ):

	s = tubes.remote.remote(host, port)

	first = s.recv()
	to_send = first.split(' ')[-2].replace(':','')
	s.sendline(to_send)

	question = re.findall('Sample 01: (.*?) - Sample 02: (.*)', s.recv())[0]
	s.sendline("A")
	answer = s.recv()
	if 'Wrong' in answer:
		correct_answer = re.findall('The expected answer was: (.*)\n', answer)[0]
		known_answers[question] = correct_answer

	print known_answers
	h = open('known_answers.txt', 'w')
	h.write(str(known_answers))
	h.close()

	s.close()
