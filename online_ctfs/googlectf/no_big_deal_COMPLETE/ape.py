#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-04-30 01:07:27
# @Last Modified by:   john
# @Last Modified time: 2016-04-30 01:08:35


from scapy.all import *

p = rdpcap('no-big-deal.pcap');
for packet in p:
	p.show();