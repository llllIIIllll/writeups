#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2017-01-26 12:10:13
# @Last Modified by:   john
# @Last Modified time: 2017-01-26 13:24:18

from PIL import Image
import sys

# there is a comment in the Question.jpg file

comment = "^[[A^[[D^[[C^[[A^[[C^[[C^[[B^[[D^[[A^[[A^[[A^[[A^[[D^[[D^[[D^[[C^[[B^[[A^[[B^[[B^[[A^[[C^[[C^[[D^[[C^[[B^[[C^[[D^[[A^[[B^[[A^[[D^[[B^[[C^[[C^[[A^[[B^[[C^[[A^[[D^[[B^[[C^[[C^[[C^[[D^[[D^[[C^[[C^[[B^[[A^[[A^[[C^[[C^[[C^[[D^[[B^[[B^[[C^[[A^[[B^[[A^[[C^[[C^[[C^[[A^[[D^[[D^[[D^[[B^[[A^[[A^[[A^[[D^[[C^[[C^[[C^[[C^[[D^[[A^[[D^[[A^[[D^[[D^[[B^[[C^[[C^[[D^[[B^[[B^[[A^[[A^[[B^[[A^[[A^[[C^[[B^[[A^[[D^[[A^[[D^[[B^[[D^[[D^[[C^[[D^[[D^[[B^[[A^[[D^[[D^[[C^[[A^[[D^[[A^[[C^[[A^[[A^[[B^[[B^[[C^[[A^[[B^[[A^[[D^[[A^[[B^[[C^[[A^[[B^[[D^[[D^[[B^[[C^[[D^[[B^[[A^[[C^[[B^[[B^[[B^[[B^[[D^[[C^[[C^[[C^[[C^[[D^[[B^[[C^[[B^[[B^[[D^[[B^[[A^[[D^[[C^[[A^[[B^[[D^[[D^[[A^[[B^[[D^[[C^[[B^[[B^[[A^[[D^[[A^[[D^[[B^[[C^[[B^[[A^[[D^[[D^[[D^[[B^[[D^[[B^[[C^[[D^[[C^[[D^[[B^[[A^[[A^[[A^[[D^[[C^[[A^[[A^[[C^[[B^[[C^[[C^[[B^[[C^[[C^[[B^[[B^[[A^[[D^[[B^[[C^[[B^[[D^[[D^[[A^[[C^[[D^[[B^[[B^[[B^[[B^[[D^[[D^[[B^[[C^[[B^[[C^[[C^[[B^[[C^[[C^[[C^[[A^[[C^[[C^[[A^[[C^[[C^[[B^[[D^[[C^[[D^[[D^[[D^[[D^[[D^[[B^[[D^[[C^[[C^[[B^[[C^[[D^[[B^[[D^[[C^[[C^[[C^[[C^[[B^[[D^[[C^[[D^[[B^[[D^[[A^[[C^[[C^[[B^[[C^[[D^[[C^[[A^[[A^[[B^[[D^[[B^[[C^[[D^[[A^[[D^[[B^[[D^[[A^[[B^[[C^[[D^[[B^[[C^[[B^[[A^[[B^[[A^[[B^[[B^[[C^[[B^[[D^[[C^[[A^[[C^[[B^[[C^[[B^[[D^[[D^[[B^[[C^[[D^[[D^[[A^[[B^[[A^[[D^[[D^[[D^[[D^[[C^[[A^[[A^[[B^[[B^[[D^[[A^[[C^[[A^[[A^[[B^[[B^[[C^[[A^[[D^[[A^[[B^[[C^[[D^[[D^[[A^[[D^[[D^[[C^[[A^[[A^[[D^[[C^[[C^[[A^[[C^[[C^[[B^[[D^[[A^[[A^[[C^[[B^[[B^[[C^[[A^[[A^[[C^[[A^[[B^[[C^[[B^[[C^[[C^[[A^[[C^[[C^[[C^[[B^[[C^[[C^[[C^[[C^[[B^[[C^[[A^[[D^[[C^[[A^[[A^[[B^[[C^[[D^[[C^[[C^[[C^[[D^[[A^[[B^[[D^[[B^[[C^[[C^[[B^[[B^[[A^[[D^[[A^[[D^[[B^[[A^[[C^[[A^[[A^[[A^[[A^[[B^[[C^[[A^[[C^[[C^[[D^[[B^[[D^[[D^[[C^[[C^[[B^[[C^[[B^[[C^[[B^[[C^[[B^[[B^[[D^[[A^[[B^[[A^[[C^[[A^[[D^[[D^[[B^[[C^[[C^[[C^[[D^[[B^[[A^[[B^[[A^[[A^[[C^[[A^[[D^[[B^[[A^[[C^[[A^[[D^[[A^[[D^[[D^[[D^[[C^[[D^[[A^[[A^[[C^[[B^[[B^[[D^[[C^[[C^[[A^[[B^[[B^[[C^[[D^[[C^[[B^[[D^[[B^[[D^[[C^[[C^[[D^[[D^[[B^[[D^[[B^[[C^[[A^[[A^[[C^[[B^[[B^[[A^[[A^[[A^[[B^[[C^[[D^[[A^[[C^[[A^[[C^[[D^[[D^[[C^[[D^[[A^[[D^[[D^[[D^[[A^[[C^[[D^[[D^[[A^[[B^[[D^[[D^[[B^[[A^[[B^[[C^[[D^[[C^[[C^[[A^[[B^[[C^[[B^[[B^[[B^[[B^[[C^[[A^[[D^[[A^[[D^[[B^[[B^[[D^[[D^[[D^[[B^[[D^[[A^[[C^[[D^[[C^[[C^[[D^[[C^[[A^[[C^[[B^[[D^[[B^[[B^[[C^[[A^[[B^[[A^[[C^[[D^[[D^[[D^[[C^[[C^[[D^[[D^[[A^[[B^[[D^[[D^[[D^[[C^[[C^[[B^[[D^[[D^[[B^[[B^[[A^[[B^[[B^[[C^[[A^[[A^[[A^[[C^[[D^[[D^[[A^[[D^[[A^[[B^[[C^[[C^[[C^[[B^[[D^[[D^[[D^[[D^[[C^[[D^[[D^[[B^[[C^[[D^[[B^[[B^[[C^[[D^[[B^[[C^[[C^[[D^[[B^[[D^[[C^[[A^[[C^[[C^[[D^[[B^[[D^[[B^[[D^[[A^[[B^[[B^[[B^[[A^[[D^[[C^[[C^[[C^[[C^[[C^[[A^[[D^[[B^[[C^[[A^[[B^[[D^[[B^[[D^[[B^[[B^[[B^[[D^[[C^[[B^[[B^[[B^[[C^[[B^[[A^[[D^[[C^[[C^[[A^[[D^[[A^[[B^[[A^[[D^[[D^[[B^[[A^[[D^[[B^[[C^[[B^[[A^[[D^[[B^[[C^[[D^[[C^[[A^[[B^[[D^[[D^[[D^[[C^[[B^[[B^[[A^[[D^[[D^[[B^[[D^[[D^[[C^[[C^[[D^[[D^[[A^[[B^[[C^[[D^[[D^[[C^[[C^[[D^[[A^[[C^[[A^[[C^[[A^[[D^[[B^[[C^[[A^[[C^[[B^[[C^[[B^[[A^[[D^[[B^[[D^[[A^[[D^[[C^[[A^[[B^[[B^[[D^[[C^[[A^[[C^[[A^[[D^[[D^[[B^[[C^[[D^[[C^[[B^[[C^[[C^[[C^[[B^[[A^[[D^[[B^[[A^[[A^[[D^[[A^[[D^[[D^[[C^[[B^[[D^[[D^[[C^[[D^[[B^[[B^[[A^[[A^[[C^[[A^[[A^[[A^[[A^[[D^[[C^[[D^[[A^[[B^[[C^[[A^[[A^[[C^[[D^[[C^[[D^[[C^[[D^[[A^[[C^[[B^[[C^[[D^[[C^[[B^[[A^[[D^[[B^[[B^[[B^[[B^[[B^[[C^[[A^[[A^[[A^[[A^[[D^[[C^[[C^[[A^[[C^[[B^[[D^[[C^[[D^[[A^[[A^[[B^[[D^[[C^[[A^[[A^[[C^[[B^[[D^[[B^[[C^[[D^[[D^[[C^[[B^[[C^[[A^[[D^[[A^[[D^[[A^[[B^[[D^[[D^[[B^[[A^[[D^[[D^[[A^[[D^[[D^[[D^[[A^[[C^[[A^[[B^[[D^[[D^[[B^[[B^[[B^[[D^[[D^[[A^[[A^[[C^[[B^[[B^[[B^[[C^[[C^[[A^[[C^[[B^[[B^[[D^[[B^[[B^[[C^[[B^[[D^[[D^[[A^[[A^[[B^[[D^[[C^[[C^[[C^[[C^[[B^[[A^[[C^[[C^[[C^[[D^[[D^[[D^[[B^[[C^[[D^[[B^[[D^[[D^[[B^[[B^[[D^[[C^[[C^[[D^[[D^[[A^[[A^[[D^[[C^[[C^[[C^[[B^[[C^[[A^[[D^[[D^[[C^[[A^[[A^[[D^[[C^[[C^[[D^[[D^[[A^[[B^[[B^[[D^[[D^[[A^[[B^[[B^[[D^[[C^[[B^[[D^[[A^[[B^[[C^[[C^[[B^[[D^[[C^[[C^[[C^[[C^[[C^[[C^[[D^[[A^[[B^[[D^[[A^[[A^[[B^[[D^[[C^[[B^[[D^[[D^[[A^[[C^[[C^[[B^[[A^[[A^[[C^[[C^[[B^[[D^[[A^[[A^[[B^[[A^[[A^[[D^[[C^[[C^[[C^[[B^[[A^[[B^[[D^[[D^[[C^[[D^[[B^[[A^[[B^[[B^[[A^[[A^[[A^[[B^[[D^[[D^[[D^[[B^[[C^[[D^[[C^[[A^[[D^[[B^[[A^[[A^[[D^[[A^[[D"

comment = comment.replace('^','').replace('[[','')

# print comment


# A is up
# B is down
# C is right
# D is left

x, y = 4846 + 61, 6900 + 61
size = 122

image = Image.open('Question.jpg')

data = image.load()

string = []
for new_place in comment:

	# new_place = 'A'
	if ( new_place == 'A' ): y -= size
	if ( new_place == 'B' ): y += size
	if ( new_place == 'C' ): x += size
	if ( new_place == 'D' ): x -= size
	
	try:
		string.append(chr(data[x, y][0]))
		# print data[x,y]
	except:
		pass

# print len(string)
sys.stdout.write( "".join(string) )

image.close()