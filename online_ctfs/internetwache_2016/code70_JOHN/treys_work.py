from string import printable


mapping = {}
out = []
for char in printable:
	q = bin((ord(char)^(2<<4))).lstrip("0b")
	q = "0" * ((2<<2)-len(q)) + q
	out.append(q)
	b = ''.join(out)
	pr = []
	s = ''
	for x in range(0,len(b),2):
		c = chr(int(b[x:x+2],2)+51)
		pr.append(c)
	s = '.'.join(pr)
	#print "'" + s + "' : '" +char + "',"
	mapping[s] = char
	
	out = []

print mapping