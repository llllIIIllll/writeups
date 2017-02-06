#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-10-28 00:05:27
# @Last Modified by:   john
# @Last Modified time: 2016-10-28 00:24:36


from PIL import Image
from glob import glob

im = Image.open('2d77fbd5eda9ed661a7834d8273815722fb97ccc.png')

data = im.load()

start_x = 17
start_y = 24

delta_x = 24 - start_x
delta_y = 44 - start_y

# 80 columns
# 12 rows

first  = 'ABCDEFGHI'
second = 'JKLMNOPQR'
third  = 'STUVWXYZ'


for x in range( 80 ):
	holes_at = []
	for y in range( 12 ):
		point = data[ start_x + delta_x * x, start_y + delta_y * y  ]
		# print point
		if point == (255, 255, 255, 255):
			holes_at += [ y ]

	# print "column", x, holes_at
	letters_to_use = ""

	for number in holes_at:

		if ( number == 0 ): letters_to_use = first
		if ( number == 1 ): letters_to_use = second
		if ( number == 2 ): letters_to_use = third

		if ( number > 3 ):
			actual_number = number - 2
			index = actual_number - 1

			if letters_to_use != "":
				print letters_to_use[index],

im.show()
im.close()