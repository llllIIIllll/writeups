#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-02-20 18:26:05
# @Last Modified by:   john
# @Last Modified time: 2016-02-21 12:40:05

import requests
from colorama import *

from binascii import unhexlify

hosts = [

	'496e2074686520656e642c206974277320616c6c2061626f757420666c61.2015.ctf.internetwache.org',
	'67732e0a5768657468657220796f752077696e206f72206c6f736520646f.2015.ctf.internetwache.org',
	'65736e2774206d61747465722e0a7b4f66632c2077696e6e696e67206973.2015.ctf.internetwache.org',
	'20636f6f6c65720a44696420796f752066696e64206f7468657220666c61.2015.ctf.internetwache.org',
	'67733f0a4e6f626f62792066696e6473206f7468657220666c616773210a.2015.ctf.internetwache.org',
	'53757065726d616e206973206d79206865726f2e0a5f4845524f2121215f.2015.ctf.internetwache.org',
	'0a48656c70206d65206d7920667269656e642c2049276d206c6f73742069.2015.ctf.internetwache.org',
	'6e206d79206f776e206d696e642e0a416c776179732c20616c776179732c.2015.ctf.internetwache.org',
	'e206d79206f776e206d696e642e0a416c776179732c20616c776179732c.2015.ctf.internetwache.org',
	'20666f72206576657220616c6f6e652e0a437279696e6720756e74696c20.2015.ctf.internetwache.org',
	'49276d206479696e672e0a4b696e6773206e65766572206469652e0a536f.2015.ctf.internetwache.org',
	'20646f20492e0a7d210a.2015.ctf.internetwache.org',
]

# Turns out they are all just hex encoded strings!

text = []
for host in hosts:
	try:
		g = host.split('.')[0]
		text.append(unhexlify(g))
	except:
		pass

# Put all the text together...
text =  ''.join([ x for x in text])

# And the flag is found in the first letter of each line. 
flag = ''.join( [ str(line)[0] for line in text.split('\n')[:-1] ] )
print flag