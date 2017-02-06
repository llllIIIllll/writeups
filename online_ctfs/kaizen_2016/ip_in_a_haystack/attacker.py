#!/usr/bin/env python

import ipaddress

handle = open('iplist.txt')
contents = handle.readlines()
handle.close()

counter = 0
for line in contents:

	cidr, address = line.split()
	if ipaddress.ip_address(unicode(address)) in ipaddress.ip_network(unicode(cidr)):
		counter += 1

print counter