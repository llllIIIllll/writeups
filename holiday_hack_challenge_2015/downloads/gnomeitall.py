#!/usr/bin/env python
# Copyright (c) 2105 Josh Dosis
import base64
from scapy.all import *     # This script requires Scapy

# Read the capture file into a list of packets
packets=rdpcap("giyh-capture.pcap")

# Open the output file to save the extracted content from the pcap
fp=open("outfile","wb")

for packet in packets:

   # Make sure this is a DNS packet, with the rdata record where the content is stored
   if (DNS in packet and hasattr(packet[DNS], 'an') and hasattr(packet[DNS].an, 'rdata')):

       # Make sure it's from the Gnome, not the server
       if packet.sport != 53: continue

       # Decode the base64 data
       decode=base64.b64decode(packet[DNSRR].rdata[1:])

       # Strip off the leading "FILE:" line in the decoded data
       if decode[0:5] == "FILE:":           
           fp.write(decode[5:])

fp.close()
