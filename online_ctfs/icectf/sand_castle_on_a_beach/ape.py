#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-08-19 17:29:04
# @Last Modified by:   john
# @Last Modified time: 2016-08-20 16:42:23

from PIL import Image
from pprint import pprint

''' We found this very mysterious image, it doesn't look complete and
there seems to be something hidden on it... does this mean anything to
you? This flag is not in the standard flag format.
The flag contains digits and no special characters, convert the
message to lowercase and then add IceCTF{message} to it. 10331c4d '''

filename = 'sandcastle.png'

numbers = '58-7-9.210-13-2.67-3-16.85-17-15.305-18-4.83-12-18.75-8-15.47-4-2.83-20-11.208-6-6.85-11-6.75-7-3.106-9-14'

separations = numbers.split('.')

img = Image.open(filename)
pixels = img.load()


for section in separations:

	parts = section.split('-')
	x, y = [ int(a) for a in parts[:-1] ]
	pprint(parts)
	# stuff =  pixels[x, y]
	

img.close()