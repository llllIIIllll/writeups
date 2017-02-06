#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-03-13 18:01:28
# @Last Modified by:   john
# @Last Modified time: 2016-03-13 18:14:35

from PIL import Image


def main():

    filename = "extracted_top"

    image = Image.open(filename)
    size = width, height = image.size

    data = image.load()

    all_data = []

    for x in range(width):
        for y in range(height):
            pixel = data[x, y]
            if pixel[0] == 255:
                all_data.append('1')
            if pixel[0] == 0:
                all_data.append('0')

    nonsense = []
    for i in range(0, len(all_data), 8):
        segment = all_data[i:i+8]
        nonsense.append(chr(eval('0b'+''.join(segment))))


    print ''.join(nonsense)

    # image.show()

    image.close()

if (__name__ == "__main__"):
    main()
