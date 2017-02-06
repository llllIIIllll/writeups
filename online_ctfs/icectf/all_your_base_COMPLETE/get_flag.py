#!/usr/bin/env python

h = open("flag.txt")
flag = h.read()
h.close()

print  "".join( [ chr(int(a,2)) for a in flag.split()] )