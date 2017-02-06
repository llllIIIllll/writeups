#!/usr/bin/env python

import readline

from colorama import *

start_position = 0x6042c0

conditions = [
	'int(sting[0x6042c0-start_position] == 0x0',
	'int(sting[0x6042c1-start_position] == 0x8',
	'int(sting[0x6042c1-start_position] != 0x4',
	'int(sting[0x6042c2-start_position] != 0x4',
	'int(sting[0x6042c3-start_position] == 0x4',
	'int(sting[0x6042c4-start_position] == 0x2',
	'int(sting[0x6042c4-start_position] != 0x8',
	'int(sting[0x6042c5-start_position] != 0x4',
	'int(sting[0x6042c6-start_position] != 0x4',
	'int(sting[0x6042c6-start_position] == 0x8',
	'int(sting[0x6042c7-start_position] != 0x4',
	'int(sting[0x6042c8-start_position] == 0x1',
	'int(sting[0x6042c8-start_position] == 0x2',
	'int(sting[0x6042c9-start_position] != 0x1',
	'int(sting[0x6042ca-start_position] != 0x2',
	'int(sting[0x6042cb-start_position] == 0x1',
	'int(sting[0x6042cb-start_position] != 0x2',
	'int(sting[0x6042cc-start_position] == 0x8',
	'int(sting[0x6042cc-start_position] != 0x4',
	'int(sting[0x6042cd-start_position] != 0x4',
	'int(sting[0x6042ce-start_position] == 0x2',
	'int(sting[0x6042ce-start_position] == 0x4',
	'int(sting[0x6042cf-start_position] == 0x8',
	'int(sting[0x6042d0-start_position] != 0x4',
	'int(sting[0x6042d1-start_position] == 0x1',
	'int(sting[0x6042d2-start_position] != 0x4',
	'int(sting[0x6042d3-start_position] != 0x2',
	'int(sting[0x6042d3-start_position] != 0x4',
	'int(sting[0x6042d4-start_position] == 0x1',
	'int(sting[0x6042d5-start_position] != 0x4',
	'int(sting[0x6042d5-start_position] == 0x2',
	'int(sting[0x6042d6-start_position] != 0x4',
	'int(sting[0x6042d8-start_position] == 0x4',
	'int(sting[0x6042d9-start_position] == 0x2',
	'int(sting[0x6042db-start_position] == 0x8',
	'int(sting[0x6042db-start_position] != 0x4',
	'int(sting[0x6042dc-start_position] != 0x2',
	'int(sting[0x6042dd-start_position] != 0x4',
	'int(sting[0x6042de-start_position] != 0x4',
	'int(sting[0x6042de-start_position] != 0x2',
	'int(sting[0x6042e0-start_position] == 0x2',
	'int(sting[0x6042e0-start_position] != 0x1',
	'int(sting[0x6042e1-start_position] != 0x4',
	'int(sting[0x6042e2-start_position] != 0x4',
	'int(sting[0x6042e3-start_position] == 0x1',
	'int(sting[0x6042e3-start_position] != 0x2',
	'int(sting[0x6042e4-start_position] == 0x4',
	'int(sting[0x6042e4-start_position] != 0x8',
	'int(sting[0x6042e5-start_position] != 0x4',
	'int(sting[0x6042e6-start_position] != 0x4',
	'int(sting[0x6042e7-start_position] != 0x2',
	'int(sting[0x6042e7-start_position] == 0x8',
	'int(sting[0x6042e8-start_position] == 0x2',
	'int(sting[0x6042e8-start_position] == 0x4',
	'int(sting[0x6042e9-start_position] == 0x2',
	'int(sting[0x6042ea-start_position] == 0x1',
	'int(sting[0x6042eb-start_position] != 0x4',
	'int(sting[0x6042eb-start_position] == 0x8',
	'int(sting[0x6042ec-start_position] == 0x8',
	'int(sting[0x6042ec-start_position] != 0x4',
	'int(sting[0x6042ed-start_position] == 0x1',
	'int(sting[0x6042ee-start_position] != 0x4',
	'int(sting[0x6042ef-start_position] != 0x4',
	'int(sting[0x6042f0-start_position] == 0x1',
	'int(sting[0x6042f1-start_position] == 0x1',
	'int(sting[0x6042f2-start_position] == 0x4',
]

