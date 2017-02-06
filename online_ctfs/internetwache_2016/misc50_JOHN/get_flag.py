#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-02-20 12:18:16
# @Last Modified by:   john
# @Last Modified time: 2016-02-20 12:23:20

import base64

# I got these values out by some quick regex replacing in Sublime Text 
values = '126 062 126 163 142 103 102 153 142 062 065 154 111 121 157 113 122 155 170 150 132 172 157 147 123 126 144 067 124 152 102 146 115 107 065 154 130 062 116 150 142 154 071 172 144 104 102 167 130 063 153 167 144 130 060 113 012'

# Just make into an array for easy processing...
values_list = values.split()

# Consider the values as octets, and just convert them to decimal & ascii...
characters = ''.join( [ chr(int(x,8)) for x in values_list ] )

# print characters
# Looks like it is a base64 string! Let's decode it...

print base64.b64decode( characters )