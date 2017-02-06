#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-03-19 17:37:57
# @Last Modified by:   john
# @Last Modified time: 2016-03-19 20:23:52

import string
import collections


def rotate(rotate_string, number_to_rotate_by):

    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(number_to_rotate_by)
    lower.rotate(number_to_rotate_by)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return rotate_string.translate(string.maketrans(string.ascii_uppercase, upper)).translate(string.maketrans(string.ascii_lowercase, lower))


challenge_string = 'Apcyrcb Zw Zpgyl Qrpysaf'


def brute_force_cipher():
    for i in range(len(string.ascii_uppercase)):
        print i, rotate(challenge_string, i)


def get_answer():
    return rotate(challenge_string, 12)


def get_flag():
    return get_answer().split()[-1]

print brute_force_cipher()
