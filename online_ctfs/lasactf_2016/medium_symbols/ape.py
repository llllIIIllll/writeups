#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-03-19 20:07:59
# @Last Modified by:   john
# @Last Modified time: 2016-03-19 20:09:48

handle = open('beep.txt')
content = handle.read()
handle.close()

length = len(content)
print length
bytes = []
for i in range(0, length, 2):
    byte = content[i:i+2]
    bytes.append(byte)

print ''.join([chr(int(byte)) for byte in bytes])