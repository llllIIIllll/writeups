#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-02-21 21:56:42
# @Last Modified by:   john
# @Last Modified time: 2016-02-21 22:22:51

from PIL import Image

filename = 'landscape.png'
image = Image.open( filename )

data = image.load()
size = width, height = image.size

image.close()


y = 48
characters = []
for x in range(0, 546, 7 ):
	characters.append( data[x,y][0] )

message = ''.join( [ chr(x) for x in characters ] )

array =  eval(''.join(message.split(' ')[3:-1]))

print ''.join( [ chr(x) for x in array ] )