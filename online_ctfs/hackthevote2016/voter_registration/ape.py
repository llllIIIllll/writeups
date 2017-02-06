#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-11-05 09:23:31
# @Last Modified by:   john
# @Last Modified time: 2016-11-05 15:21:11

import requests
import urllib
import random
from string import digits, ascii_uppercase

url = 'http://kansas.pwn.republican/secure/default.php?s=3&txtfirst_name=winn&txtmiddle_name=winn&txtLast_name=winn&txtname_suffix=win&txtdob=00%2F00%2F0000&txtdl_nmbr=K76987693&txtRetypeDL=K76987693&btnContinue2=Continue'

session = requests.Session()

fields = {
	"s": "3",
	"txtfirst_name": "winners",
	"txtmiddle_name": "winners",
	"txtLast_name": "winners", 
	"txtname_suffix" : "win", 
	"txtdob": "00/00/0000",
	"txtdl_nmbr": "K76987693", 
	"txtRetypeDL": "K76987693",
	"btnContinue2" : "Continue"
}

url = 'http://kansas.pwn.republican/secure/default.php'

# &rbCitizen=Y&rbAge=Y&rbResident=Y&rbFelony=rbFelony1&btnContinue=Continue

first_fields = {
	"s" : "2",
	"rbCitizen": "Y",
	"rbAge": "Y",
	"rbResident": "Y",
	"rbFelony": "rbFelony1",
	"btnContinue": "Continue"
}

def cook_get( url, fields ):

	return url + "?" + "&".join([ key + "=" + urllib.quote(value) for key, value in fields.iteritems() ])


def get_new_license():

	drivers_license = list(random.choice(ascii_uppercase) + digits[:8])
	random.shuffle( drivers_license )
	drivers_license = "".join(drivers_license )
	return drivers_license



def send_attempt( first_name, last_name, date ):

	global fields

	dl = get_new_license()


	fields["txtfirst_name"] = "john"
	fields["txtmiddle_name"] = "00/00/0000"
	fields["txtLast_name"] = "Hammond"
	fields["txtname_suffix"] = "suffix"
	fields["txtdob"] = "00/00/0000"
	fields["btnContinue2"] = "Continue"

	fields["txtdl_nmbr"] = dl + ""
	fields["txtRetypeDL"] = fields["txtdl_nmbr"] 

	request = cook_get( url, fields )

	result = session.get(request).text

	return result


print send_attempt('cdr', 'seals', '00/00/4444"')