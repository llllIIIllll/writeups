#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-03-19 21:19:26
# @Last Modified by:   john
# @Last Modified time: 2016-03-19 21:26:19

from PIL import Image
from subprocess import check_output, PIPE

white = (255, 255, 255)
black = (0, 0, 0)

image1 = Image.open('QR1.png')
image2 = Image.open('QR2.png')
data1 = image1.load()
data2 = image2.load()
size = width, height = image1.size


qr = Image.new('RGB', size, white)
new_data = qr.load()
save_filename = 'found_qr.png'

for y in range(height):
    for x in range(width):
        if data1[x, y] == data2[x, y]:
            # new_data[x, y] = white
            continue
        else:
            new_data[x, y] = black

qr.save(save_filename)
print check_output(['zbarimg', save_filename], stderr=PIPE).split()[-1]

image1.close()
image2.close()
qr.close()