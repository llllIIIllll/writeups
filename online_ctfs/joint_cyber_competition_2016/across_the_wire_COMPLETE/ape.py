#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-14 23:23:29
# @Last Modified by:   john
# @Last Modified time: 2016-05-14 23:57:18


from scapy.all import *

pcap = rdpcap('small_data.pcap')

# print vars(pcap[-7])
print pcap[-7][Raw][Raw][Raw].load

# for packet in pcap:
# 	packet.show()