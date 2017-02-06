#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-02-20 14:10:30
# @Last Modified by:   John Hammond
# @Last Modified time: 2016-02-21 15:52:46

import base64 as b

handle = open('data.txt')
content = handle.readlines()
handle.close()

for data in content:
	print "\n\n",b.b64decode(data)
	raw_input()
