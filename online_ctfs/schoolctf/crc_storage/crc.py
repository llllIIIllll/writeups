
from pprint import pprint

cache = {}

polynom = [0,1,2,4,5,7,8,10,11,12,16,22,23,26]

def crc32(s):
	pol = 0
	for i in xrange(len(polynom)):
		pol |= 1 << (31 - polynom[i])
	
	
#	print "pol =>", hex(pol)
	global cache
	if len(cache) == 0:
		for i in xrange(256):
			xor_byte = i
			for j in xrange(8):
				if (xor_byte & 1) == 1:
					xor_byte = pol ^ (xor_byte >> 1)
				else:
					xor_byte = xor_byte >> 1
		
			cache[i] = xor_byte
	
#	pprint(map(hex, cache.values()))

	sig = 0xffffffff
	s_bytes = map(ord, list(s))
	
	for c in s_bytes:
		sig = cache[(sig ^ c) & 0xff] ^ (sig >> 8)
	
	return sig ^ 0xffffffff
