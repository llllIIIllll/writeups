#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-11-06 00:48:35
# @Last Modified by:   John Hammond
# @Last Modified time: 2016-11-06 19:05:50

from PIL import Image

image = Image.open("warp_speed.jpg")

row_height = 8
number_rows = 32
side_size = 500

image_total_width = 1000

for i in range(number_rows):

	region = image.crop( ( 	0, row_height*i, 
							image_total_width, row_height*(i+1) ) )

	image.paste(region, ( -(row_height*i), row_height*i, 
							image_total_width - ( row_height*i ), row_height*(i+1) ))

image2 = Image.new( 'RGBA', (side_size,side_size) )

first_half = True

i = 0
Q = 0
while ( i < number_rows * 2 ):

	if first_half:
		region = image.crop( ( 0, row_height*i, side_size, row_height*(i+1) ) )
	else:
		region = image.crop( ( side_size, row_height*i, image_total_width, row_height*(i+1) ) )

		i += 1

	image2.paste( region, ((0, row_height*Q, side_size, row_height*(Q+1))) )

	Q += 1

	# Alternate sides
	first_half = not first_half

image2.show()
image2.save("winner.jpg")