#!/usr/bin/env python

from string import digits
from itertools import permutations, combinations
from hashlib import md5

the_hash = "b86c94e352424273f7a525e026f54cb8"

print "hello"
for p in permutations(digits, 10):
	for l in permutations(digits, 10):
		m = md5()
		code = "".join(p + l)
		m.update(code)
		if ( m.hexdigest() == the_hash ):
			print code

			exit()