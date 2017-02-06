#!/usr/bin/env python

import requests
from colorama import *






# WE SOLVED TTHIS CHALLENGE BUT IT WAS CALEB'S SCRIPT THAT WORKED


init( autoreset = True )

session = requests.Session()

headers = { 'User-Agent': '"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0"' }

url = 'https://felicity.iiit.ac.in/contest/breakin/challenges/seq/'


def hit( item ):

	page = session.get(url + str(item), headers = headers)
	response = page.text

	if '40' in response:
		print Style.BRIGHT + Fore.RED + 'response: ' +  response, '\t',
		return
	else:
		print Fore.GREEN + 'response: ' +  response, '\t',

	print  Fore.CYAN + 'outcome: ' + str(item), '\t',


def loop():



	counter = 0
	for item in order:

		print  Fore.YELLOW + 'exponent: ' + str(counter), '\t',
		
		hit( item )

		counter += 1
		print ''

# for i in range( 1, 15 ):
power = 0
while ( True ):
	

	loop()
	hit( 1329227995784915872903807060280344576**i )