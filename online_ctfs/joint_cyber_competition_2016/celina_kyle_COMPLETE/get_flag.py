#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-14 09:31:33
# @Last Modified by:   john
# @Last Modified time: 2016-05-14 11:39:44

import itertools
import requests
import re
from colorama import *

init(autoreset=True)

url = 'http://104.196.9.105:9092/login'

s = requests.Session()

def attempt(use):
	r = s.post(url, data={"username":"celinakyle","password":use})
	match = r.text.split('<div class="row">')[1]
	return match


print re.findall('Flag=(.*?)<',attempt('PROhibIT'))[0]