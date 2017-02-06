#!/usr/bin/env python

import random

class SecurePrng(object):
	def __init__(self):
		self.p = 4646704883L
		self.x = random.randint(0, self.p)
		self.y = random.randint(0, self.p)

	def next(self):
		self.x = (2 * self.x + 3) % self.p
		self.y = (3 * self.y + 9) % self.p
		return (self.x ^ self.y)



num = SecurePrng()

for i in range(100000):
	print num.next()

# random_number =
# X = (2 * X + 3) % p
# X = 3520325244
# SECOND = 3520325244

# X = (2 * X + 3) % p

#	p =  4646704883L
#   random_number = ( 2 * 482230921 + 3 ) % 4646704883L
#   