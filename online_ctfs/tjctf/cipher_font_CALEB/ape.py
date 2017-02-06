#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-27 21:33:21
# @Last Modified by:   john
# @Last Modified time: 2016-05-27 21:41:39

import hashlib

h = open('data.txt')

data = h.read().strip()

print data
m = hashlib.md5()
m.update(data)
print ""
print "tjctf{" + m.hexdigest() + "}"

h.close()