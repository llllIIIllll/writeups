import PIL
from PIL import Image
from PIL import ImageOps
from pprint import pprint
import base64 as b
from time import strftime
from colorama import *

init( autoreset = True )

half = 3

pic = Image.open("A.png")
# rainbow = Image.open("rainbow.jpg")
rainbow = Image.open("other_rainbow.png")
# rainbow = Image.open("circle_rainbow.png")
# rainbow = Image.open("square_rainbow.png")

width, height = pic.size
new_data = []

other = Image.new( 'RGB', (width, height) )
other_data = other.load()

def add_images( image1, image2 ):
	global other, other_data
	new_image = image1.copy()

	image1 = image1.load()
	image2 = image2.load()
	final = new_image.load()
	
	new_list = []
	

	r, g, b = image1.split()
	new_image = Image.merge('RGB', (r, g, b))


	final_sum = 0
	for y in xrange( height ):
		for x in xrange( width ):
			first_pixel = image1[x, y]
			second_pixel = image2[x, y]

			final_sum = second_pixel



	# return new_image
	# # return new_list


# while (True):
final_picture = add_images( rainbow, pic )
another = add_images(final_picture, pic)
again = add_images(another, pic)
more = add_images(again, pic)



other.save('other.png')