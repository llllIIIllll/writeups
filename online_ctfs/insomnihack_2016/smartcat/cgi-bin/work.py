#!/usr/bin/env python

import cgi, subprocess, os

print "X-Powered-By: %s" % headers[os.getpid()%4] 
print "Content-type: text/html"

headers = ["mod_cassette_is_back/0.1","format-me-i-im-famous","dirbuster.will.not.help.you","solve_me_already"]

print "X-Powered-By: %s" % headers[os.getpid()%4] 
print "Content-type: text/html"
print

print """
<html>

<head><title>Can I haz Smart Cat ???</title></head>

<body>

  <h3> Smart Cat debugging interface </h3>
"""

blacklist = " $;&|({`\t"
results = ""
form = cgi.FieldStorage()
dest = form.getvalue("dest", "127.0.0.1")
for badchar in blacklist:
	if badchar in dest:
		results = "Bad character %s in dest" % badchar
		break

if "%n" in dest:
	results = "Segmentation fault"

if not results:
	try:
		results = subprocess.check_output("ping -c 1 "+dest, shell=True)
	except:
		results = "Error running " + "ping -c 1 "+dest


print """

  <form method="post" action="index.cgi">
    <p>Ping destination: <input type="text" name="dest"/></p>
  </form>

  <p>Ping results:</p><br/>
  <pre>%s</pre>

  <img src="../img/cat.jpg"/>

</body>

</html>
""" % cgi.escape(results)
