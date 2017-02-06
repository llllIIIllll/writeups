#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-12-29 14:33:37
# @Last Modified by:   john
# @Last Modified time: 2016-12-29 14:44:01

import requests as r
import urllib

url = 'http://78.46.224.78:5001'

def send( string ):

	response = r.post(url + '/pay/flag', data = { "ccnr" : string })
	print response.text
	if ( "invalid" in response.text ):
		return "credit card number invalid"
	elif ( "Credit card limit exceeded!" in response.text ):
		return "CREDIT CARD LIMIT EXCEEDED"
	else:
		return response.text

sending = "000000000000000000000000000000000000000000000000000000000000000"
sending = urllib.unquote(sending)
print sending
print send( sending )
print sending