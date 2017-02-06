#!/usr/bin/env python

import numpy
from pprint import pprint

life = numpy.zeros((10, 10), dtype=numpy.byte)

game = [
	'0000000000',
	'0000000000',
	'0001111100',
	'0000000100',
	'0000001000',
	'0000010000',
	'0000100000',
	'0001000000',
	'0000000000',
	'0000000000',
]

final_game = []

for y in range(len(life)):
	for x in range( len(life[y]) ):
		life[x][y] = game[x][y]

print life

def play_life(a):
    xmax, ymax = a.shape
    b = a.copy() # copy grid & Rule 2
    for x in range(xmax):
        for y in range(ymax):
            n = numpy.sum(a[max(x - 1, 0):min(x + 2, xmax), max(y - 1, 0):min(y + 2, ymax)]) - a[x, y]
            if a[x, y]:
                if n < 2 or n > 3:
                    b[x, y] = 0 # Rule 1 and 3
            elif n == 3:
                b[x, y] = 1 # Rule 4
    return(b)

for i in range( 7 ):
	# print "ITERATION NUMBER", i+1
	life = play_life( life )
	# print(life)

string = []
for line in life:
	whole_line = "".join( [ str(item) for item in line  ] )
	string.append( whole_line )

print ','.join(string)
