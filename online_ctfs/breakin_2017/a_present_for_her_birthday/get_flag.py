#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2017-01-26 12:04:27
# @Last Modified by:   john
# @Last Modified time: 2017-01-26 12:07:21


import requests
import md5

# The cookie that you see `birthday_invite` is the MD5 hash of the word 'false'.
# So what happens if we just change that to `true?`

m = md5.md5()

m.update('true')
true = m.hexdigest()

url = 'https://felicity.iiit.ac.in/contest/extra/birthday/'

r = requests.get(url, cookies ={ "birthday_invite": true })

print r.text