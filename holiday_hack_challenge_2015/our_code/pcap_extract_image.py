#!/usr/bin/env python

from scapy.all import *
import base64 as b

pcap = rdpcap('../downloads/giyh-capture.pcap')
udp_packets = pcap[UDP]

filename = "carved_image.jpg"

dummy = open(filename, 'w')  	# I do this just to clean out the image file
dummy.write('')				 	# just in case there already is one that exists
dummy.close()				 	# we pretty much used this when debugging, really
							 	# since we ran the script multiple times  	
handle = open( filename ,'ab')
for packet in udp_packets:

	if DNS in packet[0]:
		carved_data = None
		try:
			carved_data = b.b64decode(packet[0][1].an.rdata)
		except:
			pass

		if ( carved_data ): 
			# No need to display all the data out this time...
			#print carved_data 

			if ( carved_data.startswith('FILE:') ):
				piece_of_file =  carved_data.split('FILE:')[1]
				handle.write(piece_of_file)

handle.close()