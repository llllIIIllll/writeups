#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# @Author: caleb
# @Date:   2016-05-27 21:49:28
# @Last Modified by:   caleb
# @Last Modified time: 2016-05-27 22:55:16
import requests
from bs4 import BeautifulSoup
import hashlib
​
html = requests.get('http://cipherfont.p.tjctf.org/').text
soup = BeautifulSoup(html, 'html.parser')
shifted = soup.find(class_='protected').string.strip()
actual = ''.join([ chr( ord(c) - 15 ) if (ord(c)-15) >= 33 else chr(ord(c)+79) for c in shifted ])
# I wrote "tjcftf" the first time and didn't notice D:<
flag = 'tjctf{' + hashlib.md5(actual).hexdigest() + '}'
print 'Flag is %s' % flag
