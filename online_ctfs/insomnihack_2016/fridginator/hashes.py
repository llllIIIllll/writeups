import passlib.hash

to_hash = ''

for element in dir(passlib.hash):
	try:
		string = 'passlib.hash.' + element + '.encrypt("'+ to_hash +'")'
		#print(string)
		hashed =  eval(string).split("$")[-1]

		if len( hashed ) == 32:
			print string
			print(hashed)

		if ( 'aMLNcR9UqhCIg' in hashed ):
			print "FOUND A MATCH FOR 'a'"
			raw_input()

		if ( '67d4b8f7' in hashes ):
			print "FOUND A MATCH FOR ''"
			raw_input()

	except:
		pass