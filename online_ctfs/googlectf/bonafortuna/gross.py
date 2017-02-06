#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-04-29 14:43:39
# @Last Modified by:   john
# @Last Modified time: 2016-04-29 15:03:31


from scapy.all import *

p = rdpcap('thing.pcap')

count = 0
for packet in p:
	# if ( packet[TCP].dport == 1194 ):
		
	# 		# print packet[Raw].load
	# 	packet.show()
	# 	count  += 1
	try:
		print packet[Raw].load
	except:
		pass

print count