#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: John Hammond
# @Date:   2016-11-17 14:17:34
# @Last Modified by:   John Hammond
# @Last Modified time: 2016-11-21 00:34:56

from glob import glob
import datetime
import calendar

# get an array of all the files
files = glob('*.txt')

# create  a reverse lookup table for month names and their corresponding number
calendars = dict((v,k) for k,v in enumerate(calendar.month_abbr))

for file in files:

	# strip out the files from 
	weekday, day, month, year = file.replace('.txt', '').split('_')
	day = int(day)
	year = int(year)

	# get the number for the month name...
	month = calendars[month[:3]]

	# create a datetime object so we can easily find the real weekday
	date = datetime.datetime( year, month, day )
	actual_day = calendar.day_name[date.weekday()]

	'''
	after comparing the actual day with the weekday, almost all of them
	have the wrong weekday
	'''

	# the flag must be in the only one that actually have the correct weekday
	if ( actual_day == weekday ):
		print open(file).read()[:-1]  # ... this is the flag!
									  # 4eec2cd9e4bb0062d0e41c8af1bd8a0f
		exit()
