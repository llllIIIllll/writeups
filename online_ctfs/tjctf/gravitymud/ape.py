#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-28 00:28:18
# @Last Modified by:   john
# @Last Modified time: 2016-05-28 00:55:35


from pwn import *

context.log_level = 'critical'

host = 'p.tjctf.org'
port = 8006

c = tubes.remote.remote(host, port)

# commands = ["north", "west", "examine journal2"]
# b33n_m1$sing_t3h_

# commands = ["north", "west", "examine journal2", "east", "east", "east", "examine paintedeye", "down", "examine book"]
# SOMETHING IS HIDDEN IN THE TREE IN THE CLEARING

# commands = ["north", "west", "examine journal2", "east", "east", "east", "examine paintedeye", "down", "examine book", "up", "west", "west", "south", "examine tree"]
# fl4g_but_

# read paper?
# commands = ["north", "west", "examine journal2", "east", "east", "east", "examine paintedeye", "down", "examine book", "up", "west", "west", "south", "examine tree", "south", "examine paper"]


# under the rug
# tjctf{y0u_m1ght_h@v3_
# commands = ["north", "west", "examine journal2", "east", "east", "east", "examine paintedeye", "down", "examine book", "up", "west", "west", "south", "examine tree", "south", "south", "examine rug"]

# TRUST NOONE
# commands = ["north", "west", "examine journal2", "east", "east", "east", "examine paintedeye", "down", "examine book", "up", "west", "west", "south", "examine tree", "south", "south", "examine rug", "up", "east", "examine wall"]

# YOUR_A1M_IS_G3TT1NG_B3TT3R}
# ["north", "west", "examine journal2", "east", "east", "east", "examine paintedeye", "down", "examine book", "up", "west", "west", "south", "examine tree", "south", "south", "examine rug", "up", "west", "examine uvlight", "east", "down", "north", "examine paper"]


# total flag?
# tjctf{y0u_m1ght_h@v3_b33n_m1$sing_t3h_fl4g_but_YOUR_A1M_IS_G3TT1NG_B3TT3R}

commands = ["north", "west", "examine journal2", "east", "east", "east", "examine paintedeye", "down", "examine book", "up", "west", "west", "south", "examine tree", "south", "south", "examine rug", "up", "west", "examine uvlight", "east", "down", "north", "examine paper"]
commands.append("")
for command in commands:
	print c.recvuntil("turns remain")
	prompt = '\n'.join(c.recvuntil("> ").split('\n')[:-1])
	# # print prompt
	# items = [ item.replace('.','') for item in prompt.split('\n')[-2].split('Here you see ')[-1].split(',')]
	# # print items
	# exits = [ item.replace('.','').strip() for item in prompt.split('\n')[-1].split('Exits: ')[-1].split(',')]
	# print exits

	print prompt

	c.sendline(command)
c.close()