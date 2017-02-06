#!/usr/bin/env python

import subprocess
import sys

import cgi

from colorama import Fore, init


init( autoreset=True )

try:
	dest = '127.0.0.1\n' + sys.argv[1]
except:
	print Fore.RED + "Supply the command!"
	exit(-1)






blacklist = " $;&|({`\t"
results = ""
for badchar in blacklist:
	if badchar in dest:
		results = "Bad character %s in dest" % badchar
		break


if not results:
	try:
		results = subprocess.check_output("ping -c 1 "+dest, shell=True)
	except Exception as e:
		print "Error running " + "ping -c 1 " + dest
		print e.message


print cgi.escape(results)