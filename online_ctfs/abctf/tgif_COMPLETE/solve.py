#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-07-17 08:24:49
# @Last Modified by:   john
# @Last Modified time: 2016-07-17 08:44:04

import datetime

handle = open("dates.txt")


friday_count = 0
for line in handle.readlines():

	date = line.split()

	# We want one year later...
	new_year = str(int(date[-1])+1)

	new_date = " ".join( date[:-1] + [ new_year ])
	#print new_date

	try:
		date = datetime.datetime.strptime( new_date, "%B %d, %Y" )
	

		if date.weekday() == 4: friday_count += 1

	except:
		# We ran into an illogical leap year date. Skipping...
		pass

#	print 
	
print friday_count
# 194. This is the flag and solution you should submit.