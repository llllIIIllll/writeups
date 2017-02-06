#!/usr/bin/env python

from scapy.all import *
from pprint import pprint
import binascii


pcaps = rdpcap('f101.pcap')

for p in pcaps[ICMP]:
	print binascii.hexlify (p[Raw].load)
	raw_input()
