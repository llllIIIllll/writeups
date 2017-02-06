#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-07-17 08:16:18
# @Last Modified by:   john
# @Last Modified time: 2016-07-17 08:20:24

import requests, re



flag_format = r'ABCTF{.*}'


url = 'http://yrmyzscnvh.abctf.xyz/web1/'

# You can find this in the source of the webpage in a comment --
# blatantly obvious hint
password = '7xfsnj65gsklsjsdkj'

response = requests.post(url, data = { 'password': password }) 

print re.findall(flag_format, response.text)[0]

# Flag is then fount to be...
# ABCTF{insp3ct3d_dat_3l3m3nt}