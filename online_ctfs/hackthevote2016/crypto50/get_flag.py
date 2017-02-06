#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-11-05 12:15:29
# @Last Modified by:   john
# @Last Modified time: 2016-11-05 12:33:58


handle = open("kek.txt")
contents = handle.read()
handle.close()

import binascii

things = contents.split()
# print things

new = []
for thing in things:
    
    if "KEK" in thing:
        character = "0"
    else:
        character = "1"

    number = thing.count('!')
    new.append( character * number )

end = "".join(new)

print "".join([ chr(int(end[i:i+8],2)) for i in range(0,len(end), 8) ])