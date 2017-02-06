#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-03-19 19:03:12
# @Last Modified by:   john
# @Last Modified time: 2016-03-19 19:14:49

import morsecode

string = '&& &&& !&! !!! ! !&& !& !!! &!&! &&& &&& !&!!'
string += ' '
morse_string = string.replace('&', '-').replace('!', '.')

print morsecode.decodeMorse(morse_string)
