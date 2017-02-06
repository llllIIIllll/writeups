#!/usr/bin/env python

import re
from itertools import *

conditions = [
	'buffer[38]==buffer[30]==buffer[6]==buffer[8]==buffer[0]',
	'buffer[19]==buffer[20]==buffer[38]==buffer[42]==buffer[1]',
	'buffer[36]==buffer[35]==buffer[19]==buffer[3]==buffer[44]==buffer[2]',
	'buffer[41]==buffer[10]==buffer[10]==buffer[17]==buffer[19]==buffer[3]',
	'buffer[33]==buffer[21]==buffer[4]',
	'buffer[39]==buffer[8]==buffer[4]==buffer[4]==buffer[5]',
	'buffer[25]==buffer[10]==buffer[39]==buffer[14]==buffer[6]',
	'buffer[1]==buffer[15]==buffer[32]==buffer[7]',
	'buffer[5]==buffer[5]==buffer[8]==buffer[8]',
	'buffer[7]==buffer[24]==buffer[9]',
	'buffer[17]==buffer[49]==buffer[4]==buffer[32]==buffer[10]',
	'buffer[38]==buffer[42]==buffer[17]==buffer[8]==buffer[11]',
	'buffer[8]==buffer[14]==buffer[12]',
	'buffer[20]==buffer[45]==buffer[13]',
	'buffer[25]==buffer[48]==buffer[20]==buffer[9]==buffer[14]',
	'buffer[18]==buffer[31]==buffer[15]',
	'buffer[46]==buffer[24]==buffer[16]',
	'buffer[2]==buffer[13]==buffer[47]==buffer[50]==buffer[14]==buffer[17]',
	'buffer[44]==buffer[36]==buffer[3]==buffer[0]==buffer[18]',
	'buffer[30]==buffer[41]==buffer[25]==buffer[28]==buffer[19]',
	'buffer[44]==buffer[25]==buffer[20]',
	'buffer[28]==buffer[22]==buffer[21]==buffer[39]==buffer[25]==buffer[21]',
	'buffer[44]==buffer[4]==buffer[12]==buffer[31]==buffer[30]==buffer[22]',
	'buffer[32]==buffer[14]==buffer[39]==buffer[23]',
	'buffer[21]==buffer[18]==buffer[0]==buffer[21]==buffer[24]',
	'buffer[12]==buffer[17]==buffer[4]==buffer[11]==buffer[18]==buffer[25]',
	'buffer[32]==buffer[46]==buffer[20]==buffer[49]==buffer[26]',
	'buffer[39]==buffer[25]==buffer[36]==buffer[48]==buffer[27]',
	'buffer[15]==buffer[14]==buffer[28]',
	'buffer[35]==buffer[42]==buffer[1]==buffer[29]',
	'buffer[8]==buffer[31]==buffer[30]==buffer[24]==buffer[30]',
	'buffer[18]==buffer[29]==buffer[15]==buffer[42]==buffer[31]',
	'buffer[15]==buffer[5]==buffer[44]==buffer[14]==buffer[32]',
	'buffer[45]==buffer[15]==buffer[20]==buffer[32]==buffer[33]',
	'buffer[33]==buffer[3]==buffer[20]==buffer[10]==buffer[34]',
	'buffer[6]==buffer[43]==buffer[44]==buffer[44]==buffer[1]==buffer[35]',
	'buffer[25]==buffer[31]==buffer[28]==buffer[49]==buffer[36]',
	'buffer[31]==buffer[34]==buffer[34]==buffer[11]==buffer[37]',
	'buffer[36]==buffer[27]==buffer[5]==buffer[42]==buffer[38]',
	'buffer[8]==buffer[37]==buffer[39]',
	'buffer[28]==buffer[7]==buffer[44]==buffer[10]==buffer[40]',
	'buffer[26]==buffer[17]==buffer[7]==buffer[20]==buffer[41]',
	'buffer[1]==buffer[50]==buffer[28]==buffer[42]',
	'buffer[33]==buffer[46]==buffer[15]==buffer[43]',
	'buffer[42]==buffer[24]==buffer[16]==buffer[21]==buffer[45]==buffer[44]',
	'buffer[22]==buffer[40]==buffer[45]',
	'buffer[12]==buffer[46]==buffer[7]==buffer[35]==buffer[46]',
	'buffer[26]==buffer[15]==buffer[39]==buffer[12]==buffer[47]',
	'buffer[15]==buffer[8]==buffer[11]==buffer[48]',
	'buffer[37]==buffer[27]==buffer[49]',
	'buffer[8]==buffer[13]==buffer[17]==buffer[15]==buffer[24]==buffer[50]',
]

indices = []
buffer = '0'*51

count = 0
p = product(range(10), repeat=51)
for i in p:
	count += 1	
	buffer = ''.join( [ str(x) for x in i ] )
	
	works = True
	for condition in conditions:
		indices+= [ int(b) for b in re.findall('\[(\d*)\]', condition)]

		code_condition = eval(condition)
		if (not condition):
			# print " count %d failed condition %s" % (count, condition )
			works = False
			break
		else:
			# print " count %d passed condition %s" % (count, condition )
			pass
	if works:
		print "SUCCESS WITH KEY %s" % buffer
	else:
		print "%d count FAILED" % count
print "ALL DONE"