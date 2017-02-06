import PIL
from PIL import Image
from PIL import ImageOps
from pprint import pprint
import base64 as b
from time import strftime


half = 3

pic = Image.open("A.png")
# rainbow = Image.open("rainbow.jpg")
rainbow = Image.open("other_rainbow.png")
# rainbow = Image.open("circle_rainbow.png")
# rainbow = Image.open("square_rainbow.png")



width, height = pic.size

new_data = []

def add_images( image1, image2 ):

	new_image = image1.copy()

	image1 = image1.load()
	image2 = image2.load()
	final = new_image.load()
	
	for y in xrange( height ):
		for x in xrange( width ):

			first_pixel = image1[x, y]
			second_pixel = image2[x, y]

			pixel_data = []
			for i in range(3):
				try:
					pixel =  ( first_pixel[i] + second_pixel[i] ) % 255

				except:
					pixel = 0
				
				pixel_data.append(pixel)

			pixel_data = tuple(pixel_data)
			#print pixel_data
			final[x,y] = pixel_data

	return new_image


final_picture = pic
while (True):

	final_picture =  add_images( rainbow, final_picture.copy() )
	# final_picture = final_picture.resize( [int(half * s) for s in final_picture.size] )

	final_picture.show( )
	raw_input()