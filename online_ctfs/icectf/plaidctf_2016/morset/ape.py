#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-04-16 11:36:17
# @Last Modified by:   john
# @Last Modified time: 2016-04-16 12:31:44

from colorama import *
from morsecode import *
from pwnlib import tubes

host = 'morset.pwning.xxx'
port = 11821

init(autoreset=True)

s = tubes.remote.remote(host, port)

while True:

    try:
        received = s.recvuntil('\n')
        print Fore.YELLOW + "received " + received
        decoded = decodeMorse(received)
        print Fore.YELLOW + Style.BRIGHT + "decoded " + decoded + Style.NORMAL

        print "> " + Fore.MAGENTA,
        send = raw_input()
        encoded = encodeToMorse(send)
        print "sending: " + Fore.BLUE + encoded
        s.sendline(encoded)
    except:
        s = tubes.remote.remote(host, port)

s.close()