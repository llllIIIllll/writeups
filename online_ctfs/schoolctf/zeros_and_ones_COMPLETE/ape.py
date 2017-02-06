#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-11-06 01:24:20
# @Last Modified by:   john
# @Last Modified time: 2016-11-06 01:27:19

handle = open("original.txt")
contents = handle.read()
handle.close()

wants = "ZERON"

found = []
for character in contents:
	if character in wants:
		found.append(character)

print hex(int("".join(found).replace("ZERO","0").replace("ONE","1"),2))[2:-1].decode('hex')