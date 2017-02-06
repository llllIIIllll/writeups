#!/usr/bin/env python

from scapy.all import *
import base64 as b

pcap = rdpcap('../downloads/giyh-capture.pcap')
udp_packets = pcap[UDP]

for packet in udp_packets:

	if DNS in packet[0]:
		carved_data = None
		try:
			carved_data = b.b64decode(packet[0][1].an.rdata)
		except:
			pass

		if ( carved_data ): 
			print carved_data