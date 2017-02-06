#!/usr/bin/env python

import requests
from colorama import * 

url = 'http://52.91.163.151/'


for i in range( 1000 ):

	for l in range(19):
		submission = str(i).zfill(l)

		r = requests.post( url, {'cc':submission} ).text
		lines = r.split('\n')

		final = '\n'.join(lines[23:-11])
		print submission, final