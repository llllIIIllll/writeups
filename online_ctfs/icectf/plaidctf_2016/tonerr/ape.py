#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-04-16 22:00:17
# @Last Modified by:   john
# @Last Modified time: 2016-04-16 23:18:41

from Crypto.Hash import SHA256

from pwnlib import tubes 
from colorama import *

import binascii

host = 'tonnerre.pwning.xxx'
port = 8561

def tostr(A):
  return hex(A)[2:].strip('L')

def H(P):
  h = SHA256.new()
  h.update(P)
  return h.hexdigest()


# # Euclidian Algorithm

# # Start with two numbers

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

init(autoreset=True)
# input2 =
# pc =
# v = 'ebedd14b5bf7d5fd88eebb057af43803b6f88e42f7ce2a4445fdbbe69a9ad7e7a76b7df4a4e79cefd61ea0c4f426c0261acf5becb5f79cdf916d684667b6b0940b4ac2f885590648fbf2d107707acb38382a95bea9a89fb943a5c1ef6e6d064084f8225eb323f668e2c3174ab7b1dbfce831507b33e413b56a41528b1c850e59'
v = 165674960298677315369642561867883496091624769292792204074150337092614964752287803122621876963359715780971900093578962850132496591192295131510624917204670192364009271723089444839548606533268832368676268405764377988005323809734321470184299186127132537376393324213965008025487569799622831466701444653263068925529
N = 168875487862812718103814022843977235420637243601057780595044400667893046269140421123766817420546087076238158376401194506102667350322281734359552897112157094231977097740554793824701009850244904160300597684567190792283984299743604213533036681794114720417437224509607536413793425411636411563321303444740798477587L
# v = 0xd14058efb3f49bd1f1c68de447393855e004103d432fa61849f0e5262d0d9e8663c0dfcb877d40ea6de6b78efd064bdd02f6555a90d92a8a5c76b28b9a785fd861348af8a7014f4497a5de5d0d703a24ff9ec9b5c1ff8051e3825a0fc8a433296d31cf0bd5d21b09c8cd7e658f2272744b4d2fb63d4bccff8f921932a2e81813

s = tubes.remote.remote(host, port)
print s.recv()
s.sendline('get_flag')

input2 = egcd(v, N)[1] + N
print input2
exit()
print Fore.YELLOW + "Euclid:", input2

s.sendline(str(input2))
zero = s.recv()
print Fore.YELLOW + "Salt:", zero
residue = s.recv()
print Fore.YELLOW + "Residue:", residue
print Fore.MAGENTA + tostr(1)
one_hash = H(tostr(1))


session_secret = ( input2 * v ) % N
session_secret = pow(session_secret, )


print Fore.YELLOW + "Hash of 1:", one_hash
print Fore.RED + "residue " + residue
print Fore.RED + "one_hash " + one_hash
concat = residue + one_hash
# input3 = H(tostr(residue) + tostr(one_hash))
input3 = H(concat)
# input3 = str(int(str(input3),16))
print Fore.CYAN + "Input 3:", input3
s.sendline(str(input3))
print s.recv()





