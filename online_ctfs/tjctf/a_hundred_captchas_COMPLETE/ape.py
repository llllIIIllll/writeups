#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-27 22:11:41
# @Last Modified by:   john
# @Last Modified time: 2016-05-27 23:37:56

import pyfiglet as p
from string import digits, ascii_uppercase, ascii_lowercase
from pwn import *

context.log_level = 'critical'
f = p.Figlet()
characters = digits + ascii_lowercase + ascii_uppercase



mapping = {}
mapping_inverse = {}
def build_mapping():
		
	for character in characters:
		rendered = f.renderText(character)
		# use = '\n '.join(rendered.split('\n'))
		use = '\n ' + rendered
		use = str('\n ' + rendered.replace('\n', '\n ')[:-1])

		mapping[repr(character)] = repr(use)
		mapping_inverse[repr(use)] = repr(character)

build_mapping()

host = 'p.tjctf.org'
port = 8008
c = tubes.remote.remote(host, port)


# --------------------------------------------------

# while True:
for i in range(100):
	print i
	print c.recvuntil('Solve this captcha to continue:')

	given_captcha =  c.recvuntil('>>>')
	print c.recv()


	given_captcha = '\n'.join(given_captcha.split('\n')[:-1])

	columns = {}
	lines = given_captcha.split('\n')
	# for column in range(len(lines[0])):
	# 	for line in  in lines[column]:

	for line in lines:
		column = 0
		for character in line:
			if columns.has_key(column):
				columns[column].append(character)
			else:
				columns[column] = [character]
			column +=1

	def cut_columns(given_captcha, start, end):
		lines = given_captcha.split('\n')

		return '\n'.join([ line[start:end] for line in lines ])

	def get_sections(columns):

		delims = []
		for item in columns:
			if ''.join(columns[item]).strip() == '':
				# print 'delimeter at', item
				delims.append(item)

		delims.append(item+1)	

		return delims

	def get_characters( columns ):

		chars = []
		sections =  get_sections(columns)
		for i in range(len(sections)):
			if i + 1 >= len(sections):
				continue
			else:
				chars.append( cut_columns(given_captcha, sections[i], sections[i+1]) )

		return chars

	each_character = get_characters( columns )

	# print each_character
	def reverse_figlet(each_character):

		revd = []

		for char in each_character:
			revd.append( mapping_inverse[repr(char)].replace("'",''))

		return ''.join(revd)

	print given_captcha
	solution = reverse_figlet(each_character)
	c.sendline(solution)

	if ( i == 99 ):
		print c.recv()
	
# c.interactive()
c.close()
