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

			string = raw_input('new string:')
			readline.add_history(string)
			correct = False
			break
		else:
			correct = True


print Fore.GREEN + "All conditions are seemingly met, with string: "
print Fore.GREEN + Style.BRIGHT + string


