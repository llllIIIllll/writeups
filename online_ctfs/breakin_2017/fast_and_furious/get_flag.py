#!/usr/bin/env python


import requests
import re

url = 'https://felicity.iiit.ac.in/contest/extra/fastandfurious/'

print "Sending answers... (this challenge takes some time...)"
s = requests.Session()

def scrape_and_send( text ):

	challenge = re.findall('\((.*)\)', text)[0]

	answer = str(eval(challenge))

	r = s.post(url, data={"ques_ans": answer})

	if ( 'flag' in r.text ):
		print r.text
		exit()
	scrape_and_send(r.text)

r = s.get(url)
scrape_and_send(r.text)


# the_flag_is_6ffb242e3f65a2b51c36745b1cd591d1
# Flag is: 6ffb242e3f65a2b51c36745b1cd591d1
# 