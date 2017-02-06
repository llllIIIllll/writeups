#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-02-20 14:10:30
# @Last Modified by:   john
# @Last Modified time: 2016-02-20 16:53:34

import base64 as b

handle = open('data.txt')
content = handle.readlines()
handle.close()

i = 0
for data in content:
	i += 1
	print "\n" + str(i) + "\n" + b.b64decode(data)
	raw_input()


'''
Flagis:IW{QR-C0DES-RUL3}
'''