conditions = [
	'int(string[0x6042c0 - start_position],16) != 8 ',
	'int(string[0x6042c1+ 0x1 - start_position],16) == 8 ',
	'int(string[0x6042c1+ 0x1 - start_position],16) != 4 ',
	'int(string[0x6042c2+ 0x1 - start_position],16) != 4 ',
	'int(string[0x6042c2 - start_position],16) != 8 ',
	'int(string[0x6042c3 - start_position],16) == 8 ',
	'int(string[0x6042c3+ 0x1 - start_position],16) == 0x4',
	'int(string[0x6042c4+ 0x1 - start_position],16) == 0x2',
	'int(string[0x6042c4+ 0x1 - start_position],16) != 0x8',
	'int(string[0x6042c5+ 0x1 - start_position],16) != 0x4',
	'int(string[0x6042c5 - start_position],16) != 0x8',
	'int(string[0x6042c6+ 0x1 - start_position],16) != 0x4',
	'int(string[0x6042c6+ 0x1 - start_position],16) == 0x8',
	'int(string[0x6042c7 - start_position],16) == 0x4',
	'int(string[0x6042c7+ 0x1 - start_position],16) != 0x4',
	'int(string[0x6042c8+ 0x1 - start_position],16) == 0x1',
	'int(string[0x6042c8+ 0x1 - start_position],16) == 0x2',
	'int(string[0x6042c9+ 0x1 - start_position],16) != 0x1',
	'int(string[0x6042c9 - start_position],16) == 0x4',
	'int(string[0x6042ca+ 0x1 - start_position],16) != 0x2',
	'int(string[0x6042ca - start_position],16) != 0x8',
	'int(string[0x6042cb+ 0x1 - start_position],16) == 0x1',
	'int(string[0x6042cb+ 0x1 - start_position],16) != 0x2',
	'int(string[0x6042cc+ 0x1 - start_position],16) == 0x8',
	'int(string[0x6042cc+ 0x1 - start_position],16) != 0x4',
	'int(string[0x6042cd - start_position],16) != 0x8',
	'int(string[0x6042cd+ 0x1 - start_position],16) != 0x4',
	'int(string[0x6042ce+ 0x1 - start_position],16) == 0x2',
	'int(string[0x6042ce+ 0x1 - start_position],16) == 0x4',
	'int(string[0x6042cf - start_position],16) != 0x8',
	'int(string[0x6042cf+ 0x1 - start_position],16) == 0x8',
	'int(string[0x6042d0 - start_position],16) == 0x4',
	'int(string[0x6042d0+ 0x1 - start_position],16) != 0x4',
	'int(string[0x6042d1+ 0x1 - start_position],16) == 0x1',
	'int(string[0x6042d1 - start_position],16) != 0x8',
	'int(string[0x6042d2 - start_position],16) != 0x8',
	'int(string[0x6042d2+ 0x1 - start_position],16) != 0x4',
	'int(string[0x6042d3+ 0x1 - start_position],16) != 0x2',
	'int(string[0x6042d3+ 0x1 - start_position],16) != 0x4',
	'int(string[0x6042d4 - start_position],16) != 0x8',
	'int(string[0x6042d4+ 0x1 - start_position],16) == 0x1',
	'int(string[0x6042d5+ 0x1 - start_position],16) != 0x4',
	'int(string[0x6042d5+ 0x1 - start_position],16) == 0x2',
	'int(string[0x6042d6 - start_position],16) == 0x4',
	'int(string[0x6042d6+ 0x1 - start_position],16) != 0x4',
	'int(string[0x6042d7 - start_position],16) != 0x8',
	'int(string[0x6042d7 - start_position],16) == 0x4',
	'int(string[0x6042d8+ 0x1 - start_position],16) == 0x4',
	'int(string[0x6042d8 - start_position],16) == 0x4',
	'int(string[0x6042d9 - start_position],16) != 0x8',
	'int(string[0x6042d9+ 0x1 - start_position],16) == 0x2',
	'int(string[0x6042da - start_position],16) == 0x4',
	'int(string[0x6042da - start_position],16) != 0x8',
	'int(string[0x6042db+ 0x1 - start_position],16) == 0x8',
	'int(string[0x6042db+ 0x1 - start_position],16) != 0x4',
	'int(string[0x6042dc - start_position],16) == 0x4',
	'int(string[0x6042dc+ 0x1 - start_position],16) != 0x2',
	'int(string[0x6042dd - start_position],16) == 0x4',
	'int(string[0x6042dd+ 0x1 - start_position],16) != 0x4',
	'int(string[0x6042de+ 0x1 - start_position],16) != 0x4',
	'int(string[0x6042de+ 0x1 - start_position],16) != 0x2',
	'int(string[0x6042df - start_position],16) != 0x8',
	'int(string[0x6042df - start_position],16) == 0x4',
	'int(string[0x6042e0+ 0x1 - start_position],16) == 0x2',
	'int(string[0x6042e0+ 0x1 - start_position],16) != 0x1',
	'int(string[0x6042e1+ 0x1 - start_position],16) != 0x4',
	'int(string[0x6042e1 - start_position],16) != 0x8',
	'int(string[0x6042e2 - start_position],16) != 0x8',
	'int(string[0x6042e2+ 0x1 - start_position],16) != 0x4',
	'int(string[0x6042e3+ 0x1 - start_position],16) == 0x1',
	'int(string[0x6042e3+ 0x1 - start_position],16) != 0x2',
	'int(string[0x6042e4+ 0x1 - start_position],16) == 0x4',
	'int(string[0x6042e4+ 0x1 - start_position],16) != 0x8',
	'int(string[0x6042e5+ 0x1 - start_position],16) != 0x4',
	'int(string[0x6042e5 - start_position],16) == 0x4',
	'int(string[0x6042e6+ 0x1 - start_position],16) != 0x4',
	'int(string[0x6042e6 - start_position],16) == 0x4',
	'int(string[0x6042e7+ 0x1 - start_position],16) != 0x2',
	'int(string[0x6042e7+ 0x1 - start_position],16) == 0x8',
	'int(string[0x6042e8+ 0x1 - start_position],16) == 0x2',
	'int(string[0x6042e8+ 0x1 - start_position],16) == 0x4',
	'int(string[0x6042e9 - start_position],16) != 0x8',
	'int(string[0x6042e9+ 0x1 - start_position],16) == 0x2',
	'int(string[0x6042ea+ 0x1 - start_position],16) == 0x1',
	'int(string[0x6042ea - start_position],16) == 0x4',
	'int(string[0x6042eb+ 0x1 - start_position],16) != 0x4',
	'int(string[0x6042eb+ 0x1 - start_position],16) == 0x8',
	'int(string[0x6042ec+ 0x1 - start_position],16) == 0x8',
	'int(string[0x6042ec+ 0x1 - start_position],16) != 0x4',
	'int(string[0x6042ed+ 0x1 - start_position],16) == 0x1',
	'int(string[0x6042ed - start_position],16) != 0x8',
	'int(string[0x6042ee+ 0x1 - start_position],16) != 0x4',
	'int(string[0x6042ee - start_position],16) != 0x8',
	'int(string[0x6042ef+ 0x1 - start_position],16) != 0x4',
	'int(string[0x6042ef - start_position],16) == 0x4',
	'int(string[0x6042f0 - start_position],16) != 0x8',
	'int(string[0x6042f0+ 0x1 - start_position],16) == 0x1',
	'int(string[0x6042f1 - start_position],16) == 0x4',
	'int(string[0x6042f1+ 0x1 - start_position],16) == 0x1',
	'int(string[0x6042f2+ 0x1 - start_position],16) == 0x4',
	'int(string[0x6042f2 - start_position],16) == 0x8',
]

string =""
correct = False
while ( not correct ):
	for i in range(len(conditions)):
		# prin i
		# prin conditions[i]

		condition = conditions[i]
		try:
			code_condition = eval(condition)
		except IndexError:

			print Fore.YELLOW + "There is not yet a character this far in. Enter the new string:"
			string  = raw_input('new string:')
			readline.add_history(string)
			correct = False
			break
		if not( code_condition ) :
			print Fore.RED + "Condition #%d is not met:" % i
			print Fore.BLUE + condition
			print eval(str( condition.split('[')[1].split(']')[0]))

			string = raw_input('new string:')
			readline.add_history(string)
			correct = False
			break
		else:
			correct = True


print Fore.GREEN + "All conditions are seemingly met, with string: "
print Fore.GREEN + Style.BRIGHT + string


