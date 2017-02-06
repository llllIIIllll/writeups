#!/usr/bin/env python

# list of capitals 
# https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India
# nick names
# https://www.facebook.com/studyiq/posts/1068346043194980
# https://en.wikipedia.org/wiki/List_of_city_nicknames_in_India

import pwn

conn = pwn.remote( '52.91.163.151', '10101' )

answers= [
	'English', # Final destination of river Krishna
]

for answer in answers:
	print answer
	print conn.recv()
	conn.sendline( answer.lower() )
	
print conn.recvall()
