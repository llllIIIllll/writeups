#!/usr/bin/env python

'''
# http://www.splitbrain.org/services/ook

starting from 0.0.0.0, print the following IPs. 
7277067th IP Address
7234562th IP Address
7302657th IP Address
91238th IP Address
746508th IP Address
7211531th IP Address
7300098th IP Address
7211788th IP Address
723558th IP Address
91248th IP Address
7237378th IP Address
723557th IP Address
7234562th IP Address
723567th IP Address
749067th IP Address

Hint: Anything specific about all the IPs?
'''


import ipaddress
#'''

ip_addresses = [
	7277067,
	7234562,
	7302657,
	91238,
	746508,
	7211531,
	7300098,
	7211788,
	723558,
	91248,
	7237378,
	723557,
	7234562,
	723567,
	749067,
]

binary = []
for ip in ip_addresses:
	address =  str(ipaddress.IPv4Address( ip - 1 ))
	b = address 

	b = b.replace('.','')
	# b = b.replace('2','')
	binary.append( b )
	
	# But these have the wrong binary value... some have a 2 at the end!

print ''.join([ chr(int(x,2) ) for x in binary ])
#'''
'''
corrected_binary_values = [
'01111011',
'01101010',
'01111101',
'01100110',
'01110100',
'01101011',
'01111010',
'01110000',
'01110110',
'01101000',
'01110000',
'01110101',
'01101010',
'01110111',
'01111011',
]

print ''.join( [chr(int(bin,2)) for bin in corrected_binary_values ] )
#'''