import PIL
from PIL import Image
from PIL import ImageOps
from pprint import pprint
import base64 as b

half = 3

pic = Image.open("eighthCircleOfHell.png")

# pic = pic.resize( [int(half * s) for s in pic.size] )

width, height = pic.size

new_data = []

pic_data = pic.load()


pixels = []
previous_pixel = -1
count = 1
for y in xrange( height ):
	for x in xrange( width ):

		pic_pixel = pic_data[x, y]
		if ( previous_pixel == pic_pixel ):
			count += 1
		else:
			if ( count <= 7 ):
				pixels.append( count )
				count = 1

		previous_pixel = pic_pixel


print pixels
			#pic_data[x,y] = pixel_data
			
	#final.putdata( new_data )