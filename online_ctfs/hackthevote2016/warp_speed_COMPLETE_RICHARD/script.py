#!/usr/bin/python

from PIL import Image

'''
The image provided by the challenge contains the key. I used Pillow, a fork of the Python Imaging Library (PIL) to reverse manipulations to the image. 

Two effects had to be undone:

1) the "roll" effect to the image that offsets each row (8 pixels high) by 8 
pixels to the left each row.


2) a "shuffled card effect". The un-"rolled" image reveals two side by side _stacks_ of strips (8pix*500pix) which need to be shuffled together in alternating order.
'''


image = Image.open("warp_speed.jpg")

image = image.convert("RGBA")



i=0

while(i < 32):

    region = image.crop((0,8*i,1000,8*(i+1)))

    image.paste(region,(-(8*i),8*i,1000-(8*i),8*(i+1)))

    i += 1



image2 = Image.new("RGBA",(500,500))



i=0

Q=0

firstHalf = True

while (i<64):

    if firstHalf:

        region = image.crop((0,8*i,500,8*(i+1)))

    else:

        region = image.crop((500,8*i,1000,8*(i+1)))

        i += 1

    image2.paste(region,((0,8*Q,500,8*(Q+1))))

    Q += 1

    firstHalf = not firstHalf



image2.show()