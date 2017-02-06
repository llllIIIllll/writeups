#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-13 19:35:45
# @Last Modified by:   john
# @Last Modified time: 2016-05-13 19:43:32

from scapy.all import *

pcap = rdpcap('smaller.pcap')

file = []
for packet in pcap:
	file.append( packet[Raw].load[5:] )

handle = open("output.gif", 'wb')
handle.write(''.join(file))
handle.close
print "done?"

# pcap.show()