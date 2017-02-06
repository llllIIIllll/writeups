#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-07-17 08:53:19
# @Last Modified by:   john
# @Last Modified time: 2016-07-17 09:10:56

import requests
import re
import base64


flag_format = r'ABCTF{.*}'


url = 'http://yrmyzscnvh.abctf.xyz/web2/'

# You can see in the source of the webpage (in a obvious comment again)
# a blantatly given base64 code (equals signs give it away)
password = 'c3RvcHRoYXRqcw=='

password = base64.b64decode(password)
# stopthatjs

response = requests.post( url, data = { "password": password } )

print re.findall( flag_format, response.text )[0]
