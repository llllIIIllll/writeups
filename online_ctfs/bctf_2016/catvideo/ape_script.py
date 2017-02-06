#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-03-19 08:13:20
# @Last Modified by:   john
# @Last Modified time: 2016-03-21 09:27:02

from PIL import Image
from glob import glob
import os
from colorama import *
from collections import deque


def check_if_directories_exist():

    # Verify directories exist
    if not os.path.exists(altered_frames_dir) or \
       not os.path.exists(original_frames_dir):
            print(Fore.RED + "Some directories do not exist?")
            exit(-1)


def get_original_frames():

    frames_wildcard = os.path.join(original_frames_dir, '*')
    original_frame_names = glob(frames_wildcard)

    for frame in original_frame_names:
        original_frames[frame] = Image.open(frame)

#--------------------------------------------------------

init(autoreset=True)

altered_frames_dir = 'altered_frames'
original_frames_dir = 'original_frames'

original_frames = {}


check_if_directories_exist()
get_original_frames()

for frame in original_frames:

    original_name = frame
    original_frame = original_frames[frame]

    altered_name = original_name.replace('original', 'altered')
    altered_frame = original_frame.copy()

    original_frame_data = original_frame.load()
    altered_frame_data = altered_frame.load()
    size = width, height = altered_frame.size

    for shift in range(0, 9):

        for y in range(height):
            for x in range(width):

                pixel = original_frame_data[x, y]
                altered_pixel = list(pixel)

                # binary_value = bin(value)[2:].zfill(8)
                # reversed_binary_value = binary_value[::-1]
                # altered_pixel = [int(bin(value)[2:].zfill(8)[::-1], 2)
                #                  for value in pixel]

                new_pixel = []
                for value in altered_pixel:
                    binary_value = bin(value)[2:].zfill(8)[::-1]
                    binary_value = deque(binary_value)
                    binary_value.rotate(shift)
                    binary_value = list(binary_value)
                    binary_value = ''.join(binary_value)
                    decimal_value = int(binary_value,2)
                    new_pixel.append(decimal_value)

                altered_pixel = new_pixel
                # print new_pixel
                # binary_value = [bin(value)[2:].zfill(8)[::-1]
                #                 for value in pixel]

                # print binary_value

                #altered_pixel.reverse()

                # print altered_pixel, pixel
                altered_frame_data[x, y] = tuple(altered_pixel)
                # altered_frame_data[x, y] = (0, 0, 0)

        print "frame", frame
        print "shift", shift
        original_frame.show()
        altered_frame.show()
        raw_input()
