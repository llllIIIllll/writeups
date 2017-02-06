#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-10-27 13:56:30
# @Last Modified by:   john
# @Last Modified time: 2016-10-31 17:17:56


import requests
import re
import json
from credit_card_luhn_algorithm import *


len_visa = 5
len_mastercard = 8
len_american_express = 7

def strip(string):
	return re.findall('<strong>(.*?)<',string)[0]

# url = 'http://86dc35f7013f13cdb5a4e845a3d74937f2700c7b.ctf.site:20000/api.php'
url = 'http://86dc35f7013f13cdb5a4e845a3d74937f2700c7b.ctf.site:20000/'

r = requests.get(url)

print r.text
# print strip(r.text)