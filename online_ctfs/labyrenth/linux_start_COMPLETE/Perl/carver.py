#!/usr/bin/env python

import re
import base64 as b
from pwnlib import *


inputs_file = open("inputs.txt", 'w')
handle = open("bowie.pl")

# First get everything...
all_content = handle.read()

# Start to keep track of what we need to give the program..
found_inputs = [];

# Get bac to the start of the  file
# handle.seek(0)


# These are the patterns used to hunt throughout the file
input_pattern = r'\(\$input eq (.*)\)'


# ---------------------------------------------------------------------
#
#  Get the initial inputs...
#

def check_inputs( hunting_ground ):
	
	first_inputs = re.findall( input_pattern, hunting_ground )
	for one in first_inputs:
		cleaned = eval(one.replace('.', '+'))
		found_inputs.append( cleaned )
		log.info("adding " + str(cleaned)) 

check_inputs( all_content )

# print found_inputs



# ---------------------------------------------------------------------


base64_pattern = r'eval MIME::Base64::decode\("(.*?)"\);'

hunting_ground = all_content
given = 1
while ( given ):
	given = re.findall( base64_pattern, hunting_ground )
	# print given
	try:
		hunting_ground = b.b64decode(given[0])
		check_inputs( hunting_ground )
	except:
		# We must not have found anything!
		break
	# print hunting_ground

inputs_file.write("\n".join( found_inputs ) )

inputs_file.close()
handle.close()