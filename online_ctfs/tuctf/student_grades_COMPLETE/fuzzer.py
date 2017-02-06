#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-13 18:28:47
# @Last Modified by:   john
# @Last Modified time: 2016-05-13 18:57:47


import requests
from colorama import *
from hashlib import md5
from subprocess import *
from readline import *
url = 'http://104.199.151.39/postQuery.php'

init(autoreset=True)
s = requests.Session()
s.cookies.update({"session": '.eJwNz81qwzAQBOBXKXv2wYnci6GHFP-QwK4IyBGrW2KHxLKklBZjRyHvXp3nG4Z5wXnwY4AyzM5lMA5QCpFBeIT-CuULPi5QAqvbk-Jgeds41IeRdR2pxVWqfsW2K1A1jirekD0Kallg5IWisRSdJ7sTUu1yUo3HZHjbRYy3RWryrI1n1T2NvVtW39ZUZiJdf8rK3FPfJ5Gsm9D2C6q-SNnC-phLdZrIY5H2N6j3K8eTQ1Xnxu-_4J3B_Hf9DWefDsDjYut6mP0PvP8BqU9Olw.Chfnyg.lt4tVXIoeqaR3qY7P2WPn28SnN0'})

while (True):

	print Fore.CYAN + "Enter your query:"
	print Fore.YELLOW + Style.BRIGHT,
	entered = raw_input()
	print Style.NORMAL,
	
	m = md5()
	m.update(entered)
	hashed = m.hexdigest()

	name = entered + "+" + hashed
	print Fore.CYAN + "Would send..."
	# print Style.BRIGHT + "  " + name

	command = 'curl "'+url+'" --data "name='+name+'&submit=1"'
	p = Popen(command.strip(), shell=True, stdout = PIPE)

	# output = check_output(command.split())
	r = s.post(url, data = { "name": name, "submit": "1"})
	print Fore.GREEN, 
	# output = r.text
	output = p.stdout.readlines()
	for line in output:
		if ( "TUCTF" in line.upper() ):
			print Style.BRIGHT + Fore.GREEN + line
		else:
			print line

	print Style.NORMAL,
