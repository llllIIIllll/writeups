#!/usr/bin/env python

import zlib, base64, itertools, operator

class AttrDict(dict):
    def __init__(self, d):
        if not isinstance(d, dict):
            d = {a:getattr(d,a) for a in dir(d)}

        super(AttrDict, self).__init__(d)
        self.__dict__ = self


R = ('eJw1i0sKwzAMRHuULmXwpRTbYIM/QlZoEubwdVoyi4H3mHm9UccnKXaR1bVMQ2PB0Ihp'
         'iqsIuFbMfUMY3bj0iZYsjxiWXxdNktjWmPU+hrwmqG2AJWLrAWoZx3khklH3QkqVGg1/'
         'OOe80bbUjYFOR0zztn++Hv7lCwJAPlc=')

A = zlib.decompress(base64.b64decode(R)).decode().split('|')
D = dict(itertools.chain(*(zip(A[i+15], operator.attrgetter(*A[3*i+3:3*i+6])(x))
		 for i,x in enumerate((AttrDict(__builtins__), AttrDict(__builtins__), operator, itertools)))))

# print base64.b64decode(R)
# print A[20]

# print
# print D

# print 
text = 'not 0'
print not eval(A[20], D, dict(zip(A[19], A[:3]), s=text))

print "executing", A[20]
# print "globals", D

functions = {}
executing = A[20]

for item in D:
	try:
		print D[item].__name__
		functions[item] = D[item].__name__
	except:
		continue
local = dict(zip(A[19], A[:3]), s="WHAT YOU CONTROL")
print "locals", dict(zip(A[19], A[:3]), s="WHAT YOU CONTROL")
for item in local:
	try:
		print local[item]
		functions[item] = local[item]
	except:
		continue

new_string = []
for character in executing:
	if character in functions:
		new_string.append(functions[character])
	else:
		new_string.append(character)

print ''.join(new_string)
print functions['s']