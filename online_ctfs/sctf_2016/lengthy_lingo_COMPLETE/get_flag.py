#!/usr/bin/env python

handle = open('encrypted.dat')
contents = handle.read()
handle.close()

# The number of digits in each number corresponds to the ASCII code for one character.
# We use this to build our flag.

# I initially determined this by factoring all the numbers with factordb.com

final_stuff = []
contents = contents.split(', ')
for number in contents:
	final_stuff.append( chr(len(number)) )


# Looks like we missed the ending brace; I'll just tack it on...
print ''.join(final_stuff)+'}'
